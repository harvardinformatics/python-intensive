############################################################
# This script is a hook for converting Jupyter notebooks to
# Markdown files and subsequently adding metadate, alt-text
# for images, and styles for code blocks, tables, and output.
#
# Gregg Thomas, July 2025
############################################################

import sys
if sys.platform == "win32":
    import asyncio
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

import os
import re 
import base64

import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
from nbconvert.preprocessors import Preprocessor
from nbconvert import MarkdownExporter
from nbconvert.preprocessors import ClearOutputPreprocessor

############################################################
## Custom preprocessor and associated functions for 
## skipping execution of tagged cells
class SkipExecuteTaggedCellsPreprocessor(Preprocessor):
    def __init__(self, tag="no-execute", **kwargs):
        super().__init__(**kwargs)
        self.tag = tag

    def preprocess_cell(self, cell, resources, index):
        if cell.cell_type == "code" and self.tag in cell.metadata.get("tags", []):
            # Save original source to metadata
            cell.metadata["__original_source"] = cell.source
            # Replace with ' ' so it doesn't error when executed
            cell.source = " "
            cell.outputs = []
            cell.execution_count = None
        return cell, resources

def restore_skipped_cells(nb, tag="no-execute"):
    for cell in nb.cells:
        if cell.cell_type == "code" and tag in cell.metadata.get("tags", []):
            orig = cell.metadata.pop("__original_source", None)
            if orig is not None:
                cell.source = orig

############################################################        
## Custom preprocessor and associated functions for 
## handling code cells

def leadingWhitespaceToNbsp(text, tabsize=4):
    """
    Replace leading tabs with tabsize &nbsp; and leading spaces with &nbsp;, for each line.
    """
    nbsp = '&nbsp;'
    def repl(m):
        lead = m.group()
        # First replace tabs
        lead = lead.replace('\t', nbsp * tabsize)
        # Then replace spaces
        lead = lead.replace(' ', nbsp)
        return lead
    # Replace leading space/tab chars on each line
    return re.sub(r'^[ \t]+', repl, text, flags=re.MULTILINE)

def stripTrailingSpaces(text):
    return '\n'.join(line.rstrip() for line in text.splitlines())

####################

def indentBlock(block, prefix):
    lines = block.splitlines()
    return '\n'.join(prefix + line if line.strip() else prefix for line in lines)

####################

def stripANSI(text):
    ansi_escape = re.compile(r'\x1b\[[0-9;]*m')
    return ansi_escape.sub('', text)

####################

def makeOutputBlocks(outputs, indent=None):
    """
    Process a list of Jupyter cell outputs and return them as Markdown blocks.

    - If any output in the cell contains an image (PNG or SVG), 
      ALL text/plain outputs from that cell are suppressed.
      (This prevents output like <Axes: ...> above figures.)
    - Handles indented image outputs for multi-level display.
    - Formats stream and error outputs with <pre class="output-block">...</pre>.
    - Designed for nbconvert-style code cell output processing.
    """

    out_blocks = []

    # === 1. Check if there are any image outputs in the list of outputs ===
    any_images = any(
        output.output_type in {"execute_result", "display_data"} and (
            ("image/png" in output.get("data", {})) or
            ("image/svg+xml" in output.get("data", {}))
        )
        for output in outputs
    )

    # === 2. Iterate through each output ===
    for output in outputs:
        # -- Handle rich outputs (execute_result, display_data) --
        if output.output_type in {"execute_result", "display_data"}:
            data = output.get("data", {})

            # -- If 'image/png' present, emit as Markdown image and skip text/plain --
            if "image/png" in data:
                img_data = data["image/png"]
                if isinstance(img_data, list):
                    img_data = ''.join(img_data)
                img_md = f'![](data:image/png;base64,{img_data.strip()})'
                if indent:
                    img_md = indentBlock(img_md, indent)
                out_blocks.append(img_md)
                continue  # Don't emit text/plain for this output

            # -- If 'image/svg+xml' present, emit SVG directly and skip text/plain --
            if "image/svg+xml" in data:
                img_data = data["image/svg+xml"]
                if isinstance(img_data, list):
                    img_data = ''.join(img_data)
                if indent:
                    img_data = indentBlock(img_data, indent)
                out_blocks.append(img_data)
                continue  # Don't emit text/plain for this output

            # -- Only emit text/plain if no images in any output of this cell --
            if not any_images and "text/plain" in data:
                text = data["text/plain"]
                text = leadingWhitespaceToNbsp(text)
                text = stripTrailingSpaces(text)
                block = f'<pre class="output-block">{text.rstrip()}\n</pre>'
                if indent:
                    block = indentBlock(block, indent)
                out_blocks.append(block)

        # -- Handle stdout/stderr/text stream outputs --
        elif output.output_type == "stream":
            text = output.get("text", "")
            if text.strip():  # skip if only whitespace
                text = leadingWhitespaceToNbsp(text)
                text = stripTrailingSpaces(text)
                block = f'<pre class="output-block">{text.rstrip()}\n</pre>'
                if indent:
                    block = indentBlock(block, indent)
                out_blocks.append(block)

        # -- Handle exceptions (errors) --
        elif output.output_type == "error":
            text = "\n".join(output.get("traceback", []))
            text = stripANSI(text)  # remove any ANSI codes for safety
            text = leadingWhitespaceToNbsp(text)
            text = stripTrailingSpaces(text)
            if text.strip():
                block = f'<pre class="output-block">{text.rstrip()}\n</pre>'
                if indent:
                    block = indentBlock(block, indent)
                out_blocks.append(block)

    return out_blocks

####################
class CodeCellPreprocessor(Preprocessor):
    """
    For any code cell, wraps all its plain text outputs (stream, error, text/plain)
    in <pre class="output-block">...</pre>. For solution-tagged cells,
    combines code and outputs in an admonition. Also scrubs #@title lines from code cells.
    """
    def preprocess(self, nb, resources):
        new_cells = []
        for cell in nb.cells:

            if cell.cell_type == "code":
                lines = cell.source.splitlines()

                solution_cell = False
                if (
                    "solution" in cell.metadata.get("tags", []) or
                    lines[0].strip().startswith("#@title Solution")
                ):
                    solution_cell = True

                cell.source = "\n".join(line for line in lines if not line.strip().startswith('#@title Solution'))

                if solution_cell:
                    # --- SOLUTION CELL ---
                    code_block = "```python\n" + cell.source.rstrip() + "\n```"
                    output_blocks = makeOutputBlocks(cell.get("outputs", []), indent="    ")
                    markdown = (
                        '??? success "Solution"\n'
                        f"    {code_block.replace(chr(10), chr(10)+'    ')}"
                    )
                    if output_blocks:
                        markdown += "\n\n" + "\n\n".join(output_blocks)
                    new_cells.append(nbformat.v4.new_markdown_cell(markdown))

                else:
                    # --- NON-SOLUTION CODE CELL ---
                    new_cells.append(cell)
                    if cell.get("outputs"):
                        for out_block in makeOutputBlocks(cell.outputs):
                            new_cells.append(nbformat.v4.new_markdown_cell(out_block))
                    cell.outputs = []

            else:
                new_cells.append(cell)
        nb.cells = new_cells
        return nb, resources

############################################################
## Other functions

def styleLink(match):
    """
    This function styles links in markdown files.
    It checks if the link is from a specific domain (excluded_domain) or if it is
    a relative link. If so, it does not style the link.
    Otherwise, it styles the link with an external link icon and opens in a new tab.
    """

    excluded_domain = "https://informatics.fas.harvard.edu/"
    link_text = match.group(1)
    link_url = match.group(2).strip()
    if (link_url.startswith(excluded_domain)
        or not (link_url.startswith("http://") or link_url.startswith("https://"))):
        # Exclude domain and all relative links
        return match.group(0)
    return f"[{link_text} :octicons-link-external-24:]({link_url})" + '{:target="_blank"}'

############################################################
## Templates

# Template for markdown frontmatter
front_matter = """---
title: "{title}"
description: "{description}"
authors:
    {authors}
---

"""

# CSS styles for output tables, output blocks, and code blocks to be added
# to the end of the file
style = """
---

<!-- --------------------------------- -->
<!-- Page speciifc CSS -->

<style>

  /* Output table styles */

  div:has(> .dataframe) {
    width: 100%;
    overflow-x: auto;
  }

  .dataframe {
    margin-left: auto;
    margin-right: auto;
    min-width: max-content;
    font-size: 12px;
    border: none;
  }

  .dataframe thead tr:last-child th {
    font-weight: bold;
    background: #fff;    
    border-bottom: 1px solid #000;
  }

  .dataframe tbody th {
    font-weight: bold;
  }

  .dataframe th,
  .dataframe td {
    border: none;
    padding: 3px 3px 3px 18px;
    text-align: right; 
    white-space: nowrap;
  }

  .dataframe thead tr th,
  .dataframe tbody tr th,
  .dataframe tbody tr td {
    border: none;
  }

  .dataframe tbody tr:nth-child(odd) {
    background: #eee;
  }
  .dataframe tbody tr:nth-child(even) {
    background: #fff;
  }
  .dataframe tbody tr:hover {
    background: #cce6ff !important;
  }

  /* Output block styles */
  
  .output-block {
    border: 1px dotted #999999;
    margin-bottom: 0 !important;
    padding: 10px;
    overflow-x: auto;
    overflow-y: auto;
    word-break: break-all;
    word-wrap: break-word;
    white-space: pre-wrap;
    font-size: 13px;
    margin-left: 40px;
    color: rgba(0,0,0,0.87) !important; 
  }

   /* Code block styles */ 
 
   .language-python {
     padding-left: 40px;
     font-size: 15px;
   } 

  /* Hide all 2nd-level navs */
  .md-nav--secondary .md-nav__item .md-nav {
      display: none !important;
  } 
  
  /* Show when parent has .expanded class */
  .md-nav--secondary .md-nav__item.expanded > .md-nav {
      display: block !important;
  }
  
</style>
"""

############################################################
## The dict with notebook info hardcoded...

jupyter_files = {
    "Python-Part1.ipynb": {
        "title": "[Workshop] Python intensive, part 1",
        "description": (
            "Introduction to programming concepts such as functions, data types, "
            "operators, logic, and control flow."
        ),
        "authors": ["Gregg Thomas", "Tim Sackton"]
    },
    "Python-Part2.ipynb": {
        "title": "[Workshop] Python intensive, part 2",
        "description": (
            "Introduction to Python data structures, including lists and dictionaries, "
            "loops, libraries, and writing functions."
        ),
        "authors": ["Gregg Thomas", "Danielle Khost"]
    },
    "Python-Part3.ipynb": {
        "title": "[Workshop] Python intensive, part 3",
        "description": (
            "More on writing your own functions, debugging strategies, and exception "
            "handling in Python."
        ),
        "authors": ["Lei Ma", "Tim Sackton"],
    },
    "Python-Part4.ipynb": {
        "title": "[Workshop] Python intensive, part 4",
        "description": (
            "Introduction to file handling and the numpy library for numerical computing "
            "in Python, including arrays and basic operations."
        ),
        "authors": ["Lei Ma", "Adam Freedman"],
        "old-alts": [
            "A pie chart titled 'Programming Language Popularity': Python 26.9%, Ruby 26.2%, "
            "C++ 30.6%, and Java 16.2%."
        ]
    },
    "Python-Part5.ipynb": {
        "title": "[Workshop] Python intensive, part 5",
        "description": (
            "Introduction to data manipulation with pandas and data visualization with seaborn."
        ),
        "authors": ["Danielle Khost", "Adam Freedman"],
        "alts": [
            "An illustration of a penguin's head with 'bill length' and 'bill depth'. "
            "The bill length is the distance from the tip of the bill to the base, "
            "while the bill depth is the distance from the top of the bill to the bottom. "
            " Note: In the raw data, bill dimensions are recorded as 'culmen length' and 'culmen depth'. The culmen is the dorsal ridge atop the bill.",

            "A density plot with one line representing male penguins and another line representing females. "
            "The x-axis is unlabled and ranges from -3 to 4 and the y-axis is labeled Density and ranges from 0 to 0.5. "
            "Both lines are bi-modal with the female having a peak around -1 and a smaller peak around 1."
            "The male line is shifted to the right with peaks at just under 0 and 2.",            

            "A density plot with one line representing male penguins and another line representing females. "
            "The x-axis is unlabled and ranges from -4 to 4 and the y-axis is labeled Density and ranges from 0 to 0.5. "
            "Both lines are bi-modal and essentially overlapping with peaks around -1 and a smaller peak around 1.5.",

            "A density plot with six lines representing males and females from 3 penguin species. "
            "The x-axis is unlabled and ranges from -4 to 4 and the y-axis is labeled Density and ranges from 0 to 0.4. "
            "All lines are essentially overlapping with a single peak at 0.",

            "The different seaborn plot categories and the types of plots within them: relplots are scatter plots and line plots; "
            "distplots are histograms, KDE plots, ecdf plots, and rug plots; catplots are bar plots, box plots, violin plots, strip plots, swarm plots, and point plots",            

            "A histogram showing 'flipper length' in millimeters on the x-axis ranging from 170-230 and 'Count' on the y-axis ranging from 0 to 80. "
            "There is a sharp peak around 190mm, a drop-off at 205mm, and then a smaller peak around 215mm.",

            "A categorical boxplot. On the x-axis are 3 bird species: Adelie, Gentoo, and Chinstrap. The y-axis is 'bill length' in millimeters ranging from 35-60. "
            "Adelie have the shortest bill length with a median around 39mm while the other two species have similar distributions of bill length with medians around 46-47mm.",

            "An overlapping histogram showing the distribution of 'flipper length' in millimeters for 3 species of penguins: Adelie, Gentoo, and Chinstrap. "
            "The x-axis ranges from 170-230mm and the y-axis is 'Count'. Because the bars overlap, the data is difficult to parse. ",

            "A stacked histogram showing the distribution of 'flipper length' in millimeters for 3 species of penguins: Adelie, Gentoo, and Chinstrap. "
            "The x-axis ranges from 170-230mm and the y-axis is 'Count'. The bars are stacked on top of each other. "
            "The distributions for the 3 species are roughly normal. "
            "The Adelie species has a peak around 190mm with a count of 80, the Gentoo species has a peak around 210mm with a count of 20, and the Chinstrap species has a peak around 220mm with a count of 40.",

            "A scatter plot with 'bill length' in millimeters on the x-axis ranging from 35-60 and 'body mass' in grams on the y-axis ranging from 3000-6000. "
            "The points are colored by species: Adelie, Gentoo, and Chinstrap. dots represent males and x's represent females. "
            "The plot shows a clear separation between the species based on bill length and body mass and a separation between sexes within species. "
            "Adelie have the smallest bill length and body mass, centered around 40mm and 4000g, respectively. "
            "Chinstrap have longer bill lengths centered around 450mm, but a similar range of body mass to the Adelie, centered around 3800g. "
            "The Gentoo have a bill length between the other two species, centered around 47mm but higher body mass, centered around 5000g. "
            "In all species, females have both shorter bills and lower body masses.",

            "A scatter plot from a PCA analysis of three penguin species, Adeli, Gentoo, and Chinstrap. "
            "The x-axis is labeled 'PC1' and ranges from -3 to 4. The y-axis is labeled 'PC2' and ranges from -2 to 2. "
            "The Adelie and Chinstrap points cluster from -2 to -1 on PC1 and -2 to 2 on PC2. "
            "The Gentoo points separate from the other two on PC1 and cluster from 1 to 4 on PC1 and -2 to 1 on PC2. ",

            "A scatter plot from a PCA analysis of three penguin species, Adeli, Gentoo, and Chinstrap. "
            "The x-axis is labeled 'PC2' and ranges from -3 to 4. The y-axis is labeled 'PC3' and ranges from -2 to 2. "
            "Points are scattered across the with the exception of the sector where both PCs are negative. "
            "While Chinstrap points cluster at the high end of both PC1 and PC2, the distinction is not vivid.",

            "A styleized scatter plot from a PCA analysis of three penguin species, Adeli, Gentoo, and Chinstrap. "
            "The plot is titled PCA of Penguin Dataset and there are gridlines at every axis label. "
            "Four red arrows point out from the origin representing the variables: bill_depth_mm (pointing up and left), bill_length_mm (pointin up and right), body_mass_g (pointing right and slightly up), and flipper_length_mm (pointing right)"
            "The x-axis is labeled 'Principal Component 1' and ranges from -3 to 4. The y-axis is labeled 'Principal Component 2' and ranges from -2 to 2. "
            "The Adelie and Chinstrap points cluster from -2 to -1 on PC1 and -2 to 2 on PC2. "
            "The Gentoo points separate from the other two on PC1 and cluster from 1 to 4 on PC1 and -2 to 1 on PC2. "            
        ]
    },
    "Python-Part6.ipynb": {
        "title": "[Workshop] Python intensive, part 6",
        "description": (
            "Analyzing a real dataset: Indiana storms."
        ),
        "authors": ["Danielle Khost", "Lei Ma"],
        "alts": [
            "A barplot showing the number of Floods and Flash Floods in different counties in Indiana. "
            "The x-axis separates 'Flood' and 'Flash Flood' events, while the y-axis shows the number of events. "
            "Bars in each category are colored by county name. "
            "For Flash flood: Spencer 1, Marion 6, Vermillion 1, Monroe 0, Tippecanoe 0. "
            "For Flood: Spencer 1, Marion 4, Vermillion 1, Monroe 1, Tippecanoe 1. ",

            "A strip plot showing the duration of different events in hours in hours on the x-axis, ranging from 0 to 35. "
            "The y-axis shows the event type. "
            "Event types are 'Winter Weather', 'Heavy Snow', 'Thunderstorm Wind', 'Extreme Cold/Wind Chill', 'Hail', 'Heavy Rain', "
            "''Tornado', 'Heat', 'Dense Fog', 'Cold/Wind Chill', and 'Winter Storm'. "
            "Winter Weather and Heavy Snow span the range of durations, while Winter Storms last between 10 and 26 hours. "
            "Thunderstorm Wind, Hail, and Tornados have short durations, less than 1 hour. "
            "There are few Extreme Cold/Wind Chill events, mostly around 13 hours long. "
            "Heat, Dense Fog, and Cold/Wind Chill events all last between 4 and 13 hours.",

            "A strip plot showing the duration of Flood and Flash flood events in hours on the x-axis, ranging from 0 to 700. "
            "The y-axis shows the event type. "
            "Flash Floods all last under 24 hours while Floods can last up to 700 hours."
        ]
    },
    "python-healthy-habits.ipynb": {
        "title": "[Workshop] Python intensive - healthy habits",
        "description": (
            "A supplemental resource for the Python intensive workshop, "
            "Includes tips on writing clean code, using comments effectively, and following best practices."
        ),
        "authors": ["Lei Ma"],
        "alts" : []
    }
}

############################################################
## MAIN SCRIPT

skip = []
SKIP_TAG = "no-execute"

for jupyter_file in jupyter_files:

    # For debugging
    # if jupyter_file != "Python-Part6.ipynb":
    #     continue;

    if jupyter_file in skip:
        print(f"[HOOK] Skipping {jupyter_file}")
        continue

    # Set output file name
    md_path = os.path.splitext(jupyter_file)[0] + ".md"
    print(f"[HOOK] {jupyter_file}")

    # Read the Jupyter notebook
    with open(jupyter_file, encoding="utf-8") as f:
        nb = nbformat.read(f, as_version=4)

    # 1. SKIP CODE in 'no-execute' cells for execution
    prep = SkipExecuteTaggedCellsPreprocessor(tag="no-execute")
    nb, _ = prep.preprocess(nb, {})

    # 2. EXECUTE notebook (now, those cells are basically ignored/skipped)
    ep = ExecutePreprocessor(timeout=600, kernel_name='python3', allow_errors=True, exclude_tags=['no-execute'])
    ep.preprocess(nb, {'metadata': {'path': os.path.dirname(jupyter_file) or '.'}})

    # 3. RESTORE hidden code so students see the full exercise cell content
    restore_skipped_cells(nb, tag="no-execute")

    # --- INSERT PRINT CODE HERE ---
    # for cell in nb.cells:
    #     if cell.cell_type == 'code' and 'sns.histplot' in cell.source:
    #         import json
    #         print(json.dumps(cell, indent=2))
    # --- continue with markdown export ---

    # Export to Markdown
    exporter = MarkdownExporter()

    # Register the custom preprocessor to handle code cells
    exporter.register_preprocessor(CodeCellPreprocessor, enabled=True)

    # 4. Export to Markdown etc (using CodeCellPreprocessor)
    body, _ = exporter.from_notebook_node(nb)

    # Write the markdown content to the file
    with open(md_path, "w", encoding="utf-8") as out_f:
        out_f.write(body)

    # === CLEAR OUTPUTS AND SAVE .ipynb as student version ===
    clear_proc = ClearOutputPreprocessor()
    nb, _ = clear_proc.preprocess(nb, {})

    cleared_path = os.path.splitext(jupyter_file)[0] + "-student.ipynb"
    with open(cleared_path, "w", encoding="utf-8") as out_nb:
        nbformat.write(nb, out_nb) 

    ##########

    # Extract and format front-matter for the notebook
    title = jupyter_files[jupyter_file]["title"]
    description = jupyter_files[jupyter_file]["description"]
    authors = jupyter_files[jupyter_file].get("authors", [])

    author_str = "\n    ".join(f"- {author}" for author in authors)

    front_matter_content = front_matter.format(title=title, description=description, authors=author_str)

    ##########

    # Read the markdown file
    with open(md_path, encoding="utf-8") as md_stream:
        md = md_stream.read().split("\n")

    # === 1. Process image alt-texts ===
    # Read every line and detect if it starts with the image syntax
    # If so, add the alt-text
    pattern_img = r"^(\s*)!\[(.*?)\](\([^\)]*\))"
    num_img = 0
    for i in range(len(md)):
        if re.match(pattern_img, md[i]):
            alt_text = jupyter_files[jupyter_file].get("alts", [])[num_img]
            md[i] = re.sub(pattern_img, r"\1![{}]\3".format(alt_text), md[i])
            num_img += 1

    # === 2. Decorate eligible markdown links ===
    pattern_link = re.compile(r'(?<!\!)\[([^\]]+?)\]\(([^)]+?)\)')
    excluded_domain = "https://informatics.fas.harvard.edu/"

    for i in range(len(md)):
        md[i] = pattern_link.sub(styleLink, md[i])

    # Write the markdown file with front-matter, alt-texts, and styles
    md = "\n".join(md)
    with open(md_path, "w", encoding="utf-8") as md_stream:
        md_stream.write(front_matter_content + md + style)

############################################################
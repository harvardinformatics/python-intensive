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

import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
from nbconvert.preprocessors import Preprocessor
from nbconvert import MarkdownExporter
from nbconvert.preprocessors import ClearOutputPreprocessor

############################################################        
## Custom preprocessor and associated functions for 
## handling code cells

def indentBlock(block, prefix):
    lines = block.splitlines()
    return '\n'.join(prefix + line if line.strip() else prefix for line in lines)

####################

def stripANSI(text):
    ansi_escape = re.compile(r'\x1b\[[0-9;]*m')
    return ansi_escape.sub('', text)

####################

def makeOutputBlocks(outputs, indent=None):
    """Return a list of output blocks, possibly indented."""
    out_blocks = []
    for output in outputs:
        text = ''
        if output.output_type == "stream":
            text = output.get("text", "")
        elif output.output_type in {"execute_result", "display_data"}:
            text = output.get("data", {}).get("text/plain", "")
        elif output.output_type == "error":
            text = "\n".join(output.get("traceback", []))
            text = stripANSI(text)
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
                cell.source = "\n".join(line for line in lines if not line.strip().startswith('#@title'))

                if "solution" in cell.metadata.get("tags", []):
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
        "alts": [
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
            "In all species, females have both shorter bills and lower body masses."
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

skip = ["python-healthy-habits.ipynb"]

for jupyter_file in jupyter_files:

    if jupyter_file in skip:
        print(f"[HOOK] Skipping {jupyter_file}")
        continue

    # For debugging
    # if jupyter_file != "Python-Day1.ipynb":
    #     continue;

    # Set output file name
    md_path = os.path.splitext(jupyter_file)[0] + ".md"
    print(f"[HOOK] {jupyter_file}")

    # Read the Jupyter notebook
    with open(jupyter_file, encoding="utf-8") as f:
        nb = nbformat.read(f, as_version=4)

    # Execute notebook in place
    ep = ExecutePreprocessor(timeout=600, kernel_name='python3', allow_errors=True, exclude_tags=['no-execute'])
    ep.preprocess(nb, {'metadata': {'path': os.path.dirname(jupyter_file) or '.'}})

    # Export to Markdown
    exporter = MarkdownExporter()

    # Register the custom preprocessor to handle code cells
    exporter.register_preprocessor(CodeCellPreprocessor, enabled=True)

    # Convert the notebook to Markdown
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
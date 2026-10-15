---
title: "[Workshop] Python intensive - data validation"
description: "A supplemental resource for the Python intensive workshop. Basic data validation checks with pandas: headers, file size, row counts, duplicated rows, unique IDs, and missing data."
authors:
    - Gregg Thomas
---

# Basic data validation with pandas

This is a supplemental notebook for the FAS Informatics Python Intensive. It builds on the file reading and `pandas` material from Part 4.

## Basic data validation skills (the bare minimum)

While much of analytical coding could now be handed off to an LLM, it is still important to build your intuition about data (and to check the LLMs work). Here we suggest mastering a few very basic data validation techniques. These are the checks you will use to make sure your data, and any code that touches it (whether written by you or by an LLM), are doing what you expect. In this notebook, we introduce some of the most basic validation skills that are important to honing your intuition and technical skills. This is not an exhaustive list! You may want to check other things depending on your data.

For simplicity, we assume the data here is a **generic delimited text file** (*e.g.* comma-separated or tab-separated values), except where otherwise noted. Many data files, including many bioinformatics file formats, are indeed this. For other formats, notably sequence files (FASTA, FASTQ, etc.), there are other specialized libraries to read them (*e.g.* `biopython`).

Most of the code in this notebook runs on real example datasets. A few examples are labeled **(not run)** because our example datasets don't contain the situations they check for, but you can use them on your own data.

## Getting the data

We'll use three datasets that you may have seen in other parts of the workshop:

- `bird_names.csv`: a list of bird species with their scientific names, common names, and taxon IDs.
- `bird_observations.csv`: observations of birds, each with an observation ID, the time of the observation, and the taxon ID of the bird observed.
- `indiana_storms_full.csv`: storm events recorded in Indiana in 2015.

Run the following cells to download the data and load the libraries we'll use.


```python
# These lines download the files locally to the same folder as your notebook
!wget https://raw.githubusercontent.com/harvardinformatics/python-intensive/refs/heads/main/data/bird_names.csv
!wget https://raw.githubusercontent.com/harvardinformatics/python-intensive/refs/heads/main/data/bird_observations.csv
!wget https://raw.githubusercontent.com/harvardinformatics/python-intensive/refs/heads/main/data/indiana_storms_full.csv
```

<pre class="output-block">--2026-10-14 23:36:46--  https://raw.githubusercontent.com/harvardinformatics/python-intensive/refs/heads/main/data/bird_names.csv
</pre>

<pre class="output-block">Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 2606:50c0:8001::154, 2606:50c0:8002::154, 2606:50c0:8003::154, ...
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|2606:50c0:8001::154|:443... connected.
HTTP request sent, awaiting response...
</pre>

<pre class="output-block">200 OK
Length: 4383 (4.3K) [text/plain]
Saving to: ‘bird_names.csv.1’


bird_names.csv.1      0%[                    ]       0  --.-KB/s
bird_names.csv.1    100%[===================>]   4.28K  --.-KB/s    in 0.001s

2026-10-14 23:36:46 (4.05 MB/s) - ‘bird_names.csv.1’ saved [4383/4383]
</pre>

<pre class="output-block">--2026-10-14 23:36:46--  https://raw.githubusercontent.com/harvardinformatics/python-intensive/refs/heads/main/data/bird_observations.csv
</pre>

<pre class="output-block">Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 2606:50c0:8001::154, 2606:50c0:8002::154, 2606:50c0:8003::154, ...
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|2606:50c0:8001::154|:443... connected.
HTTP request sent, awaiting response...
</pre>

<pre class="output-block">200 OK
Length: 50448 (49K) [text/plain]
Saving to: ‘bird_observations.csv.1’


bird_observations.c   0%[                    ]       0  --.-KB/s
bird_observations.c 100%[===================>]  49.27K  --.-KB/s    in 0.01s

2026-10-14 23:36:47 (4.72 MB/s) - ‘bird_observations.csv.1’ saved [50448/50448]
</pre>

<pre class="output-block">--2026-10-14 23:36:47--  https://raw.githubusercontent.com/harvardinformatics/python-intensive/refs/heads/main/data/indiana_storms_full.csv
</pre>

<pre class="output-block">Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 2606:50c0:8000::154, 2606:50c0:8001::154, 2606:50c0:8002::154, ...
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|2606:50c0:8000::154|:443... connected.
HTTP request sent, awaiting response...
</pre>

<pre class="output-block">200 OK
Length: 952491 (930K) [text/plain]
Saving to: ‘indiana_storms_full.csv.1’


          indiana_s   0%[                    ]       0  --.-KB/s
indiana_storms_full 100%[===================>] 930.17K  --.-KB/s    in 0.04s

2026-10-14 23:36:47 (21.0 MB/s) - ‘indiana_storms_full.csv.1’ saved [952491/952491]
</pre>


```python
import os
import pandas as pd
```

## Does my file have headers? If so, how many?

In a basic table, the first row is often headers: names that describe each column. However, for standardized file formats headers may not be included since they should be the same across all files. Additionally, many data files (especially in bioinformatics) include metadata, provenance, and other information in the first few rows of a file. These are often denoted with a `#` at the start of the line. It is important to know if your file has headers, because they will affect how you read the file and should be skipped for any validation or analysis of the data.

Here is a simple way to check if a file has headers, by printing its first few lines with Python:


```python
with open("bird_names.csv", "r") as bird_file:
    for i in range(5):
        print(bird_file.readline(), end="")
```

<pre class="output-block">Anas rubripes,American Black Duck,6924
Fulica americana,American Coot,473
Spinus tristis,American Goldfinch,145310
Falco sparverius,American Kestrel,4665
Turdus migratorius,American Robin,12727
</pre>

This prints the first 5 lines of the file. If all you see are data values, then the file does not have headers (and you should hopefully be able to look up what the columns are). If the first row has text describing the columns, that is a header.

In this case, there is no header: every line is a bird species, with its scientific name, common name, and taxon ID. Let's also count the number of lines in the file:


```python
num_lines = 0
with open("bird_names.csv", "r") as bird_file:
    for line in bird_file:
        num_lines += 1

print(num_lines)
```

<pre class="output-block">105
</pre>

Knowing whether a file has a header matters because, by default, `pd.read_csv()` assumes that the first line of the file is a header. Let's see what happens if we read this file without telling `pandas` otherwise:


```python
bird_names_wrong = pd.read_csv("bird_names.csv")
print(len(bird_names_wrong))
bird_names_wrong.head()
```

<pre class="output-block">104
</pre>

<pre class="output-block">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Anas rubripes    American Black Duck    6924
0      Fulica americana          American Coot     473
1        Spinus tristis     American Goldfinch  145310
2      Falco sparverius       American Kestrel    4665
3    Turdus migratorius         American Robin   12727
4  Spizelloides arborea  American Tree Sparrow  474210
</pre>

`pandas` used the first bird in the file (the American Black Duck) as the column names, so that bird is no longer one of the rows of our DataFrame. The file has 105 lines, but the DataFrame only has 104 rows! `pandas` did not give us any warning or error about this, so it is up to us to notice.

To read a file that has no header, we set `header=None`, and we can provide our own column names with the `names` argument:


```python
bird_names = pd.read_csv("bird_names.csv", header=None, names=["scientific_name", "common_name", "taxon_id"])
print(len(bird_names))
bird_names.head()
```

<pre class="output-block">105
</pre>

<pre class="output-block">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;scientific_name          common_name  taxon_id
0       Anas rubripes  American Black Duck      6924
1    Fulica americana        American Coot       473
2      Spinus tristis   American Goldfinch    145310
3    Falco sparverius     American Kestrel      4665
4  Turdus migratorius       American Robin     12727
</pre>

Now the number of rows in the DataFrame matches the number of lines in the file, and the American Black Duck is back as the first row. We'll keep both versions of this DataFrame around for an exercise later.

### Metadata lines

If there are multiple metadata lines beginning with `#`, you will want to count them. None of our example files have metadata lines, so the following code is **not run**, but you could count them in a file called `my-data-file.tsv` like this:

```python
# (not run)
num_metadata_lines = 0
with open("my-data-file.tsv", "r") as data_file:
    for line in data_file:
        if line.startswith("#"):
            num_metadata_lines += 1

print(num_metadata_lines)
```

This will count the number of lines that start with a hash symbol, which are typically metadata lines in data files. **You will have to remember or account for how many header lines are in your file going forward.**

For example, if all of the metadata lines are at the top of the file, you can tell `pandas` to skip that many lines when reading the file with the `skiprows` argument:

```python
# (not run)
my_data = pd.read_csv("my-data-file.tsv", sep="\t", skiprows=num_metadata_lines)
```

Alternatively, you can tell `pandas` that `#` marks a comment with the `comment` argument:

```python
# (not run)
my_data = pd.read_csv("my-data-file.tsv", sep="\t", comment="#")
```

Be careful with `comment="#"`, though: `pandas` ignores everything after a `#` on **any** line, not just on lines that start with one. If a `#` appears in the middle of a data line, the rest of that line will be cut off.

>**Exercise**: What is one problem you could encounter when counting metadata headers in this way?

<details markdown="1"><summary>Solution</summary>

There are several possible problems, for example:

- In some file formats, the line with the column names also starts with a `#`. For example, in VCF files the column header line starts with `#CHROM`. This line would be counted as a metadata line, and if you skip every line that starts with `#` you would lose your column names.
- A data line could start with `#`, for example if a value in the first column happens to begin with `#`. This line would be counted as metadata even though it is data.
- Not all files use `#` to mark metadata lines. Some use other characters, or no special character at all.
- The loop counts every line that starts with `#` anywhere in the file, not just at the top. If there are `#` lines further down in the file, using this count with `skiprows` would skip the wrong lines.

</details>

## File size

If you have an understanding of the data files and their contents, looking at the size of a file can give you an idea if something is wrong. For example, let's say you run your big experiment and send the samples off to the sequencing facility. They send you a link to download the files which you click and let run on your computer. You return to a completed download dialogue. However, you think you should make sure it was successful, so you check some of the file sizes.

In Python, you can get the size of a file in bytes with the `os.path.getsize()` function. Let's check the sizes of the files we downloaded at the start of this notebook:


```python
for filename in ["bird_names.csv", "bird_observations.csv", "indiana_storms_full.csv"]:
    size_bytes = os.path.getsize(filename)
    size_mb = size_bytes / 1024 / 1024
    print(filename, size_bytes, "bytes", round(size_mb, 3), "MB")
```

<pre class="output-block">bird_names.csv 4383 bytes 0.004 MB
bird_observations.csv 50448 bytes 0.048 MB
indiana_storms_full.csv 952491 bytes 0.908 MB
</pre>

Back to the sequencing example: for 9 out of 10 of your samples, the sequencing read files are between 60GB and 70GB, but for one it's only 35GB. This should be a red flag to you to stop and check the file more thoroughly. Is the genome of this sample expected to be smaller? How many reads are in the file? Was the download interrupted for the last sample (likely)? Maybe the sequencing facility made a mistake and sent the wrong file or sequenced the wrong sample.

## Counting rows

In another scenario, perhaps you are processing some data and doing some filtering. How can you tell, at a glance, the extent of your filtering? Well, if the filtering works by *removing data rows* from your DataFrame, then you can count the rows before and after filtering.

Let's read in the Indiana storms data and count the rows with `len()`:


```python
storms = pd.read_csv("indiana_storms_full.csv")
print(len(storms))
```

<pre class="output-block">1315
</pre>

You can also use the `.shape` attribute of the DataFrame, which gives both the number of rows and the number of columns:


```python
storms.shape
```

<pre class="output-block">(1315, 51)
</pre>

Note that the header line of the file is not counted as a row of the DataFrame, since `pandas` used it for the column names. So, for a file with a header, the number of rows in the DataFrame is one less than the number of lines in the file.

Now, let's do some filtering. Say we only want to analyze storms that have a value for property damage, so we remove rows where the `DAMAGE_PROPERTY` column is missing with `.dropna()` (see Part 5). Then we count the rows before and after filtering:


```python
storms_damage = storms.dropna(subset=["DAMAGE_PROPERTY"])

num_before = len(storms)
num_after = len(storms_damage)
num_removed = num_before - num_after

print("Rows before filtering:", num_before)
print("Rows after filtering:", num_after)
print("Rows removed:", num_removed)
print("Percent removed:", round(num_removed / num_before * 100, 1))
```

<pre class="output-block">Rows before filtering: 1315
Rows after filtering: 1011
Rows removed: 304
Percent removed: 23.1
</pre>

Filtering removed 304 rows, about 23 percent of the data. Is this expected, or are your filtering parameters too strict? (Tweaking filtering criteria is a time-honored data analysis task.) Whether this is expected or not, you will have to report and justify this filtering when you communicate your results in talks or papers.

>**Exercise**: Filter the `storms` DataFrame to keep only the rows where the `EVENT_TYPE` is either `"Flood"` or `"Flash Flood"`. How many rows were kept, how many were removed, and what percent of the rows were removed? *Hint: the `.isin()` method may be useful here.*


```python
# Your code here
```

??? success "Solution"
    ```python
    
    storms_floods = storms[storms["EVENT_TYPE"].isin(["Flood", "Flash Flood"])]
    
    num_before = len(storms)
    num_after = len(storms_floods)
    num_removed = num_before - num_after
    
    print("Rows kept:", num_after)
    print("Rows removed:", num_removed)
    print("Percent removed:", round(num_removed / num_before * 100, 1))
    ```

    <pre class="output-block">Rows kept: 246
    Rows removed: 1069
    Percent removed: 81.3
    </pre>

## Counting duplicated rows

Another basic check would be to count duplicated rows in a DataFrame. In `pandas`, the `.duplicated()` method returns `True` for each row that is an exact copy of a row that came before it, and `False` otherwise. Since `True` counts as 1 and `False` counts as 0, we can add these up with `.sum()` to count the duplicated rows. None of our example datasets have duplicated rows, so the following code is **not run**, but for a DataFrame called `my_data` it would look like this:

```python
# (not run)
my_data.duplicated().sum()
```

If the number displayed on the screen is **0**, then there are no duplicated rows in the DataFrame. If it is greater than **0**, then there are duplicated rows. To see the duplicated rows themselves, you can use `.duplicated()` to filter the DataFrame. Setting `keep=False` marks **every** copy of a duplicated row as `True`, including the first one, so you see all of them:

```python
# (not run)
my_data[my_data.duplicated(keep=False)]
```

Note that these two can give different numbers. For example, if one row appears 3 times in the DataFrame, `my_data.duplicated().sum()` would count 2 duplicated rows (the copies after the first one), while `my_data[my_data.duplicated(keep=False)]` would show all 3 copies.

You can also check for duplicates based on only some of the columns with the `subset` argument. For example, to count rows that repeat a sample ID, even if the rest of the row is different:

```python
# (not run)
my_data.duplicated(subset=["sample_id"]).sum()
```

Again, you will have to determine if the number of duplicated rows is expected or not, and if not, you will have to figure out how and when they were added to the data. `pandas` does have a `.drop_duplicates()` method to remove duplicated rows, but you should only use it once you understand where the duplicates came from.

## Counting unique IDs

Oftentimes, one column of a data file will contain some sort of unique identifier that corresponds to the sample, event, or whatever the row represents. One good check is to count the number of these unique identifiers to match against your expectations.

For instance, perhaps you or an LLM has been processing the data through several steps and you decide it's time to pause and do some sanity checks. You started out your experiment with 100 samples, but when you count the unique sample IDs in your current data, there are only 99. Now you have to stop and assess whether this is expected or not. Did one of your steps filter out "low quality" samples and this one didn't make it? Was it dropped erroneously? Or was this a conscious choice based on other experimental design factors?

In `pandas`, the `.nunique()` method counts the number of unique values in a column. In the storms data, each storm event has an ID in the `EVENT_ID` column. Let's count the unique event IDs and compare that to the number of rows:


```python
print("Rows:", len(storms))
print("Unique event IDs:", storms["EVENT_ID"].nunique())
```

<pre class="output-block">Rows: 1315
</pre>

<pre class="output-block">Unique event IDs: 1315
</pre>

The number of unique event IDs is the same as the number of rows, so each row is a different storm event. The storms data also has an `EPISODE_ID` column. Let's count those too:


```python
storms["EPISODE_ID"].nunique()
```

<pre class="output-block">200
</pre>

There are far fewer unique episode IDs than rows. This is because a single storm episode can include several events (*e.g.* one storm system that causes hail in one county and flooding in another). So `EVENT_ID` uniquely identifies each row, but `EPISODE_ID` does not. Knowing which column (if any) uniquely identifies the rows of your data is an important part of understanding it.

To see which IDs appear most often, use the `.value_counts()` method:


```python
storms["EPISODE_ID"].value_counts().head()
```

<pre class="output-block">EPISODE_ID
98724     38
101603    29
101193    27
98723     25
94440     25
Name: count, dtype: int64
</pre>

Counting unique IDs tells you *how many* there are, but if the count doesn't match your expectations, you'll want to know *which* IDs are missing. One way to do this is with sets (see Part 2), which only contain unique values. Taking the difference between two sets with the `-` operator gives all of the values in the first set that are not in the second set. For example, to compare a list of samples you expect with the sample IDs in your data (**not run**):

```python
# (not run)
expected_ids = set(my_samples["sample_id"])
found_ids = set(my_data["sample_id"])
missing_ids = expected_ids - found_ids
print(missing_ids)
```

For the next exercise, let's read in the bird observations data:


```python
bird_obs = pd.read_csv("bird_observations.csv")
bird_obs.head()
```

<pre class="output-block">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;id         time_observed_at  taxon_id
0  145591043  2023-01-01 17:33:31 UTC     14886
1  145610149  2023-01-01 20:55:00 UTC      7004
2  145610383  2023-01-01 21:13:00 UTC      6993
3  145611915  2023-01-01 21:12:00 UTC     13858
4  145611916  2023-01-01 21:08:00 UTC     14850
</pre>

>**Exercise**: The `taxon_id` column of `bird_obs` contains the taxon ID of the bird that was observed. How many unique taxon IDs are in `bird_obs`? Are any of these taxon IDs missing from the `taxon_id` column of the `bird_names` DataFrame that we read in correctly above? What about the `bird_names_wrong` DataFrame? *Hint: in `bird_names_wrong`, the taxon IDs are in the third column, which you can select with `.iloc[:, 2]`.*


```python
# Your code here
```

??? success "Solution"
    ```python
    
    observed_ids = set(bird_obs["taxon_id"])
    print("Unique taxon IDs in bird_obs:", len(observed_ids))
    
    # bird_names was read with header=None, so it has every bird in the file
    missing_ids = observed_ids - set(bird_names["taxon_id"])
    print("Missing from bird_names:", missing_ids)
    
    # bird_names_wrong used the first bird in the file as the column names
    missing_ids_wrong = observed_ids - set(bird_names_wrong.iloc[:, 2])
    print("Missing from bird_names_wrong:", missing_ids_wrong)
    ```

    <pre class="output-block">Unique taxon IDs in bird_obs: 105
    Missing from bird_names: set()
    Missing from bird_names_wrong: {6924}
    </pre>

If you compare the two results, you'll see that how we read in `bird_names` changes the answer. A mistake in one step (reading the file) can show up as a confusing problem in a later step (comparing IDs), which is why it's good to validate your data as you go.

## Counting NAs

In a data table, the symbol `NA` is often used to denote missing data. Do you expect missing data in your data? How many missing values are too many for your experiment?

When you read a file with `pd.read_csv()`, `pandas` automatically converts empty fields and several common symbols for missing data, including `NA`, `NaN`, `N/A`, and `null`, into its own missing value, `NaN` (see Part 5). This is convenient, but be aware of it: if `NA` is a real value in one of your columns (for example, as an abbreviation), `pandas` will still treat it as missing. You can control this behavior with the `na_values` and `keep_default_na` arguments of `pd.read_csv()`.

Once the data is read in, you can count the missing values in a column with the `.isna()` method, which returns `True` for each missing value, followed by `.sum()`. Let's count the missing values in the `DAMAGE_PROPERTY` column of the storms data:


```python
print(storms["DAMAGE_PROPERTY"].isna().sum())
```

<pre class="output-block">304
</pre>

This is the same as the number of rows we removed when we filtered out the storms with missing property damage above.

You can also count the missing values in every column at once by using `.isna().sum()` on the whole DataFrame. The storms data has a lot of columns, so let's only show the ones that have at least one missing value:


```python
na_counts = storms.isna().sum()
na_counts[na_counts > 0]
```

<pre class="output-block">DAMAGE_PROPERTY        304
DAMAGE_CROPS           306
MAGNITUDE              738
MAGNITUDE_TYPE         925
FLOOD_CAUSE           1069
CATEGORY              1315
TOR_F_SCALE           1291
TOR_LENGTH            1291
TOR_WIDTH             1291
TOR_OTHER_WFO         1312
TOR_OTHER_CZ_STATE    1312
TOR_OTHER_CZ_FIPS     1312
TOR_OTHER_CZ_NAME     1312
BEGIN_RANGE            444
BEGIN_AZIMUTH          444
BEGIN_LOCATION         444
END_RANGE              444
END_AZIMUTH            444
END_LOCATION           444
BEGIN_LAT              444
BEGIN_LON              444
END_LAT                444
END_LON                444
EVENT_NARRATIVE        236
dtype: int64
</pre>

There is a lot of missing data here, but some of it is expected. For example, the `CATEGORY` column is missing in all 1315 rows, so it contains no data at all for these storms. And the columns starting with `TOR_` are only filled in for tornado events, so they are missing for most rows. Understanding *why* data is missing is just as important as counting it.

>**Exercise**: Count the number of missing values in each column of the `bird_obs` DataFrame. Then, display only the rows of `bird_obs` that have a missing value in the `time_observed_at` column.


```python
# Your code here
```

??? success "Solution"
    ```python
    
    print(bird_obs.isna().sum())
    
    bird_obs[bird_obs["time_observed_at"].isna()]
    ```

    <pre class="output-block">id                  0
    time_observed_at    3
    taxon_id            0
    dtype: int64
    </pre>

    <pre class="output-block">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;id time_observed_at  taxon_id
    568  161145010              NaN     20044
    569  161145128              NaN     20044
    961  181797640              NaN   1454382
    </pre>

## Summary

Here is a quick reference for the checks in this notebook:

| Validation check | `pandas` or Python code |
| ---------------- | ----------------------- |
| Look at the first few lines of a file | `open()` and `.readline()` |
| Read a file that has no header | `pd.read_csv(filename, header=None, names=column_names)` |
| Skip metadata lines | `pd.read_csv(filename, skiprows=n)` or `pd.read_csv(filename, comment="#")` |
| Get the size of a file in bytes | `os.path.getsize(filename)` |
| Count rows | `len(df)` or `df.shape` |
| Count duplicated rows | `df.duplicated().sum()` |
| View all copies of duplicated rows | `df[df.duplicated(keep=False)]` |
| Count unique values in a column | `df["column"].nunique()` |
| Count how often each value appears | `df["column"].value_counts()` |
| Find expected IDs that are missing | `set(expected_ids) - set(found_ids)` |
| Count missing values in a column | `df["column"].isna().sum()` |
| Count missing values in every column | `df.isna().sum()` |

None of these checks are complicated, but learning these skills even a little bit can give you powerful abilities that, at the very least, allow you to check an LLM's work, or, at most, could allow you to do the work yourself faster. Most importantly, whenever a number doesn't match your expectations, stop and figure out why before moving on.

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

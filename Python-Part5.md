---
title: "[Workshop] Python intensive, part 5"
description: "Introduction to data manipulation with pandas and data visualization with seaborn."
authors:
    - Danielle Khost
    - Adam Freedman
---

# Python intensive, part 5


```python
## Importing libraries
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
```

<pre class="output-block">---------------------------------------------------------------------------
ModuleNotFoundError                       Traceback (most recent call last)
Cell In[1], line 2
      1 ## Importing libraries
----> 2 import numpy as np
      3 import pandas as pd
      4 import seaborn as sns

ModuleNotFoundError: No module named 'numpy'
</pre>

## Review of Part 4

Welcome to Part 5 of our Python Intensive. In the previous session, we learned about data structures in python, in particular the list, the dictionary, and pandas dataframes. 

1. List
2. Of
3. Review
4. Topics
5. TBD

Today we will continue learning about how to use dataframes to transform your data. We will also briefly learn about how to plot your dataframe using the library seaborn. 

## Pandas continued

Now that we've learned how to inspect the data, let's learn how to work with the data!


```python
penguins = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2020/2020-07-28/penguins.csv')
penguins.head()
```

<pre class="output-block">---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[2], line 1
----> 1 penguins = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2020/2020-07-28/penguins.csv')
      2 penguins.head()

NameError: name 'pd' is not defined
</pre>

## Modifying a dataframe
Now that we have our external data read into a DataFrame, we can begin to work our magic. If you have ever worked with `tidyverse` in the R language some of this might look familiar to you, as `pandas` serves a similar role and can do many of the same functions. Let's look at several useful common examples.

### Filtering
When we discussed indexing, we looked at how we can select specific rows and columns in a dataframe, but often we will want to select rows based on a certain condition, e.g. in the dataframe that we just imported, only take the rows where the 'body_mass_g' column has a value greater than a given number. We can do this easily by specifying which column to filter on and a boolean statement, like so:


```python
print(penguins[penguins['flipper_length_mm'] == 181.0])

#Saving as new data frame:
penguins_filtered = penguins[penguins['body_mass_g'] > 3300]

penguins_filtered.head()
```

<pre class="output-block">---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[3], line 1
----> 1 print(penguins[penguins['flipper_length_mm'] == 181.0])
      3 #Saving as new data frame:
      4 penguins_filtered = penguins[penguins['body_mass_g'] > 3300]

NameError: name 'penguins' is not defined
</pre>

We can get more advanced with our filtering logic by adding multiple conditions and the following logical operators:

- `&`: "and"
- `|`: "or"
- `~`: "not"

**Note that these are different logical operators than we have previously learned in base python!**

If using multiple conditions, be sure to enclose each of them in parentheses!


```python
penguins_filtered = penguins[(penguins['body_mass_g'] > 3300) & (penguins['bill_length_mm'] > 38)]

penguins_filtered.head()
```

<pre class="output-block">---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[4], line 1
----> 1 penguins_filtered = penguins[(penguins['body_mass_g'] > 3300) & (penguins['bill_length_mm'] > 38)]
      3 penguins_filtered.head()

NameError: name 'penguins' is not defined
</pre>

Pandas also has a helper function called `.isin()` that is similar to the `in` operator in base python. It allows you to filter a dataframe based on whether a column value is in a list of values.


```python
penguins[penguins['species'].isin(['Adelie', 'Gentoo'])]
```

<pre class="output-block">---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[5], line 1
----> 1 penguins[penguins['species'].isin(['Adelie', 'Gentoo'])]

NameError: name 'penguins' is not defined
</pre>

> Exercise: filter the dataframe to only keep the birds observed in the `year` 2007 and with a `bill_length_mm` greater than 38mm


```python
# Your code here

penguins[(penguins["year"] == 2007) & (penguins["bill_length_mm"] > 38)]
```

<pre class="output-block">---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[6], line 3
      1 # Your code here
----> 3 penguins[(penguins["year"] == 2007) & (penguins["bill_length_mm"] > 38)]

NameError: name 'penguins' is not defined
</pre>

We can also filter based on strings, not just numbers! For this, you will want to use a string matching function from python, such as `.str.contains()` (which also a partial match), `.str.startswith()` (checks to see if a value starts with a given string), or others.


```python
penguins_filtered = penguins[penguins['species'].str.contains('Adel', case=False)]

penguins_filtered
```

<pre class="output-block">---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[7], line 1
----> 1 penguins_filtered = penguins[penguins['species'].str.contains('Adel', case=False)]
      3 penguins_filtered

NameError: name 'penguins' is not defined
</pre>

In the above example, this code looks for the string 'Adel' (case-insensitive, as we specify `case=False`) and only takes rows that contain the string somewhere in the `species` column.

#### Missing data in DataFrames

Missing data in a DataFrame is represeted by `NaN` (Not a Number). Pandas handles missing data in some specific ways, which we will discuss in this section. 

Missing numbers are propagated through the DataFrame when doing arithmetic operations. In the example below, when we try to sum the two columns together element-wise, any row where one of the columns has a missing value will result in the sum being `NaN`.


```python
ser1 = pd.Series([np.nan, np.nan, 2, 3])
ser2 = pd.Series([1, 2, np.nan, 4])
ser1 + ser2
```

<pre class="output-block">---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[8], line 1
----> 1 ser1 = pd.Series([np.nan, np.nan, 2, 3])
      2 ser2 = pd.Series([1, 2, np.nan, 4])
      3 ser1 + ser2

NameError: name 'pd' is not defined
</pre>

When using descriptive statistics and computational methods like `.sum()`, `.mean()`, pandas will ignore missing values and treat them like zero. 


```python
print(ser1.sum())

print(ser1.mean())
```

<pre class="output-block">---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[9], line 1
----> 1 print(ser1.sum())
      3 print(ser1.mean())

NameError: name 'ser1' is not defined
</pre>

This behavior can be changed by using the `skipna` argument, which is `True` by default. If you set `skipna=False`, pandas will treat missing values as `NaN` and will not ignore them, resulting in the whole operation returning `NaN`.


```python
print(ser1.mean(skipna=False))
```

<pre class="output-block">---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[10], line 1
----> 1 print(ser1.mean(skipna=False))

NameError: name 'ser1' is not defined
</pre>


One very useful function to know is how to get rid of rows with missing data in them, as including them can often cause errors in downstream analysis or skew your results. There is a convenient function built in to `pandas` that does this called `.dropna()`. By default, it will drop any row that has a missing value in any column. This may not always be what you want. You can specify which columns to look at using the `subset` arugment. 


```python
penguins_nona = penguins.dropna()

penguins_nona.info()
```

<pre class="output-block">---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[11], line 1
----> 1 penguins_nona = penguins.dropna()
      3 penguins_nona.info()

NameError: name 'penguins' is not defined
</pre>


```python
penguins_nona_bill_len = penguins.dropna(subset=["bill_length_mm"])

penguins_nona_bill_len.info()
```

<pre class="output-block">---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[12], line 1
----> 1 penguins_nona_bill_len = penguins.dropna(subset=["bill_length_mm"])
      3 penguins_nona_bill_len.info()

NameError: name 'penguins' is not defined
</pre>

Alternatively, you may want to fill in missing values with a specific value. You can do this using the `.fillna()` method.

### Calculating new columns

Let's say we will want to create a new column in our dataframe by applying some function to existing columns. For instance, in the dataframe of penguins data that we have been using, we want a column that normalizes `body_mass_g` column by performing a z-transform. A z-transform is the value minus the mean of the column divided by the standard deviation of the column. 

First, we put the name of the new column, `body_mass_z` in square brackets after our `penguin` DataFrame variable. Then we pull out the `body_mass_g` column and perform the calculation, using helper methods like `.mean()` and `.std()`, on the right side of the assignment operator. This syntax is similar to creating a new key in a dictionary.


```python
# Z-transform the body mass column

penguins["body_mass_z"] = (penguins["body_mass_g"] - penguins["body_mass_g"].mean()) / penguins["body_mass_g"].std()

penguins.head(10)
```

<pre class="output-block">---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[13], line 3
      1 # Z-transform the body mass column
----> 3 penguins["body_mass_z"] = (penguins["body_mass_g"] - penguins["body_mass_g"].mean()) / penguins["body_mass_g"].std()
      5 penguins.head(10)

NameError: name 'penguins' is not defined
</pre>

>**Exercise:** We can use multiple columns in the calculation of the new column. Create a column that contains the volume of the penguin's beak by assuming it is a cylinder, with `bill_length_mm` as the height and `bill_depth_mm` as the diameter. 
>
> **Hint:** The volume of a cylinder is given by the formula $V = \pi r^2 h$, where $r$ is the radius (half the diameter) and $h$ is the height.

![An illustration of a penguin's head with 'bill length' and 'bill depth'. The bill length is the distance from the tip of the bill to the base, while the bill depth is the distance from the top of the bill to the bottom.  Note: In the raw data, bill dimensions are recorded as 'culmen length' and 'culmen depth'. The culmen is the dorsal ridge atop the bill.](https://allisonhorst.github.io/palmerpenguins/reference/figures/culmen_depth.png)


```python
# Your code here

penguins["bill_volume"] = (penguins["bill_depth_mm"]/2)**2 * np.pi * penguins["bill_length_mm"]

penguins.head()
```

<pre class="output-block">---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[14], line 3
      1 # Your code here
----> 3 penguins["bill_volume"] = (penguins["bill_depth_mm"]/2)**2 * np.pi * penguins["bill_length_mm"]
      5 penguins.head()

NameError: name 'penguins' is not defined
</pre>

### Summarizing your data

Another common task in data analysis is to calculate summary statistics of your data. Pandas as a number of helper methods like `.mean()`, `.median()`, `.count()`, `unique()`, etc. that can be used to describe your data. Pandas DataFrames has a handy `.describe()` method that will give you a summary of the data in each column. By default, it will calculate the count, mean, standard deviation, minimum, 25th percentile, median, 75th percentile, and maximum of each numerical column. However, if you give it the `include='all'` or `include='object'` argument, it will also include the count, unique, top, and freq (of top) of each categorical column.


```python
penguins.describe(include='all')
```

<pre class="output-block">---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[15], line 1
----> 1 penguins.describe(include='all')

NameError: name 'penguins' is not defined
</pre>


```python
penguins.describe(include='object')
```

<pre class="output-block">---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[16], line 1
----> 1 penguins.describe(include='object')

NameError: name 'penguins' is not defined
</pre>

### Grouping and transforming your data

What if we want to use one of the categorical variables in our data as a factor level to calculate our summaries? For example, we may want to separately get the mean flipper length of each `species` of penguin. In order to do this, we need to do the following things:

1. Split our data into different **groups** (e.g. based the values in the `species` column)
2. Apply some function (**aggregation** or **transformation**)to each group in our data (e.g. calculates the mean) 
3. Combine each group back together into an output object

We input the column we want to group by into the `.groupby()` method. This creates a **grouped dataframe** object that acts like the regular dataframe, but is split into groups based on the column we specified.


```python
penguin_groups = penguins.groupby('species')
print(penguin_groups)
```

<pre class="output-block">---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[17], line 1
----> 1 penguin_groups = penguins.groupby('species')
      2 print(penguin_groups)

NameError: name 'penguins' is not defined
</pre>

We can see that on its own this is not especially useful, as grouping the DataFrame does not produce a new DataFrame (just this weird output message telling us that this is a `DataFrameGroupBy` object). In order to output a DataFrame, we need to pass the grouped DataFrame to some function that aggregates or transforms the data in each group.

We group our data, select the column we want to aggregate (in this case, `flipper_length_mm`) and apply the `.mean()` function to it:


```python
#Note the square brackets around the column name
penguins.groupby('species')['flipper_length_mm'].mean()
```

<pre class="output-block">---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[18], line 2
      1 #Note the square brackets around the column name
----> 2 penguins.groupby('species')['flipper_length_mm'].mean()

NameError: name 'penguins' is not defined
</pre>

When we apply the `.mean()` method to the grouped dataframe, it returns a `Series` object with the mean flipper length of each species. The exact details of whether pandas returns a `groupby` object as a Series or a DataFrame gets a little technical; for our purposes, just know that you can make sure the returned object is converted to a DataFrame (which is usually most convenient) by using the `.reset_index` function:


```python
penguins.groupby('species')['flipper_length_mm'].mean().reset_index()
```

<pre class="output-block">---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[19], line 1
----> 1 penguins.groupby('species')['flipper_length_mm'].mean().reset_index()

NameError: name 'penguins' is not defined
</pre>

We can group by multiple columns by passing a *list of column names* to the `.groupby()` method (and using `reset_index()` as before to have it output as a DataFrame): 


```python
penguins.groupby(['species', 'sex'])['flipper_length_mm'].mean().reset_index()
```

<pre class="output-block">---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[20], line 1
----> 1 penguins.groupby(['species', 'sex'])['flipper_length_mm'].mean().reset_index()

NameError: name 'penguins' is not defined
</pre>

So far we have just been applying the `.mean` function to our groups, but we can use other functions as well! One very useful function to know when grouping is `.size()`, which will return the number of rows in each group.


```python
penguins.groupby(['species', 'sex']).size()
```

<pre class="output-block">---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[21], line 1
----> 1 penguins.groupby(['species', 'sex']).size()

NameError: name 'penguins' is not defined
</pre>

>**Exercise:** Use grouping to answer the following question about the penguins dataset: Which island has the most Adelie penguins?
>
> **Hint:** Think about which order you should group by for the most readable output


```python
# Your code here

penguins.groupby(['species', 'island']).size()
```

<pre class="output-block">---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[22], line 3
      1 # Your code here
----> 3 penguins.groupby(['species', 'island']).size()

NameError: name 'penguins' is not defined
</pre>

> Now try your previous code with the order of the columns to group by switched. What changes?


```python
penguins.groupby(['island', 'species']).size()
```

<pre class="output-block">---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[23], line 1
----> 1 penguins.groupby(['island', 'species']).size()

NameError: name 'penguins' is not defined
</pre>

This shows us that grouping occurs **hierarchically**, meaning pandas groups data in the order that you specify in! In our case the result is the same (i.e. the counts are equal no matter which column you group on first), but one way is more readily readable for our question than the other. 


There are niche situations where it might matter, e.g. your aggregation function depends on the order of values (e.g. if you are sorting your grouped data), or you are doing some non-commutative operation, but generally speaking the results will be the same. 

> Exercise: now that we have an understanding of pandas, let's go back to our initial example! Calculating the average body mass (in **kg**) of each penguin species, by sex. We are aiming to reproduce the table below:
>
> Make sure you end up with a DataFrame and not a Series. 


| species   | sex    | body_mass_kg|
|-----------|--------|----------|
| Adelie    | female | 3.368836 |
| Adelie    | male   | 4.043493 |
| Chinstrap | female | 3.527206 |
| Chinstrap | male   | 3.938971 |
| Gentoo    | female | 4.679741 |
| Gentoo    | male   | 5.484836 |




```python
penguins["body_mass_kg"] = penguins["body_mass_g"] / 1000

penguins.groupby(['species', 'sex'])["body_mass_kg"].mean().reset_index()
```

<pre class="output-block">---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[24], line 1
----> 1 penguins["body_mass_kg"] = penguins["body_mass_g"] / 1000
      3 penguins.groupby(['species', 'sex'])["body_mass_kg"].mean().reset_index()

NameError: name 'penguins' is not defined
</pre>

> **Exercise**: using the `.max()` function, find the largest bird on each island.


```python
penguins.groupby('island')['body_mass_g'].max()
```

<pre class="output-block">---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[25], line 1
----> 1 penguins.groupby('island')['body_mass_g'].max()

NameError: name 'penguins' is not defined
</pre>

## Seaborn
### Plotting with Seaborn
In addition to knowing how to import and manipulate data, we often want to also *visualize* our data. There are many tools available that are specialized in plotting data, such a R and ggplot, Excel, etc., but often it can be helpful to do some quick visualization in python as part of a pipeline. The "classic" way to do this is using the `matplotlib` library, but for this workshop we are instead going to use `seaborn`, which is based on `matplotlib` but has (in our opinion) better syntax (being somewhat reminiscent of `ggplot`, a commonly-used R library), and is specially designed to integrate with `pandas`. 

 Plotting can get quite complicated, so we are going to stick to some more "cookie-cutter" implementation that is geared more towards exploratory analysis, rather than making publication-quality figures.

Just as before, it can be helpful to think about what your end goal looks like. Let's say I want to end up with a scatterplot that shows bird bill length relative to body weight, with the *color* of each point corresponding to bird species, and the *shape* of the point corresponding to bird sex. With that goal in mind, let's look at syntax.

### Defining the Data
We are going to continue using our penguins data set. `seaborn` has numerous functions for drawing different plots, summarized in the figure below. There are three different broad "families" of `seaborn` plots, which are shown in the figure below:


![The different seaborn plot categories and the types of plots within them: relplots are scatter plots and line plots; distplots are histograms, KDE plots, ecdf plots, and rug plots; catplots are bar plots, box plots, violin plots, strip plots, swarm plots, and point plots](image.png)

- `relplot` plots show relationships between variables
- `displot` show distibutions
- `catplot` plot categorical data 

Each plot function within a family usually has similar syntax, as they represent data in similar ways. To create a plot, we call one of these functions and specify our (`pandas`) dataframe and which columns to encode in which axis. For example, if we wanted a histogram:


```python
penguins = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2020/2020-07-28/penguins.csv')
penguins.head()
```

<pre class="output-block">---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[26], line 1
----> 1 penguins = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2020/2020-07-28/penguins.csv')
      2 penguins.head()

NameError: name 'pd' is not defined
</pre>


```python
sns.histplot(data=penguins, x="flipper_length_mm")
```

<pre class="output-block">---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[27], line 1
----> 1 sns.histplot(data=penguins, x="flipper_length_mm")

NameError: name 'sns' is not defined
</pre>

We can see that for this type of plot, we only need to encode a single column (for the x-axis), but other types of plots might require additional axes. For example, a boxplot needs both an x and y axis defined:


```python
sns.boxplot(data=penguins,x="species",y="bill_length_mm")
```

<pre class="output-block">---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[28], line 1
----> 1 sns.boxplot(data=penguins,x="species",y="bill_length_mm")

NameError: name 'sns' is not defined
</pre>

Documentation for each plot type is on `seaborn`'s website, and it lists all required and optional arguments for each plot function: [seaborn :octicons-link-external-24:](https://seaborn.pydata.org/index.html){:target="_blank"}

### Changing plot aesthetics
We can do much more useful things than just setting the x and y axis, however! We will frequently want to group our data, e.g. by species, by sex, etc., and change the plot aesthtics to reflect these groups. To do this, we add an additional argument that specifies which column in our data frame that we want to group on. For example, to color the bars on our histogram based on species, we would use the `hue` argument: 


```python
sns.histplot(data=penguins, x="flipper_length_mm",hue="species")
```

<pre class="output-block">---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[29], line 1
----> 1 sns.histplot(data=penguins, x="flipper_length_mm",hue="species")

NameError: name 'sns' is not defined
</pre>

We can see we have changed the colors of the bars, but as they are overlapping it is difficult to read. If we dig into the documentation of the `histplot` function, we can find that there is also the `multiple` argument, which changes how overlapping bars behave...let's make them stack instead of overlap:


```python
sns.histplot(data=penguins, x="flipper_length_mm",hue="species",multiple="stack")
```

<pre class="output-block">---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[30], line 1
----> 1 sns.histplot(data=penguins, x="flipper_length_mm",hue="species",multiple="stack")

NameError: name 'sns' is not defined
</pre>

>Exercise: check the documentation page for the `scatterplot` function, and see if you can figure out how to make a scatter plot that shows bird bill length relative to body weight, with the *color* of each point corresponding to bird species, and the *shape* of the point corresponding to bird sex.


```python
sns.scatterplot(data=penguins, x='bill_length_mm', y='body_mass_g', hue='species', style='sex')
```

<pre class="output-block">---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[31], line 1
----> 1 sns.scatterplot(data=penguins, x='bill_length_mm', y='body_mass_g', hue='species', style='sex')

NameError: name 'sns' is not defined
</pre>

## Working with real life data: Data cleaning




```python
# This line downloads the file locally to the same folder as your notebook
!wget https://raw.githubusercontent.com/harvardinformatics/python-intensive/refs/heads/main/data/indiana_storms_full.csv

# This line stores the local file path as a Python string variable
storms_file = 'indiana_storms_full.csv'
```

<pre class="output-block">--2025-07-31 16:39:57--  https://raw.githubusercontent.com/harvardinformatics/python-intensive/refs/heads/main/data/indiana_storms_full.csv
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 185.199.110.133, 185.199.108.133, 185.199.109.133, ...
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|185.199.110.133|:443... connected.
HTTP request sent, awaiting response...
</pre>

<pre class="output-block">200 OK
Length: 952491 (930K) [text/plain]
Saving to: ‘indiana_storms_full.csv’


indiana_storms_full   0%[                    ]       0  --.-KB/s
</pre>

<pre class="output-block">
indiana_storms_full 100%[===================>] 930.17K  --.-KB/s    in 0.02s   

2025-07-31 16:39:57 (39.4 MB/s) - ‘indiana_storms_full.csv’ saved [952491/952491]
</pre>


```python
storms_df = pd.read_csv(storms_file)
storms_df.head()
```

<pre class="output-block">---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[33], line 1
----> 1 storms_df = pd.read_csv(storms_file)
      2 storms_df.head()

NameError: name 'pd' is not defined
</pre>

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

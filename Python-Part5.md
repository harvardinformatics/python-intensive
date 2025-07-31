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
Cell In[1], line 4
      2 import numpy as np
      3 import pandas as pd
----> 4 import seaborn as sns
      5 import matplotlib.pyplot as plt

ModuleNotFoundError: No module named 'seaborn'
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

<pre class="output-block">  species     island  bill_length_mm  bill_depth_mm  flipper_length_mm  \
0  Adelie  Torgersen            39.1           18.7              181.0   
1  Adelie  Torgersen            39.5           17.4              186.0   
2  Adelie  Torgersen            40.3           18.0              195.0   
3  Adelie  Torgersen             NaN            NaN                NaN   
4  Adelie  Torgersen            36.7           19.3              193.0   

   body_mass_g     sex  year  
0       3750.0    male  2007  
1       3800.0  female  2007  
2       3250.0  female  2007  
3          NaN     NaN  2007  
4       3450.0  female  2007
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

<pre class="output-block">       species     island  bill_length_mm  bill_depth_mm  flipper_length_mm  \
0       Adelie  Torgersen            39.1           18.7              181.0   
6       Adelie  Torgersen            38.9           17.8              181.0   
38      Adelie      Dream            37.6           19.3              181.0   
58      Adelie     Biscoe            36.5           16.6              181.0   
108     Adelie     Biscoe            38.1           17.0              181.0   
293  Chinstrap      Dream            58.0           17.8              181.0   
296  Chinstrap      Dream            42.4           17.3              181.0   

     body_mass_g     sex  year  
0         3750.0    male  2007  
6         3625.0  female  2007  
38        3300.0  female  2007  
58        2850.0  female  2008  
108       3175.0  female  2009  
293       3700.0  female  2007  
296       3600.0  female  2007
</pre>

<pre class="output-block">  species     island  bill_length_mm  bill_depth_mm  flipper_length_mm  \
0  Adelie  Torgersen            39.1           18.7              181.0   
1  Adelie  Torgersen            39.5           17.4              186.0   
4  Adelie  Torgersen            36.7           19.3              193.0   
5  Adelie  Torgersen            39.3           20.6              190.0   
6  Adelie  Torgersen            38.9           17.8              181.0   

   body_mass_g     sex  year  
0       3750.0    male  2007  
1       3800.0  female  2007  
4       3450.0  female  2007  
5       3650.0    male  2007  
6       3625.0  female  2007
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

<pre class="output-block">  species     island  bill_length_mm  bill_depth_mm  flipper_length_mm  \
0  Adelie  Torgersen            39.1           18.7              181.0   
1  Adelie  Torgersen            39.5           17.4              186.0   
5  Adelie  Torgersen            39.3           20.6              190.0   
6  Adelie  Torgersen            38.9           17.8              181.0   
7  Adelie  Torgersen            39.2           19.6              195.0   

   body_mass_g     sex  year  
0       3750.0    male  2007  
1       3800.0  female  2007  
5       3650.0    male  2007  
6       3625.0  female  2007  
7       4675.0    male  2007
</pre>

Pandas also has a helper function called `.isin()` that is similar to the `in` operator in base python. It allows you to filter a dataframe based on whether a column value is in a list of values.


```python
penguins[penguins['species'].isin(['Adelie', 'Gentoo'])]
```

<pre class="output-block">    species     island  bill_length_mm  bill_depth_mm  flipper_length_mm  \
0    Adelie  Torgersen            39.1           18.7              181.0   
1    Adelie  Torgersen            39.5           17.4              186.0   
2    Adelie  Torgersen            40.3           18.0              195.0   
3    Adelie  Torgersen             NaN            NaN                NaN   
4    Adelie  Torgersen            36.7           19.3              193.0   
..      ...        ...             ...            ...                ...   
271  Gentoo     Biscoe             NaN            NaN                NaN   
272  Gentoo     Biscoe            46.8           14.3              215.0   
273  Gentoo     Biscoe            50.4           15.7              222.0   
274  Gentoo     Biscoe            45.2           14.8              212.0   
275  Gentoo     Biscoe            49.9           16.1              213.0   

     body_mass_g     sex  year  
0         3750.0    male  2007  
1         3800.0  female  2007  
2         3250.0  female  2007  
3            NaN     NaN  2007  
4         3450.0  female  2007  
..           ...     ...   ...  
271          NaN     NaN  2009  
272       4850.0  female  2009  
273       5750.0    male  2009  
274       5200.0  female  2009  
275       5400.0    male  2009  

[276 rows x 8 columns]
</pre>

> Exercise: filter the dataframe to only keep the birds observed in the `year` 2007 and with a `bill_length_mm` greater than 38mm


```python
# Your code here

penguins[(penguins["year"] == 2007) & (penguins["bill_length_mm"] > 38)]
```

<pre class="output-block">       species     island  bill_length_mm  bill_depth_mm  flipper_length_mm  \
0       Adelie  Torgersen            39.1           18.7              181.0   
1       Adelie  Torgersen            39.5           17.4              186.0   
2       Adelie  Torgersen            40.3           18.0              195.0   
5       Adelie  Torgersen            39.3           20.6              190.0   
6       Adelie  Torgersen            38.9           17.8              181.0   
..         ...        ...             ...            ...                ...   
297  Chinstrap      Dream            48.5           17.5              191.0   
298  Chinstrap      Dream            43.2           16.6              187.0   
299  Chinstrap      Dream            50.6           19.4              193.0   
300  Chinstrap      Dream            46.7           17.9              195.0   
301  Chinstrap      Dream            52.0           19.0              197.0   

     body_mass_g     sex  year  
0         3750.0    male  2007  
1         3800.0  female  2007  
2         3250.0  female  2007  
5         3650.0    male  2007  
6         3625.0  female  2007  
..           ...     ...   ...  
297       3400.0    male  2007  
298       2900.0  female  2007  
299       3800.0    male  2007  
300       3300.0  female  2007  
301       4150.0    male  2007  

[89 rows x 8 columns]
</pre>

We can also filter based on strings, not just numbers! For this, you will want to use a string matching function from python, such as `.str.contains()` (which also a partial match), `.str.startswith()` (checks to see if a value starts with a given string), or others.


```python
penguins_filtered = penguins[penguins['species'].str.contains('Adel', case=False)]

penguins_filtered
```

<pre class="output-block">    species     island  bill_length_mm  bill_depth_mm  flipper_length_mm  \
0    Adelie  Torgersen            39.1           18.7              181.0   
1    Adelie  Torgersen            39.5           17.4              186.0   
2    Adelie  Torgersen            40.3           18.0              195.0   
3    Adelie  Torgersen             NaN            NaN                NaN   
4    Adelie  Torgersen            36.7           19.3              193.0   
..      ...        ...             ...            ...                ...   
147  Adelie      Dream            36.6           18.4              184.0   
148  Adelie      Dream            36.0           17.8              195.0   
149  Adelie      Dream            37.8           18.1              193.0   
150  Adelie      Dream            36.0           17.1              187.0   
151  Adelie      Dream            41.5           18.5              201.0   

     body_mass_g     sex  year  
0         3750.0    male  2007  
1         3800.0  female  2007  
2         3250.0  female  2007  
3            NaN     NaN  2007  
4         3450.0  female  2007  
..           ...     ...   ...  
147       3475.0  female  2009  
148       3450.0  female  2009  
149       3750.0    male  2009  
150       3700.0  female  2009  
151       4000.0    male  2009  

[152 rows x 8 columns]
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

<pre class="output-block">0    NaN
1    NaN
2    NaN
3    7.0
dtype: float64
</pre>

When using descriptive statistics and computational methods like `.sum()`, `.mean()`, pandas will ignore missing values and treat them like zero. 


```python
print(ser1.sum())

print(ser1.mean())
```

<pre class="output-block">5.0
2.5
</pre>

This behavior can be changed by using the `skipna` argument, which is `True` by default. If you set `skipna=False`, pandas will treat missing values as `NaN` and will not ignore them, resulting in the whole operation returning `NaN`.


```python
print(ser1.mean(skipna=False))
```

<pre class="output-block">nan
</pre>


One very useful function to know is how to get rid of rows with missing data in them, as including them can often cause errors in downstream analysis or skew your results. There is a convenient function built in to `pandas` that does this called `.dropna()`. By default, it will drop any row that has a missing value in any column. This may not always be what you want. You can specify which columns to look at using the `subset` arugment. 


```python
penguins_nona = penguins.dropna()

penguins_nona.info()
```

<pre class="output-block"><class 'pandas.core.frame.DataFrame'>
Index: 333 entries, 0 to 343
Data columns (total 8 columns):
 #   Column             Non-Null Count  Dtype  
---  ------             --------------  -----  
 0   species            333 non-null    object 
 1   island             333 non-null    object 
 2   bill_length_mm     333 non-null    float64
 3   bill_depth_mm      333 non-null    float64
 4   flipper_length_mm  333 non-null    float64
 5   body_mass_g        333 non-null    float64
 6   sex                333 non-null    object 
 7   year               333 non-null    int64  
dtypes: float64(4), int64(1), object(3)
memory usage: 23.4+ KB
</pre>


```python
penguins_nona_bill_len = penguins.dropna(subset=["bill_length_mm"])

penguins_nona_bill_len.info()
```

<pre class="output-block"><class 'pandas.core.frame.DataFrame'>
Index: 342 entries, 0 to 343
Data columns (total 8 columns):
 #   Column             Non-Null Count  Dtype  
---  ------             --------------  -----  
 0   species            342 non-null    object 
 1   island             342 non-null    object 
 2   bill_length_mm     342 non-null    float64
 3   bill_depth_mm      342 non-null    float64
 4   flipper_length_mm  342 non-null    float64
 5   body_mass_g        342 non-null    float64
 6   sex                333 non-null    object 
 7   year               342 non-null    int64  
dtypes: float64(4), int64(1), object(3)
memory usage: 24.0+ KB
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

<pre class="output-block">  species     island  bill_length_mm  bill_depth_mm  flipper_length_mm  \
0  Adelie  Torgersen            39.1           18.7              181.0   
1  Adelie  Torgersen            39.5           17.4              186.0   
2  Adelie  Torgersen            40.3           18.0              195.0   
3  Adelie  Torgersen             NaN            NaN                NaN   
4  Adelie  Torgersen            36.7           19.3              193.0   
5  Adelie  Torgersen            39.3           20.6              190.0   
6  Adelie  Torgersen            38.9           17.8              181.0   
7  Adelie  Torgersen            39.2           19.6              195.0   
8  Adelie  Torgersen            34.1           18.1              193.0   
9  Adelie  Torgersen            42.0           20.2              190.0   

   body_mass_g     sex  year  body_mass_z  
0       3750.0    male  2007    -0.563317  
1       3800.0  female  2007    -0.500969  
2       3250.0  female  2007    -1.186793  
3          NaN     NaN  2007          NaN  
4       3450.0  female  2007    -0.937403  
5       3650.0    male  2007    -0.688012  
6       3625.0  female  2007    -0.719186  
7       4675.0    male  2007     0.590115  
8       3475.0     NaN  2007    -0.906229  
9       4250.0     NaN  2007     0.060160
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

<pre class="output-block">  species     island  bill_length_mm  bill_depth_mm  flipper_length_mm  \
0  Adelie  Torgersen            39.1           18.7              181.0   
1  Adelie  Torgersen            39.5           17.4              186.0   
2  Adelie  Torgersen            40.3           18.0              195.0   
3  Adelie  Torgersen             NaN            NaN                NaN   
4  Adelie  Torgersen            36.7           19.3              193.0   

   body_mass_g     sex  year  body_mass_z   bill_volume  
0       3750.0    male  2007    -0.563317  10738.654055  
1       3800.0  female  2007    -0.500969   9392.592344  
2       3250.0  female  2007    -1.186793  10255.100899  
3          NaN     NaN  2007          NaN           NaN  
4       3450.0  female  2007    -0.937403  10736.693701
</pre>

### Summarizing your data

Another common task in data analysis is to calculate summary statistics of your data. Pandas as a number of helper methods like `.mean()`, `.median()`, `.count()`, `unique()`, etc. that can be used to describe your data. Pandas DataFrames has a handy `.describe()` method that will give you a summary of the data in each column. By default, it will calculate the count, mean, standard deviation, minimum, 25th percentile, median, 75th percentile, and maximum of each numerical column. However, if you give it the `include='all'` or `include='object'` argument, it will also include the count, unique, top, and freq (of top) of each categorical column.


```python
penguins.describe(include='all')
```

<pre class="output-block">       species  island  bill_length_mm  bill_depth_mm  flipper_length_mm  \
count      344     344      342.000000     342.000000         342.000000   
unique       3       3             NaN            NaN                NaN   
top     Adelie  Biscoe             NaN            NaN                NaN   
freq       152     168             NaN            NaN                NaN   
mean       NaN     NaN       43.921930      17.151170         200.915205   
std        NaN     NaN        5.459584       1.974793          14.061714   
min        NaN     NaN       32.100000      13.100000         172.000000   
25%        NaN     NaN       39.225000      15.600000         190.000000   
50%        NaN     NaN       44.450000      17.300000         197.000000   
75%        NaN     NaN       48.500000      18.700000         213.000000   
max        NaN     NaN       59.600000      21.500000         231.000000   

        body_mass_g   sex         year   body_mass_z   bill_volume  
count    342.000000   333   344.000000  3.420000e+02    342.000000  
unique          NaN     2          NaN           NaN           NaN  
top             NaN  male          NaN           NaN           NaN  
freq            NaN   168          NaN           NaN           NaN  
mean    4201.754386   NaN  2008.029070  1.246566e-16  10216.041172  
std      801.954536   NaN     0.818356  1.000000e+00   2468.270185  
min     2700.000000   NaN  2007.000000 -1.872618e+00   5782.155471  
25%     3550.000000   NaN  2007.000000 -8.127074e-01   8433.676950  
50%     4050.000000   NaN  2008.000000 -1.892307e-01   9954.426135  
75%     4750.000000   NaN  2009.000000  6.836368e-01  11537.641963  
max     6300.000000   NaN  2009.000000  2.616415e+00  18416.870649
</pre>


```python
penguins.describe(include='object')
```

<pre class="output-block">       species  island   sex
count      344     344   333
unique       3       3     2
top     Adelie  Biscoe  male
freq       152     168   168
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

<pre class="output-block"><pandas.core.groupby.generic.DataFrameGroupBy object at 0x00000230B3808AA0>
</pre>

We can see that on its own this is not especially useful, as grouping the DataFrame does not produce a new DataFrame (just this weird output message telling us that this is a `DataFrameGroupBy` object). In order to output a DataFrame, we need to pass the grouped DataFrame to some function that aggregates or transforms the data in each group.

We group our data, select the column we want to aggregate (in this case, `flipper_length_mm`) and apply the `.mean()` function to it:


```python
#Note the square brackets around the column name
penguins.groupby('species')['flipper_length_mm'].mean()
```

<pre class="output-block">species
Adelie       189.953642
Chinstrap    195.823529
Gentoo       217.186992
Name: flipper_length_mm, dtype: float64
</pre>

When we apply the `.mean()` method to the grouped dataframe, it returns a `Series` object with the mean flipper length of each species. The exact details of whether pandas returns a `groupby` object as a Series or a DataFrame gets a little technical; for our purposes, just know that you can make sure the returned object is converted to a DataFrame (which is usually most convenient) by using the `.reset_index` function:


```python
penguins.groupby('species')['flipper_length_mm'].mean().reset_index()
```

<pre class="output-block">     species  flipper_length_mm
0     Adelie         189.953642
1  Chinstrap         195.823529
2     Gentoo         217.186992
</pre>

We can group by multiple columns by passing a *list of column names* to the `.groupby()` method (and using `reset_index()` as before to have it output as a DataFrame): 


```python
penguins.groupby(['species', 'sex'])['flipper_length_mm'].mean().reset_index()
```

<pre class="output-block">     species     sex  flipper_length_mm
0     Adelie  female         187.794521
1     Adelie    male         192.410959
2  Chinstrap  female         191.735294
3  Chinstrap    male         199.911765
4     Gentoo  female         212.706897
5     Gentoo    male         221.540984
</pre>

So far we have just been applying the `.mean` function to our groups, but we can use other functions as well! One very useful function to know when grouping is `.size()`, which will return the number of rows in each group.


```python
penguins.groupby(['species', 'sex']).size()
```

<pre class="output-block">species    sex   
Adelie     female    73
           male      73
Chinstrap  female    34
           male      34
Gentoo     female    58
           male      61
dtype: int64
</pre>

>**Exercise:** Use grouping to answer the following question about the penguins dataset: Which island has the most Adelie penguins?
>
> **Hint:** Think about which order you should group by for the most readable output


```python
# Your code here

penguins.groupby(['species', 'island']).size()
```

<pre class="output-block">species    island   
Adelie     Biscoe        44
           Dream         56
           Torgersen     52
Chinstrap  Dream         68
Gentoo     Biscoe       124
dtype: int64
</pre>

> Now try your previous code with the order of the columns to group by switched. What changes?


```python
penguins.groupby(['island', 'species']).size()
```

<pre class="output-block">island     species  
Biscoe     Adelie        44
           Gentoo       124
Dream      Adelie        56
           Chinstrap     68
Torgersen  Adelie        52
dtype: int64
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

<pre class="output-block">     species     sex  body_mass_kg
0     Adelie  female      3.368836
1     Adelie    male      4.043493
2  Chinstrap  female      3.527206
3  Chinstrap    male      3.938971
4     Gentoo  female      4.679741
5     Gentoo    male      5.484836
</pre>

> **Exercise**: using the `.max()` function, find the largest bird on each island.


```python
penguins.groupby('island')['body_mass_g'].max()
```

<pre class="output-block">island
Biscoe       6300.0
Dream        4800.0
Torgersen    4700.0
Name: body_mass_g, dtype: float64
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

<pre class="output-block">  species     island  bill_length_mm  bill_depth_mm  flipper_length_mm  \
0  Adelie  Torgersen            39.1           18.7              181.0   
1  Adelie  Torgersen            39.5           17.4              186.0   
2  Adelie  Torgersen            40.3           18.0              195.0   
3  Adelie  Torgersen             NaN            NaN                NaN   
4  Adelie  Torgersen            36.7           19.3              193.0   

   body_mass_g     sex  year  
0       3750.0    male  2007  
1       3800.0  female  2007  
2       3250.0  female  2007  
3          NaN     NaN  2007  
4       3450.0  female  2007
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

<pre class="output-block">SYSTEM_WGETRC = c:/progra~1/wget/etc/wgetrc
syswgetrc = C:\bin\programs\gnuwin32/etc/wgetrc
--2025-07-31 12:19:32--  https://raw.githubusercontent.com/harvardinformatics/python-intensive/refs/heads/main/data/indiana_storms_full.csv
Resolving raw.githubusercontent.com... 185.199.108.133, 185.199.109.133, 185.199.110.133, ...
Connecting to raw.githubusercontent.com|185.199.108.133|:443... connected.
OpenSSL: error:140770FC:SSL routines:SSL23_GET_SERVER_HELLO:unknown protocol
Unable to establish SSL connection.
</pre>


```python
storms_df = pd.read_csv(storms_file)
storms_df.head()
```

<pre class="output-block">---------------------------------------------------------------------------
FileNotFoundError                         Traceback (most recent call last)
Cell In[33], line 1
----> 1 storms_df = pd.read_csv(storms_file)
      2 storms_df.head()

File C:\bin\miniforge3\Lib\site-packages\pandas\io\parsers\readers.py:1026, in read_csv(filepath_or_buffer, sep, delimiter, header, names, index_col, usecols, dtype, engine, converters, true_values, false_values, skipinitialspace, skiprows, skipfooter, nrows, na_values, keep_default_na, na_filter, verbose, skip_blank_lines, parse_dates, infer_datetime_format, keep_date_col, date_parser, date_format, dayfirst, cache_dates, iterator, chunksize, compression, thousands, decimal, lineterminator, quotechar, quoting, doublequote, escapechar, comment, encoding, encoding_errors, dialect, on_bad_lines, delim_whitespace, low_memory, memory_map, float_precision, storage_options, dtype_backend)
   1013 kwds_defaults = _refine_defaults_read(
   1014     dialect,
   1015     delimiter,
   (...)   1022     dtype_backend=dtype_backend,
   1023 )
   1024 kwds.update(kwds_defaults)
-> 1026 return _read(filepath_or_buffer, kwds)

File C:\bin\miniforge3\Lib\site-packages\pandas\io\parsers\readers.py:620, in _read(filepath_or_buffer, kwds)
    617 _validate_names(kwds.get("names", None))
    619 # Create the parser.
--> 620 parser = TextFileReader(filepath_or_buffer, **kwds)
    622 if chunksize or iterator:
    623     return parser

File C:\bin\miniforge3\Lib\site-packages\pandas\io\parsers\readers.py:1620, in TextFileReader.__init__(self, f, engine, **kwds)
   1617     self.options["has_index_names"] = kwds["has_index_names"]
   1619 self.handles: IOHandles | None = None
-> 1620 self._engine = self._make_engine(f, self.engine)

File C:\bin\miniforge3\Lib\site-packages\pandas\io\parsers\readers.py:1880, in TextFileReader._make_engine(self, f, engine)
   1878     if "b" not in mode:
   1879         mode += "b"
-> 1880 self.handles = get_handle(
   1881     f,
   1882     mode,
   1883     encoding=self.options.get("encoding", None),
   1884     compression=self.options.get("compression", None),
   1885     memory_map=self.options.get("memory_map", False),
   1886     is_text=is_text,
   1887     errors=self.options.get("encoding_errors", "strict"),
   1888     storage_options=self.options.get("storage_options", None),
   1889 )
   1890 assert self.handles is not None
   1891 f = self.handles.handle

File C:\bin\miniforge3\Lib\site-packages\pandas\io\common.py:873, in get_handle(path_or_buf, mode, encoding, compression, memory_map, is_text, errors, storage_options)
    868 elif isinstance(handle, str):
    869     # Check whether the filename is to be opened in binary mode.
    870     # Binary mode does not support 'encoding' and 'newline'.
    871     if ioargs.encoding and "b" not in ioargs.mode:
    872         # Encoding
--> 873         handle = open(
    874             handle,
    875             ioargs.mode,
    876             encoding=ioargs.encoding,
    877             errors=errors,
    878             newline="",
    879         )
    880     else:
    881         # Binary mode
    882         handle = open(handle, ioargs.mode)

FileNotFoundError: [Errno 2] No such file or directory: 'indiana_storms_full.csv'
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

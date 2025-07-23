---
title: "[Workshop] Python intensive, day 6"
description: "Analyzing a real dataset: Indiana storms."
authors:
    - Danielle Khost
    - Lei Ma
---

# Python intensive, day 6

## Putting it all together: exploring storm data

For our final section, we are going to do some exploratory analysis of a real world dataset, coding in pairs or groups as we did on the previous days. There are several different "paths" you can choose to follow based on what you are interested in working on, so either come to a consensus within your group, or group up based on shared interest! First, let's download our data:


```python
# This line downloads the file locally to the same folder as your notebook
!wget https://raw.githubusercontent.com/harvardinformatics/python-intensive/refs/heads/main/data/indiana_storms_full.csv

# This line stores the local file path as a Python string variable
storms_file = 'indiana_storms_full.csv'

```


```python
import pandas as pd
storms_df = pd.read_csv(storms_file)
storms_df.head()
```


```python
storms_df.info()
```

## Data Cleaning: subsetting columns

This is a file that contains data from the National Weather Service. It contains data on storm events in the state of Indiana in 2015. There is quite a lot of information in there with 50 columns in the dataset, so before we do any analysis let's do a bit of cleanup! 

We are primarily interested in type of storm event "EVENT_TYPE", the county in which the event occurred "CZ_NAME", and the time of the event "BEGIN_DATE_TIME", "END_DATE_TIME", "CZ_TIMEZONE". Let's also throw in there "BEGIN_LOCATION", "END_LOCATION", "BEGIN_LAT", "BEGIN_LON", "END_LAT", and "END_LON" just in case. So the first thing we need to do is subset the data to only include these columns.


```python
storms_df = storms_df[["EVENT_TYPE", "CZ_NAME", "BEGIN_DATE_TIME", "END_DATE_TIME", "CZ_TIMEZONE",  "BEGIN_LOCATION", "END_LOCATION", "BEGIN_LAT", "BEGIN_LON", "END_LAT", "END_LON"]]
```

Now, let's check if there are any missing values in the columns we are interested in. If there are, we should remove the rows with missing values.


```python
storms_df.info()
```

Only some storm events have a begin and end location, but at least there aren't any that only have a begin and not and end. Data looks good! The next thing we need to do is to convert the "BEGIN_DATE_TIME" and "END_DATE_TIME" columns to datetime objects. This will make it easier to work with these columns later on.

### Working with dates and times

>**Question:** How many hours are there between 9:00 AM and 10:00 AM on a given date? 

**Answer:** Any number between 0 and 13, depending on the time zones of the two locations.

Time, as we all know, is a human construct that is on its face numerical, but is also more complex than simple numbers. Consider all that we do with dates and times: we want to compare time, do arithmetic to find time intervals, aggregate by year, month, day, day of the week, etc. Time consists of many different units and cannot be simply added or coded. Consider that there are a variable number of days in a month, and some months have different number of days on certain years (leap days). Then, we might want to measure durations of time, or keep track of time stamps specific to a location and date. These require computers to think of time in different ways. 

Pandas has an implementation of datetime objects called `pd.datetime`. Consider this akin to the `str` object for strings, or the `int` object for integers. This object has a lot of built-in functionality that makes it easy to work with dates and times. But before we learn how to convert data to this object type, let's go over a few basic tips for how to record your time data. 

* If you just want to record the date, use the format `YYYY-MM-DD`. When you convert to a `pd.datetime` object, it will automatically set the time to midnight with no time zone information. This is called a "naive" datetime object.
* If you need to record a timestamp - e.g. the time and date something happened - use the format `YYYY-MM-DD HH:MM:SS+0500`. This is the ISO 8601 standard format for datetime objects. The `+0500` is the time zone offset from GMT. When pandas parses this string, it will create what is called an "aware" datetime object. ***Good data practice is to always record your times in this format and to always include the time zone offset*** unless you are absolutely sure that A. Everything happens in the same time zone and you'll never have to compare to another dataset, and B. None of your data will be affected by daylight savings time.
* If you need to record a time series, you want to record the time a `YYYY-MM-DD HH:MM:SS` (ISO 8601 again) but import the data as **time deltas**, aka `pd.Timedelta`. This is a special type of datetime object that represents the difference between two times. This is useful if the duration, and not the specific time of day, matters the most.

Pandas is an essential library for time series analysis that many other libraries build upon. See the docs for more information on how pandas handles date [time objects :octicons-link-external-24:](https://pandas.pydata.org/docs/user_guide/timeseries.html){:target="_blank"} and [time deltas :octicons-link-external-24:](https://pandas.pydata.org/docs/user_guide/timedeltas.html){:target="_blank"}. 

Even if you aren't doing time series analysis, you will find it useful to import any column of dates or times as a datetime object, as it will provide you with a lot of useful functionality. For example:

* Pandas can automatically parse human readable dates and times written in various formats into a standardized `datetime` object. [docs :octicons-link-external-24:](https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html){:target="_blank"}
* You can extract various components of the date/time for analysis or printing purposes. See the list of attributes and method of the `pd.Timestamp` class [here :octicons-link-external-24:](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.html){:target="_blank"}, which include `day_of_week`, `day_of_year`, `weekofyear`, `.day_name()`, etc. 
* You can perform calculations on dates and times, such as converting between time zones, finding the difference (**delta**) between two times, resampling the frequency of a time series, or finding the time that is a certain duration away from a given time. 
* You can control how the date is displayed when you print it out or export your data by using string format codes specific for datetime objects. [docs :octicons-link-external-24:](https://docs.python.org/3/library/datetime.html#format-codes){:target="_blank"} 

Here's an example of pandas in action with datetime objects: [link :octicons-link-external-24:](https://pandas.pydata.org/docs/getting_started/intro_tutorials/09_timeseries.html){:target="_blank"}

```python
# Convert all date time columns to datetime objects with correct timezone parsing
# I wrote a regex to extract just the number from the timezone column and then made it an ISO8601 compliant timezone string
# Pandas does not support multiple time zones in the same column, so we will convert all times to UTC and then convert to one of the local time zones
storms_df['BEGIN_DATE_TIME'] = pd.to_datetime(storms_df["BEGIN_DATE_TIME"]+"-0"+storms_df["CZ_TIMEZONE"].str.extract(r'([0-9]+)')[0]+"00", format="mixed", utc=True).dt.tz_convert("-05:00")
storms_df['END_DATE_TIME'] = pd.to_datetime(storms_df["END_DATE_TIME"]+"-0"+storms_df["CZ_TIMEZONE"].str.extract(r'([0-9]+)')[0]+"00", format="mixed", utc=True).dt.tz_convert("-05:00")
```

Here's what the times look like now:


```python
storms_df["BEGIN_DATE_TIME"].head()
```

```python
storms_df.info()
```

## Warm-up exercises

Here are some warm-up exercises to get started working with data that is a mix of categorical and datetime data. One helpful tip to working with datetime objects is to get the series of the datetime object and then use the `.dt` accessor to access the datetime properties. You can find all the properties of the datetime object [here :octicons-link-external-24:](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.html){:target="_blank"}.


```python
# example of getting an attribute of a datetime object

storms_df["END_DATE_TIME"].dt.day_of_year
```

```python
# example of using a method of a datetime object

storms_df["END_DATE_TIME"].dt.month_name()
```

The next three exercises are one-liners what will use the method `.value_counts()` to get the number of rows for each unique value in a column. This is a useful method to get a sense of the distribution of the data in a column. Below, we demonstrate by counting the number of each event type. (Compare this to the `groupby().size()` method we used last time)


```python
storms_df["EVENT_TYPE"].value_counts()
```

>**Exercise:** Are storms more common on weekends or weekdays? YES/NO. Display your answer by counting the number of events that happend on each day of the week. Don't worry about sorting the days of the week, just display the counts. Look at the datetime object documentation to see how to get the day of the week from the `.dt` accessor. 


```python
# display the number of events (rows) for each day of the week
# Your code here

storms_df['BEGIN_DATE_TIME'].dt.day_name().value_counts()
```

>**Exercise:** Which events tend to span more than one county? Display the counts of each event type that spans more than one county. (Hint: Events which span more than one county will have non-null values for `BEGIN_LOCATION` and `END_LOCATION`.) 


```python
storms_df[~storms_df["BEGIN_LOCATION"].isna()]["EVENT_TYPE"].value_counts()
```

>**Exercise:** Which events tend to be multi-day events? Display the counts of each event type that has a duration of more than 1 day (24 hours).
>
>You will need to use the `pd.Timedelta()` function in your filtering criteria. Docs [here :octicons-link-external-24:](https://pandas.pydata.org/docs/user_guide/timedeltas.html){:target="_blank"} and [here :octicons-link-external-24:](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.html#pandas.Timedelta){:target="_blank"}

```python
# Your code here
# Find duration of events

storms_df['EVENT_DURATION'] = storms_df["END_DATE_TIME"] - storms_df["BEGIN_DATE_TIME"]

# filter for events that last more than one day and count them
storms_df[storms_df['EVENT_DURATION'] > pd.Timedelta(days=1)]["EVENT_TYPE"].value_counts()
```

>**Exercise:** Create two lists: a list of all county names and a list of all event types. How many counties and event types are there? You will be using the Series methods `.unique()` and `.tolist()` here. 


```python
# Your code here

county_list = storms_df["CZ_NAME"].unique().tolist()
print(county_list)
print(f"There are {len(county_list)} counties in the dataset")
event_list = storms_df["EVENT_TYPE"].unique().tolist()
print(event_list)
print(f"There are {len(event_list)} event types in the dataset")
```

>**Exercise:** Function-writing warmup. Write a function called `get_event_county` that takes as input the storms dataframe object, a county name (as a string), and an event type (as a string). The function should return a dataframe that contains only that county and event type.
>
> This function is ideally a one-liner that filters the dataframe based on two criteria. Remember to enclose each condition in `()` and use the `&` operator to combine them.


```python
# Your code here

def get_event_county(storms, county, event):
    return storms[(storms["EVENT_TYPE"] == event) & (storms["CZ_NAME"] == county)]
```


```python
# test your code
# should return a dataframe with 7 rows
get_event_county(storms_df, "ELKHART", "Thunderstorm Wind")
```

Now that we have imported our data, cleaned it up and begun to explore it, let's split off into groups! We have a few paths we can take:

1. A guided path: We will guide you through writing functions that summarize and print the data in different ways. This will help you practice writing functions, filtering data, and practice a tiny bit of plotting. 
2. A few self-guided exploratory questions that you can approach however you want, but focus on different skills:
    * Question 1: What is the most dangerous county in Indiana? We provide a separate table of county info so you can normalize the data by county area. You will need to learn how to merge two dataframes together.
    * Question 2: What is the best time to visit Indiana if you want to take cool pictures of clouds? This will help you practice summarizing data and, depending on how you approach it, work with date time objects of various duration. 
    * Question 3: Create a plot that compares the duration in hours of each common event type. This will help you practice creating new columns and plotting data. 

## Path 1: function writing practice

1. Write a function called `storm_by_county` that takes as input the storms object, a **LIST** of county names, and returns a dataframe of all of the events that occurred in a given county and the date they began. Include an optional argument `storm_type` that by default is `None` and includes all event types, but if given a list, only includes those events.


```python
# your code here

def storm_by_county(storms, county, storm_type=None):
    if storm_type:
        matches = storms[(storms['CZ_NAME'].isin(county)) & (storms['EVENT_TYPE'].isin(storm_type))]
    else:
        matches = storms[(storms['CZ_NAME'].isin(county))]
    
    return matches
```


```python
# test your function
# should return 8 rows of data
storm_by_county(storms_df, ["OHIO"])
```

```python
# test your function
# should return 11 rows of data

storm_by_county(storms_df, ["ELKHART", "ST. JOSEPH"], ["Thunderstorm Wind"])
```

2. Create a function called `display_storms` that takes a storms object, iterates through each row, and prints out each event as a sentence, including the event type, the county, and the date and time of the event. This exercise helps with iterating over data. An example output would be: "A thunderstorm occurred in Marion County on 2015-06-15 13:45:00". (as a bonus, you can try and format the date and time to be more human-readable)

**HINT:** You will need to use the `.iterrows()` method


```python
# your code here

def display_storms(storms):
    for index, event in storms.iterrows():
        print("A", event["EVENT_TYPE"], "occurred on", event["BEGIN_DATE_TIME"], "in", event["CZ_NAME"], "county.")
```

3. Test your function by:
- Printing all storm events in TIPPECANOE county
- Printing all "Flood" and "Flash Flood" events in the following counties: MARION, MONROE, SPENCER, VERMILLION
- Print all "Tornado" events *in the whole state*, i.e. all the counties.


```python
## Test your storm_by_county function

# 3.1: Display all storm events in TIPPECANOE county.
print("--- 3.1 ---")
display_storms(storm_by_county(storms_df, ["TIPPECANOE"]))

# 3.2: Display all Flood and Flash Flood events in the following counties: MARION, MONROE, SPENCER, VERMILLION
print("--- 3.2 ---")
counties_to_check = ["MARION", "MONROE", "SPENCER", "VERMILLION"]
storm_types = ["Flood", "Flash Flood"]

display_storms(storm_by_county(storms_df, counties_to_check, storm_types))

# 3.3: Display all Tornado events that occurred in the state.
print("--- 3.3 ---")
county_list = storms_df["CZ_NAME"].unique()
display_storms(storm_by_county(storms_df, county_list, storm_type=["Tornado"]))
```

4. Make a histogram that displays the count of the events which contain "flood" in the following counties: ["MARION", "MONROE", "SPENCER", "VERMILLION", "TIPPECANOE"]. The x axis will be the different "flood" event types, and the color of the bar will be the county. The y axis will be the count of the events.

HINT: First, you will have to find a way to get all values of `EVENT_TYPE` that contain the word "flood" (case insensitive) and make that into a list. Then, you can pass that list and your county list to your `storm_by_county()` function. There are many ways to get the values that contain "flood". One way is to use `str.contains()`, but will involve chaining a few methods and doing some dataframe subsetting. Another way is to use a for loop and an if statement and may be more readable. 

When you make a histogram using `sns.histplot()`, you can use the `multiple='dodge'` argument to make the bars side by side.


```python
# import seaborn
import seaborn as sns

# str.contains method
storm_list = storms_df["EVENT_TYPE"][storms_df["EVENT_TYPE"].str.contains("flood", case=False)].unique().tolist()

# for loop method
storm_list = []
for event in storms_df["EVENT_TYPE"].dropna().unique():
    if "flood" in event.lower():
        storm_list.append(event)

# make a subset
storms_subset = storm_by_county(storms_df, county=["MARION", "MONROE", "SPENCER", "VERMILLION", "TIPPECANOE"], storm_type = storm_list)

# plot the subset
sns.histplot(storms_subset, x="EVENT_TYPE", hue="CZ_NAME", multiple="dodge", shrink=0.8)
```

5. Write another function called `summarise_storms` which takes as input the storms object you created, a list of counties, and an optional list of `storm_type` that displays only certain storm types (aka the same arguments as `storm_by_county`). Instead of returning every event, it returns a dataframe summarizing the number of occurences of each event in those counties. **HINT** You may want to use your previous function `storm_by_county` to avoid repeating code!


```python
## your code here

# def storm_by_county(INSERT ARGUMENTS):

def summarise_storms(storms, county, storm_type=None):
  df = storm_by_county(storms, county, storm_type).groupby(["CZ_NAME","EVENT_TYPE"]).size().reset_index()
  
  return df

```

5. Test your function by:
- Printing the number of all events in PIKE county without printing information about each one
- Printing the total number of "Thunderstorm Wind" events in the following counties: ELKHART, LA PORTE, BOONE


```python
## Test your modified storm_by_county function

# 5.1 Display the number of all events in PIKE county
print("--- 5.1 ---")
print(summarise_storms(storms_df, ["PIKE"]))

# 5.2 Display the number of Thunderstorm Wind events in the following counties: ELKHART, LA PORTE, BOONE
print("--- 5.2 ---")
print(summarise_storms(storms_df, ["ELKHART", "LA PORTE", "BOONE"], ["Thunderstorm Wind"]))
```

6. Use your function to summarize the total counts of each weather event in each county.


```python
# your code here

all_weather = storms_df["EVENT_TYPE"].unique().tolist()
all_counties = storms_df["CZ_NAME"].unique().tolist()

summarise_storms(storms_df, all_counties, all_weather)
```

## Self-guided exploratory questions

Here are a few questions we've come up with that can be approached in multiple different ways.

**Question 1:** What is the most dangerous county in Indiana, assuming danger only comes from the storm events? You will need to account for the area of each county to answer this question. We've provided code to get the table from wikipedia that lists county information. 


```python
!pip install lxml
county_info = pd.read_html("https://en.wikipedia.org/wiki/List_of_counties_in_Indiana")
county_info = county_info[1]
```

```python
county_info[["County", "Area[3][12]"]]
```

```python
# cleaning county_info
county_info["County"] = county_info["County"].str.replace(" County", "").str.upper()
county_info["Area_sq_mi"] = pd.to_numeric(county_info["Area[3][12]"].str.extract(r'([0-9,]+)')[0])

# merge the two dataframes
storms_merged = pd.merge(storms_df, county_info, left_on="CZ_NAME", right_on="County")
```


```python
# grouping by county and area
df = storms_merged.groupby(["CZ_NAME", "Area_sq_mi"])["EVENT_TYPE"].count().reset_index()
print(df.head())

# normalizing number of events by area
df["normalized"] = df["EVENT_TYPE"] / df["Area_sq_mi"]

# sorting by normalized value
df.sort_values("normalized", ascending=False)
```

**Question 2:** What is the best time to visit Indiana if you want to take cool pictures of clouds? The main idea of this question is to summarize the data in such a way that you can tell which month or week or your choice of span of days has the highest concentration of events of interest. 


```python
# decide which weather events probably have cool clouds
cool_clouds = ["Thunderstorm wind", "Tornado", "Lightning", "Heavy Rain"]

# filter for cool clouds
df_clouds = storms_df[storms_df["EVENT_TYPE"].isin(cool_clouds)]

# group by month and number of events
df_clouds.groupby(df_clouds["BEGIN_DATE_TIME"].dt.month)["EVENT_TYPE"].count().reset_index()
```

**Question 3:** Create a plot that compares the duration in hours of each common event type. Some events occur only infrequently, so your first step would be to filter those out. Then, you will need to decide what type of plot to make. Take a look at the [seaborn gallery :octicons-link-external-24:](https://seaborn.pydata.org/examples/index.html){:target="_blank"}. If you are having trouble deciding how to represent your data, take a look at this [infographic :octicons-link-external-24:](https://github.com/Financial-Times/chart-doctor/blob/main/visual-vocabulary/poster.png){:target="_blank"}

```python
# get event duration. We've already done this, but the code is reproduced before

storms_df["EVENT_DURATION"] = storms_df["END_DATE_TIME"] - storms_df["BEGIN_DATE_TIME"]

# filter out events which only occurred <10 times in the year

storms_filtered = storms_df.groupby("EVENT_TYPE").filter(lambda x: len(x) > 10)

# group by event type and calculate average duration

print(storms_filtered.groupby("EVENT_TYPE")["EVENT_DURATION"].mean())


```

```python
storms_filtered.groupby("EVENT_TYPE")["EVENT_DURATION"].describe()
```

```python
# plot the distribution of event durations as a stripplot with points using seaborn
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates

storms_no_flood = storms_filtered[~storms_filtered["EVENT_TYPE"].str.contains("Flood")]

# convert EVENT_DURATION to number of hours
storms_no_flood["EVENT_DURATION_HOURS"] = storms_no_flood["EVENT_DURATION"].dt.total_seconds() / 3600

fig, ax = plt.subplots()

ax = sns.stripplot(data=storms_no_flood, x="EVENT_DURATION_HOURS", y="EVENT_TYPE")

plt.show()
```

```python
# plot the distribution of event durations as a stripplot with points using seaborn
# separately plotting EVENT_TYPE = flood

fig, ax = plt.subplots()

storms_flood_only = storms_filtered[storms_filtered["EVENT_TYPE"].str.contains("Flood")]

# convert EVENT_DURATION to number of hours
storms_flood_only["EVENT_DURATION_HOURS"] = storms_flood_only["EVENT_DURATION"].dt.total_seconds() / 3600

ax = sns.stripplot(data=storms_flood_only, x="EVENT_DURATION_HOURS", y="EVENT_TYPE")

plt.show()
```

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

</style>

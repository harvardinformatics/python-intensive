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
!wget https://informatics.fas.harvard.edu/workshops/python-intensive/data/indiana_storms_full.csv

# This line stores the local file path as a Python string variable
storms_file = 'indiana_storms_full.csv'

```


```python
import pandas as pd
storms_df = pd.read_csv(storms_file)
storms_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>BEGIN_YEARMONTH</th>
      <th>BEGIN_DAY</th>
      <th>BEGIN_TIME</th>
      <th>END_YEARMONTH</th>
      <th>END_DAY</th>
      <th>END_TIME</th>
      <th>EPISODE_ID</th>
      <th>EVENT_ID</th>
      <th>STATE</th>
      <th>STATE_FIPS</th>
      <th>...</th>
      <th>END_RANGE</th>
      <th>END_AZIMUTH</th>
      <th>END_LOCATION</th>
      <th>BEGIN_LAT</th>
      <th>BEGIN_LON</th>
      <th>END_LAT</th>
      <th>END_LON</th>
      <th>EPISODE_NARRATIVE</th>
      <th>EVENT_NARRATIVE</th>
      <th>DATA_SOURCE</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>201501</td>
      <td>8</td>
      <td>1700</td>
      <td>201501</td>
      <td>9</td>
      <td>1200</td>
      <td>91570</td>
      <td>548696</td>
      <td>INDIANA</td>
      <td>18</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>A quick-moving Alberta Clipper brought a quick...</td>
      <td>Periods of snow during the late afternoon hour...</td>
      <td>CSV</td>
    </tr>
    <tr>
      <th>1</th>
      <td>201501</td>
      <td>5</td>
      <td>2200</td>
      <td>201501</td>
      <td>6</td>
      <td>830</td>
      <td>92441</td>
      <td>555468</td>
      <td>INDIANA</td>
      <td>18</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>An Alberta Clipper brought a quick round of sn...</td>
      <td>Snowfall accumulation observations ranged from...</td>
      <td>CSV</td>
    </tr>
    <tr>
      <th>2</th>
      <td>201501</td>
      <td>5</td>
      <td>2200</td>
      <td>201501</td>
      <td>6</td>
      <td>900</td>
      <td>92441</td>
      <td>555469</td>
      <td>INDIANA</td>
      <td>18</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>An Alberta Clipper brought a quick round of sn...</td>
      <td>Snowfall accumulation observations ranged from...</td>
      <td>CSV</td>
    </tr>
    <tr>
      <th>3</th>
      <td>201501</td>
      <td>5</td>
      <td>2200</td>
      <td>201501</td>
      <td>6</td>
      <td>900</td>
      <td>92441</td>
      <td>555470</td>
      <td>INDIANA</td>
      <td>18</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>An Alberta Clipper brought a quick round of sn...</td>
      <td>Snowfall accumulation observations ranged from...</td>
      <td>CSV</td>
    </tr>
    <tr>
      <th>4</th>
      <td>201501</td>
      <td>5</td>
      <td>2215</td>
      <td>201501</td>
      <td>6</td>
      <td>930</td>
      <td>92441</td>
      <td>555471</td>
      <td>INDIANA</td>
      <td>18</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>An Alberta Clipper brought a quick round of sn...</td>
      <td>Snowfall accumulation of 5.5 inches was report...</td>
      <td>CSV</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 51 columns</p>
</div>




```python
storms_df.info()
```

<pre class="output-block">
&lt;class 'pandas.core.frame.DataFrame'&gt;
RangeIndex: 1315 entries, 0 to 1314
Data columns (total 51 columns):
 #   Column              Non-Null Count  Dtype  
---  ------              --------------  -----  
 0   BEGIN_YEARMONTH     1315 non-null   int64  
 1   BEGIN_DAY           1315 non-null   int64  
 2   BEGIN_TIME          1315 non-null   int64  
 3   END_YEARMONTH       1315 non-null   int64  
 4   END_DAY             1315 non-null   int64  
 5   END_TIME            1315 non-null   int64  
 6   EPISODE_ID          1315 non-null   int64  
 7   EVENT_ID            1315 non-null   int64  
 8   STATE               1315 non-null   object 
 9   STATE_FIPS          1315 non-null   int64  
 10  YEAR                1315 non-null   int64  
 11  MONTH_NAME          1315 non-null   object 
 12  EVENT_TYPE          1315 non-null   object 
 13  CZ_TYPE             1315 non-null   object 
 14  CZ_FIPS             1315 non-null   int64  
 15  CZ_NAME             1315 non-null   object 
 16  WFO                 1315 non-null   object 
 17  BEGIN_DATE_TIME     1315 non-null   object 
 18  CZ_TIMEZONE         1315 non-null   object 
 19  END_DATE_TIME       1315 non-null   object 
 20  INJURIES_DIRECT     1315 non-null   int64  
 21  INJURIES_INDIRECT   1315 non-null   int64  
 22  DEATHS_DIRECT       1315 non-null   int64  
 23  DEATHS_INDIRECT     1315 non-null   int64  
 24  DAMAGE_PROPERTY     1011 non-null   object 
 25  DAMAGE_CROPS        1009 non-null   object 
 26  SOURCE              1315 non-null   object 
 27  MAGNITUDE           577 non-null    float64
 28  MAGNITUDE_TYPE      390 non-null    object 
 29  FLOOD_CAUSE         246 non-null    object 
 30  CATEGORY            0 non-null      float64
 31  TOR_F_SCALE         24 non-null     object 
 32  TOR_LENGTH          24 non-null     float64
 33  TOR_WIDTH           24 non-null     float64
 34  TOR_OTHER_WFO       3 non-null      object 
 35  TOR_OTHER_CZ_STATE  3 non-null      object 
 36  TOR_OTHER_CZ_FIPS   3 non-null      float64
 37  TOR_OTHER_CZ_NAME   3 non-null      object 
 38  BEGIN_RANGE         871 non-null    float64
 39  BEGIN_AZIMUTH       871 non-null    object 
 40  BEGIN_LOCATION      871 non-null    object 
 41  END_RANGE           871 non-null    float64
 42  END_AZIMUTH         871 non-null    object 
 43  END_LOCATION        871 non-null    object 
 44  BEGIN_LAT           871 non-null    float64
 45  BEGIN_LON           871 non-null    float64
 46  END_LAT             871 non-null    float64
 47  END_LON             871 non-null    float64
 48  EPISODE_NARRATIVE   1315 non-null   object 
 49  EVENT_NARRATIVE     1079 non-null   object 
 50  DATA_SOURCE         1315 non-null   object 
dtypes: float64(11), int64(15), object(25)
memory usage: 524.1+ KB
</pre>

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

<pre class="output-block">
&lt;class 'pandas.core.frame.DataFrame'&gt;
RangeIndex: 1315 entries, 0 to 1314
Data columns (total 11 columns):
 #   Column           Non-Null Count  Dtype  
---  ------           --------------  -----  
 0   EVENT_TYPE       1315 non-null   object 
 1   CZ_NAME          1315 non-null   object 
 2   BEGIN_DATE_TIME  1315 non-null   object 
 3   END_DATE_TIME    1315 non-null   object 
 4   CZ_TIMEZONE      1315 non-null   object 
 5   BEGIN_LOCATION   871 non-null    object 
 6   END_LOCATION     871 non-null    object 
 7   BEGIN_LAT        871 non-null    float64
 8   BEGIN_LON        871 non-null    float64
 9   END_LAT          871 non-null    float64
 10  END_LON          871 non-null    float64
dtypes: float64(4), object(7)
memory usage: 113.1+ KB
</pre>

Only some storm events have a begin and end location, but at least there aren't any that only have a begin and not and end. Data looks good! The next thing we need to do is to convert the "BEGIN_DATE_TIME" and "END_DATE_TIME" columns to datetime objects. This will make it easier to work with these columns later on.

### Working with dates and times

>**Question:** How many hours are there between 9:00 AM and 10:00 AM on a given date? 

**Answer:** Any number between 0 and 13, depending on the time zones of the two locations.

Time, as we all know, is a human construct that is on its face numerical, but is also more complex than simple numbers. Consider all that we do with dates and times: we want to compare time, do arithmetic to find time intervals, aggregate by year, month, day, day of the week, etc. Time consists of many different units and cannot be simply added or coded. Consider that there are a variable number of days in a month, and some months have different number of days on certain years (leap days). Then, we might want to measure durations of time, or keep track of time stamps specific to a location and date. These require computers to think of time in different ways. 

Pandas has an implementation of datetime objects called `pd.datetime`. Consider this akin to the `str` object for strings, or the `int` object for integers. This object has a lot of built-in functionality that makes it easy to work with dates and times. But before we learn how to convert data to this object type, let's go over a few basic tips for how to record your time data. 

* If you just want to record the date, use the format `YYYY-MM-DD`. When you convert to a `pd.datetime` object, it will automatically set the time to midnight with no time zone information. This is called a "naive" datetime object.
* If you need to record a timestamp - e.g. the time and date something happened - use the format `YYYY-MM-DD HH:MM:SS+0500`. This is the ISO 8601 standard format for datetime objects. The `+0500` is the time zone offset from GMT. When pandas parses this string, it will create what is called an "aware" datetime object. ***Good data practice is to always record your times in this format and to always include the time zone offset*** unless you are absolutely sure that A. Everything happens in the same time zone and you'll never have to compare to another dataset, and B. None of your data will be affected by daylight savings time.
* If you need to record a time series, you want to record the time a `YYYY-MM-DD HH:MM:SS` (ISO 8601 again) but import the data as **time deltas**, aka `pd.Timedelta`. This is a special type of datetime object that represents the difference between two times. This is useful if the duration, and not the specific time of day, matters the most.

Pandas is an essential library for time series analysis that many other libraries build upon. See the docs for more information on how pandas handles date [time objects](https://pandas.pydata.org/docs/user_guide/timeseries.html) and [time deltas](https://pandas.pydata.org/docs/user_guide/timedeltas.html). 

Even if you aren't doing time series analysis, you will find it useful to import any column of dates or times as a datetime object, as it will provide you with a lot of useful functionality. For example:

* Pandas can automatically parse human readable dates and times written in various formats into a standardized `datetime` object. [docs](https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html)
* You can extract various components of the date/time for analysis or printing purposes. See the list of attributes and method of the `pd.Timestamp` class [here](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.html), which include `day_of_week`, `day_of_year`, `weekofyear`, `.day_name()`, etc. 
* You can perform calculations on dates and times, such as converting between time zones, finding the difference (**delta**) between two times, resampling the frequency of a time series, or finding the time that is a certain duration away from a given time. 
* You can control how the date is displayed when you print it out or export your data by using string format codes specific for datetime objects. [docs](https://docs.python.org/3/library/datetime.html#format-codes) 

Here's an example of pandas in action with datetime objects: [link](https://pandas.pydata.org/docs/getting_started/intro_tutorials/09_timeseries.html)


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




<pre class="output-block">
0   2015-01-08 17:00:00-05:00
1   2015-01-05 22:00:00-05:00
2   2015-01-05 22:00:00-05:00
3   2015-01-05 22:00:00-05:00
4   2015-01-05 22:15:00-05:00
Name: BEGIN_DATE_TIME, dtype: datetime64[ns, UTC-05:00]
</pre>

## Warm-up exercises

Here are some warm-up exercises to get started working with data that is a mix of categorical and datetime data. One helpful tip to working with datetime objects is to get the series of the datetime object and then use the `.dt` accessor to access the datetime properties. You can find all the properties of the datetime object [here](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.html).


```python
# example of getting an attribute of a datetime object

storms_df["END_DATE_TIME"].dt.day_of_year
```




<pre class="output-block">
0         9
1         6
2         6
3         6
4         6
       ... 
1310    357
1311    357
1312    365
1313    357
1314      1
Name: END_DATE_TIME, Length: 1315, dtype: int32
</pre>

```python
# example of using a method of a datetime object

storms_df["END_DATE_TIME"].dt.month_name()
```




<pre class="output-block">
0        January
1        January
2        January
3        January
4        January
          ...   
1310    December
1311    December
1312    December
1313    December
1314     January
Name: END_DATE_TIME, Length: 1315, dtype: object
</pre>

The next three exercises are one-liners what will use the method `.value_counts()` to get the number of rows for each unique value in a column. This is a useful method to get a sense of the distribution of the data in a column. Below, we demonstrate by counting the number of each event type. (Compare this to the `groupby().size()` method we used last time)


```python
storms_df["EVENT_TYPE"].value_counts()
```




<pre class="output-block">
EVENT_TYPE
Thunderstorm Wind          383
Hail                       187
Winter Weather             162
Heavy Snow                 131
Flood                      125
Flash Flood                121
Dense Fog                   40
Winter Storm                33
Heavy Rain                  27
Extreme Cold/Wind Chill     26
Tornado                     24
Heat                        15
Cold/Wind Chill             12
Excessive Heat               6
Frost/Freeze                 6
Strong Wind                  5
Lightning                    3
Ice Storm                    3
Lake-Effect Snow             2
High Wind                    2
Funnel Cloud                 1
Blizzard                     1
Name: count, dtype: int64
</pre>

>**Exercise:** Are storms more common on weekends or weekdays? YES/NO. Display your answer by counting the number of events that happend on each day of the week. Don't worry about sorting the days of the week, just display the counts. Look at the datetime object documentation to see how to get the day of the week from the `.dt` accessor. 


```python
# display the number of events (rows) for each day of the week
# Your code here

storms_df['BEGIN_DATE_TIME'].dt.day_name().value_counts()
```




<pre class="output-block">
BEGIN_DATE_TIME
Monday       275
Wednesday    208
Friday       205
Sunday       188
Saturday     166
Tuesday      154
Thursday     119
Name: count, dtype: int64
</pre>

>**Exercise:** Which events tend to span more than one county? Display the counts of each event type that spans more than one county. (Hint: Events which span more than one county will have non-null values for `BEGIN_LOCATION` and `END_LOCATION`.) 


```python
storms_df[~storms_df["BEGIN_LOCATION"].isna()]["EVENT_TYPE"].value_counts()
```




<pre class="output-block">
EVENT_TYPE
Thunderstorm Wind    383
Hail                 187
Flood                125
Flash Flood          121
Heavy Rain            27
Tornado               24
Lightning              3
Funnel Cloud           1
Name: count, dtype: int64
</pre>

>**Exercise:** Which events tend to be multi-day events? Display the counts of each event type that has a duration of more than 1 day (24 hours).
>
>You will need to use the `pd.Timedelta()` function in your filtering criteria. Docs [here](https://pandas.pydata.org/docs/user_guide/timedeltas.html) and [here](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.html#pandas.Timedelta)


```python
# Your code here
# Find duration of events

storms_df['EVENT_DURATION'] = storms_df["END_DATE_TIME"] - storms_df["BEGIN_DATE_TIME"]

# filter for events that last more than one day and count them
storms_df[storms_df['EVENT_DURATION'] > pd.Timedelta(days=1)]["EVENT_TYPE"].value_counts()
```




<pre class="output-block">
EVENT_TYPE
Flood                      48
Heavy Snow                 24
Excessive Heat              6
Winter Storm                4
Winter Weather              3
Flash Flood                 1
Blizzard                    1
Lake-Effect Snow            1
Extreme Cold/Wind Chill     1
Name: count, dtype: int64
</pre>

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

<pre class="output-block">
['NOBLE', 'MADISON', 'DELAWARE', 'HENRY', 'RANDOLPH', 'MARION', 'STEUBEN', 'LAGRANGE', 'WHITLEY', 'KOSCIUSKO', 'HANCOCK', 'FAYETTE', 'WAYNE', 'FRANKLIN', 'DEARBORN', 'MARSHALL', 'LA PORTE', 'ELKHART', 'WHITE', 'GIBSON', 'PIKE', 'POSEY', 'SPENCER', 'VANDERBURGH', 'WARRICK', 'CASS', 'PULASKI', 'MIAMI', 'FULTON', 'STARKE', 'ST. JOSEPH', 'ALLEN', 'WABASH', 'HUNTINGTON', 'WELLS', 'ADAMS', 'GRANT', 'BLACKFORD', 'JAY', 'PORTER', 'TIPPECANOE', 'RIPLEY', 'UNION', 'SWITZERLAND', 'CLINTON', 'HOWARD', 'TIPTON', 'BOONE', 'HAMILTON', 'DE KALB', 'ORANGE', 'CRAWFORD', 'BROWN', 'JOHNSON', 'PERRY', 'CLARK', 'HARRISON', 'MARTIN', 'WASHINGTON', 'DAVIESS', 'RUSH', 'DUBOIS', 'MONROE', 'KNOX', 'FLOYD', 'VERMILLION', 'HENDRICKS', 'MORGAN', 'JEFFERSON', 'SCOTT', 'JENNINGS', 'PARKE', 'OWEN', 'PUTNAM', 'WARREN', 'NEWTON', 'GREENE', 'CARROLL', 'SHELBY', 'MONTGOMERY', 'FOUNTAIN', 'JACKSON', 'JASPER', 'SULLIVAN', 'DECATUR', 'VIGO', 'LAKE', 'LAWRENCE', 'BARTHOLOMEW', 'OHIO', 'BENTON', 'CLAY']
There are 92 counties in the dataset
['Winter Weather', 'Heavy Snow', 'Ice Storm', 'Thunderstorm Wind', 'Extreme Cold/Wind Chill', 'Flash Flood', 'Hail', 'Heavy Rain', 'Flood', 'Tornado', 'Lightning', 'Heat', 'Funnel Cloud', 'Excessive Heat', 'Dense Fog', 'Cold/Wind Chill', 'Winter Storm', 'Lake-Effect Snow', 'Blizzard', 'Frost/Freeze', 'Strong Wind', 'High Wind']
There are 22 event types in the dataset
</pre>

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




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>EVENT_TYPE</th>
      <th>CZ_NAME</th>
      <th>BEGIN_DATE_TIME</th>
      <th>END_DATE_TIME</th>
      <th>CZ_TIMEZONE</th>
      <th>BEGIN_LOCATION</th>
      <th>END_LOCATION</th>
      <th>BEGIN_LAT</th>
      <th>BEGIN_LON</th>
      <th>END_LAT</th>
      <th>END_LON</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>572</th>
      <td>Thunderstorm Wind</td>
      <td>ELKHART</td>
      <td>2015-07-18 17:55:00-05:00</td>
      <td>2015-07-18 17:58:00-05:00</td>
      <td>EST-5</td>
      <td>JAMESTOWN</td>
      <td>JAMESTOWN</td>
      <td>41.6400</td>
      <td>-86.0200</td>
      <td>41.6400</td>
      <td>-86.0200</td>
    </tr>
    <tr>
      <th>574</th>
      <td>Thunderstorm Wind</td>
      <td>ELKHART</td>
      <td>2015-07-18 17:58:00-05:00</td>
      <td>2015-07-18 18:01:00-05:00</td>
      <td>EST-5</td>
      <td>ELKHART</td>
      <td>ELKHART</td>
      <td>41.7026</td>
      <td>-85.9467</td>
      <td>41.7026</td>
      <td>-85.9467</td>
    </tr>
    <tr>
      <th>583</th>
      <td>Thunderstorm Wind</td>
      <td>ELKHART</td>
      <td>2015-07-18 18:15:00-05:00</td>
      <td>2015-07-18 18:18:00-05:00</td>
      <td>EST-5</td>
      <td>BRISTOL</td>
      <td>BRISTOL</td>
      <td>41.6900</td>
      <td>-85.8200</td>
      <td>41.6900</td>
      <td>-85.8200</td>
    </tr>
    <tr>
      <th>591</th>
      <td>Thunderstorm Wind</td>
      <td>ELKHART</td>
      <td>2015-07-18 18:35:00-05:00</td>
      <td>2015-07-18 18:38:00-05:00</td>
      <td>EST-5</td>
      <td>ELKHART MIDWAY ARPT</td>
      <td>ELKHART MIDWAY ARPT</td>
      <td>41.6100</td>
      <td>-85.8700</td>
      <td>41.6100</td>
      <td>-85.8700</td>
    </tr>
    <tr>
      <th>592</th>
      <td>Thunderstorm Wind</td>
      <td>ELKHART</td>
      <td>2015-07-13 20:47:00-05:00</td>
      <td>2015-07-13 20:50:00-05:00</td>
      <td>EST-5</td>
      <td>MILLERSBURG</td>
      <td>MILLERSBURG</td>
      <td>41.5100</td>
      <td>-85.7300</td>
      <td>41.5100</td>
      <td>-85.7300</td>
    </tr>
    <tr>
      <th>608</th>
      <td>Thunderstorm Wind</td>
      <td>ELKHART</td>
      <td>2015-07-18 17:50:00-05:00</td>
      <td>2015-07-18 17:53:00-05:00</td>
      <td>EST-5</td>
      <td>ELKHART</td>
      <td>ELKHART</td>
      <td>41.6800</td>
      <td>-85.9800</td>
      <td>41.6800</td>
      <td>-85.9800</td>
    </tr>
    <tr>
      <th>971</th>
      <td>Thunderstorm Wind</td>
      <td>ELKHART</td>
      <td>2015-08-02 23:25:00-05:00</td>
      <td>2015-08-02 23:26:00-05:00</td>
      <td>EST-5</td>
      <td>GOSHEN</td>
      <td>GOSHEN</td>
      <td>41.5800</td>
      <td>-85.8300</td>
      <td>41.5800</td>
      <td>-85.8300</td>
    </tr>
  </tbody>
</table>
</div>



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




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>EVENT_TYPE</th>
      <th>CZ_NAME</th>
      <th>BEGIN_DATE_TIME</th>
      <th>END_DATE_TIME</th>
      <th>CZ_TIMEZONE</th>
      <th>BEGIN_LOCATION</th>
      <th>END_LOCATION</th>
      <th>BEGIN_LAT</th>
      <th>BEGIN_LON</th>
      <th>END_LAT</th>
      <th>END_LON</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>429</th>
      <td>Thunderstorm Wind</td>
      <td>OHIO</td>
      <td>2015-06-30 12:48:00-05:00</td>
      <td>2015-06-30 12:51:00-05:00</td>
      <td>EST-5</td>
      <td>FRENCH</td>
      <td>FRENCH</td>
      <td>39.0000</td>
      <td>-84.8800</td>
      <td>39.0000</td>
      <td>-84.8800</td>
    </tr>
    <tr>
      <th>702</th>
      <td>Winter Weather</td>
      <td>OHIO</td>
      <td>2015-03-01 02:00:00-05:00</td>
      <td>2015-03-01 17:00:00-05:00</td>
      <td>EST-5</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>849</th>
      <td>Winter Storm</td>
      <td>OHIO</td>
      <td>2015-02-21 00:00:00-05:00</td>
      <td>2015-02-21 18:00:00-05:00</td>
      <td>EST-5</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>878</th>
      <td>Winter Weather</td>
      <td>OHIO</td>
      <td>2015-02-18 00:00:00-05:00</td>
      <td>2015-02-18 19:00:00-05:00</td>
      <td>EST-5</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>897</th>
      <td>Winter Weather</td>
      <td>OHIO</td>
      <td>2015-02-14 10:00:00-05:00</td>
      <td>2015-02-14 17:00:00-05:00</td>
      <td>EST-5</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>907</th>
      <td>Winter Storm</td>
      <td>OHIO</td>
      <td>2015-02-15 22:00:00-05:00</td>
      <td>2015-02-17 00:00:00-05:00</td>
      <td>EST-5</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>919</th>
      <td>Winter Storm</td>
      <td>OHIO</td>
      <td>2015-03-04 13:00:00-05:00</td>
      <td>2015-03-05 13:00:00-05:00</td>
      <td>EST-5</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1070</th>
      <td>Thunderstorm Wind</td>
      <td>OHIO</td>
      <td>2015-07-13 23:15:00-05:00</td>
      <td>2015-07-13 23:17:00-05:00</td>
      <td>EST-5</td>
      <td>COFIELD CORNER</td>
      <td>COFIELD CORNER</td>
      <td>38.9526</td>
      <td>-84.9598</td>
      <td>38.9526</td>
      <td>-84.9598</td>
    </tr>
  </tbody>
</table>
</div>




```python
# test your function
# should return 11 rows of data

storm_by_county(storms_df, ["ELKHART", "ST. JOSEPH"], ["Thunderstorm Wind"])
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>EVENT_TYPE</th>
      <th>CZ_NAME</th>
      <th>BEGIN_DATE_TIME</th>
      <th>END_DATE_TIME</th>
      <th>CZ_TIMEZONE</th>
      <th>BEGIN_LOCATION</th>
      <th>END_LOCATION</th>
      <th>BEGIN_LAT</th>
      <th>BEGIN_LON</th>
      <th>END_LAT</th>
      <th>END_LON</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>281</th>
      <td>Thunderstorm Wind</td>
      <td>ST. JOSEPH</td>
      <td>2015-06-11 15:26:00-05:00</td>
      <td>2015-06-11 15:26:00-05:00</td>
      <td>EST-5</td>
      <td>ROSELAND</td>
      <td>ROSELAND</td>
      <td>41.7226</td>
      <td>-86.2559</td>
      <td>41.7226</td>
      <td>-86.2559</td>
    </tr>
    <tr>
      <th>480</th>
      <td>Thunderstorm Wind</td>
      <td>ST. JOSEPH</td>
      <td>2015-06-08 16:30:00-05:00</td>
      <td>2015-06-08 16:30:00-05:00</td>
      <td>EST-5</td>
      <td>GRANGER</td>
      <td>GRANGER</td>
      <td>41.7400</td>
      <td>-86.1400</td>
      <td>41.7400</td>
      <td>-86.1400</td>
    </tr>
    <tr>
      <th>571</th>
      <td>Thunderstorm Wind</td>
      <td>ST. JOSEPH</td>
      <td>2015-07-18 17:43:00-05:00</td>
      <td>2015-07-18 17:46:00-05:00</td>
      <td>EST-5</td>
      <td>GILMER PARK</td>
      <td>GILMER PARK</td>
      <td>41.6285</td>
      <td>-86.2971</td>
      <td>41.6285</td>
      <td>-86.2971</td>
    </tr>
    <tr>
      <th>572</th>
      <td>Thunderstorm Wind</td>
      <td>ELKHART</td>
      <td>2015-07-18 17:55:00-05:00</td>
      <td>2015-07-18 17:58:00-05:00</td>
      <td>EST-5</td>
      <td>JAMESTOWN</td>
      <td>JAMESTOWN</td>
      <td>41.6400</td>
      <td>-86.0200</td>
      <td>41.6400</td>
      <td>-86.0200</td>
    </tr>
    <tr>
      <th>574</th>
      <td>Thunderstorm Wind</td>
      <td>ELKHART</td>
      <td>2015-07-18 17:58:00-05:00</td>
      <td>2015-07-18 18:01:00-05:00</td>
      <td>EST-5</td>
      <td>ELKHART</td>
      <td>ELKHART</td>
      <td>41.7026</td>
      <td>-85.9467</td>
      <td>41.7026</td>
      <td>-85.9467</td>
    </tr>
    <tr>
      <th>582</th>
      <td>Thunderstorm Wind</td>
      <td>ST. JOSEPH</td>
      <td>2015-07-18 18:04:00-05:00</td>
      <td>2015-07-18 18:07:00-05:00</td>
      <td>EST-5</td>
      <td>GLENWOOD</td>
      <td>GLENWOOD</td>
      <td>41.6700</td>
      <td>-86.0800</td>
      <td>41.6700</td>
      <td>-86.0800</td>
    </tr>
    <tr>
      <th>583</th>
      <td>Thunderstorm Wind</td>
      <td>ELKHART</td>
      <td>2015-07-18 18:15:00-05:00</td>
      <td>2015-07-18 18:18:00-05:00</td>
      <td>EST-5</td>
      <td>BRISTOL</td>
      <td>BRISTOL</td>
      <td>41.6900</td>
      <td>-85.8200</td>
      <td>41.6900</td>
      <td>-85.8200</td>
    </tr>
    <tr>
      <th>591</th>
      <td>Thunderstorm Wind</td>
      <td>ELKHART</td>
      <td>2015-07-18 18:35:00-05:00</td>
      <td>2015-07-18 18:38:00-05:00</td>
      <td>EST-5</td>
      <td>ELKHART MIDWAY ARPT</td>
      <td>ELKHART MIDWAY ARPT</td>
      <td>41.6100</td>
      <td>-85.8700</td>
      <td>41.6100</td>
      <td>-85.8700</td>
    </tr>
    <tr>
      <th>592</th>
      <td>Thunderstorm Wind</td>
      <td>ELKHART</td>
      <td>2015-07-13 20:47:00-05:00</td>
      <td>2015-07-13 20:50:00-05:00</td>
      <td>EST-5</td>
      <td>MILLERSBURG</td>
      <td>MILLERSBURG</td>
      <td>41.5100</td>
      <td>-85.7300</td>
      <td>41.5100</td>
      <td>-85.7300</td>
    </tr>
    <tr>
      <th>608</th>
      <td>Thunderstorm Wind</td>
      <td>ELKHART</td>
      <td>2015-07-18 17:50:00-05:00</td>
      <td>2015-07-18 17:53:00-05:00</td>
      <td>EST-5</td>
      <td>ELKHART</td>
      <td>ELKHART</td>
      <td>41.6800</td>
      <td>-85.9800</td>
      <td>41.6800</td>
      <td>-85.9800</td>
    </tr>
    <tr>
      <th>971</th>
      <td>Thunderstorm Wind</td>
      <td>ELKHART</td>
      <td>2015-08-02 23:25:00-05:00</td>
      <td>2015-08-02 23:26:00-05:00</td>
      <td>EST-5</td>
      <td>GOSHEN</td>
      <td>GOSHEN</td>
      <td>41.5800</td>
      <td>-85.8300</td>
      <td>41.5800</td>
      <td>-85.8300</td>
    </tr>
  </tbody>
</table>
</div>



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

<pre class="output-block">
--- 3.1 ---
A Heavy Snow occurred on 2015-01-05 21:00:00-05:00 in TIPPECANOE county.
A Hail occurred on 2015-04-08 16:15:00-05:00 in TIPPECANOE county.
A Hail occurred on 2015-04-08 16:25:00-05:00 in TIPPECANOE county.
A Thunderstorm Wind occurred on 2015-06-12 16:37:00-05:00 in TIPPECANOE county.
A Thunderstorm Wind occurred on 2015-06-12 16:40:00-05:00 in TIPPECANOE county.
A Thunderstorm Wind occurred on 2015-06-21 00:15:00-05:00 in TIPPECANOE county.
A Thunderstorm Wind occurred on 2015-06-07 19:15:00-05:00 in TIPPECANOE county.
A Hail occurred on 2015-06-08 19:50:00-05:00 in TIPPECANOE county.
A Thunderstorm Wind occurred on 2015-06-07 18:51:00-05:00 in TIPPECANOE county.
A Thunderstorm Wind occurred on 2015-06-21 00:10:00-05:00 in TIPPECANOE county.
A Thunderstorm Wind occurred on 2015-06-21 00:27:00-05:00 in TIPPECANOE county.
A Thunderstorm Wind occurred on 2015-07-13 09:50:00-05:00 in TIPPECANOE county.
A Tornado occurred on 2015-07-17 15:33:00-05:00 in TIPPECANOE county.
A Flood occurred on 2015-07-17 15:30:00-05:00 in TIPPECANOE county.
A Hail occurred on 2015-07-17 15:04:00-05:00 in TIPPECANOE county.
A Thunderstorm Wind occurred on 2015-07-17 15:04:00-05:00 in TIPPECANOE county.
A Tornado occurred on 2015-07-17 15:38:00-05:00 in TIPPECANOE county.
A Hail occurred on 2015-09-18 21:34:00-05:00 in TIPPECANOE county.
A Thunderstorm Wind occurred on 2015-09-18 21:42:00-05:00 in TIPPECANOE county.
A Hail occurred on 2015-09-18 21:43:00-05:00 in TIPPECANOE county.
A Thunderstorm Wind occurred on 2015-09-18 21:43:00-05:00 in TIPPECANOE county.
--- 3.2 ---
A Flash Flood occurred on 2015-06-22 05:20:00-05:00 in SPENCER county.
A Flood occurred on 2015-04-08 16:36:00-05:00 in MARION county.
A Flood occurred on 2015-06-08 02:16:00-05:00 in VERMILLION county.
A Flash Flood occurred on 2015-06-25 08:00:00-05:00 in VERMILLION county.
A Flood occurred on 2015-06-26 22:45:00-05:00 in MARION county.
A Flood occurred on 2015-06-19 10:23:00-05:00 in MONROE county.
A Flash Flood occurred on 2015-07-20 23:25:00-05:00 in MARION county.
A Flash Flood occurred on 2015-07-21 00:14:00-05:00 in MARION county.
A Flash Flood occurred on 2015-07-26 18:26:00-05:00 in MARION county.
A Flash Flood occurred on 2015-07-07 14:20:00-05:00 in MARION county.
A Flash Flood occurred on 2015-07-14 01:20:00-05:00 in MARION county.
A Flood occurred on 2015-07-17 18:29:00-05:00 in MARION county.
A Flash Flood occurred on 2015-07-20 23:20:00-05:00 in MARION county.
A Flood occurred on 2015-12-27 11:30:00-05:00 in MARION county.
A Flood occurred on 2015-12-30 22:00:00-05:00 in SPENCER county.
--- 3.3 ---
A Tornado occurred on 2015-04-07 15:27:00-05:00 in PERRY county.
A Tornado occurred on 2015-05-30 19:47:00-05:00 in MARION county.
A Tornado occurred on 2015-06-07 16:28:00-05:00 in JASPER county.
A Tornado occurred on 2015-06-07 16:37:00-05:00 in JASPER county.
A Tornado occurred on 2015-06-19 15:40:00-05:00 in PERRY county.
A Tornado occurred on 2015-07-13 20:25:00-05:00 in PUTNAM county.
A Tornado occurred on 2015-07-17 15:33:00-05:00 in TIPPECANOE county.
A Tornado occurred on 2015-07-13 20:27:00-05:00 in PUTNAM county.
A Tornado occurred on 2015-07-12 02:38:00-05:00 in JOHNSON county.
A Tornado occurred on 2015-07-13 19:59:00-05:00 in BENTON county.
A Tornado occurred on 2015-04-07 14:20:00-05:00 in VANDERBURGH county.
A Tornado occurred on 2015-04-07 14:28:00-05:00 in WARRICK county.
A Tornado occurred on 2015-04-07 14:47:00-05:00 in WARRICK county.
A Tornado occurred on 2015-04-07 14:54:00-05:00 in WARRICK county.
A Tornado occurred on 2015-04-07 14:56:00-05:00 in SPENCER county.
A Tornado occurred on 2015-07-13 20:15:00-05:00 in WARREN county.
A Tornado occurred on 2015-07-17 15:38:00-05:00 in TIPPECANOE county.
A Tornado occurred on 2015-06-07 17:31:00-05:00 in STARKE county.
A Tornado occurred on 2015-12-23 15:42:00-05:00 in JOHNSON county.
A Tornado occurred on 2015-12-23 15:55:00-05:00 in HAMILTON county.
A Tornado occurred on 2015-12-23 16:55:00-05:00 in WAYNE county.
A Tornado occurred on 2015-12-23 16:39:00-05:00 in SPENCER county.
A Tornado occurred on 2015-12-23 16:13:00-05:00 in DECATUR county.
A Tornado occurred on 2015-12-23 16:14:00-05:00 in RUSH county.
</pre>

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




<pre class="output-block">
&lt;Axes: xlabel='EVENT_TYPE', ylabel='Count'&gt;
</pre>

![A barplot showing the number of Floods and Flash Floods in different counties in Indiana. The x-axis separates 'Flood' and 'Flash Flood' events, while the y-axis shows the number of events. Bars in each category are colored by county name. For Flash flood: Spencer 1, Marion 6, Vermillion 1, Monroe 0, Tippecanoe 0. For Flood: Spencer 1, Marion 4, Vermillion 1, Monroe 1, Tippecanoe 1. ](Python-Day6_files/Python-Day6_39_1.png)
    


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

<pre class="output-block">
--- 5.1 ---
  CZ_NAME       EVENT_TYPE  0
0    PIKE  Cold/Wind Chill  2
1    PIKE        Dense Fog  6
2    PIKE   Excessive Heat  1
3    PIKE            Flood  6
4    PIKE     Frost/Freeze  1
5    PIKE             Heat  2
6    PIKE       Heavy Snow  1
7    PIKE     Winter Storm  2
8    PIKE   Winter Weather  3
--- 5.2 ---
    CZ_NAME         EVENT_TYPE  0
0     BOONE  Thunderstorm Wind  7
1   ELKHART  Thunderstorm Wind  7
2  LA PORTE  Thunderstorm Wind  5
</pre>

6. Use your function to summarize the total counts of each weather event in each county.


```python
# your code here

all_weather = storms_df["EVENT_TYPE"].unique().tolist()
all_counties = storms_df["CZ_NAME"].unique().tolist()

summarise_storms(storms_df, all_counties, all_weather)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>CZ_NAME</th>
      <th>EVENT_TYPE</th>
      <th>0</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>ADAMS</td>
      <td>Extreme Cold/Wind Chill</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>ADAMS</td>
      <td>Hail</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>ADAMS</td>
      <td>Heavy Rain</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>ADAMS</td>
      <td>Heavy Snow</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>ADAMS</td>
      <td>Winter Weather</td>
      <td>5</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>467</th>
      <td>WHITLEY</td>
      <td>Flash Flood</td>
      <td>1</td>
    </tr>
    <tr>
      <th>468</th>
      <td>WHITLEY</td>
      <td>Flood</td>
      <td>3</td>
    </tr>
    <tr>
      <th>469</th>
      <td>WHITLEY</td>
      <td>Hail</td>
      <td>1</td>
    </tr>
    <tr>
      <th>470</th>
      <td>WHITLEY</td>
      <td>Heavy Snow</td>
      <td>2</td>
    </tr>
    <tr>
      <th>471</th>
      <td>WHITLEY</td>
      <td>Winter Weather</td>
      <td>5</td>
    </tr>
  </tbody>
</table>
<p>472 rows × 3 columns</p>
</div>



## Self-guided exploratory questions

Here are a few questions we've come up with that can be approached in multiple different ways.

**Question 1:** What is the most dangerous county in Indiana, assuming danger only comes from the storm events? You will need to account for the area of each county to answer this question. We've provided code to get the table from wikipedia that lists county information. 


```python
!pip install lxml
county_info = pd.read_html("https://en.wikipedia.org/wiki/List_of_counties_in_Indiana")
county_info = county_info[1]
```

<pre class="output-block">
Requirement already satisfied: lxml in /opt/homebrew/Caskroom/miniforge/base/envs/pyworkshop/lib/python3.13/site-packages (5.3.0)
</pre>

You will need to do some data cleaning to get the county names to match up and to extract the area of each county. Then you will need to merge the two dataframes together. 


```python
county_info[["County", "Area[3][12]"]]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>County</th>
      <th>Area[3][12]</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Adams County</td>
      <td>339 sq mi (878 km2)</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Allen County</td>
      <td>657 sq mi (1,702 km2)</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Bartholomew County</td>
      <td>407 sq mi (1,054 km2)</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Benton County</td>
      <td>406 sq mi (1,052 km2)</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Blackford County</td>
      <td>165 sq mi (427 km2)</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>87</th>
      <td>Washington County</td>
      <td>514 sq mi (1,331 km2)</td>
    </tr>
    <tr>
      <th>88</th>
      <td>Wayne County</td>
      <td>402 sq mi (1,041 km2)</td>
    </tr>
    <tr>
      <th>89</th>
      <td>Wells County</td>
      <td>368 sq mi (953 km2)</td>
    </tr>
    <tr>
      <th>90</th>
      <td>White County</td>
      <td>505 sq mi (1,308 km2)</td>
    </tr>
    <tr>
      <th>91</th>
      <td>Whitley County</td>
      <td>336 sq mi (870 km2)</td>
    </tr>
  </tbody>
</table>
<p>92 rows × 2 columns</p>
</div>




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

<pre class="output-block">
       CZ_NAME  Area_sq_mi  EVENT_TYPE
0        ADAMS         339           9
1        ALLEN         657          31
2  BARTHOLOMEW         407           7
3       BENTON         406           4
4    BLACKFORD         165           6
</pre>

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>CZ_NAME</th>
      <th>Area_sq_mi</th>
      <th>EVENT_TYPE</th>
      <th>normalized</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>79</th>
      <td>VANDERBURGH</td>
      <td>233</td>
      <td>39</td>
      <td>0.167382</td>
    </tr>
    <tr>
      <th>20</th>
      <td>FLOYD</td>
      <td>148</td>
      <td>19</td>
      <td>0.128378</td>
    </tr>
    <tr>
      <th>46</th>
      <td>MARION</td>
      <td>396</td>
      <td>41</td>
      <td>0.103535</td>
    </tr>
    <tr>
      <th>9</th>
      <td>CLARK</td>
      <td>373</td>
      <td>37</td>
      <td>0.099196</td>
    </tr>
    <tr>
      <th>33</th>
      <td>HUNTINGTON</td>
      <td>383</td>
      <td>37</td>
      <td>0.096606</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>10</th>
      <td>CLAY</td>
      <td>358</td>
      <td>2</td>
      <td>0.005587</td>
    </tr>
    <tr>
      <th>26</th>
      <td>GREENE</td>
      <td>543</td>
      <td>3</td>
      <td>0.005525</td>
    </tr>
    <tr>
      <th>7</th>
      <td>CARROLL</td>
      <td>372</td>
      <td>2</td>
      <td>0.005376</td>
    </tr>
    <tr>
      <th>44</th>
      <td>LAWRENCE</td>
      <td>449</td>
      <td>2</td>
      <td>0.004454</td>
    </tr>
    <tr>
      <th>74</th>
      <td>SULLIVAN</td>
      <td>447</td>
      <td>1</td>
      <td>0.002237</td>
    </tr>
  </tbody>
</table>
<p>90 rows × 4 columns</p>
</div>



**Question 2:** What is the best time to visit Indiana if you want to take cool pictures of clouds? The main idea of this question is to summarize the data in such a way that you can tell which month or week or your choice of span of days has the highest concentration of events of interest. 


```python
# decide which weather events probably have cool clouds
cool_clouds = ["Thunderstorm wind", "Tornado", "Lightning", "Heavy Rain"]

# filter for cool clouds
df_clouds = storms_df[storms_df["EVENT_TYPE"].isin(cool_clouds)]

# group by month and number of events
df_clouds.groupby(df_clouds["BEGIN_DATE_TIME"].dt.month)["EVENT_TYPE"].count().reset_index()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>BEGIN_DATE_TIME</th>
      <th>EVENT_TYPE</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>4</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>9</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>1</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>14</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7</td>
      <td>12</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8</td>
      <td>1</td>
    </tr>
    <tr>
      <th>8</th>
      <td>10</td>
      <td>2</td>
    </tr>
    <tr>
      <th>9</th>
      <td>11</td>
      <td>1</td>
    </tr>
    <tr>
      <th>10</th>
      <td>12</td>
      <td>8</td>
    </tr>
  </tbody>
</table>
</div>



**Question 3:** Create a plot that compares the duration in hours of each common event type. Some events occur only infrequently, so your first step would be to filter those out. Then, you will need to decide what type of plot to make. Take a look at the [seaborn gallery](https://seaborn.pydata.org/examples/index.html). If you are having trouble deciding how to represent your data, take a look at this [infographic](https://github.com/Financial-Times/chart-doctor/blob/main/visual-vocabulary/poster.png)


```python
# get event duration. We've already done this, but the code is reproduced before

storms_df["EVENT_DURATION"] = storms_df["END_DATE_TIME"] - storms_df["BEGIN_DATE_TIME"]

# filter out events which only occurred <10 times in the year

storms_filtered = storms_df.groupby("EVENT_TYPE").filter(lambda x: len(x) > 10)

# group by event type and calculate average duration

print(storms_filtered.groupby("EVENT_TYPE")["EVENT_DURATION"].mean())


```

<pre class="output-block">
EVENT_TYPE
Cold/Wind Chill                     0 days 09:00:00
Dense Fog                           0 days 07:27:00
Extreme Cold/Wind Chill   0 days 12:20:46.153846153
Flash Flood               0 days 02:13:29.256198347
Flood                        4 days 01:25:38.880000
Hail                      0 days 00:01:21.818181818
Heat                                0 days 05:24:00
Heavy Rain                0 days 02:08:44.444444444
Heavy Snow                0 days 16:16:49.923664122
Thunderstorm Wind         0 days 00:00:41.984334203
Tornado                             0 days 00:02:35
Winter Storm              0 days 16:39:05.454545454
Winter Weather            0 days 12:19:15.185185185
Name: EVENT_DURATION, dtype: timedelta64[ns]
</pre>

```python
storms_filtered.groupby("EVENT_TYPE")["EVENT_DURATION"].describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
    </tr>
    <tr>
      <th>EVENT_TYPE</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Cold/Wind Chill</th>
      <td>12</td>
      <td>0 days 09:00:00</td>
      <td>0 days 02:05:20.154737286</td>
      <td>0 days 07:00:00</td>
      <td>0 days 07:00:00</td>
      <td>0 days 09:00:00</td>
      <td>0 days 11:00:00</td>
      <td>0 days 11:00:00</td>
    </tr>
    <tr>
      <th>Dense Fog</th>
      <td>40</td>
      <td>0 days 07:27:00</td>
      <td>0 days 03:16:24.370352945</td>
      <td>0 days 04:00:00</td>
      <td>0 days 05:00:00</td>
      <td>0 days 05:00:00</td>
      <td>0 days 10:00:00</td>
      <td>0 days 13:00:00</td>
    </tr>
    <tr>
      <th>Extreme Cold/Wind Chill</th>
      <td>26</td>
      <td>0 days 12:20:46.153846153</td>
      <td>0 days 04:00:33.883213306</td>
      <td>0 days 03:00:00</td>
      <td>0 days 12:00:00</td>
      <td>0 days 12:00:00</td>
      <td>0 days 12:00:00</td>
      <td>1 days 06:00:00</td>
    </tr>
    <tr>
      <th>Flash Flood</th>
      <td>121</td>
      <td>0 days 02:13:29.256198347</td>
      <td>0 days 03:20:21.201559833</td>
      <td>0 days 00:00:00</td>
      <td>0 days 00:00:00</td>
      <td>0 days 01:51:00</td>
      <td>0 days 03:30:00</td>
      <td>1 days 03:35:00</td>
    </tr>
    <tr>
      <th>Flood</th>
      <td>125</td>
      <td>4 days 01:25:38.880000</td>
      <td>7 days 03:59:43.207680028</td>
      <td>0 days 00:00:00</td>
      <td>0 days 01:30:00</td>
      <td>0 days 02:18:00</td>
      <td>3 days 19:00:00</td>
      <td>29 days 09:00:00</td>
    </tr>
    <tr>
      <th>Hail</th>
      <td>187</td>
      <td>0 days 00:01:21.818181818</td>
      <td>0 days 00:01:23.851565542</td>
      <td>0 days 00:00:00</td>
      <td>0 days 00:00:00</td>
      <td>0 days 00:02:00</td>
      <td>0 days 00:02:00</td>
      <td>0 days 00:10:00</td>
    </tr>
    <tr>
      <th>Heat</th>
      <td>15</td>
      <td>0 days 05:24:00</td>
      <td>0 days 00:49:41.083216358</td>
      <td>0 days 05:00:00</td>
      <td>0 days 05:00:00</td>
      <td>0 days 05:00:00</td>
      <td>0 days 05:00:00</td>
      <td>0 days 07:00:00</td>
    </tr>
    <tr>
      <th>Heavy Rain</th>
      <td>27</td>
      <td>0 days 02:08:44.444444444</td>
      <td>0 days 03:40:57.113426770</td>
      <td>0 days 00:00:00</td>
      <td>0 days 00:00:00</td>
      <td>0 days 00:00:00</td>
      <td>0 days 03:00:00</td>
      <td>0 days 12:15:00</td>
    </tr>
    <tr>
      <th>Heavy Snow</th>
      <td>131</td>
      <td>0 days 16:16:49.923664122</td>
      <td>0 days 06:48:08.251044631</td>
      <td>0 days 08:00:00</td>
      <td>0 days 11:37:30</td>
      <td>0 days 15:00:00</td>
      <td>0 days 15:00:00</td>
      <td>1 days 10:00:00</td>
    </tr>
    <tr>
      <th>Thunderstorm Wind</th>
      <td>383</td>
      <td>0 days 00:00:41.984334203</td>
      <td>0 days 00:01:27.395291215</td>
      <td>0 days 00:00:00</td>
      <td>0 days 00:00:00</td>
      <td>0 days 00:00:00</td>
      <td>0 days 00:01:00</td>
      <td>0 days 00:11:00</td>
    </tr>
    <tr>
      <th>Tornado</th>
      <td>24</td>
      <td>0 days 00:02:35</td>
      <td>0 days 00:02:03.745882671</td>
      <td>0 days 00:00:00</td>
      <td>0 days 00:01:00</td>
      <td>0 days 00:02:00</td>
      <td>0 days 00:03:15</td>
      <td>0 days 00:08:00</td>
    </tr>
    <tr>
      <th>Winter Storm</th>
      <td>33</td>
      <td>0 days 16:39:05.454545454</td>
      <td>0 days 05:00:36.440386566</td>
      <td>0 days 11:00:00</td>
      <td>0 days 12:30:00</td>
      <td>0 days 15:00:00</td>
      <td>0 days 20:00:00</td>
      <td>1 days 02:00:00</td>
    </tr>
    <tr>
      <th>Winter Weather</th>
      <td>162</td>
      <td>0 days 12:19:15.185185185</td>
      <td>0 days 05:43:50.386658814</td>
      <td>0 days 00:01:00</td>
      <td>0 days 07:15:00</td>
      <td>0 days 11:00:00</td>
      <td>0 days 17:00:00</td>
      <td>1 days 06:00:00</td>
    </tr>
  </tbody>
</table>
</div>




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

<pre class="output-block">
/var/folders/k6/w69wqlhj5ml2h98s23wzt51c0000gq/T/ipykernel_54224/105044077.py:9: SettingWithCopyWarning: 
A value is trying to be set on a copy of a slice from a DataFrame.
Try using .loc[row_indexer,col_indexer] = value instead

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
  storms_no_flood["EVENT_DURATION_HOURS"] = storms_no_flood["EVENT_DURATION"].dt.total_seconds() / 3600
</pre>

![A strip plot showing the duration of different events in hours in hours on the x-axis, ranging from 0 to 35. The y-axis shows the event type. Event types are 'Winter Weather', 'Heavy Snow', 'Thunderstorm Wind', 'Extreme Cold/Wind Chill', 'Hail', 'Heavy Rain', ''Tornado', 'Heat', 'Dense Fog', 'Cold/Wind Chill', and 'Winter Storm'. Winter Weather and Heavy Snow span the range of durations, while Winter Storms last between 10 and 26 hours. Thunderstorm Wind, Hail, and Tornados have short durations, less than 1 hour. There are few Extreme Cold/Wind Chill events, mostly around 13 hours long. Heat, Dense Fog, and Cold/Wind Chill events all last between 4 and 13 hours.](Python-Day6_files/Python-Day6_58_1.png)
    



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

<pre class="output-block">
/var/folders/k6/w69wqlhj5ml2h98s23wzt51c0000gq/T/ipykernel_54224/2645905542.py:9: SettingWithCopyWarning: 
A value is trying to be set on a copy of a slice from a DataFrame.
Try using .loc[row_indexer,col_indexer] = value instead

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
  storms_flood_only["EVENT_DURATION_HOURS"] = storms_flood_only["EVENT_DURATION"].dt.total_seconds() / 3600
</pre>

![A strip plot showing the duration of Flood and Flash flood events in hours on the x-axis, ranging from 0 to 700. The y-axis shows the event type. Flash Floods all last under 24 hours while Floods can last up to 700 hours.](Python-Day6_files/Python-Day6_59_1.png)
    


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

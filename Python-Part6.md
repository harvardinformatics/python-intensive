---
title: "[Workshop] Python intensive, part 6"
description: "Analyzing a real dataset: Indiana storms."
authors:
    - Danielle Khost
    - Lei Ma
---

# Python intensive, part 6

## Putting it all together: exploring storm data

For our final section, we are going to do some exploratory analysis of a real world dataset, coding in pairs or groups as we did on the previous days. There are several different "paths" you can choose to follow based on what you are interested in working on, so either come to a consensus within your group, or group up based on shared interest! First, let's download our data:


```python
# This line downloads the file locally to the same folder as your notebook
!wget https://raw.githubusercontent.com/harvardinformatics/python-intensive/refs/heads/main/data/indiana_storms_full.csv

import os

# This line stores the local file path as a Python string variable
storms_file = 'indiana_storms_full.csv'
if not os.path.isfile(storms_file):
    storms_file = 'data/indiana_storms_full.csv'
```

<pre class="output-block">--2026-10-15 03:47:07--  https://raw.githubusercontent.com/harvardinformatics/python-intensive/refs/heads/main/data/indiana_storms_full.csv
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 185.199.108.133, 185.199.109.133, 185.199.110.133, ...
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|185.199.108.133|:443... connected.
HTTP request sent, awaiting response...
</pre>

<pre class="output-block">200 OK
Length: 952491 (930K) [text/plain]
Saving to: ‘indiana_storms_full.csv’


indiana_storms_full   0%[                    ]       0  --.-KB/s
</pre>

<pre class="output-block">
indiana_storms_full 100%[===================>] 930.17K  --.-KB/s    in 0.05s

2026-10-15 03:47:07 (17.9 MB/s) - ‘indiana_storms_full.csv’ saved [952491/952491]
</pre>


```python
import pandas as pd
storms_df = pd.read_csv(storms_file)
storms_df.head()
```

<pre class="output-block">&nbsp;&nbsp;&nbsp;BEGIN_YEARMONTH  BEGIN_DAY  BEGIN_TIME  END_YEARMONTH  END_DAY  END_TIME  \
0           201501          8        1700         201501        9      1200
1           201501          5        2200         201501        6       830
2           201501          5        2200         201501        6       900
3           201501          5        2200         201501        6       900
4           201501          5        2215         201501        6       930

&nbsp;&nbsp;&nbsp;EPISODE_ID  EVENT_ID    STATE  STATE_FIPS  ...  END_RANGE END_AZIMUTH  \
0       91570    548696  INDIANA          18  ...        NaN         NaN
1       92441    555468  INDIANA          18  ...        NaN         NaN
2       92441    555469  INDIANA          18  ...        NaN         NaN
3       92441    555470  INDIANA          18  ...        NaN         NaN
4       92441    555471  INDIANA          18  ...        NaN         NaN

&nbsp;&nbsp;END_LOCATION BEGIN_LAT  BEGIN_LON END_LAT END_LON  \
0          NaN       NaN        NaN     NaN     NaN
1          NaN       NaN        NaN     NaN     NaN
2          NaN       NaN        NaN     NaN     NaN
3          NaN       NaN        NaN     NaN     NaN
4          NaN       NaN        NaN     NaN     NaN

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;EPISODE_NARRATIVE  \
0  A quick-moving Alberta Clipper brought a quick...
1  An Alberta Clipper brought a quick round of sn...
2  An Alberta Clipper brought a quick round of sn...
3  An Alberta Clipper brought a quick round of sn...
4  An Alberta Clipper brought a quick round of sn...

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;EVENT_NARRATIVE DATA_SOURCE
0  Periods of snow during the late afternoon hour...         CSV
1  Snowfall accumulation observations ranged from...         CSV
2  Snowfall accumulation observations ranged from...         CSV
3  Snowfall accumulation observations ranged from...         CSV
4  Snowfall accumulation of 5.5 inches was report...         CSV

[5 rows x 51 columns]
</pre>


```python
storms_df.info()
```

<pre class="output-block"><class 'pandas.DataFrame'>
RangeIndex: 1315 entries, 0 to 1314
Data columns (total 51 columns):
&nbsp;#   Column              Non-Null Count  Dtype
---  ------              --------------  -----
&nbsp;0   BEGIN_YEARMONTH     1315 non-null   int64
&nbsp;1   BEGIN_DAY           1315 non-null   int64
&nbsp;2   BEGIN_TIME          1315 non-null   int64
&nbsp;3   END_YEARMONTH       1315 non-null   int64
&nbsp;4   END_DAY             1315 non-null   int64
&nbsp;5   END_TIME            1315 non-null   int64
&nbsp;6   EPISODE_ID          1315 non-null   int64
&nbsp;7   EVENT_ID            1315 non-null   int64
&nbsp;8   STATE               1315 non-null   str
&nbsp;9   STATE_FIPS          1315 non-null   int64
&nbsp;10  YEAR                1315 non-null   int64
&nbsp;11  MONTH_NAME          1315 non-null   str
&nbsp;12  EVENT_TYPE          1315 non-null   str
&nbsp;13  CZ_TYPE             1315 non-null   str
&nbsp;14  CZ_FIPS             1315 non-null   int64
&nbsp;15  CZ_NAME             1315 non-null   str
&nbsp;16  WFO                 1315 non-null   str
&nbsp;17  BEGIN_DATE_TIME     1315 non-null   str
&nbsp;18  CZ_TIMEZONE         1315 non-null   str
&nbsp;19  END_DATE_TIME       1315 non-null   str
&nbsp;20  INJURIES_DIRECT     1315 non-null   int64
&nbsp;21  INJURIES_INDIRECT   1315 non-null   int64
&nbsp;22  DEATHS_DIRECT       1315 non-null   int64
&nbsp;23  DEATHS_INDIRECT     1315 non-null   int64
&nbsp;24  DAMAGE_PROPERTY     1011 non-null   str
&nbsp;25  DAMAGE_CROPS        1009 non-null   str
&nbsp;26  SOURCE              1315 non-null   str
&nbsp;27  MAGNITUDE           577 non-null    float64
&nbsp;28  MAGNITUDE_TYPE      390 non-null    str
&nbsp;29  FLOOD_CAUSE         246 non-null    str
&nbsp;30  CATEGORY            0 non-null      float64
&nbsp;31  TOR_F_SCALE         24 non-null     str
&nbsp;32  TOR_LENGTH          24 non-null     float64
&nbsp;33  TOR_WIDTH           24 non-null     float64
&nbsp;34  TOR_OTHER_WFO       3 non-null      str
&nbsp;35  TOR_OTHER_CZ_STATE  3 non-null      str
&nbsp;36  TOR_OTHER_CZ_FIPS   3 non-null      float64
&nbsp;37  TOR_OTHER_CZ_NAME   3 non-null      str
&nbsp;38  BEGIN_RANGE         871 non-null    float64
&nbsp;39  BEGIN_AZIMUTH       871 non-null    str
&nbsp;40  BEGIN_LOCATION      871 non-null    str
&nbsp;41  END_RANGE           871 non-null    float64
&nbsp;42  END_AZIMUTH         871 non-null    str
&nbsp;43  END_LOCATION        871 non-null    str
&nbsp;44  BEGIN_LAT           871 non-null    float64
&nbsp;45  BEGIN_LON           871 non-null    float64
&nbsp;46  END_LAT             871 non-null    float64
&nbsp;47  END_LON             871 non-null    float64
&nbsp;48  EPISODE_NARRATIVE   1315 non-null   str
&nbsp;49  EVENT_NARRATIVE     1079 non-null   str
&nbsp;50  DATA_SOURCE         1315 non-null   str
dtypes: float64(11), int64(15), str(25)
memory usage: 524.1 KB
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

<pre class="output-block"><class 'pandas.DataFrame'>
RangeIndex: 1315 entries, 0 to 1314
Data columns (total 11 columns):
&nbsp;#   Column           Non-Null Count  Dtype
---  ------           --------------  -----
&nbsp;0   EVENT_TYPE       1315 non-null   str
&nbsp;1   CZ_NAME          1315 non-null   str
&nbsp;2   BEGIN_DATE_TIME  1315 non-null   str
&nbsp;3   END_DATE_TIME    1315 non-null   str
&nbsp;4   CZ_TIMEZONE      1315 non-null   str
&nbsp;5   BEGIN_LOCATION   871 non-null    str
&nbsp;6   END_LOCATION     871 non-null    str
&nbsp;7   BEGIN_LAT        871 non-null    float64
&nbsp;8   BEGIN_LON        871 non-null    float64
&nbsp;9   END_LAT          871 non-null    float64
&nbsp;10  END_LON          871 non-null    float64
dtypes: float64(4), str(7)
memory usage: 113.1 KB
</pre>

Only some storm events have a begin and end location, but at least there aren't any that only have a begin and not and end. Data looks good! The next thing we need to do is to convert the "BEGIN_DATE_TIME" and "END_DATE_TIME" columns to datetime objects. Additionally, these data are spread out over two time zones and we want to convert it to a single time zone for clarity. This will make it easier to work with these columns later on. For more information on the proper way to manage dates and times in Python, see the section in our Python Healthy Habits document "Working with dates and times". 


```python
# Convert all date time columns to datetime objects with correct timezone parsing
# I wrote a regex to extract just the number from the timezone column and then made it an ISO8601 compliant timezone string
# Pandas does not support multiple time zones in the same column, so we will convert all times to UTC and then convert to one of the local time zones
storms_df['BEGIN_DATE_TIME'] = pd.to_datetime(storms_df["BEGIN_DATE_TIME"]+"-0"+storms_df["CZ_TIMEZONE"].str.extract(r'([0-9]+)')[0]+"00", format="mixed", utc=True).dt.tz_convert("-05:00")
storms_df['END_DATE_TIME'] = pd.to_datetime(storms_df["END_DATE_TIME"]+"-0"+storms_df["CZ_TIMEZONE"].str.extract(r'([0-9]+)')[0]+"00", format="mixed", utc=True).dt.tz_convert("-05:00")
```

Here's a breakdown of the code I used to convert the "BEGIN_DATE_TIME" and "END_DATE_TIME" columns to datetime objects:

```python
storms_df['BEGIN_DATE_TIME'] = pd.to_datetime(storms_df["BEGIN_DATE_TIME"]+"-0"+storms_df["CZ_TIMEZONE"].str.extract(r'([0-9]+)')[0]+"00", format="mixed", utc=True).dt.tz_convert("-05:00")
```

| Code                                                              | Explanation |
| ----------------------------------------------------------------- | ----------- |
| `pd.to_datetime()`                                                | This function converts a string or a list of strings to a datetime object. However, I first need to convert the string into something that is can parse.|
| `storms_df["BEGIN_DATE_TIME"]`                                    | This column is alredy in a format that pandas can parse, but it is missing the time zone information.|
| `+"-0"+storms_df["CZ_TIMEZONE"].str.extract(r'([0-9]+)')[0]+"00"` | This adds the time zone offset to the string by concatenating `-0` and the regex match for the time zone offset. Plus, it adds `00` to the end to represent the minutes.|
| `format="mixed"`                                                  | This tells pandas to try to parse the string in a mixed format, which means it will attempt to infer the format of the date and time.|
| `utc=True`                                                        | This tells pandas to treat the datetime object as UTC time, which is a standard time zone that is not affected by daylight savings time.|
| `.dt.tz_convert("-05:00")`                                        | This converts the datetime object to the specified time zone, which is Eastern Standard Time (EST) in this case.|


Here's what the times look like now:


```python
storms_df["BEGIN_DATE_TIME"].head()
```

<pre class="output-block">0   2015-01-08 17:00:00-05:00
1   2015-01-05 22:00:00-05:00
2   2015-01-05 22:00:00-05:00
3   2015-01-05 22:00:00-05:00
4   2015-01-05 22:15:00-05:00
Name: BEGIN_DATE_TIME, dtype: datetime64[us, UTC-05:00]
</pre>


```python
storms_df.info()
```

<pre class="output-block"><class 'pandas.DataFrame'>
RangeIndex: 1315 entries, 0 to 1314
Data columns (total 11 columns):
&nbsp;#   Column           Non-Null Count  Dtype
---  ------           --------------  -----
&nbsp;0   EVENT_TYPE       1315 non-null   str
&nbsp;1   CZ_NAME          1315 non-null   str
&nbsp;2   BEGIN_DATE_TIME  1315 non-null   datetime64[us, UTC-05:00]
&nbsp;3   END_DATE_TIME    1315 non-null   datetime64[us, UTC-05:00]
&nbsp;4   CZ_TIMEZONE      1315 non-null   str
&nbsp;5   BEGIN_LOCATION   871 non-null    str
&nbsp;6   END_LOCATION     871 non-null    str
&nbsp;7   BEGIN_LAT        871 non-null    float64
&nbsp;8   BEGIN_LON        871 non-null    float64
&nbsp;9   END_LAT          871 non-null    float64
&nbsp;10  END_LON          871 non-null    float64
dtypes: datetime64[us, UTC-05:00](2), float64(4), str(5)
memory usage: 113.1 KB
</pre>

## Warm-up exercises

Here are some warm-up exercises to get started working with data that is a mix of categorical and datetime data. One helpful tip to working with datetime objects is to get the series of the datetime object and then use the `.dt` accessor to access the datetime properties. You can find all the properties of the datetime object [here :octicons-link-external-24:](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.html){:target="_blank"}.


```python
# example of getting an attribute of a datetime object

storms_df["END_DATE_TIME"].dt.day_of_year
```

<pre class="output-block">0         9
1         6
2         6
3         6
4         6
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;...
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

<pre class="output-block">0        January
1        January
2        January
3        January
4        January
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;...
1310    December
1311    December
1312    December
1313    December
1314     January
Name: END_DATE_TIME, Length: 1315, dtype: str
</pre>

The next three exercises are one-liners what will use the method `.value_counts()` to get the number of rows for each unique value in a column. This is a useful method to get a sense of the distribution of the data in a column. Below, we demonstrate by counting the number of each event type. (Compare this to the `groupby().size()` method we used last time)


```python
storms_df["EVENT_TYPE"].value_counts()
```

<pre class="output-block">EVENT_TYPE
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
Ice Storm                    3
Lightning                    3
Lake-Effect Snow             2
High Wind                    2
Funnel Cloud                 1
Blizzard                     1
Name: count, dtype: int64
</pre>

>**Exercise:** Are storms more common on weekends or weekdays? YES/NO. Display your answer by counting the number of events that happend on each day of the week. Don't worry about sorting the days of the week, just display the counts. Look at the datetime object documentation to see how to get the day of the week from the `.dt` accessor. 


```python
# Your code here
```

??? success "Solution"
    ```python
    
    storms_df['BEGIN_DATE_TIME'].dt.day_name().value_counts()
    ```

    <pre class="output-block">BEGIN_DATE_TIME
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
# Your code here
```

??? success "Solution"
    ```python
    
    storms_df[~storms_df["BEGIN_LOCATION"].isna()]["EVENT_TYPE"].value_counts()
    ```

    <pre class="output-block">EVENT_TYPE
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
>You will need to use the `pd.Timedelta()` function in your filtering criteria. Docs [here :octicons-link-external-24:](https://pandas.pydata.org/docs/user_guide/timedeltas.html){:target="_blank"} and [here :octicons-link-external-24:](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.html#pandas.Timedelta){:target="_blank"}


```python
# Your code here
```

??? success "Solution"
    ```python
    
    # Find duration of events
    storms_df['EVENT_DURATION'] = storms_df["END_DATE_TIME"] - storms_df["BEGIN_DATE_TIME"]
    
    # filter for events that last more than one day and count them
    storms_df[storms_df['EVENT_DURATION'] > pd.Timedelta(days=1)]["EVENT_TYPE"].value_counts()
    ```

    <pre class="output-block">EVENT_TYPE
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
```

??? success "Solution"
    ```python
    
    county_list = storms_df["CZ_NAME"].unique().tolist()
    print(county_list)
    print(f"There are {len(county_list)} counties in the dataset")
    event_list = storms_df["EVENT_TYPE"].unique().tolist()
    print(event_list)
    print(f"There are {len(event_list)} event types in the dataset")
    ```

    <pre class="output-block">['NOBLE', 'MADISON', 'DELAWARE', 'HENRY', 'RANDOLPH', 'MARION', 'STEUBEN', 'LAGRANGE', 'WHITLEY', 'KOSCIUSKO', 'HANCOCK', 'FAYETTE', 'WAYNE', 'FRANKLIN', 'DEARBORN', 'MARSHALL', 'LA PORTE', 'ELKHART', 'WHITE', 'GIBSON', 'PIKE', 'POSEY', 'SPENCER', 'VANDERBURGH', 'WARRICK', 'CASS', 'PULASKI', 'MIAMI', 'FULTON', 'STARKE', 'ST. JOSEPH', 'ALLEN', 'WABASH', 'HUNTINGTON', 'WELLS', 'ADAMS', 'GRANT', 'BLACKFORD', 'JAY', 'PORTER', 'TIPPECANOE', 'RIPLEY', 'UNION', 'SWITZERLAND', 'CLINTON', 'HOWARD', 'TIPTON', 'BOONE', 'HAMILTON', 'DE KALB', 'ORANGE', 'CRAWFORD', 'BROWN', 'JOHNSON', 'PERRY', 'CLARK', 'HARRISON', 'MARTIN', 'WASHINGTON', 'DAVIESS', 'RUSH', 'DUBOIS', 'MONROE', 'KNOX', 'FLOYD', 'VERMILLION', 'HENDRICKS', 'MORGAN', 'JEFFERSON', 'SCOTT', 'JENNINGS', 'PARKE', 'OWEN', 'PUTNAM', 'WARREN', 'NEWTON', 'GREENE', 'CARROLL', 'SHELBY', 'MONTGOMERY', 'FOUNTAIN', 'JACKSON', 'Vanderburgh', 'Warrick', 'JASPER', 'SULLIVAN', 'DECATUR', 'VIGO', 'LAKE', 'LAWRENCE', 'BARTHOLOMEW', 'Spencer', 'Gibson', 'OHIO', 'Pike', 'Posey', 'BENTON', 'CLAY', 'Elkhart']
    There are 99 counties in the dataset
    ['Winter Weather', 'Heavy Snow', 'Ice Storm', 'Thunderstorm Wind', 'Extreme Cold/Wind Chill', 'Flash Flood', 'Hail', 'Heavy Rain', 'Flood', 'Tornado', 'Lightning', 'Heat', 'Funnel Cloud', 'Excessive Heat', 'Dense Fog', 'Cold/Wind Chill', 'Winter Storm', 'Lake-Effect Snow', 'Blizzard', 'Frost/Freeze', 'Strong Wind', 'High Wind']
    There are 22 event types in the dataset
    </pre>

>**Exercise:** Function-writing warmup. Write a function called `get_event_county` that takes as input the storms dataframe object, a county name (as a string), and an event type (as a string). The function should return a dataframe that contains only that county and event type.
>
> This function is ideally a one-liner that filters the dataframe based on two criteria. Remember to enclose each condition in `()` and use the `&` operator to combine them.


```python
# Your code here
```


```python
# test your code
# should return a dataframe with 7 rows
get_event_county(storms_df, "ELKHART", "Thunderstorm Wind")
```

??? success "Solution"
    ```python
    
    def get_event_county(storms, county, event):
        return storms[(storms["EVENT_TYPE"] == event) & (storms["CZ_NAME"] == county)]
    
    get_event_county(storms_df, "ELKHART", "Thunderstorm Wind")
    ```

    <pre class="output-block">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;EVENT_TYPE  CZ_NAME           BEGIN_DATE_TIME  \
    572  Thunderstorm Wind  ELKHART 2015-07-18 17:55:00-05:00
    574  Thunderstorm Wind  ELKHART 2015-07-18 17:58:00-05:00
    583  Thunderstorm Wind  ELKHART 2015-07-18 18:15:00-05:00
    591  Thunderstorm Wind  ELKHART 2015-07-18 18:35:00-05:00
    592  Thunderstorm Wind  ELKHART 2015-07-13 20:47:00-05:00
    608  Thunderstorm Wind  ELKHART 2015-07-18 17:50:00-05:00
    971  Thunderstorm Wind  ELKHART 2015-08-02 23:25:00-05:00
    
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;END_DATE_TIME CZ_TIMEZONE       BEGIN_LOCATION  \
    572 2015-07-18 17:58:00-05:00       EST-5            JAMESTOWN
    574 2015-07-18 18:01:00-05:00       EST-5              ELKHART
    583 2015-07-18 18:18:00-05:00       EST-5              BRISTOL
    591 2015-07-18 18:38:00-05:00       EST-5  ELKHART MIDWAY ARPT
    592 2015-07-13 20:50:00-05:00       EST-5          MILLERSBURG
    608 2015-07-18 17:53:00-05:00       EST-5              ELKHART
    971 2015-08-02 23:26:00-05:00       EST-5               GOSHEN
    
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;END_LOCATION  BEGIN_LAT  BEGIN_LON  END_LAT  END_LON  \
    572            JAMESTOWN    41.6400   -86.0200  41.6400 -86.0200
    574              ELKHART    41.7026   -85.9467  41.7026 -85.9467
    583              BRISTOL    41.6900   -85.8200  41.6900 -85.8200
    591  ELKHART MIDWAY ARPT    41.6100   -85.8700  41.6100 -85.8700
    592          MILLERSBURG    41.5100   -85.7300  41.5100 -85.7300
    608              ELKHART    41.6800   -85.9800  41.6800 -85.9800
    971               GOSHEN    41.5800   -85.8300  41.5800 -85.8300
    
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;EVENT_DURATION
    572 0 days 00:03:00
    574 0 days 00:03:00
    583 0 days 00:03:00
    591 0 days 00:03:00
    592 0 days 00:03:00
    608 0 days 00:03:00
    971 0 days 00:01:00
    </pre>

Now that we have imported our data, cleaned it up and begun to explore it, let's split off into groups! We have a few paths we can take:

1. A guided path: We will guide you through writing functions that summarize and print the data in different ways. This will help you practice writing functions, filtering data, and practice a tiny bit of plotting. 
2. A few self-guided exploratory questions that you can approach however you want, but focus on different skills:
    * Question 1: What is the most dangerous county in Indiana? We provide a separate table of county info so you can normalize the data by county area. You will need to learn how to merge two dataframes together.
    * Question 2: What is the best time to visit Indiana if you want to take cool pictures of clouds? This will help you practice summarizing data and, depending on how you approach it, work with date time objects of various duration. 
    * Question 3: Create a plot that compares the duration in hours of each common event type. This will help you practice creating new columns and plotting data. 

## Path 1: function writing practice

1. Write a function called `storm_by_county` that takes as input the storms object, a **LIST** of county names, and returns a dataframe of all of the events that occurred in a given county and the date they began. Include an optional argument `storm_type` that by default is `None` and includes all event types, but if given a list, only includes those events.


```python
# Your code here
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

??? success "Solution"
    ```python
    
    def storm_by_county(storms, county, storm_type=None):
        if storm_type:
            matches = storms[(storms['CZ_NAME'].isin(county)) & (storms['EVENT_TYPE'].isin(storm_type))]
        else:
            matches = storms[(storms['CZ_NAME'].isin(county))]
        
        return matches
    
    storm_by_county(storms_df, ["OHIO"])
    
    print("...")
    
    storm_by_county(storms_df, ["ELKHART", "ST. JOSEPH"], ["Thunderstorm Wind"])
    ```

    <pre class="output-block">...
    </pre>

    <pre class="output-block">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;EVENT_TYPE     CZ_NAME           BEGIN_DATE_TIME  \
    281  Thunderstorm Wind  ST. JOSEPH 2015-06-11 15:26:00-05:00
    480  Thunderstorm Wind  ST. JOSEPH 2015-06-08 16:30:00-05:00
    571  Thunderstorm Wind  ST. JOSEPH 2015-07-18 17:43:00-05:00
    572  Thunderstorm Wind     ELKHART 2015-07-18 17:55:00-05:00
    574  Thunderstorm Wind     ELKHART 2015-07-18 17:58:00-05:00
    582  Thunderstorm Wind  ST. JOSEPH 2015-07-18 18:04:00-05:00
    583  Thunderstorm Wind     ELKHART 2015-07-18 18:15:00-05:00
    591  Thunderstorm Wind     ELKHART 2015-07-18 18:35:00-05:00
    592  Thunderstorm Wind     ELKHART 2015-07-13 20:47:00-05:00
    608  Thunderstorm Wind     ELKHART 2015-07-18 17:50:00-05:00
    971  Thunderstorm Wind     ELKHART 2015-08-02 23:25:00-05:00
    
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;END_DATE_TIME CZ_TIMEZONE       BEGIN_LOCATION  \
    281 2015-06-11 15:26:00-05:00       EST-5             ROSELAND
    480 2015-06-08 16:30:00-05:00       EST-5              GRANGER
    571 2015-07-18 17:46:00-05:00       EST-5          GILMER PARK
    572 2015-07-18 17:58:00-05:00       EST-5            JAMESTOWN
    574 2015-07-18 18:01:00-05:00       EST-5              ELKHART
    582 2015-07-18 18:07:00-05:00       EST-5             GLENWOOD
    583 2015-07-18 18:18:00-05:00       EST-5              BRISTOL
    591 2015-07-18 18:38:00-05:00       EST-5  ELKHART MIDWAY ARPT
    592 2015-07-13 20:50:00-05:00       EST-5          MILLERSBURG
    608 2015-07-18 17:53:00-05:00       EST-5              ELKHART
    971 2015-08-02 23:26:00-05:00       EST-5               GOSHEN
    
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;END_LOCATION  BEGIN_LAT  BEGIN_LON  END_LAT  END_LON  \
    281             ROSELAND    41.7226   -86.2559  41.7226 -86.2559
    480              GRANGER    41.7400   -86.1400  41.7400 -86.1400
    571          GILMER PARK    41.6285   -86.2971  41.6285 -86.2971
    572            JAMESTOWN    41.6400   -86.0200  41.6400 -86.0200
    574              ELKHART    41.7026   -85.9467  41.7026 -85.9467
    582             GLENWOOD    41.6700   -86.0800  41.6700 -86.0800
    583              BRISTOL    41.6900   -85.8200  41.6900 -85.8200
    591  ELKHART MIDWAY ARPT    41.6100   -85.8700  41.6100 -85.8700
    592          MILLERSBURG    41.5100   -85.7300  41.5100 -85.7300
    608              ELKHART    41.6800   -85.9800  41.6800 -85.9800
    971               GOSHEN    41.5800   -85.8300  41.5800 -85.8300
    
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;EVENT_DURATION
    281 0 days 00:00:00
    480 0 days 00:00:00
    571 0 days 00:03:00
    572 0 days 00:03:00
    574 0 days 00:03:00
    582 0 days 00:03:00
    583 0 days 00:03:00
    591 0 days 00:03:00
    592 0 days 00:03:00
    608 0 days 00:03:00
    971 0 days 00:01:00
    </pre>

2. Create a function called `display_storms` that takes a storms object, iterates through each row, and prints out each event as a sentence, including the event type, the county, and the date and time of the event. This exercise helps with iterating over data. An example output would be: "A thunderstorm occurred in Marion County on 2015-06-15 13:45:00". (as a bonus, you can try and format the date and time to be more human-readable)

**HINT:** You will need to use the `.iterrows()` method


```python
# Your code here
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

??? success "Solution"
    ```python
    
    def display_storms(storms):
        for index, event in storms.iterrows():
            print("A", event["EVENT_TYPE"], "occurred on", event["BEGIN_DATE_TIME"], "in", event["CZ_NAME"], "county.")
    
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

    <pre class="output-block">--- 3.1 ---
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
# Your code here
```

??? success "Solution"
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

    ![A barplot showing the number of Floods and Flash Floods in different counties in Indiana. The x-axis separates 'Flood' and 'Flash Flood' events, while the y-axis shows the number of events. Bars in each category are colored by county name. For Flash flood: Spencer 1, Marion 6, Vermillion 1, Monroe 0, Tippecanoe 0. For Flood: Spencer 1, Marion 4, Vermillion 1, Monroe 1, Tippecanoe 1. ](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAioAAAGxCAYAAABMeZ2uAAAAOnRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjExLjIsIGh0dHBzOi8vbWF0cGxvdGxpYi5vcmcvgI3uAAAAAAlwSFlzAAAPYQAAD2EBqD+naQAARBVJREFUeJzt3X18zvX////7gW12YhPDMGzOl7yx0YkhIXKSnOYtcjaN3qmUwoQhWlIh75yUQ5GEKPLW+136JFqJtxkVo2i9t5xlyTY7s5Pj+4ffjp+jY5uNYztes9v1cjkul47n8/l6Ph+HHB33XsfzeL1MFovFIgAAAAOq5OwCAAAACkNQAQAAhkVQAQAAhkVQAQAAhkVQAQAAhkVQAQAAhkVQAQAAhkVQAQAAhlXF2QXcjLy8PJ05c0bVqlWTyWRydjkAAKAYLBaLUlNTVa9ePVWqVPQ5k3IdVM6cOaMGDRo4uwwAAHADEhMT5e/vX+SYch1UqlWrJunqC/X29nZyNQAAoDhSUlLUoEED6+d4Ucp1UMn/usfb25ugAgBAOVOcbRtspgUAAIZFUAEAAIZFUAEAAIZVrveoAACcKzc3V9nZ2c4uAwbj4uKiypUrO2QuggoAoMQsFovOnTunS5cuObsUGFT16tXl5+d309c5I6gAAEosP6TUrl1bHh4eXHQTVhaLRenp6fr9998lSXXr1r2p+QgqAIASyc3NtYaUmjVrOrscGJC7u7sk6ffff1ft2rVv6msgNtMCAEokf0+Kh4eHkyuBkeX//bjZPUwEFQDADeHrHhTFUX8/DBFUkpKSdOjQIaWlpTm7FAAAYCBO3aOSlpam8PBwbdu2TUFBQfr99981c+ZMhYeHO7MsAEA5dfbsWX300Uc6ceKEPDw8FBQUpCFDhsjT01OSNH78+CKPX7lypapUKfqjcc+ePXrvvffUqVMnjRkzxtqel5en8PBwTZo0SW3btrU55rnnnlNeXp5ef/31Qudr2rSppk+fbtP3008/6ZVXXpGHh4feeOMNm/EFefPNN+Xm5lZk/eWNU4PKyJEj9dNPP+nkyZOqW7eusrKytH79emeWBAAop8xms5588kndf//96tq1q3Jzc7V3717NnTtX//73v9WiRQvdfffddsdduXJF06dPl4+PT7G+roiLi5PZbNbGjRv1wAMPyM/PT9LVoGI2m9WvXz+boLJ//3698cYbMplMGjJkiDp27Gg337p162QymTR69GibX8msWLFC77//vtzc3KxBJS4uTmvXrtWKFSvsanPUtUuMxGlB5dChQ9q2bZs+//xz678UNzc3hYWFOaskAEA5tWfPHoWHh2vFihV2Z+UvXrwoi8UiqeAzKuHh4crOztbHH39c7A96b29vNWnSRHPmzNHKlSuLHGs2mzVgwADrP/81qEhXN5527NhR69at07Rp0yRdDVDr16/XoEGDtHPnTpvxlStXvu7ZoVuF04LK//3f/8nDw0PdunXTqVOnlJ6erqZNm1p/0lSQrKwsZWVlWZ+npKSURamGlZCQoKSkJGeXUShfX181bNjQ2WUAqAAWLVqk1q1b67HHHrPrq1GjRqHHvfnmm3r77be1fv16tW/fvtjrmUwmLVy4UH369NEzzzyjFi1aFDguLS1NGzdu1EcffSRJGjBggJYsWaJq1arZjR03bpxeeOEFa1D5+OOP5evrq3vuuccuqFQkTgsqZ86cUe3atfXwww8rNjZWVatW1W+//aZFixZpwoQJBR4TFRWluXPnlnGlxpSQkKCgli2UnpHp7FIK5eFeVXHHTxBWAJS6ffv2adiwYSX6pcnevXv1zDPP6LnnntOIESNKvGb+V0wzZszQ1q1bCxyzadMm1apVS927d5ck+fn5aePGjQUGqv79++vxxx9XdHS0OnXqJLPZXOi3DDk5OXZnVOrXr39LfkY6Lai4uLjo119/1ahRo6z/gt955x2NHz9eHTt2VOvWre2OiYiI0LPPPmt9npKSogYNGpRZzUaSlJSk9IxMrQ9vq6C6Xs4ux07c2csa+dZhJSUlEVQAlLqUlBTVrl272OMTEhI0ZMgQ3XfffXr55ZdveN2FCxeqQ4cO2rdvnzp06GDXbzabNX78eGuAeuyxx2Q2mwsMKq6urnr00UdlNpvVoEED7d27V+vXr9fmzZvtxppMJrv9NkWdOSrPnBZUAgICJEkTJ060to0ZM0b/+Mc/9M033xQYVNzc3G653cw3K6iul4IDfJxdBgA4Ve3atZWQkFCssenp6XrooYfk4+OjjRs33tQG1ODgYA0bNkxTp07V7t27bfri4uL07bffqlatWtazHxcvXtT+/fv1448/6o477rCbLywsTHfddZeqV6+uPn36FBq+2KNSBnr27CmTyaTTp09bN9NeuHBB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M8+oefPmZVZrPqcFlT/++EMjR45UUFCQqlevrt27d8vDw0ObN292VkkAAAfwaeAj32a+zi7DzsCBA1W9enWtXbtW06dPt7abzWY1btxY9913303N7+Lioho1auj333+36wsJCdG+ffu0ZcsWPfroo7py5Yree+89bdu2rUyDyn/+8x/Fx8frgw8+sIaUfMOHD9f8+fO1fPlym6DSs2dP/fnnn5oxY4a2bNlSZrXmc9qvfnr27KkDBw5ozJgxCg0N1Zo1a/T999+rVatWzioJAHALc3V11aOPPqo1a9ZY265cuaL169crLCzM7oN78eLF6tSpk81j//79hc4fHR2t+Ph4hYaGFtgfFhYms9ksSdq2bZtq1qxZ6NjSEhsbq0qVKqldu3Z2fSaTSe3atSvwBy0LFy7Uxx9/rO+++64syrTh1D0q1apVK/J7NQAAHCksLExLlizR119/rc6dO+uTTz7Rn3/+qTFjxtiNfeihh+z2qLRo0cLm+eLFi7Vx40ZdvnxZx44d0wsvvKBHH320wLVHjBihqVOn6tSpU1q9erXCwsIc9rqKKzMzU25ubta9OH/l4+OjzMxMu/bg4GA9/PDDmjp1qvbu3VvaZdow1GZaAABK0x133KG77rpLa9asUefOnWU2m9W7d2+bX6HmK84elfwwk5SUpKioKO3evVsvvPBCgT/8qFGjhh566CFFRkZqz549eu+99xz2uorL399fGRkZOn/+vOrUqWPXHx8fL39//wKPXbBggVq2bKkdO3aUdpk2uHsyAKBCCQsL04cffqhjx47p888/v6kzG/lhZsCAAfr00091/PhxvfTSS0Wu/f7776t3794FBoXS1rt3b1WuXLnAkPTbb79p9+7devDBBws8tnHjxpo4caIiIiKUm5tb2qVaEVQAABXK8OHDZTKZNHToUNWuXdt6/ZKbVbNmTc2ePVuvvvqqzp49W+CYHj16KDo6Wm+++aZD1iypwMBATZ48WfPnz9fu3but7UlJSRo9erQCAwM1adKkQo+fNWuWEhISynRTLV/9AAAcKjkx2dDreHl56eGHH9aaNWs0bdo0ValS8Edh/v6Ta/Xp00czZswodO6JEydq6dKlmjNnjlatWmXXbzKZbmgDbUG1XHuRuOv1X2vRokWqUaOGBg4cqNq1a8vb21txcXG6//779dVXX8nLy6vQOmrVqqXn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objjcdcNK/v27dOcOXOsz0+cOCFXV1cFBgZa25YvX64777xTnTt31ssvv6xJkyZJkjp37qyaNWuqVq1aSklJUWJiop588km98sorJe6/Vnh4uMLDw63P3377bb344ovKyMiQn5+fEhMTFRQUpJdeekn33XefzbERERF6++23NWPGDC1YsMDu9Xbu3FlpaWn69NNP1bt3b2v7a6+9poMHDyo6OtratmTJEr300ktyc3OTt7e34uPj9dBDD+mf//ynatasaTNncV6HoxFUAAAOkZSUpPSMdE1+5EX51wm8/gE36bfz8VqyYZaSkpKuG1T69eunfv36WZ937dpV/v7+Wr9+fbHWev75563BZefOnXrwwQfVrl07DR8+vMT9BZk7d64WLVqkd999V4MHD5bJZJIkHTx4UN9++61NUElLS9PGjRs1fPhwvfvuu5o3b54qV65sN2etWrU0ffp09erVS5UqFbzT44UXXtAbb7yhTZs2qU+fPpKkM2fOaNiwYeratav2798vDw+PAv8cygpBBQDgUP51AtXEP8jZZZSavn37KiAgQN988401iJSk/68SEhI0f/58zZs3T0OGDLHpa9++vdq3b2/TtmnTJtWsWVNvv/22/P399emnn+rBBx+0m3fy5Ml6+eWXtX79eo0aNarAdV955RXNmzfPGlKkq1/lrF+/Xs2bN9fy5cv13HPPXfc1lCY20wIAUALZ2dm6dOlSgXtDCutPSEjQwYMHbR4pKSmSpE8//VQ5OTkaO3ZssdY3m80KCwuTp6enRo4cKbPZXOC42rVra8qUKZo1a5aysrLs+otat1GjRuratau2b99u017U6ygtnFEBAOA68j+gU1NTtXLlSmVkZGjEiBHF7t+0aZO+/PJLmzmXLVume+65R4mJiXJ3d5efn99164iLi9OBAwe0efNmSVf3hwQHB+vcuXMFHj9lyhStWLFCy5YtszszkpCQUOS6jRs31qeffmrTVtTrKC0EFQAAriP/A9rT01PNmzfX/v37dfvttxe7v6i9HW5ubsrKytKVK1fk6upaZB1ms1nBwcE6e/aszp49K0kKDAzU2rVrNW3aNLvxXl5emjVrlmbNmqXx48eXaN3U1FS5ubnZtLFHBQAAA7reB/TNfIC3adNGeXl5+uGHHxQSElLouOzsbL333nuqXbu2Jk6caG2vUqWKzGZzgUFF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bg0fPlzu7u5KTU1V/fr19cknn6hRo0bOLAsAABiE086opKSkaOjQoRo9erTi4+N19uxZ1axZU48++qizSgIAAAbjtKCyfft2paSkKCIiQpLk4uKiadOm6euvv9bJkyedVRYAADAQp331Exsbq8aNG6t69erWtjvvvNPa17RpU7tjsrKylJWVZX2enJws6erZGUe7fPmyJOni/04oJyvD4fPfrOTTP0uS4s6mau+JP5xcjb0jCamSpOSEZJ39/qyTq7GXcvrq35mYmBjrv2ujqVSpkvLy8pxdRqH8/Pzk5+fn7DJuCu/zm2P09/mlXy5Jkk4mJ+vAuXPOLaYQxy5dkiSd/v1XHT0V49xiCnD6wv8kXX2vOPKzNn8ui8Vy/cEWJxk9erSlY8eONm15eXmWSpUqWVauXFngMZGRkRZJPHjw4MGDB49b4JGYmHjdvOC0MyouLi7KzMy0abty5Yry8vLk6upa4DERERF69tlnrc/z8vJ08eJF1axZUyaTqVTrhXOlpKSoQYMGSkxMlLe3t7PLAVAKeJ9XHBaLRampqapXr951xzotqDRq1Eg7duywaTt9+rQkqWHDhgUe4+bmJjc3N5u2a786wq3P29ub/4ABtzje5xWDj49PscY5bTPt/fffr/Pnz+vAgQPWtu3bt8vLy0v33HOPs8oCAAAG4rQzKnfddZcGDhyoESNGaP78+bp48aJmzZqlyMhIeXh4OKssAABgIE694NsHH3ygJUuWaM2aNXJzc9OqVas0YsQIZ5YEg3Jzc1NkZKTdV38Abh28z1EQk8VSnN8GAQAAlD2n3+sHAACgMAQVAABgWAQVAABgWAQVlMiECRO0evVqh803atQobdiwwWHzSY6vsSjPPPOMli9fXiZrAeUZ70vcKKf+6gfG89xzzyk6OtqufdOmTWrUqJGOHj2qunXrOmy977//Xn/7299KdExZ11iUuLg4fqEAiPclSg9BBTaOHz8uDw8PvfTSSzbtderUcVJF9spDjUBFw/sSpYWgAjs1atTQ3XffXayxM2bM0JdffimTyaRatWqpS5cueuqpp2zu13T06FEtWbJEp06dUqNGjfTEE0+offv21v7s7Gy9+uqr2rNnj6pUqaKxY8eqf//+DqtRktauXastW7YoNTVV7du319SpU1W7du0SjbFYLFq2bJm2b9+umjVratCgQcVeH6gI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)

5. Write another function called `summarise_storms` which takes as input the storms object you created, a list of counties, and an optional list of `storm_type` that displays only certain storm types (aka the same arguments as `storm_by_county`). Instead of returning every event, it returns a dataframe summarizing the number of occurences of each event in those counties. **HINT** You may want to use your previous function `storm_by_county` to avoid repeating code!


```python
# Your code here
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

??? success "Solution"
    ```python
    
    def summarise_storms(storms, county, storm_type=None):
      df = storm_by_county(storms, county, storm_type).groupby(["CZ_NAME","EVENT_TYPE"]).size().reset_index()
      
      return df
    
    # 5.1 Display the number of all events in PIKE county
    print("--- 5.1 ---")
    print(summarise_storms(storms_df, ["PIKE"]))
    
    # 5.2 Display the number of Thunderstorm Wind events in the following counties: ELKHART, LA PORTE, BOONE
    print("--- 5.2 ---")
    print(summarise_storms(storms_df, ["ELKHART", "LA PORTE", "BOONE"], ["Thunderstorm Wind"]))
    ```

    <pre class="output-block">--- 5.1 ---
    &nbsp;&nbsp;CZ_NAME       EVENT_TYPE  0
    0    PIKE  Cold/Wind Chill  2
    1    PIKE        Dense Fog  5
    2    PIKE            Flood  6
    3    PIKE     Frost/Freeze  1
    4    PIKE       Heavy Snow  1
    5    PIKE     Winter Storm  2
    6    PIKE   Winter Weather  3
    --- 5.2 ---
    &nbsp;&nbsp;&nbsp;&nbsp;CZ_NAME         EVENT_TYPE  0
    0     BOONE  Thunderstorm Wind  7
    1   ELKHART  Thunderstorm Wind  7
    2  LA PORTE  Thunderstorm Wind  5
    </pre>

6. Use your function to summarize the total counts of each weather event in each county.


```python
# Your code here
```

??? success "Solution"
    ```python
    
    all_weather = storms_df["EVENT_TYPE"].unique().tolist()
    all_counties = storms_df["CZ_NAME"].unique().tolist()
    
    summarise_storms(storms_df, all_counties, all_weather)
    ```

    <pre class="output-block">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CZ_NAME               EVENT_TYPE  0
    0      ADAMS  Extreme Cold/Wind Chill  1
    1      ADAMS                     Hail  1
    2      ADAMS               Heavy Rain  1
    3      ADAMS               Heavy Snow  1
    4      ADAMS           Winter Weather  5
    ..       ...                      ... ..
    473  WHITLEY               Heavy Snow  2
    474  WHITLEY           Winter Weather  5
    475  Warrick                Dense Fog  1
    476  Warrick           Excessive Heat  1
    477  Warrick                     Heat  3
    
    [478 rows x 3 columns]
    </pre>

## Self-guided exploratory questions

Here are a few questions we've come up with that can be approached in multiple different ways.

**Question 1:** What is the most dangerous county in Indiana, assuming danger only comes from the storm events? You will need to account for the area of each county to answer this question. We've provided code to get the table from wikipedia that lists county information. 


```python
!pip install lxml
county_info = pd.read_html("https://en.wikipedia.org/wiki/List_of_counties_in_Indiana", storage_options={"User-Agent": "Mozilla/5.0"})
county_info = county_info[1]
```

<pre class="output-block">Collecting lxml
</pre>

<pre class="output-block">&nbsp;&nbsp;Downloading lxml-6.1.3-cp311-cp311-manylinux_2_26_x86_64.manylinux_2_28_x86_64.whl.metadata (3.3 kB)
</pre>

<pre class="output-block">Downloading lxml-6.1.3-cp311-cp311-manylinux_2_26_x86_64.manylinux_2_28_x86_64.whl (5.2 MB)
[?25l   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m0.0/5.2 MB[0m [31m?[0m eta [36m-:--:--[0m
</pre>

<pre class="output-block">
[2K   [91m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m[90m╺[0m[90m━━━[0m [32m4.7/5.2 MB[0m [31m26.8 MB/s[0m eta [36m0:00:01[0m
</pre>

<pre class="output-block">
[2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m5.2/5.2 MB[0m [31m16.8 MB/s[0m  [33m0:00:00[0m
[?25h
</pre>

<pre class="output-block">Installing collected packages: lxml
</pre>

<pre class="output-block">Successfully installed lxml-6.1.3
</pre>

You will need to do some data cleaning to get the county names to match up and to extract the area of each county. Then you will need to merge the two dataframes together. 


```python
county_info[["County", "Area[3][12]"]]
```

<pre class="output-block">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;County            Area[3][12]
0         Adams County    339 sq mi (878 km2)
1         Allen County  657 sq mi (1,702 km2)
2   Bartholomew County  407 sq mi (1,054 km2)
3        Benton County  406 sq mi (1,052 km2)
4     Blackford County    165 sq mi (427 km2)
..                 ...                    ...
87   Washington County  514 sq mi (1,331 km2)
88        Wayne County  402 sq mi (1,041 km2)
89        Wells County    368 sq mi (953 km2)
90        White County  505 sq mi (1,308 km2)
91      Whitley County    336 sq mi (870 km2)

[92 rows x 2 columns]
</pre>


```python
# Your code here
```

??? success "Solution"
    ```python
    
    # cleaning county_info
    county_info["County"] = county_info["County"].str.replace(" County", "").str.upper()
    county_info["Area_sq_mi"] = pd.to_numeric(county_info["Area[3][12]"].str.extract(r'([0-9,]+)')[0])
    
    # merge the two dataframes
    storms_merged = pd.merge(storms_df, county_info, left_on="CZ_NAME", right_on="County")
    ```

??? success "Solution"
    ```python
    
    # grouping by county and area
    df = storms_merged.groupby(["CZ_NAME", "Area_sq_mi"])["EVENT_TYPE"].count().reset_index()
    print(df.head())
    
    # normalizing number of events by area
    df["normalized"] = df["EVENT_TYPE"] / df["Area_sq_mi"]
    
    # sorting by normalized value
    df.sort_values("normalized", ascending=False)
    ```

    <pre class="output-block">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CZ_NAME  Area_sq_mi  EVENT_TYPE
    0        ADAMS         339           9
    1        ALLEN         657          31
    2  BARTHOLOMEW         407           7
    3       BENTON         406           4
    4    BLACKFORD         165           6
    </pre>

    <pre class="output-block">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CZ_NAME  Area_sq_mi  EVENT_TYPE  normalized
    79  VANDERBURGH         233          34    0.145923
    20        FLOYD         148          19    0.128378
    46       MARION         396          41    0.103535
    9         CLARK         373          37    0.099196
    33   HUNTINGTON         383          37    0.096606
    ..          ...         ...         ...         ...
    10         CLAY         358           2    0.005587
    26       GREENE         543           3    0.005525
    7       CARROLL         372           2    0.005376
    44     LAWRENCE         449           2    0.004454
    74     SULLIVAN         447           1    0.002237
    
    [90 rows x 4 columns]
    </pre>

**Question 2:** What is the best time to visit Indiana if you want to take cool pictures of clouds? The main idea of this question is to summarize the data in such a way that you can tell which month or week or your choice of span of days has the highest concentration of events of interest. 


```python
# Your code here
```

??? success "Solution"
    ```python
    
    # decide which weather events probably have cool clouds
    cool_clouds = ["Thunderstorm wind", "Tornado", "Lightning", "Heavy Rain"]
    
    # filter for cool clouds
    df_clouds = storms_df[storms_df["EVENT_TYPE"].isin(cool_clouds)]
    
    # group by month and number of events
    df_clouds.groupby(df_clouds["BEGIN_DATE_TIME"].dt.month)["EVENT_TYPE"].count().reset_index()
    ```

    <pre class="output-block">&nbsp;&nbsp;&nbsp;&nbsp;BEGIN_DATE_TIME  EVENT_TYPE
    0                 1           1
    1                 2           1
    2                 3           4
    3                 4           9
    4                 5           1
    5                 6          14
    6                 7          12
    7                 8           1
    8                10           2
    9                11           1
    10               12           8
    </pre>

**Question 3:** Create a plot that compares the duration in hours of each common event type. Some events occur only infrequently, so your first step would be to filter those out. Then, you will need to decide what type of plot to make. Take a look at the [seaborn gallery :octicons-link-external-24:](https://seaborn.pydata.org/examples/index.html){:target="_blank"}. If you are having trouble deciding how to represent your data, take a look at this [infographic :octicons-link-external-24:](https://github.com/Financial-Times/chart-doctor/blob/main/visual-vocabulary/poster.png){:target="_blank"}


```python
# Your code here
```

??? success "Solution"
    ```python
    
    # get event duration. We've already done this, but the code is reproduced before
    
    storms_df["EVENT_DURATION"] = storms_df["END_DATE_TIME"] - storms_df["BEGIN_DATE_TIME"]
    
    # filter out events which only occurred <10 times in the year
    
    storms_filtered = storms_df.groupby("EVENT_TYPE").filter(lambda x: len(x) > 10)
    
    # group by event type and calculate average duration
    
    print(storms_filtered.groupby("EVENT_TYPE")["EVENT_DURATION"].mean())
    
    storms_filtered.groupby("EVENT_TYPE")["EVENT_DURATION"].describe()
    ```

    <pre class="output-block">EVENT_TYPE
    Cold/Wind Chill                  0 days 09:00:00
    Dense Fog                        0 days 07:27:00
    Extreme Cold/Wind Chill   0 days 12:20:46.153846
    Flash Flood               0 days 02:13:29.256198
    Flood                     4 days 01:25:38.880000
    Hail                      0 days 00:01:21.818181
    Heat                             0 days 05:24:00
    Heavy Rain                0 days 02:08:44.444444
    Heavy Snow                0 days 16:16:49.923664
    Thunderstorm Wind         0 days 00:00:41.984334
    Tornado                          0 days 00:02:35
    Winter Storm              0 days 16:39:05.454545
    Winter Weather            0 days 12:19:15.185185
    Name: EVENT_DURATION, dtype: timedelta64[us]
    </pre>

    <pre class="output-block">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;count                    mean                     std  \
    EVENT_TYPE
    Cold/Wind Chill            12         0 days 09:00:00  0 days 02:05:20.154737
    Dense Fog                  40         0 days 07:27:00  0 days 03:16:24.370352
    Extreme Cold/Wind Chill    26  0 days 12:20:46.153846  0 days 04:00:33.883213
    Flash Flood               121  0 days 02:13:29.256198  0 days 03:20:21.201559
    Flood                     125  4 days 01:25:38.880000  7 days 03:59:43.207680
    Hail                      187  0 days 00:01:21.818181  0 days 00:01:23.851565
    Heat                       15         0 days 05:24:00  0 days 00:49:41.083216
    Heavy Rain                 27  0 days 02:08:44.444444  0 days 03:40:57.113426
    Heavy Snow                131  0 days 16:16:49.923664  0 days 06:48:08.251044
    Thunderstorm Wind         383  0 days 00:00:41.984334  0 days 00:01:27.395291
    Tornado                    24         0 days 00:02:35  0 days 00:02:03.745882
    Winter Storm               33  0 days 16:39:05.454545  0 days 05:00:36.440386
    Winter Weather            162  0 days 12:19:15.185185  0 days 05:43:50.386658
    
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;min              25%              50%  \
    EVENT_TYPE
    Cold/Wind Chill          0 days 07:00:00  0 days 07:00:00  0 days 09:00:00
    Dense Fog                0 days 04:00:00  0 days 05:00:00  0 days 05:00:00
    Extreme Cold/Wind Chill  0 days 03:00:00  0 days 12:00:00  0 days 12:00:00
    Flash Flood              0 days 00:00:00  0 days 00:00:00  0 days 01:51:00
    Flood                    0 days 00:00:00  0 days 01:30:00  0 days 02:18:00
    Hail                     0 days 00:00:00  0 days 00:00:00  0 days 00:02:00
    Heat                     0 days 05:00:00  0 days 05:00:00  0 days 05:00:00
    Heavy Rain               0 days 00:00:00  0 days 00:00:00  0 days 00:00:00
    Heavy Snow               0 days 08:00:00  0 days 11:37:30  0 days 15:00:00
    Thunderstorm Wind        0 days 00:00:00  0 days 00:00:00  0 days 00:00:00
    Tornado                  0 days 00:00:00  0 days 00:01:00  0 days 00:02:00
    Winter Storm             0 days 11:00:00  0 days 12:30:00  0 days 15:00:00
    Winter Weather           0 days 00:01:00  0 days 07:15:00  0 days 11:00:00
    
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;75%               max
    EVENT_TYPE
    Cold/Wind Chill          0 days 11:00:00   0 days 11:00:00
    Dense Fog                0 days 10:00:00   0 days 13:00:00
    Extreme Cold/Wind Chill  0 days 12:00:00   1 days 06:00:00
    Flash Flood              0 days 03:30:00   1 days 03:35:00
    Flood                    3 days 19:00:00  29 days 09:00:00
    Hail                     0 days 00:02:00   0 days 00:10:00
    Heat                     0 days 05:00:00   0 days 07:00:00
    Heavy Rain               0 days 03:00:00   0 days 12:15:00
    Heavy Snow               0 days 15:00:00   1 days 10:00:00
    Thunderstorm Wind        0 days 00:01:00   0 days 00:11:00
    Tornado                  0 days 00:03:15   0 days 00:08:00
    Winter Storm             0 days 20:00:00   1 days 02:00:00
    Winter Weather           0 days 17:00:00   1 days 06:00:00
    </pre>

??? success "Solution"
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

    ![A strip plot showing the duration of different events in hours in hours on the x-axis, ranging from 0 to 35. The y-axis shows the event type. Event types are 'Winter Weather', 'Heavy Snow', 'Thunderstorm Wind', 'Extreme Cold/Wind Chill', 'Hail', 'Heavy Rain', ''Tornado', 'Heat', 'Dense Fog', 'Cold/Wind Chill', and 'Winter Storm'. Winter Weather and Heavy Snow span the range of durations, while Winter Storms last between 10 and 26 hours. Thunderstorm Wind, Hail, and Tornados have short durations, less than 1 hour. There are few Extreme Cold/Wind Chill events, mostly around 13 hours long. Heat, Dense Fog, and Cold/Wind Chill events all last between 4 and 13 hours.](data:image/png;base64,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1kk8XyYGuhjXzkmykM1vfkVF3e+wuAx25uf3lB/Tu7sojSbLoPkPukDWtyKqFMa3IkUlP3+PKPdYMBcxLy8vDBs2DFOnToWBwf/+2LRo0QLDhw/H5MmTFebifvjgknLlymHYsGHifZmzDR48WGEO7f79+1GvXj34+/vj4sWLAIClS5fi4MGDkMvlCAwMhJ2dHS5evIiaNWtKtq3OiBEjMGzYMKW7VQwaNAjDhg3D559/rhAfM2YMrl+/DltbW1y5cgVGRkbYu3cvunfvDgCoUKECrly5gnr16uHSpUuoXbs2zpw5g2HDhomj5gDw559/on///jh//rw4Yj5gwABUr15dob8uXbqgQYMGue5fXTukPV3VFDTd6qkvdNSNJub0pltDzSiWo6X6ufP5GbnMzwgpAPi0Ud2mT1v1fS0a0DBP8fzuA2QVpfvGt0TInK7YN75lrorRn/vUz1M8W35GffOTX1H5PB+/2/z838iv/P6e8qrL/z/BU+GDjXfhfLApjRdWl8ZjKk74aGwiDSiMR2NTFp9NgTgWEgO5kDXi1sXVGiuHS98b2y84Jl8XTHot8sfD9y7ic7Qsh1PftNN4XwuO3MvXvNj87Jef/PJ7/vKjKPsqzvLzu83P/438Ko2/Jx4TAbl//2bBTKQBLJiJiIhKnty+f3NKBhERERGRBBbMREREREQSWDATEREREUlgwUxEREREJIEFMxERERGRBBbMREREREQSWDATEREREUlgwUxEREREJIEFMxERERGRBBbMREREREQSWDATEREREUlgwUxEREREJIEFMxERERGRBBbMREREREQSWDATEREREUlgwUxEREREJIEFMxERERGRBBbMREREREQSWDATEREREUnQ03YCRESkml9wDFb4hyE0Ngm1rUwxzqsmurhaazstrVtw5B7+ufAIKemZMNbXxcgW1TGtWx1tp0VEpZhMEARB20kQlXQJCQkwNzdHfHw8ypcvr+10qJjz2RQIv5AYCAIgkwFd6lpjlbebwjZ+wTH4fFOg0r7VLUwQm5AKq/KGAIDYhFTJYvr9oju3+xSlvBa/C47cw8rT4UrxL9o6sWjOpeL8Qaw451bU+MGwaOT2/ZsFcynStGlTtG3bFr/99ptCfMWKFZg6dSqSkpK0lFnuPXnyBLNmzUJAQADi4+NRt25djB07Ft7e3tDTK75fiLBgLrvy+gbvsykQR4NjlOJdXRWL5t7LzuFWZHyu85DJgFXD3RT6Vld0S+2Tn2PKr/wUvzW+OwRVb1oyAA9/7aHZBIu5/PyeVL0msl8HALRarErlVpKL5vwUvvxg+D+F/fcot+/fnMNcimRkZCAzM1MpLpfLkZGRoYWM8iYtLQ2dOnXCy5cvcfToUTx9+hRLly7FhQsXcOzYMW2nR6Qk+w3+VmQ8UtIzcSsyHp9vCoSfioJY3CdE9bpjH8RDY/P2AVcQgM83BcJl1lEsOHIPQFbxk9M+KwIU35Tzc0zZ+/Vedg4us46i97JzOW4PAKtVFARScQAqi2WpeGml6vfk45vz70nVa0IQgPmH7+arvfz83vOa24evUW3K6/FmF74p6VnvzSnpmVh5Olz8P6rO2rMReYqXVvl9nRcGFsxlVGpqKqZOnQp7e3uYm5ujRYsWOHXqlMI2rVq1gp6eHvT19WFvb4+xY8ciLi5OXD9hwgR06dJFqe2GDRvixx9/xFdffYUOHToora9Xrx7mzp2rFL9z5w5CQ0Pxyy+/wMXFBWZmZnB3d8fatWvRvXt3cTtra2v88ssv6NmzJypXrowaNWpgxYoVCm29fv0an3zyCSpXrozy5cujR48eCA0NFdcvWLAArVq1Epd3794NPT09rF27Voz17t0b06ZNkzqNVMbNP3w3T3EgqwBQRf5BvLaVab5yev8N+W50Yo7bP4hV3CY/x5TfNzV5HuP0P/ktLtV9EHvyOjnP7Wm6mFGX24evUW3Jz/H+c+GRyvjGi6rj2TI+/IOQQ7y0Kk4folgwl1HDhg3DjRs3cPToUTx58gRffPEFevbsieDgYHGb06dP4927d0hOTsbx48cRHh6OcePGiesHDx6MEydOIDo6WozdunULt2/fxpAhQzBq1Cj4+/sjIuJ/n4gvXLiAkJAQjBgxQiknc3NzAFAq3D+UkZGBxYsXY9y4cQgLC8Mvv/yCCRMm4Pr16wrHd+/ePZw9exYhISEoV64cunTpgtTUVABA69atcfnyZXGayqlTp1ChQgWxb7lcjtOnT6N169a5PqdU9jxWUWQAqouPvBrnVRMyWf7333jxEXR1cm6glpWZwvKjV6pzVxcHitebWlmR3+Iyrx/EpNrT9O89e479h6qYqY4Xtfwcb/bI8oeS01THSZG6D/33ohOKOBMWzKXOn3/+CT09PYWfSZMmKWxz584d7N69G76+vqhbty7Mzc3h7e2NLl26YOPGjeJ2urq64gizs7MzFixYgF27donTPlq2bAl7e3ts27ZN3Gfz5s1o2rQpnJ2d0bBhQ7i5uWHDhg3i+vXr16NDhw5wcHBQyt3JyQkzZszAN998A0dHR3h7e2Pt2rV48eKF0raTJk1C9+7dYW5ujiFDhqBOnTo4d+4cgKyi/ejRo1izZg3q1KmDatWqYe3atXj58qWYq7u7OwwNDcV9AgICMHnyZAQEBAAArl+/jsTERLUFc2pqKhISEhR+qAxSM9gjdWWIuhr2w3gXV2usGu6GhnYVYGKgm+fUktMykZ4pPVYrkwHj2znlue0PqXtTu6uFN7WyQl3h++EHoA+1cLJUGbcwNchze8V9RFjTgqNUv56Dn+X+WgPSDG2Ms7NgLmUmTpyId+/eKfz88ccfCttcu3YNgiDAwcEBRkZGMDQ0hIGBAfbt26cwGuzv7w8vLy9UrlwZ+vr68PT0RHp6OmJisr5+kslkGDp0KDZv3gwAEAQBW7duxfDhw8U2xowZg40bN0Iul+Pt27fYvn07Pv30U7X5z5s3Dw8ePMCUKVMAAN9//z1q1aolFrLZateurbBcqVIlcbpIcHAwjI2N0bBhQ3G9ubk5XF1dERISAgDQ19dHixYtEBAQgJcvXyI0NBQTJkzAu3fvcO/ePQQEBKBx48biqPeH5s+fD3Nzc/HHzs5O7TFR6aVuBFdqZFfdN6qq4l1crbFvfEuEzOma59x0ZNJf3za0q4DVw93QWQMXz6g7Xr1cjHBT/qj6BiI3H4AuhL9UGS9noJfn9jQ9IhybkKoy/jxRdbyoqfv/lFkI0yRy+8G6tEtT86E/PaPoJ26xYC5lZDKZ0gizjo7irzkzMxNGRkaIj49HUlIS3r59i+TkZKSlpWH79u0AgKioKPTs2RPdunXDzZs3kZSUhGvXrgEA0tPTxbaGDRuGwMBAsciMjo7G4MGDxfVDhw7F69evcfz4cezYsQO6urro27ev5DE4Ojpi/Pjx2LRpEx4+fIhatWrhu+++UzrOD71/wxdV62UymcI27dq1g7+/PwICAtC0aVOUL18erVu3FmPt2rVTm+P06dMRHx8v/jx9+lTymKh0UvdGWRhvoHkllYIMwL7xLTVSLAPF+zyUVh9+A5HbD0DqRoWfJ6bmqz1Nyu+oubYVxqvcSF/1t0rq4qWVug8IBZmull/F9z5dVGgaNWqEd+/e4eLFi2qLwhs3bkAmk2Hq1KkKsQ/VrVsXjRs3xubNmxEdHY1OnTrByspKXG9mZoaBAwdiw4YNiI6OxtChQ2FkZJTrXMuVK4fmzZvj6NGjud7HxcUFycnJCA4OhqurKwAgKSkJISEh+Oyzz8Tt2rVrh9mzZ+PAgQPieWjXrh1OnjyJc+fOwcfHR20fhoaGMDQsHvPqSItkUPluKfXHXE9HpnKkSlOjsToy6WIZ0PybjYuNmcpb4NWx4S0WC1MXV+s8316rtpWpyt9VLSuzPLen6RHhcV414eMbqDClSVPThkoadXOcy9rcZ/tKJiqvn7CvZFLkuXCEuQxyc3NDz549MWbMGJw5cwapqakIDw/H3Llz8d9//wEAatasiZSUFPz3339IS0vD2bNnMXPmTJXtDRs2DL6+vti1a5fCdIxsY8eOxZ49e3D27FnJ6RjXrl3DkCFDcPr0abx58wYpKSk4cuQItmzZgo8++ijXx9e4cWN06NABPj4+ePz4MV69eoVx48bB3NxcYfTb3d0dRkZG2LJlC7y8vABkFcz79u2TnL9MlM1BzR9te4tyavfRUVOt5nSBXm6+5jYx0IWhXs4jUFL55Ud+pwdQ0dPk70rTI8L5HTUvKur+DxaXixJLo+ndXfDhX0YZgBndXYo8FxbMZdT27dvx8ccfY+jQoTA1NUXXrl0hl8vRo0fWjf+dnZ2xfPlyfP311zAxMcFnn32GL7/8UmVbQ4YMwZMnT5Ceno4+ffoorff09ETNmjXRoEEDuLm5KTfw/xo3boy+fftizpw5cHR0hIWFBb7++mtMmjQJv/76a56Ob+vWrbC1tYWrqytsbW0RGRmJI0eOwNjYWNwmex6zTCZDy5YtAWSNvpuamkrOXybKNl3NH+0ZEg8WcLFRXUzkNBo7t0+9HPOpZWWWq7sgSOXX2K6CyngTe9VxIP+FjrpRdc59LjyaLEoL44PS+/P2NTltSBPU/R/8WeL/prGaKRQ5XchroKu6PDPQK1tlW5f/f6CTwuvVWzsfovikv1IkMzMTMplMac6yIAiQy+XQ1S343KeMjAyVT9zLvnOGqj4yMzPh4OCAadOmYeLEiQXOITMzEzo6OgrzlNUde07kcjkEQVDIOz9t8Ul/ZZdfcAxWBITjQWwialmZYXw7J8k/5n7BMSq/ds5N0ZLd173oBKR+cNFLdhsCoNQ+kPVG62JTPsf8AKDv8vO48fSNuNzEvgJ2j2spuU9+qHua2bh2TpjaVXVRr+5Jid3qWWPlcPUfyKlw5PX1X9Ll9Xjz8xovyH6Ud3w0NhUby5cvx/fff4+nT5/CzKx4X7yRXyyYKS80UWRItVGSipgFR+5h48VHSE7LhIlB1mODcyoIfDYF4lhIDORC1pztLq4slqn4ys9rvCD7Ud6wYCate/XqFapUqYJKlSph1apV6Nevn7ZTKjQsmImIiEqe3L5/8y4ZVGgsLCyQlpamkakgRERERNpStmaPU5FjsUxEREQlHQtmIiIiIiIJLJiJiIiIiCSwYCYiIiIiksCCmYiIiIhIAgtmIiIiIiIJLJiJiIiIiCSwYCYiIiIiksCCmYiIiIhIAgtmIiIiIiIJLJiJiIiIiCSwYCYiIiIiksCCmYiIiIhIAgtmIiIiIiIJLJiJiIiIiCSwYCYiIiIiksCCmYiIiIhIAgtmIiIiIiIJetpOoLhKSEjA8+fPUbNmTa30n5ycjKdPn8LZ2Vkr/ZdU4eHhsLS0hLm5eYHaefjwISpWrIgKFSpoJrF8qP7dIaVYY7sK2DO+pRayISIiKrvK3AhzVFQU7t27p/YnNDQUALB//360atVKa3leuHABrq6uhd5PYmIiHjx4UOj95EV8fDzu37+vFH/y5AkePnyoFA8LC8OrV68AAB06dMCOHTsKnEOvXr3g6+tb4HbyS1WxDAA3nr5B3+XnizgbIiKisq3MjTAvWLAAfn5+AABBEBAaGgpbW1uYmZkBAAwNDXHr1i1tplik/Pz8MGbMGLx580bbqYhu376NNm3a4P79+6hdu7YYb968OeLi4vDmzRsYGhoCAN68eQNnZ2ds3rwZgwcPhpOTk1ZHhYvCjadvtJ0CERFRmVLmRpiXLl0qjiYHBgYCAH777TcxpqpYTk9PR2RkJORyuUI8Li5OacTz7du3CqOjCQkJCAsLk2wnW2JiIp49eyaZvyAIePLkCeLj45XWvd9X9shxenq6uP7ly5d48eKFuJycnIyoqCjI5XLx+N9fn5aWhocPH+apr5iYGERFRYnxyMhIhf1iYmLw8uVLyWP08PCAiYkJAgICxNj9+/eRkJAAGxsbXL58WYyfPn0acrkc7dq1AwCsWbMGnTp1EteHhYUhMTERABAbG4ukpCSVfQqCgMePH+Pdu3eSuREREVHZU+YK5rzIyMjAl19+CVtbWzRp0gS2trY4d+6cuH7jxo3o1auXwj5nz55VmEqxf/9+NG/eXLIdAJgzZw4sLS3h7u4OKysr7N27Vymf7du3o1q1avDw8ICDgwNatmwpFq3v9zVu3DjY2dmhV69eeP78Oe7du4cGDRqgVq1aaNiwIRo2bIjAwEDcuXMHCxYswNu3b9GnTx/06dMHmzZtAgD88ccfsLS0RIsWLVClShUMHDhQodhU19fMmTMxaNAgeHp6ok6dOqhVqxaaN2+O69evo3nz5mjSpAmqVauGjz/+GJmZmSrPu4GBAVq0aAF/f38x5u/vj5YtW6JDhw5K8bp168La2hqA8pSM5s2b49tvv4WTkxOaNm2KihUrYvz48Qr9BQUFwdnZGfXq1UPVqlUxdOhQpKSkqMyNiIiIyh4WzBJevXoFfX19xMbGIjY2Fr169cK4ceM03s7x48fx888/49ixY4iKisK5c+ewa9cuhTbOnz+PsWPHYuvWrYiOjsbLly/RpEkTDBo0CIIgKPQlCAJevXqFe/fuoWrVqvjuu+/QoEEDvHz5ElFRUdi6dSvu3LmDZs2aYenSpTAzMxNHmCdPnoyAgAB8++232L59O6KjoxEeHo4bN25g5syZSsf1YV/Zuc6YMQPPnj3Do0ePEB4ejhYtWmDOnDmIiopCWFgYTpw4gZ07d6o9Z15eXkqFcbt27dC2bVulePv27SXPv5+fH06cOIGnT5/iypUrWLNmDU6dOgUga2R52LBhaNasGeLi4vDixQuYmZkhIiJCss3U1FQkJCQo/BAREVHpxIJZgp6eHn755Rfo6OhAJpNh2LBhCA4ORlpamkbbWbNmDfr27Yu2bdsCAGrVqoWJEycqtPHnn3+ic+fOsLW1xYMHDxAREYHBgwfj+vXrePTokbidTCbDggULoKurK8YSEhJgaWkpxurWrYtPPvlEbb4rVqxAr1690LVrVwBAtWrVMGPGDKxevVphOomqvgCgVatW4si7lZUVWrVqhTZt2qBz585iex4eHrhx44baHLy8vBAbG4u7d+8CAAICAsSC+dKlS3j37h1evXqFoKAgeHl5qW0HACZMmIAaNWoAABo3bgxXV1ex7wsXLiAoKAiLFi2Cnp4edHR0sGDBAujr60u2OX/+fJibm4s/dnZ2kttr2oIj94q0PyIiorKszF30lxcWFhbixWUAYGpqCrlcjuTkZBgYGGisnbCwMPTt21dhn3r16iksBwcH4/nz5+jZs6dC3NnZGa9evRILQgsLC5QvX15hm1mzZmHAgAE4deoUOnXqhJ49e0oWmWFhYUr9NGjQAO/evUNkZCTs7e3V9gUAtra2CsvlypVTus1buXLl1M4nBgB3d3eYmprC398fcrkcb9++RdOmTaGvrw9bW1tcuHABcXFxACDOX1Yne+Q7m6mpqTivOSwsDBUrVoSNjY24vkKFCqhWrZpkm9OnT8fkyZPF5YSEhCItmleeDkcj+wro4mpdZH0SERGVVSyYC0AmkynFMjIy8tyOsbGx0sVmycnJCsv6+voYPHgw/vzzT8m2PhztBbJGa6OionDmzBmcPHkSAwYMwMCBA7FixQq1+Xw4hzd72cTERLIvTdHT00Pr1q3Fgrlly5biqG/2tIy4uDg0bNgQlSpVync/qs49oHz+P2RoaKjwIUgbVgSEs2AmIiIqApySUQCVK1dGbGyswhzimzdv5rmdxo0b4/Tp0wqx9+8QAWRNczhw4ABSU1MV4u/fBUOd9PR0GBgYoGPHjpg/fz4WLVqEbdu2AQCMjIyU2mjcuLHCPGEAOHnyJKpVqwZLS8vcHlaBeXl54fTp0+L85Wxt27ZFQEAAAgICcpy/nJNGjRrh3bt3uHr1qhi7e/cuYmNjC9RuUXgQm6jtFIiIiMoEFswF0K5dO7x9+xbTp0/H9evXsWbNGvz+++95bmfKlCm4fv06vv76a1y5cgW///47/v33X4VtvvvuO6SmpqJHjx44duwYLl++jOXLl8PDwyPH9rt06YLFixfj4sWLOHfuHP799194enoCyJrSkZKSgv/++0+8rdy0adNw//59jBs3DpcvX8bq1auxcOFCzJ07N8/HVhBeXl548eIFDhw4oFQwX7p0CcHBwQUumGvXro0BAwZgxIgR8PPzw8mTJzFkyJBCHT3XlFpWZtpOgYiIqEwo0wWzjo4OnJ2dVc7DNTc3R61atRRixsbGcHZ2FospW1tbHD58GLdu3YKPjw9u3LiBtWvXok6dOnlqx9HRESdPnsTdu3cxfvx4BAcH499//1Vop2rVqggMDET9+vUxc+ZMfPXVV7h//77C7edU9QUA27Ztw/PnzzF58mRMmzYNHh4e4lPsatWqhWXLlmHZsmXo27cvNm3aBDs7O5w/fx6vXr3C2LFjsX37dqxduxYjR47MsS8bGxulOcO2trYKc4SBrAv/sm8Fp06TJk3QuHFjuLi4oGnTpmK8Ro0a8PT0hIuLC1q3bq2wz4cPLqlVq5bS79fBwUFhpHz9+vXo1q0bvvvuO/z222+YMWMGunfvjooVK0rmp00yGTC+nZO20yAiIioTZML78wmIKF8SEhJgbm6O+Ph4lR/A8qr294eRlqn6v2YVM0P83KceOnP+MhERUYHk9v27TI8wExVXofO6w0BX+aLSce2ccOX7jiyWiYiIihDvkkFUTIXO667tFIiIiAgcYSYiIiIiksSCmYiIiIhIAgtmIiIiIiIJLJiJiIiIiCSwYCYiIiIiksCCmYiIiIhIAgtmIiIiIiIJLJiJiIiIiCSwYCYiIiIiksCCmYiIiIhIAgtmIiIiIiIJLJiJiIiIiCSwYCYiIiIiksCCmYiIiIhIAgtmIiIiIiIJLJiJiIiIiCSwYCYiIiIiksCCmYiIiIhIAgtmIiIiIiIJLJhLgT179mDt2rWS2xw+fBgrV64slP7nzJmDS5cuFbidBQsW4Ny5cwVuZ+bMmbhx44bkNh/mnNMyUVmy4Mg9uMw6iurfHYLLrKNYcOSetlMiItIqPW11/OzZMyxatEjlunHjxqF27do5thEaGooVK1ZgyZIlGs6u6MTExODAgQOIiIiAubk5XF1d0b17d+jq6ua6jdOnTyMsLAxjx45Vu82FCxdw6dIlfPHFFwrxixcv4tq1a2jdujU2btyI+fPnw8jISFy/ePFiJCYm4qefflLYb9q0aejevTvatm2L9evXw9bWFs2bN891zqps2rQJ5cqVQ6tWrSS3u3HjBk6ePIkXL16gWrVqaNmyJZo0aSKuX7VqFerVq4fGjRurbePDnHNaJmV+wTFY4R+G0Ngk1LYyxTivmujiaq3ttKiAFhy5h5Wnw8XllPRMcXlatzraSouISKu0NsL84sULLF26FPr6+qhevbrCj7Gxca7aePLkCZYuXVrImRae5cuXw9HREfv27YOZmRmSkpKwfv161KtXDy9evCiSHFatWoWoqCiYmZlhyZIlCqOq7969w8yZM/HLL78gOjpajN+9excLFy6ETCYDAMyePRuenp6FnmtKSgoGDRqEdu3a4cGDB7CwsEB4eDi++OILfPLJJ3lqq6hyLq38gmPw+aZA3IqMR0p6Jm5FxsPHNxB+wTHaTo0K6P1iOTdxIqKyQGsjzNmGDRuGRo0aqVy3du1aJCcnY9KkSWJs7969uH79OsaOHStOMfjqq68AAC1btoSrqys2bNiAGTNm4N9//8XTp0/x9ddfo2rVqkhKSsK2bdsQFhaGatWqoV+/frCxsRHb/u+//5Camor69evj1KlTiIuLQ9++feHm5obAwEAcOHAA+vr6GDRoEGrWrKmQa05tf2j//v2YMGECtm7disGDByusi4iIgKGhobgcHR2Nbdu2ITo6GrVq1cLQoUNRrlw5yfMaHh6OLVu2QEdHB23btlW5jVwux5EjR7Bnzx44OTnB3t4e/v7+aNeuHYCsUWkbGxvY29sjICAAQ4YMAQD4+/vDxMREHH2NjIxE3bp1xXZnzpyJfv36ITY2FpcvX4apqSmGDx8OKysrhf5PnDiBkydPwtbWFr1795Y8HgCYMGECAgICEBQUBHt7e4V1N2/eVNr+6NGjavv/MGfKmxX+YUoxQQBWBIRzlJmIiEqdYj2H2cPDA9OmTcOOHTsAAPfu3cOwYcNQs2ZNGBkZiQVQ9si0hYUFIiIi8Mcff6B58+Zi8WpgYIDHjx+jfv362LdvH8qXL48rV66gXr16CAwMFPs7fvw4pk2bBm9vbyQlJSEiIgIeHh4YN24cRo8eDR0dHdy4cQNubm6IiooS98tN2x/65Zdf4OXlpVQsA4CjoyPKly8PAAgODkbdunVx7NgxlCtXDitXrkTjxo0RHx+vtu1bt26hYcOGCAwMREZGBnx8fODr66u03eXLlyGXy8WRVi8vL/j7+4vrs4vntm3bKsVbtmwJAwMDAFnTF+7cuSOuX7VqFfr374+//voLenp6OHToEBo3boyEhARxm8WLF6NXr1549+4dnjx5gpYtW+LZs2dqj+nZs2f4559/8P333ysVywCUPnR9//33kv1/mDPlTWhsksr4g9jEIs6EiIio8Gl9hHnRokWoXLmyQmzhwoUwMDBAgwYN8Ouvv+Kzzz5D48aNMXToUPTq1QsjRowAAHz88cdYuXKlOMIMAAcPHkRmZiZ++uknhWL0o48+QteuXRUufPvuu+/w7bff4tSpU2IsIyMDFy5cEAvWe/fuYe/evXjw4IE4quvs7IytW7diypQpAICJEyfmqu1saWlpuHr1KmbNmpXj+fnmm2/QqlUrHDhwAAAwdepUuLq64tdff8X8+fNV7pM9v3j79u0AgEmTJsHJyUlpu4MHD6Jbt27Q0cn63OTl5YWtW7ciJSUFxsbGCAgIwJgxY1CtWjVx7rMgCDh9+jS+/vprybwbN26MnTt3isdQrVo17NmzB5988glevnyJH3/8EevWrcPQoUMBAG3atMFHH32ktr1Lly5BLpejTZs2kv3mpn9NSE1NRWpqqrj8fjFeFtS2MsWtSOUPbbWszLSQDRERUeHSesFsa2uLqlWrKsSy58YCWcXe0aNH4ebmBnNzc5UFqCrvF1+pqak4evQoevTogW+++QaCIEAQBISHh+PatWsK+3l6eorFMpBVHNesWVNhCkTt2rXx9OnTPLedLTExEXK5HNbW0l9dy+Vy+Pv7Y9OmTWLM2NgYgwcPxokTJyT3+e+//8RYhQoV0LNnT6UR3IMHD2LGjBnispeXF9LS0nDhwgV4enriypUr8PX1RZUqVfD48WNERkbizZs3ePHiBdq3by+Ze/fu3cV/GxoaombNmuI5u3TpElJTUzFw4EBxm169esHc3Fxte2/evAGAHM9ZbvrXhPnz5ytdCFmWjPOqCR/fQAjC/2IyGTC+nfIHMyIiKhq8GLvwaL1glprDDGQVz71794afnx9Gjx6NChUq5NimoaEhTExMxOU3b94gPT0dVatWRbVq1cS4vb09vLy8FPZ9fz8A0NXVVZhPnB3LyMjIc9vZzM3Noa+vj8jISMnjiIuLQ2pqKqpUqaIQr1KlCmJiVF9cFRcXh7S0NKVR+ypVqigUzE+fPsXdu3fRtWtXhZwdHR3h7+8PuVwOW1tbODg4AADc3d0REBCAuLg4mJmZwc3NTTJ3Vecx+5zFxsaiQoUK0NNTfPl9mPP7LC0tAWTNPc5N0SzVvyZMnz4dkydPFpcTEhJgZ2ensfaLuy6u1lg13A0rAsLxIDYRtazMML6dEzrzDzMRkVZkX4ydLfti7FXD3Vg0a4DWC+acPHz4EN999x2GDBmCZcuWYejQoWjatCkAxZFoKRUrVoShoSHq1asHHx8fjeaXn7b19PTQunVrHD16FHPnzlV7HBYWFjAxMVEqrJ8+faq2OKtUqRKMjY2VRpM/bOPgwYNo2bKl0qhu9jxmuVwuXvwHQJzHHBcXhzZt2igVu3lRtWpVvH79Gu/evRNvYZeZmalwJ44PZc+ZPnLkiPj71yZDQ0OlD1JlTRdXa/4RJiIqJngxduEq1hf9ZWZmwtvbG+3atcOWLVswatQoDBs2DG/fvgUAcbRZ6gI4ADAwMMDHH3+M3377Da9fvxbjqampuZ7ioem2f/jhB9y8eROLFy9WWnf27FmxrV69emH16tVIT08HALx+/RpbtmxRO99XJpOhZ8+eWLt2LTIzMwFkFdj79+9X2O7gwYPo2bOn0v7t27fH1atXcejQIaWC+dSpUzh9+nSO0zFy0rJlS1SoUAGrV68WYxs3bhR/r6pYWlpi0qRJWLRokdLFlOnp6Th8+HCBciIiIirJeDF24dL6CLOqi/4GDx6M5s2bY968eQgLC8OePXsAAH/88QeaNGmCyZMnY/Xq1ahXrx7s7e3x0UcfoVGjRmjVqpXaezj/9ddf+Oijj1C3bl106tQJaWlpCAwMxPjx4wtcAOan7TZt2mD79u344osv8O+//8LT0xMpKSm4c+cOzM3NxWNeuHAh2rVrh6ZNm8LNzQ0nT55EzZo1FW6196H58+ejZcuWaNasGRo0aIBTp04p3AYvJSUF/v7++P3335X29fLyQnp6Om7fvq1QMLds2RKRkZHIyMhQO9Ukt8zMzPDHH39gzJgxCAgIgJ6eHm7evCk5JQPIurNIZmYmWrVqhTZt2sDJyQnR0dG4ffs2Bg4cqDBvmYjyx0BXB2mZcuW4XrEeXyEq83gxduHSWsFctWpV/PHHHyrXmZmZISMjAxYWFti/f79YSJmYmGD37t04fvw4kpKSYGpqips3b+Lo0aN48eIFLCwsUKNGDZWjthYWFjh37hzOnTuH4OBgWFpaYsmSJQr3Sh48eLA4kpvN29tbacrE6NGjYWb2vxdgbtpW5eOPP0b37t1x5swZ8Ul/U6dORf369cVt7O3tERwcjCNHjiAmJgZDhgxBhw4dxDtbAEDfvn0VRtmdnJxw9+5dHDhwALq6upg1axZiY2PFKQ8nTpxA1apV4ezsrJSTjY0NVq9ejczMTHH+MgCUK1cOf//9N+Lj49GwYUOFfWbPng0PDw9xed68eQpP3gOyLt58fxrJiBEj4O7ujjNnzsDGxgbr1q3D/v37FY79Q3p6evjtt9/w7bff4syZM3j16hW6du0Kd3d3hXOdm/4/zDmnZaKyYnSrGiofUjKmVQ0tZENEucWLsQuXTBDeP7VUFnz++ecwMTFR+4GF8i4hIQHm5uaIj49XuMsKUUm04Mg9bLz4CMlpmTAx0MXIFtUxtSsfi01U3PkFx/Bi7DzK7fs3C+YyaMuWLWjatClq166t7VRKDRbMREREJU9u37+1PoeZil72w0KIiIiIKGe8ioOIiIiISAILZiIiIiIiCSyYiYiIiIgksGAmIiIiIpLAgpmIiIiISAILZiIiIiIiCSyYiYiIiIgksGAmIiIiIpLAgpmIiIiISAILZiIiIiIiCSyYiYiIiIgksGAmIiIiIpLAgpmIiIiISAILZiIiIiIiCbkumF+8eIGoqCjJbcLCwhAcHFzgpIiIiIiIiotcF8wbN27E77//Li4vWbIE06dPV9hm79692LBhg+ayIyIiIiLSsnxPycjIyEB6eromcyEiIiIiKnY4h5mIiIiISIKethMgItW8Fvnj4atkhdgXbZ0wrVsdLWVERERUNuVphDkpKQmRkZGIjIxEfHy8wnJ2jKgkcnV1xcaNG9UuFzVVxTIArDwdjgVH7mkhIyIiorIrTwXz6tWrYWdnBzs7O/z8888Ky9kxoqLQokULTJs2TSm+Zs0aWFpa5rm9t2/fKszJ/3C5qKkqlrOtPB1ehJkQERFRrqdkDBw4EI0aNcpxOwcHh4LkQ5QrycnJSE1NVYqnpaUhKSkpz+2FhITAwMBAE6kRERFRKZPrgtne3h729vaIiIhAaGgoqlevjjp1OJeSir/27dvjypUrkMlksLGxQZcuXTBv3jyUL19e3Mbd3R1Tp07FJ598osVMiYiIqDjK05SMmTNnombNmujWrRtcXFwwZsyYwsqLSGMOHTqEmJgYREVFYceOHbh58yYmTJigsI22p2DklV9wjLZTICIiKjNyXTCHhIRg0aJFWLlyJYKDg/Hvv/9i69atCAgIKMT0iNRbsWIFTE1NFX6mTJmitJ2xsTFMTU1hZmaGhg0b4rfffsN///0HuVye775TU1ORkJCg8FOUVgRwHjMREVFRyXXBfPXqVfTp0weff/456tatC29vb3z66ae4cuVKYeZHpNbYsWMRExOj8DN//nyl7c6fP49u3brBzs4OZmZm8PLyQlpaGqKjo/Pd9/z582Fubi7+2NnZFeRQ8uxBbGKR9kdERFSW5bpgfvnypVJR4ODggBcvXmg8KaLc0NfXVxph/vDCvZiYGHTt2hWenp4ICAhAZGQk/P39AaBAUzCmT5+O+Ph48efp06cFOpa8qmVlVqT9ERERlWW5vuhPEATxvsvZ4uPjkZiYqBAzMzODubm5ZrMkyqfAwEAIgoDZs2eLsXv3Cn4fY0NDQxgaGha4nfwa385Ja30TERGVNXl60t/q1auxevVqlfFsU6ZMweLFiwueGZEGODo6Ijk5Gfv27cNHH32Ea9euYebMmdpOq8A6u1prOwUiIqIyg/dhplLNxcUFv//+Oz799FPEx8fDzs4OY8aMwQ8//KDt1IiIiKiEkAmCIGg7CaK8SklJga6urtKc5fT0dKSlpaFcuXJK+6Snp0NfXx+CIODt27coV64cZDIZgKwHoRgYGEBPT0/lck4SEhJgbm6O+Ph4hfs755e6R2MDgKNlOZz6pl2B+yAiIirrcvv+neuL/rZs2YKjR49qJDmigjI2Nlb5ZD59fX2VxXL2OgCQyWQwNTUVi2UAMDExUSiOP1wuav7feqGGhYlSnMUyERFR0ct1RWBsbIxevXph7NixWLRokdqihIg0w/9bL22nQERERMjDCHPfvn1x7tw5nDp1Co0aNcLFixcLMy8iIiIiomIhT985e3h44MaNG5g2bRratGmDyZMnw93dXWEbZ2dn1K9fX6NJEhERERFpS54naRobG2Px4sUIDw/HwoULldbztnJEREREVJrkuWC+ffs2vL29ERcXh2PHjimNMBsZGWksOSIiIiIibcv1HGa5XI4FCxbA3d0dDRo0QFBQEDp16oQKFSoo/LBgJiIiIqLSJNcjzMuXL8fixYuxZcsW9OvXrzBzIiIiIiIqNnJdMDdu3BhBQUGwtuYjeYmIiIio7Mj1lIzr16/jr7/+KsxciIiIiIiKnVwXzGlpaUhNTS3MXIiIiIiIip1cF8xERERERGVRnm4rFxoaip07d0puwweXEBEREVFpkqeC+cCBAzhw4IDkNnxwCRERERGVJnkqmCdMmIC5c+dKbsP7MBMRERFRaZKngtnQ0BAVKlQopFSIiIiIiIofXvRHRERERCQh1yPMtWrVgqWlZa4bvnDhApKSktC5c+d8JUZEREREVBzkumDu3bt3nhq+cOECYmJiWDATERERUYnGKRlERERERBJYMBMRERERScjTXTKISoO9e/eifv36cHJy0nYqkrwW+ePhq2RxuYaFCfy/9dJiRqSKX3AMVviHITQ2CbWtTDHOqya6uFprOy2NKgvHSEQkhSPMZcDt27exd+9epXhycjJ8fX0RHR1d9Enl0e3bt+Hr6wtfX19s3boVp0+fRmJiYr7a+uqrr+Dv76/hDDXrw2IZAB6+SobXouKdd1njFxyDzzcF4lZkPFLSM3ErMh4+voHwC47RdmoaUxaOkYgoJyyYy4Ddu3fjq6++Uoq/fv0a3t7euHXrVtEnlUe7d++Gj48Pjh49igMHDmDixImoXr06jh07lue2+vbti5o1axZClprzYbGcU7yk8AuOQe9l5+Ay6yh6LzuX76JLU+0U1Ar/MKWYIAArAsK1kE3hKAvHSESUk0KbkmFrawtDQ8PCap4K2c2bNxEWFoZq1aqhadOm0NP730slODgYN27cAACYm5ujfv36qF69urg+PDwcgYGBGDhwoEKbDx48wM2bN9GkSROV60NDQ3Hr1i0MGDBAZU6Wlpbw9fUFAAiCgAEDBsDHxwcRERHiNn5+fnjx4gVkMhlsbGzg5uYGc3NzhXbatm0LOzs7cXnnzp1wd3eHvr4+bty4AVNTU7Rs2VLhmKngskcqs2WPVK4a7panr/dz205RTCMIjU1SGX8Qm79vP4qjsnCMREQ5yXVF8OeffyI2Nhbz5s3L1fZDhw7Nd1KkPUlJSejfvz/u3r0LNzc3hIaGQk9PDwcPHkS1atUAAA8fPsTRo0cBAHFxcTh9+jSmTp2K2bNnAwAyMzMxaNAguLi4oH79+mLbP/zwA5KTk9GsWTMMGTIEjo6OaNq0qbh++vTp0NHRUVswv08mk6Fz587YtWsXkpKSYGpqCgC4ePEiwsLCIAgCIiIiEBYWhp07d6Jt27bivl999RVmzpwpzmH28fFB48aN8ejRI9SrVw9Xr16Fg4MDTp8+XSKK5g8LwxZOlrgQ/hKhsUmwKp/1oTU2IVWyaCyK4lJqpDIvfeWmHU0V5zmpbWWKW5HxSvFaVmYa60PbrMob4pGKbzaqmHFAhIjKjlxXA2lpaUhNTS3MXKgQvX37VhydzRYXF6e03bfffguZTIawsDDo6+tDEAQMHToUU6ZMwX///QcA6NmzJ3r27Cnuc+fOHbi5uWHQoEFwdnZG7dq14e7ujs2bN+PXX38FkFWI79u3Dxs3boSDgwM6dOiA9evXiwXzy5cvcfDgQZVzrdV58OABzMzMYGJiIsZ+/PFHhW0WLFiA8ePH486dO5JtJSUlISgoCEZGRnj58iWqV6+O/fv34+OPP1a5fWpqqsL/h4SEhFznrUmqCsP3C7j3Cx2pkdiiKC7zO1L5YTF/N1r19u+3o6niPCfjvGrCxzcQgvC/mEwGjG9XvC8o1QiZTNsZEBEVmeI/fEYakZKSIo4KZ0tOVhw1yszMhK+vL0aPHo1du3ZBEAQIgoAqVapg69atCtvGx8cjMDAQsbGxyMzMRIUKFRAYGAhnZ2cAwLBhw/Dbb79h/vz5kMlk2LNnD/T19cVCe+zYsfjss8/w+++/w8jICL6+vqhcubLkg26yi365XI6goCAsX74cCxYsgI6O4lT8hw8fIiQkBG/evIEgCAgODsbbt29Rrlw5tW2PGDECRkZGALKmfri4uCA0NFTt9vPnz8dPP/2kdn1RUVUYSlFVNBZVcZmf0VhVxbw677dTVNMIurhaY9VwN6wICMeD2ETUsjLD+HZO6FyK7iARm6B6oOR5wrsizoSISHvyVDCHhoZi586dkts4OzsrfA1PxcP783+zRUZGYs+ePeLyy5cvkZSUhLt37+Lly5cK23bp0kX8965du/Dpp5/C2dkZDg4OMDQ0RGpqKl68eCFuM2TIEEyZMgVnzpxB27ZtsXnzZvTv318sSnv37o3x48djz549GDJkCDZs2ICRI0dCV1dX7TFkF/3p6em4cuUK6tWrh+HDhyts88UXX8DX1xfNmzeHpaUlUlJSxGOTKpgrVqyosGxoaIh379QXBNOnT8fkyZPF5YSEBIV50UVFXWEo5cOisaiKy/yMxub2A8GH7RTlVIkurtal+hZrZWHaCRFRTvJUMB84cAAHDhyQ3GbKlClYvHhxgZIi7TAzM4OOjg5GjBiBYcOGqd3uq6++wpw5czBp0iQxZmVlBeG9SqhKlSro2LEjNm/eDBcXF5w4cQInTpwQ1xsYGMDb2xvr169HrVq1EBQUhN27d0vm937Rn5KSgjZt2sDb2xsHDx4EAAQGBmLNmjUICwtDjRo1AGTNad63b59CbppgaGhYLC5qVVfMSPmw0Cmqgig/o7HqinkDPR242JRX206ZniqhYTyXRER5LJgnTJiAuXPnSm6TPYJIJY+JiQnatGmDVatWYciQIQpTHZ48eQJ7e3sIgoAXL14o3JbtzJkzeP78uVJ7w4cPx5dffolatWrB1tZW4cI7IGtahqurK3788Ue0adMmTw8SMTY2xqpVq+Du7o7Dhw+je/fueP78OQwNDcWLEwFgx44deTkFJY6qYkaKqkKnKAuivI7GqivmXWzKY9/4lpL9lPapEkWF55KIKI8Fs6GhISpUqFBIqVBxsGLFCnh5eaF169YYOHAg0tLScOrUKTg6OmL58uWQyWTo06cPvvrqKzx69AivXr3CsmXLxLtUvK9v377w8fHBTz/9hAkTJkD2wUVCderUgaenJw4dOoSNGzfmOVc3NzcMHjwY3333Hbp27QpPT0+UL18e/fr1Q8+ePXH58mXs27cv3+dCmwx0dZCWKVeO6ynO11ZVzLRwssCF8Fd4EJso3sngeWKq2kKnOBdEBSnmS/tUiaLEc0lEZR0v+isDGjRogL59+yrFy5Urh2HDhsHW1laMubi4ICQkBBs3bkRQUBAsLS0xefJkdOrUSdxm48aNWL16NW7cuIFKlSrh2LFj+O+//+Di4qLU/o8//oibN29i1KhRKnPr3bs3goKC0L9//3wdw7x58zBr1iwEBwejfv36uHLlClatWoVLly7B2dkZZ86cwS+//KJQ0H/44JIBAwYo3EcayJqz7erqKplTYRrdqgZWnlZ+MMSYVjWUYpooZoprQVSci3kiIio7ZEIuJ3fu27cPcXFxGDlyZCGnRGWJl5cXXFxcsGLFCm2nUiAJCQkwNzdHfHw8ypcvr5E2Fxy5h40XHyE5LRMmBroY2aI6pnato5G2iYiIKPfv37kumK9du4aAgIAct3N3d1eaq0r0oWPHjuHUqVP4888/ERQUlKf5y8VRYRTMREREVLhy+/6d6ykZN27cwLJly9SuT0tLQ3R0NKZMmcKCmXJ0+fJlxMXF4ejRoyW+WCYiIqLSLdcjzOoIgoDNmzdj5syZSE5Oxrp169CrVy9N5UdUInCEmYiIqOTJ7fu3jto1uXDs2DE0adIEPj4+8Pb2Rnh4OItlIiIiIipV8lUwBwYGomPHjujRowc8PDwQFhaGuXPnwsyMT34iIiIiotIlTwVzREQEhg4dimbNmsHc3BzBwcFYtWoVrK15iyciIiIiKp1yfdHf7t27MWTIEDg7O2P//v3w8PAAALx8+VJhOxMTE5iYmGg2SyIiIiIiLcl1wRwREYG0tDQEBQWhZ8+earebMmUKFi9erJHkiIiIiIi0LdcF88CBA9GoUaMct3NwcChIPkRERERExUquC2Z7e3vY29sXZi5ERERERMVOri/6e/HiBaKioiS3CQsLQ3BwcIGTIiIiIiIqLnJdMG/cuBG///67uLxkyRJMnz5dYZu9e/diw4YNmsuOiIiIiEjL8v3gkoyMDKSnp2syFyIiIiKiYqdAT/ojIiIiIirtWDATEREREUnI9V0yACApKQmRkZEAgPj4eIXl7BgRERERUWmSp4J59erVWL16tVLsfVOmTCl4VkRERERExQQfXEJEREREJIEPLiEiIiIikpDri/527NiBxYsX4/nz54WZDxERERFRsZLrgllfXx8///wzqlWrhn79+uHw4cOQy+WFmRtRmeYXHIN2i/zhOP0Qakw/hHaL/OEXHKPttIiIiMqcXBfMffr0QXR0NNatW4dXr16hZ8+ecHBwwOzZs/Ho0aNCTJFIs0aNGoU9e/ZoOw1JfsEx+HxTIB69SoZcAAQBePQqGZ9vCmTRTEREVMRkgiAI+dkxPDwc69evxz///IPo6Gh06NABo0ePRt++fWFoaKjpPKkY+vXXX3H06FHJbU6ePAldXd0iyih36tWrBx8fH0yYMEFjbSYkJMDc3Bzx8fEoX758gdtzn3ccLxLTVK6rbmGCgG+9CtwHERFRWZfb9+883VbufU5OTpg3bx7mzJmDo0ePYsWKFRgyZAi+/fZbLFy4ML/NUgnSp08fNG/eXFz28vLCN998gx49eogxHR0+Gyc/1BXLQNZIMxERERWdfBfM2W7fvo2jR4/i0qVLMDQ0hKOjoybyohKgTp06qFOnjkLM2dkZ7dq1E5dPnjyJDRs24MWLF6hTpw6mTJmicLeVH374Aebm5qhUqRL27t2LypUrY+3atejduzc+//xz3L59G5cvX4apqSkmTpyIZs2aifuOGzcOISEhkMlksLGxQZcuXTBixAjIZDJxm4yMDCxZsgQnT56Era0thg8frnQccrkc69atw+HDh5GamorWrVvjyy+/RLly5TR4tjTLLzgGXVyttZ0GERFRmZCvgjkuLg6bN2/G+vXrcePGDdSrVw+zZs2Ct7c3LCwsNJ0jlVB79uzBoEGD8P3332PAgAHYsGEDmjZtipCQEFhaWgIAgoODceTIEXTq1AmjRo1C1apVAQDnz5/H6dOnMW7cOIwZMwZHjhxB27ZtERoaCjs7OwDAmDFjkJCQAEEQEBERgR9++AFhYWGYO3eumMPEiRNx4MABzJs3D3p6ehg7diyePXumkOeUKVOwZcsWzJs3D6amppg7dy6OHz+OU6dOFdGZyrv5h++yYCYiIioiuS6Y5XI5Tp48ifXr12PPnj0wMDDAoEGDsHLlSnh4eBRmjlRCTZ06FZMnT8YPP/wAAOjVqxdcXFywYMECLFq0SNzO2toau3btUprrPGzYMPzyyy8AgO7du2P//v04cuQIPvvsMwBAkyZNxG29vLxgZ2eH/v37iwXz48ePsXbtWpw4cUIc9a5Tpw6aNm0q7vf48WMsW7YMBw4cQNeuXQEAzZs3R61atXDo0CGF6SXvS01NRWpqqrickJCQr3OUX09ec1oGERFRUcl1wbx06VJMnjwZnp6eWLFiBQYNGlSsv7Im7YqLi0NYWBi6d+8uxnR0dNC9e3dcuXJFYVtPT0+VFwa+Pz9aJpPBzs4OMTH/u0NEVFQUVq5ciTt37uDNmzdITk5GYmIiYmNjYWVlhcDAQOjp6SlMEXFzc0PlypXF5cDAQABA586dxVj16tVRr149XLlyRW3BPH/+fPz000+5PBtERERUkuW6YG7Tpg1CQkLg4uJSmPlQKfHmzRsAgJmZmUK8fPnyiI+PV4iZmpqqbENfX19hWSaTiff+TkhIgKenJ5o0aYLBgwfD0tISz549w5UrV5CSkgIAiI+PV9n2+znFx8fDxMRE6eJEVXm+b/r06Zg8ebK4nJCQIE4VKQr2lUyKrC8iIqKyLk+Pxk5PT5fcJiwsDKmpqXB1dS1wYlSy2dnZQV9fH6GhoWjcuLEYv3fvnkYuDL106RJevHiBnTt3iqPTBw4cUNimRo0aePXqFV6/fo1KlSoBAN6+faswh9nR0REJCQmIiYmBtXXWnGC5XI4HDx6gX79+avs3NDTU6u0TZ3TnB1ciIqKikut7fm3cuBG///67uLxkyRJMnz5dYZu9e/diw4YNmsuOSiw9PT0MHz4cCxcuFEdqr1y5gj179mDUqFEFbt/MzAypqakIDw8HkDUFZM6cOQrbtGrVCo6OjuIcagCYN2+ewtzjli1bonbt2pg1axayb0n+559/IiEhAQMGDChwnvn13o0+VOrMC/6IiIiKTL5vkpuRkZHjiDOVbQsXLkS5cuVQvXp1NG7cGG3btsXXX3+NXr16FbhtT09PDBs2DE2aNEGzZs3g5OSE6tWrK2yjp6eHDRs2YOvWrXB0dEStWrVw6dIlhdva6enpwdfXF8eOHYODgwPq1q2LH3/8ERs2bICNjU2B88yvLnXVF8Q6ORTTREREpFkFvg8zUTZ/f384OzuLy5aWljhz5gwePHiAFy9eoHbt2uLt5LL99NNPSnOVAWDfvn2oVauWQuyvv/5CxYoVxeV///0XP/74I2JiYlCzZk2YmZlh/Pjx4tQKIGvu/ZMnTxAUFAQbGxvY29vj6tWrsLW1Fbdxd3dHREQEgoKCkJaWhvr168PY2LjA56MgVnm7odm843iu4gEmvJ0cERFR0WLBTBrz/t0o3lerVi2l4jebuvnuLVu2VIq9Pxc6m6Ojo8KcaFU5mJiYKNz60N3dXWkbXV1dNGrUSGUu2nLl+07w2RSIYyExkAtZI8tdXK2xcribtlMjIiIqU/JUMCclJSEyMhJA1t0F3l/OjhGR5qzyZnFMRESkbXkqmFevXo3Vq1crxd43ZcqUgmdFRERERFRM5LpgHjhwYK6+snZwcChIPkRERERExUqe7sP8/t0FiIiIiIjKgnzfVo6IiIiIqCxgwUxEREREJIEFMxERERGRBBbMREREREQSWDATEREREUlgwUxEREREJIEFMxERERGRBBbMREREREQSWDATEREREUlgwUxEREREJIEFMxERERGRBBbMREREREQSWDATEREREUlgwUxEREREJIEFMxERERGRBBbMREREREQS9LSdABGRFL/gGKzwD0NobBJqW5linFdNdHG11nZaRERUhnCEmYq1/fv348qVK0rxe/fuYdOmTYXS544dOxAWFlYobVPe+AXH4PNNgbgVGY+U9EzciozH55sC4RccU2j99V52Di6zjqL3snOF1g8REZUsLJipWJs9eza2bNmiFD9x4gTGjh1bKH1+/fXXOHfuXKG0TXnz7Y5beYoXRFEX50REVHJwSgaVKikpKTh79izi4+Ph6uqKunXrKqw/dOgQXrx4AZlMBhsbG7i7u6NixYri+v379yM5OVksmHV1deHt7V2kx0D/k/AuI0/xgph/+K7aOKeAEBGVbSyYqdS4du0aevfuDQcHB1StWhVnz55F165dsWHDBshkMgDA9evXER4eDkEQEBERgZCQEOzcuRNeXl5iG6mpqbh37x4yMjKgr6/PgrmMePw6WWX8iZo4ERGVHSyYqdgL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)

??? success "Solution"
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

    ![A strip plot showing the duration of Flood and Flash flood events in hours on the x-axis, ranging from 0 to 700. The y-axis shows the event type. Flash Floods all last under 24 hours while Floods can last up to 700 hours.](data:image/png;base64,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crKkqtv/M2fO6M4779Qf//hHp2uALlZUVKTi4mK3fSsuLlZRUZGMMZetudxod2WZMGGCU7v79u2r5s2ba9GiRXr88ccdPzt3fbv4Z3+5mkBUWFio4uJiTZ8+XQ899JCmTZumHTt26J577tHvf/97TZgwoUr3/1KvvfaakpKS1L59e8e2QO8/IQ6W1KpVSz///LPTtszMTElS7dq1K6NJFcpT/2vVqmW5JpBt3rxZAwcO1GOPPaYpU6Y47Sutb8HBwYqNjbVcE6iqVaumLl26SPrlTTw9PV1PP/201q9fL6n0vlWvXl1RUVGWawLNV199pf379+vll1/Wyy+/LOmXCQoXLlxQly5d9O6776pZs2aKiopy27eYmBhHOLNSE4gufeO9+uqrlZiYqB07dkj6pV/Vq1d327eS1z4rNYEoLCxMNWvWVOfOnfXCCy9Ikm655RZlZGTopZde0oQJExQbG6vg4GCPfbNSE+hOnDih//u//9PixYudtpe8dnvqm5Uaf+F0Kizp2LGjtm7d6rRt8+bNqlOnjho0aFBJrao4pfW/SZMmuuqqqyzXBKotW7aof//+euSRR1xm5kml961t27aON0ErNXZRr149nTp1yvG4tL516NDBcQ2clZpAc8MNN+jzzz93mp13/fXXq02bNpo3b57q1asnqfS+XX/99Y7HVmrs4vjx46pZs6akX65tu+666zz2zUpNoOrUqZPLacB69eo5LoEIDw9XmzZtPPbNSk2ge/PNN1WjRg3deeedTttr1aqlxo0be+yblRq/8eu0CVQZ27ZtM0FBQea9994zxhjz448/mgYNGridyWlnpc1O3bBhgwkKCjIrV640xhhz+PBhU6dOHTNz5kyvagLR1q1bTUxMjMef5cqVK01ISIhZu3atMcaYPXv2mJiYGPOnP/3Jq5pANHfuXJOVleV4vHPnTlO3bl0zadIkx7YPP/zQhIaGmi+++MJRExkZaRYtWuRVjR24m5369ttvmxo1apht27YZY4z5+uuvTXh4uHnnnXe8qglEs2fPdszQLi4uNi+++KKRZD777DNHzcKFC010dLRJS0szxhizceNGU61aNfP3v//dq5pAtHTpUlO7dm1z6NAhY4wxp0+fNtdff7254447HDVz5841V111ldm7d68xxpg1a9aY4OBg8/HHH3tVE8hatmxpHnroIbf7ZsyY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jz/+WBMnTiz162fOnKnt27fr/fffL9Pz+7JtN954o1avXu00GnfhwgWtWbNGN954Y6nP07ZtW02dOlVPPvmksrKyJEk5OTn6+eefXWrPnz+v2NjYcvYM8A9OpwLwqZLrvC5WsuhsiWHDhmn8+PFauHChpk2b5rKIqzfHutj48eM1f/58ffPNN+ratWs5e+K+LefOndOePXv0l7/8RfXq1dNf//pXR03NmjU1d+5c/eY3v1FGRoY6dOigo0eP6qWXXtLDDz/sMcSFhIRo1qxZGjJkiB5//HG99957atmypVq3bu1SO3ToUD3zzDOaPXu2y4LDVixevFiDBg1Sx44d9etf/1r169fX9u3btWTJEk2ZMkV33XVXqV/bqFEjjR8/Xn/84x8VExPj9XP7sm3PPfeckpKS1LdvXw0bNkxFRUVatmyZjDF66qmnPD7Pb3/7W7388sv6/e9/rxdffFGZmZnq2bOn+vTpo8TEREVERGjDhg169913GYlDwCLEAfCJqKgojRgxQrt373Y51RcTE+MUvMLDwzVz5kx9/vnnbk+lWjlWSU2tWrUc+8LCwjR//nwtXbpUnTp1cjnusGHD3IYiq/3as2ePIiIiFB8fr3feeUe9evVyufaq5FqrDz/8UBs3blTdunW1dOlSp9HGkmPWqVPH6WtTUlI0YcIEbdq0SefPny/1tOXQoUO1fv167du3T+3atZMkderUyXFN2aX69u2rJk2aOB7HxsZq48aNWr58udauXatdu3apYcOG2rhxo8tyGn379lWLFi2ctk2dOlUZGRmqUaOG529eKc9fIiEhwWUiijdti4+P1969e/XGG2/ou+++U3BwsO6++27dd999Ttf0uXv+iIgILViwQCtWrFBBQYGaNm2q3bt367333tO2bdt09uxZJSQkaNeuXS53hAACRZCp6Dn5AAAAKDdG4gBc0b788kt9//33bvc1bdpUSUlJFdwieym5X6w7wcHBGj58eAW3CLhyEOIAXNG2bt2qTZs2ud2XnJxMiLuMEydOuKz/ViIkJIQQB/gRp1MBAABsiCVGAAAAbIgQBwAAYEOEOAAAABsixAEAANgQIQ4AAMCGCHEAAAA2RIgDAACwIUIcAACADRHiAAAAbOj/AfMa7ffhwFidAAAAAElFTkSuQmCC)

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

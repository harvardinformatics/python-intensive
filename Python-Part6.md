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

<pre class="output-block">--2025-09-11 19:57:04--  https://raw.githubusercontent.com/harvardinformatics/python-intensive/refs/heads/main/data/indiana_storms_full.csv
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 185.199.108.133, 185.199.109.133, 185.199.110.133, ...
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|185.199.108.133|:443... connected.
</pre>

<pre class="output-block">HTTP request sent, awaiting response...
</pre>

<pre class="output-block">200 OK
Length: 952491 (930K) [text/plain]
Saving to: ‘indiana_storms_full.csv’


indiana_storms_full   0%[                    ]       0  --.-KB/s
</pre>

<pre class="output-block">
indiana_storms_full 100%[===================>] 930.17K  --.-KB/s    in 0.05s

2025-09-11 19:57:05 (18.3 MB/s) - ‘indiana_storms_full.csv’ saved [952491/952491]
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

<pre class="output-block"><class 'pandas.core.frame.DataFrame'>
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
&nbsp;8   STATE               1315 non-null   object
&nbsp;9   STATE_FIPS          1315 non-null   int64
&nbsp;10  YEAR                1315 non-null   int64
&nbsp;11  MONTH_NAME          1315 non-null   object
&nbsp;12  EVENT_TYPE          1315 non-null   object
&nbsp;13  CZ_TYPE             1315 non-null   object
&nbsp;14  CZ_FIPS             1315 non-null   int64
&nbsp;15  CZ_NAME             1315 non-null   object
&nbsp;16  WFO                 1315 non-null   object
&nbsp;17  BEGIN_DATE_TIME     1315 non-null   object
&nbsp;18  CZ_TIMEZONE         1315 non-null   object
&nbsp;19  END_DATE_TIME       1315 non-null   object
&nbsp;20  INJURIES_DIRECT     1315 non-null   int64
&nbsp;21  INJURIES_INDIRECT   1315 non-null   int64
&nbsp;22  DEATHS_DIRECT       1315 non-null   int64
&nbsp;23  DEATHS_INDIRECT     1315 non-null   int64
&nbsp;24  DAMAGE_PROPERTY     1011 non-null   object
&nbsp;25  DAMAGE_CROPS        1009 non-null   object
&nbsp;26  SOURCE              1315 non-null   object
&nbsp;27  MAGNITUDE           577 non-null    float64
&nbsp;28  MAGNITUDE_TYPE      390 non-null    object
&nbsp;29  FLOOD_CAUSE         246 non-null    object
&nbsp;30  CATEGORY            0 non-null      float64
&nbsp;31  TOR_F_SCALE         24 non-null     object
&nbsp;32  TOR_LENGTH          24 non-null     float64
&nbsp;33  TOR_WIDTH           24 non-null     float64
&nbsp;34  TOR_OTHER_WFO       3 non-null      object
&nbsp;35  TOR_OTHER_CZ_STATE  3 non-null      object
&nbsp;36  TOR_OTHER_CZ_FIPS   3 non-null      float64
&nbsp;37  TOR_OTHER_CZ_NAME   3 non-null      object
&nbsp;38  BEGIN_RANGE         871 non-null    float64
&nbsp;39  BEGIN_AZIMUTH       871 non-null    object
&nbsp;40  BEGIN_LOCATION      871 non-null    object
&nbsp;41  END_RANGE           871 non-null    float64
&nbsp;42  END_AZIMUTH         871 non-null    object
&nbsp;43  END_LOCATION        871 non-null    object
&nbsp;44  BEGIN_LAT           871 non-null    float64
&nbsp;45  BEGIN_LON           871 non-null    float64
&nbsp;46  END_LAT             871 non-null    float64
&nbsp;47  END_LON             871 non-null    float64
&nbsp;48  EPISODE_NARRATIVE   1315 non-null   object
&nbsp;49  EVENT_NARRATIVE     1079 non-null   object
&nbsp;50  DATA_SOURCE         1315 non-null   object
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

<pre class="output-block"><class 'pandas.core.frame.DataFrame'>
RangeIndex: 1315 entries, 0 to 1314
Data columns (total 11 columns):
&nbsp;#   Column           Non-Null Count  Dtype
---  ------           --------------  -----
&nbsp;0   EVENT_TYPE       1315 non-null   object
&nbsp;1   CZ_NAME          1315 non-null   object
&nbsp;2   BEGIN_DATE_TIME  1315 non-null   object
&nbsp;3   END_DATE_TIME    1315 non-null   object
&nbsp;4   CZ_TIMEZONE      1315 non-null   object
&nbsp;5   BEGIN_LOCATION   871 non-null    object
&nbsp;6   END_LOCATION     871 non-null    object
&nbsp;7   BEGIN_LAT        871 non-null    float64
&nbsp;8   BEGIN_LON        871 non-null    float64
&nbsp;9   END_LAT          871 non-null    float64
&nbsp;10  END_LON          871 non-null    float64
dtypes: float64(4), object(7)
memory usage: 113.1+ KB
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
Name: BEGIN_DATE_TIME, dtype: datetime64[ns, UTC-05:00]
</pre>


```python
storms_df.info()
```

<pre class="output-block"><class 'pandas.core.frame.DataFrame'>
RangeIndex: 1315 entries, 0 to 1314
Data columns (total 11 columns):
&nbsp;#   Column           Non-Null Count  Dtype
---  ------           --------------  -----
&nbsp;0   EVENT_TYPE       1315 non-null   object
&nbsp;1   CZ_NAME          1315 non-null   object
&nbsp;2   BEGIN_DATE_TIME  1315 non-null   datetime64[ns, UTC-05:00]
&nbsp;3   END_DATE_TIME    1315 non-null   datetime64[ns, UTC-05:00]
&nbsp;4   CZ_TIMEZONE      1315 non-null   object
&nbsp;5   BEGIN_LOCATION   871 non-null    object
&nbsp;6   END_LOCATION     871 non-null    object
&nbsp;7   BEGIN_LAT        871 non-null    float64
&nbsp;8   BEGIN_LON        871 non-null    float64
&nbsp;9   END_LAT          871 non-null    float64
&nbsp;10  END_LON          871 non-null    float64
dtypes: datetime64[ns, UTC-05:00](2), float64(4), object(5)
memory usage: 113.1+ KB
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
Name: END_DATE_TIME, Length: 1315, dtype: object
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
High Wind                    2
Lake-Effect Snow             2
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
    Blizzard                    1
    Flash Flood                 1
    Extreme Cold/Wind Chill     1
    Lake-Effect Snow            1
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

    ![A barplot showing the number of Floods and Flash Floods in different counties in Indiana. The x-axis separates 'Flood' and 'Flash Flood' events, while the y-axis shows the number of events. Bars in each category are colored by county name. For Flash flood: Spencer 1, Marion 6, Vermillion 1, Monroe 0, Tippecanoe 0. For Flood: Spencer 1, Marion 4, Vermillion 1, Monroe 1, Tippecanoe 1. ](data:image/png;base64,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sqUqV66sBx54QE8//bQOHTpkz5IAAICB2DWofP3114qOjtbWrVv11VdfKS8vT08++aQuX75sz7IAAIBBONlz8bVr11q9TkpK0gMPPKDU1FQ9+uijNuNzcnKUk5NjeZ2dnX3XawQAAPZjqHtUsrKyJElVqlQptH/69Ony9va2bEFBQeVZHgAAKGeGCSr5+fkaMWKE2rVrp0aNGhU6JiYmRllZWZbtxIkT5VwlAAAoT3a99HOz6Oho7du3T5s3by5yjKurq1xdXcuxKgAAYE+GCCqvvPKKPvvsM23atEk1a9a0dzkAAMAg7BpUzGazhg4dqk8++UQbN25U7dq17VkOAAAwGLsGlejoaC1dulT/+c9/VLlyZZ06dUqS5O3tLXd3d3uWBgAADMCuN9PGxcUpKytL7du3V2BgoGVLTk62Z1kAAMAg7H7pBwAAoCiGeXsyAADAHxFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYdk1qGzatEndu3dX9erVZTKZtHr1anuWAwAADMauQeXy5ctq2rSp5s+fb88yAACAQTnZc/EuXbqoS5cu9iwBAAAYmF2DSknl5OQoJyfH8jo7O/uurpeRkaHMzMy7ukZppaen27uEYjFynf7+/goODrZ3GbAzfs7vnJHrzMnJkaurq73LuCWj12jv35X3VFCZPn26pk6dWi5rZWRkKDQ0TFevXimX9UrHpJNZ1yR527sQGzm5vwfKyMhIO1dSNPdK7jqYfpCwUoHxc35n7oWfc5kkme1dxK05SMq3dxG3UMm9ktIPptvtd+U9FVRiYmI0cuRIy+vs7GwFBQXdlbUyMzN19eoVtY6aLK/AWndljTvx27GD2r10pi5cuW7vUgp1/frvdTV/vrlqtqxp52psZZ3I0qa3NikzM5OgUoHxc35njP5zfvrIaW1/d7tGNW2mDjVq2LucQu09c1oxO3fquc4vq0VYO3uXY+Pn08c0d+lEu/6uvKeCiqura7mfHvMKrKUqwfXLdc3iuHrZyP8F+H88AzzlX9ff3mUAt8TP+Z0x6s/5lSu/f/2CPD3VyM/PztUU7vL/fzbvgSrV9VDNMDtXY0w8RwUAABiWXc+oXLp0SUePHrW8PnbsmHbv3q0qVapwOh4AANg3qOzcuVMdOnSwvC64/6R///5KSkqyU1UAAMAo7BpU2rdvL7PZ4LdjAwAAu+EeFQAAYFgEFQAAYFgEFQAAYFgEFQAAYFgEFQAAYFgEFQAAYFgEFQAAYFgEFQAAYFgEFQAAYFgEFQAAYFgEFQAAYFgEFQAAYFgEFQAAYFgEFQAAYFgEFQAAYFgEFQAAYFgEFQAAYFgEFQAAYFgEFQAAYFgEFQAAYFgEFQAAYFgEFQAAYFgEFQAAYFgEFQAAYFgEFQAAYFgEFQAAYFgEFQAAYFgEFQAAYFgEFQAAYFgEFQAAYFgEFQAAYFgEFQAAYFgEFQAAYFgEFQAAYFgEFQAAYFgEFQAAYFgEFQAAYFgEFQAAYFgEFQAAYFgEFQAAYFgEFQAAYFgEFQAAYFgEFQAAYFgEFQAAYFgEFQAAYFgEFQAAYFgEFQAAYFgEFQAAYFiGCCrz589XrVq15ObmptatW2v79u32LgkAABiA3YNKcnKyRo4cqcmTJystLU1NmzZVRESEzpw5Y+/SAACAndk9qLzzzjsaNGiQXnjhBTVo0EALFixQpUqVlJCQYO/SAACAnTnZc/Hc3FylpqYqJibG0ubg4KCOHTvqu+++sxmfk5OjnJwcy+usrCxJUnZ2dpnXdunSJUnSuZ8O6XrO1TKf/05l/XJEkpR+8qI2HTpr52ps7cm4KEnKysjSye9P2rkaW9m//P49k5qaavn/2mgcHByUn59v7zKKFBAQoICAAHuXcUf4Ob8zRv85v/DjBUnS0awsbT91yr7FFOHAhQuSpF/OHNf+H1LtW0whfvntJ0m//6yU5d/agrnMZvPtB5vt6JdffjFLMn/77bdW7WPGjDG3atXKZvzkyZPNktjY2NjY2Njug+3EiRO3zQp2PaNSUjExMRo5cqTldX5+vs6dOyc/Pz+ZTCY7Voa7LTs7W0FBQTpx4oS8vLzsXQ6Au4Cf84rDbDbr4sWLql69+m3H2jWo+Pv7y9HRUadPn7ZqP336dKGnlF1dXeXq6mrV5uPjczdLhMF4eXnxCwy4z/FzXjF4e3sXa5xdb6Z1cXFReHi41q9fb2nLz8/X+vXr1aZNGztWBgAAjMDul35Gjhyp/v376+GHH1arVq00d+5cXb58WS+88IK9SwMAAHZm96DSp08f/fbbb5o0aZJOnTqlZs2aae3atapWrZq9S4OBuLq6avLkyTaX/gDcP/g5R2FMZnNx3hsEAABQ/uz+wDcAAICiEFQAAIBhEVQAAIBhEVRQYu3bt9eIESPKZK7jx4/LZDJp9+7dZTJfAZPJpNWrV5fpnH90t2oH7kdl+XvjVmrVqqW5c+fe9XVQfggqsDFgwACZTCab7ejRo/YuzaJWrVo29dWsWdPeZQEV2r3wuwP3Hru/PRnG1LlzZyUmJlq1Va1a1U7VFC42NlaDBg2yvHZ0dLRjNQCke+N3B+4tnFFBoVxdXS2fjluwFRUE/v3vf+vhhx9W5cqVFRAQoOeee05nzpyx9J8/f179+vVT1apV5e7urrp169r8Ivvxxx/VoUMHVapUSU2bNi3007P/qGC9gu1Wvwz37t2rxx9/XO7u7vLz89Pf/vY3q09Nzs/PV2xsrGrWrClXV1fL83xutn37djVv3lxubm56+OGHtWvXrtvWCFQ0xf3dcf78eT3//PPy9fVVpUqV1KVLFx05csRqzEcffaSGDRvK1dVVtWrV0uzZs636z5w5o+7du8vd3V21a9fWkiVL7uqxwT4IKrhjeXl5mjZtmvbs2aPVq1fr+PHjGjBggKV/4sSJOnDggL788kulp6crLi5O/v7+VnOMHz9eo0eP1u7du1WvXj317dtX169fL5P6Ll++rIiICPn6+mrHjh1auXKlUlJS9Morr1jGzJs3T7Nnz9asWbP0/fffKyIiQn/+858tvzgvXbqkbt26qUGDBkpNTdWUKVM0evToMqkPqIgGDBignTt3as2aNfruu+9kNpv11FNPKS8vT5KUmpqq3r1769lnn9XevXs1ZcoUTZw4UUlJSVZznDhxQhs2bNCqVav0/vvvW/1HEu4Tt/18ZVQ4/fv3Nzs6Opo9PDws2zPPPGPpf+yxx8zDhw8vcv8dO3aYJZkvXrxoNpvN5u7du5tfeOGFQsceO3bMLMn8r3/9y9K2f/9+syRzenp6kWs8+OCDZhcXF6sa582bZ+mXZP7kk0/MZrPZ/MEHH5h9fX3Nly5dsvR//vnnZgcHB/OpU6fMZrPZXL16dfMbb7xhtUbLli3NQ4YMMZvNZvPChQvNfn5+5qtXr1r64+LizJLMu3btKrJOoCK51e+Om39vHD582CzJvGXLFsu+mZmZZnd3d/OKFSvMZrPZ/Nxzz5k7depkNf+YMWPMDRo0MJvNZvOhQ4fMkszbt2+39Kenp5slmefMmXMXjxLljXtUUKgOHTooLi7O8trDw6PIsQVnGPbs2aPz588rPz9fkpSRkaEGDRro5ZdfVs+ePZWWlqYnn3xSTz/9tNq2bWs1R5MmTSz/DgwMlPT7ad3Q0NAi1x0zZozVmZs/nqUpkJ6erqZNm1odQ7t27ZSfn69Dhw7J3d1dv/76q9q1a2e1X7t27bRnzx7LHE2aNJGbm5ulnw/OBGwV53dHenq6nJyc1Lp1a0ubn5+f6tevr/T0dMuYv/zlL1b7tWvXTnPnztWNGzcsc4SHh1v6Q0ND5ePjU8ZHBHsjqKBQHh4eCgkJue24gssqERERWrJkiapWraqMjAxFREQoNzdXktSlSxf99NNP+uKLL/TVV1/piSeeUHR0tGbNmmWZx9nZ2fJvk8kkSZbAUxR/f/9i1Qig/BT3dwdQXNyjgjty8OBBnT17VjNmzNCf/vQnhYaGFnqNuGrVqurfv78WL16suXPn6oMPPii3GsPCwrRnzx5dvnzZ0rZlyxY5ODiofv368vLyUvXq1bVlyxar/bZs2aIGDRpY5vj+++917do1S//WrVvL5wCA+0xYWJiuX7+ubdu2WdrOnj2rQ4cOWf3MFfYzWa9ePTk6Oio0NFTXr19Xamqqpf/QoUO6cOFCuRwDyg9BBXckODhYLi4u+sc//qEff/xRa9as0bRp06zGTJo0Sf/5z3909OhR7d+/X5999pnCwsLKrcZ+/frJzc1N/fv31759+7RhwwYNHTpUf/3rXy2f0j1mzBjNnDlTycnJOnTokMaNG6fdu3dr+PDhkqTnnntOJpNJgwYN0oEDB/TFF19YnRECUHx169bVX/7yFw0aNEibN2/Wnj17FBkZqRo1algu94waNUrr16/XtGnTdPjwYS1atEjvvfee5Sb2+vXrq3Pnzho8eLC2bdum1NRUvfjii3J3d7fnoeEuIKjgjlStWlVJSUlauXKlGjRooBkzZtj8AXdxcVFMTIyaNGmiRx99VI6Ojlq+fHm51VipUiWtW7dO586dU8uWLfXMM8/oiSee0HvvvWcZM2zYMI0cOVKjRo1S48aNtXbtWq1Zs0Z169aVJHl6eurTTz/V3r171bx5c40fP14zZ84st2MA7jeJiYkKDw9Xt27d1KZNG5nNZn3xxReWy8AtWrTQihUrtHz5cjVq1EiTJk1SbGys1X1piYmJql69uh577DH97//+r/72t7/pgQcesNMR4W4xmc1ms72LAAAAKAxnVAAAgGERVAAAgGERVAAAgGERVAAAgGERVAAAgGERVAAAgGERVAAAgGERVAAAgGERVAAAgGERVIAKaMCAATKZTDbb448/Ln9/f82YMaPQ/aZNm6Zq1aopLy9PSUlJhc7h5uZms84f51u9erXlU7KLqqVgq1WrVpHHcfz48VvuazKZNG3aNHl4eOjo0aNW+/7666/y9fW1fJRCrVq1LPt4eHioRYsWWrlypWX8lClTCp0/NDS0RF97ACVDUAEqqM6dO+vkyZNW20cffaTIyEglJibajDebzUpKStLzzz9v+TwWLy8vmzl++uknq/3c3Nw0c+ZMnT9/vtA65s2bZ7W/9PtnuBS83rFjR5HHEBQUZLXvqFGj1LBhQ6u20aNHKyIiQgMGDFB+fr5l30GDBik8PFzR0dGWttjYWJ08eVK7du1Sy5Yt1adPH3377beW/j/OffLkSW3evLkYX20ApeVk7wIA2Ierq6sCAgJs2gcOHKh58+Zp8+bNeuSRRyztX3/9tX788UcNHDjQ0mYymQqd42YdO3bU0aNHNX36dL311ls2/d7e3vL29rZq8/Hxue28kuTo6Gg1ztPTU05OTjb7Lly4UA0bNtQ777yj0aNHKykpSVu2bNHevXstZ3YkqXLlygoICFBAQIDmz5+vxYsX69NPP1Xbtm0lqdC5AdxdnFEBYKVx48Zq2bKlEhISrNoTExPVtm3bEl/qcHR01Jtvvql//OMf+vnnn8uy1GKrWrWqPvjgA02cOFFfffWVXn31Vc2bN09BQUFF7uPk5CRnZ2fl5uaWY6UA/oigAlRQn332mTw9Pa22N998U9LvZ1VWrlypS5cuSZIuXryoVatWKSoqymqOrKwsmzm6dOlis1aPHj3UrFkzTZ48+e4fWBGefvpp9e7dW507d9Zjjz2m/v37Fzk2NzdX06dPV1ZWlh5//HFL+969e22O96WXXiqP8oEKi0s/QAXVoUMHxcXFWbVVqVJFktS3b1+9+uqrWrFihaKiopScnCwHBwf16dPHanzlypWVlpZm1ebu7l7oejNnztTjjz+u0aNHl+FRlMzEiRP14YcfasKECYX2jx07VhMmTNC1a9fk6empGTNmqGvXrpb++vXra82aNVb7eHl53dWagYqOoAJUUB4eHgoJCSm0z8vLS88884wSExMVFRWlxMRE9e7dW56enlbjHBwcipzjjx599FFFREQoJiZGAwYMuNPyS8XJycnqf/9ozJgxGjBggDw9PVWtWjWr+1ckycXFpdjHC6BsEFQAFGrgwIFq3769PvvsM3377bd6++2373jOGTNmqFmzZqpfv34ZVFj2/P39CSKAwRBUgAoqJydHp06dsmpzcnKSv7+/pN/PgISEhOj5559XaGio5Z0vNzObzTZzSNIDDzwgBwfbW+AaN26sfv366d133y2joyhf169ftzlek8mkatWq2aki4P5HUAEqqLVr1yowMNCqrX79+jp48KCk3/8AR0VF6fXXX1dMTEyhc2RnZ9vMIUknT54s8m28sbGxSk5OvsPq7WP//v02x+vq6qpr167ZqSLg/mcym81mexcBAABQGN6eDAAADIugAsDQvvnmG5tnl9y8Abi/cekHgKFdvXpVv/zyS5H9vEsHuL8RVAAAgGFx6QcAABgWQQUAABgWQQUAABgWQQUAABgWQQUAABgWQQUAABgWQQUAABjW/wcUF2OzFdmbrAAAAABJRU5ErkJggg==)

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

<pre class="output-block">&nbsp;&nbsp;Downloading lxml-6.0.1-cp311-cp311-manylinux_2_26_x86_64.manylinux_2_28_x86_64.whl.metadata (3.8 kB)
Downloading lxml-6.0.1-cp311-cp311-manylinux_2_26_x86_64.manylinux_2_28_x86_64.whl (5.2 MB)
[?25l   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m0.0/5.2 MB[0m [31m?[0m eta [36m-:--:--[0m
</pre>

<pre class="output-block">
[2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m5.2/5.2 MB[0m [31m84.7 MB/s[0m  [33m0:00:00[0m
[?25h
</pre>

<pre class="output-block">Installing collected packages: lxml
</pre>

<pre class="output-block">Successfully installed lxml-6.0.1
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

    <pre class="output-block">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;count                       mean  \
    EVENT_TYPE
    Cold/Wind Chill            12            0 days 09:00:00
    Dense Fog                  40            0 days 07:27:00
    Extreme Cold/Wind Chill    26  0 days 12:20:46.153846153
    Flash Flood               121  0 days 02:13:29.256198347
    Flood                     125     4 days 01:25:38.880000
    Hail                      187  0 days 00:01:21.818181818
    Heat                       15            0 days 05:24:00
    Heavy Rain                 27  0 days 02:08:44.444444444
    Heavy Snow                131  0 days 16:16:49.923664122
    Thunderstorm Wind         383  0 days 00:00:41.984334203
    Tornado                    24            0 days 00:02:35
    Winter Storm               33  0 days 16:39:05.454545454
    Winter Weather            162  0 days 12:19:15.185185185
    
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;std              min  \
    EVENT_TYPE
    Cold/Wind Chill          0 days 02:05:20.154737286  0 days 07:00:00
    Dense Fog                0 days 03:16:24.370352945  0 days 04:00:00
    Extreme Cold/Wind Chill  0 days 04:00:33.883213306  0 days 03:00:00
    Flash Flood              0 days 03:20:21.201559833  0 days 00:00:00
    Flood                    7 days 03:59:43.207680028  0 days 00:00:00
    Hail                     0 days 00:01:23.851565542  0 days 00:00:00
    Heat                     0 days 00:49:41.083216358  0 days 05:00:00
    Heavy Rain               0 days 03:40:57.113426770  0 days 00:00:00
    Heavy Snow               0 days 06:48:08.251044631  0 days 08:00:00
    Thunderstorm Wind        0 days 00:01:27.395291215  0 days 00:00:00
    Tornado                  0 days 00:02:03.745882671  0 days 00:00:00
    Winter Storm             0 days 05:00:36.440386566  0 days 11:00:00
    Winter Weather           0 days 05:43:50.386658814  0 days 00:01:00
    
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;25%              50%              75%  \
    EVENT_TYPE
    Cold/Wind Chill          0 days 07:00:00  0 days 09:00:00  0 days 11:00:00
    Dense Fog                0 days 05:00:00  0 days 05:00:00  0 days 10:00:00
    Extreme Cold/Wind Chill  0 days 12:00:00  0 days 12:00:00  0 days 12:00:00
    Flash Flood              0 days 00:00:00  0 days 01:51:00  0 days 03:30:00
    Flood                    0 days 01:30:00  0 days 02:18:00  3 days 19:00:00
    Hail                     0 days 00:00:00  0 days 00:02:00  0 days 00:02:00
    Heat                     0 days 05:00:00  0 days 05:00:00  0 days 05:00:00
    Heavy Rain               0 days 00:00:00  0 days 00:00:00  0 days 03:00:00
    Heavy Snow               0 days 11:37:30  0 days 15:00:00  0 days 15:00:00
    Thunderstorm Wind        0 days 00:00:00  0 days 00:00:00  0 days 00:01:00
    Tornado                  0 days 00:01:00  0 days 00:02:00  0 days 00:03:15
    Winter Storm             0 days 12:30:00  0 days 15:00:00  0 days 20:00:00
    Winter Weather           0 days 07:15:00  0 days 11:00:00  0 days 17:00:00
    
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max
    EVENT_TYPE
    Cold/Wind Chill           0 days 11:00:00
    Dense Fog                 0 days 13:00:00
    Extreme Cold/Wind Chill   1 days 06:00:00
    Flash Flood               1 days 03:35:00
    Flood                    29 days 09:00:00
    Hail                      0 days 00:10:00
    Heat                      0 days 07:00:00
    Heavy Rain                0 days 12:15:00
    Heavy Snow                1 days 10:00:00
    Thunderstorm Wind         0 days 00:11:00
    Tornado                   0 days 00:08:00
    Winter Storm              1 days 02:00:00
    Winter Weather            1 days 06:00:00
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

    <pre class="output-block">/tmp/ipykernel_2217/1940921173.py:11: SettingWithCopyWarning:
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
    &nbsp;&nbsp;storms_no_flood["EVENT_DURATION_HOURS"] = storms_no_flood["EVENT_DURATION"].dt.total_seconds() / 3600
    </pre>

    ![A strip plot showing the duration of different events in hours in hours on the x-axis, ranging from 0 to 35. The y-axis shows the event type. Event types are 'Winter Weather', 'Heavy Snow', 'Thunderstorm Wind', 'Extreme Cold/Wind Chill', 'Hail', 'Heavy Rain', ''Tornado', 'Heat', 'Dense Fog', 'Cold/Wind Chill', and 'Winter Storm'. Winter Weather and Heavy Snow span the range of durations, while Winter Storms last between 10 and 26 hours. Thunderstorm Wind, Hail, and Tornados have short durations, less than 1 hour. There are few Extreme Cold/Wind Chill events, mostly around 13 hours long. Heat, Dense Fog, and Cold/Wind Chill events all last between 4 and 13 hours.](data:image/png;base64,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)

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

    <pre class="output-block">/tmp/ipykernel_2217/42002734.py:11: SettingWithCopyWarning:
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
    &nbsp;&nbsp;storms_flood_only["EVENT_DURATION_HOURS"] = storms_flood_only["EVENT_DURATION"].dt.total_seconds() / 3600
    </pre>

    ![A strip plot showing the duration of Flood and Flash flood events in hours on the x-axis, ranging from 0 to 700. The y-axis shows the event type. Flash Floods all last under 24 hours while Floods can last up to 700 hours.](data:image/png;base64,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ACxCeAMAALAI4Q0AAMAihDcAAACLEN4AAAAsQngDAACwCOENAADAImGBrgB8zxgjScrNzQ1wTQAAgKcKj9uFx3F3CG9V0PHjxyVJTZo0CXBNAACAt44fP664uDi36x2mrHgH6xQUFGj//v2qVauWHA6Hz7abm5urJk2a6Mcff1RsbKzPtmsL2k/7aT/tp/2035/tN8bo+PHjatSokUJC3F/ZRs9bFRQSEqLGjRv7bfuxsbHV8o+3EO2n/bSf9ldXtN//7S+tx60QAxYAAAAsQngDAACwCOENHouIiNC0adMUERER6KoEBO2n/bSf9tN+2h8MGLAAAABgEXreAAAALEJ4AwAAsAjhDQAAwCKENwAAAIsQ3uCxv/3tb0pMTFRkZKQ6d+6sL7/8MtBV8olPPvlE/fv3V6NGjeRwOLR06VKX9cYYPfDAA2rYsKGioqLUq1cv7dy506XMkSNHNHToUMXGxio+Pl633367Tpw4UYmtKJ+ZM2fqiiuuUK1atVS/fn3deOON2r59u0uZ06dPa9y4capTp45iYmJ000036dChQy5l9u3bp379+ik6Olr169fXpEmTlJeXV5lNKZd58+apXbt2zok3u3TpohUrVjjXV+W2l2TWrFlyOByaOHGic1lVfg0efPBBORwOl0dycrJzfVVue6Gff/5Zw4YNU506dRQVFaXU1FR99dVXzvVVef+XmJhY7P13OBwaN26cpCB//w3ggYULF5rw8HDzj3/8w2zdutWMGjXKxMfHm0OHDgW6ahX23nvvmfvuu88sXrzYSDJLlixxWT9r1iwTFxdnli5dajZt2mQGDBhgmjdvbk6dOuUs07t3b9O+fXvz+eefm08//dS0aNHCDBkypJJb4r20tDSTkZFhtmzZYrKyskzfvn1N06ZNzYkTJ5xlRo8ebZo0aWI+/PBD89VXX5mrrrrKXH311c71eXl5pm3btqZXr15m48aN5r333jN169Y1U6dODUSTvLJs2TLz7rvvmh07dpjt27ebe++919SoUcNs2bLFGFO1217Ul19+aRITE027du3MhAkTnMur8mswbdo006ZNG3PgwAHn45dffnGur8ptN8aYI0eOmGbNmpkRI0aYL774wuzevdusXLnS7Nq1y1mmKu//Dh8+7PLer1q1ykgyq1evNsYE9/tPeINHrrzySjNu3Djnz/n5+aZRo0Zm5syZAayV7xUNbwUFBSYhIcHMmTPHuezYsWMmIiLCvPbaa8YYY7799lsjyfzrX/9yllmxYoVxOBzm559/rrS6+8Lhw4eNJPPxxx8bY863tUaNGmbRokXOMtu2bTOSzPr1640x58NvSEiIOXjwoLPMvHnzTGxsrDlz5kzlNsAHateubV588cVq1fbjx4+bli1bmlWrVplu3bo5w1tVfw2mTZtm2rdvX+K6qt52Y4yZPHmyueaaa9yur277vwkTJphLL73UFBQUBP37z2lTlOns2bPasGGDevXq5VwWEhKiXr16af369QGsmf/t2bNHBw8edGl7XFycOnfu7Gz7+vXrFR8fr06dOjnL9OrVSyEhIfriiy8qvc4VkZOTI0m66KKLJEkbNmzQuXPnXNqfnJyspk2burQ/NTVVDRo0cJZJS0tTbm6utm7dWom1r5j8/HwtXLhQv/76q7p06VKt2j5u3Dj169fPpa1S9Xj/d+7cqUaNGumSSy7R0KFDtW/fPknVo+3Lli1Tp06ddMstt6h+/frq0KGD/v73vzvXV6f939mzZ7VgwQKNHDlSDocj6N9/whvK9O9//1v5+fkuH1BJatCggQ4ePBigWlWOwvaV1vaDBw+qfv36LuvDwsJ00UUXWfX6FBQUaOLEieratavatm0r6XzbwsPDFR8f71K2aPtLen0K1wW7zZs3KyYmRhERERo9erSWLFmilJSUatF2SVq4cKG+/vprzZw5s9i6qv4adO7cWZmZmXr//fc1b9487dmzR9dee62OHz9e5dsuSbt379a8efPUsmVLrVy5UmPGjNFdd92l+fPnS6pe+7+lS5fq2LFjGjFihKTg/+yH+XXrAKwxbtw4bdmyRWvXrg10VSpVq1atlJWVpZycHL355ptKT0/Xxx9/HOhqVYoff/xREyZM0KpVqxQZGRno6lS6Pn36OP/frl07de7cWc2aNdMbb7yhqKioANaschQUFKhTp06aMWOGJKlDhw7asmWLnnvuOaWnpwe4dpXrpZdeUp8+fdSoUaNAV8Uj9LyhTHXr1lVoaGixUTaHDh1SQkJCgGpVOQrbV1rbExISdPjwYZf1eXl5OnLkiDWvz/jx4/XOO+9o9erVaty4sXN5QkKCzp49q2PHjrmUL9r+kl6fwnXBLjw8XC1atFDHjh01c+ZMtW/fXk899VS1aPuGDRt0+PBhXX755QoLC1NYWJg+/vhjPf300woLC1ODBg2q/Gtwofj4eCUlJWnXrl3V4v1v2LChUlJSXJa1bt3aeeq4uuz/fvjhB33wwQe64447nMuC/f0nvKFM4eHh6tixoz788EPnsoKCAn344Yfq0qVLAGvmf82bN1dCQoJL23Nzc/XFF184296lSxcdO3ZMGzZscJb56KOPVFBQoM6dO1d6nb1hjNH48eO1ZMkSffTRR2revLnL+o4dO6pGjRou7d++fbv27dvn0v7Nmze77MBXrVql2NjYYgcGGxQUFOjMmTPVou09e/bU5s2blZWV5Xx06tRJQ4cOdf6/qr8GFzpx4oS+//57NWzYsFq8/127di02NdCOHTvUrFkzSVV//1coIyND9evXV79+/ZzLgv799+twCFQZCxcuNBERESYzM9N8++235s477zTx8fEuo2xsdfz4cbNx40azceNGI8nMnTvXbNy40fzwww/GmPND5ePj483bb79tvvnmGzNw4MASh8p36NDBfPHFF2bt2rWmZcuWVgyVHzNmjImLizNr1qxxGTJ/8uRJZ5nRo0ebpk2bmo8++sh89dVXpkuXLqZLly7O9YXD5a+//nqTlZVl3n//fVOvXj0rpkuYMmWK+fjjj82ePXvMN998Y6ZMmWIcDof55z//aYyp2m1358LRpsZU7dfg7rvvNmvWrDF79uwx69atM7169TJ169Y1hw8fNsZU7bYbc356mLCwMPOXv/zF7Ny507zyyismOjraLFiwwFmmKu//jDk/c0LTpk3N5MmTi60L5vef8AaP/fWvfzVNmzY14eHh5sorrzSff/55oKvkE6tXrzaSij3S09ONMeeHy99///2mQYMGJiIiwvTs2dNs377dZRvZ2dlmyJAhJiYmxsTGxpr/+q//MsePHw9Aa7xTUrslmYyMDGeZU6dOmbFjx5ratWub6Oho87vf/c4cOHDAZTt79+41ffr0MVFRUaZu3brm7rvvNufOnavk1nhv5MiRplmzZiY8PNzUq1fP9OzZ0xncjKnabXenaHiryq/BoEGDTMOGDU14eLi5+OKLzaBBg1zmOKvKbS+0fPly07ZtWxMREWGSk5PNCy+84LK+Ku//jDFm5cqVRlKxNhkT3O+/wxhj/Nu3BwAAAF/hmjcAAACLEN4AAAAsQngDAACwCOENAADAIoQ3AAAAixDeAAAA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q1WrVjp8+LAGDRqkTz75xKVMZGSkrrvuOl133XW6//77dccdd2jatGmV9lkCyoOeNwCV6vbbb9fatWv1zjvv6LPPPnMZqFBes2bN0vLly7V+/Xof1LBs8+fP19GjR3XTTTdJki666CLVrVtXGzZscCmXm5urXbt2OcNHSZo0aaJBgwZp6tSpkqTs7Gy9/fbbWrhwoUuP1caNG3X06FH985//9Lq+119/vS666CI9/vjjxdYtW7ZMO3fu1JAhQ9zWb/z48br33nuLTSniC4MHD9bOnTu1fPnyYusef/xx1alTR9ddd50kqVWrVvrpp5906NAhl3Jff/21IiMj1bRpU7fPM27cOG3ZskVLliwptT4pKSn69ddfy9ESoPLQ8wbAp86cOaODBw+6LAsLC1PdunUlne8pa9GihYYPH67k5OQSe4KMMcW2IZ0fPVhSr1NqaqqGDh2qp59+2ket+H8nT57UwYMHlZeXp59++klLlizRE088oTFjxqhHjx7Ocn/60580Y8YMNWjQQFdddZWys7P18MMPq169evr9739f6nNMmDBBbdu21VdffaW1a9eqTp06uvXWW4udlu3bt69eeukl9e7d26s21KxZU88//7xzipPx48crNjZWH374oSZNmqSbb75Zt956q9vfnzp1qv7+979rz549xU5xV9TgwYO1aNEipaena86cOerZs6dyc3P1t7/9TcuWLdOiRYucI03T0tLUqlUrDRkyRI888ogSEhL09ddf689//rMmTJig0NBQt88THR2tUaNGadq0abrxxht15MgR3XLLLRo5cqTatWunWrVq6auvvtKjjz6qgQMH+rSNgM8ZAPCR9PR0I6nYo1WrVi7lZsyYYSSZRx99tNg2MjIyStyGJHPgwAHn8wwcONDl9/bs2WPCw8ONu92aJLNkyRKv2tOtWzfnc4eHh5uGDRuaG264wSxevLhY2by8PPP000+b1NRUEx0dbRo3bmwGDRpk9uzZ41KuWbNm5oknnij2+2lpaaZPnz4mNTXVjB07tsT6vP766yY8PNz88ssvzjZLMhs3bixWtqTn+eSTT0xaWpqJjY014eHhpk2bNuaxxx4zeXl5LuVKeq0K37P09PQS61ZUSe+RMcasXr3aSDJHjx51Ljt37pyZM2eOadOmjQkPDzexsbEmLS3NrF27ttjv//zzzyY9Pd00bdrUREVFmZSUFDNr1ixz9uzZUp/DGGP27dtnwsLCzOuvv25Onz5tpkyZYi6//HITFxdnoqOjTatWrcyf//xnc/LkSY/aCASKwxg/XSkKAAAAn+OaNwAAAIsQ3gBUS59++mmxOcgufMC9ffv2lfra7du3L9BVBKo0TpsCqJZOnTqln3/+2e16T6cqqY7y8vJKnaA4MTFRYWGMhwP8hfAGAABgEU6bAgAAWITwBgAAYBHCGwAAgEUIbwAAABYhvAEAAFiE8AYAAGARwhsAAIBF/g/Sp/Iqe6J1CAAAAABJRU5ErkJggg==)

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

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

<pre class="output-block">--2025-08-27 20:00:08--  https://raw.githubusercontent.com/harvardinformatics/python-intensive/refs/heads/main/data/indiana_storms_full.csv
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 185.199.111.133, 185.199.108.133, 185.199.110.133, ...
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|185.199.111.133|:443... connected.
HTTP request sent, awaiting response...
</pre>

<pre class="output-block">200 OK
Length: 952491 (930K) [text/plain]
Saving to: ‘indiana_storms_full.csv’


indiana_storms_full   0%[                    ]       0  --.-KB/s
indiana_storms_full 100%[===================>] 930.17K  --.-KB/s    in 0.007s

2025-08-27 20:00:08 (122 MB/s) - ‘indiana_storms_full.csv’ saved [952491/952491]
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

    ![A barplot showing the number of Floods and Flash Floods in different counties in Indiana. The x-axis separates 'Flood' and 'Flash Flood' events, while the y-axis shows the number of events. Bars in each category are colored by county name. For Flash flood: Spencer 1, Marion 6, Vermillion 1, Monroe 0, Tippecanoe 0. For Flood: Spencer 1, Marion 4, Vermillion 1, Monroe 1, Tippecanoe 1. ](data:image/png;base64,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sqUqV66sBx54QE8//bQOHTpkz5IAAICB2DWofP3114qOjtbWrVv11VdfKS8vT08++aQuX75sz7IAAIBBONlz8bVr11q9TkpK0gMPPKDU1FQ9+uijNuNzcnKUk5NjeZ2dnX3XawQAAPZjqHtUsrKyJElVqlQptH/69Ony9va2bEFBQeVZHgAAKGeGCSr5+fkaMWKE2rVrp0aNGhU6JiYmRllZWZbtxIkT5VwlAAAoT3a99HOz6Oho7du3T5s3by5yjKurq1xdXcuxKgAAYE+GCCqvvPKKPvvsM23atEk1a9a0dzkAAMAg7BpUzGazhg4dqk8++UQbN25U7dq17VkOAAAwGLsGlejoaC1dulT/+c9/VLlyZZ06dUqS5O3tLXd3d3uWBgAADMCuN9PGxcUpKytL7du3V2BgoGVLTk62Z1kAAMAg7H7pBwAAoCiGeXsyAADAHxFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYdk1qGzatEndu3dX9erVZTKZtHr1anuWAwAADMauQeXy5ctq2rSp5s+fb88yAACAQTnZc/EuXbqoS5cu9iwBAAAYmF2DSknl5OQoJyfH8jo7O/uurpeRkaHMzMy7ukZppaen27uEYjFynf7+/goODrZ3GbAzfs7vnJHrzMnJkaurq73LuCWj12jv35X3VFCZPn26pk6dWi5rZWRkKDQ0TFevXimX9UrHpJNZ1yR527sQGzm5vwfKyMhIO1dSNPdK7jqYfpCwUoHxc35n7oWfc5kkme1dxK05SMq3dxG3UMm9ktIPptvtd+U9FVRiYmI0cuRIy+vs7GwFBQXdlbUyMzN19eoVtY6aLK/AWndljTvx27GD2r10pi5cuW7v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TZ48+e4fWBGefvpp9e7dW507d9Zjjz2m/v37Fzk2NzdX06dPV1ZWlh5//HFL+969e22O96WXXiqP8oEKi0s/QAXVoUMHxcXFWbVVqVJFktS3b1+9+uqrWrFihaKiopScnCwHBwf16dPHanzlypWVlpZm1ebu7l7oejNnztTjjz+u0aNHl+FRlMzEiRP14YcfasKECYX2jx07VhMmTNC1a9fk6empGTNmqGvXrpb++vXra82aNVb7eHl53dWagYqOoAJUUB4eHgoJCSm0z8vLS88884wSExMVFRWlxMRE9e7dW56enlbjHBwcipzjjx599FFFREQoJiZGAwYMuNPyS8XJycnqf/9ozJgxGjBggDw9PVWtWjWr+1ckycXFpdjHC6BsEFQAFGrgwIFq3769PvvsM3377bd6++2373jOGTNmqFmzZqpfv34ZVFj2/P39CSKAwRBUgAoqJydHp06dsmpzcnKSv7+/pN/PgISEhOj5559XaGio5Z0vNzObzTZzSNIDDzwgBwfbW+AaN26sfv366d133y2joyhf169ftzlek8mkatWq2aki4P5HUAEqqLVr1yowMNCqrX79+jp48KCk3/8AR0VF6fXXX1dMTEyhc2RnZ9vMIUknT54s8m28sbGxSk5OvsPq7WP//v02x+vq6qpr167ZqSLg/mcym81mexcBAABQGN6eDAAADIugAsDQvvnmG5tnl9y8Abi/cekHgKFdvXpVv/zyS5H9vEsHuL8RVAAAgGFx6QcAABgWQQUAABgWQQUAABgWQQUAABgWQQUAABgWQQUAABgWQQUAABjW/wcUF2OzFdmbrAAAAABJRU5ErkJggg==)

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
[2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m5.2/5.2 MB[0m [31m73.4 MB/s[0m  [33m0:00:00[0m
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

    <pre class="output-block">/tmp/ipykernel_2220/1940921173.py:11: SettingWithCopyWarning:
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

    <pre class="output-block">/tmp/ipykernel_2220/42002734.py:11: SettingWithCopyWarning:
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
    &nbsp;&nbsp;storms_flood_only["EVENT_DURATION_HOURS"] = storms_flood_only["EVENT_DURATION"].dt.total_seconds() / 3600
    </pre>

    ![A strip plot showing the duration of Flood and Flash flood events in hours on the x-axis, ranging from 0 to 700. The y-axis shows the event type. Flash Floods all last under 24 hours while Floods can last up to 700 hours.](data:image/png;base64,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peuvv17PPvusVq5c6WzZ2r9/v9q2bav27dsrMTFR3bp1U+/evV328cADD6hXr15KSkrSn//8Z/3www9ux9hNmDDBpYzPPvtskdu99tprOnfunP75z3+qVatW+s1vfqPnnntOr7zyio4cOSJJeuKJJzRhwgQNHDhQzZo106xZs3TNNdfo6aefdu4jLy9PL7/8slq2bKnbbrtN48ePL7F8M2bMUGxsrPPWsGHDErcHAAD2CviYty5dumju3LnO+9WqVSt22/yWqC1btujEiRPKy8uTdCm0JScn695771X//v319ddf69Zbb1W/fv10ww03uOyjdevWzv/Xq1dPknT06FE1b9682OOOHz/epYWvYGtevh07dqhNmzYudejUqZPy8vK0c+dORUZG6uDBg+rUqZPL4zp16qQtW7Y499G6dWtFREQ413fs2LHYsknSpEmT9Mc//tF5Pzs726cBLsQheTKcLSqMsYAAAPhbwMNbtWrV1KRJE7fb5XdJpqam6tVXX1WdOnW0f/9+paam6sKFC5KkHj166IcfftCKFSu0evVqde3aVaNHj9YTTzzh3E/VqlWd/3f857ea8kNgcWrXru1RGQMlPDxc4eHhftu/p/MQht2Q6LcyAACASwLebeqp7777TseOHdPMmTN14403qnnz5i6TFfLVqVNHaWlpmj9/vp5++mm9+OKL5VbGFi1aaMuWLfrll1+cy9avX6+QkBA1a9ZMMTExql+/vtavX+/yuPXr1ys5Odm5j2+++Ubnzp1zrv/888/LpwJlMKrz1fq/7sW3XgIAAN+wJrw1atRIYWFh+utf/6o9e/Zo6dKlmjZtmss2Dz/8sN555x3t3r1b27dv1/Lly9WiRYtyK+PgwYMVERGhtLQ0bdu2TWvWrNH/+3//T3fddZfi4+MlXeqCnTVrlt544w3t3LlTEydO1ObNmzV27FhJ0u9+9zs5HA6NGDFC3377rVasWOHSchisCG4AAJQPa8JbnTp1lJGRoYULFyo5OVkzZ84sFGrCwsI0adIktW7dWjfddJOqVKmiBQsWlFsZo6KitGrVKh0/flzXXXedbr/9dnXt2lXPPfecc5v77rtPf/zjH3X//fcrJSVF7733npYuXaqmTZtKkqKjo7Vs2TJt3bpVbdu21UMPPaRZs2aVWx1Ka9X2w4EuAgAAlYLDGMOVVSuY7OxsxcbG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eumll4o8/uuvv64qVapo9OjRRZapqFvnzp2dx3n66add9vfZZ5+pZ8+eqlGjhiIiIpSSkqLZs2crNzfXZbv85/uHH35wWd6vXz8NGzas5CftP4YNG6Z+/foVWr527Vo5HA6dPHnSuSw3N1dPPfWUUlJSFBERoRo1aqhHjx5av369y2MfeeQRXXPNNYX2WfD5zz9G/q1OnTrq2bOntm7d6vK4n3/+Wffee68aNWqk8PBwJSQkKDU1tdBxgWBDeAPgU927d9ehQ4dcbm+//baGDBmi9PT0QtsbY5SRkaGhQ4eqatWqkqSYmJhC+ygYJCIiIjRr1iydOHGiyHI888wzLo+XpPT0dOf9f/3rXx7VZ8SIETp06JC+//57vf3220pOTtbAgQP1+9//3punxcXUqVN16NAhbdu2TUOGDNGIESO0cuXKQtu9/PLL+r//+z+9/vrrOnfunCRp0aJFzjp8+eWXkqQPPvjAuaxgsMy3ePFi3XzzzWrQoIHWrFmj7777TmPHjtWjjz6qgQMHquAvJTocDj388MOlrqOnjDEaOHCgpk6dqrFjx2rHjh1au3atGjZsqM6dO2vJkiWl3vfOnTt16NAhrVq1SufPn1evXr104cIF5/r+/ftr06ZNmjdvnnbt2qWlS5eqc+fOOnbsmA9qBvhPaKALAKBiyW/BKOjuu+/WM888o3Xr1unXv/61c/nHH3+sPXv26O6773YuczgcRe7jct26ddPu3bs1Y8YMPfbYY4XWx8bGKjY21mVZXFyc2/0WFBUV5XxMgwYNdP3116t58+YaPny47rzzTnXr1s2r/UlS9erVnfucMGGCHnvsMa1evVo9evRwbrN371599tlnevvtt7VmzRotWrRIv/vd71SzZk3nNvmBrlatWiXW65dfftGIESPUp08fvfjii87l99xzj+Lj49WnTx+9+eabGjBggHPdmDFjNHv2bI0fP16tWrXyuo6eevPNN/XWW29p6dKl6t27t3P5iy++qGPHjumee+7RLbfcomrVqnm977p16zpf83HjxqlPnz767rvv1Lp1a508eVKffvqp1q5dq5tvvlmS1LhxY/3qV7/yWd0Af6HlDUC5SElJ0XXXXad//OMfLsvT09N1ww03qHnz5l7tr0qVKpo+fbr++te/6qeffvJlUd1KS0tTjRo1im3l8lReXp7efvttnThxQmFhYS7r0tPT1atXL8XGxmrIkCF6+eWXS32c999/X8eOHdMDDzxQaF3v3r2VlJSk119/3WV5p06ddNttt2nixImlPq4nXnvtNSUlJbkEt3z333+/jh07ptWrV5fpGFlZWVqwYIEkOZ/n6OhoRUdHa8mSJTp//nyZ9g+UN8IbAJ9avny588SYf5s+fbqkS61vCxcu1OnTpyVJp06d0ltvvaXhw4e77CMrK6vQPi5vlcr329/+Vtdcc42mTJni/4pdJiQkRElJSdq3b1+pHj9hwgRFR0crPDxct99+u2rUqKF77rnHuT4vL08ZGRkaMmSIJGngwIFat26d9u7dW6rj7dq1S5LUokWLItc3b97cuc3lZsyYoffee0+ffvppqY5b1Huh4Ou4a9euYsuVv7yosnmiQYMGio6OVlxcnF577TX16dPH+SUhNDRUGRkZmjdvnuLi4tSpUyc9+OCD+uabb0p1LKA8Ed4A+FSXLl20efNml9vIkSMlSYMGDVJubq7efPNNSdIbb7yhkJAQl+466VK3YsF9FDeof9asWZo3b5527Njh34oVYIxxTo7w1vjx47V582Z99NFH6tChg5566ik1adLEuX716tX65Zdf1LNnT0lS7dq1dcsttxRqtSxNmb2RnJysoUOHlrr1raj3QlGvo7fl8tSnn36qjRs3KiMjQ0lJSXr++edd1vfv318HDx7U0qVL1b17d61du1bXXnutMjIy/FIewFcY8wbAp6pVq+YSRC4XExOj22+/Xenp6Ro+fLjS09N15513Kjo62mW7kJCQYvdR0E033aTU1FRNmjTJ45mQZZWbm6vMzExdd911ki7VS7rUYljQyZMnC429q127tpo0aaImTZpo4cKFSklJUfv27ZWcnCzp0kSF48ePKzIy0vmYvLw8ffPNN/rzn/+skBDvvncnJSVJknbs2KEbbrih0PodO3Y4j13Qn//8ZyUlJZVq4kBR74WCXdxJSUnFBu/85fnlj4mJKfY5llToeb7yyisVFxenZs2a6ejRoxowYIA++eQTl20iIiJ0yy236JZbbtHkyZN1zz33aMqUKeX2XgJKg5Y3AOXq7rvv1rp167R8+XJ99tlnLhMVSmvmzJlatmyZNmzY4IMSujdv3jydOHFC/fv3lyTVrFlTtWvX1saNG122y87O1u7du53hoygNGzbUgAEDNGnSJEnSsWPH9M4772jBggUuLVabNm3SiRMn9P7773td3ltvvVU1a9bUk08+WWjd0qVLlZmZqUGDBhVbvjFjxujBBx8sdEkRXxg4cKAyMzO1bNmyQuuefPJJ1apVS7fccoskqVmzZvrpp5905MgRl+2+/vprRUREqFGjRsUeZ/To0dq2bZsWL15cYnmSk5P1yy+/lKImQPmh5Q2AT50/f16HDx92WRYaGqratWtLutRS1qRJEw0dOlTNmzcvsiXIGFNoH9Kl2YNFtTqlpKRo8ODBevbZZ31Ui/86c+aMDh8+rJycHP30009avHixnnrqKd17773q0qWLc7s//vGPmj59uuLj43X99dfr2LFjmjZtmurUqaP/+Z//KfEYY8eOVatWrfTVV19p3bp1qlWrlu68885C3bI9e/bUyy+/rO7du3tVh2rVqumFF15wXuJkzJgxiomJ0Ycffqjx48fr9ttv15133lns4ydNmqS///3v2rt3b6Eu7rIaOHCgFi5cqLS0ND3++OPq2rWrsrOz9be//U1Lly7VwoULnTNNU1NT1axZMw0aNEiPPvqoEhIS9PXXX+tPf/qTxo4dqypVqhR7nKioKI0YMUJTpkxRv379dPz4cd1xxx0aPny4WrdurerVq+urr77SY489pr59+/q0joDPGQDwkbS0NCOp0K1Zs2Yu202fPt1IMo899lihfaSnpxe5D0nm0KFDzuP07dvX5XF79+41YWFhpriPNUlm8eLFXtXn5ptvdh47LCzM1KtXz9x2221m0aJFhbbNyckxzz77rElJSTFRUVGmQYMGZsCAAWbv3r0u2zVu3Ng89dRThR6fmppqevToYVJSUsyoUaOKLM8bb7xhwsLCzM8//+yssySzadOmQtsWdZxPPvnEpKammpiYGBMWFmZatmxpnnjiCZOTk+OyXVHPVf5rlpaWVmTZCirqNTLGmDVr1hhJ5sSJE85lFy9eNI8//rhp2bKlCQsLMzExMSY1NdWsW7eu0OMPHDhg0tLSTKNGjUxkZKRJTk42M2fONBcuXCjxGMYYs3//fhMaGmreeOMNc+7cOTNx4kRz7bXXmtjYWBMVFWWaNWtm/vSnP5kzZ854VEcgUBzG+GmkKAAAAHyOMW8AAAAWIbwBqJQ+/fTTQtcgu/yG4u3fv7/E527//v2BLiJQodFtCqBSOnv2rA4cOFDsek8vVVIZ5eTklHiB4sTERIWGMh8O8BfCGwAAgEXoNgUAALAI4Q0AAMAihDcAAACLEN4AAAAsQngDAACwCOENAADAIoQ3AAAAi/x/RaDsKnGy3TAAAAAASUVORK5CYII=)

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

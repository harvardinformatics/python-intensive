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

<pre class="output-block">--2025-08-28 02:34:46--  https://raw.githubusercontent.com/harvardinformatics/python-intensive/refs/heads/main/data/indiana_storms_full.csv
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 185.199.110.133, 185.199.108.133, 185.199.111.133, ...
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|185.199.110.133|:443... connected.
HTTP request sent, awaiting response...
</pre>

<pre class="output-block">200 OK
Length: 952491 (930K) [text/plain]
Saving to: ‘indiana_storms_full.csv’


indiana_storms_full   0%[                    ]       0  --.-KB/s
indiana_storms_full 100%[===================>] 930.17K  --.-KB/s    in 0.006s

2025-08-28 02:34:47 (150 MB/s) - ‘indiana_storms_full.csv’ saved [952491/952491]
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
</pre>

<pre class="output-block">Downloading lxml-6.0.1-cp311-cp311-manylinux_2_26_x86_64.manylinux_2_28_x86_64.whl (5.2 MB)
[?25l   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m0.0/5.2 MB[0m [31m?[0m eta [36m-:--:--[0m
</pre>

<pre class="output-block">
[2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m5.2/5.2 MB[0m [31m70.7 MB/s[0m  [33m0:00:00[0m
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

    <pre class="output-block">/tmp/ipykernel_2218/1940921173.py:11: SettingWithCopyWarning:
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

    <pre class="output-block">/tmp/ipykernel_2218/42002734.py:11: SettingWithCopyWarning:
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
    &nbsp;&nbsp;storms_flood_only["EVENT_DURATION_HOURS"] = storms_flood_only["EVENT_DURATION"].dt.total_seconds() / 3600
    </pre>

    ![A strip plot showing the duration of Flood and Flash flood events in hours on the x-axis, ranging from 0 to 700. The y-axis shows the event type. Flash Floods all last under 24 hours while Floods can last up to 700 hours.](data:image/png;base64,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ycnJ6tOnjwYOHOiyj3vuuUcDBgxQSkqK/vznP+u7774r9xq7yZMnu5TxySefdLvdyy+/rNOnT+v//u//1K5dO/3yl7/UU089pRdeeEGHDh2SJD3yyCOaPHmyhg4dqlatWmnu3Lm64oor9Pjjjzv3UVRUpAULFqht27a68cYbNWnSpDLLN3v2bMXFxTkfTZs2LXN7f8k/XaDLpr6tng+v5ZZXAAD4ScDDW69evZSdne18lBaMJGnTpk0aOHCgmjVrpjp16qhHjx6Szoc2Sbrzzju1aNEiXXHFFfrjH/+ojz/+uMQ+OnTo4Px/o0aNJMml69WdSZMmuZRx5MiRbrfbvn27OnbsqNq1azuXde/eXUVFRdqxY4fy8/N14MABde/e3eV53bt31/bt25376NChgyIjI53ru3XrVmb5pk6dqry8POfj+++/L3N7fyoy0r7ckxrzAvcsBQDAHwI+YKF27dpq0aJFudsVd0mmpaXppZdeUoMGDbR//36lpaXp7NmzkqR+/frpu+++08qVK7VmzRr17t1b48aN0yOPPOLcT61atZz/d/xnxtiioqIyXzshIcGjMgZKRESEIiIiAl0MF0bn71maRjcqAAA+FfCWN0998803ys3N1Zw5c3TdddepdevWblvMGjRooPT0dL344ot6/PHH9dxzz1VZGdu0aaMvv/xSP//8s3PZhg0bFBISolatWik2NlaNGzfWhg0bXJ63YcMGpaamOvfx1Vdf6fTp/07P8cknn1RNBXyMaUMAAPA9a8Jbs2bNFB4err/+9a/as2ePli9frpkzZ7psc//99+vNN9/U7t27tW3bNr311ltq06ZNlZVx+PDhioyMVHp6urZu3aq1a9fq//2//6ff/va3SkxMlHS+C3bu3Ll69dVXtWPHDk2ZMkXZ2dmaMGGCJOk3v/mNHA6HRo8era+//lorV650aTm0CdOGAADge9aEtwYNGigrK0uLFy9Wamqq5syZUyLUhIeHa+rUqerQoYOuv/56hYaGatGiRVVWxujoaK1evVpHjhzRVVddpVtuuUW9e/fWU0895dzmrrvu0h/+8Afdfffdat++vd555x0tX75cLVu2lCTFxMRoxYoV2rJlizp16qT77rtPc+fOrbI6+IpDTBsCAIA/OIzxYgZWWCE/P19xcXHKy8tTbGxspfeXPOVtj7cNcUjN6kXr3v5t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hAkTnMur83swffp007ZtW3Pw4EHn46effnKur851N8aYI0eOmObNm5uMjAzz6aefmj179pjVq1eb3bt3O7epzt9/hw8fdvns16xZYySZtWvXGmOC+/MnvMEjv/jFL8y4ceOcPxcWFprGjRub2bNnB7BUvndxeCsqKjJJSUnm4Ycfdi47duyYiYiIMK+88ooxxpivv/7aSDL/+te/nNusWrXKOBwO8+OPP1ZZ2X3h8OHDRpL54IMPjDHn61qrVi2zePFi5zbbt283kszGjRuNMefDb0hIiMnJyXFuM3/+fBMbG2vOnDlTtRXwgbp165rnn3++RtX9+PHjpmXLlmbNmjWmR48ezvBW3d+D6dOnm44dO7pdV93rbowxkydPNtdee22p62va99+ECRPM5ZdfboqKioL+86fbFOU6e/asNm3apD59+jiXhYSEqE+fPtq4cWMAS+Z/e/fuVU5Ojkvd4+Li1LVrV2fdN27cqPj4eHXp0sW5TZ8+fRQSEqJPP/20ystcGXl5eZKkevXqSZI2bdqkc+fOudS/devWatasmUv927dvr8TEROc2aWlpys/P17Zt26qw9JVTWFioRYsW6eeff1a3bt1qVN3HjRunAQMGuNRVqhmf/65du9S4cWNddtllGj58uPbv3y+pZtR9+fLl6tKli2699VY1bNhQnTp10t///nfn+pr0/Xf27Fm9+OKLGjVqlBwOR9B//oQ3lOvf//63CgsLXQ5QSUpMTFROTk6ASlU1iutXVt1zcnLUsGFDl/VhYWGqV6+eVe9PUVGRJk6cqO7du6tdu3aSztctPDxc8fHxLtteXH9370/xumC3ZcsWxcTEKCIiQmPGjNHSpUuVmppaI+ouSYsWLdIXX3yh2bNnl1hX3d+Drl27KisrS++8847mz5+vvXv36rrrrtPx48erfd0lac+ePZo/f75atmyp1atX684779Rdd92lhQsXSqpZ33/Lli3TsWPHlJGRISn4j/0wv+4dgDXGjRunrVu3av369YEuSpVq1aqVsrOzlZeXp9dff13p6en64IMPAl2sKvH9999rwoQJWrNmjSIjIwNdnCrXr18/5/87dOigrl27qnnz5nrttdcUFRUVwJJVjaKiInXp0kWzZs2SJHXq1Elbt27VM888o/T09ACXrmotWLBA/fr1U+PGjQNdFI/Q8oZyJSQkKDQ0tMQo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XaslS5boN7/5jerVq+fcpjjQ1a9fv8x6/fzzzxo9erQGDRqk5557zrn8jjvuUGJiogYNGqTXXntNQ4YMca4bP3685s2bp0mTJqldu3Ze19FTr732ml5//XUtX75cAwcOdC5/7rnnlJubqzvuuEM33HCDateu7fW+GzZs6PzMJ06cqEGDBumbb75Rhw4ddOzYMX300Udat26devToIUlq3ry5fvGLX/isboC/0PIGoEq0b99eV111lf7xj3+4LM/MzNQ111yj1q1be7W/0NBQzZo1S3/961/1ww8/+LKo5UpPT1fdunVLbeXyVFFRkd544w0dPXpU4eHhLusyMzM1YMAAxcXFacSIEVqwYEGFX+ef//yncnNzdc8995RYN3DgQKWkpOiVV15xWd69e3fdeOONmjJlSoVf1xMvv/yyUlJSXIJbsbvvvlu5ublas2ZNpV4jLy9PixYtkiTn+xwTE6OYmBgtW7ZMZ86cqdT+gapGeAPgU2+99ZbzxFj8mDVrlqTzrW+LFy/WiRMnJEnHjx/X66+/rlGjRrnsIy8vr8Q+LmyVKvbrX/9aV1xxhaZPn+7/il0gJCREKSkp2rdvX4WeP3nyZMXExCgiIkK33HKL6tatqzvuuMO5vqioSFlZWRoxYoQkaejQoVq/fr327t1bodfbuXOnJKlNmzZu17du3dq5zYVmz56td955Rx999FGFXtfdsXDx57hz585Sy1W83F3ZPNGkSRPFxMQoPj5eL7/8sgYNGuT8IyEsLExZWVlauHCh4uPj1b17d91777366quvKvRaQFUivAHwqV69eik7O9vlMWbMGEnSsGHDVFhYqNdee02S9OqrryokJMSlu04636148T5Ku6h/7ty5WrhwobZv3+7fil3EGOMcHOGtSZMmKTs7W++//766du2qxx57TC1atHCuX7NmjX7++Wf1799fkpSQkKAbbrihRKtlRcrsjdTUVI0cObLCrW/ujgV3n6O35fLURx99pE2bNikrK0spKSl65plnXNbffPPNOnDggJYvX66+fftq3bp1uvLKK5WVleWX8gC+wjVvAHyqdu3aLkHkQrGxsbrllluUmZmpUaNGKTMzU7fddptiYmJctgsJCSl1Hxe7/vrrlZaWpqlTp3o8ErKyCgsLtWvXLl111VWSztdLOt9ieLFjx46VuPYuISFBLVq0UIsWLbR48WK1b99eXbp0UWpqqqTzAxWOHDmiqKgo53OKior01Vdf6c9//rNCQrz7uzslJUWStH37dl1zzTUl1m/fvt352hf785//rJSUlAoNHHB3LFzcxZ2SklJq8C5eXlz+2NjYUt9jSSXe50svvVTx8fFq1aqVDh8+rCFDhujDDz902SYyMlI33HCDbrjhBk2bNk133HGHpk+fXmXHElARtLwBqFK333671q9fr7feeksff/yxy0CFipozZ45WrFihjRs3+qCE5Vu4cKGOHj2qm2++WZJUr149JSQkaNOmTS7b5efna/fu3c7w4U7Tpk01ZMgQTZ06VZKUm5urN998U4sWLXJpsdq8ebOOHj2qf/7zn16X91e/+pXq1aunRx99tMS65cuXa9euXRo2bFip5Rs/frzuvffeElOK+MLQoUO1a9curVixosS6Rx99VPXr19cNN9wgSWrVqpV++OEHHTp0yGW7L774QpGRkWrWrFmprzNu3Dht3bpVS5cuLbM8qamp+vnnnytQE6Dq0PIGwKfOnDmjnJwcl2VhYWFKSEiQdL6lrEWLFho5cqRat27ttiXIGFNiH9L50YPuWp3at2+v4cOH68knn/RRLf7r5MmTysnJUUFBgX744QctXbpUjz32mO6880716tXLud0f/vAHzZo1S4mJibr66quVm5urmTNnqkGDBvqf//mfMl9jwoQJateunT7//HOtX79e9evX12233VaiW7Z///5asGCB+vbt61UdateurWeffdY5xcn48eMVGxur9957T5MmTdItt9yi2267rdTnT506VX//+9+1d+/eEl3clTV06FAtXrxY6enpevjhh9W7d2/l5+frb3/7m5YvX67Fixc7R5qmpaWpVatWGjZsmB588EElJSXpiy++0J/+9CdNmDBBoaGhpb5OdHS0Ro8erenTp+umm27SkSNHdOutt2rUqFHq0KGD6tSpo88//1wPPfSQBg8e7NM6Aj5nAMBH0tPTjaQSj1atWrlsN2vWLCPJPPTQQyX2kZmZ6XYfkszBgwedrzN48GCX5+3du9eEh4eb0r7WJJmlS5d6VZ8ePXo4Xzs8PNw0atTI3HjjjWbJkiUlti0oKDBPPvmkad++vYmOjjZNmjQxQ4YMMXv37nXZrnnz5uaxxx4r8fy0tDTTr18/0759ezN27Fi35Xn11VdNeHi4+emnn5x1lmQ2b95cYlt3r/Phhx+atLQ0Exsba8LDw03btm3NI488YgoKCly2c/deFX9m6enpbst2MXefkTHGrF271kgyR48edS47d+6cefjhh03btm1NeHi4iY2NNWlpaWb9+vUlnv/jjz+a9PR006xZMxMVFWVSU1PNnDlzzNmzZ8t8DWOM2b9/vwkLCzOvvvqqOX36tJkyZYq58sorTVxcnImOjjatWrUyf/rTn8zJkyc9qiMQKA5j/HSlKAAAAHyOa94AAAAsQngDUCN99NFHJeYgu/CB0u3fv7/M927//v2BLiJQrdFtCqBGOnXqlH788cdS13s6VUlNVFBQUOYExcnJyQoLYzwc4C+ENwAAAIvQbQoAAGARwhsAAIBFCG8AAAAWIbwBAABYhPAGAABgEcIbAACARQhvAAAAFvn/45jC9/0GyZoAAAAASUVORK5CYII=)

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

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

<pre class="output-block">--2025-08-28 02:38:14--  https://raw.githubusercontent.com/harvardinformatics/python-intensive/refs/heads/main/data/indiana_storms_full.csv
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 185.199.108.133, 185.199.111.133, 185.199.110.133, ...
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|185.199.108.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 952491 (930K) [text/plain]
Saving to: ‘indiana_storms_full.csv’


indiana_storms_full   0%[                    ]       0  --.-KB/s
indiana_storms_full 100%[===================>] 930.17K  --.-KB/s    in 0.01s
</pre>

<pre class="output-block">2025-08-28 02:38:14 (78.1 MB/s) - ‘indiana_storms_full.csv’ saved [952491/952491]
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

    ![A barplot showing the number of Floods and Flash Floods in different counties in Indiana. The x-axis separates 'Flood' and 'Flash Flood' events, while the y-axis shows the number of events. Bars in each category are colored by county name. For Flash flood: Spencer 1, Marion 6, Vermillion 1, Monroe 0, Tippecanoe 0. For Flood: Spencer 1, Marion 4, Vermillion 1, Monroe 1, Tippecanoe 1. ](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAioAAAGwCAYAAACHJU4LAAAAOnRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjEwLjUsIGh0dHBzOi8vbWF0cGxvdGxpYi5vcmcvWftoOwAAAAlwSFlzAAAPYQAAD2EBqD+naQAARLJJREFUeJzt3XlclXX+///nYUeQRTBBhdRQwV1J/ahNaWlo6kx+TM1k0jDHklxySckdp9TS1CZDm2GxcUOtHNv0G45mWm6g5oJbaVi5hAu4Asr5/dGP8/F0QAGRcymP++123cbzfr+v9/t1MSzPrus61zGZzWazAAAADMjB3gUAAAAUhaACAAAMi6ACAAAMi6ACAAAMi6ACAAAMi6ACAAAMi6ACAAAMy8neBdyJ/Px8/frrr6pcubJMJpO9ywEAAMVgNpt18eJFVa9eXQ4Otz5nck8HlV9//VVBQUH2LgMAAJTCiRMnVLNmzVuOuaeDSuXKlSX9fqBeXl52rgYAABRHdna2goKCLH/Hb+WeDioFl3u8vLwIKgAA3GOKc9sGN9MCAADDIqgAAADDIqgAAADDuqfvUQEA2N+NGzeUl5dn7zJgIM7OznJ0dCyTuQgqAIBSMZvNOnXqlC5cuGDvUmBAPj4+CggIuOPnnBFUAAClUhBSHnjgAVWqVIkHb0LS7wH2ypUrOnPmjCQpMDDwjuYjqAAASuzGjRuWkOLn52fvcmAw7u7ukqQzZ87ogQceuKPLQNxMCwAosYJ7UipVqmTnSmBUBd8bd3r/EkEFAFBqXO5BUcrqe4OgAgAADIugAgAADMvuQeWXX35RZGSk/Pz85O7ursaNG2vnzp32LgsAABiAXYPK+fPn1a5dOzk7O+vLL7/UgQMHNHv2bPn6+tqzLADAPezUqVMaOnSo6tSpI1dXVwUFBal79+5av369pkyZIpPJVOQ2derU286flJQkk8mkzp07W7VfuHBBJpNJGzdutNln8ODBcnR01MqVK236Cmr643yS9Pbbb8tkMql9+/Y24/+4hYaG3v6Lcw+y69uTZ86cqaCgICUmJlraateubceKAAD3suPHj6tdu3by8fHR22+/rcaNGysvL0/r1q1TdHS0du7cqZdeeslmv5iYGK1evVrPPfdcsdZxcnJSSkqKNmzYoA4dOtxy7JUrV7R8+XK99tprSkhIUK9evWzGBAYGasOGDfr5559Vs2ZNS3tCQoKCg4Ntxjds2FApKSk2Nd2P7HpUa9asUUREhHr16qWvv/5aNWrU0JAhQzRo0KBCx+fk5CgnJ8fyOjs7u7xKNaSMjAxlZmbau4wi+fv7F/oDBgB3y5AhQ2QymbR9+3Z5eHhY2hs2bKioqCh5enrK09PTap8lS5bo3//+tz7//HPVrVu3WOt4eHiod+/eGjdunLZt23bLsStXrlSDBg00btw4Va9eXSdOnFBQUJDVmAceeEDh4eFatGiRxo8fL0n69ttvlZmZqV69eunAgQNW452cnBQQEFCsWu91dg0qP/74o+Li4jRy5Ei9/vrr2rFjh4YNGyYXFxf179/fZvz06dOLdVquIsjIyFBYaH1duXrN3qUUqZK7m9IPHiKsACgX586d09q1a/XGG29YhZQCPj4+Nm2pqakaNGiQZsyYoYiIiBKtN2XKFIWEhGjVqlV65plnihwXHx+vyMhIeXt7q0uXLkpKStLEiRNtxkVFRem1116zBJWEhAT169evRDXdj+waVPLz8/Xwww/rzTfflCQ1b95c+/bt04IFCwoNKjExMRo5cqTldXZ2tk0qrSgyMzN15eo1Lf5bM4UFet5+h3KWfvKSIj/YrczMTIIKgHJx9OhRmc3mYt+rcebMGfXo0UM9e/bU6NGjS7xe9erVNXz4cI0fP15PP/10oWOOHDmirVu36uOPP5YkRUZGauTIkZowYYLNc0a6deuml156SZs2bVJ4eLhWrFihzZs3KyEhwWbevXv32pwZioyM1IIFC0p8HEZn16ASGBioBg0aWLWFhYXpo48+KnS8q6urXF1dy6O0e0ZYoKda1PK2dxkAYHdms7nYY/Py8vTMM8+oWrVq+uc//1nqNceOHauFCxcqISFBvXv3tulPSEhQRESE/P39JUlPPfWUBg4cqP/+97964oknrMY6OzsrMjJSiYmJ+vHHH1WvXj01adKk0HXr16+vNWvWWLV5eXmV+jiMzK5BpV27djp06JBV2+HDh/Xggw/aqSIAwL2qbt26MplMOnjw4G3HDhs2TEeOHNGOHTvk5uZW6jV9fHwUExOjqVOnqlu3blZ9N27c0KJFi3Tq1CmrG11v3LihhIQEm6Ai/X75p3Xr1tq3b5+ioqKKXNfFxUUhISGlrvteYte3J7/66qvaunWr3nzzTR09elRLly7VBx98oOjoaHuWBQC4B1WpUkURERGaP3++Ll++bNN/4cIFSdIHH3yghIQEffTRR1bvsCmtoUOHysHBQfPmzbNq/+KLL3Tx4kXt2rVLu3fvtmzLli3Txx9/bKnnZg0bNlTDhg21b9++Yr8D6X5n16DSsmVLffLJJ1q2bJkaNWqkadOmae7cudw8BAAolfnz5+vGjRtq1aqVPvroIx05ckTp6el699131aZNG23ZskVDhw7VpEmTVKdOHZ06dcpqy8rKKvGabm5umjp1qt59912r9vj4eHXt2lVNmzZVo0aNLFvv3r3l4+OjJUuWFDrff//7X508ebLQm38LXL9+3ab206dPl7j2e4Hdn0zbrVs37d27V9euXVN6enqRb00GAOB26tSpo7S0NHXo0EGjRo1So0aN1KlTJ61fv15xcXH617/+pdzcXE2YMEGBgYE22/Dhw0u1bv/+/VWnTh3L69OnT+vzzz9Xz549bcY6ODioR48eio+PL3QuDw+PW4YUSdq/f79N7ffrbRMmc0nuPjKY7OxseXt7Kysr6769iagoaWlpCg8PV+rkRwx5M23a8SyFT92s1NRUtWjRwt7lAChj165d07Fjx1S7du07uscD969bfY+U5O+33c+oAAAAFIWgAgDATRo2bGh5gu0ft6LuK8Hdc39+MAAAAKX0xRdfKC8vr9C+atWqlXM1IKgAAHCT+/Wm1HsVl34AAIBhEVQAAIBhEVQAAIBhEVQAAIBhcTMtAKBMZWRkKDMzs1zW8vf3V3BwcLmsBfsgqAAAykxGRoZCQ8N09eqVclnP3b2SDh5MJ6zcxwgqAIAyk5mZqatXr6h11GR5Bda6q2tlnzyubQlTlZmZWaKg8ttvv2nSpEn6/PPPdfr0afn6+qpp06aaNGmS2rVrp1q1aumnn36SJFWqVEn169dXTEyMevXqJUmaMmWKpk6dajNv/fr1dfDgQUlS+/bt9fXXX2vZsmV69tlnLWPmzp2ruXPn6vjx45a23NxczZ07V0uWLNGRI0csa7744ouKjIyUs7OzBgwYoEWLFtmsGRERobVr10qSVd3u7u566KGHNHz4cL344ovF/toYEUEFAFDmvAJrqUpwfXuXUaiePXsqNzdXixYtUp06dXT69GmtX79eZ8+etYyJjY3VoEGDlJ2drdmzZ6tPnz6qUaOG2rZtK+n3p9empKRYzevkZP0n1c3NTRMmTFDPnj3l7OxcaC25ubmKiIjQnj17NG3aNLVr105eXl7aunWrZs2apebNm6tZs2aSpM6dOysxMdFqf1dXV6vXBXVfuXJFK1eu1KBBg1SjRg116dKlVF8rIyCoAAAqjAsXLuibb77Rxo0b9dhjj0n6/QFvrVq1shpXuXJlBQQEKCAgQPPnz9fixYv16aefWoKKk5OTAgICbrlW3759tWbNGv3zn//UkCFDCh0zd+5cbdq0STt37lTz5s0t7XXq1FGvXr2Um5traXN1db3tmgV1S9LYsWP11ltv6auvvrqngwrv+gEAVBgFn9mzevVq5eTkFGsfJycnOTs7W4WG4vDy8tL48eMVGxury5cvFzpmyZIl6tixo1VIKeDs7CwPD48SrVkgPz9fH330kc6fPy8XF5dSzWEUBBUAQIXh5OSkpKQkLVq0SD4+PmrXrp1ef/11ff/994WOz83N1fTp05WVlaXHH3/c0r53716bDyx86aWXbPYfMmSI3Nzc9M477xQ6/5EjRxQaGlqs2j/77DObNd98802rMWPHjpWnp6dcXV31zDPPyNfXl3tUAAC4l/Ts2VNdu3bVN998o61bt+rLL7/UW2+9pX/9618aMGCApN//4E+YMEHXrl2Tp6enZsyYoa5du1rmqF+/vtasWWM1r5eXl81arq6uio2N1dChQ/Xyyy/b9JvN5mLX3aFDB8XFxVm1ValSxer1mDFjNGDAAJ08eVJjxozRkCFDFBISUuw1jIigAgCocNzc3NSpUyd16tRJEydO1IsvvqjJkydbgkrBH3xPT09Vq1ZNJpPJan8XF5diB4DIyEjNmjVLf//731WrVi2rvnr16lneKXQ7Hh4et13T399fISEhCgkJ0cqVK9W4cWM9/PDDatCgQbHWMCIu/QAAKrwGDRpY3UdS8Ac/ICDAJqSUlIODg6ZPn664uDirtyVL0nPPPaeUlBTt2rXLZr+8vLwi720pjqCgIPXp00cxMTGlnsMIOKMCAChz2SePG3KNs2fPqlevXoqKilKTJk1UuXJl7dy5U2+99Zb+8pe/FHue69ev69SpU1ZtJpNJ1apVK3R8165d1bp1ay1cuNBqzIgRI/T555/riSee0LRp0/TII49Yapo5c6bi4+Mtb0/OycmxWdPJyUn+/v5F1jl8+HA1atRIO3fu1MMPP1zs4zMSggoAoMz4+/vL3b2StiXYPhDtbnB3r3TLP9R/5OnpqdatW2vOnDn64YcflJeXp6CgIA0aNEivv/56sefZv3+/AgMDrdpcXV117dq1IveZOXOm5e3NN+/z1Vdfac6cOVq4cKFGjx6tSpUqKSwsTMOGDVOjRo0sY9euXWuz5s0PmStMgwYN9OSTT2rSpEn64osvin18RmIyl+ROHoPJzs6Wt7e3srKyCr2J6X6Wlpam8PBwpU5+RC1qedu7HBtpx7MUPnWzUlNT1aJFC3uXA6CMXbt2TceOHVPt2rXl5uZm1cdn/UC69fdISf5+c0YFAFCmgoODCQ8oM9xMCwAADIugAgAADIugAgAADIugAgAADIugAgAADIugAgAADIugAgAADIvnqAAAyhQPfENZIqgAAMpMRkaGwkLr68rVoh8lX5Yqubsp/eAhwsp9jKACACgzmZmZunL1mhb/rZnCAj3v6lrpJy8p8oPdyszMLFFQGTBggBYtWqTBgwdrwYIFVn3R0dF6//331b9/fyUlJVnav/vuOz3yyCPq3LmzPv/8c6t9jh8/rtq1a1te+/r6qnHjxvr73/+uP/3pT5b2KVOmaPXq1dq9e7el7dy5c4qNjdUnn3yikydPyt/fX507d9aUKVOsjqmg5unTp2vcuHGW9tWrV6tHjx66hz8N57YIKgCAMhcW6GnIzyErEBQUpOXLl2vOnDlyd3eX9Ptn0yxdurTQ0BMfH6+hQ4cqPj5ev/76q6pXr24zJiUlRQ0bNlRmZqbeeOMNdevWTYcPHy7yE5XPnTun//mf/5GLi4sWLFighg0b6vjx45owYYJatmyp7777TnXq1LGMd3Nz08yZMzV48GD5+vqW0VfC+LiZFgBQ4bRo0UJBQUH6+OOPLW0ff/yxgoOD1bx5c6uxly5dUnJysl5++WV17drV6kzLzfz8/BQQEKBGjRrp9ddfV3Z2trZt21ZkDePHj9evv/6qlJQUdenSRcHBwXr00Ue1bt06OTs7Kzo62mp8x44dFRAQoOnTp5f+wO9BBBUAQIUUFRWlxMREy+uEhAS98MILNuNWrFih0NBQ1a9fX5GRkUpISLjlpZarV6/qww8/lCS5uLgUOiY/P1/Lly9Xv379FBAQYNXn7u6uIUOGaN26dTp37pyl3dHRUW+++ab+8Y9/6Oeffy7Rsd7LCCoAgAopMjJSmzdv1k8//aSffvpJW7ZsUWRkpM24+Ph4S3vnzp2VlZWlr7/+2mZc27Zt5enpKQ8PD82aNUvh4eF64oknCl37t99+04ULFxQWFlZof1hYmMxms44ePWrV3qNHDzVr1kyTJ08u6eHeswgqAIAKqWrVqpZLOYmJieratav8/f2txhw6dEjbt29X3759JUlOTk7q06eP4uPjbeZLTk7Wrl279NFHHykkJERJSUlydna+ZQ2luQl25syZWrRokdLT00u8772Im2kBABVWVFSUXnnlFUnS/Pnzbfrj4+N1/fp1q5tnzWazXF1d9d5778nb+/9uGA4KClLdunVVt25dXb9+XT169NC+ffvk6upqM2/VqlXl4+NTZNhIT0+XyWRSSEiITd+jjz6qiIgIxcTEaMCAASU95HsOZ1QAABVW586dlZubq7y8PEVERFj1Xb9+XR9++KFmz56t3bt3W7Y9e/aoevXqWrZsWZHzPvPMM3JyctL7779faL+Dg4N69+6tpUuX6tSpU1Z9V69e1fvvv6+IiAhVqVKl0P1nzJihTz/9VN99910Jj/jewxkVAECZSz956Z5Yw9HR0XJWw9HR0arvs88+0/nz5zVw4ECrMyeS1LNnT8XHx+ull14qdF6TyaRhw4ZpypQpGjx4sCpVqmQz5s0339T69evVqVMnvfXWW2rUqJGOHTumCRMmKC8vr9AzPAUaN26sfv366d133y3pId9zCCoAgDLj7++vSu5uivxgd7msV8ndzea+kpLy8vIqtD0+Pl4dO3a0CSnS70Hlrbfe0vfff1/k/v3799f48eP13nvv6bXXXrPp9/Pz09atWxUbG6vBgwfr1KlTqlKlirp06aLFixff9iF2sbGxSk5OLsYR3ttM5nv4cXbZ2dny9vZWVlZWkd8o96u0tDSFh4crdfIjhnyoUtrxLIVP3azU1FS1aNHC3uUAKGPXrl3TsWPHVLt2bbm5uVn18Vk/kG79PVKSv9+cUQEAlKng4GDCA8oMN9MCAADDIqgAAADDIqgAAADDIqgAAADDsmtQmTJlikwmk9UWGhpqz5IAAICB2P1dPw0bNlRKSorltZOT3UsCAAAGYfdU4OTkZPMR10XJyclRTk6O5XV2dvbdKgsAABiA3YPKkSNHVL16dbm5ualNmzaaPn16ke+/nz59uqZOnVrOFQIASoIHvqEs2fUeldatWyspKUlr165VXFycjh07pj/96U+6ePFioeNjYmKUlZVl2U6cOFHOFQMAbiUjI0OhYaEKDw8vly00LFQZGRnFrq979+7q3LlzoX3ffPONTCaTvv/+e5v7Jwu2rVu3SpKSkpIsbQ4ODgoMDFSfPn1samnfvr1MJpNmzJhhs17Xrl1lMpk0ZcoUq/EjRowo8vUfmUwmrV69utC+jRs3ymQy6cKFC5a2GzduaM6cOWrcuLHc3Nzk6+urLl26aMuWLVb7FhzfH79WFy5ckMlk0saNG4usqazZ9YxKly5dLP9u0qSJWrdurQcffFArVqzQwIEDbca7uroW+nHZAABjyMzM1NUrV/Xoa4/KO+jufrxH1oksbXprkzIzM4t9VmXgwIHq2bOnfv75Z9WsWdOqLzExUQ8//LDlke4pKSlq2LCh1Rg/Pz/Lv728vHTo0CGZzWYdO3ZMQ4YMUa9evbRt2zarfYKCgpSUlKRx48ZZ2n755RetX79egYGBJTrmO2E2m/Xss88qJSVFb7/9tp544gllZ2dr/vz5at++vVauXKmnn37aMt7JyUkpKSnasGGDOnToUG51/pHdL/3czMfHR/Xq1dPRo0ftXQoA4A54B3nLv+6dfVjg3dCtWzdVrVpVSUlJmjBhgqX90qVLWrlypd5++21Lm5+f3y3voTSZTJb+wMBADRw4UMOGDVN2drbV59d069ZNK1as0JYtW9SuXTtJ0qJFi/Tkk0+W6GzQnVqxYoVWrVqlNWvWqHv37pb2Dz74QGfPntWLL76oTp06ycPDQ5Lk4eGh3r17a9y4cTbhqzwZ6jkqly5d0g8//FCuCRMAUHE4OTnp+eefV1JSkm7+TN6VK1fqxo0b6tu3b6nmPXPmjD755BM5OjrK0dHRqs/FxUX9+vVTYmKipS0pKUlRUVGlO4hSWrp0qerVq2cVUgqMGjVKZ8+e1VdffWXVPmXKFO3du1erVq0qrzJt2DWojB49Wl9//bWOHz+ub7/9Vj169JCjo2Opv1EAALidqKgo/fDDD/r6668tbYmJierZs6e8vf/vclXbtm3l6elptd0sKytLnp6e8vDwULVq1bRhwwZFR0dbzkj8cc0VK1bo8uXL2rRpk7KystStW7e7d5CFOHz4sMLCwgrtK2g/fPiwVXv16tU1fPhwjR8/XtevX7/rNRbGrpd+fv75Z/Xt21dnz55V1apV9cgjj2jr1q2qWrWqPcsCANzHQkND1bZtWyUkJKh9+/Y6evSovvnmG8XGxlqNS05OLvIPuyRVrlxZaWlpysvL05dffqklS5bojTfeKHRs06ZNVbduXa1atUobNmzQX//6V7s8N+zms0jFNXbsWC1cuFAJCQnq3bv3Xajq1uwaVJYvX27P5QEAFdTAgQM1dOhQzZ8/X4mJiXrooYf02GOPWY0JCgpSSEhIkXM4ODhY+sPCwvTDDz/o5Zdf1r///e9Cx0dFRWn+/Pk6cOCAtm/fXnYHU0z16tVTenp6oX0F7fXq1bPp8/HxUUxMjKZOnVruZ4Ekg92jAgBAeejdu7ccHBy0dOlSffjhh4qKipLJZLqjOceNG6fk5GSlpaUV2v/cc89p7969atSokRo0aHBHa5XGs88+qyNHjujTTz+16Zs9e7b8/PzUqVOnQvcdOnSoHBwcNG/evLtdpg1DvesHAIDy4OnpqT59+igmJkbZ2dkaMGCAzZizZ8/q1KlTVm0+Pj5yc3MrdM6goCD16NFDkyZN0meffWbT7+vrq5MnT8rZ2blEtf7222/avXu3VVtgYKCqVasmSTp27JhNf926dW3mefbZZ7Vy5Ur179/f5u3Ja9as0cqVKwu9v0aS3NzcNHXqVEVHR5eo9rJAUAEAlLmsE1mGX2PgwIGKj4/XU089perVq9v0d+zY0aZt2bJlevbZZ4uc89VXX1WbNm20fft2tWrVyqbfx8enxHUuXbpUS5cutWqbNm2a5e3VI0eOtNnnm2++sWkzmUxasWKF5s6dqzlz5mjIkCGWp8Jv3LjR8tbpovTv31+zZ8/WgQMHSnwMd8JkLs2dNQaRnZ0tb29vZWVlWb1nvSJIS0tTeHi4Uic/oha17u5DlUoj7XiWwqduVmpqqlq0aGHvcgCUsWvXrunYsWOqXbu21RmGgifTXr1ytVzqcK/kroPpB3mMvgEV9T0ilezvN2dUAABlJjg4WAfTD/JZPygzBBUAQJkKDg4mPKDM8K4fAABgWAQVAABgWAQVAABgWAQVAABgWAQVAABgWAQVAABgWAQVAABgWDxHBQBQpjIyMnjgG8oMZ1QAAGUmIyNDYaGhCg8PL5ctLDRUGRkZJapxwIABMplMeumll2z6oqOjZTKZrD6k8MSJE4qKilL16tXl4uKiBx98UMOHD9fZs2et9m3fvr1MJpOWL19u1T537lzVqlXL8jopKUkmk0kmk0kODg4KDAxUnz59Cj2O/fv3q3fv3qpatapcXV1Vr149TZo0SVeuXLEaV6tWLcucN28zZswo0dfGiDijAgAoM5mZmbpy9armtntEId5393PIjmZlacSWzcrMzCzxWZWgoCAtX75cc+bMkbu7u6TfP5tm6dKlVnP9+OOPatOmjerVq6dly5apdu3a2r9/v8aMGaMvv/xSW7duVZUqVSzj3dzcNGHCBPXs2fOWn5Ls5eWlQ4cOyWw269ixYxoyZIh69eqlbdu2WcZs3bpVHTt2VMeOHfX555+rWrVq2r59u0aNGqX169drw4YNcnFxsYyPjY3VoEGDrNapXLlyib4uRkRQAQCUuRBvbzXy87N3GUVq0aKFfvjhB3388cfq16+fJOnjjz9WcHCwateubRkXHR0tFxcX/b//9/8sgSY4OFjNmzfXQw89pPHjxysuLs4yvm/fvlqzZo3++c9/asiQIUWubzKZFBAQIEkKDAzUwIEDNWzYMGVnZ8vLy0tms1kDBw5UWFiYPv74Yzk4/H4B5MEHH1S9evXUvHlzzZkzR2PHjrXMWblyZcuc9xMu/QAAKqSoqCglJiZaXickJOiFF16wvD537pzWrVunIUOGWEJKgYCAAPXr10/Jyckym82Wdi8vL40fP16xsbG6fPlyseo4c+aMPvnkEzk6OsrR0VGStHv3bh04cEAjR460hJQCTZs2VceOHbVs2bISH/O9iKACAKiQIiMjtXnzZv3000/66aeftGXLFkVGRlr6jxw5IrPZrLCwsEL3DwsL0/nz5/Xbb79ZtQ8ZMkRubm565513ilw7KytLnp6e8vDwULVq1bRhwwZFR0fLw8NDknT48GHLGkWtXTCmwNixY+Xp6Wm1ffPNN7f/Qhgcl34AABVS1apV1bVrVyUlJclsNqtr167y9/e3GXfzGZPicHV1VWxsrIYOHaqXX3650DGVK1dWWlqa8vLy9OWXX2rJkiV644037mjtMWPGWN0ELEk1atQoUe1GxBkVAECFFRUVpaSkJC1atEhRUVFWfSEhITKZTEpPTy903/T0dPn6+qpq1ao2fZGRkXrwwQf197//vdB9HRwcFBISorCwMI0cOVL/8z//YxVq6tWrZ1mjqLULxhTw9/dXSEiI1fbHS1b3IoIKAKDC6ty5s3Jzc5WXl6eIiAirPj8/P3Xq1Envv/++rl69atV36tQpLVmyRH369JHJZLKZ18HBQdOnT1dcXJyOHz9+2zrGjRun5ORkpaWlSZKaNWum0NBQzZkzR/n5+VZj9+zZo5SUFPXt27eER3tvIqgAACosR0dHpaen68CBA5YbWW/23nvvKScnRxEREdq0aZNOnDihtWvXqlOnTqpRo0ahl2sKdO3aVa1bt9bChQtvW0dQUJB69OihSZMmSfr9XUHx8fE6cOCAevbsqe3btysjI0MrV65U9+7d1aZNG40YMcJqjosXL+rUqVNWW3Z2dsm+IAbEPSoAgDJ3NCvrnlnDy8uryL66detq586dmjx5snr37q1z584pICBATz/9tCZPnmz1DJXCzJw5U23bti1WHa+++qratGmj7du3q1WrVmrbtq22bt2qqVOnqkuXLrp48aKCg4PVv39/xcTEyNXV1Wr/SZMmWYJOgcGDB2vBggXFWt+oTOaS3iVkINnZ2fL29lZWVtYtv9HuR2lpaQoPD1fq5EfUotbdfahSaaQdz1L41M1KTU1VixYt7F0OgDJ27do1HTt2TLVr15abm5ulveDJtFf+cKnkbqnk7q70gwd5jL4BFfU9IpXs7zdnVAAAZSY4OFjpBw/yWT8oMwQVAECZCg4OJjygzHAzLQAAMCyCCgAAMCyCCgAAMCyCCgAAMCyCCgAAMCyCCgAAMCyCCgAAMCyeowIAKFMZGRk88A1lhjMqAIAy8/sj9MMUHh5eLltYaJgyMjKKVZvJZLrlNmXKFB0/flwmk0m7d++WJMvrgs3Pz09PPvmkdu3aZZm3ffv2ln43Nzc1aNBA77//vqU/KSmp0PX++Fj5U6dOaejQoapTp45cXV0VFBSk7t27a/369TbHMn36dDk6Ourtt9+26StYr3PnzlbtFy5ckMlk0saNG63aP/vsMz322GOqXLmyKlWqpJYtWyopKclqzB+/DjdvW7duLc6Xv9Q4owIAKDOZmZm6cvWKRjw3TTWr1b6ra/18+pjmLp2ozMzMYp1VOXnypOXfycnJmjRpkg4dOmRp8/T0LPJMUEpKiho2bKiff/5Zw4YNU5cuXXTw4EH5+PhIkgYNGqTY2FhduXJFH374oaKjo+Xr66u+fftK+v2DD29eS/o9OBU4fvy42rVrJx8fH7399ttq3Lix8vLytG7dOkVHR+vgwYNW+yYkJOi1115TQkKCxowZY1Ovk5OTUlJStGHDBnXo0KHIr8k//vEPjRgxQmPHjlVcXJxcXFz0n//8Ry+99JL27dunWbNmFfp1uJmfn1+R85cFggoAoMzVrFZbD9UMs3cZVgICAiz/9vb2lslksmqTVGRQ8fPzU0BAgAICAjRr1iy1a9dO27ZtU0REhCSpUqVKlrmmTJmipUuXas2aNZagUthaNxsyZIhMJpO2b98uDw8PS3vDhg0VFRVlNfbrr7/W1atXFRsbqw8//FDffvutzSc0e3h4qHfv3ho3bpy2bdtW6JonTpzQqFGjNGLECL355puW9lGjRsnFxUXDhg1Tr1691Lp1a5uvQ3ni0g8AACXg7u4uScrNzb3lmFv13+zcuXNau3atoqOjrUJKgYKzNgXi4+PVt29fOTs7q2/fvoqPjy903ilTpmjv3r1atWpVof2rVq1SXl6eRo8ebdM3ePBgeXp6atmyZcU6hruJoAIAQDFduHBB06ZNk6enp1q1amXTf+PGDS1evFjff/+9Hn/8cUt7VlaWPD09rbYuXbpIko4ePSqz2azQ0NDbrp+dna1Vq1YpMjJSkhQZGakVK1bo0qVLNmOrV6+u4cOHa/z48bp+/bpN/+HDh+Xt7a3AwECbPhcXF9WpU0eHDx+2am/btq3NcdxtXPoBAOA22rZtKwcHB12+fFl16tRRcnKyqlWrZul///339a9//Uu5ublydHTUq6++qpdfftnSX7lyZaWlpVnNWXBmxmw2F7uOZcuW6aGHHlLTpk0lSc2aNdODDz6o5ORkDRw40Gb82LFjtXDhQiUkJKh3794lOubCJCcnKyysfC/pEVQAALiN5ORkNWjQQH5+fjaXYiSpX79+Gj9+vNzd3RUYGCgHB+sLFg4ODgoJCSl07rp168pkMtncMFuY+Ph47d+/X05O//fnOz8/XwkJCYUGFR8fH8XExGjq1Knq1q2bVV+9evWUlZWlX3/9VdWrV7fqy83N1Q8//GBzI25QUFCRx3G3cOkHAIDbCAoK0kMPPVRoSJF+vzk3JCRENWrUsAkpt1OlShVFRERo/vz5unz5sk3/hQsXJEl79+7Vzp07tXHjRu3evduybdy4Ud99912RQWfo0KFycHDQvHnzrNp79uwpZ2dnzZ4922afBQsW6PLly5abge2JMyoAgDL38+lj98UaZcVsNuvUqVM27Q888IAcHBw0f/58tWvXTq1atVJsbKyaNGmi69ev66uvvlJcXJzS09MVHx+vVq1a6dFHH7WZp2XLloqPjy/0uSpubm6aOnWqoqOjrdqDg4P11ltvadSoUXJzc9Nf//pXOTs76z//+Y9ef/11jRo1yuodP5J09uxZm+Pw8fGxeSZMWSKoAADKjL+/vyq5V9LcpRPLZb1K7pXk7+9fLmvdiezs7EJvWj158qQCAgJUp04dpaWl6Y033tCoUaN08uRJVa1aVeHh4YqLi1Nubq4WL16ssWPHFjp/z549NXv2bKu3Gd+sf//+mj17tg4cOGDVPmLECNWpU0ezZs3SvHnzdOPGDTVs2FBxcXF64YUXbObp2LGjTduyZcv07LPPFufLUComc0nu4jGY7OxseXt7KysrS15eXvYup1ylpaUpPDxcqZMfUYta3vYux0ba8SyFT92s1NRUtWjRwt7lAChj165d07Fjx1S7dm2b/5rmEfqQbv09UpK/35xRAQCUqeDgYMIDyoxhbqadMWOGTCaTRowYYe9SAACAQRgiqOzYsUMLFy5UkyZN7F0KAAAwELsHlUuXLqlfv3765z//KV9fX3uXAwAADMTu96hER0era9eu6tixo/7+97/fcmxOTo5ycnIsr7Ozs+92eQBgV+V5Y2pJmM1mOTk5KScn566+NRX3rrJ6r45dg8ry5cuVlpamHTt2FGv89OnTNXXq1LtcFQAYQ0ZGhsJC6+vK1Wv2LsWGh4eHlixZouvXr6tRo0ZydXW1d0kwmCtXrkiSnJ2d72geuwWVEydOaPjw4frqq6+KncZjYmI0cuRIy+vs7GwFBQXdrRIBwK4yMzN15eo1Lf5bM4UF3v0PfyupMyd36LyHh86ePStfX1+ZTCZ7lwQDMJvNunLlis6cOSMfHx85Ojre0Xx2Cyqpqak6c+aM1TM2bty4oU2bNum9995TTk6OzcG5urqS2gFUOGGBnoZ8XlLq8U16f8dJvfLKK8rKyrJ3OTAYHx8fBQQE3PE8dgsqTzzxhPbu3WvV9sILLyg0NFRjx4694wQGALi7TDIrISFBQ4YMUe3ate1dDgzE2dm5zP6O2y2oVK5cWY0aNbJq8/DwkJ+fn007AMC4TCYTN9TirrH725MBAACKYve3J99s48aN9i4BAAAYCGdUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYZUqqNSpU0dnz561ab9w4YLq1Klzx0UBAABIpQwqx48f140bN2zac3Jy9Msvv9xxUQAAAJLkVJLBa9assfx73bp18vb2try+ceOG1q9fr1q1apVZcQAAoGIrUVB5+umnJUkmk0n9+/e36nN2dlatWrU0e/bsMisOAABUbCUKKvn5+ZKk2rVra8eOHfL3978rRQEAAEglDCoFjh07VtZ1AAAA2ChVUJGk9evXa/369Tpz5ozlTEuBhISEOy4MAACgVEFl6tSpio2N1cMPP6zAwECZTKayrgsAAKB0QWXBggVKSkrSX//617KuBwAAwKJUz1HJzc1V27Zty7oWAAAAK6UKKi+++KKWLl1a1rUAAABYKdWln2vXrumDDz5QSkqKmjRpImdnZ6v+d955p0yKAwAAFVupgsr333+vZs2aSZL27dtn1ceNtQAAoKyUKqhs2LChrOsAAACwUap7VAAAAMpDqc6odOjQ4ZaXeP773/+WuiAAAIACpQoqBfenFMjLy9Pu3bu1b98+mw8rBAAAKK1SBZU5c+YU2j5lyhRdunTpjgoCAAAoUKb3qERGRvI5PwAAoMyUaVD57rvv5ObmVpZTAgCACqxUl37+93//1+q12WzWyZMntXPnTk2cOLFMCgMAAChVUPH29rZ67eDgoPr16ys2NlZPPvlkmRQGAABQqqCSmJhY1nUAAADYuKN7VFJTU7V48WItXrxYu3btKvH+cXFxatKkiby8vOTl5aU2bdroyy+/vJOSAADAfaRUZ1TOnDmjZ599Vhs3bpSPj48k6cKFC+rQoYOWL1+uqlWrFmuemjVrasaMGapbt67MZrMWLVqkv/zlL9q1a5caNmxYmtIAAMB9pFRnVIYOHaqLFy9q//79OnfunM6dO6d9+/YpOztbw4YNK/Y83bt311NPPaW6deuqXr16euONN+Tp6amtW7eWpiwAAHCfKdUZlbVr1yolJUVhYWGWtgYNGmj+/Pmlvpn2xo0bWrlypS5fvqw2bdoUOiYnJ0c5OTmW19nZ2aVaCwAA3BtKdUYlPz9fzs7ONu3Ozs7Kz88v0Vx79+6Vp6enXF1d9dJLL+mTTz5RgwYNCh07ffp0eXt7W7agoKDSlA8AAO4RpQoqjz/+uIYPH65ff/3V0vbLL7/o1Vdf1RNPPFGiuerXr6/du3dr27Ztevnll9W/f38dOHCg0LExMTHKysqybCdOnChN+QAA4B5Rqks/7733nv785z+rVq1alrMaJ06cUKNGjbR48eISzeXi4qKQkBBJUnh4uHbs2KF58+Zp4cKFNmNdXV3l6upampIBAMA9qFRBJSgoSGlpaUpJSdHBgwclSWFhYerYseMdF5Sfn291HwoAAKi4ShRU/vvf/+qVV17R1q1b5eXlpU6dOqlTp06SpKysLDVs2FALFizQn/70p2LNFxMToy5duig4OFgXL17U0qVLtXHjRq1bt67kRwIAAO47JQoqc+fO1aBBg+Tl5WXT5+3trcGDB+udd94pdlA5c+aMnn/+eZ08eVLe3t5q0qSJ1q1bZwk/AACgYitRUNmzZ49mzpxZZP+TTz6pWbNmFXu++Pj4kiwPAAAqmBK96+f06dOFvi25gJOTk3777bc7LgoAAEAqYVCpUaOG9u3bV2T/999/r8DAwDsuCgAAQCphUHnqqac0ceJEXbt2zabv6tWrmjx5srp161ZmxQEAgIqtRPeoTJgwQR9//LHq1aunV155RfXr15ckHTx4UPPnz9eNGzc0fvz4u1IoAACoeEoUVKpVq6Zvv/1WL7/8smJiYmQ2myVJJpNJERERmj9/vqpVq3ZXCgUAABVPiR/49uCDD+qLL77Q+fPndfToUZnNZtWtW1e+vr53oz4AAFCBlerJtJLk6+urli1blmUtAAAAVkr1oYQAAADlgaACAAAMi6ACAAAMi6ACAAAMi6ACAAAMi6ACAAAMi6ACAAAMi6ACAAAMi6ACAAAMi6ACAAAMi6ACAAAMi6ACAAAMi6ACAAAMi6ACAAAMi6ACAAAMi6ACAAAMi6ACAAAMi6ACAAAMi6ACAAAMi6ACAAAMi6ACAAAMi6ACAAAMi6ACAAAMi6ACAAAMi6ACAAAMi6ACAAAMi6ACAAAMi6ACAAAMi6ACAAAMi6ACAAAMi6ACAAAMi6ACAAAMi6ACAAAMi6ACAAAMi6ACAAAMi6ACAAAMi6ACAAAMi6ACAAAMi6ACAAAMi6ACAAAMi6ACAAAMy65BZfr06WrZsqUqV66sBx54QE8//bQOHTpkz5IAAICB2DWofP3114qOjtbWrVv11VdfKS8vT08++aQuX75sz7IAAIBBONlz8bVr11q9TkpK0gMPPKDU1FQ9+uijNuNzcnKUk5NjeZ2dnX3XawQAAPZjqHtUsrKyJElVqlQptH/69Ony9va2bEFBQeVZHgAAKGeGCSr5+fkaMWKE2rVrp0aNGhU6JiYmRllZWZbtxIkT5VwlAAAoT3a99HOz6Oho7du3T5s3by5yjKurq1xdXcuxKgAAYE+GCCqvvPKKPvvsM23atEk1a9a0dzkAAMAg7BpUzGazhg4dqk8++UQbN25U7dq17VkOAAAwGLsGlejoaC1dulT/+c9/VLlyZZ06dUqS5O3tLXd3d3uWBgAADMCuN9PGxcUpKytL7du3V2BgoGVLTk62Z1kAAMAg7H7pBwAAoCiGeXsyAADAHxFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYRFUAACAYdk1qGzatEndu3dX9erVZTKZtHr1anuWAwAADMauQeXy5ctq2rSp5s+fb88yAACAQTnZc/EuXbqoS5cu9iwBAAAYmF2DSknl5OQoJyfH8jo7O/uurpeRkaHMzMy7ukZppaen27uEYjFynf7+/goODrZ3GbAzfs7vnJHrzMnJkaurq73LuCWj12jv35X3VFCZPn26pk6dWi5rZWRkKDQ0TFevXimX9UrHpJNZ1yR527sQGzm5vwfKyMhIO1dSNPdK7jqYfpCwUoHxc35n7oWfc5kkme1dxK05SMq3dxG3UMm9ktIPptvtd+U9FVRiYmI0cuRIy+vs7GwFBQXdlbUyMzN19eoVtY6aLK/AWndljTvx27GD2r10pi5cuW7v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TZ48+e4fWBGefvpp9e7dW507d9Zjjz2m/v37Fzk2NzdX06dPV1ZWlh5//HFL+969e22O96WXXiqP8oEKi0s/QAXVoUMHxcXFWbVVqVJFktS3b1+9+uqrWrFihaKiopScnCwHBwf16dPHanzlypWVlpZm1ebu7l7oejNnztTjjz+u0aNHl+FRlMzEiRP14YcfasKECYX2jx07VhMmTNC1a9fk6empGTNmqGvXrpb++vXra82aNVb7eHl53dWagYqOoAJUUB4eHgoJCSm0z8vLS88884wSExMVFRWlxMRE9e7dW56enlbjHBwcipzjjx599FFFREQoJiZGAwYMuNPyS8XJycnqf/9ozJgxGjBggDw9PVWtWjWr+1ckycXFpdjHC6BsEFQAFGrgwIFq3769PvvsM3377bd6++2373jOGTNmqFmzZqpfv34ZVFj2/P39CSKAwRBUgAoqJydHp06dsmpzcnKSv7+/pN/PgISEhOj5559XaGio5Z0vNzObzTZzSNIDDzwgBwfbW+AaN26sfv366d133y2joyhf169ftzlek8mkatWq2aki4P5HUAEqqLVr1yowMNCqrX79+jp48KCk3/8AR0VF6fXXX1dMTEyhc2RnZ9vMIUknT54s8m28sbGxSk5OvsPq7WP//v02x+vq6qpr167ZqSLg/mcym81mexcBAABQGN6eDAAADIugAsDQvvnmG5tnl9y8Abi/cekHgKFdvXpVv/zyS5H9vEsHuL8RVAAAgGFx6QcAABgWQQUAABgWQQUAABgWQQUAABgWQQUAABgWQQUAABgWQQUAABjW/wcUF2OzFdmbrAAAAABJRU5ErkJggg==)

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
[2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m5.2/5.2 MB[0m [31m86.5 MB/s[0m  [33m0:00:00[0m
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

    <pre class="output-block">/tmp/ipykernel_2239/1940921173.py:11: SettingWithCopyWarning:
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
    &nbsp;&nbsp;storms_no_flood["EVENT_DURATION_HOURS"] = storms_no_flood["EVENT_DURATION"].dt.total_seconds() / 3600
    </pre>

    ![A strip plot showing the duration of different events in hours in hours on the x-axis, ranging from 0 to 35. The y-axis shows the event type. Event types are 'Winter Weather', 'Heavy Snow', 'Thunderstorm Wind', 'Extreme Cold/Wind Chill', 'Hail', 'Heavy Rain', ''Tornado', 'Heat', 'Dense Fog', 'Cold/Wind Chill', and 'Winter Storm'. Winter Weather and Heavy Snow span the range of durations, while Winter Storms last between 10 and 26 hours. Thunderstorm Wind, Hail, and Tornados have short durations, less than 1 hour. There are few Extreme Cold/Wind Chill events, mostly around 13 hours long. Heat, Dense Fog, and Cold/Wind Chill events all last between 4 and 13 hours.](data:image/png;base64,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aKWpFgBgZWWFiIgIzJgxA7/99hsuXbqE8PBwuQveEhIS8OjRI7z44oty+7Zu3RouLi5Yv369MIoMAM7OzmjWrBk+//zzZ85HfpY333wTIpEI48ePx5UrV/DLL79g5cqVle5T1b4i/ZD4OGLfpB648nEI9k3qwQS5jlA3ChXSjs8vEdVfBk+SDx06BCcnJ7mlIoFbsmQJ/vrrL+ECOCcnJ3z++eeYO3cuEhMTATy5UMvY2Bje3t6wt7dHRkaG2rYWLVqEefPmITIyEl5eXggJCcHPP/+MVq1aPdcxaFNv586dcfbsWbi5uWH8+PHw8vLCq6++isuXL2PNmjUAAAsLCxw+fBj3799Hp06d8Prrr6NPnz7YsGGD2no/+eQT9OzZEwMHDkTfvn3x4osvIiAgQFi/b98+9O/fHw0aKM+0CQ4ORl5eHoKCguTKAwMDkZeX99xJspWVFX766SdcvHgR7du3x4cffojly5c/c7+q9BURaW/z6ACE+DjC6P+Hjo1EQL92jtg0KqDyHYmI6jCRTNMro6hW8/Pzw9y5czF06FBDh1Kr5ebmwtbWFjk5ObCxsTF0OERERFQFmrx/G3wkmfSnuLgYQ4YMQb9+/QwdChEREVGNxpFkIi1wJJmIiKj24UgyEREREdFzYJJMRERERKSASTIRERERkQImyURERERECpgkExEREREpYJJMRERERKSASTIRERERkQImyURERERECpgkExEREREpYJJMRERERKSASTIRERERkQImyURERERECpgkExEREREpYJJMRERERKSASTIRERERkQImyURERERECpgkExEREREpaGDoAIjoX66zf1YqS1/2igEiISIiqt80Gkn29vbG/fv3hccTJ07E3bt3hcfZ2dmwsLDQXXRE9YiqBLmyciIiIqo+GiXJycnJKC0tFR5//fXXyM3NFR7LZDIUFhbqLjqiahIUFISpU6cKj11dXbFmzRqDxfMsr30Wb+gQiIiI6pXnmm4hk8mUykQi0fNUSVSp8PBwPHz4EHv37pUrl0qlCA4OxoMHD2BnZ/fMen788UeYmJhUT5DV4NzNh4YOgYiIqF7hnGSqlxo1amToEIiIiKgG02i6hUgkUhop5sgx1TT37t3DiBEj0Lx5c1hYWMDX1xfffPON3DaK0y2epaioCLm5uXKLvh2+nKX3NomIiOorjUaSZTIZ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YmqCv7MdLMTG8He2w5ZRAdUy8qpNwlXTk7SaHt/z4pxkIqInNJ6TfPjwYdja2la6zauvvqp1QGQYs2bNQteuXTF58mSMGzcOlpaWuHLlCo4ePYoNGzbAxcUFYrEY69evx4QJE3Dp0iUsWrRIqR5XV1d0794dERERKCsrU3kujBs3DgMGDEBZWRnCwsI0jtXCwgLjx4/H/PnzMWjQILi5uaGkpATr16/HwIEDER8frzQdozZoYCRCabnyPP4GRvLDvhOD3TDh6wQ8PeVfJALCu7li8+9pSuWqRoglPo56mUPr7mClcn5rZQmXNvvoU02P73mpO794ESQR1TcajySHhYVh0KBBapfXXnutOuKkaubn54fY2FhcvXoVPXv2RPv27fHRRx+hWbNmAAB7e3tER0dj9+7d8Pb2xrJly7By5UqVdY0cORKJiYl47bXXYG5urrS+b9++cHJygkQiEerX1OTJk5GUlITdu3fD398fq1evxvLly9GuXTvs2LEDkZGRWtVrSON7qv759rd7yZerGwme1c9TbyPEVaXN1I6afqeKmh7f89LnNw1ERDWZSKbBLSiMjIyQlZVVZ3+UgfQjPz8fzZs3R1RUFAYPHmzocLSSm5sLW1tb5OTk6HR+8vKDydh2Mh2PistgITZGeHdXzAzxfPaONdjhy1ka33VCm330qabHR0REqmny/q1RkmxsbIzMzEwmyaSV8vJy3L17F6tWrcK3336LtLQ0NGhQrXchrDbVlSQTERFR9dHk/VujDIX3PabnkZGRgVatWqFFixaIjo6utQkyERER1X0aZSlhYWEq55gSVYWrqys/aBEREVGtoFGSXPEjEEREREREdZlGSbKRkRFEipd1KxCJRCgtLX2uoIiIiIiIDEmjJPnHH39UmySfPHkS69atU/uLZUREREREtYVGSfKgQYOUylJSUjB79mz89NNPGDlyJD7++GNdxUZEREREZBBa/yz17du3MX78ePj6+qK0tBTnz5/Htm3b0LJlS13GR0RERESkdxonyTk5OZg1axbc3Nxw+fJlHDt2DD/99BPatWtXHfEREREREemdRtMtVqxYgeXLl8PR0RHffPMNQkNDqysuIiIiIiKD0fhnqc3NzdG3b18YGxur3e7HH3/USXBENRV/cY+IiKj2qbZf3BszZswzbwFHRERERFTbaZQkR0dHV1MYRERE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)

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

    <pre class="output-block">/tmp/ipykernel_2239/42002734.py:11: SettingWithCopyWarning:
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
    &nbsp;&nbsp;storms_flood_only["EVENT_DURATION_HOURS"] = storms_flood_only["EVENT_DURATION"].dt.total_seconds() / 3600
    </pre>

    ![A strip plot showing the duration of Flood and Flash flood events in hours on the x-axis, ranging from 0 to 700. The y-axis shows the event type. Flash Floods all last under 24 hours while Floods can last up to 700 hours.](data:image/png;base64,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lJSkxx9/XN9//73bPnYTJ050KePcuXOL3e7111/X2bNn9X//939q3bq1fvOb3+j555/XP/7xDx09elSS9NRTT2nixIkaNGiQmjdvrlmzZunqq6/Ws88+69xHfn6+Xn31VbVq1Uq33HKLJkyYUGr5ZsyYobi4OOejUaNGpW5fERhBCgCAfwS8z1v37t01b94859/Vq1cvcduClqgtW7bo+PHjys/Pl3QxtCUnJ+u+++7Tbbfdpq+//lo333yzbr31VnXp0sVlH23btnX+f/369SVJmZmZatGiRYnHnTBhgksLX+HWvAI7d+5Uu3btXOrQtWtX5efna9euXYqKitKhQ4fUtWtXl+d17dpVW7Zsce6jbdu2ioyMdK7v3LlziWWTpMmTJ+uBBx5w/p2TkxPQAMcIUgAA/Cfg4a169epq2rSp2+0KLkmmpKTotddeU506dXTw4EGlpKTo/PnzkqTevXvr+++/1wcffKDVq1erR48eGjNmjJ566innfqpVq+b8f8d/5q0oCIElqV27tkdlDJSIiAhFREQEtAwOSVHhoWpWr4bGdLuKEaQAAPhJwC+beurbb79VVlaWZs6cqRtuuEEtWrRwGaxQoE6dOkpNTdWCBQv07LPP6pVXXqmwMrZs2VJbtmzRL7/84ly2fv16hYSEqHnz5oqNjVWDBg20fv16l+etX79eycnJzn188803Onv2rHP9559/XjEVKIe2jeK1Y1ovvTumK8ENAAA/sia8NW7cWOHh4frLX/6iffv2admyZXriiSdctnn00Uf17rvvau/evdq+fbvee+89tWzZssLKOGTIEEVGRio1NVXbtm3TmjVr9L//+7+66667VK9ePUkXL8HOmjVLb775pnbt2qVJkyYpIyND48aNkyT9/ve/l8Ph0MiRI7Vjxw598MEHLi2HwYrLpAAAVAxrwludOnWUnp6uRYsWKTk5WTNnziwSasLDwzV58mS1bdtWv/71rxUaGqqFCxdWWBmjo6O1atUqHTt2TNdee61uv/129ejRQ88//7xzm/vvv18PPPCAHnzwQbVp00YrV67UsmXL1KxZM0lSTEyMli9frq1bt6p9+/Z65JFHNGvWrAqrQ1m9sGavWk5ZWeokvQAAoPwcxhjPblwJa+Tk5CguLk7Z2dmKjY0t9/4SJ73v1fYOh0qcpBcAABTP0/O3NS1vCJywEIf7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CdWrV08XLlxQenp6sfuIjIwscpzC+1u6dKkcDkepZSl4JCYmuq1Pt27dnNtHRETo8ssvV79+/bR48WKX7Q4cOCCHw6GMjIxi9zF+/Hjn34mJic59RkdHq02bNvrb3/5W7PHfeOMNhYaGasyYMcWWqbhHt27dnMd59tlnXfa3YcMG9enTRzVr1lRkZKTatGmjOXPmKC8vz2W7gtf7+++/d1l+6623avjw4aW/aP8xfPhw3XrrrUWWr127Vg6HQydOnHAuy8vL0zPPPKM2bdooMjJSNWvWVO/evbV+/XqX5z722GO6+uqri+yz8OtfcIyCR506ddSnTx9t3brV5Xk///yz7rvvPjVu3FgRERFKSEhQSkpKkeMCwYbwBsCnevXqpcOHD7s83nnnHQ0dOlRpaWlFtjfGKD09XcOGDVO1atUkSbGxsUX2UThIREZGatasWTp+/Hix5Xjuuedcni9JaWlpzr//9a9/eVSfkSNH6vDhw/ruu+/0zjvvKDk5WYMGDdK9997rzcviYtq0aTp8+LC2bdumoUOHauTIkVqxYkWR7V599VX9v//3//TGG2/o7NmzkqTFixc76/Dll19Kkj788EPnssLBssCSJUt04403qmHDhlqzZo2+/fZbjRs3Tn/60580aNAgFb5TosPh0KOPPlrmOnrKGKNBgwZp2rRpGjdunHbu3Km1a9eqUaNG6tatm5YuXVrmfe/atUuHDx/WqlWrdO7cOfXt21fnz593rr/tttu0efNmzZ8/X7t379ayZcvUrVs3ZWVl+aBmgP+EBboAACqXghaMwu6++24999xzWrdunX71q185l3/yySfat2+f7r77bucyh8NR7D4u1bNnT+3du1czZszQk08+WWR9XFyc4uLiXJbFx8e73W9h0dHRzuc0bNhQ119/vVq0aKERI0bozjvvVM+ePb3anyTVqFHDuc+JEyfqySef1OrVq9W7d2/nNvv379eGDRv0zjvvaM2aNVq8eLF+//vf67LLLnNuUxDoatWqVWq9fvnlF40cOVL9+/fXK6+84lx+zz33qF69eurfv7/eeustDRw40Llu7NixmjNnjiZMmKDWrVt7XUdPvfXWW3r77be1bNky9evXz7n8lVdeUVZWlu655x7ddNNNql69utf7rlu3rvM9Hz9+vPr3769vv/1Wbdu21YkTJ/TZZ59p7dq1uvHG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)

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

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

<pre class="output-block">SYSTEM_WGETRC = c:/progra~1/wget/etc/wgetrc
syswgetrc = C:\bin\programs\gnuwin32/etc/wgetrc
--2025-08-27 15:57:36--  https://raw.githubusercontent.com/harvardinformatics/python-intensive/refs/heads/main/data/indiana_storms_full.csv
Resolving raw.githubusercontent.com... 185.199.110.133, 185.199.111.133, 185.199.108.133, ...
Connecting to raw.githubusercontent.com|185.199.110.133|:443... connected.
OpenSSL: error:140770FC:SSL routines:SSL23_GET_SERVER_HELLO:unknown protocol
Unable to establish SSL connection.
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

<pre class="output-block">Requirement already satisfied: lxml in c:\bin\miniforge3\lib\site-packages (6.0.0)
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

    <pre class="output-block">C:\Users\Gregg\AppData\Local\Temp\ipykernel_44052\1940921173.py:11: SettingWithCopyWarning:
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
    &nbsp;&nbsp;storms_no_flood["EVENT_DURATION_HOURS"] = storms_no_flood["EVENT_DURATION"].dt.total_seconds() / 3600
    </pre>

    ![A strip plot showing the duration of different events in hours in hours on the x-axis, ranging from 0 to 35. The y-axis shows the event type. Event types are 'Winter Weather', 'Heavy Snow', 'Thunderstorm Wind', 'Extreme Cold/Wind Chill', 'Hail', 'Heavy Rain', ''Tornado', 'Heat', 'Dense Fog', 'Cold/Wind Chill', and 'Winter Storm'. Winter Weather and Heavy Snow span the range of durations, while Winter Storms last between 10 and 26 hours. Thunderstorm Wind, Hail, and Tornados have short durations, less than 1 hour. There are few Extreme Cold/Wind Chill events, mostly around 13 hours long. Heat, Dense Fog, and Cold/Wind Chill events all last between 4 and 13 hours.](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAskAAAGwCAYAAABb8Ph5AAAAOnRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjEwLjUsIGh0dHBzOi8vbWF0cGxvdGxpYi5vcmcvWftoOwAAAAlwSFlzAAAPYQAAD2EBqD+naQAAehJJREFUeJzt3XlYVOXfBvB7QId1ABcEVBARWQXcF0xh1Bo0DdPSzAVyKUNTf+ZambuoqbnlUhaYadnmkuWWMSS4JSmWIiKKaIHkxqYswrx/+HJqNmSGgWG5P9c1l8xztu85HJx7nnnOGZFCoVCAiIiIiIgEJsYugIiIiIiopmFIJiIiIiJSwZBMRERERKSCIZmIiIiISAVDMhERERGRCoZkIiIiIiIVDMlERERERCoaGLsAotqotLQUf//9NyQSCUQikbHLISIiogpQKBTIzc1F8+bNYWJSfl8xQzKRHv7++284OzsbuwwiIiLSw82bN9GyZcty52FIJtKDRCIB8OSPzMbGxsjVEBERUUXk5OTA2dlZeB0vD0MykR7KhljY2NgwJBMREdUyFRkqyQv3iIiIiIhUMCQTEREREalgSCYiIiIiUsGQTERERESkgiGZiIiIiEgFQzIRERERkQqGZCIiIiIiFQzJREREREQq+GUiRFTjHL6YiU0xV3Hldh48HKwRIXWHzNex3GVWHLyM6BNpeFRcAouGpggPdMXs/l5Vsi19TNyRgMOXMqFQACIRIPNxxJbRnQy+HaD69qk6Vdc+Veex02db1VlfdZ2z+v7t6qMu/m1Q1REpFAqFsYsgzeRyOaRSKe7fvw87Oztjl1Mjubq6Ytq0aZg2bVq1bjcnJwe2trbIzs7mN+4Z2OGLmXhjR4JSmwjAltGdtL6YrTh4GZtjU9Xa3wxqU+6LraZtAcDWcrZVtpwuL7QTdyTg0MVMtfYQ3/JDhz4hpbr2Sd9l9AlEGs8JEbBlVPn7pCt9zj1Dbgso//dUXccB0P+c1ZW+f7v6qM7jRzWXLq/fHG5RDbZs2QKJRILHjx8LbXl5eWjYsCGCg4OV5pXL5RCJREhNTUVgYCAyMjJga2tb4W2Fh4dj8ODBBqpc2eXLlyESiXDq1Cml9u7du8Pc3BwFBQVCW0FBAczNzfHpp58aZNvR0dF8o1BPRP6UpNam0NJe5pPj13RqL/Pe3j90agf+faFNvJWNR8UlSLyV/STMaggUwjKXNE87oqUd+DeklHVjKBTAoYuZmKghWFWkdoPvk6Zlvih/mbJA9Ki4BADwqLgEm2NTseLg5XL3aVPMVbU2hQLYJFcPV6o1hm6Mg/e8QwjdGFdubYB+556+5u39U6d2QP/joA9tx+ppx1BXn8Zd19wer7m9Mqrz+FHdwJBcDaRSKfLy8nD27Fmh7fjx43B0dMTp06eVwmVMTAxcXFzQpk0biMViODo6Vuj7xQ2tqKhIrc3LywuOjo6Qy+VCW25uLn7//XfY29srheeTJ0+isLAQffr0qY5yDUrTvlP1Sbv7UKd2AHhcqvkDMW3tZf7J1fy71tYO6BektH1eV155mnrxymsvU137pE/giD6RprF9+0nN7WUu/p2juf2vbK3L6BPi0+9pPse0tVdGVm6hTu0AkJSRq7H9cobm41MZ2k5NQ3/0XFRSqrn9seb2yrhyO09je8ptzce1ttD1zSBVHENyNfD09ISTk5NSuJTL5QgNDUXr1q2VwmXZEIuyn0UiER48eADg397Uw4cPw9vbG9bW1ggJCUFGRgYAYMGCBdi+fTv27dsHkUgEkUgkbPPmzZsYNmwY7Ozs0LhxY4SGhiItLU3YblkP9NKlS9G8eXN4enpq3BepVKq0H3FxcfDw8MCgQYPU9q9Vq1Zo3bo1AGDfvn3o2LEjzM3N4ebmhoULFyr1rK9ZswZ+fn6wsrKCs7MzIiIikJeXJ6zrtddeQ3Z2trBfCxYsEJZ9+PAhxo4dC4lEAhcXF3z88cdKNRtq34kA4IaWsK6tvTbQ542JPoGjrAdZ1cMize1lSrS8m9DWDugX4mvr2MPaWnd1c7Ax09jeTKK5vTbQ580gVRxDcjWRSqWIiYkRnsfExCA4OBhBQUFC+6NHj3D69GkhJGvy8OFDrFq1Cjt27MCvv/6K9PR0zJgxAwAwY8YMDBs2TAjOGRkZCAwMRHFxMWQyGSQSCY4fP474+HghYP+31/TYsWNITk7G0aNHceDAAa37ERcXJwRcTftR1l62H8ePH8eYMWMwdepUXLp0CVu3bkV0dDSWLl0qzG9iYoL169fj4sWL2L59O3755RfMmjULABAYGIi1a9fCxsZG2K+yfQaA1atXo3Pnzjh37hwiIiLw5ptvIjk5GQAMtu+FhYXIyclRelD9VF09bDWdIQPH0z4r0+eY6xPim1qLdWqvbtXZ61pd7CWaj20zLe2kjENIqhZDcjWRSqWIj4/H48ePkZubi3PnziEoKAi9e/cWemDLhiiUF5KLi4uxZcsWdO7cGR07dsTkyZNx7NgxAIC1tTUsLCxgZmYGR0dHODo6QiwWY/fu3SgtLcW2bdvg5+cHb29vREVFIT09Xan318rKCtu2bYOvry98fX217kd+fj5+++03AE96ecv2o2zoyKNHj3DmzBlhPxYuXIg5c+YgLCwMbm5uePbZZ7F48WJs3bpVWO+0adMglUrh6uqKPn36YMmSJfj6668BAGKxGLa2thCJRMJ+WVtbC8sOGDAAERERcHd3x+zZs9G0aVMhsBtq3yMjI2Frays8nJ2dtf6OKoMfm9V82gJd9Q+KqqH0GB5WFW8wPBysNba3dZBoXcZKrPmGT5ZmDQ1SU23i2sRSc3tTK4Nu56WOmv8vHaqlvTJu5+g+xKWmq6tDSGoKhuRqEhwcLITL48ePw8PDA/b29ggKChLCpVwuh5ubG1xcXLSux9LSEm3atBGeOzk5ISsrq9xtJyYm4urVq5BIJLC2toa1tTUaN26MgoICpKb++27Tz88PYnH5797d3d3RsmVLyOVy5OTkCGHfyckJLi4uOHnypFrYT0xMxKJFi4RtW1tbY8KECcjIyMDDh08+zv3555/Rt29ftGjRAhKJBKNHj8bdu3eF6eXx9/cXfi4L0mXHxFD7PnfuXGRnZwuPmzdvPrUuXfFjs9qhlZbwoK29rtIaOHIKNLZXRgMTzcFbWzsAREjd1fK6SARMCm6jeQFU7z7VdHMHeGtsf8fAd5w4kXpHc/u1uwbdDqDfG6eari7uU03C+yRXk7JwGRMTg/v37yMoKAgA0Lx5czg7O+PEiROIiYl56oVuDRsq92iIRCI87S5+eXl56NSpE3bu3Kk2zd7eXvjZyqpiPQTBwcGIiYmBv78/2rZti2bNmgGAMORCoVDA3d1d6G3Ny8vDwoULMWTIELV1mZubIy0tDQMHDsSbb76JpUuXonHjxoiLi8O4ceNQVFQES8vyw4emY1JaWmrQfTczM4OZWdWOWyvvYzPenqh8DUxEGi/SKy9E6WvuAG9M3JGg1PspAvCOllBRV3k4WCPxlvqFc1Xx4mwiEkFTf7NJOb9fma8jtozqhE3yVKTczkVbBwkmBbfBc+X8LVXnPtV0Ml9HbB2t2/HTR3X2hEZI3THxiwSlC2mf9sappquL+1STMCRXo7KL3u7fv4+ZM2cK7b1798bBgwdx5swZvPnmm5XahlgsRkmJ8kUwHTt2xO7du9GsWTOD3NNXKpViypQp8PHxUbqFXe/evfHJJ59AoVAoDRnp2LEjkpOT4e7urnF9CQkJKC0txerVq2Fi8uTDjbKhFuXtV0UYet+rEj8209+EXm4a77X6em83g29L9v/3ia3q8FDTVeeLs7eTRGN49XYq/29a5uuo0xtMBg5luh4/fVTnGxN93jjVdHVxn2oSDreoRmUXvZ0/f17oSQae9MBu3boVRUVF5Y5HrghXV1dcuHABycnJuHPnDoqLizFy5Eg0bdoUoaGhOH78OK5fvw65XI4pU6bg1q1beu1Hfn4+PvvsM7X9OH36tNJ4ZAB4//338fnnn2PhwoW4ePEikpKS8NVXX+G9994D8KSXvbi4GBs2bMC1a9ewY8cObNmyRW2/8vLycOzYMdy5c6dCwzAAGHzfqxI/NntC24Vf5V0QNru/F94MagNLsSkAwFJsiojgNpgVUjXf2iXzdcS+ST1xaVEI9k3q+dQXJLGp5v9qxQ1qxn/B2jpkTcvpiC97cQ5wtoOl2BQBznbYOqpTlbw46zN0Qh/VuU/6sDHX3K9lq6W9Nqiu320ZXf92a4O6uE81Rc34H7qekEqlePToEdzd3eHg4CC0BwUFITc3V7hVXGVMmDABnp6e6Ny5M+zt7REfHw9LS0v8+uuvcHFxwZAhQ+Dt7Y1x48ahoKBAr97V1q1bo1WrVsjNzVUKyS4uLmjevDmKioqUephlMhkOHDiAI0eOoEuXLujevTs+/PBDtGrVCgAQEBCANWvWYMWKFWjXrh127tyJyMhIpW0GBgZi4sSJGD58OOzt7bFy5coK1Wrofa9K1f1iUVMtHtxOY/sSLe1lZvf3wqVFIUhb/jwuLQqpUEB+M0jzsY0w8DEf90xrje3jtbQDQAdnO43tHV00t5cJ0fIC2b+d9hfON3pr3t83tByfMrq+OOtTW9l2qiu8VlfgaK1lDLtbORfGffBygE7ttUFNf2NC9Ru/lppID1X1tdSHL2byYzNU73FYcfAytp9Mw8OiEliKn3xNclX0QOuznRc/ise5mw+E5x1d7PB9RM+nbmvijgQcuZSJUsWTXmKZryM2jyr/q4Sr6zjoU1tdJf0gBtf/cy9qt6ZW+GVGcLnL8P8IosrR5fWbIZlID1UVkomIiKjq6PL6zeEWREREREQqGJKJiIiIiFQwJBMRERERqWBIJiIiIiJSwZBMRERERKSCIZmIiIiISAVDMhERERGRCoZkIiIiIiIVDMlERERERCoYkomIiIiIVDAkExERERGpYEgmIiIiIlLBkExEREREpIIhmYiIiIhIBUMyEREREZEKhmQiIiIiIhUMyUREREREKhiSiYiIiIhUMCQTEREREaloYOwCiIio/jh8MRObYq7iyu08eDhYI0LqDpmvY5UtR2QM+pyvKw5eRvSJNDwqLoFFQ1OEB7pidn+vaqqYNBEpFAqFsYsgqm1ycnJga2uL7Oxs2NjYGLscqgX0edGs6DKq8znZWiD2yj86vdhO3JGAw5cyoVAAIhEg83HEltGdKrXPmup8Y0eCWvvW0Z3KPRb6LlcX8c1C9dP1mOtzvq44eBmbY1PV2t8MasOgbGC6vH4zJBPpgSGZdKHpRVMEYEs5L5oVXUbbC7Kq8l5sJ+5IwKGLmWrtIb7lB2Vdw4P3vIN4VFyq1m7R0ARJi/trXa7r0p+RlVuo1t5MYoYz7/bTulxdo/GcEAFbRun/ZqEq37zVBfoc8y5Lj+Kf3CK1dnuJGL+9+6zGZdzm/Aj1v4wnY2KvLX9e17Jrvao8x3R5/eaY5DogPDwcgwcPVmuXy+UQiUR48OBBtdekq08++QQBAQGwtraGnZ0dOnTogMjISGOXRWQQkT8lqbUptLTrusymmKsVqmH7yTSt0w5fUg/IAHBESzvwb3hIvJWNR8UlSLyVjYlfJOCwhrBdRlNALq+9jKaAXF57XaXpd61QAJvk6j2Q/3X4YiZCN8bBe94hhG6ME35H+vwO9VmmNtPnmGsKyOW1A9AYkMtrr8s0nWNv7DDOOcaQTEb32WefYdq0aZgyZQrOnz+P+Ph4zJo1C3l5ecYujUijFQcvw3veIbjO+RHe8w5hxcHL5c5/4+5DndoBIE3LtLS7D5XCzpXbFfs7eVhUohSQ/kvb54ml5XzOqG9gI/1p+12n3M7Vukx5oVaf32F9+70nZWg+tkkZOdVcSf2hrfOgvE6FqsKQXM/ExcWhV69esLCwgLOzM6ZMmYL8/Hxh+o4dO9C5c2dIJBI4Ojri1VdfRVZWFgCgtLQULVu2xObNm5XWee7cOZiYmODGjRsYO3YsBg4cqDS9uLgYzZo1w6effqqxpv3792PYsGEYN24c3N3d4evrixEjRmDp0qXCPGW95atWrYKTkxOaNGmCSZMmobi4WJjn/v37GDNmDBo1agRLS0v0798fKSkpAACFQgF7e3t8++23wvzt27eHk5OT0rExMzPDw4fagwtR2djBR8UlAIBHxSXYHJtablDWljX1Hev2396VsjoqwpC9fvoENqocDwdrje1tHSRalykv1OrzO2RopKp2457m1+B0Le1ViSG5HklNTUVISAiGDh2KCxcuYPfu3YiLi8PkyZOFeYqLi7F48WIkJiZi7969SEtLQ3h4OADAxMQEI0aMwK5du5TWu3PnTvTs2ROtWrXC+PHjcejQIWRkZAjTDxw4gIcPH2L48OEa63J0dMSpU6dw48aNcuuPiYlBamoqYmJisH37dkRHRyM6OlqYHh4ejrNnz2L//v04efIkFAoFBgwYgOLiYohEIvTu3RtyuRzAk0CdlJSER48e4fLlJ+EmNjYWXbp0gaWlpdq2CwsLkZOTo/Sg+umT49d0atdV2UfjVcVQvX76BDaqnAipO0Qi5TaRCJgU3EbrMuWFWn1+h6YmIo3tDbS0V4Sun8xUp6ISzQMeih8bdiBEB2c7je0dXTS312X6n0mGx5BcRxw4cADW1tZKj/79lS+EiYyMxMiRIzFt2jS0bdsWgYGBWL9+PT7//HMUFBQAAMaOHYv+/fvDzc0N3bt3x/r163Hw4EFh6MPIkSMRHx+P9PR0AE96l7/66iuMHDkSABAYGAhPT0/s2LFD2G5UVBRefvllWFtr/g95/vz5sLOzg6urKzw9PREeHo6vv/4apaXK/wk1atQIGzduhJeXFwYOHIjnn38ex44dAwCkpKRg//792LZtG3r16oWAgADs3LkTf/31F/bu3QsACA4OFkLyr7/+ig4dOii1yeVyBAUFaawxMjIStra2wsPZ2bkivxaqgx5rGYOgrV0X//1oXB8iABZi06fOZ4je3gipu9qLmQjlBzaqHJmvI7aM6oQAZztYik0R4GyHraM64blyLmgqL9TqE7pLtJzn2tqfRp9PZmoCQ9/xwMHGXGN7M4nm9rqsibVYp/aqxJBcR0ilUpw/f17psW3bNqV5EhMTER0drRSkZTIZSktLcf36dQBAQkICBg0aBBcXF0gkEiE0loXi9u3bw9vbW+hNjo2NRVZWFl5++WVhO+PHj0dUVBQA4Pbt2zh48CDGjh2rtXYnJyecPHkSf/zxB6ZOnYrHjx8jLCwMISEhSkHZ19cXpqamSsuVDQVJSkpCgwYN0K1bN2F6kyZN4OnpiaSkJ+OYgoKCcOnSJfzzzz+IjY1FcHCwEJKLi4tx4sQJBAcHa6xx7ty5yM7OFh43b94s57dBpJ+KXoSnjUgEhPdwfep8hurtVQ0KCg1tZFgyX0fsm9QTlxaFYN+knuUGZKD8UKtP6PZ20nzueDnpd5ef6BNpGtvLu9C0JjB0b6c+F8/WVVZizV/hoa29KvHLROoIKysruLu7K7XdunVL6XleXh7eeOMNTJkyRW15FxcX5OfnQyaTQSaTYefOnbC3t0d6ejpkMhmKiv69KnfkyJHYtWsX5syZg127diEkJARNmjQRpo8ZMwZz5szByZMnceLECbRu3Rq9evV66j60a9cO7dq1Q0REBCZOnIhevXohNjYWUqkUANCwYUOl+UUikVpvc3n8/PzQuHFjxMbGIjY2FkuXLoWjoyNWrFiB3377DcXFxQgMDNS4rJmZGczMzCq8Laq7GpiINPYaV+bj5jIVvQivPCdS75Q7/Wk9hRWlLdBvkqfW2duB1UbeThKNn0yUhVqZr6NOv68IqTsmfpGgdLFnZc4pbWPqHxZVfKx9VXJtYqnxItpWTa0Muh19Lp6tq27n1Jy72bAnuR7p2LEjLl26BHd3d7WHWCzG5cuXcffuXSxfvhy9evWCl5eX0FP7X6+++ir+/PNPJCQk4NtvvxWGWpRp0qQJBg8ejKioKERHR+O1117TuVYfHx8AULqosDze3t54/PgxTp8+LbTdvXsXycnJwrpEIhF69eqFffv24eLFi3jmmWfg7++PwsJCbN26FZ07d4aVlWH/46O6Z0IvN43tr/fW3A4AFg01D4GwVBkaoW2MaEW5NLEqN2hr6ym0NdfcX6KtHdDvwj1t7yMM8P6CtNBnSEV59Ol9Lk9F/zaMZe4Ab43t7xj4Cz5Uf0dl6uPfRk263oEhuR6ZPXs2Tpw4gcmTJ+P8+fNISUnBvn37hAv3XFxcIBaLsWHDBly7dg379+/H4sWL1dbj6uqKwMBAjBs3DiUlJXjhhRfU5hk/fjy2b9+OpKQkhIWFlVvXm2++icWLFyM+Ph43btzAqVOnMGbMGNjb26NHjx4V2re2bdsiNDQUEyZMQFxcHBITEzFq1Ci0aNECoaGhwnzBwcH48ssv0b59e1hbW8PExAS9e/fGzp07tY5HJvqv2f298GZQG+FF3FJsiojgNpgVov1FMzzQtULtmgKNKlvzBjBroPm/7nf6e2l9gQlwttP68fzKlwM0LvOBlnZAvxeyN3prDmYTg8oPbPqEeHrC0KG2bJ26DPkoT0X/NoxF5uuIraOVj9/Ho8s/fvYSzWNnm0m0fxop89G8vvr4qYyh39hVBv+HqUf8/f0RGxuLd999F7169YJCoUCbNm2Eu07Y29sjOjoa77zzDtavX4+OHTti1apVGkPwyJEjERERgTFjxsDCwkJter9+/eDk5ARfX180b9683Lr69euHzz77DJs3b8bdu3fRtGlT9OjRA8eOHVMaxvE0UVFRmDp1KgYOHIiioiL07t0bP/30k9IwjaCgIJSUlCiNPQ4ODsa+ffu0jkcmUjW7v5dOXxVbNu/2k2l4WFQCS/GTr4pWDdZlgWaTPBUpt3PRwESE3ILHUOBJj5LM1xGbRz35BrzDFzOF+do6SDApuA2e83WEAtD54/CyIKBpfdro87F7RY+DqsQFMgQsOIzsgsdCm615AyQukJW7HD2h65CK6qTvOVGddD1+Swb7afwWzCWD22ldZsvoTpi4IwFHLmWiVKH+916fqP4/WJH/j6oKv5aaqkReXh5atGiBqKgoDBkyxNjlGBy/lppqMm0BurZuh6i24d9GzaXL6zdDMhlUaWkp7ty5g9WrV+Orr75CamoqGjSoex9YMCQTERHVPrq8fte99EJGlZ6ejtatW6Nly5aIjo6ukwGZiIiI6j4mGDIoV1dX8MMJIiIiqu14dwsiIiIiIhUMyUREREREKhiSiYiIiIhUMCQTEREREalgSCYiIiIiUsGQTERERESkgiGZiIiIiEgFQzIRERERkQqGZCIiIiIiFQzJREREREQqGJKJiIiIiFQwJBMRERERqWBIJiIiIiJSwZBMRERERKSCIZmIiIiISAVDMhERERGRCoZkIiIiIiIVDYxdABH9y3XOj2ptW0d3gszX0QjVEBER1V/sSSaqITQFZAB4Y0cCDl/MrOZqiIiI6jeGZA3kcjlEIhEePHhglO2LRCLs3bvXKNuujVxdXbF27dpKrcPYv/OneWvX78YugYiIqF6pdyFZJBKV+1iwYIGxS6wWwcHBmDZtmrHLEOTl5aFhw4b46quvlNpfeeUViEQipKWlKbW7urpi3rx5AIDffvsNr7/+enWVahRFJQr2JhMREVWjeheSMzIyhMfatWthY2Oj1DZjxgxjl1hpRUVFtW5b1tbW6Ny5M+RyuVK7XC6Hs7OzUvv169dx48YN9OnTBwBgb28PS0tLg9RRk22Spxq7BCIionqj3oVkR0dH4WFrawuRSKTUZm1tLcybkJCAzp07w9LSEoGBgUhOThamhYeHY/DgwUrrnjZtGoKDg4XnwcHBmDJlCmbNmoXGjRvD0dFRrac6JSUFvXv3hrm5OXx8fHD06FG1mm/evIlhw4bBzs4OjRs3RmhoqFLPalktS5cuRfPmzeHp6QkA2LRpE9q2bQtzc3M4ODjgpZdeEuaPjY3FunXrhB70svXFxsaia9euMDMzg5OTE+bMmYPHjx8r7dPkyZMxbdo0NG3aFDKZTBiqcPjwYXTo0AEWFhbo06cPsrKycPDgQXh7e8PGxgavvvoqHj58qPV3I5VKlcJwUlISCgoK8Oabbyq1y+VymJmZoUePHgDUh1uIRCJs27YNL774IiwtLdG2bVvs379faVs//fQTPDw8YGFhAalUqtZTraqwsBA5OTlKj+qWcju32rdJRERUX9W7kKyLd999F6tXr8bZs2fRoEEDjB07Vud1bN++HVZWVjh9+jRWrlyJRYsWCUG4tLQUQ4YMgVgsxunTp7FlyxbMnj1bafni4mLIZDJIJBIcP34c8fHxsLa2RkhIiFIv7rFjx5CcnIyjR4/iwIEDOHv2LKZMmYJFixYhOTkZhw4dQu/evQEA69atQ48ePTBhwgShB93Z2Rl//fUXBgwYgC5duiAxMRGbN2/Gp59+iiVLlqjtk1gsRnx8PLZs2SK0L1iwABs3bsSJEyeEYL927Vrs2rULP/74I44cOYINGzZoPVZSqRTJycnIyMgAAMTExOCZZ55Bnz59lEJyTEwMevToAXNzc63rWrhwIYYNG4YLFy5gwIABGDlyJO7duwfgyZuOIUOGYNCgQTh//jzGjx+POXPmlPdrRGRkJGxtbYWHs7NzufNXhbYOkmrfJhERUX3FkFyOpUuXIigoCD4+PpgzZw5OnDiBgoICndbh7++P+fPno23bthgzZgw6d+6MY8eOAQB+/vlnXL58GZ9//jkCAgLQu3dvLFu2TGn53bt3o7S0FNu2bYOfnx+8vb0RFRWF9PR0peBoZWWFbdu2wdfXF76+vkhPT4eVlRUGDhyIVq1aoUOHDpgyZQoAwNbWFmKxGJaWlkIPuqmpKTZt2gRnZ2ds3LgRXl5eGDx4MBYuXIjVq1ejtLRU2Fbbtm2xcuVKeHp6Cr3WALBkyRL07NkTHTp0wLhx4xAbG4vNmzejQ4cO6NWrF1566SXExMRoPVY9e/aEWCwW9ksulyMoKAidOnXCnTt3cP36dQBPerulUmm5xz08PBwjRoyAu7s7li1bhry8PJw5cwYAsHnzZrRp0warV6+Gp6cnRo4cifDw8HLXN3fuXGRnZwuPmzdvljt/VQh0a1Lt2yQiIqqvGJLL4e/vL/zs5OQEAMjKytJ7HWXrKVtHUlISnJ2d0bx5c2F62RCCMomJibh69SokEgmsra1hbW2Nxo0bo6CgAKmp/45R9fPzg1gsFp4/++yzaNWqFdzc3DB69Gjs3Lmz3KEOZfX06NEDIpFIaOvZsyfy8vJw69Ytoa1Tp05P3VcHBwdYWlrCzc1Nqa2842dpaYkuXboIITk2NhbBwcFo0KABAgMDIZfLce3aNaSnpz81JP+3FisrK9jY2Cgd927duinNr3rcVZmZmcHGxkbpUd1OXLtb7dskIiKqr/hlIuVo2LCh8HNZcCzrUTUxMYFCoVCav7i4uNx1lK3nv72yT5OXl4dOnTph586datPs7e2Fn62srJSmSSQS/P7775DL5Thy5Ajef/99LFiwAL/99hvs7OwqvH1NVLdVRvV46bPvUqkUu3fvxsWLF/Ho0SN07NgRABAUFISYmBiUlpbC0tJSLeSWV0tFt13TcUwyERFR9WFPsp7s7e2FsbNlzp8/r9M6vL29cfPmTaX1nDp1Smmejh07IiUlBc2aNYO7u7vSw9bWttz1N2jQAP369cPKlStx4cIFpKWl4ZdffgEAiMVilJSUqNVz8uRJpfAfHx8PiUSCli1b6rRv+pJKpUhJScGuXbvwzDPPwNTUFADQu3dvxMbGQi6XC8My9OXt7S0MvSijetxrIo5JJiIiqj4MyXrq06cPzp49i88//xwpKSmYP38+/vzzT53W0a9fP3h4eCAsLAyJiYk4fvw43n33XaV5Ro4ciaZNmyI0NBTHjx/H9evXIZfLMWXKFKUhEKoOHDiA9evX4/z587hx4wY+//xzlJaWCmOIXV1dcfr0aaSlpeHOnTsoLS1FREQEbt68ibfeeguXL1/Gvn37MH/+fEyfPh0mJtVzqgQGBsLMzAwbNmxAUFCQ0N61a1dkZWVh3759Tx1q8TQTJ05ESkoKZs6cieTkZOzatQvR0dGVrLzqTQpuY+wSiIiI6g2GZD3JZDLMmzcPs2bNQpcuXZCbm4sxY8botA4TExPs2bMHjx49QteuXTF+/HgsXbpUaR5LS0v8+uuvcHFxwZAhQ+Dt7Y1x48ahoKCg3HGxdnZ2+P7779GnTx94e3tjy5Yt+PLLL+Hr6wsAmDFjBkxNTeHj4wN7e3ukp6ejRYsW+Omnn3DmzBkEBARg4sSJGDduHN577z3dD5CezM3N0b17d+Tm5irdTs/MzExor2xIdnFxwXfffYe9e/ciICAAW7ZsUbtg0hjSlj+vsb2ZxAwfj+6E53wdq7kiIiKi+kukUB1YS0RPlZOTA1tbW2RnZxvlIj4iIiLSnS6v3+xJJiIiIiJSwZBMRERERKSCIZmIiIiISAVDMhERERGRCoZkIiIiIiIVDMlERERERCoYkomIiIiIVDAkExERERGpYEgmIiIiIlLBkExEREREpIIhmYiIiIhIBUMyEREREZEKhmQiIiIiIhUMyUREREREKhiSiYiIiIhUMCQTEREREalgSCYiIiIiUsGQTERERESkgiGZiIiIiEgFQzIRERERkYoGxi6AiIiMz/2dH/G49N/nDUyAq8ueN15BRERGxp5kIqJ6TjUgA8Dj0iftRET1FUNyLRceHo7BgweXO09wcDCmTZtm8G0bYr1paWkQiUQ4f/58la8nOjoadnZ2wvMFCxagffv2wvOKHMv67vDFTIRujIP3vEMI3RiHwxczjV0SGYBqQH5aOxFRfWDUkBweHg6RSKT2CAkJqfA6qioAVoerV6/itddeQ8uWLWFmZobWrVtjxIgROHv2bLVsXyqVYtu2bXBycsLy5cuVps2ZMwcikQhyuVypPTg4GKNHjwYAfP/991i8eHG11GqIYzV8+HBcuXKlCqus2w5fzMQbOxKQeCsbj4pLkHgrGxO/SGBQJiKiOsnoPckhISHIyMhQenz55ZcG3YZCocDjx48Nus7KOnv2LDp16oQrV65g69atuHTpEvbs2QMvLy+8/fbbVb79e/fuIT4+HoMGDUJwcLBaGI6JiYGzs7NSe0FBAU6dOoU+ffoAABo3bgyJRFLltRrqWFlYWKBZs2ZVWGndtinmqlqbQgFskqcaoRoiIqKqZfSQbGZmBkdHR6VHo0aNAAByuRxisRjHjx8X5l+5ciWaNWuG27dvIzw8HLGxsVi3bp3QC52Wlga5XA6RSISDBw+iU6dOMDMzQ1xcHEpLSxEZGYnWrVvDwsICAQEB+Pbbb4V1ly13+PBhdOjQARYWFujTpw+ysrJw8OBBeHt7w8bGBq+++ioePnwoLPe09apSKBQIDw9H27Ztcfz4cTz//PNo06YN2rdvj/nz52Pfvn3CvH/88Qf69OkDCwsLNGnSBK+//jry8vK0rjs/Px9jxoyBtbU1nJycsHr1ao3z/fjjj+jYsSMcHBwglUoRHx8vvJHIzc3FuXPnMHv2bKWQfPLkSRQWFkIqlQJQ78V3dXXFsmXLMHbsWEgkEri4uODjjz9W2u6ZM2fQoUMHmJubo3Pnzjh37pzWfdH1WAHAtWvXIJVKYWlpiYCAAJw8eVKYpjrcQheFhYXIyclRetQ3V25rPu9SbudWcyVERFSGw+CqjtFDcnnKQtjo0aORnZ2Nc+fOYd68edi2bRscHBywbt069OjRAxMmTBB6oZ2dnYXl58yZg+XLlyMpKQn+/v6IjIzE559/ji1btuDixYv43//+h1GjRiE2NlZpuwsWLMDGjRtx4sQJ3Lx5E8OGDcPatWuxa9cu/Pjjjzhy5Ag2bNggzF/R9ZY5f/48Ll68iLfffhsmJuq/grIgl5+fD5lMhkaNGuG3337DN998g59//hmTJ0/WesxmzpyJ2NhY7Nu3D0eOHIFcLsfvv/+uNt/+/fsRGhoK4Mmwi7y8PPz2228AgOPHj8PDwwNDhw7F6dOnUVBQAOBJ77KrqytcXV21bn/16tVC+I2IiMCbb76J5ORkAEBeXh4GDhwIHx8fJCQkYMGCBZgxY4bWdelyrMq8++67mDFjBs6fPw8PDw+MGDHCIJ8iREZGwtbWVnj89zyrLzwcrDW2t3Wo+k8TiIhIHYfBVS2jh+QDBw7A2tpa6bFs2TJh+pIlS9CoUSO8/vrrGDVqFMLCwvDCCy8AAGxtbSEWi2FpaSn0QpuamgrLLlq0CM8++yzatGkDKysrLFu2DJ999hlkMhnc3NwQHh6OUaNGYevWrUo1LVmyBD179kSHDh0wbtw4xMbGYvPmzejQoQN69eqFl156CTExMQCe9DBWdL1lUlJSAABeXl7lHptdu3ahoKAAn3/+Odq1a4c+ffpg48aN2LFjB27fvq02f15eHj799FOsWrUKffv2hZ+fH7Zv364WEgsLC3Ho0CHhOLZt2xYtWrQQeo3lcjmCgoLg6OgIFxcXoTdWLpcLvcjaDBgwABEREXB3d8fs2bPRtGlT4Vjt2rULpaWl+PTTT+Hr64uBAwdi5syZ5a6voseqzIwZM/D888/Dw8MDCxcuxI0bN3D1qvowAV3NnTsX2dnZwuPmzZuVXmdtEyF1h0ik3CYSAZOC2xinICKieo7D4KqW0e+TLJVKsXnzZqW2xo0bCz+LxWLs3LkT/v7+aNWqFT788MMKr7tz587Cz1evXsXDhw/x7LPPKs1TVFSEDh06KLX5+/sLPzs4OMDS0hJubm5KbWfOnNF5vWUUCkWF6k9KSkJAQACsrKyEtp49e6K0tBTJyclwcHBQmj81NRVFRUXo1q2b0Na4cWN4enoqzffLL7+gWbNm8PX1FdrKxiXPnTsXcrlcCK9BQUGQy+Xo3r07Tp8+jQkTJpRb83+PnUgkgqOjI7KysoT98ff3h7m5uTBPjx49yl1fRY+Vpu07OTkBALKysiocsrUxMzODmZlZpdZR28l8HbFlVCdskqci5XYu2jpIMCm4DZ7zdTR2aURE9RKHwVUto4dkKysruLu7lzvPiRMnADy52OzevXtKofFp6y5TNo73xx9/RIsWLZTmUw0/DRs2FH4WiURKz8vaSktLdV5vGQ8PDwDA5cuXtQbpqrR//36hF7mMVCrF1KlTcffuXZw7dw5BQUEAnoTkrVu3onfv3igqKhIu2tOmvGOlD12PlervDkCltk/KZL6OkDEUExHVCB4O1ki8la3WzmFwhmH04RZPk5qaiv/973/45JNP0K1bN4SFhSmFHrFYjJKSkqeux8fHB2ZmZkhPT4e7u7vSozLjS/VZb/v27eHj44PVq1drDHAPHjwAAHh7eyMxMRH5+fnCtPj4eJiYmKj1DgNAmzZt0LBhQ5w+fVpou3//vtJtzxQKBX744QdhPHIZqVSK/Px8rFmzBm3bthXuAtG7d2+cOXMGBw8eFIZl6Mvb2xsXLlwQxjgDwKlTp8pdpqLHioj018BEpFM7EdUMHAZXtYwekgsLC5GZman0uHPnDgCgpKQEo0aNgkwmw2uvvYaoqChcuHBB6Y4Nrq6uOH36NNLS0nDnzh2tvYYSiQQzZszA//73P2zfvh2pqan4/fffsWHDBmzfvl3v+vVZr0gkQlRUFK5cuYJevXrhp59+wrVr13DhwgUsXbpUCLAjR46Eubk5wsLC8OeffyImJgZvvfUWRo8erTbUAgCsra0xbtw4zJw5E7/88gv+/PNPhIeHK13wlpCQgIcPH+KZZ55RWtbNzQ0uLi7YsGGD0IsMAM7OzmjevDk+/vjjp45HfppXX30VIpEIEyZMwKVLl/DTTz9h1apV5S5T0WNFRPqb0MtNY/vrvTW3E1HNUDYMLsDZDpZiUwQ422HrqE4cBmcgRh9ucejQIWHsaBlPT09cvnwZS5cuxY0bN3DgwAEAT8aYfvzxxxgxYgSee+45BAQEYMaMGQgLC4OPjw8ePXqE69eva93W4sWLYW9vj8jISFy7dg12dnbo2LEj3nnnnUrtgz7r7dq1K86ePYulS5diwoQJuHPnDpycnBAYGIi1a9cCACwtLXH48GFMnToVXbp0gaWlJYYOHYo1a9ZoXe8HH3yAvLw8DBo0CBKJBG+//Tays//9KGbfvn0YMGAAGjRQ/9VLpVJs374dwcHBSu1BQUGIjo6udEi2trbGDz/8gIkTJ6JDhw7w8fHBihUrMHTo0HKXq8ixIiL9ze7/ZMz+9pNpeFhUAkuxKcIDXTErpHJj+Ymo6nEYXNURKXS9MopqNX9/f7z33nsYNmyYsUup1XJycmBra4vs7GzY2NgYuxwiIiKqAF1ev40+3IKqT1FREYYOHYr+/fsbuxQiIiKiGo09yUR6YE8yERFR7cOeZCIiIiKiSmBIJiIiIiJSwZBMRERERKSCIZmIiIiISAVDMhERERGRCoZkIiIiIiIVDMlERERERCoYkomIiIiIVDAkExERERGpYEgmIiIiIlLBkExEREREpIIhmYiIiIhIBUMyEREREZEKhmQiIiIiIhUMyUREREREKhiSiYiIiIhUMCQTEREREaloYOwCiOhfbnN/RKni3+cmIuBa5PPGK4iIiKie0qkn2cfHB/fu3ROeR0RE4M6dO8LzrKwsWFpaGq46onpENSADQKkCaD3nR+MUREREVI/pFJIvX76Mx48fC8+/+OIL5OTkCM8VCgUKCgoMVx1RFQkODsa0adOE566urli7dq3R6gGgFpDLKAAcvphZrbUQERHVd5Uak6xQqL+qi0SiyqySqFzh4eEYPHiwWrtcLodIJMKDBw8qtJ7vv/8eixcvNmxxVSjypyRjl0BERFSv8MI9qpcaN24MiURi7DIqLO3uQ/YmExERVSOdQrJIJFLrKWbPMdU0d+/exYgRI9CiRQtYWlrCz88PX375pdI8qsMtnqawsBA5OTlKj+q2SZ5a7dskIiKqr3S6u4VCoUDfvn3RoMGTxR49eoRBgwZBLBYDgNJ4ZSJjKSgoQKdOnTB79mzY2Njgxx9/xOjRo9GmTRt07dpVr3VGRkZi4cKFBq5UNym3c426fSIiovpEp5A8f/58peehoaFq8wwdOrRyFRE9xYEDB2Btba3UVlJSIvzcokULzJgxQ3j+1ltv4fDhw/j666/1Dslz587F9OnThec5OTlwdnbWa136autQe4aHEBER1XaVCslExiCVSrF582alttOnT2PUqFEAngTmZcuW4euvv8Zff/2FoqIiFBYWVur2hGZmZjAzM6tU3ZU1KbiNUbdPRERUn+j8ZSKnTp3CDz/8gKKiIvTt2xchISFVUReRVlZWVnB3d1dqu3XrlvDzBx98gHXr1mHt2rXw8/ODlZUVpk2bhqKiouou1aCe83U0dglERET1hk4h+dtvv8Xw4cNhYWGBhg0bYs2aNVixYoXSR9tExhYfH4/Q0FChZ7m0tBRXrlyBj4+PkSvTXzOJcXuxiYiI6hud7m4RGRmJCRMmIDs7G/fv38eSJUuwbNmyqqqNSC9t27bF0aNHceLECSQlJeGNN97A7du3jV1WpSwZ3M7YJRAREdUrOoXk5ORkzJgxA6ampgCAt99+G7m5ucjKyqqS4oj08d5776Fjx46QyWQIDg6Go6Ojxi8gqWnEpppvp9jAhEMtiIiIqptIoelr87QwMTFBZmYmmjVrJrRJJBIkJibCzc2tSgokqolycnJga2uL7Oxs2NjYGGy9Hu/+hKKSf/8kxaYiXFk6wGDrJyIiqs90ef3W+cK9bdu2Kd1+6/Hjx4iOjkbTpk2FtilTpui6WiICGIiJiIhqCJ16kl1dXZ/6DXsikQjXrl2rdGFENVlV9SQTERFR1amynuS0tLTK1EVEREREVCvodOHepk2bqqoOIiIiIqIaQ6eQ/N5770Emk+Hvv/+uqnqIiIiIiIxOp5D8559/okGDBmjXrh2++OKLqqqJiIiIiMiodBqT3Lx5c/z444+Ijo7GlClTsGfPHrz77rto0EB5Nf7+/gYtkoiIiIioOul0d4v/+vnnnxESEgKFQgGFQgGRSCT8W1JSYug6iWoU3t2CiIio9tHl9Vun4RZl1qxZg9DQUIwaNQpXrlzB9evXce3aNeFfIiIiIqLaTKfhFteuXUNYWBhSUlKwa9cuhIaGVlVdRERERERGo1NPsr+/PxwcHPDnn38yIBMRERFRnaVTSJ4zZw527typ9BXURERERER1jU4hef78+cjOzq6qWoiIiIiIagSdQrKeN8IgIiIiIqpVdL67hUgkqoo6iIiIiIhqDJ3ubgEAffv2VfvyEFW///673gURERERERmbziFZJpPB2tq6KmohIiIiIqoRdA7JM2fORLNmzaqiFiIiIiKiGkGnMckcj0xERERE9QHvbkFEREREpEKn4RbXr1+Hvb19hee3sbHB+fPn4ebmpnNhRPXR4YuZ2BRzFVdu58HDwRoRUnfIfB31nq8mqE21EhERlREpqrB7WCKRIDExkSGZjC46OhrTpk3DgwcPDLK+nJwc2NraIjs7GzY2NgZZ5+GLmXhjR4Ja+9bRnZRCpab5RCJgy6hOAFCjAml5tTIoExFRddPl9Vvn+yRT7RIeHo7BgwertcvlcohEIoOFxqpSVmfZw97eHgMGDMAff/yh03qGDx+OK1euVFGVhvHeXs37pNq+Keaq2jwKBfDWrnN4Y0cCEm9l41FxCRJvZWPiFwk4fDGzSuqtCG21bpKn6ryuwxczEboxDt7zDiF0Y5xR96sm1UJERFWDIZlqheTkZGRkZODw4cMoLCzE888/j6Kiogovb2FhUePvyvJPrub9UW2/cjtP43xFJaVqbdoCaXWFPG21ptzO1Wk9ZT3SNeENQE2qparwTQAREUMy/UdcXBx69eoFCwsLODs7Y8qUKcjPzxem79ixA507d4ZEIoGjoyNeffVVZGVlAQBKS0vRsmVLbN68WWmd586dg4mJCW7cuIGxY8di4MCBStOLi4vRrFkzfPrpp+XW1qxZMzg6OqJjx46YNm0abt68icuXLwvT16xZAz8/P1hZWcHZ2RkRERHIy/s3oEVHR8POzk54vmDBArRv3x47duyAq6srbG1t8corryA3V7fwZgweDrrdp1w1kFZnyNNWa1sHSbnLqYa0yJ+S1OZRfQNQXcHOkL3jNVF9eBNARFQRVRqSecu42iM1NRUhISEYOnQoLly4gN27dyMuLg6TJ08W5ikuLsbixYuRmJiIvXv3Ii0tDeHh4QAAExMTjBgxArt27VJa786dO9GzZ0+0atUK48ePx6FDh5CRkSFMP3DgAB4+fIjhw4dXqM7s7Gx89dVXAACxWCy0m5iYYP369bh48SK2b9+OX375BbNmzXrqPu/duxcHDhzAgQMHEBsbi+XLl2uct7CwEDk5OUoPY4mQukOXPy3VQFqdIU9TrSIRMCm4jdZlNIW0tLsPNc5b9gagOoOdoXrHa6q6/iaAiKiiqjQk85ZxNcOBAwdgbW2t9Ojfv7/SPJGRkRg5ciSmTZuGtm3bIjAwEOvXr8fnn3+OgoICAMDYsWPRv39/uLm5oXv37li/fj0OHjwo9NiOHDkS8fHxSE9PB/Ckd/mrr77CyJEjAQCBgYHw9PTEjh07hO1GRUXh5Zdffuq3OLZs2RLW1taws7PDrl278MILL8DLy0uYPm3aNEilUri6uqJPnz5YsmQJvv7663LXWVpaiujoaLRr1w69evXC6NGjcezYMY3zRkZGwtbWVng4OzuXu+6qJPN1xJZRnRDgbAdLsSksG5pqnVdTIK3OkKdaa4CzHbaO6oTnyrloT1NI06bsDUB1Bjt9e8dri7r+JoCIqKJ0Cslubm64e/duhec/ePAgWrRooXNRZFhSqRTnz59Xemzbtk1pnsTERERHRysFaZlMhtLSUly/fh0AkJCQgEGDBsHFxQUSiQRBQUEAIITi9u3bw9vbW+hNjo2NRVZWFl5++WVhO+PHj0dUVBQA4Pbt2zh48CDGjh371H04fvw4EhISEB0dDQ8PD2zZskVp+s8//4y+ffuiRYsWkEgkGD16NO7evYuHDzX3QAKAq6srJJJ/g42Tk5MwfETV3LlzkZ2dLTxu3rz51JqrkszXEfsm9cSlRSH48JX2GnuWXZtYagyk1R3y/lvrvkk9yw3IgPaQpuq/bwCqM9jp0ztemzjYmGlsbybR3E5EVFfpFJLT0tJQUlJS4fmfeeYZmJnxP1Zjs7Kygru7u9JD9c1LXl4e3njjDaUgnZiYiJSUFLRp0wb5+fmQyWSwsbHBzp078dtvv2HPnj0AoHQB3ciRI4WQvGvXLoSEhKBJkybC9DFjxuDatWs4efIkvvjiC7Ru3Rq9evV66j60bt0anp6eCAsLw/jx45WGZ6SlpWHgwIHw9/fHd999h4SEBHz00Udqtalq2LCh0nORSITSUvWL3wDAzMwMNjY2So+aQlNv7cejO0E+U6oxkNb0kKctxLs2sdTaI12dwV+f3nEiIqp9dPoyEaq7OnbsiEuXLsHd3V3j9D/++AN3797F8uXLhaEGZ8+eVZvv1VdfxXvvvYeEhAR8++23aj2+TZo0weDBgxEVFYWTJ0/itdde07nWSZMmITIyEnv27MGLL76IhIQElJaWYvXq1TAxefK+72lDLeoama9jhe87XBbyNslTkXI7F20dJJgU3KbGhLwIqTsmfpGA/47WEomAdwZ4a61R2zJVFfx1Od61ze2cQo3tWbma24mI6iqdQ/Lhw4dha2tb7jwvvPCC3gWRccyePRvdu3fH5MmTMX78eFhZWeHSpUs4evQoNm7cCBcXF4jFYmzYsAETJ07En3/+icWLF6utx9XVFYGBgRg3bhxKSko0ngvjx4/HwIEDUVJSgrCwMJ1rtbS0xIQJEzB//nwMHjwY7u7uKC4uxoYNGzBo0CDEx8erhXNSVpNDnj4hvqYH/9rEw8Eaibey1drryphrIqKK0jkkPy3UiEQinYZkUM3g7++P2NhYvPvuu+jVqxcUCgXatGkjDGuwt7dHdHQ03nnnHaxfvx4dO3bEqlWrNIbgkSNHIiIiAmPGjIGFhYXa9H79+sHJyQm+vr5o3ry5XvVOnjwZa9aswTfffINhw4ZhzZo1WLFiBebOnYvevXsjMjISY8aM0WvdxhLi64hDGu7G0L9d/Qt6+oT4mhz8a5Pq7pUnIqqpdPpaahMTE2RmZtb4L2Wgmi0vLw8tWrRAVFQUhgwZYuxy9FIVX0sNABN3JODIpUyUKgAT0ZPgt/n/v26aqLocvpjJXnkiqpN0ef3WqSeZ9z2myigtLcWdO3ewevVq2NnZcViOBltGMxCT8bFXnohIx5DM+x5TZaSnp6N169Zo2bIloqOj0aABrxslIiKimkmnlBIWFqZxjClRRbi6uvKNFhEREdUKOoXksi+BICIiIiKqy3QKySYmJk8dlywSifD48eNKFUVEREREZEw6heTvv/9ea0g+efIk1q9fr/Uby4iIiIiIagudQvLgwYPV2pKTkzFnzhz88MMPGDlyJBYtWmSo2oiIiIiIjMJE3wX//vtvTJgwAX5+fnj8+DHOnz+P7du3o1WrVoasj4iIiIio2ukckrOzszF79my4u7vj4sWLOHbsGH744Qe0a9euKuojIiIiIqp2Og23WLlyJVasWAFHR0d8+eWXCA0Nraq6iIiIiIiMRuevpbawsEC/fv1gamqqdb7vv//eIMUR1VRV9bXUREREVHWq7Gupx4wZw6+mJiIiIqI6T6eQHB0dXUVlEBERERHVHHrf3UKbrKwsQ6+SiIiIiKha6RSSLS0t8c8//wjPn3/+eWRkZAjPb9++DScnJ8NVR0RERERkBDqF5IKCAvz3Or9ff/0Vjx49UppHh+sAiYiIiIhqJIMPt+CFfURERERU2xk8JBMRERER1XY6hWSRSKTUU6z6nIiIiIioLtDpFnAKhQIeHh5CMM7Ly0OHDh1gYmIiTCciIiIiqu10CslRUVFVVQcRERERUY2hU0geNWpUuV9HTUSV8+JH8Th384HwvIOzHfZM6mm8goiIiOopncYkt2zZEnPmzEFKSkpV1UNUJeRyOUQiER48eGDsUrRSDcgAcO7mA7z4UbxxCiIiIqrHdArJERER+Pbbb+Hl5YVevXohOjoaDx8+rKraqIYru3BT22PBggXGLrFWUQ3IT2snIiKiqqNTSJ43bx6uXr2KY8eOwc3NDZMnT4aTkxMmTJiA06dPV1WNVENlZGQIj7Vr18LGxkapbcaMGTqtr7i4uIoqrf1WHLxs7BKIiIjqFb3ukxwcHIzt27cjMzMTq1evRlJSEnr06AFfX1+sWbPG0DVSDeXo6Cg8bG1tIRKJhOfNmjXDmjVr0LJlS5iZmaF9+/Y4dOiQsGxaWhpEIhF2796NoKAgmJubY+fOnQgPD8fgwYOxatUqODk5oUmTJpg0aZJSgN6xYwc6d+4MiUQCR0dHvPrqq8jKylKq7aeffoKHhwcsLCwglUqRlpamVv93330HX19fmJmZwdXVFatXr66yY1VZm2NTcfhiprHLICIiqjcq9WUi1tbWGD9+POLi4vDDDz8gMzMTM2fONFRtVIutW7cOq1evxqpVq3DhwgXIZDK88MILauPZ58yZg6lTpyIpKQkymQwAEBMTg9TUVMTExGD79u2Ijo5GdHS0sExxcTEWL16MxMRE7N27F2lpaQgPDxem37x5E0OGDMGgQYNw/vx5jB8/HnPmzFHabkJCAoYNG4ZXXnkFf/zxBxYsWIB58+Ypbee/CgsLkZOTo/SobpvkqdW+TSIiovpKp7tbqHr48CG+/vprREVFIS4uDm3atGFIJgDAqlWrMHv2bLzyyisAgBUrViAmJgZr167FRx99JMw3bdo0DBkyRGnZRo0aYePGjTA1NYWXlxeef/55HDt2DBMmTAAAjB07VpjXzc0N69evR5cuXZCXlwdra2ts3rwZbdq0EXqGPT098ccff2DFihXCcmvWrEHfvn0xb948AICHhwcuXbqEDz74QClwl4mMjMTChQsNc3D0lHI716jbJyIiqk/06kk+ceIExo8fDycnJ0yaNAmurq6IiYnBlStX1HrsqP7JycnB33//jZ49lW9d1rNnTyQlJSm1de7cWW15X19fpVsNOjk5KQ2nSEhIwKBBg+Di4gKJRIKgoCAAQHp6OgAgKSkJ3bp1U1pnjx49lJ4nJSVprC8lJQUlJSVqNc2dOxfZ2dnC4+bNm1r3v6q0dZBU+zaJiIjqK516kleuXImoqChcuXIFnTt3xgcffIARI0ZAIuGLN+nHyspKra1hw4ZKz0UiEUpLSwEA+fn5kMlkkMlk2LlzJ+zt7ZGeng6ZTIaioqIqq9PMzAxmZmZVtv6KmBTcxqjbJyIiqk90CskffPABRo0ahW+++Qbt2rWrqpqolrOxsUHz5s0RHx8v9PICQHx8PLp27VqpdV++fBl3797F8uXL4ezsDAA4e/as0jze3t7Yv3+/UtupU6fU5omPV77/cHx8PDw8PGrkF+Y0MBHhOV9HY5dBRERUb+g03MLf3x8LFiwQAvLy5cuVvpzh7t278PHxMWiBVDvNnDkTK1aswO7du5GcnIw5c+bg/PnzmDp1aqXW6+LiArFYjA0bNuDatWvYv38/Fi9erDTPxIkTkZKSgpkzZyI5ORm7du1SuyDv7bffxrFjx7B48WJcuXIF27dvx8aNG3W+bV11eb23m7FLICIiqld0CslyuRyFhYXC82XLluHevXvC88ePHyM5Odlw1VGtNWXKFEyfPh1vv/02/Pz8cOjQIezfvx9t27at1Hrt7e0RHR2Nb775Bj4+Pli+fDlWrVqlNI+Liwu+++477N27FwEBAdiyZQuWLVumNE/Hjh3x9ddf46uvvkK7du3w/vvvY9GiRRov2qsuHZztNLY7SMwwK8SreoshIiKq50QKhUJR0ZlNTEyQmZmJZs2aAQAkEgkSExPh5vakl+v27dto3ry5xgufiOqSnJwc2NraIjs7GzY2NgZbr+pXU3d0scP3ET21L0BEREQVpsvrd6VuAUdEhrVnEgMxERFRTaDTcAuRSASRSKTWRkRERERUl+jUk6xQKBAeHi7cCqugoAATJ04UbuP13/HKRERERES1lU4hOSwsTOn5qFGj1OYZM2ZM5SoiIiIiIjIynUJyVFRUVdVBRERERFRj6PW11EREREREdRlDMhERERGRCoZkIiIiIiIVDMlERERERCoYkomIiIiIVDAkExERERGpYEgmIiIiIlLBkExEREREpIIhmYiIiIhIBUMyEREREZEKhmQiIiIiIhUMyUREREREKhiSiYiIiIhUMCQTEREREalgSCYiIiIiUsGQTERERESkooGxCyAiUnX4YiY2xVzFldt58HCwRoTUHTJfx1q/LSIiqj1ECoVCYewiiGqbnJwc2NraIjs7GzY2NsYup045fDETb+xIUGvfOrqTwcNrdW6LiIiMT5fXbw63oBopPDwcgwcPVmuXy+UQiUR48OCBQbZj6PVR5UX+lKRTe2W8t/cPndqJiKj+YEgmohol7e5Dndor45/cIp3aiYio/mBIplotLi4OvXr1goWFBZydnTFlyhTk5+cL03fs2IHOnTtDIpHA0dERr776KrKysgAAaWlpkEqlAIBGjRpBJBIhPDxc43YKCwuRk5Oj9CAiIqK6iyGZaq3U1FSEhIRg6NChuHDhAnbv3o24uDhMnjxZmKe4uBiLFy9GYmIi9u7di7S0NCEIOzs747vvvgMAJCcnIyMjA+vWrdO4rcjISNja2goPZ2fnKt8/qnpiU83/BYob8L9GIqL6jhfuUY0UHh6OL774Aubm5krtJSUlKCgowP379zFjxgyYmppi69atwvS4uDgEBQUhPz9fbVkAOHv2LLp06YLc3FxYW1tDLpdDKpXi/v37sLOz01pPYWEhCgsLhec5OTlwdnbmhXtVwHXOj1qnpS1/3qDbWnHwMjbHpqq1RwS3wawQL4Nui4iIjE+XC/d4CziqsaRSKTZv3qzUdvr0aYwaNQoAkJiYiAsXLmDnzp3CdIVCgdLSUly/fh3e3t5ISEjAggULkJiYiPv376O0tBQAkJ6eDh8fnwrXYmZmBjMzMwPsFdUks/s/CcLbT6bhYVEJLMWmCA90ZUAmIiKGZKq5rKys4O7urtR269Yt4ee8vDy88cYbmDJlitqyLi4uyM/Ph0wmg0wmw86dO2Fvb4/09HTIZDIUFfHCLHpidn8vISwTERGVYUimWqtjx464dOmSWpAu88cff+Du3btYvny5MIb47NmzSvOIxWIAT4ZxUM0mMnYBRERUr/DqFKq1Zs+ejRMnTmDy5Mk4f/48UlJSsG/fPuHCPRcXF4jFYmzYsAHXrl3D/v37sXjxYqV1tGrVCiKRCAcOHMA///yDvLw8Y+wK/UeIli/xCGnHL/cgIqLqw5BMtZa/vz9iY2Nx5coV9OrVCx06dMD777+P5s2bAwDs7e0RHR2Nb775Bj4+Pli+fDlWrVqltI4WLVpg4cKFmDNnDhwcHJTujEHGsWV0J4T4OsLk/7uOTURA/3aO2Dyqk3ELIyKieoV3tyDSA7+WmoiIqPbh11ITEREREVUCQzIRERERkQqGZCIiIiIiFQzJREREREQqGJKJiIiIiFQwJBMRERERqWBIJiIiIiJSwZBMRERERKSCIZmIiIiISAVDMhERERGRCoZkIiIiIiIVDMlERERERCoYkomIiIiIVDAkExERERGpYEgmIiIiIlLBkExEREREpIIhmYiIiIhIBUMyEREREZEKhmQiIiIiIhUNjF0AEZGqwxczsSnmKq7czoOHgzUipO6Q+ToauyxBddXH40BEZDwihUKhMHYRRLVNTk4ObG1tkZ2dDRsbG2OXU6ccvpiJN3YkKLWJAGwZ3alGBDCN9YmALaMMW5+m7QDA1hp8HICaUx8RkSa6vH5zuAURVanDFzMRujEO3vMOIXRjHA5fzCx3/sifktTaFFrajWFTzFW1NoUC2CRPNeh25u39U6f26qbt91FTfk9ERJXFkFxPhYeHQyQSQSQSoWHDhnBwcMCzzz6Lzz77DKWlpcYu76n+W/9/H1evqgcYMp6y3sbEW9l4VFyCxFvZeGNHQrlBOe3uQ53aq9uV23ka21Nu5xp0O1m5hTq1V7cbWn4f2tqJiGobhuR6LCQkBBkZGUhLS8PBgwchlUoxdepUDBw4EI8fPzZ2eU9VVv9/H61btzZ2WfQfdbG30cPBWmN7WwdJNVdiXNrG6XH8HhHVFQzJ9ZiZmRkcHR3RokULdOzYEe+88w727duHgwcPIjo6WpjvwYMHGD9+POzt7WFjY4M+ffogMTFRmL5gwQK0b98eO3bsgKurK2xtbfHKK68gN/ffnrVvv/0Wfn5+sLCwQJMmTdCvXz/k5+cL07dt2wZvb2+Ym5vDy8sLmzZtqnD9/32YmpoCAGJjY9G1a1eYmZnByckJc+bMUQr+ubm5GDlyJKysrODk5IQPP/wQwcHBmDZtWiWOKKmqi72NgW2aamlvUs2VEBFRVWJIJiV9+vRBQEAAvv/+e6Ht5ZdfRlZWFg4ePIiEhAR07NgRffv2xb1794R5UlNTsXfvXhw4cAAHDhxAbGwsli9fDgDIyMjAiBEjMHbsWCQlJUEul2PIkCEou2Z0586deP/997F06VIkJSVh2bJlmDdvHrZv367XPvz1118YMGAAunTpgsTERGzevBmffvoplixZIswzffp0xMfHY//+/Th69CiOHz+O33//Xes6CwsLkZOTo/Sgp6uLvY07T9/Q3H5KczsREdVOvAUcqfHy8sKFCxcAAHFxcThz5gyysrJgZmYGAFi1ahX27t2Lb7/9Fq+//joAoLS0FNHR0ZBInnzkPHr0aBw7dgxLly5FRkYGHj9+jCFDhqBVq1YAAD8/P2F78+fPx+rVqzFkyBAAQOvWrXHp0iVs3boVYWFhWus8cOAArK3//ei7f//++Oabb7Bp0yY4Oztj48aNEIlE8PLywt9//43Zs2fj/fffR35+PrZv345du3ahb9++AICoqCg0b95c67YiIyOxcOFCnY8l1T05BZqHImlr15dI9OSCQFUmIoNuhoiItGBIJjUKhQIi0ZNX4sTEROTl5aFJE+WPkh89eoTU1H+v5nd1dRUCMgA4OTkhKysLABAQEIC+ffvCz88PMpkMzz33HF566SU0atQI+fn5SE1Nxbhx4zBhwgRh+cePH8PW1rbcOqVSKTZv3iw8t7KyAgAkJSWhR48ewj4AQM+ePZGXl4dbt27h/v37KC4uRteuXYXptra28PT01LqtuXPnYvr06cLznJwcODs7l1sfUWWYikR4rCElm4iYkomIqgNDMqlJSkoSLoDLy8uDk5MT5HK52nx2dnbCzw0bNlSaJhKJhLtkmJqa4ujRozhx4gSOHDmCDRs24N1338Xp06dhaWkJAPjkk0/QrVs3pXWUjS/WxsrKCu7u7rrunl7MzMyEnnSi6uDb3AaJt7LV21uU/+axuoigedgMIzwR1RUck0xKfvnlF/zxxx8YOnQoAKBjx47IzMxEgwYN4O7urvRo2lTzBUyaiEQi9OzZEwsXLsS5c+cgFouxZ88eODg4oHnz5rh27Zra+vW9U4W3tzdOnjyJ/35PTnx8PCQSCVq2bAk3Nzc0bNgQv/32mzA9OzsbV65c0Wt7pF0zieY3FtraawMbc819C7Za2vUVIXWHaqexSARMCm5j0O3oq1UTS83tTa2quRIioqrBkFyPFRYWIjMzE3/99Rd+//13LFu2DKGhoRg4cCDGjBkDAOjXrx969OiBwYMH48iRI0hLS8OJEyfw7rvv4uzZsxXazunTp7Fs2TKcPXsW6enp+P777/HPP//A29sbALBw4UJERkZi/fr1uHLlCv744w9ERUVhzZo1eu1XREQEbt68ibfeeguXL1/Gvn37MH/+fEyfPh0mJiaQSCQICwvDzJkzERMTg4sXL2LcuHEwMTFRGqJBlbd4cDuN7Uu0tAOApVjzJwja2qvbBy8H6NSuL5mvI7aM6oQAZztYik0R4GyHraM64bka8m12cwd4a2x/p79XNVdCRFQ1ONyiHjt06BCcnJzQoEEDNGrUCAEBAVi/fj3CwsJgYvLk/ZNIJMJPP/2Ed999F6+99hr++ecfODo6onfv3nBwcKjQdmxsbPDrr79i7dq1yMnJQatWrbB69Wr0798fADB+/HhYWlrigw8+wMyZM2FlZQU/Pz+9b8fWokUL/PTTT5g5cyYCAgLQuHFjjBs3Du+9954wz5o1azBx4kQMHDgQNjY2mDVrFm7evAlzc3O9tkmayXwdsXV0J2ySpyLldi7aOkgwKbhNuUHvw+HtNX7d8drh7auw0orTZ58qs62a+hXP1XkciIiMQaRQaLp+mqh+yc/PR4sWLbB69WqMGzfuqfPr8t3vpLvDFzMZvoiIyOB0ef1mTzLVS+fOncPly5fRtWtXZGdnY9GiRQCA0NBQI1dGQM3uQSUiovqBIZnqrVWrViE5ORlisRidOnXC8ePHdboYkYiIiOouhmSqlzp06ICEBPVxr0REREQA725BRERERKSGIZmIiIiISAVDMhERERGRCoZkIiIiIiIVDMlERERERCoYkomIiIiIVDAkExERERGpYEgmIiIiIlLBkExEREREpIIhmYiIiIhIBUMyEREREZEKhmQiIiIiIhUMyUREREREKhiSiYiIiIhUMCQTEREREalgSCYiIiIiUsGQTERERESkooGxCyAiIsNacfAyok+k4VFxCSwamiI80BWz+3sZuywiolqFIZmI6rXDFzOxKeYqrtzOg4eDNSKk7pD5Ohq7LL2tOHgZm2NTheePikuE5wzKREQVx+EWtdiCBQvQvn37cucJDw/H4MGDDb5tQ61XJBJh7969Vb4euVwOkUiEBw8eAACio6NhZ2cnTK/IsaS65/DFTLyxIwGJt7LxqLgEibey8caOBBy+mGns0vT2adx1ze3xmtuJiEgzhmQjyczMxFtvvQU3NzeYmZnB2dkZgwYNwrFjx6pl+6+99hree+89dO/eHRMnTlSatmXLFohEIkRHRyu1h4eHo1evXgCAdevWqU2vKoY4VoGBgcjIyICtrW0VVkq1TeRPSTq11wZFJaWa2x9rbiciIs043MII0tLS0LNnT9jZ2eGDDz6An58fiouLcfjwYUyaNAmXL1+u0u2XlJTgwIED+PHHH1FSUoI9e/YoTY+JiYGzszPkcjnCw8OFdrlcjrCwMACotrBpqGMlFovh6Fh7P0KnqnHj7kOd2omIqP5gT7IRREREQCQS4cyZMxg6dCg8PDzg6+uL6dOn49SpU8J86enpCA0NhbW1NWxsbDBs2DDcvn1b63pLSkowffp02NnZoUmTJpg1axYUCoXafCdOnEDDhg3RpUsXSKVSJCcnIzPz34+XY2NjMWfOHMjlcqHt+vXruHHjBqRSKQD14RbBwcGYMmUKZs2ahcaNG8PR0RELFixQ2m5KSgp69+4Nc3Nz+Pj44OjRowY7VgBw584dvPjii7C0tETbtm2xf/9+YZrqcAtdFRYWIicnR+lBtZ/6X0f57UREVH8wJFeze/fu4dChQ5g0aRKsrKzUppeNky0tLUVoaCju3buH2NhYHD16FNeuXcPw4cO1rnv16tWIjo7GZ599hri4ONy7d0+tlxgA9u/fj0GDBkEkEqFnz55o2LAhYmJiAACXLl3Co0ePMG7cONy9exfXrz8ZxxgTEwNzc3P06NFD6/a3b98OKysrnD59GitXrsSiRYuEIFxaWoohQ4ZALBbj9OnT2LJlC2bPnm2QY1Vm4cKFGDZsGC5cuIABAwZg5MiRuHfvXrnbqKjIyEjY2toKD2dnZ4Osl4iIiGomhuRqdvXqVSgUCnh5lX+V+bFjx/DHH39g165d6NSpE7p164bPP/8csbGx+O233zQus3btWsydOxdDhgyBt7c3tmzZonFYxL59+/DCCy8AAKysrNC1a1eh11gul+OZZ56BmZkZAgMDldp79OgBMzMzrTX7+/tj/vz5aNu2LcaMGYPOnTsL44Z//vlnXL58GZ9//jkCAgLQu3dvLFu2zCDHqkx4eDhGjBgBd3d3LFu2DHl5eThz5kyFln2auXPnIjs7W3jcvHnTIOslMjR7iVhjezOJ9r9dIiJSx5BczTQNf9AkKSkJzs7OSj2WPj4+sLOzQ1KS+kVF2dnZyMjIQLdu3YS2Bg0aoHPnzmrr/fvvv9G3b1+hLTg4WCkMBwcHAwCCgoKU2suGWmjj7++v9NzJyQlZWVlK+9O8eXNhenm90kDFj5Wm7VtZWcHGxkbYfmWZmZnBxsZG6UG1n0jH9tpgyWA/Le3tqrkSIqLajSG5mrVt2xYikajKL87TZv/+/Xj22Wdhbm4utEmlUly5cgV//fUX5HI5goKCAPwbklNTU3Hz5k306dOn3HU3bNhQ6blIJEJpqf5X1Ot6rAy9far76uKYZJmvI7aO7oQAZztYik0R4GyHj0d3wnO1+N7PRETGwJBczRo3bgyZTIaPPvoI+fn5atPLLizz9vbGzZs3lT7Wv3TpEh48eAAfHx+15WxtbeHk5ITTp08LbY8fP0ZCQoLSfPv27UNoaKhSW2BgIMRiMTZt2oSCggJ06tQJANClSxf8888/+Oyzz4RhGfoq25+MjAyhTfXCO1UVPVZE+rJoaKqx3VKsub22kPk6Yt+knri0KAT7JvVkQCYi0gNDshF89NFHKCkpQdeuXfHdd98hJSUFSUlJWL9+vTAEoV+/fvDz88PIkSPx+++/48yZMxgzZgyCgoLUhlCUmTp1KpYvX469e/fi8uXLiIiIUAqSWVlZOHv2LAYOHKi0nIWFBbp3744NGzagZ8+eMDV9EhDEYrFSu2pPrS769esHDw8PhIWFITExEcePH8e777771OUqcqyI9BUe6KpTOxER1R8MyUbg5uaG33//HVKpFG+//TbatWuHZ599FseOHcPmzZsBPBkqsG/fPjRq1Ai9e/dGv3794Obmht27d2td79tvv43Ro0cjLCwMPXr0gEQiwYsvvihM/+GHH9C1a1c0bdpUbVmpVIrc3FxhPHKZoKAg5ObmPnU88tOYmJhgz549ePToEbp27Yrx48dj6dKlT12uIseKSF+z+3vhzaA2Qs+xpdgUEcFtMCuEX99MRFTfiRS6Xh1FtdYLL7yAZ555BrNmzTJ2KbVeTk4ObG1tkZ2dzYv4iIiIagldXr/Zk1yPPPPMMxgxYoSxyyAiIiKq8diTTKQH9iQTERHVPuxJJiIiIiKqBIZkIiIiIiIVDMlERERERCoYkomIiIiIVDAkExERERGpYEgmIiIiIlLBkExEREREpIIhmYiIiIhIBUMyEREREZEKhmQiIiIiIhUMyUREREREKhiSiYiIiIhUMCQTEREREalgSCYiIiIiUsGQTERERESkgiGZiIiIiEgFQzIRERERkQqGZCIiIiIiFQ2MXQAREdVOhy9mYlPMVVy5nQcPB2tESN0h83U0+DKVWa661PT6ajIeO6qpRAqFQmHsIqjqyOVySKVS3L9/H3Z2dsYup87IycmBra0tsrOzYWNjY+xyiJRUR+g4fDETb+xIUGoTiYAtozpp3ZY+y1RmuepS0+uryXjsqLrp8vrN4Ra1xJYtWyCRSPD48WOhLS8vDw0bNkRwcLDSvHK5HCKRCKmpqQgMDERGRgZsbW0rvK3w8HAMHjzYQJWrKykpwfLly+Hl5QULCws0btwY3bp1w7Zt24R5goODMW3atCqrgaiuKgsdibey8ai4BIm3sjFxRwIOX8w06HY2xVxVa1MogE3yVIMuU5nlqkt11nf4YiZCN8bBe94hhG6MM/jvtbpV9+92xcHL8J53CK5zfoT3vENYcfBylWyH6gYOt6glpFIp8vLycPbsWXTv3h0AcPz4cTg6OuL06dMoKCiAubk5ACAmJgYuLi5o06YNAMDR0TjvxouKiiAWi9XaFy5ciK1bt2Ljxo3o3LkzcnJycPbsWdy/f7/aaiCqqyJ/SlJrU/x/+9N6a3Xpfb5yO09je8rtXK3LJGVonnY5I0frMgBw8W/N0y/+lV3uctVF3/3SlWqva+KtbEz8IqFW97rqcx7pa8XBy9gc+2/4flRcIjyf3d/L4Nuj2o89ybWEp6cnnJycIJfLhTa5XI7Q0FC0bt0ap06dUmqXSqXCzyKRCA8ePAAAREdHw87ODocPH4a3tzesra0REhKCjIwMAMCCBQuwfft27Nu3DyKRCCKRSNjmzZs3MWzYMNjZ2aFx48YIDQ1FWlqasN2yHuilS5eiefPm8PT01Lgv+/fvR0REBF5++WW0bt0aAQEBGDduHGbMmCGsJzY2FuvWrRNqKNtObGwsunbtCjMzMzg5OWHOnDlKvevBwcGYPHkypk2bhqZNm0ImkwnH4PDhw+jQoQMsLCzQp08fZGVl4eDBg/D29oaNjQ1effVVPHz4sDK/JiKjS7+n+RzW1g5o6X3+ovzeZw8Ha43tbR0kWpcxNRHp1F6mpFTzqEBt7dWtVMuoRUPXV9N71PXhYGOmsb2ZRHN7ZXwad11ze7zmdiKG5FpEKpUiJiZGeB4TE4Pg4GAEBQUJ7Y8ePcLp06eFkKzJw4cPsWrVKuzYsQO//vor0tPThYA6Y8YMDBs2TAjOGRkZCAwMRHFxMWQyGSQSCY4fP474+HghYBcVFQnrPnbsGJKTk3H06FEcOHBA4/YdHR3xyy+/4J9//tE4fd26dejRowcmTJgg1ODs7Iy//voLAwYMQJcuXZCYmIjNmzfj008/xZIlS5SW3759O8RiMeLj47FlyxahfcGCBdi4cSNOnDghBP61a9di165d+PHHH3HkyBFs2LBBY02FhYXIyclRehDVRNquMinv6pOnhS9NH/FHSN0hUsm2IhEwKbiN1u1oC42PnxImtU2tGRFZe/1P2y9d1fQedYNSPbkMoKikVHP7Y83tRBxuUYtIpVJMmzYNjx8/xqNHj3Du3DkEBQWhuLhYCIMnT55EYWFhuSG5bP6y4RiTJ0/GokWLAADW1tawsLBAYWGh0jCNL774AqWlpdi2bRtE//+fV1RUFOzs7CCXy/Hcc88BAKysrLBt27ZyhzisWbMGL730EhwdHeHr64vAwECEhoaif//+AABbW1uIxWJYWloq1bBp0yY4Oztj48aNEIlE8PLywt9//43Zs2fj/fffh4nJk/d8bdu2xcqVK4XlynrJlyxZgp49ewIAxo0bh7lz5yI1NRVubm4AgJdeegkxMTGYPXu2Ws2RkZFYuHCh1n0iqilMTUQaw1l5vbXlfeRd3kf8W0Z1wiZ5KlJu56KtgwSTgtvguXI+9m9uZ460u+o92s1tzcvbJfp/JVre6Wjrya4NbucUamzPyimo5kqI1LEnuRYJDg5Gfn4+fvvtNxw/fhweHh6wt7dHUFCQMC5ZLpfDzc0NLi4uWtdjaWkpBGQAcHJyQlZWVrnbTkxMxNWrVyGRSGBtbQ1ra2s0btwYBQUFSE3996M+Pz+/p44B9vHxwZ9//olTp05h7NixyMrKwqBBgzB+/Phyl0tKSkKPHj2EkA4APXv2RF5eHm7duiW0derUSePy/v7+ws8ODg6wtLQUAnJZm7bjMHfuXGRnZwuPmzdvllsrkbHo06tZ3kfe5fUyy3wdsW9ST1xaFIJ9k3qWG5Cp8rRl4Roy6kQv+gzb0VcDLW8UtbUTsSe5FnF3d0fLli0RExOD+/fvIygoCADQvHlzODs748SJE4iJiUGfPn3KXU/Dhg2VnotEIjztToB5eXno1KkTdu7cqTbN3t5e+NnKyqpC+2JiYoIuXbqgS5cumDZtGr744guMHj0a7777Llq3bl2hdWijrYb/7rdIJNJ4HEpLNX/sZmZmBjMzw4+RI6rpDHlhldZew1zN7U9TU6KNvUSMf3KL1NqbSQx70bBFQ1M8Ki5Ra7cUmxp0O9UpQuqOiV8kKL0BeNqwHX2ZiETQNEjnaWPiqf5iT3ItI5VKIZfLIZfLlW791rt3bxw8eBBnzpwpd6hFRYjFYpSUKP9H3LFjR6SkpKBZs2Zwd3dXeuhyezltfHx8AAD5+flaa/D29sbJkyeVAn18fDwkEglatmxZ6RqI6qvywqshe/r0XZdrE0uN7a2aVuxNeVVbMthPp3Z9hQe66tReG8h8HbFlVCcEONvBUmyKAGc7bB3VqUo+lfB20nyeeTnxXvekGUNyLSOVShEXF4fz588LPckAEBQUhK1bt6KoqKjSIdnV1RUXLlxAcnIy7ty5g+LiYowcORJNmzZFaGgojh8/juvXr0Mul2PKlClKQx0q4qWXXsKHH36I06dP48aNG5DL5Zg0aRI8PDzg5eUl1HD69GmkpaXhzp07KC0tRUREBG7evIm33noLly9fxr59+zB//nxMnz5dGI9MVN+JTTX/LYgbaP8bKS+86nOBnjb6rmvuAG+N7e/UkNt2yXwdsXW0ctD7eLThg97s/l54M6iN0HNsKTZFRHAbzAqpGcdBX9U1bMeQ5zLVD0wWtYxUKsWjR4/g7u4OBwcHoT0oKAi5ubnCreIqY8KECfD09ETnzp1hb2+P+Ph4WFpa4tdff4WLiwuGDBkCb29vjBs3DgUFBTp/45xMJsMPP/yAQYMGwcPDA2FhYfDy8sKRI0fQoMGTEUAzZsyAqakpfHx8YG9vj/T0dLRo0QI//fQTzpw5g4CAAEycOBHjxo3De++9V6n9JapLxj2jebjSeC3tQPnhwZA9ffquq7pCaGVUV9Cb3d8LlxaFIG3587i0KKTWB+TqVJ291lQ38GupifTAr6WmmmzFwcvYfjIND4tKYCk2RXig61PD1OGLmTrdqYKIqDbS5fWbIZlIDwzJREREtY8ur98cbkFEREREpIIhmYiIiIhIBUMyEREREZEKhmQiIiIiIhUMyUREREREKhiSiYiIiIhUMCQTEREREalgSCYiIiIiUtHA2AUQ1UZl38GTk5Nj5EqIiIioospetyvyXXoMyUR6yM3NBQA4OzsbuRIiIiLSVW5uLmxtbcudh19LTaSH0tJS/P3335BIJBCJRAZdd05ODpydnXHz5s16/ZXXPA5P8Dj8i8fiCR6HJ3gc/sVj8URFjoNCoUBubi6aN28OE5PyRx2zJ5lIDyYmJmjZsmWVbsPGxqZe/2dXhsfhCR6Hf/FYPMHj8ASPw794LJ542nF4Wg9yGV64R0RERESkgiGZiIiIiEgFQzJRDWNmZob58+fDzMzM2KUYFY/DEzwO/+KxeILH4Qkeh3/xWDxh6OPAC/eIiIiIiFSwJ5mIiIiISAVDMhERERGRCoZkIiIiIiIVDMlERERERCoYkolqkI8++giurq4wNzdHt27dcObMGWOXVO0WLFgAkUik9PDy8jJ2WVXu119/xaBBg9C8eXOIRCLs3btXabpCocD7778PJycnWFhYoF+/fkhJSTFOsVXsacciPDxc7RwJCQkxTrFVJDIyEl26dIFEIkGzZs0wePBgJCcnK81TUFCASZMmoUmTJrC2tsbQoUNx+/ZtI1VcdSpyLIKDg9XOiYkTJxqp4qqxefNm+Pv7C1+U0aNHDxw8eFCYXl/Oh6cdB0OeCwzJRDXE7t27MX36dMyfPx+///47AgICIJPJkJWVZezSqp2vry8yMjKER1xcnLFLqnL5+fkICAjARx99pHH6ypUrsX79emzZsgWnT5+GlZUVZDIZCgoKqrnSqve0YwEAISEhSufIl19+WY0VVr3Y2FhMmjQJp06dwtGjR1FcXIznnnsO+fn5wjz/+9//8MMPP+Cbb75BbGws/v77bwwZMsSIVVeNihwLAJgwYYLSObFy5UojVVw1WrZsieXLlyMhIQFnz55Fnz59EBoaiosXLwKoP+fD044DYMBzQUFENULXrl0VkyZNEp6XlJQomjdvroiMjDRiVdVv/vz5ioCAAGOXYVQAFHv27BGel5aWKhwdHRUffPCB0PbgwQOFmZmZ4ssvvzRChdVH9VgoFApFWFiYIjQ01Cj1GEtWVpYCgCI2NlahUDz5/Tds2FDxzTffCPMkJSUpAChOnjxprDKrheqxUCgUiqCgIMXUqVONV5SRNGrUSLFt27Z6fT4oFP8eB4XCsOcCe5KJaoCioiIkJCSgX79+QpuJiQn69euHkydPGrEy40hJSUHz5s3h5uaGkSNHIj093dglGdX169eRmZmpdH7Y2tqiW7du9fL8AAC5XI5mzZrB09MTb775Ju7evWvskqpUdnY2AKBx48YAgISEBBQXFyudE15eXnBxcanz54TqsSizc+dONG3aFO3atcPcuXPx8OFDY5RXLUpKSvDVV18hPz8fPXr0qLfng+pxKGOoc6GBoQolIv3duXMHJSUlcHBwUGp3cHDA5cuXjVSVcXTr1g3R0dHw9PRERkYGFi5ciF69euHPP/+ERCIxdnlGkZmZCQAaz4+yafVJSEgIhgwZgtatWyM1NRXvvPMO+vfvj5MnT8LU1NTY5RlcaWkppk2bhp49e6Jdu3YAnpwTYrEYdnZ2SvPW9XNC07EAgFdffRWtWrVC8+bNceHCBcyePRvJycn4/vvvjVit4f3xxx/o0aMHCgoKYG1tjT179sDHxwfnz5+vV+eDtuMAGPZcYEgmohqlf//+ws/+/v7o1q0bWrVqha+//hrjxo0zYmVUU7zyyivCz35+fvD390ebNm0gl8vRt29fI1ZWNSZNmoQ///yzXozNfxptx+L1118Xfvbz84OTkxP69u2L1NRUtGnTprrLrDKenp44f/48srOz8e233yIsLAyxsbHGLqvaaTsOPj4+Bj0XONyCqAZo2rQpTE1N1a5Evn37NhwdHY1UVc1gZ2cHDw8PXL161dilGE3ZOcDzQzM3Nzc0bdq0Tp4jkydPxoEDBxATE4OWLVsK7Y6OjigqKsKDBw+U5q/L54S2Y6FJt27dAKDOnRNisRju7u7o1KkTIiMjERAQgHXr1tW780HbcdCkMucCQzJRDSAWi9GpUyccO3ZMaCstLcWxY8eUxlnVR3l5eUhNTYWTk5OxSzGa1q1bw9HRUen8yMnJwenTp+v9+QEAt27dwt27d+vUOaJQKDB58mTs2bMHv/zyC1q3bq00vVOnTmjYsKHSOZGcnIz09PQ6d0487Vhocv78eQCoU+eEJqWlpSgsLKxX54MmZcdBk8qcCxxuQVRDTJ8+HWFhYejcuTO6du2KtWvXIj8/H6+99pqxS6tWM2bMwKBBg9CqVSv8/fffmD9/PkxNTTFixAhjl1al8vLylHo6rl+/jvPnz6Nx48ZwcXHBtGnTsGTJErRt2xatW7fGvHnz0Lx5cwwePNh4RVeR8o5F48aNsXDhQgwdOhSOjo5ITU3FrFmz4O7uDplMZsSqDWvSpEnYtWsX9u3bB4lEIowrtbW1hYWFBWxtbTFu3DhMnz4djRs3ho2NDd566y306NED3bt3N3L1hvW0Y5Gamopdu3ZhwIABaNKkCS5cuID//e9/6N27N/z9/Y1cveHMnTsX/fv3h4uLC3Jzc7Fr1y7I5XIcPny4Xp0P5R0Hg58LBrlHBhEZxIYNGxQuLi4KsVis6Nq1q+LUqVPGLqnaDR8+XOHk5KQQi8WKFi1aKIYPH664evWqscuqcjExMQoAao+wsDCFQvHkNnDz5s1TODg4KMzMzBR9+/ZVJCcnG7foKlLesXj48KHiueeeU9jb2ysaNmyoaNWqlWLChAmKzMxMY5dtUJr2H4AiKipKmOfRo0eKiIgIRaNGjRSWlpaKF198UZGRkWG8oqvI045Fenq6onfv3orGjRsrzMzMFO7u7oqZM2cqsrOzjVu4gY0dO1bRqlUrhVgsVtjb2yv69u2rOHLkiDC9vpwP5R0HQ58LIoVCoahMoiciIiIiqms4JpmIiIiISAVDMhERERGRCoZkIiIiIiIVDMlERERERCoYkomIiIiIVDAkExERERGpYEgmIiIiIlLBkExEREREpIIhmYiIiIhIBUMyEVEtEx4eDpFIpPbo06cPmjZtiuXLl2tcbvHixXBwcEBxcTGio6M1rsPc3FxtO6rr27t3L0QiUbm1lD1cXV2fuj/BwcHC/GZmZmjRogUGDRqE77//Xmm+tLQ0iEQinD9/XuM6pk2bJjx3dXUV1mlpaQk/Pz9s27ZN4/a//PJLmJqaYtKkSRpr0vQIDg4WtrN27Vql9Z04cQIDBgxAo0aNYG5uDj8/P6xZswYlJSVK85Ud7xs3bii1Dx48GOHh4eUftP8XHh6OwYMHq7XL5XKIRCI8ePBAaCspKcGHH34IPz8/mJubo1GjRujfvz/i4+OVll2wYAHat2+vtk7V41+2jbKHvb09BgwYgD/++ENpuX/++QdvvvkmXFxcYGZmBkdHR8hkMrXtEtU0DMlERLVQSEgIMjIylB7fffcdRo0ahaioKLX5FQoFoqOjMWbMGDRs2BAAYGNjo7YO1cBmbm6OFStW4P79+xrrWLdundLyABAVFSU8/+233yq0PxMmTEBGRgZSU1Px3XffwcfHB6+88gpef/11XQ6LkkWLFiEjIwN//vknRo0ahQkTJuDgwYNq83366aeYNWsWvvzySxQUFAAAvv/+e2Efzpw5AwD4+eefhTbVAF9mz549CAoKQsuWLRETE4PLly9j6tSpWLJkCV555RUoFAql+UUiEd5//32997GiFAoFXnnlFSxatAhTp05FUlIS5HI5nJ2dERwcjL179+q97uTkZGRkZODw4cMoLCzE888/j6KiImH60KFDce7cOWzfvh1XrlzB/v37ERwcjLt37xpgz4iqTgNjF0BERLor65FTNW7cOKxbtw5xcXF45plnhPbY2Fhcu3YN48aNE9pEIpHGdfxXv379cPXqVURGRmLlypVq021tbWFra6vUZmdn99T1qrK0tBSWadmyJbp37w4vLy+MHTsWw4YNQ79+/XRaHwBIJBJhnbNnz8bKlStx9OhR9O/fX5jn+vXrOHHiBL777jvExMTg+++/x6uvvorGjRsL85QF5yZNmpS7X/n5+ZgwYQJeeOEFfPzxx0L7+PHj4eDggBdeeAFff/01hg8fLkybPHky1qxZg5kzZ6Jdu3Y672NFff311/j222+xf/9+DBo0SGj/+OOPcffuXYwfPx7PPvssrKysdF53s2bNhN/5tGnT8MILL+Dy5cvw9/fHgwcPcPz4ccjlcgQFBQEAWrVqha5duxps34iqCnuSiYjqED8/P3Tp0gWfffaZUntUVBQCAwPh5eWl0/pMTU2xbNkybNiwAbdu3TJkqU8VFhaGRo0aae21rajS0lJ89913uH//PsRisdK0qKgoPP/887C1tcWoUaPw6aef6r2dI0eO4O7du5gxY4batEGDBsHDwwNffvmlUnvPnj0xcOBAzJkzR+/tVsSuXbvg4eGhFJDLvP3227h79y6OHj1aqW1kZ2fjq6++AgDhOFtbW8Pa2hp79+5FYWFhpdZPVN0YkomIaqEDBw4IAaTssWzZMgBPepO/+eYb5OXlAQByc3Px7bffYuzYsUrryM7OVlvHf3tZy7z44oto37495s+fX/U79h8mJibw8PBAWlqaXsvPnj0b1tbWMDMzw0svvYRGjRph/PjxwvTS0lJER0dj1KhRAIBXXnkFcXFxuH79ul7bu3LlCgDA29tb43QvLy9hnv+KjIzEoUOHcPz4cb22q+lcUP09XrlyRWtdZe2aaquIli1bwtraGnZ2dti1axdeeOEF4c1YgwYNEB0dje3bt8POzg49e/bEO++8gwsXLui1LaLqxJBMRFQLSaVSnD9/XukxceJEAMCIESNQUlKCr7/+GgCwe/dumJiYKH3MDzwZjqC6Dm0Xt61YsQLbt29HUlJS1e6YCoVCIVwkqKuZM2fi/Pnz+OWXX9CtWzd8+OGHcHd3F6YfPXoU+fn5GDBgAACgadOmePbZZ9V64fWpWRc+Pj4YM2aM3r3Jms4FTb9HXeuqqOPHjyMhIQHR0dHw8PDAli1blKYPHToUf//9N/bv34+QkBDI5XJ07NgR0dHRVVIPkaFwTDIRUS1kZWWlFPj+y8bGBi+99BKioqIwduxYREVFYdiwYbC2tlaaz8TEROs6VPXu3RsymQxz586t8J0XKqukpAQpKSno0qULgCf7BTzpAVf14MEDtbHRTZs2hbu7O9zd3fHNN9/Az88PnTt3ho+PD4AnF+zdu3cPFhYWwjKlpaW4cOECFi5cCBMT3fqRPDw8AABJSUkIDAxUm56UlCRsW9XChQvh4eGh1wV0ms4F1aExHh4eWt/glLWX1W9jY6P1GANQO86tW7eGnZ0dPD09kZWVheHDh+PXX39Vmsfc3BzPPvssnn32WcybNw/jx4/H/Pnzq+1cItIHe5KJiOqgcePGIS4uDgcOHMCJEyeULtjT1/Lly/HDDz/g5MmTBqjw6bZv34779+9j6NChAIDGjRujadOmSEhIUJovJycHV69eFUKeJs7Ozhg+fDjmzp0LALh79y727duHr776SqkH9ty5c7h//z6OHDmic73PPfccGjdujNWrV6tN279/P1JSUjBixAit9U2ePBnvvPOO2q3iDOGVV15BSkoKfvjhB7Vpq1evRpMmTfDss88CADw9PXHr1i3cvn1bab7ff/8d5ubmcHFx0bqdSZMm4c8//8SePXvKrcfHxwf5+fl67AlR9WFPMhFRLVRYWIjMzEyltgYNGqBp06YAnvT8uru7Y8yYMfDy8tLYs6lQKNTWATy5W4GmXlQ/Pz+MHDkS69evN9Be/Ovhw4fIzMzE48ePcevWLezZswcffvgh3nzzTUilUmG+6dOnY9myZXBwcED37t1x9+5dLF68GPb29hgyZEi525g6dSratWuHs2fPIi4uDk2aNMGwYcPUhnMMGDAAn376KUJCQnTaBysrK2zdulW4dd3kyZNhY2ODY8eOYebMmXjppZcwbNgwrcvPnTsXn3zyCa5fv642NKayXnnlFXzzzTcICwvDBx98gL59+yInJwcfffQR9u/fj2+++Ua4s4VMJoOnpydGjBiBJUuWwNHREb///jvee+89TJ06Faamplq3Y2lpiQkTJmD+/PkYPHgw7t27h5dffhljx46Fv78/JBIJzp49i5UrVyI0NNSg+0hkcAoiIqpVwsLCFADUHp6enkrzLVu2TAFAsXLlSrV1REVFaVwHAEVGRoawndDQUKXlrl+/rhCLxQptLx8AFHv27NFpf4KCgoRti8VihZOTk2LgwIGK77//Xm3ex48fK9avX6/w8/NTWFpaKlq2bKkYPny44vr160rztWrVSvHhhx+qLS+TyRT9+/dX+Pn5KSIiIjTWs3v3boVYLFb8888/wj4DUJw7d05tXk3b+fXXXxUymUxhY2OjEIvFCl9fX8WqVasUjx8/VppP07Eq+52FhYVprE2Vpt+RQqFQxMTEKAAo7t+/L7QVFxcrPvjgA4Wvr69CLBYrbGxsFDKZTBEXF6e2/F9//aUICwtTuLi4KCwsLBQ+Pj6K5cuXK4qKisrdhkKhUKSnpysaNGig2L17t6KgoEAxZ84cRceOHRW2trYKS0tLhaenp+K9995TPHz4sEL7SGQsIoWiikbyExERERHVUhyTTERERESkgiGZiIiqzPHjx9Xu4fvfB2mXnp5e7rFLT083dolEdRqHWxARUZV59OgR/vrrL63TK3oLuvro8ePH5X6RiqurKxo04PX3RFWFIZmIiIiISAWHWxARERERqWBIJiIiIiJSwZBMRERERKSCIZmIiIiISAVDMhERERGRCoZkIiIiIiIVDMlERERERCr+D8MgnVj13MpwAAAAAElFTkSuQmCC)

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

    <pre class="output-block">C:\Users\Gregg\AppData\Local\Temp\ipykernel_44052\42002734.py:11: SettingWithCopyWarning:
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
    &nbsp;&nbsp;storms_flood_only["EVENT_DURATION_HOURS"] = storms_flood_only["EVENT_DURATION"].dt.total_seconds() / 3600
    </pre>

    ![A strip plot showing the duration of Flood and Flash flood events in hours on the x-axis, ranging from 0 to 700. The y-axis shows the event type. Flash Floods all last under 24 hours while Floods can last up to 700 hours.](data:image/png;base64,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N2+uWbNm6ZprrtEzzzzj3kZ+fr7mzp2rli1b6tZbb9X48eNLrN+MGTMUFxfnvjVs2LDE8oFizMUQt+/IaY38xwYCHAAAARD0a966deumOXPmuO9Xr1692LIFPVGbN2/WsWPHlJ+fL+liaEtNTdW9996r2267TV9++aVuvvlm9e/fXzfccIPHNtq0aeP+f7169SRJhw8fVkpK8af8xo8f79HDd3lvXoHt27erbdu2Hm3o3Lmz8vPztWPHDkVFRenAgQPq3Lmzx+M6d+6szZs3u7fRpk0bRUZGutd36tSp2LpJ0qRJk3T//fe77+fk5AQtwBUwkl5Y863SWiYGtR4AAFQ2QQ9v1atXV9OmTb2WKzglmZaWppdffll16tTR/v37lZaWpvPnz0uSevXqpe+++07vvPOOVq1ape7du2v06NF68skn3dupVq2a+/8u18VfUy8IgcWpXbu2T3UMloiICEVERAS7GoXsOnQi2FUAAKDSCfppU1998803OnLkiGbOnKmf//znSklJ8RisUKBOnTpKT0/X/Pnz9cwzz+ill14qtzq2aNFCmzdv1qlTp9zL1q1bp5CQEDVv3lyxsbGqX7++1q1b5/G4devWKTU11b2Nr776SmfPnnWv//TTT8unAQ5rllAj2FUAAKDSsSa8NWrUSOHh4frTn/6kPXv2aNmyZZo2bZpHmUcffVRvvvmmdu/erW3btumtt95SixYtyq2OgwcPVmRkpNLT07V161atXr1a//3f/63f/va3SkhIkHTxFOysWbP02muvaceOHZo4caI2bdqksWPHSpJ+85vfyOVyacSIEfr666/1zjvvePQc2sIlaXTXq4NdDQAAKh1rwludOnWUmZmphQsXKjU1VTNnziwUasLDwzVp0iS1adNGv/jFLxQaGqoFCxaUWx2jo6O1cuVKHT16VNddd51uv/12de/eXc8//7y7zH333af7779fDzzwgFq3bq13331Xy5YtU7NmzSRJMTExWr58ubZs2aJ27drp4Ycf1qxZs8qtDWUV4pKSakXrxd+2181c7wYAgONcxhgT7ErAWTk5OYqLi1N2drZiY2PLvL2kiW/7VC7EJe2Z0bvMzwcAQFXk6/Hbmp43AAAAVIDRpqg8Iqt5/9mwlduy9MLq3dp56KSSE2I0qltTphMBAMAP9LzBMbn5JZ+BX7ktS7/7xwZt/iFb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nzhxwjRr1sysWrXKdOnSxR3eKvtrMGXKFNO2bdsi11X2thtjzIQJE8yNN95Y7Pqqtv8bO3asufrqq01+fn6Ff/85bQqvzp8/rw0bNqhHjx7uZSEhIerRo4fWr18fxJoF3t69e5WVleXR9ri4OHXs2NHd9vXr1ys+Pl4dOnRwl+nRo4dCQkL02WeflXudyyI7O1uSdMUVV0iSNmzYoAsXLni0PyUlRY0aNfJof+vWrZWQkOAuk5aWppycHG3btq0ca182eXl5WrBggU6dOqVOnTpVqbaPHj1avXv39mirVDXe/127dql+/fq66qqrNHjwYO3fv19S1Wj7smXL1KFDB91xxx2qW7eu2rVrp7/+9a/u9VVp/3f+/HnNnz9fw4cPl8vlqvDvP+ENXv373/9WXl6exx+oJCUkJCgrKytItSofBe0rqe1ZWVmqW7eux/qwsDBdccUVVr0++fn5GjdunDp37qxWrVpJuti28PBwxcfHe5S9vP1FvT4F6yq6LVu2KCYmRhERERo5cqSWLFmi1NTUKtF2SVqwYIG+/PJLzZgxo9C6yv4adOzYUZmZmXr33Xc1Z84c7d27Vz//+c914sSJSt92SdqzZ4/mzJmjZs2aaeXKlbr33nt13333ad68eZKq1v5v6dKlOn78uIYNGyap4v/thwV06wCsMXr0aG3dulVr164NdlXKVfPmzbVp0yZlZ2dr0aJFSk9P14cffhjsapWL77//XmPHjtWqVasUGRkZ7OqUu169ern/36ZNG3Xs2FGNGzfW66+/rqioqCDWrHzk5+erQ4cOmj59uiSpXbt22rp1q/7yl78oPT09yLUrX3PnzlWvXr1Uv379YFfFJ/S8wavatWsrNDS00CibQ4cOKTExMUi1Kh8F7Sup7YmJiTp8+LDH+tzcXB09etSa12fMmDF66623tHr1ajVo0MC9PDExUefPn9fx48c9yl/e/qJen4J1FV14eLiaNm2q9u3ba8aMGWrbtq2effbZKtH2DRs26PDhw7r22msVFhamsLAwffjhh3ruuecUFhamhISESv8aXCo+Pl7JycnavXt3lXj/69Wrp9TUVI9lLVq0cJ86rir7v++++07vvfee7r77bveyiv7+E97gVXh4uNq3b6/333/fvSw/P1/vv/++OnXqFMSaBV6TJk2UmJjo0facnBx99tln7rZ36tRJx48f14YNG9xlPvjgA+Xn56tjx47lXmd/GGM0ZswYLVmyRB988IGaNGnisb59+/aqVq2aR/t37Nih/fv3e7R/y5YtHjvwVatWKTY2ttCBwQb5+fk6d+5clWh79+7dtWXLFm3atMl969ChgwYPHuz+f2V/DS518uRJffvtt6pXr16VeP87d+5caGqgnTt3qnHjxpIq//6vQEZGhurWravevXu7l1X49z+gwyFQaSxYsMBERESYzMxM8/XXX5t77rnHxMfHe4yysdWJEyfMxo0bzcaNG40kM3v2bLNx40bz3XffGWMuDpWPj483b775pvnqq69Mv379ihwq365dO/PZZ5+ZtWvXmmbNmlkxVP7ee+81cXFxZs2aNR5D5k+fPu0uM3LkSNOoUSPzwQcfmC+++MJ06tTJdOrUyb2+YLj8zTffbDZt2mTeffddU6dOHSumS5g4caL58MMPzd69e81XX31lJk6caFwul/nnP/9pjKncbS/OpaNNjancr8EDDzxg1qxZY/bu3WvWrVtnevToYWrXrm0OHz5sjKncbTfm4vQwYWFh5o9//KPZtWuXefnll010dLSZP3++u0xl3v8Zc3HmhEaNGpkJEyYUWleR33/CG3z2pz/9yTRq1MiEh4ebn/3sZ+bTTz8NdpUcsXr1aiOp0C09Pd0Yc3G4/OTJk01CQoKJiIgw3bt3Nzt27PDYxpEjR8ygQYNMTEyMiY2NNf/1X/9lTpw4EYTW+KeodksyGRkZ7jJnzpwxo0aNMjVr1jTR0dHmV7/6lTl48KDHdvbt22d69eploqKiTO3atc0DDzxgLly4UM6t8d/w4cNN48aNTXh4uKlTp47p3r27O7gZU7nbXpzLw1tlfg0GDBhg6tWrZ8LDw82VV15pBgwY4DHHWWVue4Hly5ebVq1amYiICJOSkmJeeuklj/WVef9njDErV640kgq1yZiK/f67jDEmsH17AAAAcArXvAEAAFiE8AYAAGARwhsAAIBFCG8AAAAWIbwBAABYhPAGAABgEcIbAACARQhvAAAAFiG8AQAAWITwBsAxw4YNk8vlKnT75S9/qdq1a2vmzJlFPm7atGlKSEjQhQsXlJmZWeQ2IiMjCz3P5dtbunSpXC5XiXUpuCUlJXltT9euXd3lIyIidOWVV6pPnz5avHixR7l9+/bJ5XJp06ZNRW5j3Lhx7vtJSUnubUZHR6t169b629/+VuTzv/rqqwoNDdXo0aOLrFNRt65du7qf55lnnvHY3ieffKJbbrlFNWvWVGRkpFq3bq3Zs2crLy/Po1zB6/3dd995LO/fv7+GDRtW8ov2H8OGDVP//v0LLV+zZo1cLpeOHz/uXpaXl6enn35arVu3VmRkpGrWrKlevXpp3bp1Ho997LHHdM011xTa5uWvf8FzFNzq1KmjW265RVu2bPF43E8//aR7771XjRo1UkREhBITE5WWllboeYGKhvAGwFE9e/bUwYMHPW5vvPGGhgwZooyMjELljTHKzMzU0KFDVa1aNUlSbGxsoW1cHiQiIyM1a9YsHTt2rMh6PPvssx6Pl6SMjAz3/X/9618+tWfEiBE6ePCgvv32W73xxhtKTU3VwIEDdc899/jzsniYOnWqDh48qK1bt2rIkCEaMWKEVqxYUajc3Llz9T//8z969dVXdfbsWUnS4sWL3W34/PPPJUnvvfeee9nlwbLAkiVL1KVLFzVo0ECrV6/WN998o7Fjx+oPf/iDBg4cqMt/KdHlcunRRx8tdRt9ZYzRwIEDNXXqVI0dO1bbt2/XmjVr1LBhQ3Xt2lVLly4t9bZ37NihgwcPauXKlTp37px69+6t8+fPu9ffdttt2rhxo+bNm6edO3dq2bJl6tq1q44cOeJAy4DACQt2BQBULgU9GJe766679Oyzz2rt2rW68cYb3cs//PBD7dmzR3fddZd7mcvlKnIbl+rRo4d2796tGTNm6PHHHy+0Pi4uTnFxcR7L4uPjvW73ctHR0e7HNGjQQNdff71SUlI0fPhw3XnnnerRo4df25OkGjVquLc5YcIEPf7441q1apV69erlLrN371598skneuONN7R69WotXrxYv/nNb3TFFVe4yxQEulq1apXYrlOnTmnEiBHq27evXnrpJffyu+++WwkJCerbt69ef/11DRgwwL1uzJgxmj17tsaPH69WrVr53UZfvf7661q0aJGWLVumPn36uJe/9NJLOnLkiO6++27ddNNNql69ut/brlu3rvs9HzdunPr27atvvvlGbdq00fHjx/Xxxx9rzZo16tKliySpcePG+tnPfuZY24BAoecNQLlo3bq1rrvuOv3973/3WJ6RkaEbbrhBKSkpfm0vNDRU06dP15/+9Cf98MMPTlbVq/T0dNWsWbPYXi5f5efn64033tCxY8cUHh7usS4jI0O9e/dWXFychgwZorlz55b6ef75z3/qyJEjevDBBwut69Onj5KTk/Xqq696LO/cubNuvfVWTZw4sdTP64tXXnlFycnJHsGtwAMPPKAjR45o1apVZXqO7OxsLViwQJLcr3NMTIxiYmK0dOlSnTt3rkzbB8ob4Q2Ao9566y33gbHgNn36dEkXe98WLlyokydPSpJOnDihRYsWafjw4R7byM7OLrSNS3ulCvzqV7/SNddcoylTpgS+YZcICQlRcnKy9u3bV6rHT5gwQTExMYqIiNDtt9+umjVr6u6773avz8/PV2ZmpoYMGSJJGjhwoNauXau9e/eW6vl27twpSWrRokWR61NSUtxlLjVjxgy9++67+vjjj0v1vEX9LVz+Pu7cubPYehUsL6puvmjQoIFiYmIUHx+vV155RX379nV/SQgLC1NmZqbmzZun+Ph4de7cWQ899JC++uqrUj0XUJ4IbwAc1a1bN23atMnjNnLkSEnSoEGDlJeXp9dff12S9NprrykkJMTjdJ108bTi5dso7qL+WbNmad68edq+fXtgG3YZY4x7cIS/xo8fr02bNumDDz5Qx44d9fTTT6tp06bu9atWrdKpU6d0yy23SJJq166tm266qVCvZWnq7I/U1FQNHTq01L1vRf0tFPU++lsvX3388cfasGGDMjMzlZycrL/85S8e62+77TYdOHBAy5YtU8+ePbVmzRpde+21yszMDEh9AKdwzRsAR1WvXt0jiFwqNjZWt99+uzIyMjR8+HBlZGTozjvvVExMjEe5kJCQYrdxuV/84hdKS0vTpEmTfB4JWVZ5eXnatWuXrrvuOkkX2yVd7DG83PHjxwtde1e7dm01bdpUTZs21cKFC9W6dWt16NBBqampki4OVDh69KiioqLcj8nPz9dXX32l3//+9woJ8e97d3JysiRp+/btuuGGGwqt3759u/u5L/f73/9eycnJpRo4UNTfwuWnuJOTk4sN3gXLC+ofGxtb7GssqdDr3KRJE8XHx6t58+Y6fPiwBgwYoI8++sijTGRkpG666SbddNNNmjx5su6++25NmTKl3P6WgNKg5w1Aubrrrru0du1avfXWW/rkk088BiqU1syZM7V8+XKtX7/egRp6N2/ePB07dky33XabJOmKK65Q7dq1tWHDBo9yOTk52r17tzt8FKVhw4YaMGCAJk2aJEk6cuSI3nzzTS1YsMCjx2rjxo06duyY/vnPf/pd35tvvllXXHGFnnrqqULrli1bpl27dmnQoEHF1m/MmDF66KGHCk0p4oSBAwdq165dWr58eaF1Tz31lGrVqqWbbrpJktS8eXP98MMPOnTokEe5L7/8UpGRkWrUqFGxzzN69Ght3bpVS5YsKbE+qampOnXqVClaApQfet4AOOrcuXPKysryWBYWFqbatWtLuthT1rRpUw0dOlQpKSlF9gQZYwptQ7o4erCoXqfWrVtr8ODBeu655xxqxf87ffq0srKylJubqx9++EFLlizR008/rXvvvVfdunVzl7v//vs1ffp0JSQk6Prrr9eRI0c0bdo01alTR7/+9a9LfI6xY8eqVatW+uKLL7R27VrVqlVLd955Z6HTsrfccovmzp2rnj17+tWG6tWr68UXX3RPcTJmzBjFxsbq/fff1/jx43X77bfrzjvvLPbxkyZN0l//+lft3bu30Cnusho4cKAWLlyo9PR0PfHEE+revbtycnL05z//WcuWLdPChQvdI03T0tLUvHlzDRo0SH/4wx+UmJioL7/8Uo888ojGjh2r0NDQYp8nOjpaI0aM0JQpU9S/f38dPXpUd9xxh4YPH642bdqoRo0a+uKLL/T444+rX79+jrYRcJwBAIekp6cbSYVuzZs39yg3ffp0I8k8/vjjhbaRkZFR5DYkmYMHD7qfp1+/fh6P27t3rwkPDzfF7dYkmSVLlvjVni5durifOzw83NSrV8/ceuutZvHixYXK5ubmmueee860bt3aREdHmwYNGpgBAwaYvXv3epRr3Lixefrppws9Pi0tzfTq1cu0bt3ajBo1qsj6vPbaayY8PNz89NNP7jZLMhs3bixUtqjn+eijj0xaWpqJjY014eHhpmXLlubJJ580ubm5HuWKeq0K3rP09PQi63a5ot4jY4xZvXq1kWSOHTvmXnbhwgXzxBNPmJYtW5rw8HATGxtr0tLSzNq1aws9/scffzTp6emmUaNGJioqyqSmppqZM2ea8+fPl/gcxhizf/9+ExYWZl577TVz9uxZM3HiRHPttdeauLg4Ex0dbZo3b24eeeQRc/r0aZ/aCASLy5gAXSkKAAAAx3HNGwAAgEUIbwCqpI8//rjQHGSX3lC8/fv3l/ja7d+/P9hVBCo1TpsCqJLOnDmjH3/8sdj1vk5VUhXl5uaWOEFxUlKSwsIYDwcECuENAADAIpw2BQAAsAjhDQAAwCKENwAAAIsQ3gAAACxCeAMAALAI4Q0AAMAihDcAAACL/B/rrTsfFzY8ZQAAAABJRU5ErkJggg==)

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

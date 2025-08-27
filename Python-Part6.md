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

# This line stores the local file path as a Python string variable
storms_file = 'indiana_storms_full.csv'
```

<pre class="output-block">--2025-08-27 14:15:35--  https://raw.githubusercontent.com/harvardinformatics/python-intensive/refs/heads/main/data/indiana_storms_full.csv
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 185.199.110.133, 185.199.109.133, 185.199.108.133, ...
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|185.199.110.133|:443... connected.
HTTP request sent, awaiting response...
</pre>

<pre class="output-block">200 OK
Length: 952491 (930K) [text/plain]
Saving to: ‘indiana_storms_full.csv’


indiana_storms_full   0%[                    ]       0  --.-KB/s
</pre>

<pre class="output-block">
indiana_storms_full 100%[===================>] 930.17K  --.-KB/s    in 0.03s   

2025-08-27 14:15:35 (31.9 MB/s) - ‘indiana_storms_full.csv’ saved [952491/952491]
</pre>


```python
import pandas as pd
storms_df = pd.read_csv(storms_file)
storms_df.head()
```

<pre class="output-block">   BEGIN_YEARMONTH  BEGIN_DAY  BEGIN_TIME  END_YEARMONTH  END_DAY  END_TIME  \
0           201501          8        1700         201501        9      1200   
1           201501          5        2200         201501        6       830   
2           201501          5        2200         201501        6       900   
3           201501          5        2200         201501        6       900   
4           201501          5        2215         201501        6       930   

   EPISODE_ID  EVENT_ID    STATE  STATE_FIPS  ...  END_RANGE END_AZIMUTH  \
0       91570    548696  INDIANA          18  ...        NaN         NaN   
1       92441    555468  INDIANA          18  ...        NaN         NaN   
2       92441    555469  INDIANA          18  ...        NaN         NaN   
3       92441    555470  INDIANA          18  ...        NaN         NaN   
4       92441    555471  INDIANA          18  ...        NaN         NaN   

  END_LOCATION BEGIN_LAT  BEGIN_LON END_LAT END_LON  \
0          NaN       NaN        NaN     NaN     NaN   
1          NaN       NaN        NaN     NaN     NaN   
2          NaN       NaN        NaN     NaN     NaN   
3          NaN       NaN        NaN     NaN     NaN   
4          NaN       NaN        NaN     NaN     NaN   

                                   EPISODE_NARRATIVE  \
0  A quick-moving Alberta Clipper brought a quick...   
1  An Alberta Clipper brought a quick round of sn...   
2  An Alberta Clipper brought a quick round of sn...   
3  An Alberta Clipper brought a quick round of sn...   
4  An Alberta Clipper brought a quick round of sn...   

                                     EVENT_NARRATIVE DATA_SOURCE  
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

<pre class="output-block"><class 'pandas.core.frame.DataFrame'>
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
 #   Column           Non-Null Count  Dtype                    
---  ------           --------------  -----                    
 0   EVENT_TYPE       1315 non-null   object                   
 1   CZ_NAME          1315 non-null   object                   
 2   BEGIN_DATE_TIME  1315 non-null   datetime64[ns, UTC-05:00]
 3   END_DATE_TIME    1315 non-null   datetime64[ns, UTC-05:00]
 4   CZ_TIMEZONE      1315 non-null   object                   
 5   BEGIN_LOCATION   871 non-null    object                   
 6   END_LOCATION     871 non-null    object                   
 7   BEGIN_LAT        871 non-null    float64                  
 8   BEGIN_LON        871 non-null    float64                  
 9   END_LAT          871 non-null    float64                  
 10  END_LON          871 non-null    float64                  
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

<pre class="output-block">0        January
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

<pre class="output-block">---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[21], line 3
      1 # test your code
      2 # should return a dataframe with 7 rows
----> 3 get_event_county(storms_df, "ELKHART", "Thunderstorm Wind")

NameError: name 'get_event_county' is not defined
</pre>


```python

def get_event_county(storms, county, event):
    return storms[(storms["EVENT_TYPE"] == event) & (storms["CZ_NAME"] == county)]
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
# Your code here
```


```python
# test your function
# should return 8 rows of data
storm_by_county(storms_df, ["OHIO"])
```

<pre class="output-block">---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[24], line 3
      1 # test your function
      2 # should return 8 rows of data
----> 3 storm_by_county(storms_df, ["OHIO"])

NameError: name 'storm_by_county' is not defined
</pre>


```python
# test your function
# should return 11 rows of data

storm_by_county(storms_df, ["ELKHART", "ST. JOSEPH"], ["Thunderstorm Wind"])
```

<pre class="output-block">---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[25], line 4
      1 # test your function
      2 # should return 11 rows of data
----> 4 storm_by_county(storms_df, ["ELKHART", "ST. JOSEPH"], ["Thunderstorm Wind"])

NameError: name 'storm_by_county' is not defined
</pre>


```python

def storm_by_county(storms, county, storm_type=None):
    if storm_type:
        matches = storms[(storms['CZ_NAME'].isin(county)) & (storms['EVENT_TYPE'].isin(storm_type))]
    else:
        matches = storms[(storms['CZ_NAME'].isin(county))]
    
    return matches
```

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

<pre class="output-block">--- 3.1 ---
</pre>

<pre class="output-block">---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[28], line 5
      1 ## Test your storm_by_county function
      2 
      3 # 3.1: Display all storm events in TIPPECANOE county.
      4 print("--- 3.1 ---")
----> 5 display_storms(storm_by_county(storms_df, ["TIPPECANOE"]))
      7 # 3.2: Display all Flood and Flash Flood events in the following counties: MARION, MONROE, SPENCER, VERMILLION
      8 print("--- 3.2 ---")

NameError: name 'display_storms' is not defined
</pre>


```python

def display_storms(storms):
    for index, event in storms.iterrows():
        print("A", event["EVENT_TYPE"], "occurred on", event["BEGIN_DATE_TIME"], "in", event["CZ_NAME"], "county.")
```

4. Make a histogram that displays the count of the events which contain "flood" in the following counties: ["MARION", "MONROE", "SPENCER", "VERMILLION", "TIPPECANOE"]. The x axis will be the different "flood" event types, and the color of the bar will be the county. The y axis will be the count of the events.

HINT: First, you will have to find a way to get all values of `EVENT_TYPE` that contain the word "flood" (case insensitive) and make that into a list. Then, you can pass that list and your county list to your `storm_by_county()` function. There are many ways to get the values that contain "flood". One way is to use `str.contains()`, but will involve chaining a few methods and doing some dataframe subsetting. Another way is to use a for loop and an if statement and may be more readable. 

When you make a histogram using `sns.histplot()`, you can use the `multiple='dodge'` argument to make the bars side by side.


```python
# Your code here
```


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

<pre class="output-block"><Axes: xlabel='EVENT_TYPE', ylabel='Count'>
</pre>

<pre class="output-block"><Figure size 640x480 with 1 Axes>
</pre>

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

<pre class="output-block">--- 5.1 ---
</pre>

<pre class="output-block">---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[33], line 5
      1 ## Test your modified storm_by_county function
      2 
      3 # 5.1 Display the number of all events in PIKE county
      4 print("--- 5.1 ---")
----> 5 print(summarise_storms(storms_df, ["PIKE"]))
      7 # 5.2 Display the number of Thunderstorm Wind events in the following counties: ELKHART, LA PORTE, BOONE
      8 print("--- 5.2 ---")

NameError: name 'summarise_storms' is not defined
</pre>


```python

def summarise_storms(storms, county, storm_type=None):
  df = storm_by_county(storms, county, storm_type).groupby(["CZ_NAME","EVENT_TYPE"]).size().reset_index()
  
  return df
```

6. Use your function to summarize the total counts of each weather event in each county.


```python
# Your code here
```


```python

all_weather = storms_df["EVENT_TYPE"].unique().tolist()
all_counties = storms_df["CZ_NAME"].unique().tolist()

summarise_storms(storms_df, all_counties, all_weather)
```

<pre class="output-block">     CZ_NAME               EVENT_TYPE  0
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
county_info = pd.read_html("https://en.wikipedia.org/wiki/List_of_counties_in_Indiana")
county_info = county_info[1]
```

<pre class="output-block">Collecting lxml
</pre>

<pre class="output-block">  Downloading lxml-6.0.1-cp311-cp311-manylinux_2_26_x86_64.manylinux_2_28_x86_64.whl.metadata (3.8 kB)
Downloading lxml-6.0.1-cp311-cp311-manylinux_2_26_x86_64.manylinux_2_28_x86_64.whl (5.2 MB)
[?25l   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m0.0/5.2 MB[0m [31m?[0m eta [36m-:--:--[0m
</pre>

<pre class="output-block">
[2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m5.2/5.2 MB[0m [31m36.7 MB/s[0m  [33m0:00:00[0m
[?25h
</pre>

<pre class="output-block">Installing collected packages: lxml
</pre>

<pre class="output-block">Successfully installed lxml-6.0.1
</pre>

<pre class="output-block">---------------------------------------------------------------------------
HTTPError                                 Traceback (most recent call last)
Cell In[37], line 2
      1 get_ipython().system('pip install lxml')
----> 2 county_info = pd.read_html("https://en.wikipedia.org/wiki/List_of_counties_in_Indiana")
      3 county_info = county_info[1]

File /opt/hostedtoolcache/Python/3.11.13/x64/lib/python3.11/site-packages/pandas/io/html.py:1240, in read_html(io, match, flavor, header, index_col, skiprows, attrs, parse_dates, thousands, encoding, decimal, converters, na_values, keep_default_na, displayed_only, extract_links, dtype_backend, storage_options)
   1224 if isinstance(io, str) and not any(
   1225     [
   1226         is_file_like(io),
   (...)   1230     ]
   1231 ):
   1232     warnings.warn(
   1233         "Passing literal html to 'read_html' is deprecated and "
   1234         "will be removed in a future version. To read from a "
   (...)   1237         stacklevel=find_stack_level(),
   1238     )
-> 1240 return _parse(
   1241     flavor=flavor,
   1242     io=io,
   1243     match=match,
   1244     header=header,
   1245     index_col=index_col,
   1246     skiprows=skiprows,
   1247     parse_dates=parse_dates,
   1248     thousands=thousands,
   1249     attrs=attrs,
   1250     encoding=encoding,
   1251     decimal=decimal,
   1252     converters=converters,
   1253     na_values=na_values,
   1254     keep_default_na=keep_default_na,
   1255     displayed_only=displayed_only,
   1256     extract_links=extract_links,
   1257     dtype_backend=dtype_backend,
   1258     storage_options=storage_options,
   1259 )

File /opt/hostedtoolcache/Python/3.11.13/x64/lib/python3.11/site-packages/pandas/io/html.py:983, in _parse(flavor, io, match, attrs, encoding, displayed_only, extract_links, storage_options, **kwargs)
    972 p = parser(
    973     io,
    974     compiled_match,
   (...)    979     storage_options,
    980 )
    982 try:
--> 983     tables = p.parse_tables()
    984 except ValueError as caught:
    985     # if `io` is an io-like object, check if it's seekable
    986     # and try to rewind it before trying the next parser
    987     if hasattr(io, "seekable") and io.seekable():

File /opt/hostedtoolcache/Python/3.11.13/x64/lib/python3.11/site-packages/pandas/io/html.py:249, in _HtmlFrameParser.parse_tables(self)
    241 def parse_tables(self):
    242     """
    243     Parse and return all tables from the DOM.
    244 
   (...)    247     list of parsed (header, body, footer) tuples from tables.
    248     """
--> 249     tables = self._parse_tables(self._build_doc(), self.match, self.attrs)
    250     return (self._parse_thead_tbody_tfoot(table) for table in tables)

File /opt/hostedtoolcache/Python/3.11.13/x64/lib/python3.11/site-packages/pandas/io/html.py:806, in _LxmlFrameParser._build_doc(self)
    804             pass
    805     else:
--> 806         raise e
    807 else:
    808     if not hasattr(r, "text_content"):

File /opt/hostedtoolcache/Python/3.11.13/x64/lib/python3.11/site-packages/pandas/io/html.py:785, in _LxmlFrameParser._build_doc(self)
    783 try:
    784     if is_url(self.io):
--> 785         with get_handle(
    786             self.io, "r", storage_options=self.storage_options
    787         ) as f:
    788             r = parse(f.handle, parser=parser)
    789     else:
    790         # try to parse the input in the simplest way

File /opt/hostedtoolcache/Python/3.11.13/x64/lib/python3.11/site-packages/pandas/io/common.py:728, in get_handle(path_or_buf, mode, encoding, compression, memory_map, is_text, errors, storage_options)
    725     codecs.lookup_error(errors)
    727 # open URLs
--> 728 ioargs = _get_filepath_or_buffer(
    729     path_or_buf,
    730     encoding=encoding,
    731     compression=compression,
    732     mode=mode,
    733     storage_options=storage_options,
    734 )
    736 handle = ioargs.filepath_or_buffer
    737 handles: list[BaseBuffer]

File /opt/hostedtoolcache/Python/3.11.13/x64/lib/python3.11/site-packages/pandas/io/common.py:384, in _get_filepath_or_buffer(filepath_or_buffer, encoding, compression, mode, storage_options)
    382 # assuming storage_options is to be interpreted as headers
    383 req_info = urllib.request.Request(filepath_or_buffer, headers=storage_options)
--> 384 with urlopen(req_info) as req:
    385     content_encoding = req.headers.get("Content-Encoding", None)
    386     if content_encoding == "gzip":
    387         # Override compression based on Content-Encoding header

File /opt/hostedtoolcache/Python/3.11.13/x64/lib/python3.11/site-packages/pandas/io/common.py:289, in urlopen(*args, **kwargs)
    283 """
    284 Lazy-import wrapper for stdlib urlopen, as that imports a big chunk of
    285 the stdlib.
    286 """
    287 import urllib.request
--> 289 return urllib.request.urlopen(*args, **kwargs)

File /opt/hostedtoolcache/Python/3.11.13/x64/lib/python3.11/urllib/request.py:216, in urlopen(url, data, timeout, cafile, capath, cadefault, context)
    214 else:
    215     opener = _opener
--> 216 return opener.open(url, data, timeout)

File /opt/hostedtoolcache/Python/3.11.13/x64/lib/python3.11/urllib/request.py:525, in OpenerDirector.open(self, fullurl, data, timeout)
    523 for processor in self.process_response.get(protocol, []):
    524     meth = getattr(processor, meth_name)
--> 525     response = meth(req, response)
    527 return response

File /opt/hostedtoolcache/Python/3.11.13/x64/lib/python3.11/urllib/request.py:634, in HTTPErrorProcessor.http_response(self, request, response)
    631 # According to RFC 2616, "2xx" code indicates that the client's
    632 # request was successfully received, understood, and accepted.
    633 if not (200 <= code < 300):
--> 634     response = self.parent.error(
    635         'http', request, response, code, msg, hdrs)
    637 return response

File /opt/hostedtoolcache/Python/3.11.13/x64/lib/python3.11/urllib/request.py:563, in OpenerDirector.error(self, proto, *args)
    561 if http_err:
    562     args = (dict, 'default', 'http_error_default') + orig_args
--> 563     return self._call_chain(*args)

File /opt/hostedtoolcache/Python/3.11.13/x64/lib/python3.11/urllib/request.py:496, in OpenerDirector._call_chain(self, chain, kind, meth_name, *args)
    494 for handler in handlers:
    495     func = getattr(handler, meth_name)
--> 496     result = func(*args)
    497     if result is not None:
    498         return result

File /opt/hostedtoolcache/Python/3.11.13/x64/lib/python3.11/urllib/request.py:643, in HTTPDefaultErrorHandler.http_error_default(self, req, fp, code, msg, hdrs)
    642 def http_error_default(self, req, fp, code, msg, hdrs):
--> 643     raise HTTPError(req.full_url, code, msg, hdrs, fp)

HTTPError: HTTP Error 403: Forbidden
</pre>

You will need to do some data cleaning to get the county names to match up and to extract the area of each county. Then you will need to merge the two dataframes together. 


```python
county_info[["County", "Area[3][12]"]]
```

<pre class="output-block">---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[38], line 1
----> 1 county_info[["County", "Area[3][12]"]]

NameError: name 'county_info' is not defined
</pre>


```python
# Your code here
```


```python

# cleaning county_info
county_info["County"] = county_info["County"].str.replace(" County", "").str.upper()
county_info["Area_sq_mi"] = pd.to_numeric(county_info["Area[3][12]"].str.extract(r'([0-9,]+)')[0])

# merge the two dataframes
storms_merged = pd.merge(storms_df, county_info, left_on="CZ_NAME", right_on="County")
```

<pre class="output-block">---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[40], line 4
      1 #@title Solution: data cleaning {display-mode: "form"}
      2 
      3 # cleaning county_info
----> 4 county_info["County"] = county_info["County"].str.replace(" County", "").str.upper()
      5 county_info["Area_sq_mi"] = pd.to_numeric(county_info["Area[3][12]"].str.extract(r'([0-9,]+)')[0])
      7 # merge the two dataframes

NameError: name 'county_info' is not defined
</pre>


```python

# grouping by county and area
df = storms_merged.groupby(["CZ_NAME", "Area_sq_mi"])["EVENT_TYPE"].count().reset_index()
print(df.head())

# normalizing number of events by area
df["normalized"] = df["EVENT_TYPE"] / df["Area_sq_mi"]

# sorting by normalized value
df.sort_values("normalized", ascending=False)
```

<pre class="output-block">---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[41], line 4
      1 #@title Solution: example {display-mode: "form"}
      2 
      3 # grouping by county and area
----> 4 df = storms_merged.groupby(["CZ_NAME", "Area_sq_mi"])["EVENT_TYPE"].count().reset_index()
      5 print(df.head())
      7 # normalizing number of events by area

NameError: name 'storms_merged' is not defined
</pre>

**Question 2:** What is the best time to visit Indiana if you want to take cool pictures of clouds? The main idea of this question is to summarize the data in such a way that you can tell which month or week or your choice of span of days has the highest concentration of events of interest. 


```python
# Your code here
```


```python

# decide which weather events probably have cool clouds
cool_clouds = ["Thunderstorm wind", "Tornado", "Lightning", "Heavy Rain"]

# filter for cool clouds
df_clouds = storms_df[storms_df["EVENT_TYPE"].isin(cool_clouds)]

# group by month and number of events
df_clouds.groupby(df_clouds["BEGIN_DATE_TIME"].dt.month)["EVENT_TYPE"].count().reset_index()
```

<pre class="output-block">    BEGIN_DATE_TIME  EVENT_TYPE
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

<pre class="output-block">                        count                       mean  \
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

                                               std              min  \
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

                                     25%              50%              75%  \
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

                                      max  
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

<pre class="output-block">/tmp/ipykernel_2219/1940921173.py:11: SettingWithCopyWarning: 
A value is trying to be set on a copy of a slice from a DataFrame.
Try using .loc[row_indexer,col_indexer] = value instead

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
  storms_no_flood["EVENT_DURATION_HOURS"] = storms_no_flood["EVENT_DURATION"].dt.total_seconds() / 3600
</pre>

<pre class="output-block"><Figure size 640x480 with 1 Axes>
</pre>


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

<pre class="output-block">/tmp/ipykernel_2219/42002734.py:11: SettingWithCopyWarning: 
A value is trying to be set on a copy of a slice from a DataFrame.
Try using .loc[row_indexer,col_indexer] = value instead

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
  storms_flood_only["EVENT_DURATION_HOURS"] = storms_flood_only["EVENT_DURATION"].dt.total_seconds() / 3600
</pre>

<pre class="output-block"><Figure size 640x480 with 1 Axes>
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

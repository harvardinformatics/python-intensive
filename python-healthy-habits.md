---
title: "[Workshop] Python intensive - healthy habits"
description: "A supplemental resource for the Python intensive workshop, Includes tips on writing clean code, using comments effectively, and following best practices."
authors:
    - Lei Ma
---

# Python Healthy Habits

This is a companion Jupyter notebook to the six day FAS Informatics Python Intensive. This notebook collects tips, tricks, and healthy habits for Python and programming in general that we couldn't fit in the main course or that were too heavy on lecture.

## How to get unstuck: troubleshooting/debugging

In order to write larger programs, we need to hone our skills of troubleshooting. In this section, we're going to be talking about debugging code. We typically picture debugging as something that happens when you run something and there's an error message. However, there are many other reasons why we might want to take a closer look at our code and the tips here will be useful throughout the code-writing process.

### Manual debugging

Here are some steps to figure out what's wrong that just involve using your own brain. This is usually my first resort as it is quick and many issues end up being about a simple typo or missing step.

* Read the error message
    * What line does it refer to?
    * What state should the code be in at that point?
* (Re)Read your code
    * Explain it line by line to another person or an inanimate object
* Add error checks
    * Print messages to check variables and progress - as a programmer you should develop the skills to have a good idea of the expected state of your variables in your program, so printing them out along the way is helpful to figure out where something is going wrong
    * Peel back layers and test each layer (e.g. test each function)
* Get another pair of eyes to look at it

### Asking for help

Often times, the quickest way to get unstuck is to ask someone for help. There are some steps you can take to make it easier for others to help you. You may know all the context of your code, but a friend or one of us at office hours is going in fresh. Here's some information that you should provide when asking for help (in approximate order of effort):

1. Error message
2. What you expected to happen
3. What is the command you used
4. Your environment/context
5. A minimal reproducible example

Numbers 1 through 3 are the bare minimum information, while 4 and 5 are helpful for trickier problems. Number 5 is especially important if you are asking for help in an asynchronous way, like on a forum or in an email. This allows the person helping you to run code to see the error message for themselves and test out solutions before getting back to you.

If you're not familiar with **minimal reproducible examples**, it's a way to pare down your code to the smallest amount that still produces the error. Often in the process of doing this, you will find the error yourself. How to make a reproducible example (AKA **reprex**)? Here are some steps:

1. Start with a fresh script
2. Import only the libraries you need
3. Create only the data objects/variables you need (You may need to generate data or subset your data if it's large)
4. Write only the code that produces the error
5. Annotate the code with comments to explain what you are trying to do

If you want to then share this code (and the dummy data!) with someone else, you can either send the script to them or you can use a Python package called `reprexpy`, which will format both your code and your output in a way that is easy to post in plain text online or in an email. For more information see the docs for [reprexpy :octicons-link-external-24:](https://reprexpy.readthedocs.io/en/latest/){:target="_blank"}.  

### Using your IDE's tools

Programmers typically choose a text editor in which to write their code. Oftentimes, these text editors have extra features that aid programmers when coding (*e.g.* colored syntax, parentheses match highlighting, error checking). These text editors with extra featuers are called integrated development environments, or **IDEs**. RStudio is an example of an IDE, and other text editors have become so feature rich that they are essentially IDEs in practice, like [VScode :octicons-link-external-24:](https://code.visualstudio.com/){:target="_blank"}

In this workshop, we are coding a Jupyter notebook in Google Colab, which has IDE-like features. There are some features that might be useful for examining your code. For example, you can use the `{x}` button on the left sidebar to examine the variables in your environment. You can also use the `print()` function within blocks of your code to see what is happening at each step.

### Tests

A very helpful approach to debugging - and, indeed, writing code in general - is to have some small input data that you can use to test. Ideally this should be something that runs fast and you know what the expected output is. While this won't necessarily help you fix problems that cause your code to simply not execute, it can be extremely useful if you are not certain of how to program something, or if your program is running but with unexpected results.

For example, if you have a dataset that you have manually processed, but now want to automate with a Python script or set of scripts, you will very likely want to check your code by running it against a test input that has a known output.

This is particularly important if you are going to use LLMs for debugging, as discussed below. LLMs rarely make syntax errors, but do make logic errors.

## Code annotation

In the first few sessions of our workshop, we learned the building blocks of computer programs. Another important aspect of the text of a program is, **code annotation**. When you begin to write longer functions or scripts, it's important to leave breadcrumbs for yourself (and others) about what your code does. Code annotations are text that is visible in the document, but ignored by the Python interpreter, and therefore won't affect how the program runs. One of the most basic ways to annotate your code is with `#comments` throughout your program. Every programming language has a character that indicates a comment. For Python, that character is `#`. As soon as the Python interpreter sees this character on a line, it ignores everything after it. Though remember, `#` is different from the string `"#"`. The first one will be interpreted as a comment and the subsequent text ignored. The second will be interpreted as a string because of the double-quotes. 

While you can and should generously sprinkle comments through your program, there are also some standardized ways to annotate code in Python. If you are annotating functions, you should use something called a **"docstring"**. This is a string that is the first line of a function and is enclosed in triple quotes. It should describe what the function does, what inputs it takes, and what it returns. Here is an example of a docstring:

```python
def add(x, y):
    """
    This function adds two numbers together.
    
    Parameters:
    x (int): The first number to add
    y (int): The second number to add
    
    Returns:
    int: The sum of x and y
    """
    return x + y
```

Notice that the docstring helps the user of the function remember the type of input the function takes and what it returns.

Here is an example of a fully annotated script:


```python
# This script adds two numbers together and prints it
# Author: Your Name

# Import the necessary libraries
import numpy as np

# Define the use input function
def user_input():
    """
    This function asks the user for two numbers.
    
    Returns:
    int: The first number the user inputs
    int: The second number the user inputs
    """
    x = int(input("Enter the first number: "))
    y = int(input("Enter the second number: "))
    return x, y

# Define the add function
def add(x, y):
    """
    This function adds two numbers together.
    
    Parameters:
    x (int): The first number to add
    y (int): The second number to add
    
    Returns:
    int: The sum of x and y
    """
    return x + y

# main code
x, y = user_input()
print(add(x, y))
```

<pre class="output-block">---------------------------------------------------------------------------
StdinNotImplementedError                  Traceback (most recent call last)
Cell In[1], line 35
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;32     return x + y
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;34 # main code
---> 35 x, y = user_input()
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;36 print(add(x, y))

Cell In[1], line 16, in user_input()
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;8 def user_input():
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;9     """
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;10     This function asks the user for two numbers.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;11
&nbsp;&nbsp;&nbsp;(...)     14     int: The second number the user inputs
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;15     """
---> 16     x = int(input("Enter the first number: "))
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;17     y = int(input("Enter the second number: "))
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;18     return x, y

File C:\bin\miniforge3\Lib\site-packages\ipykernel\kernelbase.py:1281, in Kernel.raw_input(self, prompt)
&nbsp;&nbsp;&nbsp;1279 if not self._allow_stdin:
&nbsp;&nbsp;&nbsp;1280     msg = "raw_input was called, but this frontend does not support input requests."
-> 1281     raise StdinNotImplementedError(msg)
&nbsp;&nbsp;&nbsp;1282 return self._input_request(
&nbsp;&nbsp;&nbsp;1283     str(prompt),
&nbsp;&nbsp;&nbsp;1284     self._parent_ident["shell"],
&nbsp;&nbsp;&nbsp;1285     self.get_parent("shell"),
&nbsp;&nbsp;&nbsp;1286     password=False,
&nbsp;&nbsp;&nbsp;1287 )

StdinNotImplementedError: raw_input was called, but this frontend does not support input requests.
</pre>

## More advanced control flow

Computer programs work by reading a text document line by line from top to bottom and executing the code on each line in sequence. However, we've previously learned how to control the execution of certain blocks of code based on the state of the program using **conditional statements**, **loops**, and **functions**.

The following lessons on **control flow** are concerned with making a function or another block of code self-monitor its state and to give feedback to the user when it reaches certains states, such as errors or deliberate stopping points. Think of these tools as a way to make the code anticipate conditions and interrupt itself when those conditions are encountered.

### Exception Handling

**Exception handling** is a fundamental concept in Python that allows you to manage and respond to errors gracefully, ensuring that a program can continue running or fail in a controlled manner. When your code encounters an issue—such as trying to divide by zero, accessing a file that doesn't exist, or converting user input to the wrong type—Python **raises** an "exception." Without proper handling, these exceptions can (and usually do) cause your program to crash, or worse create unpredictable bugs. This is called an **unhandled exception**. By using **try and except blocks**, you can anticipate potential errors, catch these exceptions, and define alternative actions or informative messages for the user.

As an example, here is a simple function that calcutes the log2 fold change, that is log2(x/y). We will write this naively, and then see what errors we get with different inputs.


```python
import math

def log2fc(x, y):
    return math.log2(x/y)
```


```python
log2fc(0,0)
```

<pre class="output-block">---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)
Cell In[3], line 1
----> 1 log2fc(0,0)

Cell In[2], line 4, in log2fc(x, y)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3 def log2fc(x, y):
----> 4     return math.log2(x/y)

ZeroDivisionError: division by zero
</pre>


```python
log2fc(10,0)
```

<pre class="output-block">---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)
Cell In[4], line 1
----> 1 log2fc(10,0)

Cell In[2], line 4, in log2fc(x, y)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3 def log2fc(x, y):
----> 4     return math.log2(x/y)

ZeroDivisionError: division by zero
</pre>


```python
log2fc(0,10)
```

<pre class="output-block">---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
Cell In[5], line 1
----> 1 log2fc(0,10)

Cell In[2], line 4, in log2fc(x, y)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3 def log2fc(x, y):
----> 4     return math.log2(x/y)

ValueError: math domain error
</pre>


```python
log2fc("a", "b")
```

<pre class="output-block">---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[6], line 1
----> 1 log2fc("a", "b")

Cell In[2], line 4, in log2fc(x, y)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3 def log2fc(x, y):
----> 4     return math.log2(x/y)

TypeError: unsupported operand type(s) for /: 'str' and 'str'
</pre>

We see that there are three kinds of errors here, that we might want to handle. The first is a "ZeroDivisionError", when we try to divide by 0. The second is a ValueError, since the math.log2 function does not like returning -Inf for log2(0), and in our function we probably don't want that either. The last is a TypeError if we give inputs that don't have division methods (e.g., strings).

For any error, we can "catch" the error with a try-except statement, which has the following basic form:

```
try:
    code to try goes here
except ErrorType:
    code to run if try block generates ErrorType goes here
```

In a way, `try` is like an `if` statement: `if` statements check a condition to determine if the block of code should be executed. For `try`, the condition is simply "does this block of code run without error?" If so, proceed, otherwise run the code under `except`. In fact, we can even use `else` after `try` (see below)

A few things to note:

- **Specifying Error Types**: You don't need to specify an error type after `except`; if you don't, the except block will catch any error. Normally, this isn't a good idea because you might want to return specific messages or handle particular error types differently.
- **Multiple Except Blocks**: except statements actually function somewhat like `elif`: you can have many of them, each with a different ErrorType. You can also list multiple error types within a single except statement using parentheses, e.g., `except (KeyError, ValueError):` if you want to catch both errors.
- **`else` and `finally` Blocks**: You can have an `else` block (which runs only if no errors occur) or a `finally` block (which runs after the try-except regardless of whether an error occurred).

Below is a slightly improved version of our function that catches TypeErrors.


```python
def log2fc(x, y):
    try:
        ratio = x/y
    except TypeError:
        print("Error: x and y must be numbers")
        return None

    return math.log2(ratio)
```


```python
log2fc("1", "2")
```

<pre class="output-block">Error: x and y must be numbers
</pre>

>**Exercise:** Annotate the below function with comments `# like this` to explain what each try and except block is doing.
>
> Think about why there are two try/except blocks. Share with your neighbor to see if your annotations are interpreting the code the same way. After sharing with your neighbor, what are some additional questions that you have about exception handling?


```python
def log2fc(x, y):
    try:
        ratio = x/y

    # this adds a pseudocount to y if it is 0
    except ZeroDivisionError:
        y_adj = y + 1e-10
        ratio = x/y_adj
        print(f"Warning: y was 0, correcting to {y_adj}")
    # this returns none if x or y are not numbers

    except TypeError:
        print("Error: x and y must be numbers")
        return None

    # the log of 0 is undefined, but we make it return 0 instead of error
    # needs a separate try block because log2 needs to be evaluated first
    try:
        return math.log2(ratio)
    except ValueError:
        print(f"Error: log2({ratio}) is undefined, using 0")
        return 0
```


```python
# this demonstrates the error and warning messages

print(("a warning is printed when y is 0"))
print(log2fc(1,0))
print('---')
print("the log of 0 is returned as 0")
print(log2fc(0,11))
print('---')
print("an error is printed when x or y are not numbers")
print(log2fc("10",0))
```

<pre class="output-block">a warning is printed when y is 0
Warning: y was 0, correcting to 1e-10
33.219280948873624
---
the log of 0 is returned as 0
Error: log2(0.0) is undefined, using 0
0
---
an error is printed when x or y are not numbers
Error: x and y must be numbers
None
</pre>

>**Exercise**: Work with a neighbor to write the user input portion of our random walk function (from day 3). The function should take a `step_size` and `walk_size` and check that both inputs are valid. If both inputs are valid, it should return both the `step_size` and `walk_size`.
> 1. **Discuss** what conditions might need to be checked in the context of a random walk
> 2. **Plan** which order to check these conditions makes the most sense.
> 3. **Write** a function that checks that `step_size` and `walk_size` are compatible with a random walk scenario
> 4. **Test** your function
>
> Share your answer with another pair and see if they did things differently.


```python
# Your code here
def get_user_inputs(step_size, walk_size):
    if not isinstance(step_size, int) or not isinstance(walk_size, int):
        raise ValueError("Both step_size and walk_size should be integers.")

    if step_size <= 0 or walk_size <= 0:
        raise ValueError("Both step_size and walk_size should be positive integers.")

    return step_size, walk_size
```


```python
# test your code for proper functioning here

print(get_user_inputs(3, 10))
print(get_user_inputs(10, 10))

# test code for error handling here
# what errors should we test for?
```

<pre class="output-block">(3, 10)
(10, 10)
</pre>

Example of a use-case for handling exceptions in your own code:

You have written a function that reads in a file and processes it, but it requires that certain things in the file are numerical. It works on your own data that you know is nice and clean, but you want your code to also work on you colleague's data. So you might add a `try`/`except` block to catch `ValueError` if the data is not numerical. Then you might `try` to convert the data to a float, and if that fails, you might `except` and print a message to the user that the data is not numerical.

### Controlling behavior with break and continue

Sometimes you might want to exit a loop early or you might want to skip the rest of the code and start the next iteration. The `break` and `continue` statements are used for such finer grained control over your loops. The `break` statement will exit the innermost `for` or `while` loop it is in. In the below example, we use a while loop to find the first number that is divisible by 7.


```python
num = 22
while True: # this would run forever if it weren't for the break statement
    num += 1
    if num % 7 == 0:
        print(f"{num} is divisible by 7")
        break
    else:
        print(f"{num} is not divisible by 7")
```

<pre class="output-block">23 is not divisible by 7
24 is not divisible by 7
25 is not divisible by 7
26 is not divisible by 7
27 is not divisible by 7
28 is divisible by 7
</pre>

`continue` is used to skip the rest of the code in the loop and start the next iteration. In the below example, we use a for loop to print all the numbers from 1 to 10 that are not divisible by 3.


```python
for i in range(1, 12):
    # if it is divisible by 3, skip the rest of the loop (the print statement)
    if i % 3 == 0:
        continue
    print(i)
```

<pre class="output-block">1
2
4
5
7
8
10
11
</pre>

Both `break` and `continue` can be used in loops made with `for` or `while`.

>**Exercise:** Work with a neighbor to complete the code below. It is intended to be a simple guessing game. The computer will pick a random number between 1 and 10 and ask the user to input a guess. **While the user's guess is wrong**, the computer will tell the user if the guess is high or low. The break statement should be used to exit the loop when the user guesses correctly.  


```python

import random

def guessing_game():
    # generate a random number betwee 1 and 10
    number = random.randint(1, 10)
    print("I'm thinking of a number between 1 and 10.")

    # this begins the while loop
    # note that the loop has no end condition. It relies on the break statement!
    while True:
        # ask the user to guess the number
        # note that input() always returns a string
        guess = input("Take a guess: ")
        # try to convert the input to an integer
        try:
            guess = int(guess)
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue
        # your code here
        # start with an else statement
        # if the guess is correct, print a message and break the loop
        # if the guess is too low, print a message
        # if the guess is too high, print a message
        else:
            if guess == number:
                print(f"Good job! The number was {number}.")
                break
            elif guess < number:
                print("Your guess is too low.")
            else:
                print("Your guess is too high.")
```


```python
# check your code
guessing_game()
```

<pre class="output-block">I'm thinking of a number between 1 and 10.
</pre>

<pre class="output-block">---------------------------------------------------------------------------
StdinNotImplementedError                  Traceback (most recent call last)
Cell In[16], line 2
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1 # check your code
----> 2 guessing_game()

Cell In[15], line 13, in guessing_game()
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;8 # this begins the while loop
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;9 # note that the loop has no end condition. It relies on the break statement!
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;10 while True:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;11     # ask the user to guess the number
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;12     # note that input() always returns a string
---> 13     guess = input("Take a guess: ")
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;14     # try to convert the input to an integer
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;15     try:

File C:\bin\miniforge3\Lib\site-packages\ipykernel\kernelbase.py:1281, in Kernel.raw_input(self, prompt)
&nbsp;&nbsp;&nbsp;1279 if not self._allow_stdin:
&nbsp;&nbsp;&nbsp;1280     msg = "raw_input was called, but this frontend does not support input requests."
-> 1281     raise StdinNotImplementedError(msg)
&nbsp;&nbsp;&nbsp;1282 return self._input_request(
&nbsp;&nbsp;&nbsp;1283     str(prompt),
&nbsp;&nbsp;&nbsp;1284     self._parent_ident["shell"],
&nbsp;&nbsp;&nbsp;1285     self.get_parent("shell"),
&nbsp;&nbsp;&nbsp;1286     password=False,
&nbsp;&nbsp;&nbsp;1287 )

StdinNotImplementedError: raw_input was called, but this frontend does not support input requests.
</pre>

## Working with dates and times

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

# Pass by reference vs. pass by copy

Now that we've encountered python objects (strings, numbers, booleans), and a few different data structures (lists, dictionaries, pandas Series and DataFrames), it's important to understand how they are stored in memory. In Python, there are two ways that objects can be passed around: **by reference** and **by copy**. 

When an object is passed by reference, it means that the variable is simply a pointer to the object in memory. If you modify the object, the changes will be reflected in all variables that point to that object. 

When an object is passed by copy, it means that a new object is created in memory and the variable points to that new object. If you modify the object, the changes will not be reflected in the original object. This is the case for strings and tuples.

In general, base python data structures like lists and dictionaries are passed by reference, while pandas objects like Series and DataFrames are passed by copy. Run the code blocks below to see some demonstrations of how reference vs copy can impact your data. 


```python
a = ["my", "list", "of", "words"]
b = a
b[0] = "your"
print(a)
```

<pre class="output-block">['your', 'list', 'of', 'words']
</pre>

In the above code, we create a list `a` and then assign it to `b`. When we modify `b`, we see that `a` is also modified, because both variables point to the same object in memory.


```python
a = ["my", "list", "of", "words"]
b = a[0]
b = "your"
print(a)
```

<pre class="output-block">['my', 'list', 'of', 'words']
</pre>

In the above code, we create a list `a`, and then assign a slice of `a` to `b`. When we modify `b`, we see that `a` is not modified, because creating a slice of a list creates a **shallow copy** of the list. Once the slice is modified, it is a new object in memory that does not affect the original list.


```python
a_series = pd.Series(["my", "list", "of", "words"])
b_series = a_series[:]

# Modify b_series
b_series[0] = "your"

print("a_series:\n", a_series)
print("b_series:\n", b_series)
```

<pre class="output-block">---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[19], line 1
----> 1 a_series = pd.Series(["my", "list", "of", "words"])
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2 b_series = a_series[:]
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4 # Modify b_series

NameError: name 'pd' is not defined
</pre>

In the above code, we do the same thing as before - create a slice of a list and assign it to a new variable. This behaves the same as a list and both `a_series` and `b_series` are modified. 


```python
with pd.option_context("mode.copy_on_write", True):

    a_series = pd.Series(["my", "list", "of", "words"])
    b_series = a_series[:]

    # Modify b_series
    b_series[0] = "your"

    print("a_series:\n", a_series)
    print("b_series:\n", b_series)
```

<pre class="output-block">---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[20], line 1
----> 1 with pd.option_context("mode.copy_on_write", True):
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3     a_series = pd.Series(["my", "list", "of", "words"])
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4     b_series = a_series[:]

NameError: name 'pd' is not defined
</pre>

In the above code, we wrap the entire code block in a `with` statement to ensure that the code is processed with the pandas **Copy-on-Write** behavior. This means that when we modify `b_series`, it does not affect `a_series`, because a new copy of the Series is created in memory. This copy-on-write behavior is specific to pandas and can be toggled on in your scripts and notebooks. It will become standard in a future version of pandas, but for now it is an optional feature.

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

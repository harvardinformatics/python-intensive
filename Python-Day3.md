---
title: "[Workshop] Python intensive, day 3"
description: "More on writing your own functions, debugging strategies, and exception handling in Python."
authors:
    - Lei Ma
    - Tim Sackton
---

# Python intensive, day 3

## Review of Days 1 + 2

Welcome to day 3 of our python intensive course. This is the last day of the "introduction to computer science" part of the course, after which we will move on to the "introduction to data science" part. Let's review what we have learned so far:

1. A computer program is a sequence of instructions that is read from top to bottom and executed by the computer. You need to give it extremely precise instructions. It's helpful to use **pseudocode** to plan our the logic of your program before you apply the **syntax** of your programming language.
2. **Variables** are assigned to data using the `=` operator.
3. **Functions** are blocks of code that are executed when called. You can also think of operators as functions that take arguments on both sides.
4. We learned about various data types, including **integers**, **strings**, and **booleans** and how various operators work with them. Knowing what data type you are working with is very important!
5. **Conditional statements** like `if`, `elif`, `else` allow you to control the flow of the program, skipping code that doesn't need to be executed.
6. **Loops** like `for` and `while` allow you to repeat code multiple times. For while loops, it's important to make sure that it will end by using an update variable. For loops use iterables to repeat code.
7. **Iterables** are objects that can be looped over, like **lists**, **dictionaries**, and **strings**. They are indexed starting at 0 and can be sliced using the `:` operator.
8. **Lists** are a basic data structure that store multiple values. They are indexed by their position in the list.
9. While learning about lists, we learned about methods, which are functions that are attached to objects and can modify that object **in place** or give you information about that object.
10. **Dictionaries** are another type of basic data structure that store key-value pairs. They are indexed by their keys.
11. How to write **functions** of your own and either print the results or return the values.

## Metaprogramming skills and debugging

Today we will learn how to turn functions into programs. So far, we have learned how to create small self-contained functions. But today we will build from these to create a simulation of a random walk. Given the inputs of a step size and boundary size, it will simulate a walk from the middle of a defined (represented by `-`) space until the object runs into a wall. Here's what it might look like to use this function:

```python
random_walk(step_size = 1, walk_size = 10)
```

output:

```jupyter
Starting random walk with boundary size: 10 and step size: 1
-----O----
----O-----
---O------
--O-------
-O--------
--O-------
-O--------
--O-------
-O--------
--O-------
-O--------
O---------
-O--------
O---------
X---------
Reached boundary!
```

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

### Tests

A very helpful approach to debugging - and, indeed, writing code in general - is to have some small input data that you can use to test. Ideally this should be something that runs fast and where you know what the expected output is. While this won't necessarily help you fix problems that cause your code to simply not execute, it can be extremely useful if you are not certain of how to program something, or if your program is running but with unexpected results.

For example, if you have a dataset that you have manually processed, but now want to automate with a Python script or set of scripts, you will very likely want to check your code by running it against a test input that has a known output.

This is particularly important if you are going to use LLMs for debugging, as discussed below. LLMs rarely make syntax errors, but do make logic errors.

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

If you want to then share this code (and the dummy data!) with someone else, you can either send the script to them or you can use a Python package called `reprexpy`, which will format both your code and your output in a way that is easy to post in plain text online or in an email. For more information see the docs for [reprexpy](https://reprexpy.readthedocs.io/en/latest/).  

### Using your IDE's tools

Programmers typically choose a text editor in which to write their code. Oftentimes, these text editors have extra features that aid programmers when coding (*e.g.* colored syntax, parentheses match highlighting, error checking). These text editors with extra featuers are called integrated development environments, or **IDEs**. RStudio is an example of an IDE, and other text editors have become so feature rich that they are essentially IDEs in practice, like [VScode](https://code.visualstudio.com/)

Today, we are working in a Jupyter notebook in Google Colab, which has IDE-like features. There are some features that might be useful for examining your code. For example, you can use the `{x}` button on the left sidebar to examine the variables in your environment. You can also use the `print()` function within blocks of your code to see what is happening at each step.

### Pair programming

**Pair programming** is a technique where two programmers work together on the same code. One person is the "driver" who writes the code, while the other person is the "navigator" who reviews the code as it is written. This can be a very effective way to catch errors early and to learn from each other. Let's practice by working on one component of the random walk function together.

>**Exercise:** Write a function called `display_walk` that takes a walk size and position argument and prints a string of dashes with an 'O' at the position. For example, `display_walk(size = 10, position = 3)` should print `---O------`. If the position is outside the walk size, it should print an 'X' at the end. For example, `display_walk(size = 10, position = 12)` should print `----------X`.
>
> 1. Work together to write out pseudocode for this function. Make sure to check in on any potential logic errors.
> 2. One person should write the code while the other person dictates out the pseudocode.
> **Important** One line in your pseudocode could correspond to one line of code, but that may or may not be the case
> 3. For each line of code, **PAUSE** and both of you should check to make sure it matches the pseudocode.
>
> You are allowed to use LLMs or the internet to look up how to do specific parts of your code, but try not to look up the entire solution.


```python
# Your code here

# Solution using lists
def display_walk(size, position):
    walk = list("-") * size
    if position < size and position >= 0:
        walk[position] = "O"
    elif position >= size:
        walk[size - 1] = "X"
    elif position < 0:
        walk[0] = "X"
    print("".join(walk))

# Solution using string concatenation
def display_walk(size, position):
    if 0 <= position < size:
    # Create a string with 'O' at the specified position
        walk = '-' * position + 'O' + '-' * (size - position - 1)
    elif position < 0:
        # Position is out of bounds, place 'X' at the end
        walk = "X" + '-' * (size - 1)
    else: # position >= size
        # Position is out of bounds, place 'X' at the beginning
        walk = '-' * (size - 1) + "X"
    print(walk)
```


```python
# test your code here
display_walk(10, -1)
display_walk(10, 0)
display_walk(10, 5)
display_walk(10, 9)
display_walk(10, 11)

# Expected output
# X---------
# O---------
# -----O----
# ---------O
# ---------X
```

<pre class="output-block">
X---------
O---------
-----O----
---------O
---------X
</pre>

>**Discussion**: What were some questions that came up while writing this function? Did you get answers to them or are they still unanswered?

## f-strings

One quick string concept to cover before we move on to other topics is **f-strings**. F-strings are a way to format strings in Python. The way they work is to start a string with the keyword `f`, preceding the first quotation mark. Then, whenever you need to insert a variable within the string that has previously been assigned, you surround that variable name with `{}`. Think of `{}` as a carve-out from the string where code is valid again.

They are a way to embed variables into strings. Here's an example:


```python
my_num = 1004210.52049

print(f"my number is: {my_num}. Hooray!")
print(f"twice my number is: {my_num * 2}. Hooray!")
print(f"my original number, {my_num}, did not change")
```

<pre class="output-block">
my number is: 1004210.52049. Hooray!
twice my number is: 2008421.04098. Hooray!
my original number, 1004210.52049, did not change
</pre>

You cannot do f-string formatting with a string that is stored inside a variable. You can only do it with strings that are written directly in the code.

The reason we might use f-strings rather than passing multiple arguments to the `print()` function is that it is easier to read in code form, faster to type, and you can attach formatting to the variables that you are embedding. This formatting does not affect the underlying variable, but rather how it is displayed.

Below are a few examples of how you might format numbers while inside an f-string. You don't have to memorize this syntax or use it yourself, but you will see it in future code and it's good to know what it is.


```python
# rounds to 2 decimal places
print(f"my number is: {my_num:.2f}")

# rounds to nearst whole number
print(f"my number is: {my_num:.0f}")

# adds commas to separate thousands
print(f"my number is: {my_num:,}")

# adds commas to separate thousands and rounds to 2 decimal places
print(f"my number is: {my_num:,.2f}")

# original number
print(my_num)
```

<pre class="output-block">
my number is: 1004210.52
my number is: 1004211
my number is: 1,004,210.52049
my number is: 1,004,210.52
1004210.52049
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


<pre class="output-block">
---------------------------------------------------------------------------

ZeroDivisionError                         Traceback (most recent call last)

Cell In[4], line 1
----&gt; 1 log2fc(0,0)


Cell In[3], line 4, in log2fc(x, y)
      3 def log2fc(x, y):
----&gt; 4     return math.log2(x/y)


ZeroDivisionError: division by zero
</pre>

```python
log2fc(10,0)
```


<pre class="output-block">
---------------------------------------------------------------------------

ZeroDivisionError                         Traceback (most recent call last)

Cell In[5], line 1
----&gt; 1 log2fc(10,0)


Cell In[3], line 4, in log2fc(x, y)
      3 def log2fc(x, y):
----&gt; 4     return math.log2(x/y)


ZeroDivisionError: division by zero
</pre>

```python
log2fc(0,10)
```


<pre class="output-block">
---------------------------------------------------------------------------

ValueError                                Traceback (most recent call last)

Cell In[6], line 1
----&gt; 1 log2fc(0,10)


Cell In[3], line 4, in log2fc(x, y)
      3 def log2fc(x, y):
----&gt; 4     return math.log2(x/y)


ValueError: math domain error
</pre>

```python
log2fc("a", "b")
```


<pre class="output-block">
---------------------------------------------------------------------------

TypeError                                 Traceback (most recent call last)

Cell In[7], line 1
----&gt; 1 log2fc("a", "b")


Cell In[3], line 4, in log2fc(x, y)
      3 def log2fc(x, y):
----&gt; 4     return math.log2(x/y)


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

- Specifying Error Types: You don't need to specify an error type after `except`; if you don't, the except block will catch any error. Normally, this isn't a good idea because you might want to return specific messages or handle particular error types differently.
- Multiple Except Blocks: except statements actually function somewhat like `elif`: you can have many of them, each with a different ErrorType. You can also list multiple error types within a single except statement using parentheses, e.g., `except (KeyError, ValueError):` if you want to catch both errors.
- `else` and `finally` Blocks: You can have an `else` block (which runs only if no errors occur) or a `finally` block (which runs after the try-except regardless of whether an error occurred).

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

<pre class="output-block">
Error: x and y must be numbers
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

<pre class="output-block">
a warning is printed when y is 0
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

>**Exercise**: Work with a neighbor to write the user input portion of our random walk function. The function should take a `step_size` and `walk_size` and check that both inputs are valid. If both inputs are valid, it should return both the `step_size` and `walk_size`.
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

<pre class="output-block">
(3, 10)
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

<pre class="output-block">
23 is not divisible by 7
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

<pre class="output-block">
1
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

<pre class="output-block">
I'm thinking of a number between 1 and 10.
Your guess is too high.
Good job! The number was 1.
</pre>

## Functions to Programs

## Code annotation

In the past couple of sessions, we have learned the building blocks of computer programs. We have just one more concept and activity before you are ready to write your random walk program. That is, **code annotation**. When you begin to write longer functions or scripts, it's important to leave breadcrumbs for yourself (and others) about what your code does. While you can sprinkle `#comments` throughout your program, there are also some standardized ways to do so.

If you are annotating functions, you should use something called a **"docstring"**. This is a string that is the first line of a function and is enclosed in triple quotes. It should describe what the function does, what inputs it takes, and what it returns. Here is an example of a docstring:

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

In contrast, if you are annotating a script, which may be calling many functions, you should use comments. Comments are denoted by a `#` symbol. Here is an example of a commented script:


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

>**Exercise:** Copy and paste your `display_walk` function from above into the cell below. Add a docstring to the function that describes what it does, what inputs it takes, and what it returns. Then, call `help(display_walk)` and see what happens!
>
> If short on time, you can also use LLMs to write your docstring. Usually they do pretty well.


```python

def display_walk(size, position):
    """
    Parameters: size (int) - a positive integer representing the size of the walk
                position (int) - an integer representing the position of the walker
    Displays a walk of size `size` with a walker at position `position`.
    Walkers are represented by 'O' and out of bounds positions are represented by 'X'.
    Unoccupied positions are represented by '-'.
    """
    if 0 <= position < size:
    # Create a string with 'O' at the specified position
        walk = '-' * position + 'O' + '-' * (size - position - 1)
    elif position < 0:
        # Position is out of bounds, place 'X' at the end
        walk = "X" + '-' * (size - 1)
    else: # position >= size
        # Position is out of bounds, place 'X' at the beginning
        walk = '-' * (size - 1) + "X"
    print(walk)

# try calling help on your function
help(display_walk)
```

<pre class="output-block">
Help on function display_walk in module __main__:

display_walk(size, position)
    Parameters: size (int) - a positive integer representing the size of the walk
                position (int) - an integer representing the position of the walker
    Displays a walk of size `size` with a walker at position `position`.
    Walkers are represented by 'O' and out of bounds positions are represented by 'X'.
    Unoccupied positions are represented by '-'.
</pre>

>**Exercise:** For our final activity before writing our program, let's review the topics we have already learned. On a piece of paper or on the white board, draw a concept map of how all the topics connect to each other. It's fine if this only makes sense to you, but you can also work with others to see how they connect the topics. You may find this concept map as a helpful reference when you are writing your random walk program.
>
>Topics/Concepts to include on the drawing:
>
>* Conditionals (if/else)
>* Loops
>    * For loops
>    * While loops
>* Strings
>* Numerical values
>* Booleans
>* Lists
>* Dictionaries
>* Exceptions
>* Functions
>* Methods
>* Pseudocode
>* Control flow
>* Debugging
>
>Feel free to add more to your map!

## Random walk program

For this exercise, you already know the concepts needed to create a random walk. Everyone will likely write a slightly different program so we aren't going to give a whole lot of structure because we want you to explore what is possible. There is just one thing that you will all probably need, which is to import the `random` module. This module has a function called `random.choice()` which will randomly select an element from a list. See below for an example:


```python
import random

print(random.choice(["heads", "tails"]))
```

<pre class="output-block">
heads
</pre>

Write your code below. If you get stuck, check out your concept map, work with a neighbor, or review the topics we learned today. And of course, remember to use your debugging skills!


```python
import random

def get_user_inputs(step_size, walk_size):
    """
    Validate the user inputs for step size and walk size.
    If the inputs are valid, return them.
    """
    if not isinstance(step_size, int) or not isinstance(walk_size, int):
        raise ValueError("Both step_size and walk_size should be integers.")

    if step_size <= 0 or walk_size <= 0:
        raise ValueError("Both step_size and walk_size should be positive integers.")

    return step_size, walk_size

def display_walk(position, walk_size, boundary_symbol='X', walker_symbol='O', open_space='-'):
    """
    Display the current position of the walker on the walk line.
    Input:
    - position: the current position of the walker
    - walk_size: the size of the walk line
    - boundary_symbol: the symbol to represent reaching the boundary
    - walker_symbol: the symbol to represent the walker
    - open_space: the symbol to represent an open space
    Return: None (but print the walk line)
    """
    # walk line represented by a list of string symbols
    walk_line = [open_space] * walk_size
    # if statement to check if the position is within the walk line
    if 0 <= position < walk_size:
        walk_line[position] = walker_symbol
    # if the position is outside the walk line, put boundary symbol at the edge
    else:
        symbol_position = 0 if position < 0 else walk_size - 1
        walk_line[symbol_position] = boundary_symbol
    # joins the symbols to create a string and prints it
    print("".join(walk_line))

def random_walk(step_size, walk_size):
    """
    Simulate a random walk on a line with a given step size and walk size.
    Input:
    - step_size: the size of each step in the walk
    - walk_size: the size of the walk line
    Return: None (but print the walk line at each step and when the boundary is reached)
    """
    position = walk_size // 2  # Start from the middle of the walk line
    print(f"Starting random walk with boundary size: {walk_size} and step size: {step_size}")

    # loop walk until boundary is reached
    while 0 <= position < walk_size:
        # display current position
        display_walk(position, walk_size)
        # generate random direction
        direction = random.choice([-1, 1])
        # update current position
        position += direction * step_size

    # calls the display walk function at the end one more time
    display_walk(position, walk_size)
    print("Reached boundary!")

# runs random walk. but calls get_user_inputs to validate inputs first
def run_random_walk(step_size, walk_size):
    try:
        step_size, walk_size = get_user_inputs(step_size, walk_size)
        random_walk(step_size, walk_size)
    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```


```python
run_random_walk(2, 10)
```

<pre class="output-block">
Starting random walk with boundary size: 10 and step size: 2
-----O----
-------O--
-----O----
-------O--
---------O
-------O--
-----O----
-------O--
---------O
---------X
Reached boundary!
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

</style>

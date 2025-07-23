---
title: "[Workshop] Python intensive, day 3"
description: "More on writing your own functions, debugging strategies, and exception handling in Python."
authors:
    - Lei Ma
    - Tim Sackton
---

## Review of Day 1 + 2

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

## Functions to Programs

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

!!! Note
    If you are reading the completed solution to this exercise, you will notice extra code that **raise exceptions** in **try ... except** blocks. To learn more about how to use exceptions, check out our companion notebook "Python Healthy Habits" which covers some more advanced function writing. 


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

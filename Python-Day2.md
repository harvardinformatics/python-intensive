---
title: "[Workshop] Python intensive, day 2"
description: "Introduction to Python data structures, including lists and dictionaries, loops, libraries, and writing functions."
authors:
    - Gregg Thomas
    - Danielle Khost
---

## Introduction - Day 2

Welcome (back) to the Harvard Informatics Python workshop. This is day two of six, where we aim to give a whirlwind, yet thorough, introduction programming concepts, the Python programming language, and how to use Python and some popular libaries to facilitate data analyses.

Yesterday, we learned some foundational programming concepts and how they are implemented in Python. Specifically, we learned about:

1.   How computers need every single step given to them in order to complete a task with programming. This requires the programmer to conceptualize a problem at a high level, perhaps with **pseudocode**, and then break down that problem in every single step.
2.   Data can be stored and manipulated in a program by assigning it to an internal **variable** name with the assignment operator (`=`).
3.   **Functions** are blocks of code that perform a specific task and can be "looked up" from another program - like another recipe in a recipe book. Functions require input in the form of **arguments** and **return** output.
4.   **Operators** are functions that perform universal tasks, such as `+` for the addition of integers.
5.   Functions and operators may work on specific **data types**, such as **strings** or **integers**. It is important to remember what data type your function expects.
6.   **Boolean** (`True` or `False`) is a data type that allows programmers to express and evaluate complex logical statements. Booleans have operators that work on them, such as `and`, `or`, and `not`.
7.   **Conditional** (`if`, `elif`, `else`) statements allow programmers to execute certain blocks of code depending on the state of the data in their program by testing logical conditions. Data is compared with **comparison operators** such as `>`, `==`, or `in`.
8.   **Loops** (`while`, `for`) allow sets of instructions to be automatically repeated depending on the conditions of the program.

Today we will build on this by learning about **iterable data structures**, which will enhance what we can do with `for` loops, and we will learn to write our own functions.



### Installing/running this notebook

This workshop exists as a **Jupyter notebook**. You can participate in this workshop by using this notebook by simply uploading it to Google Colab. Go to  https://colab.research.google.com/ to do so. That's it! This is the recommended way for participating in this workshop. Skip the bleo instructions if you will be using Google Colab.

---
**See above for the recommended way to participate in this workshop. Only follow these instructions if Google Colab isn't working**

If for some reason Google Colab isn't working, or you prefer to run this locally, you will need to install python, anaconda, and the necessary libraries. You will have to follow these steps to do so. Note that some steps are only meant for specific operating systems.

0. If you are on Windows, [install WSL :octicons-link-external-24:](https://learn.microsoft.com/en-us/windows/wsl/install){:target="_blank"}. Once WSL is installed, you'll have a Linux terminal available to you in Windows. You can open this terminal by typing "wsl" in the search bar and clicking the app that appears. You'll also find your Linux distribution as a mounted drive in your file explorer.

1. Install mamba, a package manager using the command line - Terminal for Mac or WSL for Windows.

    1.1. For Mac, if you already have brew installed, install mamba using `brew install miniforge` and initialize it using `conda init zsh`. Then restart your terminal. If you don't have homebrew (i.e. the brew command doesn't exist), install brew first using `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
    
    1.2. For Windows, download the Linux (x86_64) installer from the miniforge repository [here :octicons-link-external-24:](https://github.com/conda-forge/miniforge){:target="_blank"} and install with `bash Miniforge3-Linux-x86_64.sh`.

2. Create a new environment using mamba with `mamba create -n pyworkshop numpy pandas matplotlib seaborn jupyter` and activate it with `conda activate pyworkshop`.

3. You can now run the jupyter notebook by typing `jupyter notebook` in the terminal. This will open a browser window with the jupyter notebook interface. You can navigate to the folder where you saved this notebook and open it.

4. Alternatively, install [VSCode :octicons-link-external-24:](https://code.visualstudio.com/){:target="_blank"} and the Python extension. Then open this notebook in VSCode and run it with the kernel that belongs to the pyworkshop environment. [How to guide here :octicons-link-external-24:](https://code.visualstudio.com/docs/datascience/jupyter-notebooks){:target="_blank"}

---

### Jokes

To re-iterate some of the concepts we talked about at the beginning of yesterday's workshop, let's start with a joke about computer programmers.

Sam asks their computer programmer spouse to go get some groceries. Sam tells him, "Please go to the store to get some groceries. Buy a loaf of bread. If they have eggs, get a dozen." The spouse comes back with 13 loaves of bread. This joke is funny if you understand how computer programs evaluate commands.

Below is some pseudocode that represents what the computer programmer did.

```
go to the store

loaf_of_bread = 1
if eggs:
    loaf_of_bread += 12
```

This joke illustrates that what may make sense in natural language does not immediately translate to computer language. And therefore we have to be really specific, giving every instruction even, when we're programming.

## Iterables

We left off yesterday talking about `for` loops. `for` loops work by performing a set of instructions (block of code) on every item in a **sequence of items**. We talked about looping over the characters in a string:


```python
my_string = "Hello!"

for current_character in my_string:
  print(current_character)
```

<pre class="output-block">
H
e
l
l
o
!
</pre>

This works because, in Python, strings are **iterable** objects. Iterables are those objects that can be broken up into individual **elements**, and can subsequently be looped over using `for`. In this case, for the string, each **character** is an individual **element**.

Integers, floating point numbers, and boolean `True` and `False` are **not iterable objects**. They are not made up of a sequence or collection of elements, but rather are single pieces of information.

This is explained rather clearly if you try to loop over an integer:


```python
for x in 1048:
  print(x)
print("Done.")
```


<pre class="output-block">
---------------------------------------------------------------------------

TypeError                                 Traceback (most recent call last)

&lt;ipython-input-2-50b9ec0fcae9&gt; in &lt;cell line: 1&gt;()
----&gt; 1 for x in 1048:
      2   print(x)
      3 print("Done.")


TypeError: 'int' object is not iterable
</pre>

### Indexing strings

Because strings are **iterable**, meaning they are made up of smaller **elements**, it is possible to access these elements one at a time. This is called **indexing**.

In Python, each character of a string is assigned a number based on its location within the string:

```
HELLO
|||||
01234
```

Notice that the first number is 0, not 1. Python in general uses **0-based indexing**, simply meaning that counts start from 0.

Syntactically, individual characters within a string are accessed within a program by giving the string (possibly raw, but usually as a variable name) followed by square brackets `[]` with the index contained in them:


```python
my_string = "hello world!"
print(my_string[2]) # Prints the third character because of 0-based indexing!

print("---")

first_char = my_string[0]
print(first_char)
```

<pre class="output-block">
l
---
h
</pre>

Strings can also be indexed in reverse by providing a negative index:


```python
my_string = "hello world!"
print(my_string[-2])
```

<pre class="output-block">
d
</pre>

Since there is no -0, reverse string indexing starts from -1.

Ok, well how does this relate to `for` loops? Well, perhaps you have a string and you want to run some code for each letter in the string, but instead of the character itself you were interested in the **index of that character**.

Using a couple of functions, we can **loop over a string by index**:


```python
my_string = "hello world!"
my_string_length = len(my_string)

for cur_index in range(my_string_length):
  print(cur_index, my_string[cur_index])
```

<pre class="output-block">
0 h
1 e
2 l
3 l
4 o
5  
6 w
7 o
8 r
9 l
10 d
11 !
</pre>

We learned about the `len()` function yesterday. It takes as input a string argument and returns the number of characters in that string.

`range()` is another function that returns **an object containing the indices**. The `for` loop directly takes that object and loops over it, assigning `cur_index` the value of the index for the current iteration of the loop. Inside the loop, we've printed out both the index and the corresponding character in the string using string indexing with `[]`.

> **Exercise**: Store a string in a variable. Print out the characters of the string in reverse. No palindromes allowed! This will require you to use a `for` loop and reverse indexing.
>
> **BONUS**: Instead of printing each character out in reverse one at a time, print the whole string in reverse at once. *Hint: remember the string concatenation operator `+`*.


```python
# Your code here: reverse a string

my_string = "stressed"
my_rev_string = "" # For bonus

for str_ind in range(len(my_string)):
  rev_ind = str_ind + 1
  rev_char = my_string[-rev_ind]
  my_rev_string += rev_char # For bonus
  print(rev_char)

print(my_rev_string) # For bonus

## Alternate bonus solution without indexing

my_rev_string = ""
for char in my_string:
  my_rev_string = char + my_rev_string
print(my_rev_string)

```

<pre class="output-block">
d
e
s
s
e
r
t
s
desserts
desserts
</pre>

### Slicing strings

In addition to indexing to retrieve one character from a string at a time, you can also **slice** strings to get chunks of them.

Slicing is again done by giving the name of the string followed by square brackets `[]`. But this time, instead of a single number in the brackets, you provide two numbers, a start index and an end index, separated by a colon `:`.

For example, to get the 2nd to 5th characters from a string:


```python
my_string = "hello_world!"
print(my_string[1:6])
```

<pre class="output-block">
ello_
</pre>

Remember, Python strings a **0-based indexed**, so to get the second character, you give the index `1`, since counting starts at 0.

Also, the second index in a slice (the one after `:`) is **non-inclusive**. This means that even though we've given `6`, it does not retrieve the 7th character (6th index). Think of it as saying, "Give me this string from this index *up to* this index."

There are some other shortcuts:

*   If the index before the colon `:` is excluded, it will start at the beginning of the string.
*   If the index after the colon `:` is excluded, it will return all characters from the start index to the end of the string.
*   A second colon `:` and number N can be added. This indicates to get every Nth character from the first index to the second.



```python
print(my_string[:6])     # Gets every character from the beginning up to but not including the 6th character
print(my_string[3:])     # Gets every character from the 4th character to the end of the string
print(my_string[1:6:2])  # Gets every second (every other) character from the 2nd to 5th character
```

<pre class="output-block">
hello_
lo_world!
el_
wol
</pre>

String slicing also works in reverse with negative indices:


```python
print(my_string[:-3])   # Gets every character from the beginning to the third from last
print(my_string[2:-4])  # Gets every character from the 3rd to the 4th from last
```

<pre class="output-block">
hello_wor
llo_wo
</pre>

Regardless of the presence of negative indices, the characters are retrieved left to right. This means if you give it non-sensical ranges where the first number is larger than the second number, it will return nothing. The exception is if you give it a negative increment after the second colon:


```python
print(my_string[2:1])    # Fails because the starting index is larger than the ending index
print(my_string[-3:-6])  # Fails for the same reason
print(my_string[6:1:-2]) # Gets every other charcater in reverse from the 7th to the 2nd
print("Done.")
```

<pre class="output-block">


wol
Done.
</pre>

Let's break down the last one. We start at index 6, which is the 7th character `w`. We proceed at an increment of -2, meaning we move left. We step over `_`, retrieve `o`, step over the second `l`, retrieve the first `l`, and step over the `e`. `e` is the character at the first index so we stop.

> **Exercise**: Reverse the string you used from your previous exercise using slicing only. This is tricky, *but should only take one line of code to do using slicing* (and then possibly another line to print the result). Remember the shortcuts for the beginning and end of strings and the negative steps to go backwards when slicing.


```python
# Your code here: reverse a string with slicing only
my_string = "stressed"
print(my_string[::-1])
```

<pre class="output-block">
desserts
</pre>

### Strings are immutable

An important note. Though we can access individual characters within a string with **indexing**, we cannot change individual parts of a string. In other words, strings are **immutable**.


```python
my_string = "hello_world!"
print(my_string[1])
my_string[1] = "a" # This is not permitted because strings are immutable!
```

<pre class="output-block">
e



---------------------------------------------------------------------------

TypeError                                 Traceback (most recent call last)

&lt;ipython-input-38-5a964ad8245f&gt; in &lt;cell line: 3&gt;()
      1 my_string = "hello_world!"
      2 print(my_string[1])
----&gt; 3 my_string[1] = "a" # This is not permitted because strings are immutable!


TypeError: 'str' object does not support item assignment
</pre>

So, strings are **iterable** but **immutable**.

### Lists

Up to now, we've dealt with individual data types, **integers** and **strings**. However, to really scale up the power of our programming in order to manipulate and analyize a lot of data, we'll want to group lots of strings and/or integers together and perform operations on them in a loop or all at once. For this, programming languages typically have higher-order **data structures** in which individual instances of other data types can be stored, organized, and accessed.

For Python, the most adaptable data structure is the **list**. Lists are exactly what they sound like they are: lists of other objects, grouped together in a single object.

#### List properties

*   Lists are **iterable**, meaning we can use a `for` loop to go over each individual item one at a time and perform computations.
*   Lists are **indexed** which means, like strings, individual elements of a list can be accessed by an integer value based on their ordering in the list. Lists can also be **sliced** by index like strings.
*   Lists are **mutable**, unlike strings, meaning that they can be changed by index on the fly. But be careful doing this while looping over the list! This can have unexpected consequences.
*   Lists can contain mixed data types.

Lists are defined, confusingly, also with square brackets `[]`, and individual items in the list are separated by a comma `,`.


```python
my_list = [1, 2, 3, 4, 5]
print(my_list)
print(my_list[1])

print("---")

my_list2 = ["hello", -12, "world", 985, "adshgadk"]
print(my_list2[2])
print(my_list2[::-1])
```

<pre class="output-block">
[1, 2, 3, 4, 5]
2
---
world
['adshgadk', 985, 'world', -12, 'hello']
</pre>

> **Exercise**: Use a `for` loop to iterate over a list of numbers. At the end of the loop print out the largest number in the list (`list_max`), the smallest number in the list (`list_min`), the sum of all the numbers in the list (`list_sum`), and the average of the list (`list_avg`). Do not use any functions to achieve this. Some of these will require conditional checks (`if` statements) to achieve!
>
> *Consider: What will the starting values of these variables need to be?*
>
> *Hint: Calculating the average will also require you to count the number of items in the list (`list_tally`).*
>
> *Hint: Break this down into smaller problems. First do one thing (like the sum or the tally), then add code for the others one at a time.*


```python
my_list = [1, 2, 3, 4, 5] # Change to any list of numbers you like

# Your code here

# Initialize these variables with sensible values
list_tally = 0
list_sum = 0
list_max = 0
list_min = 9999

for num in my_list:
  # Add code for the for loop here
  list_tally += 1
  list_sum += num

  if num > list_max:
    list_max = num

  if num < list_min:
    list_min = num

list_avg = list_sum / list_tally

print("There are", list_tally, "numbers in the list.")
print("The largest number is:", list_max)
print("The smallest number is:", list_min)
print("The sum of all the numbers is:", list_sum)
print("The average of the numbers is:", list_avg)
```

<pre class="output-block">
There are 5 numbers in the list.
The largest number is: 5
The smallest number is: 1
The sum of all the numbers is: 15
The average of the numbers is: 3.0
</pre>

#### List functions

Just like there are functions and operators for integers and strings, there are also functions and operators for lists.

In fact...


```python
print(len(my_list))
print(max(my_list))
print(min(my_list))
print(sum(my_list))
```

<pre class="output-block">
5
5
1
15
</pre>

Sorry! But you can see here why functions are so nice. We've compacted all that code down to four lines.

Notice that there is no built-in mean() function. There are external libraries that have mean() functions, but more on those later.

> **Exercise**: Calculate the average of your list using the functions provided above. This should only require one line of code (and potentially a `print()` statement).


```python
# Your code here
print(sum(my_list) / len(my_list))
```

<pre class="output-block">
3.0
</pre>

Also, recall lists can contain **mixed data types**. Again, remembering your data types is important because some functions may expect a list with only integers, or a list with only strings.


```python
my_mixed_list = [1, 2, "hello", 3, 4, 5]
print(sum(my_mixed_list))
```


<pre class="output-block">
---------------------------------------------------------------------------

TypeError                                 Traceback (most recent call last)

&lt;ipython-input-48-827a549aa0a9&gt; in &lt;cell line: 2&gt;()
      1 my_mixed_list = [1, 2, "hello", 3, 4, 5]
----&gt; 2 print(sum(my_mixed_list))


TypeError: unsupported operand type(s) for +: 'int' and 'str'
</pre>

Internally, `sum()` is probably doing exactly what we did above with the `for` loop, adding each number in the list to a variable with `+=`. However, when it comes to the third element of the list, `"hello"`, it is trying to add a string to an integer and we run into a data type error for the `+` operator.

#### List inclusion with `in`

As with **strings** and other **iterables**, the `in` operator works on lists:


```python
my_string_list = ["with", "cat", "like", "tread"]
print("cat" in my_string_list)
```

<pre class="output-block">
True
</pre>

> **Exercise**: Use if statements to find Waldo.
>
> **BONUS**: If Waldo isn't in any of these places, print out a message saying so. *Hint: use a boolean to flag when Waldo is found*


```python
beach_tourists=["Alice","Mason","Emma","Liam","Olivia","Walden","Ethan","Sophia","Oliver","Ava","Mia","William","Logan","Lucas","Charlotte","Amelia","Harper","James"]
music_festival_attendees=["Jackson","Sophia","Aiden","Isabella","Lucas","Noah","Levi","Benjamin","Elijah","Mason","Elena","Eliana","Mateo","Jack","Luna","Eleanor","Ezra","Willow","Henry"]
history_class_students=["Emily","James","Wally","Ella","Jacob","Amelia","Michael","Evelyn","Alexander","Avery","Mila","Aria","Ella","Layla","Scarlett","Grace","Wyatt","Ellie","Paisley","Daniel"]
office_building_employees=["Walter","Charlotte","Alexander","Scarlett","Michael","Victoria","Samuel","Aubrey","Olive","Nathan","Camila","Gabriel","Isaac","Waldo","Savannah","Gabriella","Nora","Chloe","Zoe","Stella","Riley"]
marathon_participants=["Daniel","Harper","Henry","Grace","Sebastian","Hannah","Victoria","Archer","Aurora","Brooklyn","Parker","Elias","Adeline","Julia","David","Liam","Josie","Carter","Jaxon"]

# Your code here to determine which location Waldo is in (if any!)

waldo_found = False

if "Waldo" in beach_tourists:
  print("Waldo is at the beach!")
  waldo_found = True

if "Waldo" in music_festival_attendees:
  print("Waldo is at the music festival!")
  waldo_found = True

if "Waldo" in history_class_students:
  print("Waldo is in class!")
  waldo_found = True

if "Waldo" in office_building_employees:
  print("Waldo is at the office!")
  waldo_found = True

if "Waldo" in marathon_participants:
  print("Waldo is running a marathon!")
  waldo_found = True

if not waldo_found:
  print("Waldo isn't in any of these places!")
```

<pre class="output-block">
Waldo is at the office!
</pre>

#### List concatenation with `+`

Just like with strings, the concatenation `+` operator works on lists to combine them:


```python
my_list1 = [1,2,3]
my_list2 = [4,5,6]

print(my_list1 + my_list2)
```

<pre class="output-block">
[1, 2, 3, 4, 5, 6]
</pre>

> **Exercise**: Use list concatenation with `+` to more succinctly determine if Waldo is at one of the locations above. Note that we won't be able to tell *which* location he is in with this method.


```python
# Your code here to concatenate lists and check if Waldo is in any
all_names = beach_tourists + music_festival_attendees + history_class_students + office_building_employees + marathon_participants

if "Waldo" in all_names:
  print("Waldo is in one of these locations!")
else:
  print("Waldo is NOT in any of these locations!")
```

While this is a much shorter bit of code, it is telling us less specific information.

#### Nested lists

Lists are an extremely open and flexible data structure. They can contain any type of data, mixed data types, and even other data structures, including other lists! In other words, you can have a list of lists, or a **nested list**:


```python
list_of_lists = [ [1,2,3], [4,5,6] ]
print(list_of_lists)
print("---")

# OR #

my_list1 = [1,2,3]
my_list2 = [4,5,6]

list_of_lists = [ my_list1, my_list2 ]
print(list_of_lists)
```

<pre class="output-block">
[[1, 2, 3], [4, 5, 6]]
---
[[1, 2, 3], [4, 5, 6]]
</pre>

Note that this is inherently different than when concatenated the two lists above. The result of concatenation was a single list of integers. Here we have a single list of lists (of integers - yes this can get confusing).

This also affects how you loop over the elements in the lists:


```python
my_list1 = [1,2,3]
my_list2 = [4,5,6]

concatenated_list = my_list1 + my_list2
list_of_lists = [ my_list1, my_list2 ]

for element in concatenated_list:
  print(element)

print("---")

for element in list_of_lists:
  print(element)
```

<pre class="output-block">
1
2
3
4
5
6
---
[1, 2, 3]
[4, 5, 6]
</pre>

> **Exercise**: Use **nested lists** to find Waldo. Again, using this method we won't be able to determine the name of the location where Waldo is, but we can tell if he is in any of the locations.
>
> **BONUS**: Similar to before, also print a message if Waldo isn't in any of these locations (using a boolean flag).


```python
beach_tourists=["Alice","Mason","Emma","Liam","Olivia","Walden","Ethan","Sophia","Oliver","Ava","Mia","William","Logan","Lucas","Charlotte","Amelia","Harper","James"]
music_festival_attendees=["Jackson","Sophia","Aiden","Isabella","Lucas","Noah","Levi","Benjamin","Elijah","Mason","Elena","Eliana","Mateo","Jack","Luna","Eleanor","Ezra","Willow","Henry"]
history_class_students=["Emily","James","Wally","Ella","Jacob","Amelia","Michael","Evelyn","Alexander","Avery","Mila","Aria","Ella","Layla","Scarlett","Grace","Wyatt","Ellie","Paisley","Daniel"]
office_building_employees=["Walter","Charlotte","Alexander","Scarlett","Michael","Victoria","Samuel","Aubrey","Olive","Nathan","Camila","Gabriel","Isaac","Waldo","Savannah","Gabriella","Nora","Chloe","Zoe","Stella","Riley"]
marathon_participants=["Daniel","Harper","Henry","Grace","Sebastian","Hannah","Victoria","Archer","Aurora","Brooklyn","Parker","Elias","Adeline","Julia","David","Liam","Josie","Carter","Jaxon"]

# Your code here to determine if Waldo is in any of these locations with a nested list

all_names = [ beach_tourists, music_festival_attendees, history_class_students, office_building_employees, marathon_participants ]
waldo_found = False

for location_list in all_names:
  if "Waldo" in location_list:
    print("Waldo is in one of these locations!")
    waldo_found = True

if not waldo_found:
  print("Waldo is NOT in any of these locations!")
```

<pre class="output-block">
Waldo is in one of these locations!
</pre>

##### Indexing nested lists

A single list can be indexed in much the same way as a string, e.g. `my_list[1]` will return the second element of the list. However, it can be difficult to grasp how nested lists are indexed. This is done by adding another set of square brackets `[]` on to the end of the indexed outer list:


```python
my_list1 = [1,2,3]
my_list2 = [4,5,6]

list_of_lists = [ my_list1, my_list2 ]

print("All lists:                           ", list_of_lists)
print("The second list:                     ", list_of_lists[1])
print("The third element of the second list:", list_of_lists[1][2])
```

<pre class="output-block">
All lists:                            [[1, 2, 3], [4, 5, 6]]
The second list:                      [4, 5, 6]
The third element of the second list: 6
</pre>

In a way, nested lists can be thought of as higher-order data structures. In this case, with just a single level, it could be thought of as a matrix or a table, so the index `list_of_lists[1][2]` is like saying, "Give me the data in the 3rd column of the 2nd row." This can be broken up to be more easily understood:


```python
my_list1 = [1,2,3]
my_list2 = [4,5,6]

list_of_lists = [ my_list1, my_list2 ]
second_row = list_of_lists[1]
second_row_third_col = second_row[2]

print("All lists:                           ", list_of_lists)
print("The second list:                     ", second_row)
print("The third element of the second list:", second_row_third_col)
```

<pre class="output-block">
All lists:                            [[1, 2, 3], [4, 5, 6]]
The second list:                      [4, 5, 6]
The third element of the second list: 6
</pre>

#### Nested loops

Since lists are **iterable**, nested lists of course imply the existence of **nested loops**.


```python
my_list1 = [1,2,3]
my_list2 = [4,5,6]

list_of_lists = [ my_list1, my_list2 ]

for outer_list in list_of_lists:
  print(outer_list);
  for inner_num in outer_list:
    print(inner_num)
  print("---")
```

<pre class="output-block">
[1, 2, 3]
1
2
3
---
[4, 5, 6]
4
5
6
---
</pre>

> **Exercise**: Using your nested list of names in each location from above, find the position of Waldo's name, or its **index** in any of the lists. 
>
> *Hint: remember the `range()` function, which allows us to loop over the indices of an iterable object (like a list).*
>
> **BONUS**: Edit your code to find the **index** of any name that starts with "Wal". *Hint: This will require both list and string operations.*


```python
## Your code here to find the index of Waldo's name

for location_list in all_names:
  for name_index in range(len(location_list)):
    if location_list[name_index] == "Waldo":
      print("Waldo's index in one of the lists is:", name_index, "!")

    # Bonus solution
    if "Wal" in location_list[name_index]:
      print("A name starting with 'Wal' is at index", name_index, "in one of the lists!")
```

<pre class="output-block">
A name starting with 'Wal' is at index 5 in one of the lists!
A name starting with 'Wal' is at index 2 in one of the lists!
A name starting with 'Wal' is at index 0 in one of the lists!
Waldo's index in one of the lists is: 13 !
A name starting with 'Wal' is at index 13 in one of the lists!
</pre>

#### List **methods**

We're going to introduce **methods** in the context of lists, but methods are available for other data types as well (e.g. strings).

Briefly, **methods** are just like functions in that they are blocks of code stored somewhere on your computer that are looked up and run when they are called. Calling them is done slightly differently though:



```
my_list.a_method()
```

Notice the difference with functions, where we might type something like `a_function(my_list)`. For functions we would say we are **passing** the list to the function as an argument.

Methods, on the other hand, are called directly on the object with the dot `.` **operator** (officially called the attribute access operator, but we don't usually call it that).

Here is a simple **method** being used on a list called `.sort()`:



```python
my_list = [5, 8, 3, 6, 1]
print("unsorted:", my_list)
my_list.sort()
print("sorted:", my_list)
```

<pre class="output-block">
unsorted: [5, 8, 3, 6, 1]
sorted: [1, 3, 5, 6, 8]
</pre>

What else do you notice about this that is different about using a function?

In this case, the method works **in place**. That means that it modifies the object directly, rather than returning a new object.

There are also methods that **return** objects. Unfortunately, there is no obvious way to tell which methods work in place and which return objects.

Interestingly, there is also a function to sort a list, called `sorted()`, which we can use to easily highlight the difference between an in place method and a function:


```python
my_list = [5, 8, 3, 6, 1]

print("unsorted:", my_list)
my_sorted_list = sorted(my_list)
print("original still unsorted:", my_list)
print("sorted new list:" , my_sorted_list)

print("---")

my_sorted_list_or_not = my_list.sort()
print("in place method doesn't return anything:", my_sorted_list_or_not)
print("but we've still sorted the original list:", my_list)
```

<pre class="output-block">
unsorted: [5, 8, 3, 6, 1]
original still unsorted: [5, 8, 3, 6, 1]
sorted new list: [1, 3, 5, 6, 8]
---
in place method doesn't return anything: None
but we've still sorted the oritinal list: [1, 3, 5, 6, 8]
</pre>

Methods can also take arguments in addition to the object they are being called on. This is done just like with functions, with the argument going in the parentheses:


```python
my_list = [5, 8, 3, 6, 1]
print("unsorted:", my_list)
my_list.sort()
print("sorted:", my_list)
my_list.sort(reverse=True)
print("reverse sorted:", my_list)
```

<pre class="output-block">
unsorted: [5, 8, 3, 6, 1]
sorted: [1, 3, 5, 6, 8]
reverse sorted: [8, 6, 5, 3, 1]
</pre>

#### In place methods

Here are a few examples of in place list methods, that is ones that directly manipulate the list rather than returning an object.

1.   `.append(x)` : operates on a list to add the object `x` to the end of the list


```python
my_list = [1, 2, 3, 4]
print("original:", my_list)
print("---")
to_add = 5
my_list.append(to_add)
print("appended:", my_list)
```

<pre class="output-block">
original: [1, 2, 3, 4]
---
appended: [1, 2, 3, 4, 5]
</pre>

2.  `.remove(x)` : removes the first occurrence of the passed object `x` from the list. If `x` isn't in the list, an error occurs.


```python
my_list = [1, 2, 3, 4, 5]
print("original:", my_list)
my_list.remove(4)
print("modified:", my_list)
```

<pre class="output-block">
original: [1, 2, 3, 4, 5]
modified: [1, 2, 3, 5]
</pre>

> **Exercise**: `.remove()` removes only the first occurrence of the passed object from the list. This means if there are duplicates, only one will be removed. Write a block of code to remove all duplicates of an object from a list.
>
> *Hint: remember `while` loops!*


```python
my_list = [4, 10, 22, 15, 10, 8, 10, 37, 12, 10, 19, 10, 5, 27, 18, 10, 30, 7, 10, 14]
to_remove = 10
print("The list is", len(my_list), "elements long and the number", to_remove, "appears", my_list.count(to_remove), "times.")

# Add your code here
while to_remove in my_list:
  my_list.remove(to_remove)

print("The list is", len(my_list), "elements long and the number", to_remove, "appears", my_list.count(to_remove), "times.")
```

<pre class="output-block">
The list is 20 elements long and the number 10 appears 7 times.
The list is 13 elements long and the number 10 appears 0 times.
</pre>

These are just a few examples of in place methods for lists. Remember to search the docs, the web, and LLM chatbots for more examples if you have a task you need to do! There may be a method or function already out there.

#### Methods that return values

1.   `.count(x)` : counts and returns the number of occurrences of the object `x` in the list. We just saw an example of this above!
2.   `.index(x, start, end)` : returns the **index** (0-based position) of the first occurrence of the object `x`. The indexing can be done on a sub-range of the list given by the `start` and `end` indices. If the object `x` is not in the list, an error will be thrown.


```python
my_list = [1, 2, 3, 4, 2]
my_index = my_list.index(2)
print(my_index)

print("---")
my_index = my_list.index(2, 2) # If we only give it a start index, it will go to the end of the list
print(my_index)
```

<pre class="output-block">
1
---
4
</pre>

3.   `.pop([i])` : Removes and returns the element at index `i` from the list. Note that the argument `i` is given in square brackets. This means that it is optional. If no index is given, `.pop` removes and returns the last element in the list.




```python
my_list = [1, 2, 3, 4, 5, 6]
my_index_to_get = 1

print("original:", my_list)

my_list_element = my_list.pop(my_index_to_get)

print("modified:", my_list)
print("the element it removed:", my_list_element)

print("---")

the_last_element = my_list.pop()

print("modified again:", my_list)
print("the last element from the list:", the_last_element)
```

<pre class="output-block">
original: [1, 2, 3, 4, 5, 6]
modified: [1, 3, 4, 5, 6]
the element it removed: 2
---
modified again: [1, 3, 4, 5]
the last element in the list: 6
</pre>

#### List method BONUS exercise

> **BONUS EXERCISE**: Use what we've learned about lists to move Waldo from his current location to `beach_tourists`.


```python
beach_tourists=["Alice","Mason","Emma","Liam","Olivia","Walden","Ethan","Sophia","Oliver","Ava","Mia","William","Logan","Lucas","Charlotte","Amelia","Harper","James"]
music_festival_attendees=["Jackson","Sophia","Aiden","Isabella","Lucas","Noah","Levi","Benjamin","Elijah","Mason","Elena","Eliana","Mateo","Jack","Luna","Eleanor","Ezra","Willow","Henry"]
history_class_students=["Emily","James","Wally","Ella","Jacob","Amelia","Michael","Evelyn","Alexander","Avery","Mila","Aria","Ella","Layla","Scarlett","Grace","Wyatt","Waldo","Ellie","Paisley","Daniel"]
office_building_employees=["Walter","Charlotte","Alexander","Scarlett","Michael","Victoria","Samuel","Aubrey","Olive","Nathan","Camila","Gabriel","Isaac","Savannah","Gabriella","Nora","Chloe","Zoe","Stella","Riley"]
marathon_participants=["Daniel","Harper","Henry","Grace","Sebastian","Hannah","Victoria","Archer","Aurora","Brooklyn","Parker","Elias","Adeline","Julia","David","Liam","Josie","Carter","Jaxon"]

# Check and print if Waldo is at the beach initially
if "Waldo" in beach_tourists:
    print("Waldo is at the beach.")
else:
    print("Waldo is not at the beach.")

# List containing all lists
all_locations=[ beach_tourists,music_festival_attendees,history_class_students,office_building_employees,marathon_participants ]

# Write your code below to move Waldo
waldo_found=False

for location in all_locations:
    if "Waldo" in location:
        print("Waldo found in one of the locations. Moving him to the beach.")
        waldo_found=True

        # Remove Waldo from the current location
        location.remove("Waldo")

        # Add Waldo to the beach tourists
        beach_tourists.append("Waldo")

if not waldo_found:
    print("Waldo was not found in any location.")

# Write your code above to move Waldo

# Check and print if Waldo is at the beach after the move
if "Waldo" in beach_tourists:
    print("Waldo is now at the beach.")
else:
    print("Waldo is not yet at the beach.")
```

<pre class="output-block">
Waldo is not at the beach.
Waldo found in one of the locations. Moving him to the beach.
Waldo is now at the beach.
</pre>

There are many ways to do this. However, they all have some problems. For instance, as we've mentioned, we have no way of knowing *which* location Waldo was in initially. This and other organizational tasks is what our next iterable data structure, **dictionaries**, try to solve.

### Dictionaries

While lists are flexible and intuitive and useful in many cases, one of their main drawbacks is in accessing specific parts of the data. To look up and use a particular list element (e.g. the name "Waldo"), you have to know that element's positions within the list, or its **index**. An element's index may not always be easily knowable, especially for large datasets or data that has been generated or parsed programmatically.

**Dictionaries** solve this by associating two pieces of information together, allowing you to label your data and look it up by name. The term for this is a **key-value pairing**. The **key** being the data's label or name, and the **value** being the data itself.

In Python, dictionaries are declared using curly brackets `{}`, inside of which are different key-value pairs, with the keys and values separated by colons `:` and the pairs separated by commas `,` (just like list elements):


```python
my_dictionary = { 'key1' : 1, 'key2' : 3, 'key3' : 6 }
print(my_dictionary)
```

<pre class="output-block">
{'key1': 1, 'key2': 3, 'key3': 6}
</pre>

In this example, the keys are strings and the values are integers. The string `'key1'` is associated with the value `1` and so forth.

Then, individual data values can be accessed directly by their key! This is done using square brackets `[]`, just like when indexing a string or a list, but inside of the brackets instead of an index, you put the key:


```python
my_dictionary = { 'key1' : 1, 'key2' : 3, 'key3' : 6 }
print("The value of key 'key2' is:", my_dictionary['key2'])
```

<pre class="output-block">
The value of key2 is: 3
</pre>

#### Keys

Importantly, **keys themselves can be any immutable data type or structure** and **can even be mixed data types**:


```python
my_dictionary = { 123 : 1, 'key2' : 3, 7 : 6 }
print("The value of key 123 is:", my_dictionary[123])
print("The value of key 'key2' is:", my_dictionary['key2'])
print("The value of key 7 is:", my_dictionary[7])
```

<pre class="output-block">
The value of key 123 is: 1
The value of key 'key2' is: 3
The value of key 7 is: 6
</pre>

If you try to assign a mutable object, like a list as a key, you will get an error:


```python
my_incorrect_dictionary = { ['key1'] : 1, 'key2' : 3, 'key3' : 6 }
```


<pre class="output-block">
---------------------------------------------------------------------------

TypeError                                 Traceback (most recent call last)

&lt;ipython-input-6-b78fbd9b4234&gt; in &lt;cell line: 1&gt;()
----&gt; 1 my_incorrect_dict = { ['key1'] : 1, 'key2' : 3, 'key3' : 6 }


TypeError: unhashable type: 'list'
</pre>

Above, we've just added square brackets `[]` to `'key1'` to make it a single element list, however this isn't allowed for dictionary keys.

Also importantly, **keys must be unique**. If multiple identical keys exist and you try to look up that key, only one of the values of that key will be returned:


```python
my_incorrect_dictionary = { 'key1' : 1, 'key1': 2, 'key3' : 6}
print("The value of key 'key1' is:", my_incorrect_dictionary['key1'])
print(my_incorrect_dictionary)
```

<pre class="output-block">
The value of key 'key1' is: 2
</pre>

This is because the value from first instance of `key1` has actually been overwritten by the second instance. This is another **logic error**, in which the program runs, but with unexpected or unwanted results. It is up to the programmer to catch these, or else they may affect the conclusions drawn from the program!

Given the above description of dictionaries, it may be apparent that the most useful way to use keys is as string labels for your data for easy access and lookup.



##### KeyError

One more note on dictionary keys: one of the most common errors you'll see when coding in Python is `KeyError`. This happens when you try to access a key in a dictionary, but that key doesn't exist:


```python
my_dictionary = { 'key1' : 1, 'key2' : 3, 'key3' : 6 }
print("Value of key 'key7':", my_dictionary['key7'])
```


<pre class="output-block">
---------------------------------------------------------------------------

KeyError                                  Traceback (most recent call last)

&lt;ipython-input-22-58de9c881f2c&gt; in &lt;cell line: 2&gt;()
      1 my_dict = { 'key1' : 1, 'key2' : 3, 'key3' : 6 }
----&gt; 2 print("Value of key 'key7':", my_dict['key7'])


KeyError: 'key7'
</pre>

In this case, you'll have to track down why the key you're accessing doesn't exist, which could be as simple as a typo on your part, or a problem with the underlying dataset.



#### Values

Values, on the other hand, are completely flexible. They can be **mutable or immutable** and **can be mixed between data types and structures**. Values can even be other dictionaries (**nested dictionaries**)! That allows one to build some complex data tables.


```python
my_mixed_dictionary = { 'column-headers' : ['condition', 'time.point', 'measure'],
                  'sample1' : [1, 1, 0.93],
                  'sample2' : [1, 2, 0.88],
                  'sample3' : [2, 1, 0.94],
                  'meta-info' : "This dataset is made up to show the flexibility of dictionary values."
                }

print(my_mixed_dictionary['sample1'])
print(my_mixed_dictionary['sample3'][2])
print("---")
print(my_mixed_dictionary['meta-info'])

```

<pre class="output-block">
[1, 1, 0.93]
0.94
---
This dataset is made up to show the flexibility of dictionary values.
</pre>

#### Dictionary properties

1.   Dictionaries are **mutable**, meaning you can add or remove key-value pairs at will, and you can even change the value of a given key



```python
my_dictionary = { 'key1' : 1, 'key2' : 3, 'key3' : 6 }
print("Original:", my_dictionary)

my_dictionary['key4'] = 10
print("We added a key using square brackets and the assignment operator:", my_dictionary)
print("And we can access the value directly by key, e.g. 'key4':", my_dictionary['key4'])

print("---")

my_dictionary['key1'] = "NA"
print("We've changed the value of 'key1', again with the square brackets and assignment operator:", my_dictionary)
print("Value of key 'key1':", my_dictionary['key1'])
```

<pre class="output-block">
Original: {'key1': 1, 'key2': 3, 'key3': 6}
We added a key using square brackets and the assignment operator: {'key1': 1, 'key2': 3, 'key3': 6, 'key4': 10}
And we can access the value directly by key 'key4': 10
---
We've changed the value of 'key1', again with the square brackets and assignment operator: {'key1': 'NA', 'key2': 3, 'key3': 6, 'key4': 10}
Value of key 'key1': NA
</pre>

To remove a key-value pair from a dictionary, we introduce another **operator** keyword called `del` (remember, operators are symbols or keywords that perform a specific set of instructions, just like a function, but are invoked slightly differently than functions).

In the case of `del`, you simply type the keyword followed by a python object and it will delete it from the program:


```python
print("Last state of dict:", my_dictionary)

del my_dictionary['key1']

print("After removing key 'key1' with del:", my_dictionary)
```

> **Exercise**: Create a dictionary named `student_grades` with three students and their corresponding grades. The keys should be student names (e.g., "Alice", "Bob") and the values should be their grades (e.g., 85, 90). Then do the following:
>
> 1. Print the grade of one specific student by accessing it through the key.
> 2. Add a new student with their grade to the `student_grades` dictionary and print out their grade.
> 3. One student moved away, so remove them from your grade book and print out the dictionary to show they have left.


```python
## Your code goes here
student_grades = { 'Alice' : 85, 'Bob' : 90, 'Wesley' : 100 }
print("Original grades:", student_grades)
print("---")
student_grades["Gregg"] = 95
print("New student 'Gregg':", student_grades['Gregg'])
print("---")
del(student_grades["Alice"])
print("Alice moved:", student_grades)
```

<pre class="output-block">
Original grades: {'Alice': 85, 'Bob': 90, 'Wesley': 100}
---
New student 'Clara': 99
---
Alice moved: {'Bob': 90, 'Wesley': 100, 'Clara': 99}
</pre>

2.   Dictionaries are **iterable**, meaning you can loop over them with a `for` loop. More specifically, the **dictionary keys are iterable**, meaning when you loop over a dictionary, you are actually looping over the keys of the dictionary:




```python
print("Last state of dict:", my_dictionary)

for key in my_dictionary:
  print(key, ":", my_dictionary[key])
```

<pre class="output-block">
Last state of dict: {'key2': 3, 'key3': 6}
key2 : 3
key3 : 6
</pre>

You may also **loop over key-value pairs** by using the `.items()` **method**:


```python
print("Last state of dict:", my_dictionary)

for key, value in my_dictionary.items():
  print(key, ":", value)
```

<pre class="output-block">
Last state of dict: {'key2': 3, 'key3': 6}
key2 : 3
key3 : 6
</pre>

This allows you to directly access the value in the loop. But note that within the loop, the object `value` is now distinct from the data in the dictionary (i.e. `my_dictionary[key]`). This means if you wish to update the actual value in the dictionary, you should still use `my_dictionary[key]`:


```python
my_dictionary = { 'key1' : 1, 'key2' : 3, 'key3' : 6 }
print("Original state of dict:", my_dictionary)

for key, value in my_dictionary.items():
  if key == 'key2':
    value = 5       # Changing value does not affect the original dictionary
  print(key, ":", value)

print("Last state of dict:    ", my_dictionary)

for key, value in my_dictionary.items():
  if key == 'key2':
    my_dictionary[key] = 5
  print(key, ":", value)

print("Last state of dict:    ", my_dictionary)
```

<pre class="output-block">
Original state of dict: {'key1': 1, 'key2': 3, 'key3': 6}
key1 : 1
key2 : 5
key3 : 6
Last state of dict:     {'key1': 1, 'key2': 3, 'key3': 6}
key1 : 1
key2 : 3
key3 : 6
Last state of dict:     {'key1': 1, 'key2': 5, 'key3': 6}
</pre>

> **Exercise**: Recall our list of possible locations for Waldo, which is pasted below. **Edit the syntax** to turn these lists into a single dictionary. Then, print out the third name in the list of people at the office.
>
> *Hint: You will have to manually type in the key names as strings when making the dictionary.*


```python
# Original lists
beach_tourists=["Alice","Mason","Emma","Liam","Olivia","Walden","Ethan","Sophia","Oliver","Ava","Mia","William","Logan","Lucas","Charlotte","Amelia","Harper","James"]
music_festival_attendees=["Jackson","Sophia","Aiden","Isabella","Lucas","Noah","Levi","Benjamin","Elijah","Mason","Elena","Eliana","Mateo","Jack","Luna","Eleanor","Ezra","Willow","Henry"]
history_class_students=["Emily","James","Wally","Ella","Jacob","Amelia","Michael","Evelyn","Alexander","Avery","Mila","Aria","Ella","Layla","Scarlett","Grace","Wyatt","Waldo","Ellie","Paisley","Daniel"]
office_building_employees=["Walter","Charlotte","Alexander","Scarlett","Michael","Victoria","Samuel","Aubrey","Olive","Nathan","Camila","Gabriel","Isaac","Savannah","Gabriella","Nora","Chloe","Zoe","Stella","Riley"]
marathon_participants=["Daniel","Harper","Henry","Grace","Sebastian","Hannah","Victoria","Archer","Aurora","Brooklyn","Parker","Elias","Adeline","Julia","David","Liam","Josie","Carter","Jaxon"]

# Your code to convert these into a dictionary
locations = {
    "beach" : beach_tourists,
    "music-fesitval" : music_festival_attendees,
    "history-class" : history_class_students,
    "office" : office_building_employees,
    "marathon" : marathon_participants
}

print(locations["office"][2])
```

<pre class="output-block">
Alexander
</pre>

> **Exercise**: Build the dictionary **dynamically** by looping over a list of the lists of names. We have provided the list of lists as well as a list of desired key names for the dictionary. You will need to:
> * Initialize and store an empty list with `= {}`
> * Loop over one of the provided lists *by index* (recall the `range(len())` procedure)
> * Access the appropriate key name and list *by index* within the loop and add them to the dictionary


```python
# Original lists
beach_tourists=["Alice","Mason","Emma","Liam","Olivia","Walden","Ethan","Sophia","Oliver","Ava","Mia","William","Logan","Lucas","Charlotte","Amelia","Harper","James"]
music_festival_attendees=["Jackson","Sophia","Aiden","Isabella","Lucas","Noah","Levi","Benjamin","Elijah","Mason","Elena","Eliana","Mateo","Jack","Luna","Eleanor","Ezra","Willow","Henry"]
history_class_students=["Emily","James","Wally","Ella","Jacob","Amelia","Michael","Evelyn","Alexander","Avery","Mila","Aria","Ella","Layla","Scarlett","Grace","Wyatt","Waldo","Ellie","Paisley","Daniel"]
office_building_employees=["Walter","Charlotte","Alexander","Scarlett","Michael","Victoria","Samuel","Aubrey","Olive","Nathan","Camila","Gabriel","Isaac","Savannah","Gabriella","Nora","Chloe","Zoe","Stella","Riley"]
marathon_participants=["Daniel","Harper","Henry","Grace","Sebastian","Hannah","Victoria","Archer","Aurora","Brooklyn","Parker","Elias","Adeline","Julia","David","Liam","Josie","Carter","Jaxon"]

# List of lists and list of desired key names
all_names = [ beach_tourists, music_festival_attendees, history_class_students, office_building_employees, marathon_participants ]
key_names = ["beach", "music-festival", "history-class", "office", "marathon"]

# Your code here

locations = {}

for i in range(len(key_names)):
  cur_key = key_names[i]
  cur_names = all_names[i]

  locations[cur_key] = cur_names

print(locations["office"][2])
```

<pre class="output-block">
Alexander
</pre>

#### Dictionary inclusion with `in`

Like strings and lists, the `in` keyword works to check if something is in a dictionary. However, for dictionaries, `in` specifically checks whether something is a **key** of the dictionary. To check if something exists as a value, one would have to check that manually by doing key lookups.


```python
my_mixed_dictionary = { 'column-headers' : ['condition', 'time.point', 'measure'],
                        'sample1' : [1, 1, 0.93],
                        'sample2' : [1, 2, 0.88],
                        'sample3' : [2, 1, 0.94],
                        'meta-info' : "This dataset is made up to show the flexibility of dictionary values."
                }

# Check for inclusion in keys of a dict
if 'sample1' in my_mixed_dictionary:
  print("Found sample1")
else:
  print("Did not find sample1")

# If the provided object is not a key it will not be found
if 0.93 in my_mixed_dictionary:
  print("Found 0.93")
else:
  print("Did not find 0.93")

# To search values, access by key directly
if 0.93 in my_mixed_dictionary['sample1']:
  print("Found 0.93 in sample1")
else:
  print("Did not find 0.93 in sample1")

```

<pre class="output-block">
Found sample1
Did not find 0.93
Found 0.93 in sample1
</pre>

> **Exercise**: Using our `locations` dictionary that has places as keys and lists of names as values, find if Waldo is in any of the locations. This time, if he is there, display in which location he was found.


```python
# Original lists
beach_tourists=["Alice","Mason","Emma","Liam","Olivia","Walden","Ethan","Sophia","Oliver","Ava","Mia","William","Logan","Lucas","Charlotte","Amelia","Harper","James"]
music_festival_attendees=["Jackson","Sophia","Aiden","Isabella","Lucas","Noah","Levi","Benjamin","Elijah","Mason","Elena","Eliana","Mateo","Jack","Luna","Eleanor","Ezra","Willow","Henry"]
history_class_students=["Emily","James","Wally","Ella","Jacob","Amelia","Michael","Evelyn","Alexander","Avery","Mila","Aria","Ella","Layla","Scarlett","Grace","Wyatt","Waldo","Ellie","Paisley","Daniel"]
office_building_employees=["Walter","Charlotte","Alexander","Scarlett","Michael","Victoria","Samuel","Aubrey","Olive","Nathan","Camila","Gabriel","Isaac","Savannah","Gabriella","Nora","Chloe","Zoe","Stella","Riley"]
marathon_participants=["Daniel","Harper","Henry","Grace","Sebastian","Hannah","Victoria","Archer","Aurora","Brooklyn","Parker","Elias","Adeline","Julia","David","Liam","Josie","Carter","Jaxon"]

# List of lists and list of desired key names
all_names = [ beach_tourists, music_festival_attendees, history_class_students, office_building_employees, marathon_participants ]
key_names = ["beach", "music-festival", "history-class", "office", "marathon"]

# Build the locations dictionary dynamically
locations = {}

for i in range(len(key_names)):
  cur_key = key_names[i]
  cur_names = all_names[i]

  locations[cur_key] = cur_names

# Your code here

for location in locations:
  print("Searching for Waldo at the", location)
  if "Waldo" in locations[location]:
    print("Found Waldo at the", location, "!!")
```

<pre class="output-block">
Searching for Waldo at the beach
Searching for Waldo at the music-festival
Searching for Waldo at the history-class
Found Waldo at the history-class !!
Searching for Waldo at the office
Searching for Waldo at the marathon
</pre>

Hopefully the benefits of dictionaries are becoming apparent.

#### Dictionary methods and functions

Now that we know a bit about dictionary creation and manipulation, let's look at some built-in ways, methods and functions, to work with them.

1.   `.keys()` and `.values()` : returns an object that contains the dictionary's keys or values, respectively. This can be used to loop over the keys or values, or to convert them into a list of the keys or values with the `list()` function:


```python
my_dictionary = { 'key1' : 1, 'key2' : 3, 'key3' : 6 }

# You can use .keys() to loop over the keys in a dict, but
# this is the same behavior as using a for loop on the dict alone
for key in my_dictionary.keys():
  print(key, ":", my_dictionary[key])

# You can loop over the values, but you lose the association with the keys
for value in my_dictionary.values():
  print(value)

# You can convert either to a list and check for inclusion of things
my_keys = list(my_dictionary.keys())
my_values = list(my_dictionary.values())

print('key1' in my_keys)
print(7 in my_values)
```

<pre class="output-block">
key1 : 1
key2 : 3
key3 : 6
1
3
6
True
False
</pre>

2.   The `list()` function, introduced above, can also be used directly on the dictionary to get a list of the keys:


```python
my_dictionary = { 'key1' : 1, 'key2' : 3, 'key3' : 6 }
print(list(my_dictionary))
```

<pre class="output-block">
['key1', 'key2', 'key3']
</pre>

3.   `.update(x)` : add `x` to the dictionary. Especially useful for **combining dictionaries** if `x` is another dictionary, though be careful of overlapping keys - only the value from the new dictionary will be retained.


```python
my_dictionary = { 'key1' : 1, 'key2' : 3, 'key3' : 6 }
print("Original:", my_dictionary)

# .update() updates the dictionary in place, so no need to use =
my_dictionary.update( {'key4' : 9, 'key5' : 2} )
print("Updated:", my_dictionary)

print("---")

# Watch out for overlapping keys which overwrite the values!
print("key1:", my_dictionary['key1'])
my_dictionary.update( {'key1' : 99 } )
print("Updated with overwitten key1:", my_dictionary)
print("updated key1:", my_dictionary['key1'])
```

<pre class="output-block">
Original: {'key1': 1, 'key2': 3, 'key3': 6}
Updated: {'key1': 1, 'key2': 3, 'key3': 6, 'key4': 9, 'key5': 2}
---
key1: 1
Updated with overwitten key: {'key1': 99, 'key2': 3, 'key3': 6, 'key4': 9, 'key5': 2}
updated key1: 99
</pre>

4.   `len(dictionary)` : the trusty `len()` function can also be passed a dictionary, in which case it returns the number of keys in the dictionary:




```python
my_dictionary = { 'key1' : 1, 'key2' : 3, 'key3' : 6 }

num_keys = len(my_dictionary)

print("There are", num_keys, "keys in the dictionary")
```

<pre class="output-block">
There are 3 keys in the dictionary
</pre>

#### Dictionary BONUS exercise

**BONUS EXERCISE**: Use what we've learned about dictionaries and lists to move Waldo from his current location to the marathon. Careful, he might have moved since last time!


```python
# Original lists
beach_tourists=["Alice","Mason","Emma","Liam","Olivia","Walden","Ethan","Sophia","Oliver","Ava","Mia","William","Logan","Lucas","Charlotte","Amelia","Harper","James"]
music_festival_attendees=["Jackson","Sophia","Aiden","Isabella","Lucas","Noah","Levi","Benjamin","Elijah","Mason","Elena","Eliana","Mateo","Jack","Luna","Eleanor","Ezra","Waldo","Willow","Henry"]
history_class_students=["Emily","James","Wally","Ella","Jacob","Amelia","Michael","Evelyn","Alexander","Avery","Mila","Aria","Ella","Layla","Scarlett","Grace","Wyatt","Ellie","Paisley","Daniel"]
office_building_employees=["Walter","Charlotte","Alexander","Scarlett","Michael","Victoria","Samuel","Aubrey","Olive","Nathan","Camila","Gabriel","Isaac","Savannah","Gabriella","Nora","Chloe","Zoe","Stella","Riley"]
marathon_participants=["Daniel","Harper","Henry","Grace","Sebastian","Hannah","Victoria","Archer","Aurora","Brooklyn","Parker","Elias","Adeline","Julia","David","Liam","Josie","Carter","Jaxon"]

# List of lists and list of desired key names
all_names = [ beach_tourists, music_festival_attendees, history_class_students, office_building_employees, marathon_participants ]
key_names = ["beach", "music-festival", "history-class", "office", "marathon"]

# Shortcut to build the locations dictionary dynamically
locations = dict(zip(key_names, all_names)) ## Woah!

# Check and print if Waldo is at the marathon initially
if "Waldo" in locations['marathon']:
    print("Waldo is now at the marathon.")
else:
    print("Waldo is not at the marathon.")

# Your code below to move Waldo to the marathon
for location in locations:
    if "Waldo" in locations[location]:
        print("Waldo found at the", location, "- Moving him to the marathon.")
        waldo_found=True

        # Remove Waldo from the current location
        locations[location].remove("Waldo")

if not waldo_found:
    print("Waldo was not found in any location.")
else:
    locations['marathon'].append("Waldo")
# Your code above to move Waldo to the marathon

# Check and print if Waldo has been moved to the marathon
if "Waldo" in locations['marathon']:
    print("Waldo is now at the marathon.")
else:
    print("Waldo is not at the marathon.")
```

<pre class="output-block">
Waldo is not at the marathon.
Waldo found at the music-festival - Moving him to the marathon.
Waldo is at the marathon.
</pre>

### Other iterables

While strings, lists, and dictionaries are the main iterables we'll be working with, there are a couple of others that are worth a mention just so you are familiar with them.

#### Tuples

Tuples are just like lists, except they are **immutable**:


```python
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)
print(my_tuple[1])

print("---")

my_tuple2 = ("hello", -12, "world", 985, "adshgadk")
print(my_tuple2[2])
print(my_tuple2[::-1])
```

<pre class="output-block">
(1, 2, 3, 4, 5)
2
---
world
('adshgadk', 985, 'world', -12, 'hello')
</pre>

Note that tuples are defined with regular parentheses `()` rather than square brackets `[]`.

As mentioned above, tuples are immutable:


```python
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)
print(my_tuple[1])

my_tuple[1] = 7
```

<pre class="output-block">
(1, 2, 3, 4, 5)
2



---------------------------------------------------------------------------

TypeError                                 Traceback (most recent call last)

&lt;ipython-input-22-2210a4921f31&gt; in &lt;cell line: 5&gt;()
      3 print(my_tuple[1])
      4 
----&gt; 5 my_tuple[1] = 7


TypeError: 'tuple' object does not support item assignment
</pre>

Tuples are often returned by built-in functions and methods, so if you ever see data surrounded by parentheses `()`, you'll know what it is now.

Easily enough, tuples can also be converted to lists with the `list()` function:


```python
my_tuple = (1, 2, 3, 4, 5)
my_list = list(my_tuple)

print(my_tuple)
print(my_list)
```

<pre class="output-block">
(1, 2, 3, 4, 5)
[1, 2, 3, 4, 5]
</pre>

And, unlike lists, tuples can be used as keys in dictionaries:


```python
my_dictionary = { 'key1' : 1, ('key2') : 3, ('k', 'e', 'y', 3) : 6 }
print(my_dictionary)
```

<pre class="output-block">
{'key1': 1, 'key2': 3, ('k', 'e', 'y', 3): 6}
</pre>

#### Sets

Sets are essentially lists of unique elements. They allow us to perform powerful set operations on different lists, say to get the union or intersection of two lists.

Sets can be defined on their own with curly brackets `{}`, though unlike dictionaries sets do not have key-value pairs. Sets can also be created from lists with the `set()` function. This also has the benefit of removing duplicate elements from the list, which may be desireable in certain circumstances.


```python
my_set = {1, 2, 3, 4, 5}
print(my_set)

print("---")

# Sets can be used to remove duplicates from a list
my_list = (1, 1, 1, 2, 3, 3, 4, 5)
my_uniq_list = list(set(my_list))
print(my_uniq_list)
```

<pre class="output-block">
{1, 2, 3, 4, 5}
---
[1, 2, 3, 4, 5]
</pre>

And as mentioned above, set operations can be performed. This would introduce a whole new set of operators and methods, so we won't get into it here. But set operations can be really useful, so look them up if you ever need them.

### Iterable review

*   **Iterables** are objects you can loop over using a `for` loop and check for inclusion with `in`.
*   **Strings** are iterable, with the individual elements being characters.
*   **Lists** are iterable collections of potentially mixed data types, with each element being one data object
*   **Lists and strings are indexed**, meaning each element is assigned, a number starting from 0, based on its position in the iterable. Indexing can be used to slice and splice lists and strings.
*   **Dictionaries** are iterables of **key-value pairs**, which allow association of one piece of information to another, potentially for labeling.



## Importing libraries of functions

Let's again think about our recipe telling a robot how to bake chocoloate chip cookies:

```
  1. Walk_anywhere(distance=2 meters and angle=40°).
  2. Extend your arm towards the power button.
  3. Push the power button.
  4. Move your arm to the temperature dial.
  5. Set the temperature dial to 375°F (190°C).
  6. Lower your arm.
  7. Walk_anywhere(distance=0.6 meters and angle=120°).
  8. Extend your arm.
  9. Grasp the cabinet handle.
  10. Pull the cabinet open.
  11. Release the cabinet handle.
  12. Extend both arms toward the large mixing bowl on the shelf.
  13. Grasp the mixing bowl with both hands.
  .
  .
  .
  and so on.
```

Elsewhere in the recipe book are step-by-step instructions for certain tasks, like:

```
Walk_anywhere(*distance*, *angle*):
  1. Turn body *angle* degrees
  2. Repeat Step until the *distance* has been traversed
```

and:

```
Step:
  1. Lift right leg.
  2. Extend right leg.
  3. Lower right leg and lift left leg.
  4. Extend left leg.
  5. Lower left leg and lift right leg.
```

These recipes are analogous to **functions**, and because they already exist in the recipe book, we can think of them as **built-in functions**, those that come with your Python installation. We've learned about a lot of these, like `len()` for iterables, `sum()` for a list of numbers, and so on.

However, there are lots of other chefs out there writing their own recipes, and they may make their recipe books available to anyone who wants them. This is great because you may end up needing to cook some similar recipes, in which case you can go to the public library or the bookstore and pick up their book to use.

In programming terms, this is referred to as **importing a library**. The **library** written by someone else will have extra functions that, once imported, you can use in your program. **Libraries may also be referred to as modules**, among other names.

For instance, there is no built-in function in Python to calculate the log of a number:


```python
print(log(100))
```


<pre class="output-block">
---------------------------------------------------------------------------

NameError                                 Traceback (most recent call last)

&lt;ipython-input-1-85d71efb1520&gt; in &lt;cell line: 1&gt;()
----&gt; 1 print(log(100))


NameError: name 'log' is not defined
</pre>

However, there is a `math` library with a a `log()` function that you can import!


```python
import math
print(math.log(100))
```

<pre class="output-block">
4.605170185988092
</pre>

Note that by default it does natural log.

Also, notice that, in order for Python to know where to find the function even though we've imported it, we have to tell it explicitly with `math.`. This helps in the circumstance that you import multiple libraries that happen to have a function with the same name.

However, you can also directly import a function from a library with the `from` keyword:


```python
from math import log
print(log(100))
```

<pre class="output-block">
4.605170185988092
</pre>

One could also declare an **alias** for the library if you want to still import the whole library but not have to type the the complete name of it every time:


```python
import math as m
print(m.log(100))
```

<pre class="output-block">
4.605170185988092
</pre>

This means `m` exists as an object in your program (just as if you'd assigned it with `=`). But of course, this means you can't use `m` as an object name anywhere else in the program:


```python
import math as m

m = "hello world!"

print(m.log(100))
```


<pre class="output-block">
---------------------------------------------------------------------------

AttributeError                            Traceback (most recent call last)

&lt;ipython-input-7-b08afa73f34c&gt; in &lt;cell line: 5&gt;()
      3 m = "hello world!"
      4 
----&gt; 5 print(m.log(100))


AttributeError: 'str' object has no attribute 'log'
</pre>

There are many, many libraries out there. Some are pre-installed with Python (like `math`), but others you may find and have to install for yourself. Hopefully the authors have easy and clear instructions for installation...

In later days, we'll work with some libraries meant for data analysis, `numpy` and `pandas`.

## Writing functions

Of course, there may come a time when you're coding and you notice you're repeating the same set of instructions on different inputs a lot. This, of course, is the perfect use-case for a function, and like the people that write the libraries you import, you can also write your own functions!

**Write lots of functions! Functionalize everything!**

There are many reasons to write functions, even if you think you might only use it once in your notebook or workflow. Using functions in your code improves the readability of the code, because rather than puzzle through many lines trying to interpret what was going on, you can just read the function name/description and understand what happened. It also improves readability by allowing the reader to focus on the important parts of the code rather than functions that may perform rote tasks.

Functions make your code more modular and reproducible. By breaking down the analysis into discrete chunks, you can easily swap out functions to test things or move sections of code around because functions are very portable.

Functions also make your code more testable. When you encounter a bug or an unexpected outcome, you can more easily trace the source of the problem if you have functions that are well-documented and do one thing. Think of it like mixing smaller batches of reagents that you use at a time rather than one big container.

**Functions should do ONE thing**

Functions are meant to do one thing, just like a sentence is meant to express a complete thought. If you bundle your entire analysis into a single function, it's akin to writing a run-on sentence by abusing colons, semi-colons, etc. It might be correct and it might run, but it will be hard to read and also hard to debug. Make liberal use of calling functions within functions and making your code modular.


### Function syntax

When writing a function, you must start the line with the `def` keyword, which stands for *define*. Then you can give the function a name. The name can be anything, as long as the name abides by the standard object naming conventions (see Day 1). Then you type parentheses `()` followed by a colon `:`:

```
def my_function():
```

> **Review question**: What other lines of code in Python end with a colon `:`? What has to happen after those lines?

Here is an example function. What happens when we run this block?


```python
def my_function():
  print("hello world!")
```

Nothing! Because though we've defined the function, we haven't yet **called** it. The same way when you're coding and call a built-in function (like `len()` or `abs()`), in your program, after you've defined the function, you can type its name to call it:


```python
my_function()
```

<pre class="output-block">
hello world!
</pre>

Great! Now anytime we want to print "hello world!" all we have to do is type `my_function()`!

Well, ok so that's not very useful. Let's make a more interesting function.

> **Exercise**: Below, we've provided the code for a magic 8 ball type response. It randomly selects an answer from a list of answers. This code is not in a function. Put it in a function called `magic_8_ball()` and call it a few times in the code block. Remember, every line of code you want to be included in the function must be indented!


```python
import random # This is a built-in Python library for random-number generation tasks (such as randomly selecting an element from a list)

# Your code here: move the code into a function called magic_8_ball()
def magic_8_ball():
    # List of possible responses
    responses = [
        "Yes", "No", "Maybe", "Ask again later", "Definitely",
        "I have no idea", "Very doubtful", "Without a doubt", "Outlook not so good"
    ]

    # Select a random response
    answer = random.choice(responses)

    # Print the response
    print("The Magic 8-Ball says:", answer)

# Call the function to see the Magic 8-Ball in action
magic_8_ball()
magic_8_ball()
magic_8_ball()
```

<pre class="output-block">
The Magic 8-Ball says: Very doubtful
The Magic 8-Ball says: No
The Magic 8-Ball says: Outlook not so good
</pre>

### Handling arguments

Of course, just like the built-in functions, our functions are a lot more versatile and useful if they **accept input in the form of arguments**.

We know how to provide arguments by placing them in the parentheses during the function call (e.g. with `abs(-5)`, `-5` is the argument).

When writing a function, we must also defined which arguments are accepted within the parentheses of our function definition:

```
def my_function(arg1, arg2, ...)
```

You can name the arguments anything you'd like, as long as the names conform to the object naming conventions we've gone over (see Day 1). And in this example, the `...` indicates that you can define more arguments for your function if they are needed. Of course, as we saw above with the hello world! and `magic_8_ball()` functions, a function doesn't have to have arguments at all.

Here is an example of a simple function with one argument, a number:


```python
def square(num):
  print(num * num)

square(2)

my_other_num = 4
square(my_other_num)
```

<pre class="output-block">
4
16
</pre>

Here, we've told the function to expect a single number as an argument. Within the function, we call this number object `num`. The function then simply prints out the square of the number. And we've shown a couple of ways to call the function.

Just like with built-in functions, if we don't provide the expected number of arguments to our function, the program will stop with an error:


```python
square(2, 4)
```


<pre class="output-block">
---------------------------------------------------------------------------

TypeError                                 Traceback (most recent call last)

&lt;ipython-input-8-6622a44528c4&gt; in &lt;cell line: 1&gt;()
----&gt; 1 square(2, 4)


TypeError: square() takes 1 positional argument but 2 were given
</pre>

> **Exercise**: Edit the `magic_8_ball()` function to take a question (a single string) as an argument and print it out before the response.


```python
import random # This is a built-in Python library for random-number generation tasks (such as randomly selecting an element from a list)

# Your code here: edit the magic_8_ball function to accept a question string as an argument
# and to print out the question in addition to the answer.
def magic_8_ball(question):
    # List of possible responses
    responses = [
        "Yes", "No", "Maybe", "Ask again later", "Definitely",
        "I have no idea", "Very doubtful", "Without a doubt", "Outlook not so good"
    ]

    # Select a random response
    answer = random.choice(responses)

    # Print the response
    print(question, ":", answer)

# Call the function to see the Magic 8-Ball in action
magic_8_ball("Will it snow tomorrow?")
```

<pre class="output-block">
Will it snow tomorrow? : Outlook not so good
</pre>

#### Default arguments

It is also possible to define default values for a particular argument, in which case they do not necessarily need to be provided when the function is called:


```python
def square(num=2):
  print(num * num)

square()
square(3)
```

<pre class="output-block">
4
9
</pre>

This might be especially useful when you have optional code you'd like to run in your function only sometimes:


```python
def square(num, also_cube=False):
  print(num * num)
  if also_cube:
    print(num ** 3)

square(2)
print("---")
square(2, True)
```

<pre class="output-block">
4
---
4
8
</pre>

> **Exercise**: Write a function that takes two numbers: one to be the base and another to be the exponent. By default, this function should square the provided base number. However, if an exponent is provided, it will raise the base to that power. Provide use cases that show the function being used both with its default behavior (squaring the base) and with another exponent.


```python
# Your code here
def power(base, exponent=2):
  print(base ** exponent)

# Provide test cases for your function below
power(2)
power(2, 3)
```

<pre class="output-block">
4
8
</pre>

Note that arguments with default values must appear at the end of the list of arguments in your function definition:


```python
def add_2_nums(num1, also_multiply=False, num2):
  print(num1 + num2)
  if also_multiply:
    print(num1 * num2)

add_2_nums(2, 3)
```

This prevents the above from running, which would result in an error (because `num2` would be undefined).

### Named arguments

So far, whether its been built-in functions or those we've written, we've called them simply by specifying *the values of the arguments* in the function call:


```python
def square(num, also_cube=False):
  print(num * num)
  if also_cube:
    print(num ** 3)

my_num = 2
square(my_num)
print("---")
square(my_num, True)
```

<pre class="output-block">
4
---
4
8
</pre>

These are treated as **positional arguments**, which means they are assigned to the parameter in the function simply based on the order in which they are provided: the first argument provided will be given to the first parameter in the function, the second argument to the second parameter, and so on.

However, we can also directly assign the values of the arguments directly in our function call:


```python
def square(num, also_cube=False):
  print(num * num)
  if also_cube:
    print(num ** 3)

my_num = 2
square(num = my_num)
print("---")
square(num = my_num, also_cube = True)
print("---")
square(also_cube = True, num = 3)
```

<pre class="output-block">
4
---
4
8
---
9
27
</pre>

These are now called **named arguments**.

This can greatly increase the clarity of our code, and, as shown above, obviates the need to provide arguments in any particular order. This also let's us selectively specify argument values when each one has a default:


```python
def greet(person="Bob", greeting="Hello", punctuation="!"):
  print(greeting, person, punctuation)

message = greet(person="Alice", punctuation="?")


```

<pre class="output-block">
Hello Alice ?
</pre>

Here, we only provided values for `person` and `puncutation`, skipping over `greeting` in our function call, which uses it's default value. The combined use of default values for our arguments in the function and calling the function with named arguments makes our function call clearer and less error-prone.

### Writing functions exercise

> **Exercise**: Write a function that takes a **list of numbers** as an argument and prints out the tally (number of numbers), and the min, max, sum, and average of the numbers in the list. Call this function `num_summary()`. Run it on the lists provided below.
>
> *Hint: While you could code these simple tasks yourself with a `for` loop and some `if` statements, remember there are functions that do these tasks for us that you can call in your own function. See the [List functions](#list-functions) section.*


```python
# Your code here: a num_summary() function

def num_summary(nums):
  num_nums = len(nums)
  max_num = max(nums)
  min_num = min(nums)
  sum_nums = sum(nums)

  avg_num = sum_nums / num_nums

  print("There are", num_nums, "numbers in the list.")
  print("The largest number is:", max_num)
  print("The smallest number is:", min_num)
  print("The sum of all the numbers is:", sum_nums)
  print("The average of the numbers is:", avg_num)

# These are the test cases to run the num_summary() function on
nums1 = [23, 85, 56, 34, 78, 22]
nums2 = [17, 48, 92, 55, 83, 24, 63, 7, 31, 89]
nums3 = [59, 44, 66, 12, 5, 95, 23, 37]

for num_list in [nums1, nums2, nums3]:
  num_summary(num_list)
  print("---")
```

<pre class="output-block">
There are 6 numbers in the list.
The largest number is: 85
The smallest number is: 22
The sum of all the numbers is: 298
The average of the numbers is: 49.666666666666664
---
There are 10 numbers in the list.
The largest number is: 92
The smallest number is: 7
The sum of all the numbers is: 509
The average of the numbers is: 50.9
---
There are 8 numbers in the list.
The largest number is: 95
The smallest number is: 5
The sum of all the numbers is: 341
The average of the numbers is: 42.625
---
</pre>

### `return`ing data

So far we've covered how to pass information to the function in the form of arguments. However, we haven't done anything else with the information generated by the function other than print it to the screen. It wouldn't be very helpful if that's the only way functions provided information.

However, this isn't the case. Functions can **return** information by using the `return` keyword:


```python
def square(num):
  num_squared = num * num
  return num_squared

my_num = 2
my_num_squared = square(my_num)
print(my_num_squared)
```

<pre class="output-block">
4
</pre>

Now, we're free to use the output of our function elsewhere in the program! Or we can just print it again.

Any type of object can be returned:


```python
def list_to_dict(pairs):
    return dict(pairs)

pair_list = [('apple', 2), ('banana', 5), ('orange', 3)]
fruit_dictionary = list_to_dict(pair_list)
print(fruit_dictionary)
```

<pre class="output-block">
{'apple': 2, 'banana': 5, 'orange': 3}
</pre>

For instance, this function, which takes a **list of tuples** and converts them into a **dictionary**. This dictionary is returned and printed to the screen.

> **Exercise:** Write a function called `in_list` that takes a number and a list of numbers and checks if that number already exists in the list. If it does, print "number already exists!" or something similar. If it doesn't, add that number to the list. In both cases, return the list.


```python
# Your code here

def in_list(value, a_list):
  if value in a_list:
    print(value, "is already in the list!")
  else:
    print("Adding", value, "to the list!")
    a_list.append(value)
  return a_list

# Test your code on these lists
my_list = [1, 2, 3, 4, 5]
print("Original:", my_list)
print("---")

my_list = in_list(3, my_list)
print("After first call:", my_list)
print("---")

my_list = in_list(30, my_list)
print("After second call:", my_list)

```

<pre class="output-block">
Original: [1, 2, 3, 4, 5]
---
3 is already in the list!
After first call: [1, 2, 3, 4, 5]
---
Adding 30 to the list!
After second call: [1, 2, 3, 4, 5, 30]
</pre>

#### Unpacking returned values

Multiple values can be `return`ed from a function. This is done simply by separating them by commas `,` after the return keyword. By default, they are returned as a **tuple**:


```python
def square_and_cube(num):
  num_squared = num * num
  num_cubed = num ** 3

  return num_squared, num_cubed

my_result = square_and_cube(3)
print(my_result)
```

<pre class="output-block">
(9, 27)
</pre>

However, you can also explicitly assign each returned value to its own object as it is returned by separating your variable names by commas `,`:


```python
def square_and_cube(num):
  num_squared = num * num
  num_cubed = num ** 3

  return num_squared, num_cubed

result_squared, result_cubed = square_and_cube(3)
print(result_squared)
print(result_cubed)
```

<pre class="output-block">
9
27
</pre>

This can be done for any number of returned values, given enough variable names. However, if you don't provide the correct number of names, an error will occur.

This is actually a general feature of lists and tuples called **unpacking**:


```python
my_list = [1,2,3]
num1, num2, num3 = my_list

print(num1)
print(num2)
print(num3)
```

<pre class="output-block">
1
2
3
</pre>

> **Exercise**: Modify the `num_summary()` function so that instead of printing the information to the screen, it returns it to the function call. Do this any way you like (return a list or dict, unpack values, etc.). Do this for the three provided lists, then display the highest average number from the three lists. In other words, the output of this block should be a single number: the highest average number from the averages of the three lists.


```python
# Modify your function here
def num_summary(nums):
  num_nums = len(nums)
  max_num = max(nums)
  min_num = min(nums)
  sum_nums = sum(nums)

  avg_num = sum_nums / num_nums

  return [num_nums, max_num, min_num, sum_nums, avg_num]

# Run your modified function on these lists 
nums1 = [23, 85, 56, 34, 78, 22]
nums2 = [17, 48, 92, 55, 83, 24, 63, 7, 31, 89]
nums3 = [59, 44, 66, 12, 5, 95, 23, 37]

# Your code here
avgs = []
for num_list in [nums1, nums2, nums3]:
  cur_result = num_summary(num_list)
  avgs.append(cur_result[4])

# Print only the highest of the averages
print("The highest average number is:", max(avgs))
```

<pre class="output-block">
The highest average number is: 50.9
</pre>

#### `None`

In Python, in order for the language to function consistently, all functions return a value, even those without an explicit `return` statement. The default return value for a Python function is `None`:


```python
def greet():
  print("hello world!")

result = greet()
print(result)

```

<pre class="output-block">
hello world!
None
</pre>

In Python, `None` is actually its own data type, meant to indicate the absence of information or as a placeholder. `None` is most often seen when trying to use the result of a function, as shown above, but it can actually be a useful initial or default data value, since it evaluates to `False` as a boolean:


```python
data = None
print(data)
print(bool(data))

if data:
  process_data(data)
else:
  print("No data has been provided")
```

<pre class="output-block">
None
False
No data has been provided
</pre>

Other libraries may have their own special values, like `NA`, to indicate lack of data.

### Documenting functions

One step towards having a readable and well-documented function is to choose a descriptive name for it. The name should use a verb like "plot" or "calculate". Try and follow some consistent naming conventions with regard to capitalization and underscores. It'll be easier to remember what your functions are called if you don't mix up conventions like "plot" and "Plot" or "plot_this" and "plotThis". For more guidance, see the [python style guide :octicons-link-external-24:](https://peps.python.org/pep-0008/#naming-conventions){:target="_blank"}.

Another tip for writing good functions: it is best practice to **document** it with what it does. That way, when future you or someone else reads it, the function's useage is immediately clear. You can annotate functions with a triple quote at the beginning of a function body, which is called a **docstring**. Typical contents of a docstring are:

* one sentence describing the usage
* list of all parameters and what type they should be
* what the function returns

See below:

```python
def fibonacci(n):
    """
    Calculate the nth number in the fibonacci sequence
    Input: n, an integer
    Returns: the nth number in the fibonacci sequence, an integer
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
```

## Commenting your code

You've probably seen the lines of code starting with the `#` symbol (known as a number sign, hashtag, pound sign, or octothorp) throughout our workshop. These lines are called **comments**. Comments must start with `#` but afterwards can contain anything, even python keywords like `in`, `if`, `for`, etc. This is because that Python is programmed such that if the interpreter encounters a line starting with `#`, it simply ignores it. It does not try to execute it as a line of code.

This allows programmers to document their code in fine detail, section-by-section or even line-by-line. A good rule of thumb is to write a comment for every chunk of code that does something specific, or if it is not obvious why you had to write code that way. These comments will primarily benefit yourself for when you go back to your code and ask yourself, "Why did I do it this way?". It is also good practice to have comments exist on their own line rather than in-line with your code.

## Day 2 review

We covered a lot of ground today. Since we learned about `for` loops, we needed to learn about all the **iterables** in Python so that we know everything we can loop over.

*   **Iterables** are data structures that are collections of individual elements that can be looped over with `for`.
*   **Lists** are mixed collections of any type of data. They are **indexed** and **mutable**.
*   **Dictionaries** are mixed collections of any type of data in the form of **key-value pairs**. This allows association between one piece of information and another, for quick look-up and labeling.

We also learned that we can write our own functions!

*   If we write a piece of code we end up using a lot, it is a good idea to **generalize it as a function**.
*   Functions are defined with `def`, a function name, and arguments within parentheses `()` followed by a colon `:`.
*   Any code we want to be in our function must be **indented as a block of code**.
*   Functions take **arguments as input** and **`return` values as output**.

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

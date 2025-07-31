---
title: "[Workshop] Python intensive, part 4"
description: "Introduction to file handling and the numpy library for numerical computing in Python, including arrays and basic operations."
authors:
    - Lei Ma
    - Adam Freedman
---

# Python intensive, part 4

## What is python and why do we need it/why are you taking this workshop?

* Python is a programming language that is commonly used for data analysis
* R is another commonly used programming language, probably second to python
* Python is more general purpose than R, which is specifically for data analysis
* Programming languages are a way for humans to give the computer commands
* Regardless of how you collect data, it needs to be analyzed and code is the best way (Don't use excel!)

## Jupyter basics

Jupyter notebooks are text files that can be rendered as formatted text **and** run code given the proper setup (see Installation).

Text is split into **cells**. Double clicking a cell allows you to edit it.

For code cells, there is also an option to run the code. You can do this by pressing **SHIFT+ENTER** while having it selected, or press the **Run** button at the top of the cell (exact location depends on the editor you're using). Because of the way we set up the notebook the code cells will be running Python code.

For this workshop, we'll be asking you to follow along by running code cells and by doing coding exercises by writing or editing code in code cell.

**IMPORTANT**: Run the code cells below to **import** the **libraries** we'll be using during this workshop.


```python
# Run this cell to import the libraries we'll be using
# If you don't have the kernel loaded or installed, it will not work

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
```

<pre class="output-block">---------------------------------------------------------------------------
ModuleNotFoundError                       Traceback (most recent call last)
Cell In[1], line 4
      1 # Run this cell to import the libraries we'll be using
      2 # If you don't have the kernel loaded or installed, it will not work
----> 4 import numpy as np
      5 import pandas as pd
      6 import matplotlib.pyplot as plt

ModuleNotFoundError: No module named 'numpy'
</pre>

And run the following to demonstrate how the code blocks run and display code:


```python
# Run this cell to print a message to the screen
print("this is my code cell")
```

<pre class="output-block">this is my code cell
</pre>

Any **variables** that you assign in one cell will be available in other cells. But they will not be saved between sessions. If you close the notebook and re-open it, you will need to re-run the previous cells to get your variables back. Therefore, it's important to be aware of the state of your notebook and the order in which your cells were run.


```python
my_string = "this is my code cell"
```


```python
print(my_string)
```

<pre class="output-block">this is my code cell
</pre>

Jupyter notebooks can be exported to pdf or html, so that other people can view both the code and its output. It's a good format for handing in homeworks, for example, since you can show your work. In this notebook, there will be exercises with placeholders for the code that you will have to fill in. For these exercises, we encourage you to work with each other, use google, LLMs, and whatever other resources if you are stuck. It's not an exam, but just a way to get practice of the concepts. Afterwards, we will post the completed notebook on our website so you can have examples of solutions.

## Python refresher

Let's begin by reviewing some of the terms we've covered in the past sessions that will come up again today.

| Term | Definition |
| --- | --- |
| Object | The thing itself (an instance of a class) |
| Variable | The name we give the object (a pointer to the object) |
| Class | The blueprint for the object (defines the attributes and methods of object) |
| Method | A function that belongs to an object |
| Attribute | A property of an object |
| Function | A piece of code that takes an input and gives an output/does something |
| Argument| The objects that are passed to the function for it to operate on |
| Library | Collections of python functions/capabilities that can be installed and loaded on top of base python

### Object Methods

Everything in python is an **object**, and depending on the type of object, they may have certain **methods** that can be called on them. For example, strings have a method called `upper()` that converts the string to uppercase.


```python
my_string = "hello"
my_string.upper()
```

<pre class="output-block">'HELLO'
</pre>


In the above code, `my_string` is a string object, and we are calling the `upper()` method on it. The method is called by using the `.` operator. Methods are functions that can only be used on objects of certain classes. You will often see methods strung together, like below:


```python
my_string = "hello"
# This first makes the first letter uppercase, then swaps the cases of each letter
my_string.capitalize().swapcase()
```

<pre class="output-block">'hELLO'
</pre>

### Object Attributes

We'll be learning about some more complex objects today, like **numpy arrays**, which also have attributes. **Attributes** are properties of an object that can be accessed using the `.` operator. For example, numpy arrays have an attribute called `shape` that tells you the dimensions of the array. The difference between an attribute and a method is that attributes are information about a given object, rather than a task being performed on the object. Practically, this means that, while both attributes and methods are called on an object with the dot operator `.`, attributes are accessed without parentheses, so you don't need to call them like functions.


```python
# this makes a np array (we'll learn more about these shortly!)
my_array = np.array([1, 2, 3, 4, 5])

# this gets the size (total number of elements) of the array
my_array.size
```

<pre class="output-block">---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[7], line 2
      1 # this makes a np array (we'll learn more about these shortly!)
----> 2 my_array = np.array([1, 2, 3, 4, 5])
      4 # this gets the size (total number of elements) of the array
      5 my_array.size

NameError: name 'np' is not defined
</pre>

## Base Python Data Structures

When we want to store multiple pieces of data, we use data structures, which are a more complex type of object. We will go over two fundamental data structures that exist in base python (i.e. that don't require additional libraries). 

### Lists

**Lists** are one the most flexible of data structures in Python. They are created with `[]` and can contain any type of data. Each **element** in a list is separated by a comma. Lists are ordered and can be indexed, sliced, and concatenated just like strings. When lists are all numerical, they can also support mathematical operations like `max()` and `min()`. Lists can also be nested using another `[]` within the list.

Lists are our first introduction to a **mutable** data structure, meaning you can change a list without having to create a new one. Indeed, list methods may modify your data **in place** and/or **return** a new object. If the method modifies the object in place, its return value will be `None`. Modifying in place means you don't have to assign the result of the method to a new variable, while returning a new object means you do have to assign it. For example, `list.append(x)` updates the list in place, while `list.pop()` both returns the last element and removes it from the list in place.

Below are some useful operations and methods for lists. For a full list of methods, you can use `help()` on the list or consult the [docs :octicons-link-external-24:](https://docs.python.org/3/library/stdtypes.html#list){:target="_blank"} page.

**Operations and methods for lists**

| Operation/Method | Description |
| --- | --- |
| `+` | Concatenation |
| `*` | Repetition |
| `[]`, `[:]` | Indexing, slicing |
| `.append(x)` | Add `x` to the end of the list |
| `.extend([x, y, z])` | Add `[x, y, z]` to the end of the list |
| `.insert(i, x)` | Add `x` at index `i` of the list |
| `.pop(i)` | Remove and return the element at index `i`, defaults to last element if none given |

**Use cases for lists**

Lists are a data structure that is always there in the background, being useful. We see them when creating simple ordered collections to iterate through, when we need to store a sequence of data to reference later, or when we need to collected a bunch of objects together. Think of lists as a small temporary transport for data. Lists are not good for large datasets (because it will be slow) or when you need to do a lot of mathematical operations (because it lacks functionality).

### Dictionaries

**Dictionaries** store **key:value pairs**. Keys must be immutable and are typically strings or numerical identifiers, while the values can be just about anything, including other dictionaries, lists, or individual values. You can create a dictionary with `{}` or with the `dict()` function. The two ways to create a dictionary are shown below:

```python
my_dict = {'a': 1, 'b': 2, 'c': 3}
my_dict = dict(("a", 1), ("b", 2), ("c", 3))
```

In recent versions of Python (3.8+), dictionaries keys maintain the order in which they were added, which is useful to maintain consistency when looping over the keys. However, in previous versions of Python, dictionaries were unordered. You can't index or slice dictionaries (since dictionary elements aren't accessed by index). But you can retrieve items by their key, e.g. `my_dict["a"]` or `my_dict.get("a")`. Like lists, dictionaries are mutable, so you can add, remove, or update the key:value pairs in place. Other methods return "View objects" that allow you to see the items in the dictionary, but won't allow you to modify the dictionary, however these objects can usually be easily converted to lists with the `list()` function. Here are some useful methods for dictionaries:

**Operations and methods for dictionaries**

| Operation/Method | Description |
| --- | --- |
| `[<key>]` | Retrieve value by key |
| `.keys()` | Returns a view object of the keys |
| `.values()` | Returns a view object of the values |
| `.items()` | Returns a view object of the key:value pairs |
| `.update(dict)` | Updates the dictionary with the key:value pairs from another dictionary |

**Use cases for dictionaries**

Dictionaries are a data structure that is more specialized for information that can be organized in a key:value pair way. You may see dictionaries being used to store associations between a name/ID and some characteristics, or to store a set of parameters for a function, or to organize a hierarchical grouping of information. Dictionaries are optimized for fast access to the values by key and for flexible organization of the data. Although you can edit the values of a dictionary, they aren't good for mathematical operations or for ordered data.

## Learning to read documentation



Today our first lesson will be about how to read documentation, because we are going to start using libraries such as **numpy** and **pandas**, which have many features that we do not have the time to cover in detail. Instead, if you can read documentation efficiently, you can learn how to use these libraries on your own.


**Programming effectively actually involves a lot of reading**

Programming involves reading primarily documentation, but also code, search results, stackexchange queries, etc. These are just a few examples of what you'll read as you work on code. Reading the documentation of a package or library or software that you are using should probably be the first thing you do when you start using it. However, software docs pages are a much different sort of writing than we may be used to, if we're primarily used to reading journal articles, textbooks, and protocols. Knowing how and how much to read documentation is a skill that needs to be developed over time to suit your own needs. There's definitely no need to read every single page of documentation of a piece of software, especially for large libraries like `numpy` or `matplotlib`.

**There are a variety of ways software can be documented**

You may be handed a single script from a colleague to perform some action and that script may have **comments** in the code detailing what it does or what certain lines do. Individual functions may have what is called a **docstring**, which is a string that occurs immediately after the function definition detailing how do use that function, inputs, and outputs. Another type of documentation is a docs page or **API reference** on a website for that software, such as the page for the seaborn's [scatterplot :octicons-link-external-24:](https://seaborn.pydata.org/generated/seaborn.scatterplot.html){:target="_blank"} function. Many software packages also have some introductory pages like **vignettes** or **tutorials** that guide you through the basics of the software. The [Getting started tutorials :octicons-link-external-24:](https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html){:target="_blank"} of Pandas is a good example of this.

**What documentation are we meant to read?**

In general, documentation is meant to be a reference manual more than a textbook. A lot of documentation is really repetitive, because it has to exhaustively cover every single function, class, and use-case available to the user. I do not recommend reading documentation like a book or in any linear way. That's like learning a foreign language by reading the dictionary. For example, `numpy` has a variety of [mathematical functions :octicons-link-external-24:](https://numpy.org/doc/stable/reference/routines.math.html){:target="_blank"}, but you are not required to look at the doc page of each of those. It is enough to know that it exists and when you do want to use a particular one, to check the page of that specific function. The most important parts of the documentation to read first are the tutorials/user guides, which introduce the basic functionality of the software with some example code. Often times, this code is exactly what you need to get started. If you get stuck, then it's time to read the docs pages for the specific commands you are using.

### Anatomy of a docs page

Scientific articles typically have the same sections: Introduction, Methods, Results/Discussion. Similarly, docs pages for a function should all have some common components:

* Function name and how to call it
    * parameters in parentheses with any defaults showing
    * positional parameters first, keyword parameters after asterisk
* Description of function
* Detailed parameters that can be passed to each function
    * type of object that can be passed
    * description of what the parameter does
* Returns
    * type of object(s) returned
    * description of the object
* Examples

**Just the basics**

If this is your first time encountering the function, glance at the function name and description and then go directly to the examples. This will help you understand if this function does what you think it does and give you a template to use it.


>**Exercise:** TBD


**Troubleshooting**

Looking at a docs page is helpful for troubleshooting certain errors.

>**Exercise:** TBD

**Exploring**

If you are trying to find a specific way to customize the pie chart, it is worth reading the entire list of parameters to see what options are available.

>**Discussion:** TBD

## Refresher: importing libraries

Recall that we covered how to **import libraries** of functions previously. For instance, we can import the built-in `math` library and then use the functions it contains:


```python
import math
print(math.log(100))
```

<pre class="output-block">4.605170185988092
</pre>

We need to type `math.` so Python knows where to look for the `log()` function.

We can also use an **alias** if we don't want to type `math.` every time we use a function from the library:


```python
import math as m
print(m.log(100))
```

<pre class="output-block">4.605170185988092
</pre>

## Reading and writing data in base python

In this next section, we'll read data of bird names and bird sightings from two CSV files and then write out the total number of sightings for each bird to a new CSV file.

### Reading data line by line

A common way to read data in Python is line by line. This is useful when you have a file that is too large to fit into memory all at once. You can read the file line by line and process each line as you go. This is also useful when you need to parse a file that has a specific structure so that it can be read into a data structure like a numpy array or pandas dataframe. In this section, when we talk about files, we mean text files that contain data that exist on your local machine. This is different from the data structures we've been working with so far, which are in memory (in your python instance).

The syntax for opening a file is `open(filename, mode)`, where mode can be `r` for reading, `w` for writing, `a` for appending. Reading mode means that you can only read the file but not change it (on the disk). Writing mode means you are creating a new file or overwriting an existing file. Appending mode means you are adding to an existing file.

When you open a file, you can read it line by line using a `for` loop. While there are several ways to open a file in Python, the most efficient is with the `with` keyword, which will automatically close the file once you've done what you need. Here's an example of how that might look with a for loop to print each line of a file:

```python
with open('filename.txt', 'r') as file:
    for line in file:
        print(line)
```

The above code will print each line of the file to the console. Notice the use of the keyword `as`, similar to how we setup an **alias** when we import a library. Here it serves a similar purpose, giving us a name to refer to the file object we've opened. We can name it anything we want, but `file` was just an example. The `line` variable is how we refer to each line of the file as we iterate through it. Again, it's an arbitrary name.

This for loop is similar to how we iterate through a list. The only difference is that we're iterating through something that is being read from our local computer rather than an object in memory.

In the example, we are only printing the lines of the file, but just as with any for loop, you can do anything you want with each line, such as apply a function to it, split it up and store it in a data structure, or write different parts of it to a new file. So think of that `print(line)` line as a placeholder for whatever you want to do with the line.

### Vocab

|Term|Definition|
|---|---|
|File|A collection of data stored on a disk|
|Line|A string of characters that ends with a newline character|
|Newline character|A special character that indicates the end of a line, usually `\n`|
|Delimiter|A character that separates data fields in a line, usually a comma, tab, or space|
|Parsing|The process of extracting data from a file|
|Whitespace|Any character that represents a space, tab, or newline|
|Leading/trailing whitespace|Whitespace at the beginning or end of a string|


Let's work through a more concrete example of how we might read and then parse through a file. Let's suppose we have a list of taxon ids and bird names that we want to read into a **dictionary**. The file looks like this:

```
Anas rubripes,American Black Duck,6924
Fulica americana,American Coot,473
Spinus tristis,American Goldfinch,145310
Falco sparverius,American Kestrel,4665
```

First, run this block to download the file to the Jupyter notebook environment..


```python
# This line downloads the file locally to the same folder as your notebook
!wget https://raw.githubusercontent.com/harvardinformatics/python-intensive/refs/heads/main/data/bird_names.csv
```

<pre class="output-block">--2025-07-31 16:39:54--  https://raw.githubusercontent.com/harvardinformatics/python-intensive/refs/heads/main/data/bird_names.csv
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 185.199.108.133, 185.199.109.133, 185.199.110.133, ...
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|185.199.108.133|:443... connected.
HTTP request sent, awaiting response...
</pre>

<pre class="output-block">200 OK
Length: 4383 (4.3K) [text/plain]
Saving to: ‘bird_names.csv’


bird_names.csv        0%[                    ]       0  --.-KB/s               
bird_names.csv      100%[===================>]   4.28K  --.-KB/s    in 0s      

2025-07-31 16:39:54 (77.8 MB/s) - ‘bird_names.csv’ saved [4383/4383]
</pre>

Then, in the code below we first read the file line by line, then strip the whitespace and split the line by a comma. Then, we will create a dictionary where the key is the taxon id and the value is the common name of the bird.


```python
filename = 'bird_names.csv'

bird_names = dict()

with open(filename, 'r') as file:
    for line in file:
        line = line.strip().split(',')
        # split out line[2]
        bird_names[line[2]] = line[1]

print(bird_names)
```

<pre class="output-block">{'6924': 'American Black Duck', '473': 'American Coot', '145310': 'American Goldfinch', '4665': 'American Kestrel', '12727': 'American Robin', '474210': 'American Tree Sparrow', '3936': 'American Woodcock', '16010': 'Ash-throated Flycatcher', '5305': 'Bald Eagle', '9346': 'Baltimore Oriole', '19893': 'Barred Owl', '2548': 'Belted Kingfisher', '144815': 'Black-capped Chickadee', '4981': 'Black-crowned Night Heron', '199916': 'Black-throated Blue Warbler', '8229': 'Blue Jay', '7458': 'Brown Creeper', '10373': 'Brown-headed Cowbird', '6993': 'Bufflehead', '7089': 'Canada Goose', '7513': 'Carolina Wren', '7428': 'Cedar Waxwing', '6571': 'Chimney Swift', '9135': 'Chipping Sparrow', '9602': 'Common Grackle', '4626': 'Common Loon', '7004': 'Common Merganser', '8010': 'Common Raven', '9721': 'Common Yellowthroat', '5112': "Cooper's Hawk", '10094': 'Dark-eyed Junco', '10676': 'Dickcissel', '120479': 'Domestic Greylag Goose', '236935': 'Domestic Mallard', '1454382': 'Double-crested Cormorant', '792988': 'Downy Woodpecker', '16782': 'Eastern Kingbird', '17008': 'Eastern Phoebe', '494355': 'Eastern Red-tailed Hawk', '515821': 'Eastern Song Sparrow', '319123': 'Eastern Wild Turkey', '14850': 'European Starling', '544795': 'European house sparrow', '122767': 'Feral Pigeon', '9156': 'Fox Sparrow', '117100': 'Golden-crowned Kinglet', '14995': 'Gray Catbird', '4368': 'Great Black-backed Gull', '4956': 'Great Blue Heron', '16028': 'Great Crested Flycatcher', '20044': 'Great Horned Owl', '7047': 'Greater Scaup', '5020': 'Green Heron', '6937': 'Green-winged Teal', '514057': 'Greylag × Canada Goose', '792990': 'Hairy Woodpecker', '12890': 'Hermit Thrush', '204533': 'Herring Gull', '7109': 'Hooded Merganser', '4209': 'Horned Grebe', '199840': 'House Finch', '13858': 'House Sparrow', '7562': 'House Wren', '4793': 'Killdeer', '10479': 'Lark Sparrow', '7054': 'Lesser Scaup', '6930': 'Mallard', '326092': 'Mallard × Muscovy Duck', '4672': 'Merlin', '3454': 'Mourning Dove', '6921': 'Mute Swan', '9083': 'Northern Cardinal', '18236': 'Northern Flicker', '14886': 'Northern Mockingbird', '555736': 'Northern Yellow-shafted Flicker', '979757': 'Orange-crowned Warbler', '116999': 'Osprey', '62550': 'Ovenbird', '4647': 'Peregrine Falcon', '17364': 'Philadelphia Vireo', '4246': 'Pied-billed Grebe', '18205': 'Red-bellied Woodpecker', '6996': 'Red-breasted Merganser', '14823': 'Red-breasted Nuthatch', '5212': 'Red-tailed Hawk', '9744': 'Red-winged Blackbird', '7056': 'Redhead', '4364': 'Ring-billed Gull', '7044': 'Ring-necked Duck', '3017': 'Rock Pigeon', '1289388': 'Ruby-crowned Kinglet', '6432': 'Ruby-throated Hummingbird', '850859': 'Ruddy Duck', '9100': 'Song Sparrow', '72458': 'Spotted Sandpiper', '11935': 'Tree Swallow', '13632': 'Tufted Titmouse', '17394': 'Warbling Vireo', '14801': 'White-breasted Nuthatch', '9176': 'White-crowned Sparrow', '9184': 'White-throated Sparrow', '906': 'Wild Turkey', '7107': 'Wood Duck', '145238': 'Yellow Warbler', '18463': 'Yellow-bellied Sapsucker'}
</pre>

>*Discussion:* Explain each line

Here are some handy functions when working with lines in files. These are all string methods, so you can use them on any string, including strings that are read from a file.

**Useful functions for reading files by line**

| Function | Description |
| --- | --- |
| `.strip()` | Removes leading and trailing whitespace and newlines from a string |
| `.split()` | Splits a string into a list of strings based on a delimiter |
| `.join()` | Joins a list of strings into a single string with a delimiter |
| `line[:]` | Indexing and slicing works on strings too |
| `.replace(old, new)` | Replaces all instances of `old` with `new` in a string |

**Useful special characters**

Special characters in files are often used as delimiters or to indicate the end of a line. The two most common special characters are:

| Character | Description |
| --- | --- |
| `\n` | Newline character |
| `\t` | Tab character |

>**Exercise**: Copy the code above and modify it so that the dictionary keys are the taxon ids and the values are another dictionary, with keys 'scientific_name' and 'common_name' and values the appropriate entries for that bird species.
>
> For example, a sample dictionary entry should look like this:
> ```
> {6924: {'scientific_name': 'Anas rubripes', 'common_name': 'American Black Duck'}}
> ```


```python
filename = 'bird_names.csv'

# Your code here
bird_names = dict()

with open(filename, 'r') as file:
    for line in file:
        line = line.strip().split(',')
        bird_names[line[2]] = {'scientific_name': line[0], 'common_name': line[1]}

print(bird_names)
```

<pre class="output-block">{'6924': {'scientific_name': 'Anas rubripes', 'common_name': 'American Black Duck'}, '473': {'scientific_name': 'Fulica americana', 'common_name': 'American Coot'}, '145310': {'scientific_name': 'Spinus tristis', 'common_name': 'American Goldfinch'}, '4665': {'scientific_name': 'Falco sparverius', 'common_name': 'American Kestrel'}, '12727': {'scientific_name': 'Turdus migratorius', 'common_name': 'American Robin'}, '474210': {'scientific_name': 'Spizelloides arborea', 'common_name': 'American Tree Sparrow'}, '3936': {'scientific_name': 'Scolopax minor', 'common_name': 'American Woodcock'}, '16010': {'scientific_name': 'Myiarchus cinerascens', 'common_name': 'Ash-throated Flycatcher'}, '5305': {'scientific_name': 'Haliaeetus leucocephalus', 'common_name': 'Bald Eagle'}, '9346': {'scientific_name': 'Icterus galbula', 'common_name': 'Baltimore Oriole'}, '19893': {'scientific_name': 'Strix varia', 'common_name': 'Barred Owl'}, '2548': {'scientific_name': 'Megaceryle alcyon', 'common_name': 'Belted Kingfisher'}, '144815': {'scientific_name': 'Poecile atricapillus', 'common_name': 'Black-capped Chickadee'}, '4981': {'scientific_name': 'Nycticorax nycticorax', 'common_name': 'Black-crowned Night Heron'}, '199916': {'scientific_name': 'Setophaga caerulescens', 'common_name': 'Black-throated Blue Warbler'}, '8229': {'scientific_name': 'Cyanocitta cristata', 'common_name': 'Blue Jay'}, '7458': {'scientific_name': 'Certhia americana', 'common_name': 'Brown Creeper'}, '10373': {'scientific_name': 'Molothrus ater', 'common_name': 'Brown-headed Cowbird'}, '6993': {'scientific_name': 'Bucephala albeola', 'common_name': 'Bufflehead'}, '7089': {'scientific_name': 'Branta canadensis', 'common_name': 'Canada Goose'}, '7513': {'scientific_name': 'Thryothorus ludovicianus', 'common_name': 'Carolina Wren'}, '7428': {'scientific_name': 'Bombycilla cedrorum', 'common_name': 'Cedar Waxwing'}, '6571': {'scientific_name': 'Chaetura pelagica', 'common_name': 'Chimney Swift'}, '9135': {'scientific_name': 'Spizella passerina', 'common_name': 'Chipping Sparrow'}, '9602': {'scientific_name': 'Quiscalus quiscula', 'common_name': 'Common Grackle'}, '4626': {'scientific_name': 'Gavia immer', 'common_name': 'Common Loon'}, '7004': {'scientific_name': 'Mergus merganser', 'common_name': 'Common Merganser'}, '8010': {'scientific_name': 'Corvus corax', 'common_name': 'Common Raven'}, '9721': {'scientific_name': 'Geothlypis trichas', 'common_name': 'Common Yellowthroat'}, '5112': {'scientific_name': 'Accipiter cooperii', 'common_name': "Cooper's Hawk"}, '10094': {'scientific_name': 'Junco hyemalis', 'common_name': 'Dark-eyed Junco'}, '10676': {'scientific_name': 'Spiza americana', 'common_name': 'Dickcissel'}, '120479': {'scientific_name': 'Anser anser domesticus', 'common_name': 'Domestic Greylag Goose'}, '236935': {'scientific_name': 'Anas platyrhynchos domesticus', 'common_name': 'Domestic Mallard'}, '1454382': {'scientific_name': 'Nannopterum auritum', 'common_name': 'Double-crested Cormorant'}, '792988': {'scientific_name': 'Dryobates pubescens', 'common_name': 'Downy Woodpecker'}, '16782': {'scientific_name': 'Tyrannus tyrannus', 'common_name': 'Eastern Kingbird'}, '17008': {'scientific_name': 'Sayornis phoebe', 'common_name': 'Eastern Phoebe'}, '494355': {'scientific_name': 'Buteo jamaicensis borealis', 'common_name': 'Eastern Red-tailed Hawk'}, '515821': {'scientific_name': 'Melospiza melodia melodia', 'common_name': 'Eastern Song Sparrow'}, '319123': {'scientific_name': 'Meleagris gallopavo silvestris', 'common_name': 'Eastern Wild Turkey'}, '14850': {'scientific_name': 'Sturnus vulgaris', 'common_name': 'European Starling'}, '544795': {'scientific_name': 'Passer domesticus domesticus', 'common_name': 'European house sparrow'}, '122767': {'scientific_name': 'Columba livia domestica', 'common_name': 'Feral Pigeon'}, '9156': {'scientific_name': 'Passerella iliaca', 'common_name': 'Fox Sparrow'}, '117100': {'scientific_name': 'Regulus satrapa', 'common_name': 'Golden-crowned Kinglet'}, '14995': {'scientific_name': 'Dumetella carolinensis', 'common_name': 'Gray Catbird'}, '4368': {'scientific_name': 'Larus marinus', 'common_name': 'Great Black-backed Gull'}, '4956': {'scientific_name': 'Ardea herodias', 'common_name': 'Great Blue Heron'}, '16028': {'scientific_name': 'Myiarchus crinitus', 'common_name': 'Great Crested Flycatcher'}, '20044': {'scientific_name': 'Bubo virginianus', 'common_name': 'Great Horned Owl'}, '7047': {'scientific_name': 'Aythya marila', 'common_name': 'Greater Scaup'}, '5020': {'scientific_name': 'Butorides virescens', 'common_name': 'Green Heron'}, '6937': {'scientific_name': 'Anas crecca', 'common_name': 'Green-winged Teal'}, '514057': {'scientific_name': 'Anser anser × Branta canadensis', 'common_name': 'Greylag × Canada Goose'}, '792990': {'scientific_name': 'Dryobates villosus', 'common_name': 'Hairy Woodpecker'}, '12890': {'scientific_name': 'Catharus guttatus', 'common_name': 'Hermit Thrush'}, '204533': {'scientific_name': 'Larus argentatus', 'common_name': 'Herring Gull'}, '7109': {'scientific_name': 'Lophodytes cucullatus', 'common_name': 'Hooded Merganser'}, '4209': {'scientific_name': 'Podiceps auritus', 'common_name': 'Horned Grebe'}, '199840': {'scientific_name': 'Haemorhous mexicanus', 'common_name': 'House Finch'}, '13858': {'scientific_name': 'Passer domesticus', 'common_name': 'House Sparrow'}, '7562': {'scientific_name': 'Troglodytes aedon', 'common_name': 'House Wren'}, '4793': {'scientific_name': 'Charadrius vociferus', 'common_name': 'Killdeer'}, '10479': {'scientific_name': 'Chondestes grammacus', 'common_name': 'Lark Sparrow'}, '7054': {'scientific_name': 'Aythya affinis', 'common_name': 'Lesser Scaup'}, '6930': {'scientific_name': 'Anas platyrhynchos', 'common_name': 'Mallard'}, '326092': {'scientific_name': 'Anas platyrhynchos × cairina moschata', 'common_name': 'Mallard × Muscovy Duck'}, '4672': {'scientific_name': 'Falco columbarius', 'common_name': 'Merlin'}, '3454': {'scientific_name': 'Zenaida macroura', 'common_name': 'Mourning Dove'}, '6921': {'scientific_name': 'Cygnus olor', 'common_name': 'Mute Swan'}, '9083': {'scientific_name': 'Cardinalis cardinalis', 'common_name': 'Northern Cardinal'}, '18236': {'scientific_name': 'Colaptes auratus', 'common_name': 'Northern Flicker'}, '14886': {'scientific_name': 'Mimus polyglottos', 'common_name': 'Northern Mockingbird'}, '555736': {'scientific_name': 'Colaptes auratus luteus', 'common_name': 'Northern Yellow-shafted Flicker'}, '979757': {'scientific_name': 'Leiothlypis celata', 'common_name': 'Orange-crowned Warbler'}, '116999': {'scientific_name': 'Pandion haliaetus', 'common_name': 'Osprey'}, '62550': {'scientific_name': 'Seiurus aurocapilla', 'common_name': 'Ovenbird'}, '4647': {'scientific_name': 'Falco peregrinus', 'common_name': 'Peregrine Falcon'}, '17364': {'scientific_name': 'Vireo philadelphicus', 'common_name': 'Philadelphia Vireo'}, '4246': {'scientific_name': 'Podilymbus podiceps', 'common_name': 'Pied-billed Grebe'}, '18205': {'scientific_name': 'Melanerpes carolinus', 'common_name': 'Red-bellied Woodpecker'}, '6996': {'scientific_name': 'Mergus serrator', 'common_name': 'Red-breasted Merganser'}, '14823': {'scientific_name': 'Sitta canadensis', 'common_name': 'Red-breasted Nuthatch'}, '5212': {'scientific_name': 'Buteo jamaicensis', 'common_name': 'Red-tailed Hawk'}, '9744': {'scientific_name': 'Agelaius phoeniceus', 'common_name': 'Red-winged Blackbird'}, '7056': {'scientific_name': 'Aythya americana', 'common_name': 'Redhead'}, '4364': {'scientific_name': 'Larus delawarensis', 'common_name': 'Ring-billed Gull'}, '7044': {'scientific_name': 'Aythya collaris', 'common_name': 'Ring-necked Duck'}, '3017': {'scientific_name': 'Columba livia', 'common_name': 'Rock Pigeon'}, '1289388': {'scientific_name': 'Corthylio calendula', 'common_name': 'Ruby-crowned Kinglet'}, '6432': {'scientific_name': 'Archilochus colubris', 'common_name': 'Ruby-throated Hummingbird'}, '850859': {'scientific_name': 'Oxyura jamaicensis', 'common_name': 'Ruddy Duck'}, '9100': {'scientific_name': 'Melospiza melodia', 'common_name': 'Song Sparrow'}, '72458': {'scientific_name': 'Actitis macularius', 'common_name': 'Spotted Sandpiper'}, '11935': {'scientific_name': 'Tachycineta bicolor', 'common_name': 'Tree Swallow'}, '13632': {'scientific_name': 'Baeolophus bicolor', 'common_name': 'Tufted Titmouse'}, '17394': {'scientific_name': 'Vireo gilvus', 'common_name': 'Warbling Vireo'}, '14801': {'scientific_name': 'Sitta carolinensis', 'common_name': 'White-breasted Nuthatch'}, '9176': {'scientific_name': 'Zonotrichia leucophrys', 'common_name': 'White-crowned Sparrow'}, '9184': {'scientific_name': 'Zonotrichia albicollis', 'common_name': 'White-throated Sparrow'}, '906': {'scientific_name': 'Meleagris gallopavo', 'common_name': 'Wild Turkey'}, '7107': {'scientific_name': 'Aix sponsa', 'common_name': 'Wood Duck'}, '145238': {'scientific_name': 'Setophaga petechia', 'common_name': 'Yellow Warbler'}, '18463': {'scientific_name': 'Sphyrapicus varius', 'common_name': 'Yellow-bellied Sapsucker'}}
</pre>

>**Exercise**: Why did we use a dictionary to store the data in the previous exercise? Think about what features of a dictionary make it a good choice or what features of lists or arrays make them a bad choice.

Below is an excerpt from a file of iNaturalist observations of birds in Cambridge, MA from the year 2023. We will loop through the file and count the number of observations of each species. We will also use the previously created dictionary to get the species names.

```csv
id,time_observed_at,taxon_id
145591043,2023-01-01 17:33:31 UTC,14886
145610149,2023-01-01 20:55:00 UTC,7004
145610383,2023-01-01 21:13:00 UTC,6993
145611915,2023-01-01 21:12:00 UTC,13858
```

Run the code block below to download the file to the Jupyter notebook environment.


```python
# This line downloads the file locally to the same folder as your notebook
!wget https://raw.githubusercontent.com/harvardinformatics/python-intensive/refs/heads/main/data/bird_observations.csv
```

<pre class="output-block">--2025-07-31 16:39:54--  https://raw.githubusercontent.com/harvardinformatics/python-intensive/refs/heads/main/data/bird_observations.csv
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 185.199.111.133, 185.199.109.133, 185.199.110.133, ...
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|185.199.111.133|:443... connected.
HTTP request sent, awaiting response...
</pre>

<pre class="output-block">200 OK
Length: 50448 (49K) [text/plain]
Saving to: ‘bird_observations.csv’


bird_observations.c   0%[                    ]       0  --.-KB/s
</pre>

<pre class="output-block">
bird_observations.c 100%[===================>]  49.27K  --.-KB/s    in 0.005s  

2025-07-31 16:39:54 (9.48 MB/s) - ‘bird_observations.csv’ saved [50448/50448]
</pre>

>**Exercise:** Work with a neighbor or two to do the following exercise:
> Loop through the file and count the number of observations of each species. After all the observations have been counted, print all the species names and the number of observations. You will need to use the dictionary you created in the previous exercise to get the species names. It's up to you what kind of data structure (if any) you want to use to store the counts.
>
> 1. Write out pseudocode for what you will do for each line in your birdfile
> 2. Try to turn the pseudocode into python code. If there's something you want to do, but don't know the syntax or function, raise your hand and we can help you.
> 3. Find out how many European Starlings were observed as proof that your code works.


```python
# Your code here
filename = 'bird_observations.csv' #keep

bird_observations = dict()

with open(filename, 'r') as birdfile: #keep
    # skip the header
    next(birdfile) #keep
    for line in birdfile: #keep
        # clean up the line and split into list
        observation = line.strip().split(',')
        # get the bird id
        id = observation[2]
        # get the bird name by looking up in the bird_names dictionary
        name = bird_names[id]['common_name']
        # if this is the first time we're seeing the bird, add it to our observations dict
        if name not in bird_observations:
            bird_observations[name] = 0
        # increment the count by 1
        bird_observations[name] += 1
print(bird_observations)
```

<pre class="output-block">{'Northern Mockingbird': 23, 'Common Merganser': 4, 'Bufflehead': 9, 'House Sparrow': 69, 'European Starling': 51, 'Northern Cardinal': 28, 'Mourning Dove': 31, 'Blue Jay': 39, 'American Black Duck': 2, 'Domestic Mallard': 14, 'Mute Swan': 33, 'Green-winged Teal': 8, 'American Robin': 92, 'Mallard': 49, 'Great Blue Heron': 26, 'Red-tailed Hawk': 36, 'Canada Goose': 112, 'Downy Woodpecker': 24, 'Ring-necked Duck': 22, 'Wild Turkey': 82, 'Common Loon': 9, 'Horned Grebe': 4, 'Redhead': 8, 'Feral Pigeon': 31, 'Golden-crowned Kinglet': 7, 'Red-bellied Woodpecker': 15, 'Hooded Merganser': 18, 'Belted Kingfisher': 3, 'Red-winged Blackbird': 35, 'Black-capped Chickadee': 14, 'Ruddy Duck': 2, 'Bald Eagle': 2, 'Dark-eyed Junco': 9, 'Carolina Wren': 7, 'House Finch': 19, 'White-throated Sparrow': 5, 'Song Sparrow': 24, 'Yellow-bellied Sapsucker': 3, 'White-breasted Nuthatch': 10, 'Eastern Red-tailed Hawk': 5, 'Tufted Titmouse': 8, "Cooper's Hawk": 17, 'Domestic Greylag Goose': 14, 'Rock Pigeon': 9, 'American Coot': 1, 'Greylag × Canada Goose': 1, 'Eastern Wild Turkey': 1, 'Brown Creeper': 7, 'Hairy Woodpecker': 2, 'Northern Flicker': 6, 'Greater Scaup': 1, 'Red-breasted Merganser': 2, 'American Woodcock': 7, 'Red-breasted Nuthatch': 1, 'Great Horned Owl': 23, 'Peregrine Falcon': 5, 'American Goldfinch': 18, 'Barred Owl': 2, 'Black-crowned Night Heron': 2, 'Tree Swallow': 11, 'Common Grackle': 14, 'Hermit Thrush': 4, 'Northern Yellow-shafted Flicker': 1, 'Chipping Sparrow': 3, 'Killdeer': 2, 'Gray Catbird': 20, 'Double-crested Cormorant': 17, 'Yellow Warbler': 3, 'Warbling Vireo': 2, 'Baltimore Oriole': 7, 'Common Yellowthroat': 2, 'White-crowned Sparrow': 2, 'Black-throated Blue Warbler': 1, 'Ovenbird': 1, 'Brown-headed Cowbird': 4, 'House Wren': 1, 'Cedar Waxwing': 4, 'European house sparrow': 1, 'Herring Gull': 4, 'Eastern Kingbird': 7, 'Great Black-backed Gull': 1, 'Green Heron': 10, 'Great Crested Flycatcher': 1, 'Wood Duck': 6, 'American Kestrel': 1, 'Osprey': 1, 'Ruby-throated Hummingbird': 3, 'Spotted Sandpiper': 2, 'Chimney Swift': 1, 'Eastern Phoebe': 1, 'Lark Sparrow': 2, 'Ring-billed Gull': 1, 'Dickcissel': 1, 'Merlin': 1, 'Ash-throated Flycatcher': 6, 'Pied-billed Grebe': 5, 'Lesser Scaup': 2, 'Orange-crowned Warbler': 2, 'Eastern Song Sparrow': 1, 'Philadelphia Vireo': 1, 'Ruby-crowned Kinglet': 2, 'Mallard × Muscovy Duck': 1, 'Fox Sparrow': 1, 'American Tree Sparrow': 1, 'Common Raven': 1}
</pre>

If you routinely find yourself reading delimited files, you might want to use the `csv` library. The `csv` library also has the ability to parse Excel files or read and write to/from dictionaries directly. For more information, here's the [doc page :octicons-link-external-24:](https://docs.python.org/3/library/csv.html){:target="_blank"}. Here's what the above code would look like using the `csv` module:


```python
import csv

filename = 'bird_observations.csv'

bird_observations = dict()

with open(filename, 'r') as birdfile:
    # this line takes the place of us having to strip and split the lines
    reader = csv.reader(birdfile, delimiter=',')
    # skip the header
    next(reader)
    for row in reader:
        id = row[2]
        name = bird_names[id]['common_name']
        if name not in bird_observations:
            bird_observations[name] = 0
        bird_observations[name] += 1
print(bird_observations)
```

<pre class="output-block">{'Northern Mockingbird': 23, 'Common Merganser': 4, 'Bufflehead': 9, 'House Sparrow': 69, 'European Starling': 51, 'Northern Cardinal': 28, 'Mourning Dove': 31, 'Blue Jay': 39, 'American Black Duck': 2, 'Domestic Mallard': 14, 'Mute Swan': 33, 'Green-winged Teal': 8, 'American Robin': 92, 'Mallard': 49, 'Great Blue Heron': 26, 'Red-tailed Hawk': 36, 'Canada Goose': 112, 'Downy Woodpecker': 24, 'Ring-necked Duck': 22, 'Wild Turkey': 82, 'Common Loon': 9, 'Horned Grebe': 4, 'Redhead': 8, 'Feral Pigeon': 31, 'Golden-crowned Kinglet': 7, 'Red-bellied Woodpecker': 15, 'Hooded Merganser': 18, 'Belted Kingfisher': 3, 'Red-winged Blackbird': 35, 'Black-capped Chickadee': 14, 'Ruddy Duck': 2, 'Bald Eagle': 2, 'Dark-eyed Junco': 9, 'Carolina Wren': 7, 'House Finch': 19, 'White-throated Sparrow': 5, 'Song Sparrow': 24, 'Yellow-bellied Sapsucker': 3, 'White-breasted Nuthatch': 10, 'Eastern Red-tailed Hawk': 5, 'Tufted Titmouse': 8, "Cooper's Hawk": 17, 'Domestic Greylag Goose': 14, 'Rock Pigeon': 9, 'American Coot': 1, 'Greylag × Canada Goose': 1, 'Eastern Wild Turkey': 1, 'Brown Creeper': 7, 'Hairy Woodpecker': 2, 'Northern Flicker': 6, 'Greater Scaup': 1, 'Red-breasted Merganser': 2, 'American Woodcock': 7, 'Red-breasted Nuthatch': 1, 'Great Horned Owl': 23, 'Peregrine Falcon': 5, 'American Goldfinch': 18, 'Barred Owl': 2, 'Black-crowned Night Heron': 2, 'Tree Swallow': 11, 'Common Grackle': 14, 'Hermit Thrush': 4, 'Northern Yellow-shafted Flicker': 1, 'Chipping Sparrow': 3, 'Killdeer': 2, 'Gray Catbird': 20, 'Double-crested Cormorant': 17, 'Yellow Warbler': 3, 'Warbling Vireo': 2, 'Baltimore Oriole': 7, 'Common Yellowthroat': 2, 'White-crowned Sparrow': 2, 'Black-throated Blue Warbler': 1, 'Ovenbird': 1, 'Brown-headed Cowbird': 4, 'House Wren': 1, 'Cedar Waxwing': 4, 'European house sparrow': 1, 'Herring Gull': 4, 'Eastern Kingbird': 7, 'Great Black-backed Gull': 1, 'Green Heron': 10, 'Great Crested Flycatcher': 1, 'Wood Duck': 6, 'American Kestrel': 1, 'Osprey': 1, 'Ruby-throated Hummingbird': 3, 'Spotted Sandpiper': 2, 'Chimney Swift': 1, 'Eastern Phoebe': 1, 'Lark Sparrow': 2, 'Ring-billed Gull': 1, 'Dickcissel': 1, 'Merlin': 1, 'Ash-throated Flycatcher': 6, 'Pied-billed Grebe': 5, 'Lesser Scaup': 2, 'Orange-crowned Warbler': 2, 'Eastern Song Sparrow': 1, 'Philadelphia Vireo': 1, 'Ruby-crowned Kinglet': 2, 'Mallard × Muscovy Duck': 1, 'Fox Sparrow': 1, 'American Tree Sparrow': 1, 'Common Raven': 1}
</pre>

### Writing data by line

Writing data to a file is similar to reading data from a file. You can open a file in write mode and then write to it line by line using the `print()` method, but this time passing in the variable we've stored the opened file in (in our case the variable is unimaginatively named `file`). Here's an example of writing a list of strings to a file:


```python
my_text = ['this is a test', 'this is another test', 'this is the final test']

with open('my_text.txt', 'w') as file:
    for line in my_text:
        print(line, file=file)

# reading it back
with open('my_text.txt', 'r') as file:
    for line in file:
        print(line)
```

<pre class="output-block">this is a test

this is another test

this is the final test
</pre>

>**BONUS Exercise:** Use the `csv` module to write the species counts to a new file. The file should have two columns: the species name and the number of observations. The file should be comma-delimited. How this is written may depend on how you stored the species counts.


```python
# your code here

import csv

with open('bird_counts.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['bird', 'count'])
    for bird, count in bird_observations.items():
        writer.writerow([bird, count])
```

# Pandas

In this section, we will learn about a python package called `pandas` that contains very helpful functions and data structures just for flat data types like the tab or comma-delimited files you might normally read in Excel. In previous iterations of this class, we taught both `pandas` and `numpy`. In this workshop, we will focus on `pandas` only, and do a deeper dive. 

## Importing data to pandas
One of the most useful features of pandas DataFrames is its ability to easily perform complex data transformations. This makes it a powerful tool for cleaning, filtering, and summarizing tabular data. As shown above, we can manually create a DataFrame from scratch, but more commonly you will want to read in data from an external source, such as the output of a bioinformatic program, and do some manipulation of it. Let's read some data into a DataFrame to demonstrate. 

Below you can see an example of how to read files into pandas using the `pd.read_csv()` function. The `csv` stands for 'comma-separated values', which means by defaults it will assume that our columns are separated by **commas**; if we wanted to change the delimiter (e.g. in the case of a tab-separated file), we can set the delimiter explicitly using the `sep=` argument. 


```python
penguins = pd.read_csv("https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2020/2020-07-28/penguins.csv", sep=',')

# The head() function from pandas prints only the first N lines of a dataframe (default: 10)
penguins.head()
```

<pre class="output-block">---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[18], line 1
----> 1 penguins = pd.read_csv("https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2020/2020-07-28/penguins.csv", sep=',')
      3 # The head() function from pandas prints only the first N lines of a dataframe (default: 10)
      4 penguins.head()

NameError: name 'pd' is not defined
</pre>

When importing data into a DataFrame, pandas automatically detects what data type each column should be. For example, if the column contains only numbers, it will be imported as an floating point or integer data type. If the column contains strings or a mixture of strings and numbers, it will be imported as an "object" data type. Below are the different data types for the penguins column. 


```python
penguins.info()
```

<pre class="output-block">---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[19], line 1
----> 1 penguins.info()

NameError: name 'penguins' is not defined
</pre>

### Looping through a dataframe
As a note, if we want to go through a dataframe line-by-line (i.e. row by row), because both the rows and columns are indexed it requires slightly more syntax than looping through other data structures (e.g. a dictionary or list). Specifically we need to use the `.iterrows()` method to make the data frame iterable. The `.iterrows()` method outputs each row as a `Series` object with a row index and the column:   


```python
for index, row in penguins.iterrows():
    print(f"Row index: {index}, {row['species']}, {row['island']}")
```

<pre class="output-block">---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[20], line 1
----> 1 for index, row in penguins.iterrows():
      2     print(f"Row index: {index}, {row['species']}, {row['island']}")

NameError: name 'penguins' is not defined
</pre>

This can be slow for very large dataframes, but is useful if you need to perform actions on individual rows.

>Consider: based on what we've learned the past several days, what are some *limitations* of `numpy`? Can you think of any tasks you might want to do or analysis you might like to perform that would be difficult with `numpy`? Does this give you a guess as to what `pandas` specializes in?

Answer: `numpy` is specialized primarily for numerical operations, e.g. matrix multiplication, vector math, etc., but is more limited when dealing with other data types such as string, python objects, etc. In contrast, `pandas` objects are able to handle mixed data easily! As you will often run into this type of data when doing bioinformatics, `pandas` can be very useful.

Before we dive into the syntax, let's take a look at an example real-world application of `pandas` for a task that you might commonly face in biology. We are going to use the "Palmer penguins" dataset, which is a collection of various biometric data for several different penguin species and is a commonly used example dataset. Let's take a quick look at what the data looks like.

In the Palmer penguins dataset, each row represents an individual penguin, and each column represent a different measurement or characteristic of the penguin, such as its body mass or island of origin. The data are organized in this way so that variables (things we may want to compare against each other) are the columns while observations (the individual penguins) are the rows. This is a common way to organize data in data science and is called **tidy data**. Tidy data formatting also makes it easy to use code to manipulate and analyze, which we will see in this lesson. 



```python
penguins = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2020/2020-07-28/penguins.csv')
penguins.head()
```

<pre class="output-block">---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[21], line 1
----> 1 penguins = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2020/2020-07-28/penguins.csv')
      2 penguins.head()

NameError: name 'pd' is not defined
</pre>

Here is an example of a transformation that we will be able to do with `pandas` that would be difficult to do manually or with `numpy`. We can summarize the data by calculating the average body mass (in kg) of each penguin species, broken up by sex. Using a few lines of code we can go from our raw data to a table that looks like this:


| species   | sex    | body_mass_kg|
|-----------|--------|----------|
| Adelie    | female | 3.368836 |
| Adelie    | male   | 4.043493 |
| Chinstrap | female | 3.527206 |
| Chinstrap | male   | 3.938971 |
| Gentoo    | female | 4.679741 |
| Gentoo    | male   | 5.484836 |


Now, let's get started learning how this is done!


## Pandas Series
A `Series` is the simplest data structure in Pandas. They are one dimensional (1D) objects composed of a **single data type** of any variety (string, integers); you can basically think of them as a single column in a spreadsheet. They are similar to arrays in `numpy`, however unlike those other 1D structures Series also have **label-based indexing**, meaning each element in the object can be accessed by specifying its specific label. In that way, they are similar to dictionaries in python. 

We can manually create a Series in several ways:

Using the `pd.Series()` function, we provide it the data we want to store as a list, and optionally we can give each row of the data a label using the `index` argument. If we don't give it the index argument, it will automatically assign a numerical index to each row starting from 0. 

When we print the Series, it will display as a column with the index on the left and the data on the right. The type of data being held in the series will be displayed at the bottom of the output. 



```python
#Using the pd.Series method:
s0 = pd.Series([10, 20, 30, 40])

print(s0)
```

<pre class="output-block">---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[22], line 2
      1 #Using the pd.Series method:
----> 2 s0 = pd.Series([10, 20, 30, 40])
      4 print(s0)

NameError: name 'pd' is not defined
</pre>


```python
#Using the pd.Series method:
s1 = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])

print(s1)
```

<pre class="output-block">---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[23], line 2
      1 #Using the pd.Series method:
----> 2 s1 = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
      4 print(s1)

NameError: name 'pd' is not defined
</pre>

Another way to create a Series is to convert a (non-nested) dictionary into a Series. The keys of the dictionary will become the index labels while the values will become the data. 


```python
# Converting from dictionary to series
my_dictionary = {'first': 10, 'second': 20, 'third': 30}
s2 = pd.Series(my_dictionary)

print(s2)
```

<pre class="output-block">---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[24], line 3
      1 # Converting from dictionary to series
      2 my_dictionary = {'first': 10, 'second': 20, 'third': 30}
----> 3 s2 = pd.Series(my_dictionary)
      5 print(s2)

NameError: name 'pd' is not defined
</pre>

We can then access specific elements in the Series by referring to its index label enclosed in quotes and brackets. This is very similar to how a dictionary works!


```python
print(s0[0])

print(s1["a"])

print(s2["second"])
```

<pre class="output-block">---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[25], line 1
----> 1 print(s0[0])
      3 print(s1["a"])
      5 print(s2["second"])

NameError: name 's0' is not defined
</pre>

### Multi-indexed Series

Series objects may have multiple levels of indices. We call this **multi-indexed**. Using layers of indexing is a way of representing two-dimensional data within a one-dimensional `Series` object. Some people really like using multi-indexed Series. You can create a multi-indexed series by passing a list of lists to the `index` argument of the `pd.Series()` function. The first list will be the outermost level of the index, the second list will be the next level, and so on.


```python
my_index = [["California", "California", "New York", "New York", "Texas", "Texas"], 
            [2001, 2002, 2001, 2002, 2001, 2002]]
my_values = [1.5, 1.7, 3.6, 4.2, 3.2, 4.5]

s3 = pd.Series(my_values, index=my_index)

print(s3)
```

<pre class="output-block">---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[26], line 5
      1 my_index = [["California", "California", "New York", "New York", "Texas", "Texas"], 
      2             [2001, 2002, 2001, 2002, 2001, 2002]]
      3 my_values = [1.5, 1.7, 3.6, 4.2, 3.2, 4.5]
----> 5 s3 = pd.Series(my_values, index=my_index)
      7 print(s3)

NameError: name 'pd' is not defined
</pre>

Retrieving an item from this data structure is similar to a nested dictionary, using successive `[]` notation. Or, you can passs it a tuple. You must pass the index labels in the order they were created (left to right)


```python
print(s3["California"])

print("---")
print(s3["California"][2001])

print("---")
print(s3[("California", 2001)])

print("---")
# you can also use slicing to select multiple elements
print(s3["California":"New York"])
```

<pre class="output-block">---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[27], line 1
----> 1 print(s3["California"])
      3 print("---")
      4 print(s3["California"][2001])

NameError: name 's3' is not defined
</pre>

In our work, we typically don't use multi-indexed Series. However, they are often the output of pandas functions, so it's good to know how to work with them. If you don't like the idea of multi-indexed Series, you can always convert them to a DataFrame using the `reset_index()` method.


```python
s3.reset_index()
```

<pre class="output-block">---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[28], line 1
----> 1 s3.reset_index()

NameError: name 's3' is not defined
</pre>

## Pandas DataFrame

While Series is a "one-dimensional" data structure, DataFrames are two-dimensional. Where Series can only contain one type of data, the pandas DataFrame can have a combination of numerical and categorical data. Additionally, DataFrames allow you do have labels for your rows and columns. 

DataFrames are essentially a **collection of Series objects**. You can also think of python DataFrames as spreadsheets from Excel or dataframes from R. 

Let's manually create a simple dataframe in pandas to showcase their behavior. In the below code, we create a dictionary where the keys are the column names and the values are lists of data. We then pass this dictionary to the `pd.DataFrame()` function to create a DataFrame. 

When we print the DataFrame, it will display as a table with the column names at the top and the data below. The index (in this case, automatically generated numerical index starting at 0) will be displayed on the left side of the table.


```python
tournamentStats = {
    "wrestler": ["Terunofuji", "Ura", "Shodai", "Takanosho"],
    "wins": [13, 6, 10, 12],
    "rank": ["yokozuna", "maegashira2", "komusubi", "maegashira6"]
}

#Converting to a pandas DataFrame
sumo = pd.DataFrame(tournamentStats)

print(sumo)
```

<pre class="output-block">---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[29], line 8
      1 tournamentStats = {
      2     "wrestler": ["Terunofuji", "Ura", "Shodai", "Takanosho"],
      3     "wins": [13, 6, 10, 12],
      4     "rank": ["yokozuna", "maegashira2", "komusubi", "maegashira6"]
      5 }
      7 #Converting to a pandas DataFrame
----> 8 sumo = pd.DataFrame(tournamentStats)
     10 print(sumo)

NameError: name 'pd' is not defined
</pre>

Pandas dataframes have many **attributes**, including `shape`, `columns`, `index`, `dtypes`. These are useful for understanding the structure of the dataframe.


```python
print(sumo.shape)

print("---")
print(sumo.columns)

print("---")
print(sumo.index)

print("---")
print(sumo.dtypes)
```

<pre class="output-block">---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[30], line 1
----> 1 print(sumo.shape)
      3 print("---")
      4 print(sumo.columns)

NameError: name 'sumo' is not defined
</pre>

Pandas DataFrames also have the handy `info()` function that summarizes the contents of the dataframe, including counts of the non-null values of each column and the data type of each column.


```python
sumo.info()
```

<pre class="output-block">---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[31], line 1
----> 1 sumo.info()

NameError: name 'sumo' is not defined
</pre>

## Selecting data in a Pandas dataframe

As with series objects, pandas dataframes rows and columns are *explicitly indexed*, which means that every row and column has a label associated with it. You can think of the explicit indices as the being the names of the rows and the names of the columns.  

Unfortunately, in pandas the syntax for subsetting rows v.s. columns is different and can get a little confusing, so let's go through several different use cases.

### Selecting columns
We can always check the names of the columns in a Pandas dataframe byt using the built-in `.columns` method, which simply lists the column index:


```python
sumo.columns
```

<pre class="output-block">---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[32], line 1
----> 1 sumo.columns

NameError: name 'sumo' is not defined
</pre>

If we want to refer to a specific column, we can specify its index (enclosed in double quotes) inside of square brackets `[]` like so:


```python
#Single column:
sumo["wrestler"]
```

<pre class="output-block">---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[33], line 2
      1 #Single column:
----> 2 sumo["wrestler"]

NameError: name 'sumo' is not defined
</pre>

If we want to refer to *multiple* columns, we need to pass the columns as a **list** by enclosing the column indices in square brackets, so you will end up with *double brackets*:


```python
#Multiple columns (note the double []!):
sumo[["wrestler", "rank"]]
```

<pre class="output-block">---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[34], line 2
      1 #Multiple columns (note the double []!):
----> 2 sumo[["wrestler", "rank"]]

NameError: name 'sumo' is not defined
</pre>

### Selecting rows:

The syntax for selecting specific rows is slightly different. Let's first check the labels of the row index; to do this we use the `.index` method:


```python
print(sumo.index)
```

<pre class="output-block">---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[35], line 1
----> 1 print(sumo.index)

NameError: name 'sumo' is not defined
</pre>

Here we can see that while the column index labels were strings, the row index labels are *numerical values*, in this case `0` thru `3`. If we wanted to pull out the first row, we need to specify its index label (`0`) in combination with the `.loc` method (which is required for rows): 


```python
sumo.loc[0]
```

<pre class="output-block">---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[36], line 1
----> 1 sumo.loc[0]

NameError: name 'sumo' is not defined
</pre>

If we want to select multiple rows, like with columns we need to pass it as a list using the double brackets. If we want to specify a **range** of rows (i.e. from this row to that row), we **don't** use double brackets and instead use `:`:


```python
print(sumo.loc[[0,1]])
```

<pre class="output-block">---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[37], line 1
----> 1 print(sumo.loc[[0,1]])

NameError: name 'sumo' is not defined
</pre>


```python

print(sumo.loc[0:2])
```

<pre class="output-block">---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[38], line 1
----> 1 print(sumo.loc[0:2])

NameError: name 'sumo' is not defined
</pre>

Note that in this case the row index labels are numbers, but do not have to be numerical, and can have string labels similar to columns. Let's show how we could change the row index labels by taking the column with the wrestler's rank and setting it as the index label (note that the labels should be unique!):


```python
sumo = sumo.set_index("rank")

print(sumo)
```

<pre class="output-block">---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[39], line 1
----> 1 sumo = sumo.set_index("rank")
      3 print(sumo)

NameError: name 'sumo' is not defined
</pre>


```python
sumo.loc["yokozuna"]
```

<pre class="output-block">---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[40], line 1
----> 1 sumo.loc["yokozuna"]

NameError: name 'sumo' is not defined
</pre>

We also need to use `.loc` if we are referring to a specific row AND column, e.g.:


```python
print(sumo.loc["komusubi", "wrestler"])
```

<pre class="output-block">---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[41], line 1
----> 1 print(sumo.loc["komusubi", "wrestler"])

NameError: name 'sumo' is not defined
</pre>

If we want to purely use numerical indexing, we can use the `.iloc()` method. If you use `.iloc()`, you can index a DataFrame just as you would a numpy array. 


```python
# Select the first two rows and the first two columns

sumo.iloc[0:2, 0:2]
```

<pre class="output-block">---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[42], line 3
      1 # Select the first two rows and the first two columns
----> 3 sumo.iloc[0:2, 0:2]

NameError: name 'sumo' is not defined
</pre>

There are many ways to select subsets of a dataframe. The rows and columns of a dataframe can be referred to either by their integer position or by their indexed name. Typically, for columns, you'll use the indexed name and can just do `[]` with the name of the column. For rows, if you want to use the integer position, you will use `.iloc[]`. If you want to use the index name, you will use `.loc[]`. 

For reference, here's a handy table on the best ways to index into a dataframe:

|Action|Named index|Integer Position|
|---|---|---|
|Select single column|`df['column_name']`|`df.iloc[:, column_position]`|
|Select multiple columns|`df[['column_name1', 'column_name2']]`|`df.iloc[:, [column_position1, column_position2]]`|
|Select single row|`df.loc['row_name']`|`df.iloc[row_position]`|
|Select multiple rows|`df.loc[['row_name1', 'row_name2']]`|`df.iloc[[row_position1, row_position2]]`|

> Exercise: we'll use the penguins dataset from our initial example.
> 1) Print the 'species' column
> 2) Print the first five columns and first five rows
> 3) Print the columns "species", "island", and "sex" and the first ten rows of the dataframe


```python
penguins.info()
```

<pre class="output-block">---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[43], line 1
----> 1 penguins.info()

NameError: name 'penguins' is not defined
</pre>


```python
# Your code here

print(penguins['species'])

print("---")
print(penguins.iloc[0:5,0:5])

print("---")
print(penguins.loc[0:10, ['species', 'island', 'sex']])
```

<pre class="output-block">---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[44], line 3
      1 # Your code here
----> 3 print(penguins['species'])
      5 print("---")
      6 print(penguins.iloc[0:5,0:5])

NameError: name 'penguins' is not defined
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

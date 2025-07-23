---
title: "[Workshop] Python intensive, day 4"
description: "Introduction to file handling and the numpy library for numerical computing in Python, including arrays and basic operations."
authors:
    - Lei Ma
    - Adam Freedman
---

# Python intensive, day 4

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

And run the following to demonstrate how the code blocks run and display code:


```python
# Run this cell to print a message to the screen
print("this is my code cell")
```

<pre class="output-block">
this is my code cell
</pre>

Any **variables** that you assign in one cell will be available in other cells. But they will not be saved between sessions. If you close the notebook and re-open it, you will need to re-run the previous cells to get your variables back. Therefore, it's important to be aware of the state of your notebook and the order in which your cells were run.


```python
my_string = "this is my code cell"
```


```python
print(my_string)
```

<pre class="output-block">
this is my code cell
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
<pre class="output-block">
'HELLO'
</pre>

In the above code, `my_string` is a string object, and we are calling the `upper()` method on it. The method is called by using the `.` operator. Methods are functions that can only be used on objects of certain classes. You will often see methods strung together, like below:


```python
my_string = "hello"
# This first makes the first letter uppercase, then swaps the cases of each letter
my_string.capitalize().swapcase()
```

<pre class="output-block">
'hELLO'
</pre>

### Object Attributes

We'll be learning about some more complex objects today, like **numpy arrays**, which also have attributes. **Attributes** are properties of an object that can be accessed using the `.` operator. For example, numpy arrays have an attribute called `shape` that tells you the dimensions of the array. The difference between an attribute and a method is that attributes are information about a given object, rather than a task being performed on the object. Practically, this means that, while both attributes and methods are called on an object with the dot operator `.`, attributes are accessed without parentheses, so you don't need to call them like functions.


```python
# this makes a np array (we'll learn more about these shortly!)
my_array = np.array([1, 2, 3, 4, 5])

# this gets the size (total number of elements) of the array
my_array.size
```

<pre class="output-block">
(5,)
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
=======

## Refresher: importing libraries

Recall that we covered how to **import libraries** of functions previously. For instance, we can import the built-in `math` library and then use the functions it contains:


```python
import math
print(math.log(100))
```

<pre class="output-block">
4.605170185988092
</pre>

We need to type `math.` so Python knows where to look for the `log()` function.

We can also use an **alias** if we don't want to type `math.` every time we use a function from the library:


```python
import math as m
print(m.log(100))
```

<pre class="output-block">
4.605170185988092
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

!wget https://informatics.fas.harvard.edu/workshops/python-intensive/data/bird_names.csv
```

<pre class="output-block">
--2025-01-15 14:50:41--  https://informatics.fas.harvard.edu/resources/Workshops/2024-Fall/Python/data/bird_names.csv
Resolving informatics.fas.harvard.edu (informatics.fas.harvard.edu)... 185.199.108.153, 185.199.111.153, 185.199.110.153, ...
Connecting to informatics.fas.harvard.edu (informatics.fas.harvard.edu)|185.199.108.153|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 4383 (4.3K) [text/csv]
Saving to: ‘bird_names.csv’

bird_names.csv      100%[===================&gt;]   4.28K  --.-KB/s    in 0s      

2025-01-15 14:50:42 (33.4 MB/s) - ‘bird_names.csv’ saved [4383/4383]
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

<pre class="output-block">
{'6924': {'scientific_name': 'Anas rubripes', 'common_name': 'American Black Duck'}, '473': {'scientific_name': 'Fulica americana', 'common_name': 'American Coot'}, '145310': {'scientific_name': 'Spinus tristis', 'common_name': 'American Goldfinch'}, '4665': {'scientific_name': 'Falco sparverius', 'common_name': 'American Kestrel'}, '12727': {'scientific_name': 'Turdus migratorius', 'common_name': 'American Robin'}, '474210': {'scientific_name': 'Spizelloides arborea', 'common_name': 'American Tree Sparrow'}, '3936': {'scientific_name': 'Scolopax minor', 'common_name': 'American Woodcock'}, '16010': {'scientific_name': 'Myiarchus cinerascens', 'common_name': 'Ash-throated Flycatcher'}, '5305': {'scientific_name': 'Haliaeetus leucocephalus', 'common_name': 'Bald Eagle'}, '9346': {'scientific_name': 'Icterus galbula', 'common_name': 'Baltimore Oriole'}, '19893': {'scientific_name': 'Strix varia', 'common_name': 'Barred Owl'}, '2548': {'scientific_name': 'Megaceryle alcyon', 'common_name': 'Belted Kingfisher'}, '144815': {'scientific_name': 'Poecile atricapillus', 'common_name': 'Black-capped Chickadee'}, '4981': {'scientific_name': 'Nycticorax nycticorax', 'common_name': 'Black-crowned Night Heron'}, '199916': {'scientific_name': 'Setophaga caerulescens', 'common_name': 'Black-throated Blue Warbler'}, '8229': {'scientific_name': 'Cyanocitta cristata', 'common_name': 'Blue Jay'}, '7458': {'scientific_name': 'Certhia americana', 'common_name': 'Brown Creeper'}, '10373': {'scientific_name': 'Molothrus ater', 'common_name': 'Brown-headed Cowbird'}, '6993': {'scientific_name': 'Bucephala albeola', 'common_name': 'Bufflehead'}, '7089': {'scientific_name': 'Branta canadensis', 'common_name': 'Canada Goose'}, '7513': {'scientific_name': 'Thryothorus ludovicianus', 'common_name': 'Carolina Wren'}, '7428': {'scientific_name': 'Bombycilla cedrorum', 'common_name': 'Cedar Waxwing'}, '6571': {'scientific_name': 'Chaetura pelagica', 'common_name': 'Chimney Swift'}, '9135': {'scientific_name': 'Spizella passerina', 'common_name': 'Chipping Sparrow'}, '9602': {'scientific_name': 'Quiscalus quiscula', 'common_name': 'Common Grackle'}, '4626': {'scientific_name': 'Gavia immer', 'common_name': 'Common Loon'}, '7004': {'scientific_name': 'Mergus merganser', 'common_name': 'Common Merganser'}, '8010': {'scientific_name': 'Corvus corax', 'common_name': 'Common Raven'}, '9721': {'scientific_name': 'Geothlypis trichas', 'common_name': 'Common Yellowthroat'}, '5112': {'scientific_name': 'Accipiter cooperii', 'common_name': "Cooper's Hawk"}, '10094': {'scientific_name': 'Junco hyemalis', 'common_name': 'Dark-eyed Junco'}, '10676': {'scientific_name': 'Spiza americana', 'common_name': 'Dickcissel'}, '120479': {'scientific_name': 'Anser anser domesticus', 'common_name': 'Domestic Greylag Goose'}, '236935': {'scientific_name': 'Anas platyrhynchos domesticus', 'common_name': 'Domestic Mallard'}, '1454382': {'scientific_name': 'Nannopterum auritum', 'common_name': 'Double-crested Cormorant'}, '792988': {'scientific_name': 'Dryobates pubescens', 'common_name': 'Downy Woodpecker'}, '16782': {'scientific_name': 'Tyrannus tyrannus', 'common_name': 'Eastern Kingbird'}, '17008': {'scientific_name': 'Sayornis phoebe', 'common_name': 'Eastern Phoebe'}, '494355': {'scientific_name': 'Buteo jamaicensis borealis', 'common_name': 'Eastern Red-tailed Hawk'}, '515821': {'scientific_name': 'Melospiza melodia melodia', 'common_name': 'Eastern Song Sparrow'}, '319123': {'scientific_name': 'Meleagris gallopavo silvestris', 'common_name': 'Eastern Wild Turkey'}, '14850': {'scientific_name': 'Sturnus vulgaris', 'common_name': 'European Starling'}, '544795': {'scientific_name': 'Passer domesticus domesticus', 'common_name': 'European house sparrow'}, '122767': {'scientific_name': 'Columba livia domestica', 'common_name': 'Feral Pigeon'}, '9156': {'scientific_name': 'Passerella iliaca', 'common_name': 'Fox Sparrow'}, '117100': {'scientific_name': 'Regulus satrapa', 'common_name': 'Golden-crowned Kinglet'}, '14995': {'scientific_name': 'Dumetella carolinensis', 'common_name': 'Gray Catbird'}, '4368': {'scientific_name': 'Larus marinus', 'common_name': 'Great Black-backed Gull'}, '4956': {'scientific_name': 'Ardea herodias', 'common_name': 'Great Blue Heron'}, '16028': {'scientific_name': 'Myiarchus crinitus', 'common_name': 'Great Crested Flycatcher'}, '20044': {'scientific_name': 'Bubo virginianus', 'common_name': 'Great Horned Owl'}, '7047': {'scientific_name': 'Aythya marila', 'common_name': 'Greater Scaup'}, '5020': {'scientific_name': 'Butorides virescens', 'common_name': 'Green Heron'}, '6937': {'scientific_name': 'Anas crecca', 'common_name': 'Green-winged Teal'}, '514057': {'scientific_name': 'Anser anser × Branta canadensis', 'common_name': 'Greylag × Canada Goose'}, '792990': {'scientific_name': 'Dryobates villosus', 'common_name': 'Hairy Woodpecker'}, '12890': {'scientific_name': 'Catharus guttatus', 'common_name': 'Hermit Thrush'}, '204533': {'scientific_name': 'Larus argentatus', 'common_name': 'Herring Gull'}, '7109': {'scientific_name': 'Lophodytes cucullatus', 'common_name': 'Hooded Merganser'}, '4209': {'scientific_name': 'Podiceps auritus', 'common_name': 'Horned Grebe'}, '199840': {'scientific_name': 'Haemorhous mexicanus', 'common_name': 'House Finch'}, '13858': {'scientific_name': 'Passer domesticus', 'common_name': 'House Sparrow'}, '7562': {'scientific_name': 'Troglodytes aedon', 'common_name': 'House Wren'}, '4793': {'scientific_name': 'Charadrius vociferus', 'common_name': 'Killdeer'}, '10479': {'scientific_name': 'Chondestes grammacus', 'common_name': 'Lark Sparrow'}, '7054': {'scientific_name': 'Aythya affinis', 'common_name': 'Lesser Scaup'}, '6930': {'scientific_name': 'Anas platyrhynchos', 'common_name': 'Mallard'}, '326092': {'scientific_name': 'Anas platyrhynchos × cairina moschata', 'common_name': 'Mallard × Muscovy Duck'}, '4672': {'scientific_name': 'Falco columbarius', 'common_name': 'Merlin'}, '3454': {'scientific_name': 'Zenaida macroura', 'common_name': 'Mourning Dove'}, '6921': {'scientific_name': 'Cygnus olor', 'common_name': 'Mute Swan'}, '9083': {'scientific_name': 'Cardinalis cardinalis', 'common_name': 'Northern Cardinal'}, '18236': {'scientific_name': 'Colaptes auratus', 'common_name': 'Northern Flicker'}, '14886': {'scientific_name': 'Mimus polyglottos', 'common_name': 'Northern Mockingbird'}, '555736': {'scientific_name': 'Colaptes auratus luteus', 'common_name': 'Northern Yellow-shafted Flicker'}, '979757': {'scientific_name': 'Leiothlypis celata', 'common_name': 'Orange-crowned Warbler'}, '116999': {'scientific_name': 'Pandion haliaetus', 'common_name': 'Osprey'}, '62550': {'scientific_name': 'Seiurus aurocapilla', 'common_name': 'Ovenbird'}, '4647': {'scientific_name': 'Falco peregrinus', 'common_name': 'Peregrine Falcon'}, '17364': {'scientific_name': 'Vireo philadelphicus', 'common_name': 'Philadelphia Vireo'}, '4246': {'scientific_name': 'Podilymbus podiceps', 'common_name': 'Pied-billed Grebe'}, '18205': {'scientific_name': 'Melanerpes carolinus', 'common_name': 'Red-bellied Woodpecker'}, '6996': {'scientific_name': 'Mergus serrator', 'common_name': 'Red-breasted Merganser'}, '14823': {'scientific_name': 'Sitta canadensis', 'common_name': 'Red-breasted Nuthatch'}, '5212': {'scientific_name': 'Buteo jamaicensis', 'common_name': 'Red-tailed Hawk'}, '9744': {'scientific_name': 'Agelaius phoeniceus', 'common_name': 'Red-winged Blackbird'}, '7056': {'scientific_name': 'Aythya americana', 'common_name': 'Redhead'}, '4364': {'scientific_name': 'Larus delawarensis', 'common_name': 'Ring-billed Gull'}, '7044': {'scientific_name': 'Aythya collaris', 'common_name': 'Ring-necked Duck'}, '3017': {'scientific_name': 'Columba livia', 'common_name': 'Rock Pigeon'}, '1289388': {'scientific_name': 'Corthylio calendula', 'common_name': 'Ruby-crowned Kinglet'}, '6432': {'scientific_name': 'Archilochus colubris', 'common_name': 'Ruby-throated Hummingbird'}, '850859': {'scientific_name': 'Oxyura jamaicensis', 'common_name': 'Ruddy Duck'}, '9100': {'scientific_name': 'Melospiza melodia', 'common_name': 'Song Sparrow'}, '72458': {'scientific_name': 'Actitis macularius', 'common_name': 'Spotted Sandpiper'}, '11935': {'scientific_name': 'Tachycineta bicolor', 'common_name': 'Tree Swallow'}, '13632': {'scientific_name': 'Baeolophus bicolor', 'common_name': 'Tufted Titmouse'}, '17394': {'scientific_name': 'Vireo gilvus', 'common_name': 'Warbling Vireo'}, '14801': {'scientific_name': 'Sitta carolinensis', 'common_name': 'White-breasted Nuthatch'}, '9176': {'scientific_name': 'Zonotrichia leucophrys', 'common_name': 'White-crowned Sparrow'}, '9184': {'scientific_name': 'Zonotrichia albicollis', 'common_name': 'White-throated Sparrow'}, '906': {'scientific_name': 'Meleagris gallopavo', 'common_name': 'Wild Turkey'}, '7107': {'scientific_name': 'Aix sponsa', 'common_name': 'Wood Duck'}, '145238': {'scientific_name': 'Setophaga petechia', 'common_name': 'Yellow Warbler'}, '18463': {'scientific_name': 'Sphyrapicus varius', 'common_name': 'Yellow-bellied Sapsucker'}}
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
!wget https://informatics.fas.harvard.edu/workshops/python-intensive/data/bird_observations.csv
```

<pre class="output-block">
--2025-01-15 14:50:33--  https://informatics.fas.harvard.edu/resources/Workshops/2024-Fall/Python/data/bird_observations.csv
Resolving informatics.fas.harvard.edu (informatics.fas.harvard.edu)... 185.199.108.153, 185.199.111.153, 185.199.110.153, ...
Connecting to informatics.fas.harvard.edu (informatics.fas.harvard.edu)|185.199.108.153|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 50448 (49K) [text/csv]
Saving to: ‘bird_observations.csv’

bird_observations.c 100%[===================&gt;]  49.27K  --.-KB/s    in 0.01s   

2025-01-15 14:50:33 (4.15 MB/s) - ‘bird_observations.csv’ saved [50448/50448]
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

<pre class="output-block">
{'Northern Mockingbird': 23, 'Common Merganser': 4, 'Bufflehead': 9, 'House Sparrow': 69, 'European Starling': 51, 'Northern Cardinal': 28, 'Mourning Dove': 31, 'Blue Jay': 39, 'American Black Duck': 2, 'Domestic Mallard': 14, 'Mute Swan': 33, 'Green-winged Teal': 8, 'American Robin': 92, 'Mallard': 49, 'Great Blue Heron': 26, 'Red-tailed Hawk': 36, 'Canada Goose': 112, 'Downy Woodpecker': 24, 'Ring-necked Duck': 22, 'Wild Turkey': 82, 'Common Loon': 9, 'Horned Grebe': 4, 'Redhead': 8, 'Feral Pigeon': 31, 'Golden-crowned Kinglet': 7, 'Red-bellied Woodpecker': 15, 'Hooded Merganser': 18, 'Belted Kingfisher': 3, 'Red-winged Blackbird': 35, 'Black-capped Chickadee': 14, 'Ruddy Duck': 2, 'Bald Eagle': 2, 'Dark-eyed Junco': 9, 'Carolina Wren': 7, 'House Finch': 19, 'White-throated Sparrow': 5, 'Song Sparrow': 24, 'Yellow-bellied Sapsucker': 3, 'White-breasted Nuthatch': 10, 'Eastern Red-tailed Hawk': 5, 'Tufted Titmouse': 8, "Cooper's Hawk": 17, 'Domestic Greylag Goose': 14, 'Rock Pigeon': 9, 'American Coot': 1, 'Greylag × Canada Goose': 1, 'Eastern Wild Turkey': 1, 'Brown Creeper': 7, 'Hairy Woodpecker': 2, 'Northern Flicker': 6, 'Greater Scaup': 1, 'Red-breasted Merganser': 2, 'American Woodcock': 7, 'Red-breasted Nuthatch': 1, 'Great Horned Owl': 23, 'Peregrine Falcon': 5, 'American Goldfinch': 18, 'Barred Owl': 2, 'Black-crowned Night Heron': 2, 'Tree Swallow': 11, 'Common Grackle': 14, 'Hermit Thrush': 4, 'Northern Yellow-shafted Flicker': 1, 'Chipping Sparrow': 3, 'Killdeer': 2, 'Gray Catbird': 20, 'Double-crested Cormorant': 17, 'Yellow Warbler': 3, 'Warbling Vireo': 2, 'Baltimore Oriole': 7, 'Common Yellowthroat': 2, 'White-crowned Sparrow': 2, 'Black-throated Blue Warbler': 1, 'Ovenbird': 1, 'Brown-headed Cowbird': 4, 'House Wren': 1, 'Cedar Waxwing': 4, 'European house sparrow': 1, 'Herring Gull': 4, 'Eastern Kingbird': 7, 'Great Black-backed Gull': 1, 'Green Heron': 10, 'Great Crested Flycatcher': 1, 'Wood Duck': 6, 'American Kestrel': 1, 'Osprey': 1, 'Ruby-throated Hummingbird': 3, 'Spotted Sandpiper': 2, 'Chimney Swift': 1, 'Eastern Phoebe': 1, 'Lark Sparrow': 2, 'Ring-billed Gull': 1, 'Dickcissel': 1, 'Merlin': 1, 'Ash-throated Flycatcher': 6, 'Pied-billed Grebe': 5, 'Lesser Scaup': 2, 'Orange-crowned Warbler': 2, 'Eastern Song Sparrow': 1, 'Philadelphia Vireo': 1, 'Ruby-crowned Kinglet': 2, 'Mallard × Muscovy Duck': 1, 'Fox Sparrow': 1, 'American Tree Sparrow': 1, 'Common Raven': 1}
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

When importing data into a DataFrame, pandas automatically detects what data type each column should be. For example, if the column contains only numbers, it will be imported as an floating point or integer data type. If the column contains strings or a mixture of strings and numbers, it will be imported as an "object" data type. Below are the different data types for the penguins column. 


```python
penguins.info()
```

### Looping through a dataframe
As a note, if we want to go through a dataframe line-by-line (i.e. row by row), because both the rows and columns are indexed it requires slightly more syntax than looping through other data structures (e.g. a dictionary or list). Specifically we need to use the `.iterrows()` method to make the data frame iterable. The `.iterrows()` method outputs each row as a `Series` object with a row index and the column:   


```python
for index, row in penguins.iterrows():
    print(f"Row index: {index}, {row['species']}, {row['island']}")
```

This can be slow for very large dataframes, but is useful if you need to perform actions on individual rows.

>Consider: based on what we've learned the past several days, what are some *limitations* of `numpy`? Can you think of any tasks you might want to do or analysis you might like to perform that would be difficult with `numpy`? Does this give you a guess as to what `pandas` specializes in?

Answer: `numpy` is specialized primarily for numerical operations, e.g. matrix multiplication, vector math, etc., but is more limited when dealing with other data types such as string, python objects, etc. In contrast, `pandas` objects are able to handle mixed data easily! As you will often run into this type of data when doing bioinformatics, `pandas` can be very useful.

Before we dive into the syntax, let's take a look at an example real-world application of `pandas` for a task that you might commonly face in biology. We are going to use the "Palmer penguins" dataset, which is a collection of various biometric data for several different penguin species and is a commonly used example dataset. Let's take a quick look at what the data looks like.

In the Palmer penguins dataset, each row represents an individual penguin, and each column represent a different measurement or characteristic of the penguin, such as its body mass or island of origin. The data are organized in this way so that variables (things we may want to compare against each other) are the columns while observations (the individual penguins) are the rows. This is a common way to organize data in data science and is called **tidy data**. Tidy data formatting also makes it easy to use code to manipulate and analyze, which we will see in this lesson. 



```python
penguins = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2020/2020-07-28/penguins.csv')
penguins.head()
```

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


```python
#Using the pd.Series method:
s1 = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])

print(s1)

```

Another way to create a Series is to convert a (non-nested) dictionary into a Series. The keys of the dictionary will become the index labels while the values will become the data. 


```python
# Converting from dictionary to series
my_dictionary = {'first': 10, 'second': 20, 'third': 30}
s2 = pd.Series(my_dictionary)

print(s2)
```

We can then access specific elements in the Series by referring to its index label enclosed in quotes and brackets. This is very similar to how a dictionary works!


```python
print(s0[0])

print(s1["a"])

print(s2["second"])
```

### Multi-indexed Series

Series objects may have multiple levels of indices. We call this **multi-indexed**. Using layers of indexing is a way of representing two-dimensional data within a one-dimensional `Series` object. Some people really like using multi-indexed Series. You can create a multi-indexed series by passing a list of lists to the `index` argument of the `pd.Series()` function. The first list will be the outermost level of the index, the second list will be the next level, and so on.


```python
my_index = [["California", "California", "New York", "New York", "Texas", "Texas"], 
            [2001, 2002, 2001, 2002, 2001, 2002]]
my_values = [1.5, 1.7, 3.6, 4.2, 3.2, 4.5]

s3 = pd.Series(my_values, index=my_index)

print(s3)

```

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

In our work, we typically don't use multi-indexed Series. However, they are often the output of pandas functions, so it's good to know how to work with them. If you don't like the idea of multi-indexed Series, you can always convert them to a DataFrame using the `reset_index()` method.


```python
s3.reset_index()
```

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

Pandas DataFrames also have the handy `info()` function that summarizes the contents of the dataframe, including counts of the non-null values of each column and the data type of each column.


```python
sumo.info()
```

## Selecting data in a Pandas dataframe

As with series objects, pandas dataframes rows and columns are *explicitly indexed*, which means that every row and column has a label associated with it. You can think of the explicit indices as the being the names of the rows and the names of the columns.  

Unfortunately, in pandas the syntax for subsetting rows v.s. columns is different and can get a little confusing, so let's go through several different use cases.

### Selecting columns
We can always check the names of the columns in a Pandas dataframe byt using the built-in `.columns` method, which simply lists the column index:


```python
sumo.columns
```

If we want to refer to a specific column, we can specify its index (enclosed in double quotes) inside of square brackets `[]` like so:


```python
#Single column:
sumo["wrestler"]
```

If we want to refer to *multiple* columns, we need to pass the columns as a **list** by enclosing the column indices in square brackets, so you will end up with *double brackets*:


```python
#Multiple columns (note the double []!):
sumo[["wrestler", "rank"]]
```

### Selecting rows:

The syntax for selecting specific rows is slightly different. Let's first check the labels of the row index; to do this we use the `.index` method:


```python
print(sumo.index)
```

Here we can see that while the column index labels were strings, the row index labels are *numerical values*, in this case `0` thru `3`. If we wanted to pull out the first row, we need to specify its index label (`0`) in combination with the `.loc` method (which is required for rows): 


```python
sumo.loc[0]
```

If we want to select multiple rows, like with columns we need to pass it as a list using the double brackets. If we want to specify a **range** of rows (i.e. from this row to that row), we **don't** use double brackets and instead use `:`:


```python
print(sumo.loc[[0,1]])
```


```python

print(sumo.loc[0:2])
```

Note that in this case the row index labels are numbers, but do not have to be numerical, and can have string labels similar to columns. Let's show how we could change the row index labels by taking the column with the wrestler's rank and setting it as the index label (note that the labels should be unique!):


```python
sumo = sumo.set_index("rank")

print(sumo)
```


```python
sumo.loc["yokozuna"]
```

We also need to use `.loc` if we are referring to a specific row AND column, e.g.:


```python
print(sumo.loc["komusubi", "wrestler"])
```

If we want to purely use numerical indexing, we can use the `.iloc()` method. If you use `.iloc()`, you can index a DataFrame just as you would a numpy array. 


```python
# Select the first two rows and the first two columns

sumo.iloc[0:2, 0:2]
```

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

=======
## Numpy

Numpy is an open-source **library** written in Python. It's main feature is the implementation of efficient **data structures** that can be used for large datasets and **functions** and **methods** for those data structures. This makes numpy well suited for scientific computing and data science.

Principal among these Numpy data structures is the **numpy array**.


### Importing Numpy

Since Numpy is an external library of functions, it needs to be **imported** before we can use it. Since Numpy is so widely used, it has become common practice to import it using the alias `np`.

> **Exercise**: Run the block of code below to import Numpy. You have to do this to be able to use any of the Numpy functions we'll talk about in the workship.


```python
# Run this block to import numpy with the alias np
import numpy as np
```

### Numpy arrays

**Numpy arrays** are a data structure that only contain one type of data, typically numerical, and are N-dimensional (any number of dimensions). You can create numpy arrays using the `np.array()` function (after running `import numpy as np`) or by converting other data structures to an array using `np.asarray()` or other helper functions. There are also many functions that can create an array with pre-filled numbers, such as `np.zeros()` and `np.arange()`. An array is defined by its `shape`, which describes the number of elements in each dimension, also known as **axes**. The first axis is the number of rows, the second is the number of columns, and so on for higher dimensional data.

Today we will be spending a lot of time with numpy arrays as they are one of the main data structures for working with numerical data. We will learn how to navigate them, read and write from them, and also how to perform mathematical operations on them. We will also use numpy to create some visualizations.

**Use cases for numpy arrays**

The use cases for numpy arrays are very broad. They are used in scientific computing, machine learning, data analysis, and more. They are optimized for fast mathematical operations and are very efficient in terms of memory usage. They are also very flexible in terms of the number of dimensions they can have, so you can store a lot of data in a single numpy array. They are not good for storing mixed data types or for storing data that is not numerical.

### Generating numpy arrays

Numpy has a variety of functions that can generate arrays for you. Some of the most common ones are `np.zeros()`, `np.ones()`, `np.arange()`, and `np.linspace()`.

>**Exercise:** Read the documentation page for [np.zeros()](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html). What is the minimal information you need to pass to the function to get an array of zeros? What parameters are optional or already have defaults?
>
> Once you have read the documentation, produce an array of zeros with 3 rows and 4 columns in the code block below.


```python
# your code here

np.zeros([3,4])
```




<pre class="output-block">
array([[0., 0., 0., 0.],
       [0., 0., 0., 0.],
       [0., 0., 0., 0.]])
</pre>

>**Exercise:** Read the documentation page for [np.arange()](https://numpy.org/doc/stable/reference/generated/numpy.arange.html).
>
> Once you have read the documentation, produce an array of the even numbers from 100 to 200 in the code block below.


```python
# your code here

np.arange(100,200,2)
```




<pre class="output-block">
array([100, 102, 104, 106, 108, 110, 112, 114, 116, 118, 120, 122, 124,
       126, 128, 130, 132, 134, 136, 138, 140, 142, 144, 146, 148, 150,
       152, 154, 156, 158, 160, 162, 164, 166, 168, 170, 172, 174, 176,
       178, 180, 182, 184, 186, 188, 190, 192, 194, 196, 198])
</pre>

Did you notice anything unexpected in the output above? Look at the last value of the result: it's 198, not 200. One might expect that, because the function call says to create an array that ends at 200, that value would be included. The fact that it doesn't has to do with python's zero-indexing behavior. To actually get 200 to be included, you'd need to set the second argument to 201. If in a scientific application you need an array that ends at (and includes) a specific value, be sure your function call is set up properly.

>**Exercise:** `size` and `shape` are attributes of numpy arrays that tells you how many elements are in the array or how many elements are in each dimension. You can access it by calling `array.size`, (where `array` is the name of your array). It can also be chained with the `arange()` function. For example, `np.arange(10).size` will return 10.
>
> `print()` the sizes and shapes of the two arrays you created above.
>
> What do you notice about the way the `size` and `shape` attributes are returned?


```python
print(np.zeros([3,4]).size)
print(np.zeros([3,4]).shape)

print(np.arange(100,200,2).size)
print(np.arange(100,200,2).shape)
```

<pre class="output-block">
12
(3, 4)
50
(50,)
</pre>

When you print the size of an array, you will get a single number of the total number of elements in the array. When you print the shape of an array, you will get a **tuple** of the number of elements in each dimension. However, if the array is one-dimensional, it will still return a tuple, but with a single element.

Recall that a **tuple** is a data structure that is similar to a list, but is immutable. This means that you cannot change the elements of a tuple after it is created. Tuples are created by using parentheses instead of square brackets. Tuples are often returned by functions that need to return multiple values.

>**Exercise:** `reshape()` is a method that can be called on a numpy array to change its shape. Use it to change the array you created using `np.arange(100,200,2)` to have 10 rows and 5 columns. [reshape() documentation](https://numpy.org/doc/stable/reference/generated/numpy.reshape.html)
>
> What are the restrictions on the shape you can pass to `reshape()`?


```python
# your code here

np.arange(100,200,2).reshape(10,5)
```




<pre class="output-block">
array([[100, 102, 104, 106, 108],
       [110, 112, 114, 116, 118],
       [120, 122, 124, 126, 128],
       [130, 132, 134, 136, 138],
       [140, 142, 144, 146, 148],
       [150, 152, 154, 156, 158],
       [160, 162, 164, 166, 168],
       [170, 172, 174, 176, 178],
       [180, 182, 184, 186, 188],
       [190, 192, 194, 196, 198]])
</pre>

### Difference between numpy arrays and lists

A one-dimensional numpy array is called a `vector` and it looks very much like a list, but with the additional restriction that **only one data type can be stored in it**. So why do we want to use numpy arrays instead of lists? Run the code blocks below to see the main reason numpy is used more for data analysis than lists. Annotate each line of code with a comment explaining what it does.


```python
my_numpy_array = np.arange(1, 1000000)
my_list = list(range(1, 1000000))
```


```python
%timeit np.sum(my_numpy_array)
```

<pre class="output-block">
431 µs ± 93.4 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
</pre>

```python
%timeit sum(my_list)
```

<pre class="output-block">
7.06 ms ± 69.7 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
</pre>

In the above code, we used the "magic command" `%timeit` to time how long it takes to run a line of code. This command runs the code multiple times and gives you the average time it took to run. We used it to compare the time it takes to sum the elements of a list and the time it takes to sum the elements of a numpy array.

Note that the `%timeit` command is specific to Jupyter notebooks. If you are running this code in a script, you would have to use the `timeit` module to time your code.

We can see that using the numpy-specific `np.sum` function on a numpy array is much faster that using the base python sum function on a list. Each operation runs in microseconds instead of milliseconds.


```python
import sys

print(f"Memory used by numpy array: {my_numpy_array.nbytes/1024/1024} MB")
list_size = (sys.getsizeof(my_list)+ sum(sys.getsizeof(item) for item in my_list)) / 1024 / 1024
print(f"Memory used by list: {list_size} MB")
```

<pre class="output-block">
Memory used by numpy array: 7.629386901855469 MB
Memory used by list: 34.33230209350586 MB
</pre>

In the above code, we printed out the memory usage of the numpy array and the list. This reveals that the numpy array also takes up less memory to store the same amount of information as a list.

In summary, numpy, which is made to do calculations, is an improvement over base python lists because it is faster and more memory efficient.

If you want some more analysis, you can check out this [stackoverflow](https://stackoverflow.com/questions/10922231/pythons-sum-vs-numpys-numpy-sum) thread.

## Numpy operations

### Broadcasting

You can perform mathematical operations on arrays and they'll propagate to each element. This is called **broadcasting**. In order for the element-wise operation to work, the two objects you're operating with either have to have the same shape or one of them has to be a **scalar**, meaning a single number. Numpy also has functions that allow you to operate on the entire array, such as `np.sum()`, `np.mean()`, etc.

Consider the following operation on two numpy arrays:



```python
predicted_array = np.array([1, 2, 3, 4, 5])
expected_array = np.array([2, 4, 1, 5, 5])

print(predicted_array - expected_array)
```

<pre class="output-block">
[-1 -2  2 -1  0]
</pre>

By using the subtraction operator `-`, which we learned is designed to subtract one single number from one other single number, we have actually performed the operation automatically on each number in the arrays. The first number in `predicted` is `1` and the first number in `expected` is `2`, so the first number in the resulting output is `2 - 1` or `-1`. The second number in `predicted` is `2` and the second number in `expected` is `4`, so the second number in the resulting output is `2 - 4` or `-2`. And so on for the remaining numbers in the arrays.

What if we tried to do this with normal Python lists?


```python
predicted_list = [1, 2, 3, 4, 5]
expected_list = [2, 4, 1, 5, 5]

print(predicted_list - expected_list)
```


<pre class="output-block">
---------------------------------------------------------------------------

TypeError                                 Traceback (most recent call last)

&lt;ipython-input-10-a158233514a6&gt; in &lt;cell line: 4&gt;()
      2 expected_list = [2, 4, 1, 5, 5]
      3 
----&gt; 4 print(predicted_list - expected_list)


TypeError: unsupported operand type(s) for -: 'list' and 'list'
</pre>

An error, stating that we can't use the subtraction operator `-` on lists. To achieve the same result as the numpy arrays, we'd have to loop over the lists by index, a much slower process that requires us to write more code.

If provided a scalar, instead of a second array, the arithmetic operation will be performed on each element in the first array using the same number on each one:


```python
single_number = 3
print(predicted_array - 3)
```

<pre class="output-block">
[-2 -1  0  1  2]
</pre>

Here, each number in `predicted_array` has `3` subtracted from it.

Again, this is something we'd have to use a loop to do with regular lists. This is a huge advantage of numpy arrays over native Python data structures like lists.

Below is a practical example that combines the array/array broadcasting and array/scalar broadcasting. Here, we calculate the mean squared error of two 1D arrays using the formula $\frac{1}{n}\sum_{i=1}^{n}(predicted_i - expected_i)^2$.


```python
predicted = np.array([1, 2, 3, 4, 5])
expected = np.array([2, 4, 1, 5, 5])
mse = (1/len(predicted)) * np.sum(np.square(predicted - expected))
print(mse)
```

<pre class="output-block">
2.0
</pre>

Breaking down the code, you can see what is produced at each step


```python
print(predicted - expected)
print(np.square(predicted - expected))
print(np.sum(np.square(predicted - expected)))
print(1/len(predicted))
```

<pre class="output-block">
[-1 -2  2 -1  0]
[1 4 4 1 0]
10
0.2
</pre>

And of course 0.2 * 10 is 2.0, the same result as the single expression above..

### Slicing and indexing numpy arrays

**Slicing** arrays is a powerful tool for **extracting subsets of data**. The syntax for slicing is `array[start:stop:step]`, similar to what we learned about slicing strings and lists. If you don't specify a start, it defaults to index 0 (the first element of the array), if you don't specify a stop, it defaults to the end of the array, and if you don't specify a step, it defaults to 1. When you specify a start and stop, the range is inclusive of the start and exclusive of the stop. Usually, you don't need to specify the step, so you can omit the second colon.

You can also use negative indices to count from the end of the array. When you use negative indices, inclusive of the start and exclusive of the stop still applies.

Here are some examples of slicing one-dimensional and two-dimensional arrays. See if you can predict the output before running the code. (Do these on the board)


```python
# Examples of slicing one-dimensional arrays
arr1 = np.array([1, 2, 3, 4, 5])
print(arr1[0:2])
print(arr1[1:3])
print(arr1[:])
print(arr1[2:])
print(arr1[-1:])
print(arr1[:-1])
print(arr1[-3:-1])
print(arr1[::2])
print(arr1[::-1])
```

<pre class="output-block">
[1 2]
[2 3]
[1 2 3 4 5]
[3 4 5]
[5]
[1 2 3 4]
[3 4]
[1 3 5]
[5 4 3 2 1]
</pre>

#### Slicing multi-dimensional arrays

Multi-dimensional numpy arrays are sliced and indexed with the same syntax as single dimensional arrays (vectors), but you need to separate the dimensions with a comma. For example, `array[i, j]` will return the element at row `i` and column `j`. In two dimensions, the first axis is the rows and the second axis is the columns. So now the syntax is `array[row_start:row_stop:row_step, col_start:col_stop:col_step]`.

Let's practice slicing the following array of 25 elements reshaped into a 5x5 array:


```python
arr = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
])
print(arr)
```

<pre class="output-block">
[[ 1  2  3  4  5]
 [ 6  7  8  9 10]
 [11 12 13 14 15]
 [16 17 18 19 20]
 [21 22 23 24 25]]
</pre>

>**Exercise**: Perform the following operations on the `arr` array:
>
> 1. Extract the first row
> 2. Extract the last column
> 3. Extract the first three rows
> 4. Extract the central 3x3 square
> 5. Extract the last column using positive indexing, and then do it again using negative indexing
> 6. Extract every other column (and all rows)
> 7. Extract every other element of the first row. You should get [1, 3, 5]
> 8. Extract the last row and reverse it. You should get [25, 24, 23, 22, 21]


```python
# 1. Extract the first row of the array
# Your code here
print(arr[0,:])
```

<pre class="output-block">
[1 2 3 4 5]
</pre>

```python
# 2. Extract the last column
# Your code here
print(arr[:,-1])
```

<pre class="output-block">
[ 5 10 15 20 25]
</pre>

```python
# 3. Extract the first three rows
# Your code here
print(arr[:3,:])
```

<pre class="output-block">
[[ 1  2  3  4  5]
 [ 6  7  8  9 10]
 [11 12 13 14 15]]
</pre>

```python
# 4. Extract the central 3x3 square
# Your code here
print(arr[1:4,1:4])
```

<pre class="output-block">
[[ 7  8  9]
 [12 13 14]
 [17 18 19]]
</pre>

```python
# 5. Extract the last column using positive indexing, then do it again using negative indexing
# Your code here
print(arr[:,4])
print(arr[:,-1])
```

<pre class="output-block">
[ 5 10 15 20 25]
[ 5 10 15 20 25]
</pre>

```python
# 6. Extract every other column (and all rows)
# Your code here
print(arr[:,::2])
```

<pre class="output-block">
[[ 1  3  5]
 [ 6  8 10]
 [11 13 15]
 [16 18 20]
 [21 23 25]]
</pre>

```python
# 7. Extract every other element of the first row. You should get [1, 3, 5]
# Your code here
print(arr[0,::2])
```

<pre class="output-block">
[1 3 5]
</pre>

```python
# 8. Extract the last row and reverse it. You should get [25, 24, 23, 22, 21]
# Your code here
print(arr[-1,::-1])
```

<pre class="output-block">
[25 24 23 22 21]
</pre>

>**Bonus Exercises**: Here are some more challenging slicing exercises:
>
> B1. Extract every other column and every other row, starting with the number 1. You should get:
> ```
> [[ 1  3  5]
>  [11 13 15]
>  [21 23 25]]
> ```
> B2. Extract a checkerboard pattern starting from the number 2. You should get:
> ```
> [[ 2  4]
>  [12 14]
>  [22 24]]
> ```


```python
# B1. Extract every other column and every other row, starting with the number 1.
# Your code here
print(arr[::2,::2])
```

<pre class="output-block">
[[ 1  3  5]
 [11 13 15]
 [21 23 25]]
</pre>

```python
# B2. Extract a checkerboard pattern starting from the number 2.
# Your code here
print(arr[1::2,1::2])
```

<pre class="output-block">
[[ 7  9]
 [17 19]]
</pre>

**IMPORTANT**: Slicing arrays creates a **view** of the original array, not a copy. This is known as "passing by reference". That means if you use a slice of an array and modify it, the original array will also be modified.


```python
arr = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
])

print("This is the original array")
print(arr)
print("This is my slice of the array")
slice = arr[1:4,1:4]
print(slice)
print("I'm going to change the slice")
slice[:,:] = 999
print(slice)
print("This is the original array")
print(arr)

```

<pre class="output-block">
This is the original array
[[ 1  2  3  4  5]
 [ 6  7  8  9 10]
 [11 12 13 14 15]
 [16 17 18 19 20]
 [21 22 23 24 25]]
This is my slice of the array
[[ 7  8  9]
 [12 13 14]
 [17 18 19]]
I'm going to change the slice
[[999 999 999]
 [999 999 999]
 [999 999 999]]
This is the original array
[[  1   2   3   4   5]
 [  6 999 999 999  10]
 [ 11 999 999 999  15]
 [ 16 999 999 999  20]
 [ 21  22  23  24  25]]
</pre>

When you do a calculation on a slice of an array, the result will be a new array.


```python
arr = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
])
print("This is the original array")
print(arr)
print("This is my slice of the array")
slice = arr[1:4,1:4]
print(slice)
print("add 100 to each element of the slice")
slice = slice + 100
print(slice)
print("This is the original array")
print(arr)
```

<pre class="output-block">
This is the original array
[[ 1  2  3  4  5]
 [ 6  7  8  9 10]
 [11 12 13 14 15]
 [16 17 18 19 20]
 [21 22 23 24 25]]
This is my slice of the array
[[ 7  8  9]
 [12 13 14]
 [17 18 19]]
add 100 to each element of the slice
[[107 108 109]
 [112 113 114]
 [117 118 119]]
This is the original array
[[ 1  2  3  4  5]
 [ 6  7  8  9 10]
 [11 12 13 14 15]
 [16 17 18 19 20]
 [21 22 23 24 25]]
</pre>

### Using boolean masks to filter arrays

You can use boolean expresssions to **filter** arrays. Here's an example:


```python
# Getting the even numbers from the array
arr = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
])

arr[arr % 2 == 0]
```




<pre class="output-block">
array([ 2,  4,  6,  8, 10, 12, 14, 16, 18, 20, 22, 24])
</pre>

Under the hood, numpy creates a boolean mask that is the same shape as the array. The mask is `True` where the condition is met and `False` where it is not. You can then use the mask to filter the array.


```python
print(arr % 2 == 0)
print(arr)
```

<pre class="output-block">
[[False  True False  True False]
 [ True False  True False  True]
 [False  True False  True False]
 [ True False  True False  True]
 [False  True False  True False]]
[[ 1  2  3  4  5]
 [ 6  7  8  9 10]
 [11 12 13 14 15]
 [16 17 18 19 20]
 [21 22 23 24 25]]
</pre>

When using boolean masks in this way, it's important to note that the original shape of the array is not preserved. So this is useful if you want to filter out elements and do something with that collection of elements, but not if you want to replace certain elements with others.

If you want to replace elements in an array based on a condition, you can use the `np.where()` function. This function takes three arguments: the condition, the value to use if the condition is `True`, and the value to use if the condition is `False`.

In the code block below, we will replace all of the odd numbers in the array with the number 0.


```python
np.where(arr % 2 == 0, arr, 0)
```




<pre class="output-block">
array([[ 0,  2,  0,  4,  0],
       [ 6,  0,  8,  0, 10],
       [ 0, 12,  0, 14,  0],
       [16,  0, 18,  0, 20],
       [ 0, 22,  0, 24,  0]])
</pre>

>**Exercise**: Perform the following operations on the `arr` array using boolean masks:
>
> 1. Extract all values less than the mean
> 2. Trim the array by removing the maximum and mininum value
> 3. Replace the maximum and minimum values with the mean of the entire array


```python
# Extract all values less than the mean
arr = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
])

# Your code here
arr[arr < np.mean(arr)]
```




<pre class="output-block">
array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12])
</pre>

```python
# Trim the array by removing the maximum and mininum value. Use np.min() and np.max() to find the min and max values
# Hint: it might be easiest to explicitly create the boolean mask for this
# The operator & is the element-wise AND operator, it returns True if both elements in an array are True
# Your code here

not_max = arr != np.max(arr)
not_min = arr != np.min(arr)
mask = not_max & not_min

# could also do: mask = (arr != np.max(arr)) & (arr != np.min(arr))
# could also do: mask = np.logical_and(arr != np.max(arr), arr != np.min(arr))
# could also do: mask = np.all([arr != np.max(arr), arr != np.min(arr)], axis=0)

arr[mask]

```




<pre class="output-block">
array([ 2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
       19, 20, 21, 22, 23, 24])
</pre>

>Compare your solution above with a neighbor. Did they do it differently? Find at least one person who did it differently.


```python
# Replace the maximum and minimum values with the mean of the entire array
# Hint: you can use the mask you created above and np.where()

np.where(mask, arr, np.mean(arr))
```




<pre class="output-block">
array([[13.,  2.,  3.,  4.,  5.],
       [ 6.,  7.,  8.,  9., 10.],
       [11., 12., 13., 14., 15.],
       [16., 17., 18., 19., 20.],
       [21., 22., 23., 24., 13.]])
</pre>

## Numpy math functions and additional capabilities

The numpy library isn't just about arrays. It also has a lot of **mathematical functions** that can be applied to arrays. Some of these functions may seem like duplicates of base python functions, but they are optimized for operating on multi-dimensional arrays whereas the base python functions are not. Other functions are unique to numpy and offer more advanced mathematical capabilities.

You can find a list of all mathematical functions in the numpy library [here](https://numpy.org/doc/stable/reference/routines.math.html).


```python
arr = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
])
```


```python
# Getting the mean of the array along the columns
np.mean(arr, axis=0)
```




<pre class="output-block">
array([11., 12., 13., 14., 15.])
</pre>

```python
# getting the mean along the rows
np.mean(arr, axis=1)
```




<pre class="output-block">
array([ 3.,  8., 13., 18., 23.])
</pre>

```python
# getting the standard deviation along the columns
np.std(arr, axis=0)
```




<pre class="output-block">
array([7.07106781, 7.07106781, 7.07106781, 7.07106781, 7.07106781])
</pre>

```python
# getting histogram of the array
np.histogram(arr, bins=5, range=(1, 25))
# if you don't want to hardcode the range, you can use the min and max functions
np.histogram(arr, bins=5, range=(np.min(arr), np.max(arr)))
```




<pre class="output-block">
(array([5, 5, 5, 5, 5]), array([ 1. ,  5.8, 10.6, 15.4, 20.2, 25. ]))
</pre>

## Reading and writing data with numpy

Typically, we're not going to be able to manually enter data into our code's data structures (*e.g.* `my_data = [2, 5, 2, 7, 4]). This would be tedious and time-consuming, given the size of our datasets. This would also make our code useful only for a single dataset at a time, which defeats one of the main purposes of programming!

Instead, we will have data stored as plain text files on our computer or hosted somewhere on the web. These files may be formatted in different ways (*e.g.* CSV files, tab-delimited files, compressed genome sequence files). While there are native Python functions to read plain text files, it is up to us as programmers to write code to accommodate the multitude of formats.

Numpy has two main **functions** for loading in text-based data such as CSVs: `np.loadtxt()` and `np.genfromtxt()`. The main difference between the two is that `np.genfromtxt()` can handle missing data, while `np.loadtxt()` cannot. So, to play it safe, it's usually best to use `np.genfromtxt()`.

Remember that numpy arrays can only contain one type of data, so if your file contains headers or mixed data types, you'll need to use additional options to tell numpy how to handle them.

We will now import a numerical dataset of red wine quality ratings and various chemical properties. It has a header row and is separated by semi-colons. Here's a preview of the data:

```
fixed acidity;volatile acidity;citric acid;residual sugar;chlorides;free sulfur dioxide;total sulfur dioxide;density;pH;sulphates;alcohol;quality
7.4;0.7;0;1.9;0.076;11;34;0.9978;3.51;0.56;9.4;5
7.8;0.88;0;2.6;0.098;25;67;0.9968;3.2;0.68;9.8;5
```


```python
# import using genfromtxt and skip the header
wines_array = np.genfromtxt('https://informatics.fas.harvard.edu/resources/Workshops/2024-Fall/Python/data/winequality-red.csv', delimiter=';', skip_header = 1)
# import the header separately
# we specify the dtype as str so that numpy doesn't try to convert the header to a number
wines_header = np.genfromtxt('https://informatics.fas.harvard.edu/resources/Workshops/2024-Fall/Python/data/winequality-red.csv', delimiter=';', max_rows=1, dtype=str)
print(wines_header)
print(wines_array)
print(wines_array.shape)
```

<pre class="output-block">
['fixed acidity' 'volatile acidity' 'citric acid' 'residual sugar'
 'chlorides' 'free sulfur dioxide' 'total sulfur dioxide' 'density' 'pH'
 'sulphates' 'alcohol' 'quality']
[[ 7.4    0.7    0.    ...  0.56   9.4    5.   ]
 [ 7.8    0.88   0.    ...  0.68   9.8    5.   ]
 [ 7.8    0.76   0.04  ...  0.65   9.8    5.   ]
 ...
 [ 6.3    0.51   0.13  ...  0.75  11.     6.   ]
 [ 5.9    0.645  0.12  ...  0.71  10.2    5.   ]
 [ 6.     0.31   0.47  ...  0.66  11.     6.   ]]
(1599, 12)
</pre>

If all of that looks confusing, just remember that `np.genfromtxt` is a **function**, which is just another block of code somewhere on the computer. Here, we've imported this function from the numpy library, which we've called `np`. Functions take **arguments**, which we learn about from **reading documentation**. Functions **return** values.

In this case, the function takes arguments like (importantly) the path to the file to read and other information about how to read the file. The function then reads the file in the background and returns a numpy array, which we've just learned how to work with.

>**Exercise**: Use `max` or `np.max` to find the max quality rating in the dataset and extract the rows with that rating. Save it to a new array called `best_wines`.


```python
# your code here

rating = np.max(wines_array[:,11])
best_wines = wines_array[wines_array[:,11] == rating]
print(best_wines.shape)
```

<pre class="output-block">
(18, 12)
</pre>

```python
print(best_wines)
```

<pre class="output-block">
[[7.9000e+00 3.5000e-01 4.6000e-01 3.6000e+00 7.8000e-02 1.5000e+01
  3.7000e+01 9.9730e-01 3.3500e+00 8.6000e-01 1.2800e+01 8.0000e+00]
 [1.0300e+01 3.2000e-01 4.5000e-01 6.4000e+00 7.3000e-02 5.0000e+00
  1.3000e+01 9.9760e-01 3.2300e+00 8.2000e-01 1.2600e+01 8.0000e+00]
 [5.6000e+00 8.5000e-01 5.0000e-02 1.4000e+00 4.5000e-02 1.2000e+01
  8.8000e+01 9.9240e-01 3.5600e+00 8.2000e-01 1.2900e+01 8.0000e+00]
 [1.2600e+01 3.1000e-01 7.2000e-01 2.2000e+00 7.2000e-02 6.0000e+00
  2.9000e+01 9.9870e-01 2.8800e+00 8.2000e-01 9.8000e+00 8.0000e+00]
 [1.1300e+01 6.2000e-01 6.7000e-01 5.2000e+00 8.6000e-02 6.0000e+00
  1.9000e+01 9.9880e-01 3.2200e+00 6.9000e-01 1.3400e+01 8.0000e+00]
 [9.4000e+00 3.0000e-01 5.6000e-01 2.8000e+00 8.0000e-02 6.0000e+00
  1.7000e+01 9.9640e-01 3.1500e+00 9.2000e-01 1.1700e+01 8.0000e+00]
 [1.0700e+01 3.5000e-01 5.3000e-01 2.6000e+00 7.0000e-02 5.0000e+00
  1.6000e+01 9.9720e-01 3.1500e+00 6.5000e-01 1.1000e+01 8.0000e+00]
 [1.0700e+01 3.5000e-01 5.3000e-01 2.6000e+00 7.0000e-02 5.0000e+00
  1.6000e+01 9.9720e-01 3.1500e+00 6.5000e-01 1.1000e+01 8.0000e+00]
 [5.0000e+00 4.2000e-01 2.4000e-01 2.0000e+00 6.0000e-02 1.9000e+01
  5.0000e+01 9.9170e-01 3.7200e+00 7.4000e-01 1.4000e+01 8.0000e+00]
 [7.8000e+00 5.7000e-01 9.0000e-02 2.3000e+00 6.5000e-02 3.4000e+01
  4.5000e+01 9.9417e-01 3.4600e+00 7.4000e-01 1.2700e+01 8.0000e+00]
 [9.1000e+00 4.0000e-01 5.0000e-01 1.8000e+00 7.1000e-02 7.0000e+00
  1.6000e+01 9.9462e-01 3.2100e+00 6.9000e-01 1.2500e+01 8.0000e+00]
 [1.0000e+01 2.6000e-01 5.4000e-01 1.9000e+00 8.3000e-02 4.2000e+01
  7.4000e+01 9.9451e-01 2.9800e+00 6.3000e-01 1.1800e+01 8.0000e+00]
 [7.9000e+00 5.4000e-01 3.4000e-01 2.5000e+00 7.6000e-02 8.0000e+00
  1.7000e+01 9.9235e-01 3.2000e+00 7.2000e-01 1.3100e+01 8.0000e+00]
 [8.6000e+00 4.2000e-01 3.9000e-01 1.8000e+00 6.8000e-02 6.0000e+00
  1.2000e+01 9.9516e-01 3.3500e+00 6.9000e-01 1.1700e+01 8.0000e+00]
 [5.5000e+00 4.9000e-01 3.0000e-02 1.8000e+00 4.4000e-02 2.8000e+01
  8.7000e+01 9.9080e-01 3.5000e+00 8.2000e-01 1.4000e+01 8.0000e+00]
 [7.2000e+00 3.3000e-01 3.3000e-01 1.7000e+00 6.1000e-02 3.0000e+00
  1.3000e+01 9.9600e-01 3.2300e+00 1.1000e+00 1.0000e+01 8.0000e+00]
 [7.2000e+00 3.8000e-01 3.1000e-01 2.0000e+00 5.6000e-02 1.5000e+01
  2.9000e+01 9.9472e-01 3.2300e+00 7.6000e-01 1.1300e+01 8.0000e+00]
 [7.4000e+00 3.6000e-01 3.0000e-01 1.8000e+00 7.4000e-02 1.7000e+01
  2.4000e+01 9.9419e-01 3.2400e+00 7.0000e-01 1.1400e+01 8.0000e+00]]
</pre>

Now that we have 18 top wines, let's save them to a new file. We can use the `np.savetxt()` function to save it as a human-readable delimited file. Instead of using semi-colons, we'll use commas to separate the values. The next few lines (`with open()`) are just to print the contents of the file to the screen.


```python
# Saving the array to a csv
np.savetxt("best_wines.csv", best_wines, delimiter=",")
# Reading it back
with open('best_wines.csv', 'r') as file:
    for line in file:
        print(line.strip())
```

<pre class="output-block">
7.900000000000000355e+00,3.499999999999999778e-01,4.600000000000000200e-01,3.600000000000000089e+00,7.799999999999999989e-02,1.500000000000000000e+01,3.700000000000000000e+01,9.972999999999999643e-01,3.350000000000000089e+00,8.599999999999999867e-01,1.280000000000000071e+01,8.000000000000000000e+00
1.030000000000000071e+01,3.200000000000000067e-01,4.500000000000000111e-01,6.400000000000000355e+00,7.299999999999999545e-02,5.000000000000000000e+00,1.300000000000000000e+01,9.976000000000000423e-01,3.229999999999999982e+00,8.199999999999999512e-01,1.259999999999999964e+01,8.000000000000000000e+00
5.599999999999999645e+00,8.499999999999999778e-01,5.000000000000000278e-02,1.399999999999999911e+00,4.499999999999999833e-02,1.200000000000000000e+01,8.800000000000000000e+01,9.923999999999999488e-01,3.560000000000000053e+00,8.199999999999999512e-01,1.290000000000000036e+01,8.000000000000000000e+00
1.259999999999999964e+01,3.099999999999999978e-01,7.199999999999999734e-01,2.200000000000000178e+00,7.199999999999999456e-02,6.000000000000000000e+00,2.900000000000000000e+01,9.987000000000000322e-01,2.879999999999999893e+00,8.199999999999999512e-01,9.800000000000000711e+00,8.000000000000000000e+00
1.130000000000000071e+01,6.199999999999999956e-01,6.700000000000000400e-01,5.200000000000000178e+00,8.599999999999999312e-02,6.000000000000000000e+00,1.900000000000000000e+01,9.988000000000000211e-01,3.220000000000000195e+00,6.899999999999999467e-01,1.340000000000000036e+01,8.000000000000000000e+00
9.400000000000000355e+00,2.999999999999999889e-01,5.600000000000000533e-01,2.799999999999999822e+00,8.000000000000000167e-02,6.000000000000000000e+00,1.700000000000000000e+01,9.963999999999999524e-01,3.149999999999999911e+00,9.200000000000000400e-01,1.169999999999999929e+01,8.000000000000000000e+00
1.069999999999999929e+01,3.499999999999999778e-01,5.300000000000000266e-01,2.600000000000000089e+00,7.000000000000000666e-02,5.000000000000000000e+00,1.600000000000000000e+01,9.971999999999999753e-01,3.149999999999999911e+00,6.500000000000000222e-01,1.100000000000000000e+01,8.000000000000000000e+00
1.069999999999999929e+01,3.499999999999999778e-01,5.300000000000000266e-01,2.600000000000000089e+00,7.000000000000000666e-02,5.000000000000000000e+00,1.600000000000000000e+01,9.971999999999999753e-01,3.149999999999999911e+00,6.500000000000000222e-01,1.100000000000000000e+01,8.000000000000000000e+00
5.000000000000000000e+00,4.199999999999999845e-01,2.399999999999999911e-01,2.000000000000000000e+00,5.999999999999999778e-02,1.900000000000000000e+01,5.000000000000000000e+01,9.917000000000000259e-01,3.720000000000000195e+00,7.399999999999999911e-01,1.400000000000000000e+01,8.000000000000000000e+00
7.799999999999999822e+00,5.699999999999999512e-01,8.999999999999999667e-02,2.299999999999999822e+00,6.500000000000000222e-02,3.400000000000000000e+01,4.500000000000000000e+01,9.941699999999999982e-01,3.459999999999999964e+00,7.399999999999999911e-01,1.269999999999999929e+01,8.000000000000000000e+00
9.099999999999999645e+00,4.000000000000000222e-01,5.000000000000000000e-01,1.800000000000000044e+00,7.099999999999999367e-02,7.000000000000000000e+00,1.600000000000000000e+01,9.946199999999999486e-01,3.209999999999999964e+00,6.899999999999999467e-01,1.250000000000000000e+01,8.000000000000000000e+00
1.000000000000000000e+01,2.600000000000000089e-01,5.400000000000000355e-01,1.899999999999999911e+00,8.300000000000000433e-02,4.200000000000000000e+01,7.400000000000000000e+01,9.945100000000000051e-01,2.979999999999999982e+00,6.300000000000000044e-01,1.180000000000000071e+01,8.000000000000000000e+00
7.900000000000000355e+00,5.400000000000000355e-01,3.400000000000000244e-01,2.500000000000000000e+00,7.599999999999999811e-02,8.000000000000000000e+00,1.700000000000000000e+01,9.923499999999999543e-01,3.200000000000000178e+00,7.199999999999999734e-01,1.309999999999999964e+01,8.000000000000000000e+00
8.599999999999999645e+00,4.199999999999999845e-01,3.900000000000000133e-01,1.800000000000000044e+00,6.800000000000000488e-02,6.000000000000000000e+00,1.200000000000000000e+01,9.951600000000000446e-01,3.350000000000000089e+00,6.899999999999999467e-01,1.169999999999999929e+01,8.000000000000000000e+00
5.500000000000000000e+00,4.899999999999999911e-01,2.999999999999999889e-02,1.800000000000000044e+00,4.399999999999999745e-02,2.800000000000000000e+01,8.700000000000000000e+01,9.908000000000000140e-01,3.500000000000000000e+00,8.199999999999999512e-01,1.400000000000000000e+01,8.000000000000000000e+00
7.200000000000000178e+00,3.300000000000000155e-01,3.300000000000000155e-01,1.699999999999999956e+00,6.099999999999999867e-02,3.000000000000000000e+00,1.300000000000000000e+01,9.959999999999999964e-01,3.229999999999999982e+00,1.100000000000000089e+00,1.000000000000000000e+01,8.000000000000000000e+00
7.200000000000000178e+00,3.800000000000000044e-01,3.099999999999999978e-01,2.000000000000000000e+00,5.600000000000000117e-02,1.500000000000000000e+01,2.900000000000000000e+01,9.947200000000000486e-01,3.229999999999999982e+00,7.600000000000000089e-01,1.130000000000000071e+01,8.000000000000000000e+00
7.400000000000000355e+00,3.599999999999999867e-01,2.999999999999999889e-01,1.800000000000000044e+00,7.399999999999999634e-02,1.700000000000000000e+01,2.400000000000000000e+01,9.941900000000000182e-01,3.240000000000000213e+00,6.999999999999999556e-01,1.140000000000000036e+01,8.000000000000000000e+00
</pre>

What happened to the numbers? The default format for `np.savetxt()` is to save the data as a floating point number with 8 decimal places. However, our original csv did not have that much precision. This is because numpy internally loaded our data in this format but just didn't display the whole thing for us. We can change a number's **display format** using the `fmt` argument. Here's how you would save the data with 3 decimal places. You will also notice that we took the `wines_header` variable and joined it into a single string with commas. This is because `np.savetxt()` expects a single string for the header row.


```python
np.savetxt("best_wines.csv", best_wines, delimiter=",", fmt='%.3f', header=','.join(wines_header))
with open('best_wines.csv', 'r') as file:
    for line in file:
        print(line.strip())
```

<pre class="output-block">
# fixed acidity,volatile acidity,citric acid,residual sugar,chlorides,free sulfur dioxide,total sulfur dioxide,density,pH,sulphates,alcohol,quality
7.900,0.350,0.460,3.600,0.078,15.000,37.000,0.997,3.350,0.860,12.800,8.000
10.300,0.320,0.450,6.400,0.073,5.000,13.000,0.998,3.230,0.820,12.600,8.000
5.600,0.850,0.050,1.400,0.045,12.000,88.000,0.992,3.560,0.820,12.900,8.000
12.600,0.310,0.720,2.200,0.072,6.000,29.000,0.999,2.880,0.820,9.800,8.000
11.300,0.620,0.670,5.200,0.086,6.000,19.000,0.999,3.220,0.690,13.400,8.000
9.400,0.300,0.560,2.800,0.080,6.000,17.000,0.996,3.150,0.920,11.700,8.000
10.700,0.350,0.530,2.600,0.070,5.000,16.000,0.997,3.150,0.650,11.000,8.000
10.700,0.350,0.530,2.600,0.070,5.000,16.000,0.997,3.150,0.650,11.000,8.000
5.000,0.420,0.240,2.000,0.060,19.000,50.000,0.992,3.720,0.740,14.000,8.000
7.800,0.570,0.090,2.300,0.065,34.000,45.000,0.994,3.460,0.740,12.700,8.000
9.100,0.400,0.500,1.800,0.071,7.000,16.000,0.995,3.210,0.690,12.500,8.000
10.000,0.260,0.540,1.900,0.083,42.000,74.000,0.995,2.980,0.630,11.800,8.000
7.900,0.540,0.340,2.500,0.076,8.000,17.000,0.992,3.200,0.720,13.100,8.000
8.600,0.420,0.390,1.800,0.068,6.000,12.000,0.995,3.350,0.690,11.700,8.000
5.500,0.490,0.030,1.800,0.044,28.000,87.000,0.991,3.500,0.820,14.000,8.000
7.200,0.330,0.330,1.700,0.061,3.000,13.000,0.996,3.230,1.100,10.000,8.000
7.200,0.380,0.310,2.000,0.056,15.000,29.000,0.995,3.230,0.760,11.300,8.000
7.400,0.360,0.300,1.800,0.074,17.000,24.000,0.994,3.240,0.700,11.400,8.000
</pre>

This way of saving the data prepends the header row with a `#` character to indicate that it is a comment. That way, if you were to load the data back in with numpy, it would ignore the header row automatically. If you don't want this behavior, you can set the `comments` argument to an empty string. There are a lot of formatting options if you need things to be precisely formatted in print, but we won't go into the details today.

>**Exercise**: Now that we've got the data, let's do one exercise focused on manipulating the data within numpy arrays. Remember what we've learned about slicing arrays and broadcasting operations.
>
> Every chemical property on the wine dataset is measured in different units. Let's normalize all the data so that it is on the same scale. To do this, we will first subtract the mean (`np.mean`) of each column from each element in the column, then divide by the standard deviation of the column (`np.std`). The quality column (last column) is not a chemical property, so we will not normalize it. Save the normalized data + original quality column to a new array.

```python
# Your code here

print(penguins['species'])

print("---")
print(penguins.iloc[0:5,0:5])

print("---")
print(penguins.loc[0:10, ['species', 'island', 'sex']])
```

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

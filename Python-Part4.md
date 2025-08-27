---
title: "[Workshop] Python intensive, part 4"
description: "Introduction to file handling and the numpy library for numerical computing in Python, including arrays and basic operations."
authors:
    - Lei Ma
    - Adam Freedman
---

# Python intensive, part 4

## Introduction

### What is Python and why do we need it/why are you taking this workshop?

* Python is a general purpose programming language that is commonly used for data analysis
* Programming languages are a way for humans to give the computer commands
* Regardless of how you collect data, it needs to be analyzed and code is the best way (Don't use excel!)

### Data analysis in Python

Parts 1-3 of this workshop covered basic programming concepts and syntax in the context of Python. Many of these skills are transferable to any programming language, though the syntax will differ. 

Starting today, we'll be using these skills to learn about Python's capabilities for large-scale data analysis, mainly using the pandas library. Recall that a "library" is just a collection of programs and functions. If the library is installed in your environment and imported into your program, you'll be able to use those functions freely. pandas is a well-maintained library that facilitates data analysis with functions and data structures for reading and interacting with large files.

We'll start with some review, and then start learning about pandas.

### Jupyter basics

Jupyter notebooks are text files that can be rendered as formatted text **and** run code given the proper setup (see Installation).

Text is split into **cells**. Double clicking a cell allows you to edit it.

For code cells, there is also an option to run the code. You can do this by pressing **SHIFT+ENTER** while having it selected, or press the **Run** button at the top of the cell (exact location depends on the editor you're using). Because of the way we set up the notebook the code cells will be running Python code.

For this workshop, we'll be asking you to follow along by running code cells and by doing coding exercises by writing or editing code in code cell.

**IMPORTANT**: Run the code cells below to **import** the **libraries** we'll be using during this workshop.


```python
# Run this cell to import the libraries we'll be using
# If you don't have the kernel loaded or installed, it will not work

import pandas as pd
import os
```

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

## Python review

Let's begin by reviewing some of the terms we've covered in the past sessions that will come up again today.

| Term      | Definition |
| --------- | ---------- |
| Object    | The thing itself (an instance of a class) |
| Variable  | The name we give the object (a pointer to the object) |
| Class     | The blueprint for the object (defines the attributes and methods of object) |
| Method    | A function that belongs to an object |
| Attribute | A property of an object |
| Function  | A piece of code that takes an input and gives an output/does something |
| Argument  | The objects that are passed to the function for it to operate on |
| Library   | Collections of python functions/capabilities that can be installed and loaded on top of base Python |

### Object Methods

Everything in Python is an **object**, and depending on the type of object, they may have certain **methods** that can be called on them. For example, strings have a method called `upper()` that converts the string to uppercase.


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

**Attributes** are properties of an object that can be accessed using the `.` operator.

We'll be learning about some more complex objects today, like **Pandas Series**, which also have attributes. For example, Pandas Series have an attribute called `size` that tells you the number of elements in the underlying data. The difference between an attribute and a method is that attributes are information about a given object, rather than a task being performed on the object. Practically, this means that, while both attributes and methods are called on an object with the dot operator `.`, attributes are accessed without parentheses, so you don't need to call them like functions.


```python
# this makes a pandas Series (we'll learn more about these shortly!)
my_array = pd.Series(["a", "b", "c", "d", "e"])

# this gets the size of the Series
my_array.size
```

<pre class="output-block">5
</pre>

### Base Python Data Structures

When we want to store multiple pieces of data, we use data structures, which are a more complex type of object. We will go over two fundamental data structures that exist in base python (i.e. that don't require additional libraries). 

#### Lists

**Lists** are one the most flexible of data structures in Python. They are created with `[]` and can contain any type of data. Each **element** in a list is separated by a comma. Lists are ordered and can be indexed, sliced, and concatenated just like strings. When lists are all numerical, they can also support mathematical operations like `max()` and `min()`. Lists can also be nested using another `[]` within the list.

Lists are our first introduction to a **mutable** data structure, meaning you can change a list without having to create a new one. Indeed, list methods may modify your data **in place** and/or **return** a new object. If the method modifies the object in place, its return value will be `None`. Modifying in place means you don't have to assign the result of the method to a new variable, while returning a new object means you do have to assign it. For example, `list.append(x)` updates the list in place, while `list.pop()` both returns the last element and removes it from the list in place.

Below are some useful operations and methods for lists. For a full list of methods, you can use `help()` on the list or consult the [docs :octicons-link-external-24:](https://docs.python.org/3/library/stdtypes.html#list){:target="_blank"} page.

**Operations and methods for lists**

| Operation/Method     | Description |
| -------------------- | ----------- |
| `+`                  | Concatenation |
| `*`                  | Repetition |
| `[]`, `[:]`          | Indexing, slicing |
| `.append(x)`         | Add `x` to the end of the list |
| `.extend([x, y, z])` | Add `[x, y, z]` to the end of the list |
| `.insert(i, x)`      | Add `x` at index `i` of the list |
| `.pop(i)`            | Remove and return the element at index `i`, defaults to last element if none given |

**Use cases for lists**

Lists are a data structure that is always there in the background, being useful. We see them when creating simple ordered collections to iterate through, when we need to store a sequence of data to reference later, or when we need to collected a bunch of objects together. Think of lists as a small temporary transport for data. Lists are not good for large datasets (because it will be slow) or when you need to do a lot of mathematical operations (because it lacks functionality).

>**Exercise**: Below is a list of numbers that strictly increases until a peak and then decreases. Find the maximum of the list and the index of the maximum value. You may do this with built-in functions or methods or by iterating through the list manually. 


```python
my_list = [1,2,3,4,5,6,5,4,3,2,1]

# your code here
```

??? success "Solution"
    ```python
    
    my_list = [1,2,3,4,5,6,5,4,3,2,1]
    
    # Using built-in methods
    max_value = max(my_list)
    max_index = my_list.index(max_value)
    print("The peak is", max_value, "at index", max_index)
    
    # By iterating through the list
    max_index = 0
    max_value = my_list[max_index]
    while max_value < my_list[max_index + 1]:
        max_index += 1
        max_value = my_list[max_index]
    print("The peak is", max_value, "at index", max_index)
    ```

    <pre class="output-block">The peak is 6 at index 5
    The peak is 6 at index 5
    </pre>

#### Dictionaries

**Dictionaries** store **key:value pairs**. Keys must be immutable and are typically strings or numerical identifiers, while the values can be just about anything, including other dictionaries, lists, or individual values. You can create a dictionary with `{}` or with the `dict()` function. The two ways to create a dictionary are shown below:

```python
my_dict = {'a': 1, 'b': 2, 'c': 3}
my_dict = dict(("a", 1), ("b", 2), ("c", 3))
```

In recent versions of Python (3.8+), dictionaries keys maintain the order in which they were added, which is useful to maintain consistency when looping over the keys. However, in previous versions of Python, dictionaries were unordered. You can't index or slice dictionaries (since dictionary elements aren't accessed by index). But you can retrieve items by their key, e.g. `my_dict["a"]` or `my_dict.get("a")`. Like lists, dictionaries are mutable, so you can add, remove, or update the key:value pairs in place. Other methods return "View objects" that allow you to see the items in the dictionary, but won't allow you to modify the dictionary, however these objects can usually be easily converted to lists with the `list()` function. Here are some useful methods for dictionaries:

**Operations and methods for dictionaries**

| Operation/Method | Description |
| ---------------- | ----------- |
| `[<key>]`        | Retrieve value by key |
| `.keys()`        | Returns a view object of the keys |
| `.values()`      | Returns a view object of the values |
| `.items()`       | Returns a view object of the key:value pairs |
| `.update(dict)`  | Updates the dictionary with the key:value pairs from another dictionary |

**Use cases for dictionaries**

Dictionaries are a data structure that is more specialized for information that can be organized in a key:value pair way. You may see dictionaries being used to store associations between a name/ID and some characteristics, or to store a set of parameters for a function, or to organize a hierarchical grouping of information. Dictionaries are optimized for fast access to the values by key and for flexible organization of the data. Although you can edit the values of a dictionary, they aren't good for mathematical operations or for ordered data.

>**Exercise**: Using the below dictionary, do the following:
> 
> 1. Print out the entries for each pet.
> 2. Add ["seeds", "fruit"] to the favorite foods of Polly the parrot
> 3. Print the age of Mittens the cat



```python
pets = {
    "Buddy": {
        "name": "Buddy",
        "breed": "Bulldog",
        "age": 4,
        "vaccinated": True,
        "favorite_foods": ["chicken", "peanut butter"],
    },
    "Mittens": {
        "name": "Mittens",
        "breed": "Persian cat",
        "age": 2,
        "vaccinated": False,
        "favorite_foods": ["tuna", "chicken"],
        "owner": {
            "name": "Alice",
            "contact": "555-0123"
        }
    },
    "Polly": {
        "name": "Polly",
        "breed": "Parrot",
        "age": 10,
        "vaccinated": True,
        "words_learned": ["hello", "bye", "Polly wants a cracker"],
    }
}

# Your code here

# 1. Print out the entries for each pet.
# 2. Add ["seeds", "fruit"] to the favorite foods of Polly the parrot
# 3. Print the age of Mittens the cat
```

??? success "Solution"
    ```python
    
    pets = {
        "Buddy": {
            "name": "Buddy",
            "breed": "Bulldog",
            "age": 4,
            "vaccinated": True,
            "favorite_foods": ["chicken", "peanut butter"],
        },
        "Mittens": {
            "name": "Mittens",
            "breed": "Persian cat",
            "age": 2,
            "vaccinated": False,
            "favorite_foods": ["tuna", "chicken"],
            "owner": {
                "name": "Alice",
                "contact": "555-0123"
            }
        },
        "Polly": {
            "name": "Polly",
            "breed": "Parrot",
            "age": 10,
            "vaccinated": True,
            "words_learned": ["hello", "bye", "Polly wants a cracker"],
        }
    }
    
    # 1. Print out the entries for each pet.
    for key in pets:
        print(pets[key])
    
    # 2. Add ["seeds", "fruit"] to the favorite foods of Polly the parrot
    pets["Polly"]["favorite_foods"] = ["seeds", "fruit"]
    print(pets["Polly"]["favorite_foods"])
    
    # 3. Print the age of Mittens the cat
    print(pets["Mittens"]["age"])
    ```

    <pre class="output-block">{'name': 'Buddy', 'breed': 'Bulldog', 'age': 4, 'vaccinated': True, 'favorite_foods': ['chicken', 'peanut butter']}
    {'name': 'Mittens', 'breed': 'Persian cat', 'age': 2, 'vaccinated': False, 'favorite_foods': ['tuna', 'chicken'], 'owner': {'name': 'Alice', 'contact': '555-0123'}}
    {'name': 'Polly', 'breed': 'Parrot', 'age': 10, 'vaccinated': True, 'words_learned': ['hello', 'bye', 'Polly wants a cracker']}
    ['seeds', 'fruit']
    2
    </pre>

### Importing libraries

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

## Reading and writing data

One thing we haven't touched on yet that is integral to data analysis is how to get that data into your program. This is usually done by **reading files**. Likewise, when you've done your analysis and want to save the results you'll have to get that information out of the program so it is saved by **creating and writing to files**. In this next section, we'll learn how to do this first in the native Python way, and then later on we'll see how we can use `pandas` functions to read and write data. We'll use an example of bird names and bird sightings from two CSV files and then write out the total number of sightings for each bird to a new CSV file.

### Vocab

Here are some terms that will be useful to know for the next sections.

| Term                        | Definition |
| --------------------------- | ---------- |
| File                        | A collection of data stored on a disk |
| Line                        | A string of characters that ends with a newline character |
| Newline character           | A special character that indicates the end of a line, usually `\n` |
| Delimiter                   | A character that separates data fields in a line, usually a comma, tab, or space |
| Parsing                     | The process of extracting data from a file |
| Whitespace                  | Any character that represents a space, tab, or newline |
| Leading/trailing whitespace | Whitespace at the beginning or end of a string |

### Reading files with Python

#### Reading data line by line

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

<pre class="output-block">SYSTEM_WGETRC = c:/progra~1/wget/etc/wgetrc
syswgetrc = C:\bin\programs\gnuwin32/etc/wgetrc
--2025-08-27 15:57:17--  https://raw.githubusercontent.com/harvardinformatics/python-intensive/refs/heads/main/data/bird_names.csv
Resolving raw.githubusercontent.com... 185.199.110.133, 185.199.111.133, 185.199.108.133, ...
Connecting to raw.githubusercontent.com|185.199.110.133|:443... connected.
OpenSSL: error:140770FC:SSL routines:SSL23_GET_SERVER_HELLO:unknown protocol
Unable to establish SSL connection.
</pre>

In the code below we first read the file line by line, then strip the whitespace and split the line by a comma. Then, we will create a dictionary where the key is the taxon id and the value is the common name of the bird.


```python
filename = 'bird_names.csv'
if not os.path.exists(filename):
    filename = 'data/bird_names.csv'

bird_names = dict()

with open(filename, 'r') as file:
    for line in file:
        line = line.strip().split(',')
        # split out line[2]
        bird_names[line[2]] = line[1]

print(bird_names)
```

<pre class="output-block">{'6924': 'American Black Duck', '473': 'American Coot', '145310': 'American Goldfinch', '4665': 'American Kestrel', '12727': 'American Robin', '474210': 'American Tree Sparrow', '3936': 'American Woodcock', '16010': 'Ash-throated Flycatcher', '5305': 'Bald Eagle', '9346': 'Baltimore Oriole', '19893': 'Barred Owl', '2548': 'Belted Kingfisher', '144815': 'Black-capped Chickadee', '4981': 'Black-crowned Night Heron', '199916': 'Black-throated Blue Warbler', '8229': 'Blue Jay', '7458': 'Brown Creeper', '10373': 'Brown-headed Cowbird', '6993': 'Bufflehead', '7089': 'Canada Goose', '7513': 'Carolina Wren', '7428': 'Cedar Waxwing', '6571': 'Chimney Swift', '9135': 'Chipping Sparrow', '9602': 'Common Grackle', '4626': 'Common Loon', '7004': 'Common Merganser', '8010': 'Common Raven', '9721': 'Common Yellowthroat', '5112': "Cooper's Hawk", '10094': 'Dark-eyed Junco', '10676': 'Dickcissel', '120479': 'Domestic Greylag Goose', '236935': 'Domestic Mallard', '1454382': 'Double-crested Cormorant', '792988': 'Downy Woodpecker', '16782': 'Eastern Kingbird', '17008': 'Eastern Phoebe', '494355': 'Eastern Red-tailed Hawk', '515821': 'Eastern Song Sparrow', '319123': 'Eastern Wild Turkey', '14850': 'European Starling', '544795': 'European house sparrow', '122767': 'Feral Pigeon', '9156': 'Fox Sparrow', '117100': 'Golden-crowned Kinglet', '14995': 'Gray Catbird', '4368': 'Great Black-backed Gull', '4956': 'Great Blue Heron', '16028': 'Great Crested Flycatcher', '20044': 'Great Horned Owl', '7047': 'Greater Scaup', '5020': 'Green Heron', '6937': 'Green-winged Teal', '514057': 'Greylag Ã— Canada Goose', '792990': 'Hairy Woodpecker', '12890': 'Hermit Thrush', '204533': 'Herring Gull', '7109': 'Hooded Merganser', '4209': 'Horned Grebe', '199840': 'House Finch', '13858': 'House Sparrow', '7562': 'House Wren', '4793': 'Killdeer', '10479': 'Lark Sparrow', '7054': 'Lesser Scaup', '6930': 'Mallard', '326092': 'Mallard Ã— Muscovy Duck', '4672': 'Merlin', '3454': 'Mourning Dove', '6921': 'Mute Swan', '9083': 'Northern Cardinal', '18236': 'Northern Flicker', '14886': 'Northern Mockingbird', '555736': 'Northern Yellow-shafted Flicker', '979757': 'Orange-crowned Warbler', '116999': 'Osprey', '62550': 'Ovenbird', '4647': 'Peregrine Falcon', '17364': 'Philadelphia Vireo', '4246': 'Pied-billed Grebe', '18205': 'Red-bellied Woodpecker', '6996': 'Red-breasted Merganser', '14823': 'Red-breasted Nuthatch', '5212': 'Red-tailed Hawk', '9744': 'Red-winged Blackbird', '7056': 'Redhead', '4364': 'Ring-billed Gull', '7044': 'Ring-necked Duck', '3017': 'Rock Pigeon', '1289388': 'Ruby-crowned Kinglet', '6432': 'Ruby-throated Hummingbird', '850859': 'Ruddy Duck', '9100': 'Song Sparrow', '72458': 'Spotted Sandpiper', '11935': 'Tree Swallow', '13632': 'Tufted Titmouse', '17394': 'Warbling Vireo', '14801': 'White-breasted Nuthatch', '9176': 'White-crowned Sparrow', '9184': 'White-throated Sparrow', '906': 'Wild Turkey', '7107': 'Wood Duck', '145238': 'Yellow Warbler', '18463': 'Yellow-bellied Sapsucker'}
</pre>

>*Discussion:* Explain each line

Here are some handy functions when working with lines in files. These are all string methods, so you can use them on any string, including strings that are read from a file.

**Useful functions for reading files by line**

| Function             | Description |
| -------------------- | ----------- |
| `.strip()`           | Removes leading and trailing whitespace and newlines from a string |
| `.split()`           | Splits a string into a list of strings based on a delimiter |
| `.join()`            | Joins a list of strings into a single string with a delimiter |
| `line[:]`            | Indexing and slicing works on strings too |
| `.replace(old, new)` | Replaces all instances of `old` with `new` in a string |

**Useful special characters**

Special characters in files are often used as delimiters or to indicate the end of a line. The two most common special characters are:

| Character | Description |
| --------- | ----------- |
| `\n`      | Newline character |
| `\t`      | Tab character |

>**Exercise**: Copy the code above and modify it so that the dictionary keys are the taxon ids and the values are another dictionary, with keys 'scientific_name' and 'common_name' and values the appropriate entries for that bird species.
>
> For example, a sample dictionary entry should look like this:
> ```
> {6924: {'scientific_name': 'Anas rubripes', 'common_name': 'American Black Duck'}}
> ```


```python
filename = 'bird_names.csv'
if not os.path.exists(filename):
    filename = 'data/bird_names.csv'

# Your code here
```

??? success "Solution"
    ```python
    
    filename = 'bird_names.csv'
    if not os.path.exists(filename):
        filename = 'data/bird_names.csv'
    
    bird_names = dict()
    
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip().split(',')
            bird_names[line[2]] = {'scientific_name': line[0], 'common_name': line[1]}
    
    print(bird_names)
    ```

    <pre class="output-block">{'6924': {'scientific_name': 'Anas rubripes', 'common_name': 'American Black Duck'}, '473': {'scientific_name': 'Fulica americana', 'common_name': 'American Coot'}, '145310': {'scientific_name': 'Spinus tristis', 'common_name': 'American Goldfinch'}, '4665': {'scientific_name': 'Falco sparverius', 'common_name': 'American Kestrel'}, '12727': {'scientific_name': 'Turdus migratorius', 'common_name': 'American Robin'}, '474210': {'scientific_name': 'Spizelloides arborea', 'common_name': 'American Tree Sparrow'}, '3936': {'scientific_name': 'Scolopax minor', 'common_name': 'American Woodcock'}, '16010': {'scientific_name': 'Myiarchus cinerascens', 'common_name': 'Ash-throated Flycatcher'}, '5305': {'scientific_name': 'Haliaeetus leucocephalus', 'common_name': 'Bald Eagle'}, '9346': {'scientific_name': 'Icterus galbula', 'common_name': 'Baltimore Oriole'}, '19893': {'scientific_name': 'Strix varia', 'common_name': 'Barred Owl'}, '2548': {'scientific_name': 'Megaceryle alcyon', 'common_name': 'Belted Kingfisher'}, '144815': {'scientific_name': 'Poecile atricapillus', 'common_name': 'Black-capped Chickadee'}, '4981': {'scientific_name': 'Nycticorax nycticorax', 'common_name': 'Black-crowned Night Heron'}, '199916': {'scientific_name': 'Setophaga caerulescens', 'common_name': 'Black-throated Blue Warbler'}, '8229': {'scientific_name': 'Cyanocitta cristata', 'common_name': 'Blue Jay'}, '7458': {'scientific_name': 'Certhia americana', 'common_name': 'Brown Creeper'}, '10373': {'scientific_name': 'Molothrus ater', 'common_name': 'Brown-headed Cowbird'}, '6993': {'scientific_name': 'Bucephala albeola', 'common_name': 'Bufflehead'}, '7089': {'scientific_name': 'Branta canadensis', 'common_name': 'Canada Goose'}, '7513': {'scientific_name': 'Thryothorus ludovicianus', 'common_name': 'Carolina Wren'}, '7428': {'scientific_name': 'Bombycilla cedrorum', 'common_name': 'Cedar Waxwing'}, '6571': {'scientific_name': 'Chaetura pelagica', 'common_name': 'Chimney Swift'}, '9135': {'scientific_name': 'Spizella passerina', 'common_name': 'Chipping Sparrow'}, '9602': {'scientific_name': 'Quiscalus quiscula', 'common_name': 'Common Grackle'}, '4626': {'scientific_name': 'Gavia immer', 'common_name': 'Common Loon'}, '7004': {'scientific_name': 'Mergus merganser', 'common_name': 'Common Merganser'}, '8010': {'scientific_name': 'Corvus corax', 'common_name': 'Common Raven'}, '9721': {'scientific_name': 'Geothlypis trichas', 'common_name': 'Common Yellowthroat'}, '5112': {'scientific_name': 'Accipiter cooperii', 'common_name': "Cooper's Hawk"}, '10094': {'scientific_name': 'Junco hyemalis', 'common_name': 'Dark-eyed Junco'}, '10676': {'scientific_name': 'Spiza americana', 'common_name': 'Dickcissel'}, '120479': {'scientific_name': 'Anser anser domesticus', 'common_name': 'Domestic Greylag Goose'}, '236935': {'scientific_name': 'Anas platyrhynchos domesticus', 'common_name': 'Domestic Mallard'}, '1454382': {'scientific_name': 'Nannopterum auritum', 'common_name': 'Double-crested Cormorant'}, '792988': {'scientific_name': 'Dryobates pubescens', 'common_name': 'Downy Woodpecker'}, '16782': {'scientific_name': 'Tyrannus tyrannus', 'common_name': 'Eastern Kingbird'}, '17008': {'scientific_name': 'Sayornis phoebe', 'common_name': 'Eastern Phoebe'}, '494355': {'scientific_name': 'Buteo jamaicensis borealis', 'common_name': 'Eastern Red-tailed Hawk'}, '515821': {'scientific_name': 'Melospiza melodia melodia', 'common_name': 'Eastern Song Sparrow'}, '319123': {'scientific_name': 'Meleagris gallopavo silvestris', 'common_name': 'Eastern Wild Turkey'}, '14850': {'scientific_name': 'Sturnus vulgaris', 'common_name': 'European Starling'}, '544795': {'scientific_name': 'Passer domesticus domesticus', 'common_name': 'European house sparrow'}, '122767': {'scientific_name': 'Columba livia domestica', 'common_name': 'Feral Pigeon'}, '9156': {'scientific_name': 'Passerella iliaca', 'common_name': 'Fox Sparrow'}, '117100': {'scientific_name': 'Regulus satrapa', 'common_name': 'Golden-crowned Kinglet'}, '14995': {'scientific_name': 'Dumetella carolinensis', 'common_name': 'Gray Catbird'}, '4368': {'scientific_name': 'Larus marinus', 'common_name': 'Great Black-backed Gull'}, '4956': {'scientific_name': 'Ardea herodias', 'common_name': 'Great Blue Heron'}, '16028': {'scientific_name': 'Myiarchus crinitus', 'common_name': 'Great Crested Flycatcher'}, '20044': {'scientific_name': 'Bubo virginianus', 'common_name': 'Great Horned Owl'}, '7047': {'scientific_name': 'Aythya marila', 'common_name': 'Greater Scaup'}, '5020': {'scientific_name': 'Butorides virescens', 'common_name': 'Green Heron'}, '6937': {'scientific_name': 'Anas crecca', 'common_name': 'Green-winged Teal'}, '514057': {'scientific_name': 'Anser anser Ã— Branta canadensis', 'common_name': 'Greylag Ã— Canada Goose'}, '792990': {'scientific_name': 'Dryobates villosus', 'common_name': 'Hairy Woodpecker'}, '12890': {'scientific_name': 'Catharus guttatus', 'common_name': 'Hermit Thrush'}, '204533': {'scientific_name': 'Larus argentatus', 'common_name': 'Herring Gull'}, '7109': {'scientific_name': 'Lophodytes cucullatus', 'common_name': 'Hooded Merganser'}, '4209': {'scientific_name': 'Podiceps auritus', 'common_name': 'Horned Grebe'}, '199840': {'scientific_name': 'Haemorhous mexicanus', 'common_name': 'House Finch'}, '13858': {'scientific_name': 'Passer domesticus', 'common_name': 'House Sparrow'}, '7562': {'scientific_name': 'Troglodytes aedon', 'common_name': 'House Wren'}, '4793': {'scientific_name': 'Charadrius vociferus', 'common_name': 'Killdeer'}, '10479': {'scientific_name': 'Chondestes grammacus', 'common_name': 'Lark Sparrow'}, '7054': {'scientific_name': 'Aythya affinis', 'common_name': 'Lesser Scaup'}, '6930': {'scientific_name': 'Anas platyrhynchos', 'common_name': 'Mallard'}, '326092': {'scientific_name': 'Anas platyrhynchos Ã— cairina moschata', 'common_name': 'Mallard Ã— Muscovy Duck'}, '4672': {'scientific_name': 'Falco columbarius', 'common_name': 'Merlin'}, '3454': {'scientific_name': 'Zenaida macroura', 'common_name': 'Mourning Dove'}, '6921': {'scientific_name': 'Cygnus olor', 'common_name': 'Mute Swan'}, '9083': {'scientific_name': 'Cardinalis cardinalis', 'common_name': 'Northern Cardinal'}, '18236': {'scientific_name': 'Colaptes auratus', 'common_name': 'Northern Flicker'}, '14886': {'scientific_name': 'Mimus polyglottos', 'common_name': 'Northern Mockingbird'}, '555736': {'scientific_name': 'Colaptes auratus luteus', 'common_name': 'Northern Yellow-shafted Flicker'}, '979757': {'scientific_name': 'Leiothlypis celata', 'common_name': 'Orange-crowned Warbler'}, '116999': {'scientific_name': 'Pandion haliaetus', 'common_name': 'Osprey'}, '62550': {'scientific_name': 'Seiurus aurocapilla', 'common_name': 'Ovenbird'}, '4647': {'scientific_name': 'Falco peregrinus', 'common_name': 'Peregrine Falcon'}, '17364': {'scientific_name': 'Vireo philadelphicus', 'common_name': 'Philadelphia Vireo'}, '4246': {'scientific_name': 'Podilymbus podiceps', 'common_name': 'Pied-billed Grebe'}, '18205': {'scientific_name': 'Melanerpes carolinus', 'common_name': 'Red-bellied Woodpecker'}, '6996': {'scientific_name': 'Mergus serrator', 'common_name': 'Red-breasted Merganser'}, '14823': {'scientific_name': 'Sitta canadensis', 'common_name': 'Red-breasted Nuthatch'}, '5212': {'scientific_name': 'Buteo jamaicensis', 'common_name': 'Red-tailed Hawk'}, '9744': {'scientific_name': 'Agelaius phoeniceus', 'common_name': 'Red-winged Blackbird'}, '7056': {'scientific_name': 'Aythya americana', 'common_name': 'Redhead'}, '4364': {'scientific_name': 'Larus delawarensis', 'common_name': 'Ring-billed Gull'}, '7044': {'scientific_name': 'Aythya collaris', 'common_name': 'Ring-necked Duck'}, '3017': {'scientific_name': 'Columba livia', 'common_name': 'Rock Pigeon'}, '1289388': {'scientific_name': 'Corthylio calendula', 'common_name': 'Ruby-crowned Kinglet'}, '6432': {'scientific_name': 'Archilochus colubris', 'common_name': 'Ruby-throated Hummingbird'}, '850859': {'scientific_name': 'Oxyura jamaicensis', 'common_name': 'Ruddy Duck'}, '9100': {'scientific_name': 'Melospiza melodia', 'common_name': 'Song Sparrow'}, '72458': {'scientific_name': 'Actitis macularius', 'common_name': 'Spotted Sandpiper'}, '11935': {'scientific_name': 'Tachycineta bicolor', 'common_name': 'Tree Swallow'}, '13632': {'scientific_name': 'Baeolophus bicolor', 'common_name': 'Tufted Titmouse'}, '17394': {'scientific_name': 'Vireo gilvus', 'common_name': 'Warbling Vireo'}, '14801': {'scientific_name': 'Sitta carolinensis', 'common_name': 'White-breasted Nuthatch'}, '9176': {'scientific_name': 'Zonotrichia leucophrys', 'common_name': 'White-crowned Sparrow'}, '9184': {'scientific_name': 'Zonotrichia albicollis', 'common_name': 'White-throated Sparrow'}, '906': {'scientific_name': 'Meleagris gallopavo', 'common_name': 'Wild Turkey'}, '7107': {'scientific_name': 'Aix sponsa', 'common_name': 'Wood Duck'}, '145238': {'scientific_name': 'Setophaga petechia', 'common_name': 'Yellow Warbler'}, '18463': {'scientific_name': 'Sphyrapicus varius', 'common_name': 'Yellow-bellied Sapsucker'}}
    </pre>

>**Exercise**: Why did we use a dictionary to store the data in the previous exercise? Think about what features of a dictionary make it a good choice or what features of lists make them a bad choice.

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

<pre class="output-block">SYSTEM_WGETRC = c:/progra~1/wget/etc/wgetrc
syswgetrc = C:\bin\programs\gnuwin32/etc/wgetrc
--2025-08-27 15:57:18--  https://raw.githubusercontent.com/harvardinformatics/python-intensive/refs/heads/main/data/bird_observations.csv
Resolving raw.githubusercontent.com... 185.199.110.133, 185.199.111.133, 185.199.108.133, ...
Connecting to raw.githubusercontent.com|185.199.110.133|:443... connected.
OpenSSL: error:140770FC:SSL routines:SSL23_GET_SERVER_HELLO:unknown protocol
Unable to establish SSL connection.
</pre>

>**Exercise:** Work with a neighbor or two to do the following exercise:
> Loop through the file and count the number of observations of each species. After all the observations have been counted, print all the species names and the number of observations. You will need to use the dictionary you created in the previous exercise to get the species names. It's up to you what kind of data structure (if any) you want to use to store the counts.
>
> 1. Write out pseudocode for what you will do for each line in your birdfile
> 2. Try to turn the pseudocode into python code. If there's something you want to do, but don't know the syntax or function, raise your hand and we can help you.
> 3. Find out how many European Starlings were observed as proof that your code works.


```python
# Your code here
filename = 'bird_observations.csv'
if not os.path.exists(filename):
    filename = 'data/bird_observations.csv'

bird_observations = dict()

with open(filename, 'r') as birdfile:
    # skip the header
    next(birdfile)
    for line in birdfile:
        # your code here
print(bird_observations)
```

<pre class="output-block">&nbsp;&nbsp;Cell In[19], line 13
&nbsp;&nbsp;&nbsp;&nbsp;print(bird_observations)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;^
IndentationError: expected an indented block after 'for' statement on line 11
</pre>

??? success "Solution"
    ```python
    
    filename = 'bird_observations.csv'
    if not os.path.exists(filename):
        filename = 'data/bird_observations.csv'
    
    bird_observations = dict()
    
    with open(filename, 'r') as birdfile:
        # skip the header
        next(birdfile)
        for line in birdfile:
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

    <pre class="output-block">{'Northern Mockingbird': 23, 'Common Merganser': 4, 'Bufflehead': 9, 'House Sparrow': 69, 'European Starling': 51, 'Northern Cardinal': 28, 'Mourning Dove': 31, 'Blue Jay': 39, 'American Black Duck': 2, 'Domestic Mallard': 14, 'Mute Swan': 33, 'Green-winged Teal': 8, 'American Robin': 92, 'Mallard': 49, 'Great Blue Heron': 26, 'Red-tailed Hawk': 36, 'Canada Goose': 112, 'Downy Woodpecker': 24, 'Ring-necked Duck': 22, 'Wild Turkey': 82, 'Common Loon': 9, 'Horned Grebe': 4, 'Redhead': 8, 'Feral Pigeon': 31, 'Golden-crowned Kinglet': 7, 'Red-bellied Woodpecker': 15, 'Hooded Merganser': 18, 'Belted Kingfisher': 3, 'Red-winged Blackbird': 35, 'Black-capped Chickadee': 14, 'Ruddy Duck': 2, 'Bald Eagle': 2, 'Dark-eyed Junco': 9, 'Carolina Wren': 7, 'House Finch': 19, 'White-throated Sparrow': 5, 'Song Sparrow': 24, 'Yellow-bellied Sapsucker': 3, 'White-breasted Nuthatch': 10, 'Eastern Red-tailed Hawk': 5, 'Tufted Titmouse': 8, "Cooper's Hawk": 17, 'Domestic Greylag Goose': 14, 'Rock Pigeon': 9, 'American Coot': 1, 'Greylag Ã— Canada Goose': 1, 'Eastern Wild Turkey': 1, 'Brown Creeper': 7, 'Hairy Woodpecker': 2, 'Northern Flicker': 6, 'Greater Scaup': 1, 'Red-breasted Merganser': 2, 'American Woodcock': 7, 'Red-breasted Nuthatch': 1, 'Great Horned Owl': 23, 'Peregrine Falcon': 5, 'American Goldfinch': 18, 'Barred Owl': 2, 'Black-crowned Night Heron': 2, 'Tree Swallow': 11, 'Common Grackle': 14, 'Hermit Thrush': 4, 'Northern Yellow-shafted Flicker': 1, 'Chipping Sparrow': 3, 'Killdeer': 2, 'Gray Catbird': 20, 'Double-crested Cormorant': 17, 'Yellow Warbler': 3, 'Warbling Vireo': 2, 'Baltimore Oriole': 7, 'Common Yellowthroat': 2, 'White-crowned Sparrow': 2, 'Black-throated Blue Warbler': 1, 'Ovenbird': 1, 'Brown-headed Cowbird': 4, 'House Wren': 1, 'Cedar Waxwing': 4, 'European house sparrow': 1, 'Herring Gull': 4, 'Eastern Kingbird': 7, 'Great Black-backed Gull': 1, 'Green Heron': 10, 'Great Crested Flycatcher': 1, 'Wood Duck': 6, 'American Kestrel': 1, 'Osprey': 1, 'Ruby-throated Hummingbird': 3, 'Spotted Sandpiper': 2, 'Chimney Swift': 1, 'Eastern Phoebe': 1, 'Lark Sparrow': 2, 'Ring-billed Gull': 1, 'Dickcissel': 1, 'Merlin': 1, 'Ash-throated Flycatcher': 6, 'Pied-billed Grebe': 5, 'Lesser Scaup': 2, 'Orange-crowned Warbler': 2, 'Eastern Song Sparrow': 1, 'Philadelphia Vireo': 1, 'Ruby-crowned Kinglet': 2, 'Mallard Ã— Muscovy Duck': 1, 'Fox Sparrow': 1, 'American Tree Sparrow': 1, 'Common Raven': 1}
    </pre>

If you routinely find yourself reading delimited files, you might want to use the `csv` library. The `csv` library also has the ability to parse Excel files or read and write to/from dictionaries directly. For more information, here's the [doc page :octicons-link-external-24:](https://docs.python.org/3/library/csv.html){:target="_blank"}. Here's what the above code would look like using the `csv` module:


```python
import csv

filename = 'bird_observations.csv'
if not os.path.exists(filename):
    filename = 'data/bird_observations.csv'

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

<pre class="output-block">{'Northern Mockingbird': 23, 'Common Merganser': 4, 'Bufflehead': 9, 'House Sparrow': 69, 'European Starling': 51, 'Northern Cardinal': 28, 'Mourning Dove': 31, 'Blue Jay': 39, 'American Black Duck': 2, 'Domestic Mallard': 14, 'Mute Swan': 33, 'Green-winged Teal': 8, 'American Robin': 92, 'Mallard': 49, 'Great Blue Heron': 26, 'Red-tailed Hawk': 36, 'Canada Goose': 112, 'Downy Woodpecker': 24, 'Ring-necked Duck': 22, 'Wild Turkey': 82, 'Common Loon': 9, 'Horned Grebe': 4, 'Redhead': 8, 'Feral Pigeon': 31, 'Golden-crowned Kinglet': 7, 'Red-bellied Woodpecker': 15, 'Hooded Merganser': 18, 'Belted Kingfisher': 3, 'Red-winged Blackbird': 35, 'Black-capped Chickadee': 14, 'Ruddy Duck': 2, 'Bald Eagle': 2, 'Dark-eyed Junco': 9, 'Carolina Wren': 7, 'House Finch': 19, 'White-throated Sparrow': 5, 'Song Sparrow': 24, 'Yellow-bellied Sapsucker': 3, 'White-breasted Nuthatch': 10, 'Eastern Red-tailed Hawk': 5, 'Tufted Titmouse': 8, "Cooper's Hawk": 17, 'Domestic Greylag Goose': 14, 'Rock Pigeon': 9, 'American Coot': 1, 'Greylag Ã— Canada Goose': 1, 'Eastern Wild Turkey': 1, 'Brown Creeper': 7, 'Hairy Woodpecker': 2, 'Northern Flicker': 6, 'Greater Scaup': 1, 'Red-breasted Merganser': 2, 'American Woodcock': 7, 'Red-breasted Nuthatch': 1, 'Great Horned Owl': 23, 'Peregrine Falcon': 5, 'American Goldfinch': 18, 'Barred Owl': 2, 'Black-crowned Night Heron': 2, 'Tree Swallow': 11, 'Common Grackle': 14, 'Hermit Thrush': 4, 'Northern Yellow-shafted Flicker': 1, 'Chipping Sparrow': 3, 'Killdeer': 2, 'Gray Catbird': 20, 'Double-crested Cormorant': 17, 'Yellow Warbler': 3, 'Warbling Vireo': 2, 'Baltimore Oriole': 7, 'Common Yellowthroat': 2, 'White-crowned Sparrow': 2, 'Black-throated Blue Warbler': 1, 'Ovenbird': 1, 'Brown-headed Cowbird': 4, 'House Wren': 1, 'Cedar Waxwing': 4, 'European house sparrow': 1, 'Herring Gull': 4, 'Eastern Kingbird': 7, 'Great Black-backed Gull': 1, 'Green Heron': 10, 'Great Crested Flycatcher': 1, 'Wood Duck': 6, 'American Kestrel': 1, 'Osprey': 1, 'Ruby-throated Hummingbird': 3, 'Spotted Sandpiper': 2, 'Chimney Swift': 1, 'Eastern Phoebe': 1, 'Lark Sparrow': 2, 'Ring-billed Gull': 1, 'Dickcissel': 1, 'Merlin': 1, 'Ash-throated Flycatcher': 6, 'Pied-billed Grebe': 5, 'Lesser Scaup': 2, 'Orange-crowned Warbler': 2, 'Eastern Song Sparrow': 1, 'Philadelphia Vireo': 1, 'Ruby-crowned Kinglet': 2, 'Mallard Ã— Muscovy Duck': 1, 'Fox Sparrow': 1, 'American Tree Sparrow': 1, 'Common Raven': 1}
</pre>

#### Writing data line by line

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

```

??? success "Solution"
    ```python
    
    import csv
    
    with open('bird_counts.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(['bird', 'count'])
        for bird, count in bird_observations.items():
            writer.writerow([bird, count])
    ```

## Pandas

In this section, we will learn about a python package called `pandas` that contains very helpful functions and data structures for flat data types like the tab or comma-delimited files you might normally read into Excel. In previous iterations of this class, we taught both `pandas` and `numpy`, which is another library that `pandas` uses under the hood. In this workshop, we will focus on `pandas` only, and do a deeper dive. 

First, we'll learn about the basic data structures available in `pandas`, what their closest corollaries are in base Python, and what advantages they have over those corollaries.


### `pandas` series

A `Series` is the simplest data structure in `pandas`. They are one dimensional (1D) objects composed of a **single data type** of any variety (string, integers); you can basically think of them as a single column in a spreadsheet. In that sense they are similar to lists in base Python (and arrays in `numpy`), however unlike those other 1D structures Series also have **label-based indexing**, meaning each element in the object can be accessed by specifying its specific label. In that way, they are also similar to dictionaries in base Python. 


#### Initializing a series

We can manually create a Series in several ways.

Using the `pd.Series()` function, we provide the data we want to store as a series, and optionally we can give each row of the data a label using the `index` argument. If we don't give it the index argument, it will automatically assign a numerical index to each row starting from 0 (just like a Python list). 

When we print the Series, it will display as a column with the index on the left and the data on the right. The type of data being held in the series will be displayed at the bottom of the output. 



```python
#Making a Series using the pd.Series method:
s0 = pd.Series([10, 20, 30, 40])

print(s0)
```

<pre class="output-block">0    10
1    20
2    30
3    40
dtype: int64
</pre>


```python
#Making a Series using the pd.Series method:
s1 = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])

print(s1)
```

<pre class="output-block">a    10
b    20
c    30
d    40
dtype: int64
</pre>

Another way to create a Series is to convert a (non-nested) dictionary into a Series. The keys of the dictionary will become the index labels while the values will become the data. 


```python
# Converting from dictionary to series
my_dictionary = {'first': 10, 'second': 20, 'third': 30}
s2 = pd.Series(my_dictionary)

print(s2)
```

<pre class="output-block">first     10
second    20
third     30
dtype: int64
</pre>

We can then access specific elements in the Series by referring to its index label enclosed in quotes and brackets. This is very similar to how a dictionary works!


```python
print(s0[0])

print(s1["a"])

print(s2["second"])
```

<pre class="output-block">10
10
20
</pre>

So, Series can be thought of as a more versatile version of base Python lists and dictionaries. They are one dimensional. They default to numerical indexing for labeling starting with index 0 (like lists), but have the capability to use labels as indexes as well (like dictionaries).

#### Multi-indexed Series

Series objects may have multiple levels of indices. We call this **multi-indexed**. Using layers of indexing is a way of representing two-dimensional data within a one-dimensional `Series` object. Some people really like using multi-indexed Series. You can create a multi-indexed series by passing a list of lists to the `index` argument of the `pd.Series()` function. The first list will be the outermost level of the index, the second list will be the next level, and so on.


```python
my_index = [["California", "California", "New York", "New York", "Texas", "Texas"], 
            [2001, 2002, 2001, 2002, 2001, 2002]]
my_values = [1.5, 1.7, 3.6, 4.2, 3.2, 4.5]

s3 = pd.Series(my_values, index=my_index)

print(s3)
print("...")
print(s3.index) # an index is an ordered set of tuples
```

<pre class="output-block">California  2001    1.5
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2002    1.7
New York    2001    3.6
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2002    4.2
Texas       2001    3.2
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2002    4.5
dtype: float64
...
MultiIndex([('California', 2001),
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;('California', 2002),
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(  'New York', 2001),
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(  'New York', 2002),
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(     'Texas', 2001),
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(     'Texas', 2002)],
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;)
</pre>

Retrieving an item from this data structure is similar to a nested dictionary, using successive `[]` notation. Or, you can pass it a tuple. You must pass the index labels in the order they were created (left to right)


```python
print("Just printing California")
print(s3["California"])
print("...")

print("Just printing California 2001")
print(s3["California"][2001])
print("...")

print("Using a tuple to get California 2001")
print(s3[("California", 2001)])
print("...")

print("you can also use slicing to select multiple elements")
print(s3["California":"New York"])
print("...")

print("You can use .index.isin to search for values that match your index")
print(s3[s3.index.isin(["Texas", "New York"], level=0)])
print("...")

print("You can select inner levels of multi-indexed series by specifying level=")
print(s3[s3.index.isin([2001], level=1)])
```

<pre class="output-block">Just printing California
2001    1.5
2002    1.7
dtype: float64
...
Just printing California 2001
1.5
...
Using a tuple to get California 2001
1.5
...
you can also use slicing to select multiple elements
California  2001    1.5
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2002    1.7
New York    2001    3.6
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2002    4.2
dtype: float64
...
You can use .index.isin to search for values that match your index
New York  2001    3.6
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2002    4.2
Texas     2001    3.2
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2002    4.5
dtype: float64
...
You can select inner levels of multi-indexed series by specifying level=
California  2001    1.5
New York    2001    3.6
Texas       2001    3.2
dtype: float64
</pre>

In our work, we typically don't use multi-indexed Series. However, they are often the output of pandas functions, so it's good to know how to work with them. If you don't like the idea of multi-indexed Series, you can always convert them to a DataFrame using the `reset_index()` method.


```python
s3.reset_index()
```

<pre class="output-block">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;level_0  level_1    0
0  California     2001  1.5
1  California     2002  1.7
2    New York     2001  3.6
3    New York     2002  4.2
4       Texas     2001  3.2
5       Texas     2002  4.5
</pre>

`pandas` Series are useful for representing a single column of data and have several operations that can be performed on them. These operations include sorting, slicing, mathematical transformations, filtering, and more.

Series objects have built-in methods like `.mean()` and `.std()` that can be used to calculate statistics on the data. Data in Series objects can also be filtered using boolean indexing, like `series_name[series_name > 0]` to get all the values greater than 0. Just like lists, you can perform mathematical operations on Series objects, like addition, subtraction, multiplication, and division.

>**Exercise**: CODE BOWLING. Using the multi-indexed Series below, we have found the most populous state in 2001 and printed it. Expand the 1 liner to at least three lines of code so that it is more readable. 


```python
my_index = [["California", "California", "New York", "New York", "Texas", "Texas"], 
            [2001, 2002, 2001, 2002, 2001, 2002]]
my_values = [1.5, 1.7, 3.6, 4.2, 3.2, 4.5]

s3 = pd.Series(my_values, index=my_index)

# make the below more readable
print(s3[s3.index.isin([2001], level=1)].sort_values(ascending=False).index[0][0])

# your code here
```

<pre class="output-block">New York
</pre>

??? success "Solution"
    ```python
    
    my_index = [["California", "California", "New York", "New York", "Texas", "Texas"], 
                [2001, 2002, 2001, 2002, 2001, 2002]]
    my_values = [1.5, 1.7, 3.6, 4.2, 3.2, 4.5]
    
    s3 = pd.Series(my_values, index=my_index)
    
    # make the below more readable
    print(s3[s3.index.isin([2001], level=1)].sort_values(ascending=False).index[0][0])
    
    # Get all values for the year 2001 across all states
    pop_2001 = s3[s3.index.isin([2001], level=1)]
    
    # Sort the values in descending order to find the most populous state
    pop_2001_sorted = pop_2001.sort_values(ascending=False)
    
    # Get the index (state name) of the most populous state in 2001
    most_populous_2001_state = pop_2001_sorted.index[0][0]
    print(most_populous_2001_state)
    ```

    <pre class="output-block">New York
    New York
    </pre>

## `pandas` DataFrame

Another `pandas` data structure is the **DataFrame**, which is really convenient for its ability to easily perform complex data transformations. This makes it a powerful tool for cleaning, filtering, and summarizing tabular data. 

While a Series is a "one-dimensional" data structure, DataFrames are two-dimensional. Where Series can only contain one type of data, DataFrames can have a combination of numerical and categorical data. Additionally, DataFrames allow you do have labels for your rows and columns. 

DataFrames are essentially a **collection of Series objects**. You can also think of python DataFrames as spreadsheets from Excel or dataframes from R. Since DataFrames are made of multiple Series, the operations we can do on Series are also available on DataFrames

### Initializing a DataFrame

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

<pre class="output-block">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;wrestler  wins         rank
0  Terunofuji    13     yokozuna
1         Ura     6  maegashira2
2      Shodai    10     komusubi
3   Takanosho    12  maegashira6
</pre>

This looks very similar to how we initialize base Python dictionaries.

Pandas dataframes have many **attributes**, including `shape`, `columns`, `index`, `dtypes`. These are useful for understanding the structure of the dataframe.


```python
print(sumo.shape)

print("...")
print(sumo.columns)

print("...")
print(sumo.index)

print("...")
print(sumo.dtypes)
```

<pre class="output-block">(4, 3)
...
Index(['wrestler', 'wins', 'rank'], dtype='object')
...
RangeIndex(start=0, stop=4, step=1)
...
wrestler    object
wins         int64
rank        object
dtype: object
</pre>

Pandas DataFrames also have the handy `info()` function that summarizes the contents of the dataframe, including counts of the non-null values of each column and the data type of each column.


```python
sumo.info()
```

<pre class="output-block"><class 'pandas.core.frame.DataFrame'>
RangeIndex: 4 entries, 0 to 3
Data columns (total 3 columns):
&nbsp;#   Column    Non-Null Count  Dtype
---  ------    --------------  -----
&nbsp;0   wrestler  4 non-null      object
&nbsp;1   wins      4 non-null      int64
&nbsp;2   rank      4 non-null      object
dtypes: int64(1), object(2)
memory usage: 228.0+ bytes
</pre>

## Importing data to `pandas`

Earlier, we leared how to read and write data from and to files in Python. Now, we'll learn how to get data into our program from files using `pandas` functions and data structures. `pandas` natively reads data from tab-delimited files into DataFrames, which is very convenient.

Below you can see an example of how to read files into pandas using the `pd.read_csv()` function. The `csv` stands for 'comma-separated values', which means by defaults it will assume that our columns are separated by **commas**; if we wanted to change the delimiter (e.g. in the case of a tab-separated file), we can set the delimiter explicitly using the `sep=` argument. 


```python
penguins = pd.read_csv("https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2020/2020-07-28/penguins.csv", sep=',')

# The head() function from pandas prints only the first N lines of a dataframe (default: 10)
penguins.head()
```

<pre class="output-block">&nbsp;&nbsp;species     island  bill_length_mm  bill_depth_mm  flipper_length_mm  \
0  Adelie  Torgersen            39.1           18.7              181.0
1  Adelie  Torgersen            39.5           17.4              186.0
2  Adelie  Torgersen            40.3           18.0              195.0
3  Adelie  Torgersen             NaN            NaN                NaN
4  Adelie  Torgersen            36.7           19.3              193.0

&nbsp;&nbsp;&nbsp;body_mass_g     sex  year
0       3750.0    male  2007
1       3800.0  female  2007
2       3250.0  female  2007
3          NaN     NaN  2007
4       3450.0  female  2007
</pre>

When importing data into a DataFrame, pandas automatically detects what data type each column should be. For example, if the column contains only numbers, it will be imported as an floating point or integer data type. If the column contains strings or a mixture of strings and numbers, it will be imported as an "object" data type. Below are the different data types for the penguins column. 


```python
penguins.info()
```

<pre class="output-block"><class 'pandas.core.frame.DataFrame'>
RangeIndex: 344 entries, 0 to 343
Data columns (total 8 columns):
&nbsp;#   Column             Non-Null Count  Dtype
---  ------             --------------  -----
&nbsp;0   species            344 non-null    object
&nbsp;1   island             344 non-null    object
&nbsp;2   bill_length_mm     342 non-null    float64
&nbsp;3   bill_depth_mm      342 non-null    float64
&nbsp;4   flipper_length_mm  342 non-null    float64
&nbsp;5   body_mass_g        342 non-null    float64
&nbsp;6   sex                333 non-null    object
&nbsp;7   year               344 non-null    int64
dtypes: float64(4), int64(1), object(3)
memory usage: 21.6+ KB
</pre>

### Looping through a dataframe

As a note, if we want to go through a dataframe line-by-line (i.e. row by row), because both the rows and columns are indexed it requires slightly more syntax than looping through other data structures (e.g. a dictionary or list). Specifically we need to use the `.iterrows()` method to make the data frame iterable. The `.iterrows()` method outputs each row as a `Series` object with a row index and the column:   


```python
for index, row in penguins.iterrows():
    print(f"Row index: {index}, {row['species']}, {row['island']}")
```

<pre class="output-block">Row index: 0, Adelie, Torgersen
</pre>

<pre class="output-block">
Row index: 1, Adelie, Torgersen
Row index: 2, Adelie, Torgersen
Row index: 3, Adelie, Torgersen
Row index: 4, Adelie, Torgersen
Row index: 5, Adelie, Torgersen
Row index: 6, Adelie, Torgersen
Row index: 7, Adelie, Torgersen
Row index: 8, Adelie, Torgersen
Row index: 9, Adelie, Torgersen
Row index: 10, Adelie, Torgersen
Row index: 11, Adelie, Torgersen
Row index: 12, Adelie, Torgersen
Row index: 13, Adelie, Torgersen
Row index: 14, Adelie, Torgersen
Row index: 15, Adelie, Torgersen
Row index: 16, Adelie, Torgersen
Row index: 17, Adelie, Torgersen
Row index: 18, Adelie, Torgersen
Row index: 19, Adelie, Torgersen
Row index: 20, Adelie, Biscoe
Row index: 21, Adelie, Biscoe
Row index: 22, Adelie, Biscoe
Row index: 23, Adelie, Biscoe
Row index: 24, Adelie, Biscoe
Row index: 25, Adelie, Biscoe
Row index: 26, Adelie, Biscoe
Row index: 27, Adelie, Biscoe
Row index: 28, Adelie, Biscoe
Row index: 29, Adelie, Biscoe
Row index: 30, Adelie, Dream
Row index: 31, Adelie, Dream
Row index: 32, Adelie, Dream
Row index: 33, Adelie, Dream
Row index: 34, Adelie, Dream
Row index: 35, Adelie, Dream
Row index: 36, Adelie, Dream
Row index: 37, Adelie, Dream
Row index: 38, Adelie, Dream
Row index: 39, Adelie, Dream
Row index: 40, Adelie, Dream
Row index: 41, Adelie, Dream
Row index: 42, Adelie, Dream
Row index: 43, Adelie, Dream
Row index: 44, Adelie, Dream
Row index: 45, Adelie, Dream
Row index: 46, Adelie, Dream
Row index: 47, Adelie, Dream
Row index: 48, Adelie, Dream
Row index: 49, Adelie, Dream
Row index: 50, Adelie, Biscoe
Row index: 51, Adelie, Biscoe
Row index: 52, Adelie, Biscoe
Row index: 53, Adelie, Biscoe
Row index: 54, Adelie, Biscoe
Row index: 55, Adelie, Biscoe
Row index: 56, Adelie, Biscoe
Row index: 57, Adelie, Biscoe
Row index: 58, Adelie, Biscoe
Row index: 59, Adelie, Biscoe
Row index: 60, Adelie, Biscoe
Row index: 61, Adelie, Biscoe
Row index: 62, Adelie, Biscoe
Row index: 63, Adelie, Biscoe
Row index: 64, Adelie, Biscoe
Row index: 65, Adelie, Biscoe
Row index: 66, Adelie, Biscoe
Row index: 67, Adelie, Biscoe
Row index: 68, Adelie, Torgersen
Row index: 69, Adelie, Torgersen
Row index: 70, Adelie, Torgersen
Row index: 71, Adelie, Torgersen
Row index: 72, Adelie, Torgersen
Row index: 73, Adelie, Torgersen
Row index: 74, Adelie, Torgersen
Row index: 75, Adelie, Torgersen
Row index: 76, Adelie, Torgersen
Row index: 77, Adelie, Torgersen
Row index: 78, Adelie, Torgersen
</pre>

<pre class="output-block">
Row index: 79, Adelie, Torgersen
Row index: 80, Adelie, Torgersen
Row index: 81, Adelie, Torgersen
Row index: 82, Adelie, Torgersen
Row index: 83, Adelie, Torgersen
Row index: 84, Adelie, Dream
Row index: 85, Adelie, Dream
Row index: 86, Adelie, Dream
Row index: 87, Adelie, Dream
Row index: 88, Adelie, Dream
Row index: 89, Adelie, Dream
Row index: 90, Adelie, Dream
Row index: 91, Adelie, Dream
Row index: 92, Adelie, Dream
Row index: 93, Adelie, Dream
Row index: 94, Adelie, Dream
Row index: 95, Adelie, Dream
Row index: 96, Adelie, Dream
Row index: 97, Adelie, Dream
Row index: 98, Adelie, Dream
Row index: 99, Adelie, Dream
Row index: 100, Adelie, Biscoe
Row index: 101, Adelie, Biscoe
Row index: 102, Adelie, Biscoe
Row index: 103, Adelie, Biscoe
Row index: 104, Adelie, Biscoe
Row index: 105, Adelie, Biscoe
Row index: 106, Adelie, Biscoe
Row index: 107, Adelie, Biscoe
Row index: 108, Adelie, Biscoe
Row index: 109, Adelie, Biscoe
Row index: 110, Adelie, Biscoe
Row index: 111, Adelie, Biscoe
Row index: 112, Adelie, Biscoe
Row index: 113, Adelie, Biscoe
Row index: 114, Adelie, Biscoe
Row index: 115, Adelie, Biscoe
Row index: 116, Adelie, Torgersen
Row index: 117, Adelie, Torgersen
Row index: 118, Adelie, Torgersen
Row index: 119, Adelie, Torgersen
Row index: 120, Adelie, Torgersen
Row index: 121, Adelie, Torgersen
Row index: 122, Adelie, Torgersen
Row index: 123, Adelie, Torgersen
Row index: 124, Adelie, Torgersen
Row index: 125, Adelie, Torgersen
Row index: 126, Adelie, Torgersen
Row index: 127, Adelie, Torgersen
Row index: 128, Adelie, Torgersen
Row index: 129, Adelie, Torgersen
Row index: 130, Adelie, Torgersen
Row index: 131, Adelie, Torgersen
Row index: 132, Adelie, Dream
Row index: 133, Adelie, Dream
Row index: 134, Adelie, Dream
Row index: 135, Adelie, Dream
Row index: 136, Adelie, Dream
Row index: 137, Adelie, Dream
Row index: 138, Adelie, Dream
Row index: 139, Adelie, Dream
Row index: 140, Adelie, Dream
Row index: 141, Adelie, Dream
Row index: 142, Adelie, Dream
Row index: 143, Adelie, Dream
Row index: 144, Adelie, Dream
Row index: 145, Adelie, Dream
Row index: 146, Adelie, Dream
Row index: 147, Adelie, Dream
Row index: 148, Adelie, Dream
Row index: 149, Adelie, Dream
Row index: 150, Adelie, Dream
Row index: 151, Adelie, Dream
Row index: 152, Gentoo, Biscoe
Row index: 153, Gentoo, Biscoe
Row index: 154, Gentoo, Biscoe
Row index: 155, Gentoo, Biscoe
Row index: 156, Gentoo, Biscoe
Row index: 157, Gentoo, Biscoe
Row index: 158, Gentoo, Biscoe
Row index: 159, Gentoo, Biscoe
Row index: 160, Gentoo, Biscoe
Row index: 161, Gentoo, Biscoe
Row index: 162, Gentoo, Biscoe
Row index: 163, Gentoo, Biscoe
Row index: 164, Gentoo, Biscoe
Row index: 165, Gentoo, Biscoe
Row index: 166, Gentoo, Biscoe
Row index: 167, Gentoo, Biscoe
Row index: 168, Gentoo, Biscoe
Row index: 169, Gentoo, Biscoe
Row index: 170, Gentoo, Biscoe
Row index: 171, Gentoo, Biscoe
Row index: 172, Gentoo, Biscoe
Row index: 173, Gentoo, Biscoe
Row index: 174, Gentoo, Biscoe
Row index: 175, Gentoo, Biscoe
Row index: 176, Gentoo, Biscoe
Row index: 177, Gentoo, Biscoe
Row index: 178, Gentoo, Biscoe
Row index: 179, Gentoo, Biscoe
Row index: 180, Gentoo, Biscoe
Row index: 181, Gentoo, Biscoe
Row index: 182, Gentoo, Biscoe
Row index: 183, Gentoo, Biscoe
Row index: 184, Gentoo, Biscoe
Row index: 185, Gentoo, Biscoe
Row index: 186, Gentoo, Biscoe
Row index: 187, Gentoo, Biscoe
Row index: 188, Gentoo, Biscoe
Row index: 189, Gentoo, Biscoe
Row index: 190, Gentoo, Biscoe
Row index: 191, Gentoo, Biscoe
Row index: 192, Gentoo, Biscoe
Row index: 193, Gentoo, Biscoe
Row index: 194, Gentoo, Biscoe
Row index: 195, Gentoo, Biscoe
Row index: 196, Gentoo, Biscoe
Row index: 197, Gentoo, Biscoe
Row index: 198, Gentoo, Biscoe
Row index: 199, Gentoo, Biscoe
Row index: 200, Gentoo, Biscoe
Row index: 201, Gentoo, Biscoe
Row index: 202, Gentoo, Biscoe
Row index: 203, Gentoo, Biscoe
Row index: 204, Gentoo, Biscoe
Row index: 205, Gentoo, Biscoe
Row index: 206, Gentoo, Biscoe
Row index: 207, Gentoo, Biscoe
Row index: 208, Gentoo, Biscoe
Row index: 209, Gentoo, Biscoe
Row index: 210, Gentoo, Biscoe
Row index: 211, Gentoo, Biscoe
Row index: 212, Gentoo, Biscoe
Row index: 213, Gentoo, Biscoe
Row index: 214, Gentoo, Biscoe
Row index: 215, Gentoo, Biscoe
Row index: 216, Gentoo, Biscoe
Row index: 217, Gentoo, Biscoe
Row index: 218, Gentoo, Biscoe
Row index: 219, Gentoo, Biscoe
Row index: 220, Gentoo, Biscoe
Row index: 221, Gentoo, Biscoe
Row index: 222, Gentoo, Biscoe
Row index: 223, Gentoo, Biscoe
Row index: 224, Gentoo, Biscoe
Row index: 225, Gentoo, Biscoe
Row index: 226, Gentoo, Biscoe
Row index: 227, Gentoo, Biscoe
Row index: 228, Gentoo, Biscoe
Row index: 229, Gentoo, Biscoe
Row index: 230, Gentoo, Biscoe
Row index: 231, Gentoo, Biscoe
Row index: 232, Gentoo, Biscoe
Row index: 233, Gentoo, Biscoe
Row index: 234, Gentoo, Biscoe
Row index: 235, Gentoo, Biscoe
Row index: 236, Gentoo, Biscoe
Row index: 237, Gentoo, Biscoe
Row index: 238, Gentoo, Biscoe
Row index: 239, Gentoo, Biscoe
Row index: 240, Gentoo, Biscoe
Row index: 241, Gentoo, Biscoe
Row index: 242, Gentoo, Biscoe
Row index: 243, Gentoo, Biscoe
Row index: 244, Gentoo, Biscoe
Row index: 245, Gentoo, Biscoe
Row index: 246, Gentoo, Biscoe
Row index: 247, Gentoo, Biscoe
Row index: 248, Gentoo, Biscoe
Row index: 249, Gentoo, Biscoe
Row index: 250, Gentoo, Biscoe
Row index: 251, Gentoo, Biscoe
Row index: 252, Gentoo, Biscoe
Row index: 253, Gentoo, Biscoe
Row index: 254, Gentoo, Biscoe
Row index: 255, Gentoo, Biscoe
Row index: 256, Gentoo, Biscoe
Row index: 257, Gentoo, Biscoe
Row index: 258, Gentoo, Biscoe
Row index: 259, Gentoo, Biscoe
Row index: 260, Gentoo, Biscoe
Row index: 261, Gentoo, Biscoe
Row index: 262, Gentoo, Biscoe
Row index: 263, Gentoo, Biscoe
Row index: 264, Gentoo, Biscoe
Row index: 265, Gentoo, Biscoe
Row index: 266, Gentoo, Biscoe
Row index: 267, Gentoo, Biscoe
Row index: 268, Gentoo, Biscoe
Row index: 269, Gentoo, Biscoe
Row index: 270, Gentoo, Biscoe
Row index: 271, Gentoo, Biscoe
Row index: 272, Gentoo, Biscoe
Row index: 273, Gentoo, Biscoe
Row index: 274, Gentoo, Biscoe
Row index: 275, Gentoo, Biscoe
Row index: 276, Chinstrap, Dream
Row index: 277, Chinstrap, Dream
Row index: 278, Chinstrap, Dream
Row index: 279, Chinstrap, Dream
Row index: 280, Chinstrap, Dream
Row index: 281, Chinstrap, Dream
Row index: 282, Chinstrap, Dream
Row index: 283, Chinstrap, Dream
Row index: 284, Chinstrap, Dream
Row index: 285, Chinstrap, Dream
Row index: 286, Chinstrap, Dream
Row index: 287, Chinstrap, Dream
Row index: 288, Chinstrap, Dream
Row index: 289, Chinstrap, Dream
Row index: 290, Chinstrap, Dream
Row index: 291, Chinstrap, Dream
Row index: 292, Chinstrap, Dream
Row index: 293, Chinstrap, Dream
Row index: 294, Chinstrap, Dream
Row index: 295, Chinstrap, Dream
Row index: 296, Chinstrap, Dream
Row index: 297, Chinstrap, Dream
Row index: 298, Chinstrap, Dream
Row index: 299, Chinstrap, Dream
Row index: 300, Chinstrap, Dream
Row index: 301, Chinstrap, Dream
Row index: 302, Chinstrap, Dream
Row index: 303, Chinstrap, Dream
Row index: 304, Chinstrap, Dream
Row index: 305, Chinstrap, Dream
Row index: 306, Chinstrap, Dream
Row index: 307, Chinstrap, Dream
Row index: 308, Chinstrap, Dream
Row index: 309, Chinstrap, Dream
Row index: 310, Chinstrap, Dream
Row index: 311, Chinstrap, Dream
Row index: 312, Chinstrap, Dream
Row index: 313, Chinstrap, Dream
Row index: 314, Chinstrap, Dream
Row index: 315, Chinstrap, Dream
Row index: 316, Chinstrap, Dream
Row index: 317, Chinstrap, Dream
Row index: 318, Chinstrap, Dream
Row index: 319, Chinstrap, Dream
Row index: 320, Chinstrap, Dream
Row index: 321, Chinstrap, Dream
Row index: 322, Chinstrap, Dream
Row index: 323, Chinstrap, Dream
Row index: 324, Chinstrap, Dream
Row index: 325, Chinstrap, Dream
Row index: 326, Chinstrap, Dream
Row index: 327, Chinstrap, Dream
Row index: 328, Chinstrap, Dream
Row index: 329, Chinstrap, Dream
Row index: 330, Chinstrap, Dream
Row index: 331, Chinstrap, Dream
Row index: 332, Chinstrap, Dream
Row index: 333, Chinstrap, Dream
Row index: 334, Chinstrap, Dream
Row index: 335, Chinstrap, Dream
Row index: 336, Chinstrap, Dream
Row index: 337, Chinstrap, Dream
Row index: 338, Chinstrap, Dream
Row index: 339, Chinstrap, Dream
Row index: 340, Chinstrap, Dream
Row index: 341, Chinstrap, Dream
Row index: 342, Chinstrap, Dream
Row index: 343, Chinstrap, Dream
</pre>

This can be slow for very large dataframes, but is useful if you need to perform actions on individual rows.

Before we dive into working with real data, we're going to create some DataFrames from scratch to better understand how they work.


## Selecting data in a `pandas` dataframe

As with series objects, `pandas` dataframes rows and columns are *explicitly indexed*, which means that every row and column has a label associated with it. You can think of the explicit indices as the being the names of the rows and the names of the columns.  

Unfortunately, in `pandas` the syntax for subsetting rows v.s. columns is different and can get a little confusing, so let's go through several different use cases.

### Selecting columns
We can always check the names of the columns in a `pandas` dataframe byt using the built-in `.columns` method, which simply lists the column index:


```python
sumo.columns
```

<pre class="output-block">Index(['wrestler', 'wins', 'rank'], dtype='object')
</pre>

If we want to refer to a specific column, we can specify its index (enclosed in double quotes) inside of square brackets `[]` like so:


```python
#Single column:
sumo["wrestler"]
```

<pre class="output-block">0    Terunofuji
1           Ura
2        Shodai
3     Takanosho
Name: wrestler, dtype: object
</pre>

If we want to refer to *multiple* columns, we need to pass the columns as a **list** by enclosing the column indices in square brackets, so you will end up with *double brackets*:


```python
#Multiple columns (note the double []!):
sumo[["wrestler", "rank"]]
```

<pre class="output-block">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;wrestler         rank
0  Terunofuji     yokozuna
1         Ura  maegashira2
2      Shodai     komusubi
3   Takanosho  maegashira6
</pre>

### Selecting rows:

The syntax for selecting specific rows is slightly different. Let's first check the labels of the row index; to do this we use the `.index` method:


```python
print(sumo.index)
```

<pre class="output-block">RangeIndex(start=0, stop=4, step=1)
</pre>

Here we can see that while the column index labels were strings, the row index labels are *numerical values*, in this case `0` thru `3`. If we wanted to pull out the first row, we need to specify its index label (`0`) in combination with the `.loc` method (which is required for rows): 


```python
sumo.loc[0]
```

<pre class="output-block">wrestler    Terunofuji
wins                13
rank          yokozuna
Name: 0, dtype: object
</pre>

If we want to select multiple rows, like with columns we need to pass it as a list using the double brackets. If we want to specify a **range** of rows (i.e. from this row to that row), we **don't** use double brackets and instead use `:`:


```python
print(sumo.loc[[0,1]])
```

<pre class="output-block">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;wrestler  wins         rank
0  Terunofuji    13     yokozuna
1         Ura     6  maegashira2
</pre>


```python
print(sumo.loc[0:2])
```

<pre class="output-block">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;wrestler  wins         rank
0  Terunofuji    13     yokozuna
1         Ura     6  maegashira2
2      Shodai    10     komusubi
</pre>

Note that in this case the row index labels are numbers, but do not have to be numerical, and can have string labels similar to columns. Let's show how we could change the row index labels by taking the column with the wrestler's rank and setting it as the index label (note that the labels should be unique!):


```python
sumo = sumo.set_index("rank")

print(sumo)
```

<pre class="output-block">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;wrestler  wins
rank
yokozuna     Terunofuji    13
maegashira2         Ura     6
komusubi         Shodai    10
maegashira6   Takanosho    12
</pre>


```python
sumo.loc["yokozuna"]
```

<pre class="output-block">wrestler    Terunofuji
wins                13
Name: yokozuna, dtype: object
</pre>

We also need to use `.loc` if we are referring to a specific row AND column, e.g.:


```python
print(sumo.loc["komusubi", "wrestler"])
```

<pre class="output-block">Shodai
</pre>

If we want to purely use numerical indexing, we can use the `.iloc()` method. If you use `.iloc()`, you can index a DataFrame using just the coordinates of the cells (but remember to begin counting from 0). 


```python
# Select the first two rows and the first two columns

sumo.iloc[0:2, 0:2]
```

<pre class="output-block">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;wrestler  wins
rank
yokozuna     Terunofuji    13
maegashira2         Ura     6
</pre>

There are many ways to select subsets of a dataframe. The rows and columns of a dataframe can be referred to either by their integer position or by their indexed name. Typically, for columns, you'll use the indexed name and can just do `[]` with the name of the column. For rows, if you want to use the integer position, you will use `.iloc[]`. If you want to use the index name, you will use `.loc[]`. 

For reference, here's a handy table on the best ways to index into a dataframe:

| Action                  | Named index                            | Integer Position |
| ----------------------- | -------------------------------------- | ---------------- |
| Select single column    | `df['column_name']`                    | `df.iloc[:, column_position]` |
| Select multiple columns | `df[['column_name1', 'column_name2']]` | `df.iloc[:, [column_position1, column_position2]]` |
| Select single row       | `df.loc['row_name']`                   | `df.iloc[row_position]` |
| Select multiple rows    | `df.loc[['row_name1', 'row_name2']]`   | `df.iloc[[row_position1, row_position2]]` |

> **Exercise**: We'll use the penguins dataset from our initial example.
> 1) Print the 'species' column
> 2) Print the first five columns and first five rows
> 3) Print the columns "species", "island", and "sex" and the first ten rows of the dataframe


```python
penguins.info()
```

<pre class="output-block"><class 'pandas.core.frame.DataFrame'>
RangeIndex: 344 entries, 0 to 343
Data columns (total 8 columns):
&nbsp;#   Column             Non-Null Count  Dtype
---  ------             --------------  -----
&nbsp;0   species            344 non-null    object
&nbsp;1   island             344 non-null    object
&nbsp;2   bill_length_mm     342 non-null    float64
&nbsp;3   bill_depth_mm      342 non-null    float64
&nbsp;4   flipper_length_mm  342 non-null    float64
&nbsp;5   body_mass_g        342 non-null    float64
&nbsp;6   sex                333 non-null    object
&nbsp;7   year               344 non-null    int64
dtypes: float64(4), int64(1), object(3)
memory usage: 21.6+ KB
</pre>


```python
# 1. Print the "species" column

# 2. Print the first 5 columns and first five rows

# 3. Print the columns "species", "island", and "sex" and the first 10 rows of the dataframe
```

??? success "Solution"
    ```python
    
    # 1. Print the "species" column
    print(penguins['species'])
    print("...")
    
    # 2. Print the first 5 columns and first five rows
    print(penguins.iloc[0:5,0:5])
    print("...")
    
    # 3. Print the columns "species", "island", and "sex" and the first 10 rows of the dataframe
    print(penguins.loc[0:10, ['species', 'island', 'sex']])
    ```

    <pre class="output-block">0         Adelie
    1         Adelie
    2         Adelie
    3         Adelie
    4         Adelie
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;...
    339    Chinstrap
    340    Chinstrap
    341    Chinstrap
    342    Chinstrap
    343    Chinstrap
    Name: species, Length: 344, dtype: object
    ...
    &nbsp;&nbsp;species     island  bill_length_mm  bill_depth_mm  flipper_length_mm
    0  Adelie  Torgersen            39.1           18.7              181.0
    1  Adelie  Torgersen            39.5           17.4              186.0
    2  Adelie  Torgersen            40.3           18.0              195.0
    3  Adelie  Torgersen             NaN            NaN                NaN
    4  Adelie  Torgersen            36.7           19.3              193.0
    ...
    &nbsp;&nbsp;&nbsp;species     island     sex
    0   Adelie  Torgersen    male
    1   Adelie  Torgersen  female
    2   Adelie  Torgersen  female
    3   Adelie  Torgersen     NaN
    4   Adelie  Torgersen  female
    5   Adelie  Torgersen    male
    6   Adelie  Torgersen  female
    7   Adelie  Torgersen    male
    8   Adelie  Torgersen     NaN
    9   Adelie  Torgersen     NaN
    10  Adelie  Torgersen     NaN
    </pre>

## Learning to read documentation

Before we dive deeper into learning about Pandas dataframes, we will learn how to read documentation. This is because libraries such as pandas have many features that we will not have the time to cover in detail. Instead, if you can read documentation efficiently, you can learn how to use these libraries on your own.

**Programming effectively actually involves a lot of reading**

Programming involves reading primarily documentation, but also code, search results, stackexchange queries, etc. These are just a few examples of what you'll read as you work on code. Reading the documentation of a package or library or software that you are using should probably be the first thing you do when you start using it. However, software docs pages are a much different sort of writing than we may be used to, if we're primarily used to reading journal articles, textbooks, and protocols. Knowing how and how much to read documentation is a skill that needs to be developed over time to suit your own needs. There's definitely no need to read every single page of documentation of a piece of software, especially for large libraries like `pandas` or `seaborn`.

**There are a variety of ways software can be documented**

You may be handed a single script from a colleague to perform some action and that script may have **comments** in the code detailing what it does or what certain lines do. Individual functions may have what is called a **docstring**, which is a string that occurs immediately after the function definition detailing how do use that function, inputs, and outputs. Another type of documentation is a docs page or **API reference** on a website for that software, such as the page for the seaborn's [scatterplot :octicons-link-external-24:](https://seaborn.pydata.org/generated/seaborn.scatterplot.html){:target="_blank"} function. Many software packages also have some introductory pages like **vignettes** or **tutorials** that guide you through the basics of the software. The [Getting started tutorials :octicons-link-external-24:](https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html){:target="_blank"} of Pandas is a good example of this.

**What documentation are we meant to read?**

In general, documentation is meant to be a reference manual more than a textbook. A lot of documentation is really repetitive, because it has to exhaustively cover every single function, class, and use-case available to the user. I do not recommend reading documentation like a book or in any linear way. That's like learning a foreign language by reading the dictionary. For example, `pandas` has a variety of [mathematical functions :octicons-link-external-24:](https://pandas.pydata.org/docs/reference/frame.html#computations-descriptive-stats){:target="_blank"}, but you are not required to look at the doc page of each of those. It is enough to know that it exists and when you do want to use a particular one, to check the page of that specific function. The most important parts of the documentation to read first are the tutorials/user guides, which introduce the basic functionality of the software with some example code. Often times, this code is exactly what you need to get started. If you get stuck, then it's time to read the docs pages for the specific commands you are using.

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


>**Exercise:** You're looking for a way to replace NaN values with a specific dummy value. Which of the following functions is best suited for this task?
>
>1. `pandas.DataFrame.dropna()` [docs :octicons-link-external-24:](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dropna.html){:target="_blank"}
>2. `pandas.DataFrame.fillna()` [docs :octicons-link-external-24:](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.fillna.html){:target="_blank"}
>3. `pandas.DataFrame.replace()` [docs :octicons-link-external-24:](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.replace.html){:target="_blank"}

<details><summary>Solution</summary>
pandas.DataFrame.fillna() is the best suited for this task. This is a function created specifically to fill NaN values with a specified value. While you could use the .replace() function to replace NaN values, fillna() is more straightforward for this task. Meanwhile, dropna() only removes rows or columns with NaN values, which is not what we want.
</details>


**Troubleshooting**

Looking at a docs page is helpful for troubleshooting certain errors. In this next exercise, you will have to take a closer look at the parameters section of the docs page to find the solution. 

>**Exercise:** You have a dataframe where some numeric values are stored as strings, and you want to convert them to numeric values. Sometimes you also have non-numeric values stored in numeric columns, that you want to convert to NaN. However, when you try to use the `pandas.to_numeric()` function, you get an error. What could be the issue? How would you fix it? [docs :octicons-link-external-24:](https://pandas.pydata.org/docs/reference/api/pandas.to_numeric.html){:target="_blank"}


```python
my_series = pd.Series(["1", "2", "missing", "3"])

pd.to_numeric(my_series)
```

<pre class="output-block">---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
File pandas/_libs/lib.pyx:2407, in pandas._libs.lib.maybe_convert_numeric()

ValueError: Unable to parse string "missing"

During handling of the above exception, another exception occurred:

ValueError                                Traceback (most recent call last)
Cell In[54], line 3
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1 my_series = pd.Series(["1", "2", "missing", "3"])
----> 3 pd.to_numeric(my_series)

File C:\bin\miniforge3\Lib\site-packages\pandas\core\tools\numeric.py:235, in to_numeric(arg, errors, downcast, dtype_backend)
&nbsp;&nbsp;&nbsp;&nbsp;233 coerce_numeric = errors not in ("ignore", "raise")
&nbsp;&nbsp;&nbsp;&nbsp;234 try:
--> 235     values, new_mask = lib.maybe_convert_numeric(  # type: ignore[call-overload]
&nbsp;&nbsp;&nbsp;&nbsp;236         values,
&nbsp;&nbsp;&nbsp;&nbsp;237         set(),
&nbsp;&nbsp;&nbsp;&nbsp;238         coerce_numeric=coerce_numeric,
&nbsp;&nbsp;&nbsp;&nbsp;239         convert_to_masked_nullable=dtype_backend is not lib.no_default
&nbsp;&nbsp;&nbsp;&nbsp;240         or isinstance(values_dtype, StringDtype)
&nbsp;&nbsp;&nbsp;&nbsp;241         and values_dtype.na_value is libmissing.NA,
&nbsp;&nbsp;&nbsp;&nbsp;242     )
&nbsp;&nbsp;&nbsp;&nbsp;243 except (ValueError, TypeError):
&nbsp;&nbsp;&nbsp;&nbsp;244     if errors == "raise":

File pandas/_libs/lib.pyx:2449, in pandas._libs.lib.maybe_convert_numeric()

ValueError: Unable to parse string "missing" at position 2
</pre>

??? success "Solution"
    ```python
    
    my_series = pd.Series(["1", "2", "missing", "3"])
    
    pd.to_numeric(my_series, errors="coerce")
    ```

    <pre class="output-block">0    1.0
    1    2.0
    2    NaN
    3    3.0
    dtype: float64
    </pre>

**Exploring**

If you have data you want to import into pandas, it is worth reading the User Guide section on [IO tools :octicons-link-external-24:](https://pandas.pydata.org/docs/user_guide/io.html){:target="_blank"} to see how to import different formats. Here you might find that if you have a large dataset that you access frequently, you can save it in a format that is optimized for speed, such as `parquet` or `pickle`. If you want to minimize the size of the file, you can save it as a `compressed pickle` format. 

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

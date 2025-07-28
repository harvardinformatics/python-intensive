---
title: "[Workshop] Python intensive, day 1"
description: "Introduction to programming concepts such as functions, data types, operators, logic, and control flow."
authors:
    - Gregg Thomas
    - Tim Sackton
---

This is a test block to trigger the workflow.

# Python intensive, day 1

## Introduction

Welcome to the first day of the Harvard Informatics Python intensive workshop. This is a six day workshop intended to give a quick, yet thorough, introduction programming concepts, the Python programming language, and how to use Python to facilitate data analysis.

Programmatic analysis of data allows the scientist to have full control over how their data is parsed, assessed, and presented, unlike using third party programs (like Excel) which may make unwanted assumptions about how you want to read your data. The upside of this is that one could conceivably perform any analysis imaginable on their data, assuming they have enough coding skills. The downside is that one must know how to program. But that is the goal of this workshop: to give you the understanding of programming concepts and underlying skills such that you can see a problem or question in your work and then be able to understand how you would code the solution.

While their are several programming languages one could use for data analysis, we chose to teach Python because it is more open-ended than alternatives (*e.g.* R being the main one for data analysis). Python is typed more like a traditional programming language, making the skills highly transferable to other languages.

### Terminology

Before we get started teaching any workshop, I like to point out that, like any specific domain, the way we talk about programming is almost its own language. Words in this context may have different meaning than in other contexts. As programmers ourselves, we are so used to using words in the context of programming that we sometimes forget others aren't used to it.

This is all to say, if you hear us saying a word that you're familiar with but it's obvious that we're using it in a different way, or if you hear an unfamiliar term, please ask us to explain it. This knowledge gap is one of the most difficult parts about teaching a specific topic mostly because the teachers aren't usually aware of it.

We also have a table of common programming terms with their definitions in this context: [Programming terminology](https://informatics.fas.harvard.edu/resources/glossary/).

Please let us know if there is anything you think we should add to this table.

### Installation

This workshop exists as a **Jupyter notebook**. You can participate in this workshop by using this notebook interactively simply by uploading it to Google Colab. Go to https://colab.research.google.com/ and upload this notebook. That's it! This is the recommended way for participating in this workshop. Skip the below instructions if you will be using Google Colab.

<br>

---

**See above for the recommended way to participate in this workshop. Only follow these instructions if Google Colab isn't working**

If for some reason Google Colab isn't working, or you prefer to run this locally, you will need to install Python, Anaconda, and the necessary libraries. You will have to follow these steps to do so. Note that some steps are only meant for specific operating systems.

0. If you are on Windows, [install WSL :octicons-link-external-24:](https://learn.microsoft.com/en-us/windows/wsl/install){:target="_blank"}. Once WSL is installed, you'll have a Linux terminal available to you in Windows. You can open this terminal by typing "wsl" in the search bar and clicking the app that appears. You'll also find your Linux distribution as a mounted drive in your file explorer.

1. Install mamba, a package manager using the command line - Terminal for Mac or WSL for Windows.

    1.1. For Mac, if you already have brew installed, install mamba using `brew install miniforge` and initialize it using `conda init zsh`. Then restart your terminal. If you don't have homebrew (i.e. the brew command doesn't exist), install brew first using `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
    
    1.2. For Windows, download the Linux (x86_64) installer from the miniforge repository [here :octicons-link-external-24:](https://github.com/conda-forge/miniforge){:target="_blank"} and install with `bash Miniforge3-Linux-x86_64.sh`.

2. Create a new environment using mamba with `mamba create -n pyworkshop numpy pandas matplotlib seaborn jupyter` and activate it with `conda activate pyworkshop`.

3. You can now run the jupyter notebook by typing `jupyter notebook` in the terminal. This will open a browser window with the jupyter notebook interface. You can navigate to the folder where you saved this notebook and open it.

4. Alternatively, install [VSCode :octicons-link-external-24:](https://code.visualstudio.com/){:target="_blank"} and the Python extension. Then open this notebook in VSCode and run it with the kernel that belongs to the pyworkshop environment. [How to guide here :octicons-link-external-24:](https://code.visualstudio.com/docs/datascience/jupyter-notebooks){:target="_blank"}

---

### Jupyter basics

Jupyter notebooks are text files that can be rendered as formatted text **and** run code given the proper setup (see Installation).

Text is split into **cells**. Double clicking a cell allows you to edit it.

For code cells, there is also an option to run the code. You can do this by pressing **SHIFT+ENTER** while having it selected, or press the **Run** button at the top of the cell (exact location depends on the editor you're using). Because of the way we set up the notebook the code cells will be running Python code.

For this workshop, we'll be asking you to follow along by running code cells and by doing coding exercises by writing or editing code in code cell.

Run the code cell below as a demo.


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

Jupyter notebooks can be exported to pdf or html, so that other people can view both the code and its output. It's a good format for handing in homeworks, for example, since you can show your work. In this notebook, there will be exercises with placeholders for the code that you will have to fill in. For these exercises, we encourage you to work with each other, use google, LLMs, and whatever other resources if you are stuck. It's not an exam, but just a way to practice the concepts. Afterwards, we will post the completed notebook on our website so you can have examples of solutions.

## What is a computer program?

Let's start by answering this general question. A computer program (depending on the context, sometimes also called software, an app, a script, a package, or a command, among others) is a set of instructions written in a way that the computer understands such that it can perform computations based on those instructions.

Think of a computer program as a cooking recipe:

```
1 cup (2 sticks) unsalted butter, softened
3/4 cup granulated sugar
3/4 cup packed brown sugar
1 teaspoon vanilla extract
2 large eggs
2 1/4 cups all-purpose flour
1 teaspoon baking soda
1/2 teaspoon salt
2 cups semi-sweet chocolate chips

    1. Preheat your oven to 375°F (190°C).
    2. In a large mixing bowl, beat the softened butter, granulated sugar, brown sugar, and vanilla extract until creamy.
    3. Add the eggs, one at a time, beating well after each addition.
    4. In a separate bowl, combine the flour, baking soda, and salt.
    5. Gradually add the dry ingredients to the wet mixture, beating until well combined.
    6. Stir in the chocolate chips and nuts, if using.
    7. Drop rounded tablespoons of dough onto ungreased baking sheets.
    8. Bake in the preheated oven for 9 to 11 minutes or until golden brown.
    9. Remove the cookies from the oven and let them cool on the baking sheets for a couple of minutes before transferring them to a wire rack to cool completely.
```

This tells us everything we need to know to bake some simple, but delicious, chocolate chip cookies.

Or does it? If we were to give these and **only these** instructions to a robot, would it be able to bake us these cookies while we sit back and read by the fire?

I highly doubt it, because a computer needs every single step, no matter how miniscule, given to it as instructions in a program. Unlike a human, computers don't remember or learn from their previous instructions.

Here is a more programmatic recipe to bake chocolate chip cookies:

```
  1. Walk to your oven.
  2. Extend your arm towards the power button.
  3. Push the power button.
  4. Move your arm to the temperature dial.
  5. Set the temperature dial to 375°F (190°C).
  6. Lower your arm.
  7. Walk toward your cabinet.
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

This recipe is much more similar to what a computer program looks like. Every single step, even ones you might not think about when doing these tasks normally, has to be given.

But even this doesn't provide all the instructions clearly. It assumes some basic knowledge of your kitchen layout and appliances. It also gives some actions, such as **Walk** or **Extend**, that could be broken down even further to their component instructions. Indeed, if we were omnipotent we could write a recipe for chocolate chip cookies just by specifying when to activate specific neurons in ones body.

Similarly, in a computer, we could write programs by specifying when to send electrical current through each individual transistor.

Luckily, though, we don't need to do that in either case. For the recipe, humans retain their previous knowledge and skills, so we know how to walk to our oven even when its not written out specifically.

And computers had programmers before us that built programming languages at higher levels than explicitly manipulating transistors, giving us the ability to write instructions in (more-or-less) plain text.

Python is one of those languages, and even more luckily, there are built-in chunks of code written by the developers of the language that allow us to do common tasks without programming them explicitly. The chunks of code written by others to do very specific things are called **functions**.

### Walk - a pseudo-function

Let's go back to our detailed recipe. I mentioned before that certain actions, like **Walk** are invoked multiple times. To me, Walk seems like a function. We can simply say Walk in our recipe, and somewhere in our recipe book, some other recipe is looked up that looks something like this:

```
Walk:
  1. Lift right leg.
  2. Extend right leg.
  3. Lower right leg and lift left leg.
  4. Extend left leg.
  5. Lower left leg and lift right leg.
```

Every time the word Walk appears in our recipe, we know to go look-up this other recipe to figure out what to do. In computer programming, we call these other recipes **functions**.

Of course, if this were the whole function, it wouldn't be very useful. Remember, if we're writing this recipe for a robot, it needs everything spelled out for it explicitly. If we just had this as our Walk function, the robot would take two steps in the direction it is facing and then be left standing on it's left leg.

> **Exercise:** What are some other pieces of information we could provide to ensure that this Walk function is useful in the context of step 1 of our detailed recipe?

Perhaps our new Walk function would look something like this:

```
Walk:
  1. Turn body to face oven
  2. Lift right leg.
  3. Extend right leg.
  4. Lower right leg and lift left leg.
  5. Extend left leg.
  6. Lower left leg and lift right leg.
  7. Repeat 2-6 until the distance to the oven has been traversed
```

Great! But this function would seem to only work for step 1. What about step 7: Walk toward your cabinet. If we just ran this version of Walk, we would be stuck at our oven forever.

We could add two different Walk functions to our recipe book:

```
Walk_to_oven:
  1. Turn body to face oven
  2. Lift right leg.
  3. Extend right leg.
  4. Lower right leg and lift left leg.
  5. Extend left leg.
  6. Lower left leg and lift right leg.
  7. Repeat 2-6 until the distance to the oven has been traversed

Walk_to_cabinet:
  1. Turn body to face cabinet
  2. Lift right leg.
  3. Extend right leg.
  4. Lower right leg and lift left leg.
  5. Extend left leg.
  6. Lower left leg and lift right leg.
  7. Repeat 2-6 until the distance to the cabinet has been traversed
```

Or, as computer programmers like to do, we could type things out only once and make a single **generic** Walk function. To do this, we'd need to provide even more specific information to our function so we can cover more cases.

I think the two most important generic parameters would be *angle* and *distance*. Given these two things, we should be able to Walk anywhere:

```
Walk_anywhere:
  1. Turn body *angle* degrees
  2. Lift right leg.
  3. Extend right leg.
  4. Lower right leg and lift left leg.
  5. Extend left leg.
  6. Lower left leg and lift right leg.
  7. Repeat 2-6 until the *distance* has been traversed
```

I want to do another thing too. I don't like seeing all those instructions spelled out when I need to repeat them over and over again. So I'm going to write another function, called Step:

```
Step:
  1. Lift right leg.
  2. Extend right leg.
  3. Lower right leg and lift left leg.
  4. Extend left leg.
  5. Lower left leg and lift right leg.

Walk_anywhere:
  1. Turn body *angle* degrees
  2. Repeat Step until the *distance* has been traversed
```

We'll take the Step function and put it somewhere else in our recipe book, so that everytime it is called in Walk_anywhere, we can go find the Step recipe to follow those instructions. And it just generally looks a lot cleaner typed out.Hopefully we'll be able to get this robot to bake us some nice cookies soon.

But how do we integrate these functions into our original recipe?

### Function arguments and the assignment operator

Most functions require some sort of input to operate. These are given as **arguments** when you invoke, or call, the function.

Here is how we could do this for our recipe:

```
  1. Walk_anywhere 2 meters at an angle of 40°.
  2. Extend your arm towards the power button.
  3. Push the power button.
  4. Move your arm to the temperature dial.
  5. Set the temperature dial to 375°F (190°C).
  6. Lower your arm.
  7. Walk_anywhere 0.6 meters at an angle of 120°.
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

Notice that instead of just saying Walk we now refer to the other recipe, or function, in our recipe book, Walk_anywhere.

> **Exercise**: What are the **arguments** we've given the Walk_anywhere function above?

Now I want to edit the **syntax** (how we type) of our recipe, just to make it a bit more consistent with how a computer program might look:

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

This introduces our first explicit programming syntax. The item assignment operator **=**.

Using the **=** operator simply means that the **thing on the left side assumes the value of the thing on the right side**. In programming, the thing on the left side is always a **variable** (and in this case an argument to our function). Variables can be re-used later on in our program with the last value they were assigned.

In our case, we're saying that we're setting the value of the variable *distance* to be 2 meters and the value of the variable *angle* to be 40°. And when we refer to *distance* and *angle* later on, we'll actually be referring to the values of 2 meters and 40°.

Then, our function will need to be modified to accept these **arguments** as **parameters**:

```
Walk_anywhere(*distance*, *angle*):
  1. Turn body *angle* degrees
  2. Repeat Step until the *distance* has been traversed
```

Here, we've assumed that the Step function exists and is available in the robot's memory, even if we haven't explicitly typed it.

But more importantly, the values of the two variables, *distance* and *angle*, are now set when we call the function in the main program.

This means that both times we call the Walk_anywhere() function, we can specify a different *distance* and *angle*, as in steps 1 and 7 of our recipe. And the same is true when, undoubtedly, we call the Walk_anywhere function again later on in our recipe.

**Exercise:** Given the syntax of our recipe book (in other words, how we've typed things up to now), in the code block below, type how you would tell the cookie baking robot to walk from the cabinet to the counter if it is 1 meter away and directly behind it.


```python
# Your pseudocode here
Walk_anywhere(distance=1 meter and angle=180°)
```

### Pseudocode and syntax

What we've shown above a is a "program" in the sense that it lays out the instructions one step at a time. However, it does this in mostly plain English. This is called **pseudocode** and is a good way to get started when you're presented with a new problem you have to code.

The concepts conveyed about **functions** here directly translate into how functions work in computer programs. They are blocks of code (recipes) available in your recipe book (sometimes called a **library**) that are available to you even if you are on a different page in the recipe book or writing your own recipe. In other words, you can tell the robot to Walk_anywhere without you yourself having to know the exact text of the Walk_anywhere recipe.

> **Exercise**: Write out pseudocode for getting on the bus to go to the grocery store. Let's go around and have each person write one line.

While the concepts are the same, the main difference between this pseudocode and an actual program is the **syntax**, which I've mentioned before is simply how things are typed or written. Each programming language has a unique syntax that provides structure and underlying instructions to the computer.

In an even more Pythonic syntax, we would call our Walk_anywhere function as:

```
Walk_anywhere(distance=2, angle=40)
```

Notice that we don't provide units (meters or °). Those things are useful for us to know as programmers and users of the program, but the program itself is mainly just interested in the data, in this case the two numbers.

### Programming in practice

Practically speaking, when we code, we type out the instructions we wish the computer to carry out using the syntax of the language in which we are coding. In most cases, we type **one instruction per line**. The computer then reads the instructions one line at a time, from top to bottom, though the most powerful basic programming techniques can change this behavior. We'll learn about those later on.

We write our programs by typing in a text file using a **text editor**. Some text editors are designed for coding with useful features such as syntax highlighting and automatic formatting. However, even the most plain text editor (e.g. Notepad) could be used to write a computer program.

In this workshop, the text editor we're using is conveniently built-in to the Jupyter notebook as the code cells.

In Python, empty lines are ignored, as are lines that begin with the `#` character. These lines are called **comments** and are meant for notetaking and documenation.

Now that we know that a **function** is like another recipe in our recipe book of code, let's look at some actual Python functions.

## Functions in Python

There are a range of Python functions built-in to the language, as well as a multitude of external **libraries** that can be **imported** to be used, like getting another recipe book from your bookshelf or at the public library.

Let's look at a very basic function. What happens when you run the single line of code below?


```python
abs(-5)
```

The `abs()` function takes as input a single **integer** and **returns** its absolute value. In this case, the absolute value of -5 is 5. Under the hood, there is some block of code that Python has installed on your computer that is looked-up and run every time it sees that you've typed and run `abs()`. I don't know what this code looks like (though I could guess for such a simple function), and I don't even know where it is on the computer. But that's what's so great about functions: they simplify tasks that are repeated often, saving us programmers time and effort.

For instance, if we needed to know the absolute value of 10 numbers and the underlying code for `abs()` is 4 lines of code and we DIDN'T have it stored as a function, we would have to write out those 4 lines 10 times (recall the Walk_to_oven and Walk_to_cabinet problem). Now, with `abs()`, we only need to write that function call 10 times.



### Functions usually require input

What happens if you run this code block:


```python
abs()
```

You get an **error** (a very common occurrence when coding). Remember, almost all functions require additional information in the form of **arguments**. In the case of `abs()` it requires a single argument, a number. Without it, the underlying code doesn't work, so it stops the program and tells us before it even tries.

How about this:


```python
abs(-5, 7, -12)
```

Still no good. In this case, the function takes EXACTLY one number and runs some code using it. This may not always be the case, and different functions are going to require different inputs.

Ok then, how would you know how many arguments a given function takes? Or if there even exists a function to do a particular task?

### Learning more about functions

If you know the name of the function and are coding in a notebook like this, you can conveniently use another function called `help()`. The `help()` function takes as an argument the name of another function and looks up some (hopefully helpful) documentation about it and prints it to the screen.

Try this:


```python
help(abs)
```

This tells us what `abs()` does and tells us that it requires one argument, `x`. (The `/` indicates that the argument is positional, but you can ignore that for now.)

What about if you know what you want to do, but you're not sure if there is a function to do it. This begins to touch a bit on a host of 'meta-skills' that one picks up as they start to code and work with computers more. It may seem obvious, but the first solution is to simply search the internet. The difficulty comes when you try to word your search, and unfortunately that will change depending on the task.

However, there are some resources that will pop-up that are generally pretty reliable. For instance, the official [Python documentation :octicons-link-external-24:](https://docs.python.org/3/){:target="_blank"} can be helpful, but is sometimes cryptic (e.g. the / above in the `abs()` `help()` output). StackExchange and [StackOverflow :octicons-link-external-24:](https://stackoverflow.com/){:target="_blank"} are great resources that provide community answers to programming problems. But sometimes it is difficult to find an answer to your specific problem unless you post it yourself.

Now, it is also feasible to ask a LLM chatbot (e.g. ChatGPT, CoPilot) to help with coding problems. While these bots have their issues with reliability for real world information, they tend to be quite accurate for basic programming problems. For instance, you could ask, "How do I get the largest number of a list of numbers in Python?" and it would probably reply with some answer related to the `max()` function.



### Functions and data types

Like we've said, functions require input in the form of arguments. For our pseudo-function Walk_anywhere(), the arguments were two numbers that represent distance and angle. For the `abs()` function in Python, the lone argument is a number that may represent anything.

In both cases, the arguments were whole numbers, or as we call them in programming lingo, **integers**.

**Integers** are only one of several basic types of data that we may be manipulating in our program.


#### Integers

In Python, an **integer** is any number that can be formed by the ten numeric symbols on your keyboard: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9.

The hyphen symbol is also allowed to indicate negative integers: -.  

So `9` is an integer, as is `298`. And `-1054`. And `298357`. And so on. They are typed plainly, with no other characters.

#### Strings

Another basic Python data type is a **string**. Strings are made up of one or more of any alpha-numeric **character** on your keyboard. Importantly, in order for Python to know a piece of data is a string, it must be encompassed by quotation marks, either 'single' or "double".

Some examples of strings are: `"hello"`, `'the quick brown fox'`, and `"99"`.

Some things that are not strings are: `hello`, `abs()`, and `99`.

Do you see why `"hello"` is a string, but `hello` is not? It's the double quotes! Without them, Python will interpret `hello` to be some sort of object like a variable or function name. With them, `"hello"` is interpreted as a string.

#### Why do data types matter?

This distinction between types of data is important because **some functions may operate differently depending on the data type provided, and some might work for one data type and not for others**.

For example, we know what `abs(-5)` will do. What about the following? Run the code block to find out:


```python
abs("-5")
```

It is more-or-less telling us that we gave it a string when this function only works for integers.

This may seem obvious with such a simple example, but later on, when data types are obfuscated behind variable names and data structures, you may start getting errors like this.



**One of the most important concepts in programming is to always know what data type you are working with.**

### More examples of functions

Let's say we have the following string: "Teach a robot to bake cookies."

And we've entered this data into our Python script and **stored it as a variable** using the **=** operator as in the code block below.



> **Exercise**: What function could we use to count the number of individual characters in our string? What happens if we use the same function to count the number of digits in a number? Enter your answer in the code below.




```python
my_string = "Teach a robot to bake cookies."

# Your code here: Find a function to put here that counts the number of characters in my_string
len(my_string)

```


```python
my_integer = 124

# Your code here: Use the same function to count the number of digits in my_integer
len(my_integer)
```

#### print()

Another important function in Python is `print()`. This function takes any number of arguments and simply displays them on the screen. This may seem unnecesary in our Jupyter notebook, where function output is automatically displayed, but `print()` allows us to display **and format** output in other environments.

> **Exercise**: Use `print()` to display both `my_string` and `my_integer` on a single line.



```python
# Your code here: Display my_string and my_integer on a single line
print(my_string, my_integer)
```

You'll notice that this worked even though we gave it mixed data types (a string and an integer).

`print()` is an important function for displaying output to a user as well as for debugging (when in doubt, print it out).

### Storing the output of functions

The same way functions require input, they usually also produce output. We say that the function **returns** this output, because it can then be used in the main program.

Up until now, we've simply typed our function and let the notebook display the returned result to us. But of course computer programs are composed of multiple instructions and instead of displaying the result of the function to the screen, we may want to save it to be used later on in the program.

To do this, we again use our trusty item assignment operator, **=**.


```python
my_integer = -5
abs_result = abs(my_integer)
print("The absolute value of", my_integer, "is", abs_result)
```

<pre class="output-block">
The absolute value of -5 is 5
</pre>

This chunk demonstrates a few things:

1.   Instead of giving the `abs()` function our data directly, we've instead given it a variable in which we've stored our data.
2.   We used `=` to assign the result of `abs()` to another variable
3.   We used `print()` to format and display the result.

> **Exercise**: Using the function you looked up and learned about above (`len()`), write a few lines of code that store a string, look-up its length, and display both the string and the length using `print()`.


```python
# Your code here: Store a string, calculate its length, and print both
my_string = "Teach a robot to bake cookies."
my_string_length = len(my_string)
print("The message: '", my_string, "' is", my_string_length, "characters long.")
```

### Variable naming rules

We've talked a little bit about storing information as **variables** with the assignment operator `=`.


```python
my_data = 5
my_message = "hello world"
```

However, there are some rules on how we can name our variables:

1.   Variable names can start with any letter, but not a number. They can contain numbers after the first character.



```python
my_data = 5 # good!
my_data2 = 6 # also good!
2_data = 7 # no good!
```


<pre class="output-block">
  File "&lt;ipython-input-4-b35b10f55182&gt;", line 5
    2_data = 7 # no good!
     ^
SyntaxError: invalid decimal literal
</pre>

2.   **Keywords**, like `if`, `while`, `in`, cannot be used as variable names because they are used for other operations. The following shows a list of keywords that cannot be used as variable names:


```python
import keyword
print(keyword.kwlist)
```

<pre class="output-block">
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
</pre>

3.   Variables are case sensitive, so the variables `count`, `Count`, and `COUNT` are all unique and can be used simultaneously, though this would not be a best practice since it makes the code harder to read.




```python
count = 5
Count = 6
COUNT = 7
print(count, Count, COUNT)
```

<pre class="output-block">
5 6 7
</pre>

## Operators as functions

As we've been discussing, **functions** are reusable blocks of code. They take input **arguments** and **return** objects that can be stored in variables and used later.

In general, when calling a function and saving its result, it is typed as:

```
my_function_result = my_function(argument1, argument2)
```

Here, the Python interpreter sees that `my_function()` has been called with two arguments and it performs some specific task on them which is returned.

There are also functions that are represented by single symbols or keywords called **operators**. These operators, when the interpreter encounters them, perform a specific task and return a result. We're already familiar with one operator, the assignment operator **=**.

```
my_data_point = 12
```

Here, we've told the program to assign the variable name on the left hand side of the equals sign to the data on the right hand side. We can also use the assignment operator `=` to assign the value of one variable to another variable. This may be useful if you want to store an initial value to compare to later:


```python
my_data_point = 12
my_initial_data = my_data_point
print(my_initial_data)
```

So in a way, operators can be seen as syntactic shortcuts. Instead of having to type something like:

```
set_equal_to(my_variable, my_data)
```

We just need to type:

```
my_variable = my_data
```

### Arithmetic operators for integers

There are other operators that, when used with **integers**, perform basic arithmetic functions. These are, somewhat predictably:

*   `+` : Add the items on the left and right together
*   `-` : Subtract the item on the right from the one on the left
*   `*` : Multiply the items on the left and right together
*   `/` : Divide (and round) the item on the left by the item on the right

Let's take a look at some of these.


```python
x = 4
y = 2

print(x + y)
print(x - y)
print(x * y)
print(x / y)
```

<pre class="output-block">
6
2
8
2.0
</pre>

Here, we've given the `print()` function a single argument: the result of the arithmetic operation, which it then displays.

Notice that, for division, we see that it has added a decimal place. It has converted our integers into **floating point** numbers, another numeric data type in Python, to deal with numbers that are not divisible:


```python
x = 3
y = 2

print(x / y)
```

<pre class="output-block">
1.5
</pre>

A couple other arithmetic operators are:

*   `**` : called the **exponentiation** operator, this raises the number on the left side to the power on the right side
*   `%`  : called the **modulo** or **modulus** operator, this divides two numbers and returns the _remainder_ of the division
*   `//` : called the **floor division operator, this divides and then rounds down

Let's take a look at some examples.


```python
x = 3
y = 2

print(x ** y)
print(x % y)
print(x // y)
```

Remember, when performing 3 / 2 with remainders, the remainder is 1, so `%` returns 1.

And without remainders it is 1.5, so `//` also rounds down to 1.

#### Order of operations

Arithmetic in Python follows the order of operations rules. Maybe you learned this as PEMDAS or something similar: **P**arentheses, **E**xponents, **M**ultiplication/**D**ivision, **A**ddition/**S**ubtraction.


```python
print(1 + 2 * 3)
print((1 + 2) * 3)
print("---")
print(3 ** 2 - 1)
print(3 ** (2 - 1))
```

### String operators, or why its important to know your data types

The above operators are useful for arithmetic on **integers** (or **floats**). However, some operators can also be used on strings.

#### Concatenate strings with `+`

The `+`, operator in particular, can be used to **concatenate**, or combine, strings together.


```python
x = "hello"
y = "world"

print(x + y)
```

This can be very useful when formatting strings, either for processing or for output.

**Remember, certain functions expect certain data types** (strings or integers). In most cases, if the wrong data type is provided, an error will stop the program, like in our `abs()` example. However, in some cases, functions that accept both data types can produce unexpected results without informing you at all!


```python
important_data_point1 = "9"
important_data_point2 = "8"

sum_of_important_data = important_data_point1 + important_data_point2

print("I'm now showing my professor my important results:", sum_of_important_data)
```

Here, no error is thrown telling you you are concatenating two strings rather than adding together two integers. That's because both things are vaild to do with Python syntax: Python has no way of knowing that you wanted to add these numbers rather than concatenate them - that's up to you to tell it! Remember, every little step of a computer program has to be given, otherwise you will get errors (relatively easy to debug) or **logic errors**, which occur when the program runs, but gives unexpected results, and are generally harder to debug.

> **Exercise**: Correct the code so that it accurately prints the sum of the two data points.


```python
# Edit and correct the code here
important_data_point1 = 9
important_data_point2 = 8

sum_of_important_data = important_data_point1 + important_data_point2

print("I'm now showing my professor my important results:", sum_of_important_data)
```

Luckily, if we ever try to `+` a string and an integer together, it stops us with an error:


```python
x = "9" + 8
```

#### Repeat strings with `*`

The other operator that can be used with strings is `*`. This works slightly differently in that it needs a string on the left side and an integer on the right:

```
my_string * n
```

Basically, this means "repeat my_string n times". Here's an example:


```python
my_string = "ha"
repeat_num = 4

print(my_string * repeat_num)
```

## Booleans and logical operators

So far, we've covered two basic data types: **integers** and **strings** (and we've also touched on **floats**) and described on how you need to be careful when giving data to functions.

However, there is another data type inherent to any programming language: the **boolean**. Booleans allow us to construct logical statements or expressions, which are the foundation for any programming task. Logical statements allow us to control the flow of our program, executing some instructions based on the current conditions in the program.

Booleans can take only two values: True or False.

In a way, booleans represent the most basic input that all computers are built on: is this transistor on (True) or off (False).

In Python, booleans are typed as `True` or `False`. Notice the capitalization -- there are no such data types as `true` or `false`.


```python
print(True)
print("--- print True check ---")
print(true)
print("--- print true check ---")
```

Here, the boolean `True` is displayed along with the message telling us it has been displayed. However, since the keyword `true` doesn't exist in Python, the error is telling us that it thinks `true` should be a variable that the programmer has put in the program, but it can't find where it is defined.

There are other ways to represent Booleans in Python as well. For instance the **integers** `1` and `0` represent `True` and `False`, respectively.

In fact, any integer _other than 0_ will return `True` if evaluated as a boolean with the `bool()` function. Likewise, any **string** other than an empty string (represented as quotes with no characters contained in them: `""` or `''`) will return `True` while the empty string will return `False`. Here, let's use the `bool()` function, which takes one argument and returns either `True` or `False`, to confirm.


```python
print("bool() of a boolean:")
print(bool(True))
print("---")

print("bool() of integers:")
print(bool(1))
print(bool(0))
print(bool(587348))
print(bool(-1))
print("---")

print("bool() of strings")
print(bool("Hello"))
print(bool(""))
print(bool(''))
print(bool("0"))
```

<pre class="output-block">
bool() of a boolean:
True
---
bool() of integers:
True
False
True
True
---
bool() of strings
True
False
False
True
</pre>

> **Exercise**: What would the following code display to the screen:

```
print(bool("False"))
```



### Logical operators: **and** and **or**

Sometimes, we want to test whether a combination of boolean values together evaluate to `True` or `False` in different ways. This allows us to make complex logical conclusions based on the state of variables in our program.

We do this with the logical operators **and** and **or**.

In both cases, the objects on the left and right of the operator are evaluated as booleans. For **and**, both objects must return `True` in order for the entire expression to be True:


```python
print(True and True)
print(True and False)
print(False and False)
```

For **or**, only one of the two booleans must be `True` for the whole expression to be True:


```python
print(True or True)
print(True or False)
print(False or False)
```

Any easy way to see how `and` and `or` work is with truth tables. In a truth table, we fill out all possible values for the variables in the expression and then evaluate each component of the expression. Here, the first two columns are for the variables being compared, A and B, and each row is a combination of values for those variables. The last columns show the result of the logical expression given those values of A and B.

A | B | A and B | A or B
---- | ---- | ------- | ------
T | T | T       | T
T | F | F       | T
F | T | F       | T
F | F | F       | F

Remember, almost every object in a program can be evaluated as a Boolean.

> **Exercise**: Write the following logical expressions:
> 1. One that uses two integers and an `and` operator and returns `True`.
> 2. One that uses two integers and an `or` operator and returns `False`.
> 3. One that uses an integer and a string with an `and` operator and returns
`True`.
> 4. One that uses an integer and a string with an `and` operator and returns `False`.
>
> Use the `bool()` function to interpret the strings and integers as Booleans.


```python
# Your code here: Two integers with and that returns True
print(1 and bool(573657))

# Your code here: Two integers with or that returns False
print(bool(0) or bool(0))

# Your code here: Integer and string with and that returns True
print(bool(235) and bool("hello"))

# Your code here: Integer and string with and that returns True
print(bool(0) and bool(""))
```

#### Complex logical statements and order of operations

Using `and` and `or`, we can evaluate multiple boolean values.


```python
print(True or True and False)
```

This statement returns `True`. Logical statements have their own order of operations, with **`and` taking precedence over `or`**. Given that, let's break the statement down.

1. We read the `and` comparison first. `True and False` evaluates to `False` - both sides of an `and` need to be True.
2. Given that, the expression reduces to `True or False`, which evaluates to `True` since only one side of an `or` statement needs to be True. This means the entire expression results in `True`.

The order of operations can be made more explicit with parentheses.


```python
print(True or (True and False))
```

This is the exact same logical expression as the one above, but we've added the parentheses to make things a little bit easier for us to parse. In logical expressions, **parentheses also affect the order of operations** as they do in mathematical expressions: they take precedence over anything else. In that way, we can change the result of this expression by moving the parentheses.


```python
print((True or True) and False)
```

Here, the parentheses tell Python to evaluate whatever is inside them first. Now the statement breaks down as:

1. We read the expression in the parentheses first. `True or True` evaluates to `True` since only one side of an `or` needs to be True for the entire expression to be True (here both sides are True, which doesn't matter for `or`).
2. Given that, the expression reduces to `True and False`. For `and` both sides need to be `True` for the expression to be True, and that isn't the case here, so the expression is `False`.

Let's summarize the **order of operations** for logical expressions:

1. Evaluate parentheses
2. Evaluate `and`
3. Evaluate `or`
4. If there are multiple similar statements in a row without parentheses, for example `True or True or True`, simply read them left to right.





Let's practice reading some more complex logical expressions.

> **Exercise**: In the code block below, first type what you think the result of each logical expression will be as a comment (just add `#` to the beginning of the line). Then, print them out to see if you were correct.
> 1.   False or False and True
> 2.   (False or False) and True
> 3.   True and True or False and False
> 4.   True and (True or False) and False
> 5.   False or False or False or False or True or False


```python
# 1. Your answer here:
# 1. Your code here
print(False or False and True)

# 2. Your answer here:
# 2. Your code here
print((False or False) and True)

# 3. Your answer here:
# 3. Your code here
print(True and True or False and False)

# 4. Your answer here:
# 4. Your code here for
print(True and (True or False) and False)

# 5. Your answer here:
# 5. Your code here for
print(False or False or False or False or True or False)
```

<pre class="output-block">
False
False
True
False
True
</pre>

### Negation operator: `not`

The result of any logical expression can be inverted with the **`not`** operator.


```python
print(not True)
print(not False)
print(not False or False or False or False or True or False)
```

Note that `not` works on individual parts of a logical expression, not the entire thing. So, `False or True` returns `True` and `not False or True` also returns `True`. This is because the `not` is only negating the first `False`, essentially making the statement `True or True`. To negate chunks of an expression, use parentheses. `not (False or True)` will indeed return `False`, since the expression itself is `True` and we are negating the whole thing.


```python
print(False or True)
print(not False or True)
print(not (False or True))
```

> **Exercise:** Fill out the following truth table. We will go from left to right. Double click on the table to edit.

A | B | A and B | not B | A and not B | A and B or A and not B | A and (B or A) and not B |
--- | --- | ------- | ----- | ----------- | ---------------------- | ------------- |
T | T |    T    |   F   |      F      |           T            |        F
T | F |    F    |   T   |      T      |           T            |        T
F | T |    F    |   F   |      F      |           F            |        F
F | F |    F    |   T   |      F      |           F            |        F

What do you notice about the second to last column of the truth table representing the full expression?

### Comparison operators for integers

One can also compare two objects in Python and return a boolean value, either `True` or `False`. Doing this can help the program make decisions about the next instructions to execute, based on how it has been programmed.

In order to compare two numbers and return either a `True` or `False` boolean value, there are several operators one can use depending on the situation. These will all seem relatively familiar based on how they are used in arithmetic.

*   `>` : Greater than. Returns `True` if the number on the left is larger than the number on the right. Returns `False` otherwise.
*   `>=` : Greater than or equal to. Returns `True` if the number on the left is larger or the same as the number on the right. Returns `False` otherwise.
*   `<` : Less than. Returns `True` if the number on the left is smaller than the number on the right. Returns `False` otherwise.
*   `<=` : Less than or equal to. Returns `True` if the number on the left is smaller or the same as the number on the right. Returns `False` otherwise.
*   `==` : Is equal to. Returns `True` if the numbers on the left and the right are the same. Returns `False` otherwise.
*   `!=` : Is not equal to. Returns `True` if the numbers on the left and right are different. Returns `False` otherwise (i.e. if they are the same).

Here are some examples.


```python
print(8 > 9)
print(9 > 9)
print(9 >= 9)
print(8 != 9)

```

### `=` vs. `==`

Recall that a single equals sign, `=`, is our **assignment operator** that assigns the value of the variable to the left of it the value to the right of it. Here we've learned that the double equals sign, `==`, is the **equality operator** that compares the values on the right and left and returns either `True` if the values are the same or `False` otherwise.

**A common point of confusion is the difference between `=` and `==`, and when to use either one**.

Remember:

*   Use `=` if you are assigning a value to a variable
*   Use `==` if you are comparing two values



```python
my_int = 5

print(my_int == 5)
print(my_int == 4)

print("---")

my_int = 4
print(my_int == 5)
print(my_int == 4)

print(my_int)
```



> **Exercise**: In the code block below, do the following:
> 1.   Assign any integer value to a variable called my_int1
> 2.   Assign any other integer value to a variable called my_int2
> 3.   Use a comparison to print out whether the two numbers are equal.


```python
# Your code here: Assign any two integers to variables my_int1 and my_int2
my_int1 = 5
my_int2 = 5

# Your code here: Print out whether the integers stored in your variables are equal to each other
print(my_int1 == my_int2)

```

### Comparison operators and strings

All of the above comparison operators also work for strings, but with the exception of `==` and `!=`, we won't be learning about them. These two, however, work as follows for strings:

*   `==` : Returns `True` if the strings are identical. Returns `False` otherwise.
*   `!=` : Returns `True` if the two strings are different. Returns `False` otherwise.

For example:


```python
print("Hello" == "Hello")
print("robot" == "cookies")
print("robot" != "cookies")
```

Importantly, case matters for these comparisons:


```python
print("Hello" == "hello")
```

Like we said above, the other operators (e.g. `>`, `<=`, etc.) do indeed work on strings, but that use-case is not common for most programmers.

### The inclusion operator for strings: `in`

The final operator we'll be learning about is the **inclusion**, or **membership**, operator for strings, `in`. It works as follows:

*   `in` : The inclusion operator for strings. Returns `True` if the string on the left is contained within (is a sub-string of) the string on the right. Returns `False` otherwise.



```python
print("lo" in "hello")
print("cookies" in "robot")
```

Checking for exact sub-strings with `in` is the most basic of pattern matching, which is extremely useful in programming.

## Review

So far, we've learned a few main things:

1. Functions are little sub-recipes of code that perform specific tasks given the appropriate input. They are usually typed as `function_name(input1, input2, ...)`.
2. Operators (e.g. `+`, `and`) can be thought of as special functions that instead take input based on what is place on either side of them.
3. Different data types exist in programming, notably **integers** and **strings** in Python. **Functions and operators may only work for a given data type**.
4. Complex logical statements can be constructed with **boolean** values (`True`, `False`) and the associated operators (e.g. `>`, `not`, `in`). Again, some of these operators only work for specific data types.

These concepts form the basis of programming in any language (though the syntax will vary), however one cannot make more than very simple programs using these types of instructions alone.

In order to write complex programs that take these basic concepts and allow them to be executed based on the **conditions** of the data within a program, and to automate the **repetition** of certain instructions, we need to learn the syntax that allows us to control the flow of the program.

### Operators table

Here is a table summarizing how the various operators we've learned about can be used on different data types:

Operator | Strings | Integers/floats | Boolean |
-------- | ------- | --------------- | ------- |
`=`      | Assigns a string to a variable name | Assigns a number to a variable name | Assigns a boolean to a variable name |
`+`      | Concatenate (combine) strings | Add two numbers | *NA* |
`-`      | *NA* | Subtract two numbers | *NA* |
`*`      | Repeat a string N times, where N is an integer | Multiply two numbers | *NA* |
`/`      | *NA* | Divide two numbers, returning a decimal | *NA* |
`**`     | *NA* | Exponentiation (raise to the power of) | *NA* |
`//`     | *NA* | Divide two numbers, rounding down to return an integer | *NA* |
`%`      | *NA* | Divide two numbers, returning the remainder as an integer | *NA* |
`in`     | Checks if one string is contained in another, returning a boolean | *NA* | *NA* |
`and`    | *NA* | *NA* | Returns `True` if both conditions are `True`, otherwise `False` |
`or`     | *NA* | *NA* | Returns `True` if at least one condition is `True`, otherwise `False` |
`not`    | *NA* | *NA* | Negates a boolean (e.g. returns `True` if `False` is input and vice versa) |
`==`     | Compares 2 strings and returns `True` if they are identical, `False` otherwise | Compares two numbers and returns `True` if they are identical, `False` otherwise | Compares two booleans and returns `True` if they are identical, `False` otherwise |
`!=` | Returns `True` if two strings are **not** identical, `False` otherwise | Returns `True` if two numbers are **not** identical, `False` otherwise | Returns `True` if two booleans are **not** identical, `False` otherwise |

## Control Flow

### Conditional statements

Let's recall the recipe to get a robot to bake us some chocolate chip cookies. We left our recipe in this state:

```
  1. Walk_anywhere(distance=2 and angle=40).
  2. Extend your arm towards the power button.
  3. Push the power button.
  4. Move your arm to the temperature dial.
  5. Set the temperature dial to 375°F (190°C).
  6. Lower your arm.
  7. Walk_anywhere(distance=0.6 and angle=120).
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

We also had these other recipes in our recipe book that the robot could look up everytime it saw them in our main recipe:

```
Step:
  1. Lift right leg.
  2. Extend right leg.
  3. Lower right leg and lift left leg.
  4. Extend left leg.
  5. Lower left leg and lift right leg.

Walk_anywhere(*distance*, *angle*):
  1. Turn body *angle* degrees
  2. Repeat Step until the *distance* has been traversed
```

We now know that these sub-recipes are called **functions**.

In our main recipe, we've called `Walk_anywhere()` twice, first to get the robot to the oven, then to get to the cabinet.

But, what if before it starts baking the cookies, the robot is already standing at the oven? While we could call `Walk_anywhere(distance=0, angle=0)`, it would be kind of pointless, and it may waste valuable time - those few seconds it takes us to lookup the `Walk_anywhere()` recipe only to have to immediately flip back to the main recipe are going to delay us from our cookies.

This is a perfect situation to check the **conditions** of our program, and only execute the `Walk_anywhere()` function if certain conditions are True (or not True, depending on the context).

In order to do this, we need one more piece of information in our recipe: our current location. Then our recipe may look like this:

```
  The current location is in front of the oven.

  1. If we aren't at our oven, Walk_anywhere(distance=2 and angle=40).
  2. Extend your arm towards the power button.
  3. Push the power button.
  .
  .
  .
  and so on.
```

Now, we've given the robot's location and we've said in step 1, only execute `Walk_anywhere()` **if** is isn't already at our oven. Now our robot knows not to bother looking up and running `Walk_anywhere()` in this case. We could change the location accordingly in the recipe and the robot would know whether or not it needed to `Walk_anywhere()`. For instance:

```
  The current location is in the living room.

  1. If we aren't at our oven, Walk_anywhere(distance=2 and angle=40).
  2. Extend your arm towards the power button.
  3. Push the power button.
  .
  .
  .
  and so on.
```

We can make our pseudocode look a little bit more programmatic by doing the following:
1. Make the current location a string variable using the `=` asignment operator.
2. In the conditional **if statement**, use a logical comparison between strings.

```
  current_location = "living room"

  1. If current_location != "oven", Walk_anywhere(distance=2 and angle=40).
  2. Extend your arm towards the power button.
  3. Push the power button.
  .
  .
  .
  and so on.
```

We of course would also have to update the `distance` and `angle` arguments in our function call to be dependent on the `current_location`, but we can ignore that for now.

> **Exercise**: Imagine you are programming a robot to navigate a maze. You know that this maze can be navigated by following the "right hand rule", which is to always keep your right hand on the wall. The robot can move or look in four directions: up, down, left, and right. How would you give the robot instructions to navigate the maze? Write pseudocode for this robot navigating the maze.


```
Look to the right:
    If there is a wall:
        Try to Move Forward
        If you can't move forward:
            Turn Left
    Else:
        Turn right
        Move Forward
```

#### `if` statements and code blocks

What we described above are called **conditional statements**. In Python (and many other programming languages), these are denoted by the keyword `if`. Following `if` is a logical expression, and if that expression returns `True`, the code *within* the if statement will be executed. If it is not `True`, the code will be skipped and the subsequent lines of code will executed. Together, the `if` keyword and the logical expression are called an **if statement**.

We mention code *within* an if statement. What does that mean? When programming, separate parts of code are broken up into chunks, or **blocks** of code. Different languages handle the denotion of blocks of code in different ways. **For Python, blocks of code are indicated by indented text**, either using tabs or spaces (though you must be consistent throughout your code).

For example:


```python
x = 5

if x < 10:
  print("The number is smaller than 10")
  # code to execute if condition is true
  # this part is indented

print("Done.")
```

Here, we have set the value of `x` to be 5, then used the keyword `if` along with a logical expression (`x < 10`). Since the logical expression evaluates to `True`, the indented code block is executed.

Code blocks can be more than one line. After an **if statement** that returns `True`, every subsequent line that is indented one more level than the **if statement** itself will be executed.


```python
x = 5

if x < 10:
  print("Your number is", x)
  print("The number is smaller than 10")

print("Done.")
```

This indentation syntax is required by Python, as that is how it knows which instructions to execute after an if statement. If the indentation is incorrect, you will see an error, such as the following:


```python
x = 5

if x < 10:
print("Your number is", x)
print("The number is smaller than 10")

print("Done.")
```


```python
x = 5

if x < 10:
  print("Your number is", x)
    print("The number is smaller than 10")

print("Done.")
```

In addition to syntax errors, which Python will catch, mis-placed indentation can also lead to **logic errors**, where the code will run, but with unexpected results.

Here, we will change the value of `x` so that the if statement is no longer `True`, but we will make a mistake with our indentation.


```python
x = 12

if x < 10:
  print("Your number is", x)
print("The number is smaller than 10")

print("Done.")
```

In this case, the program is telling us that our number is smaller than 10, even though it is clearly not. This is because the second `print()` statement is not indented to be included in the if statement, rather it is part of the outer code block that will be executed regardless of the result of the if statement.

Remember, the computer doesn't know what you intend with your program. It will run according to its rules, so you have to be explicit with your instructions, in this case with indentation.

Also note the colon character, `:`, after the `if` keyword and logical expression. This is also syntactically required by Python after any if statement. Without it, you will see an error:


```python
x = 5

if x < 10
  print("Your number is", x)
  print("The number is smaller than 10")

print("Done.")
```

> **Exercise**: Pick a message and store it as a string. Print the message only if the string has at least 10 characters. This will require you to use the built-in `len()` function that we learned about before.


```python
# Your code here
my_msg = "the quick brown fox jumped over the lazy dog"
my_msg_length = len(my_msg)

if my_msg_length > 10:
  print("'", my_msg, "' has", my_msg_length, "characters.")
  print("This is more than 10 characters.")

print("Done.")
```

#### `elif` and `else`

**if statements** are extremely powerful. They essentially let us change the instructions in our program given various inputs to it.

However, two other keywords, **`elif`** and **`else`**, give us even more control over the flow of our program.

Let's talk about `else` first. `else` essentially provides an alternative block of code to be run if an `if` statement is `False`. `else` does not require a logical expression of its own, rather it uses the same one in the preceding `if` statement.

*   `else` : Used after an `if` statement. The block of code within `else` will be executed only if the condition in the if statement is `False`.





```python
x = 12

print("Your number is", x)

if x < 10:
  print("The number is smaller than 10")
else:
  print("The number is equal to or larger than 10")

print("Done.")
```

So here, the value of `x` is set to 12. Then we evaluate the expression `x < 10`. This returns `False`, so the code within the if statement is skipped. However, since the **next unindented line of code** after the if statment is `else:` (again note the required colon `:`), we instead execute the code within the **else statement**, again denoted by indentation.

**`else` must always follow a block of code from an `if` statement!**. `else` will not work if it is before the `if`, because Python reads the file from top-to-bottom:


```python
x = 12

print("Your number is", x)

else:
  print("The number is equal to or larger than 10")
if x < 10:
  print("The number is smaller than 10")


print("Done.")
```

`else` will also not work on its own, because it has no logical expression to evaluate:


```python
x = 12

print("Your number is", x)

else:
  print("The number is equal to or larger than 10")

print("Done.")
```



> **Exercise**: Debug the following code so the code block runs without error.




```python
## Debug this code
x = 12

print("Your number is", x)

if x < 10:
  print("The number is smaller than 10")
print("You will have to find a larger number.")
else:
  print("The number is equal to or larger than 10")

print("Done.")
```

`elif` is also used in conjunction with `if`, but unlike `else`, elif allows us to test another condition. Like `if`, the keyword `elif` is typed followed by the logical statement to evaluate. If *that* statement evaluates to `True`, the code within the `elif` statement is executed. It is important to know that **`elif`'s logical expression will only be evaluated if the `if` statement was `False`**. This structure essentially allows us to test alternate conditions in sequence.


```python
x = 12

print("Your number is", x)

if x < 10:
  print("The number is smaller than 10")
elif x < 20:
  print("The number is larger than 10 but smaller than 20")
else:
  print("The number is equal to or larger than 20")

print("Done.")
```

In this case, with `x` being 12, the logical statement in the if statement is tested first. Since `x < 10` is `False`, now the logical statement in the `elif` statement is evaluated, skipping the code within the if statement (indented under it). Since `x < 20` is `True` in this case, the code enters the `elif` block and executes the instructions to print a message. Then, since **none of the above conditions were `False`, the `else` statement is ignored**.

Again, note the colon `:` character which is required after any conditional statement.

You can use any number of `elif` statements in a row (as long as they follow an initial `if` statement).


```python
x = 16

print("Your number is", x)

if x < 10:
  print("The number is smaller than 10")
elif x < 15:
  print("The number is larger than 10 but smaller than 15")
elif x < 20:
  print("The number is larger than 15 but smaller than 20")
else:
  print("The number is equal to or larger than 20")

print("Done.")
```

#### More complex conditional statements

And remember, logical statements can be more complex using the `and` and `or` operators.


```python
temperature = 72
weather = "rainy"

print("The temperature is", temperature, "degrees Fahrenheit and the weather is", weather + ".")

if temperature <= 32 and weather == "snowy":
  print("Wear a heavy coat and snow boots.")
elif temperature > 32 and weather == "rainy":
  print("Wear a raincoat and boots.")
else:
  print("Your guess is as good as mine!")
```

Here, our very basic weather bot checks a couple of conditions based on the temperature and precipiation and gives clothing recommendations. Obviously, there are many more combinations of temperature and weather we could test.

> **Exercise**: Add another `elif` statement that checks any other combination of conditions and gives a recommendation.


```python
temperature = 72
weather = "rainy"

print("The temperature is", temperature, "degrees Fahrenheit and the weather is", weather + ".")

if temperature <= 32 and weather == "snowy":
  print("Wear a heavy coat and snow boots.")
elif temperature > 32 and weather == "rainy":
  print("Wear a raincoat and boots.")

# Add your elif here
elif temperature > 60 and weather == "sunny":
  print("Wear shorts and a t-shirt.")


else:
  print("Your guess is as good as mine!")
```

> **Exercise**: initialize two integer variables called `x` and `y`, give them whatever values you like. Write a series of conditional statements that check the following:
> 1. `x` and `y` are both even
> 2. one is even and the other isn't
> 3. `x` and `y` are both odd
>
> *Hint: If a number is even and you divide it by 2, what will the remainder be? Which operator returns the remainder of a division?*


```python
# Your code here

x = 5
y = 8

if x % 2 == 0 and y % 2 == 0:
    print("x and y are both even")
elif (x % 2 == 0 and y % 2 != 0) or (x % 2 != 0 and y % 2 == 0):
    print("one is even, one is odd")
elif x % 2 != 0 and y % 2 != 0:
    print("x and y are both odd")
```

---

Recall also the `in` operator for strings. You can use it to check if one string is contained within the other. It will return `True` if it is and `False` if it isn't:


```python
my_string = "1234"
print("2" in my_string)
```

Since this returns a boolean value (`True` or `False`), it can also be used when checking conditions with `if` or `elif`:


```python
my_string = "1234"

if "2" in my_string:
  print("In the if statement.")
else:
  print("In the else statement.")

print("Done.")
```

Likewise, the `not` operator can be used to negate a logical condition in `if` statements:


```python
my_string = "1234"

if not "2" in my_string:
  print("In the if statement.")
else:
  print("In the else statement.")

print("Done.")
```

> **Exercise:** Store a string (`my_string`) and store two other smaller strings (`my_substr1`, `my_substr2`). Then use a series of `if` and `elif` statements to:

*   Print a message indicating if both sub-strings are contained within `my_string`
*   Otherwise, print a message if only one of the sub-strings is contained within `my_string`. The message should indicate which sub-string was found, so you will need two `elif`s.
*   Finally, use an `else` statement to print a different string if neither sub-string is contained within `my_string`


```python
# Your code here: Pick your string and sub-strings
my_string = "everything changed when the fire nation attacked"
my_substr1 = "fire nation"
my_substr2 = "water tribe"

# Your code here: Fill in the conditional statements
if my_substr1 in my_string and my_substr2 in my_string: # An if statement if both sub-strings are found
  print("Both substrings found:", my_substr1, ",", my_substr2)
elif my_substr1 in my_string and not my_substr2 in my_string: # An elif statement if only sub-string 1 is found
  print("Substring 1 found:", my_substr1)
elif not my_substr1 in my_string and my_substr2 in my_string: # An elif statement if only sub-string 2 is found
  print("Substring 2 found:", my_substr2)
else: # Else handles if neither sub-strings are found
  print("Neither substring found.")

print("Done.")
```

#### Nested conditional statements

Stringing `if`, `elif`, and `else` statements together is a great way to execute code under different conditions, especially if the conditions are independent of one another. However, if the evaluation of conditions depends on previous conditions, you would need to use a **nested conditional** statement.

Here is a simple example of an un-nested `if` statement that programs typical car driving behavior.

Nesting is useful when the outcome of one condition directly influences whether another condition should be checked. These can be thought of as a decision tree.


```python
light = "green"
pedestrian = False

if light == "green" and not pedestrian:
    print("Go")
else:
    print("Stop")
```

Here, the `if` statement evaluates both whether the light is green and whether a pedestrian is present. If either of those evaluated to `False`, the `if` statement wouldn't be executed and the `else` statement would. Here since `light == "green"` is `True` and `not pedestrian` (which in this case is the same as saying `not False`) is also `True`, so "Go" is printed out.

However, we can write this code another, equivalent way with nesting.


```python
light = "green"
pedestrian = False

if light == "green":
    if pedestrian == False:
        print("Go")
    else:
        print("Stop")
elif light == "red":
    print("Stop")
```

This code has the same behavior as above. However, instead of a two part logical expression with `and`, we've broken that up into two separate `if`statements.

First, `light == "green"` is evaluated. Since that is `True`, we execute the code within the `if` statement. In this case, that code is another `if` statement, and since `pedestrian == False` evaluates to `True`, "Go" is printed to the screen. If either were `False`, "Stop" would be printed.

**In this way, you could think of nested if statements as implicit `and`s**.

The question then is when is it best to use nested statements? In the above example, the non-nested solution is the one I would use because it requires fewer lines of code and is generally easier to understand for someone used to looking at logical statements.

Nested if statements are best when the conditions are dependent on one another.

Let's return to our terrible weatherbot. We can add a nested if statement to make it a little better.


```python
temperature = 72
weather = "rainy"

print("The temperature is", temperature, "degrees Fahrenheit and the weather is", weather + ".")

if temperature <= 32:
  if weather == "snowy":
    print("Wear a heavy coat and snow boots.")
  else:
    print("Wear a heavy coat and warm shoes.")
elif temperature > 32 and weather == "rainy":
  print("Wear a raincoat and boots.")
elif temperature > 60 and weather == "sunny":
  print("Wear shorts and a t-shirt.")
else:
  print("Your guess is as good as mine!")
```

Now, the bot first checks if the temperature is below 32, and then checks whether it is precipitating or not before it gives a recommendation. This allows us to build a better decision tree and makes the bot a little more flexible.

> **Exercise**: Improve the weatherbot further. Consider temperature ranges from below 32, 33-60, and 60-90 as well as weather conditions "sunny", "cloudy", and "precipitating". Make recommendations for each combination.
>
> **BONUS**: Add another variable, `windy`, which will be a boolean. For each temperature category, if it is rainy (precipitating when above freezing), also check if it is windy or not and recommend an umbrella accordingly (yes if not windy, no if windy).


```python
# Your code here
# Edit weatherbot to give more specific recommendations
# Consider temperatures below 32, 33-60, and 60-90
# Consider conditions "sunny", "cloudy", "precipitating"
# Make weatherbot give recommendations for each temperature-weather combination
# BONUS: Add a windy variable that is a boolean and give recommendations about
#        whether or not to bring an umbrella when its raining (no if windy, yes if not)

temperature = 72
weather = "precipitating" # Possible conditions: "sunny", "cloudy", or "precipitating"
windy = True

print("The temperature is", temperature, "degrees Fahrenheit and the weather is", weather + ".")

if temperature <= 32:
  if weather == "precipitating":
    print("Wear a heavy coat and snow boots.")
  else:
    print("Wear a heavy coat and warm shoes.")
elif temperature > 32 and temperature <= 60:
  if weather == "precipitating":
    print("Wear a raincoat and boots.")
    if windy:
      print("Leave your umbrella at home.")
    else:
      print("And take an umbrella.")
  if weather == "cloudy":
    print("Wear a heavy jacket and warm shoes.")
  else:
    print("Wear a light jacket and light shoes.")
elif temperature > 60 and temperature <= 80:
  if weather == "precipitating":
    print("Wear a light raincoat and rain shoes.")
    if windy:
      print("Leave your umbrella at home.")
    else:
      print("And take an umbrella.")
  elif weather == "cloudy":
    print("Wear a light jacket and light shoes.")
  else:
    print("Wear shorts and a t-shirt.")
else:
  print("Your guess is as good as mine!")
```

#### Review of conditionals

By default, computer programs are read line-by-line from top to bottom by the computer with each instruction occuring one after the other. Here, with conditional statements, we've learned that we can tell the computer to only read some lines depending on the conditions of the program.

We should know:

1.   How `if`, `elif`, and `else` work to check logical statements and execute code accordingly. We know that `if` always comes first and doesn't necessarily need to be followed by any `elif` or `else` statements -- that depends on the problem you are trying to code around and is up to you to determine.
2.   The proper syntax of these statements, which includes `<keyword> <logical expressions>:` where keyword is one of the three conditionals mentioned in point 1. Remember the colon `:`!
3.   That conditional statements are followed by **blocks of code indicated by indentation**. Indentation is how Python knows what to execute given a conditional.
4. Nested conditional statements are useful for dependent logical expressions and building decision trees.

### Loops

Another important way to control the flow of a program is with **loops**. Loops allow us to automatically repeat certain blocks of code while changing some of the variables through each **iteration** of the loop. This *automatic repetition* is one of the main benefits of having computers complete tasks for us.

We've already introduced loops without calling them out with our robot cookie recipe. Indeed, loops are so integral to computing it would be hard to come up with an example that doesn't introduce them.

Recall our `Walk_anywhere()` function:

```
Walk_anywhere(*distance*, *angle*):
  1. Turn body *angle* degrees
  2. Repeat Step until the *distance* has been traversed
```

The word "Repeat" here is an implicit loop!

Much like the conditional keywords (`if`/`else`), almost universally across programming languages there are two types of loops: `while` and `for` loops.

Our `Walk_anywhere()` function seems like a perfect example to introduce the first of the two types of loops: the `while` loop.

#### `while` loops

`while` loops work by first checking a logical statement. If the statement evaluates to `True`, the code inside of the `while` loop is executed. In this way, `while` loops are very similar to `if` statements. However, unlike `if` statements, the code within the `while` loop is **repeated until the logical statement is no longer `True`**.

Here is a simple example:


```python
x = 0

while x < 5:
  print(x)
  x = x + 1

print("Done.")
```

Let's break this down. First, we have an integer called `x` and initially set to be 0. Then the program encounters the `while` line followed by a logical statement, `x < 5`. Since `x` is 0, this evaluates to `True` and the code inside of the `while` loop is executed.

Here is where things start to differ. First, we simply print the value of `x`, which is useful for demonstrating how the loop works.

Then, we change the value of `x` by saying `x = x + 1`. This is a key technique in programming, especially for `while` loops. This update statement takes the previous value of `x` and adds 1 to it with the addition `+` operator. Then it assigns this value to be the new value of `x`. After this is done, since we're in a `while` loop, Python knows to go back up to the line with `while` and re-evaluate the logical statement. If it is still `True`, the code within the loop is executed again.

A few key points related to logic and syntax:
1.   Just like an `if` statement, the colon is required after the logical statement of a `while` line.
2.   Also like conditionals, indentation is required syntactically and to ensure the code runs according to the programmer's goal. Everything under the `while` line that is indented is included in the **block** of code that will be run in the `while` loop.
3.   Notice that the last iteration prints out 4. This is because of our logical statement, `x < 5`.

> **Exercise**: Change the above loop to also print out the value of `x` when it is 5.






```python
# Edit code here so the loop prints out 5 as well

x = 0

while x <= 5:
  print(x)
  x = x + 1

print("Done.")

## OR ##

x = 0

while x < 5:
  print(x)
  x = x + 1

print(x)
print("Done.")
```

This can actually be done two ways in this case. We could change the logical statement itself, or we could simply print `x` after the loop. The second solution works because during the iteration when `x` is 4, the line `x = x + 1` is still executed, thus updating the value of `x` even though the loop will not be run for another iteration.

##### Update operators

Updating a variable, e.g. `x = x + 1` is such a common occurrence in programming that many languages have implemented special **operators** to do this automatically and with less typing (programmers are efficient/lazy). Remember, an **operator** is just a special symbol or word that performs a specific task, like another recipe in our recipe book.

We know that with the addition `+` operator, we can add two integers together, and we've just seen how this can be used in the `while` loop.

The **in-place addition operator** or **addition update operator** looks like this in Python:

```
x += 1
```

When talking about this operator, we may say **plus-equals**. However, this is exactly equivalent to typing `x = x + 1`.

> **Exercise**: Use the in-place addition operator `+=` in the loop that counts from 0 to 5.


```python
## Edit the loop to use the in-place addition operator

x = 0

while x < 5:
  print(x)
  x += 1

print("Done.")
```

Each arithmetic operator has a corresponding in-place update operator:

* `+=` : Addition
* `-=` : Subtraction
* `*=` : Multiplication
* `/=` : Division (floating-point)
* `//=` : Floor Division
* `%=` : Modulus
* `**=` : Exponentiation


##### Infinite loops

Be wary of infinite loops. Since `while` loops run as long as a logical statement is `True`, if your code is written such that the statement is never updated to conditions where it is `False`, the loop will run forever. This is called an **infinite loop**.

Here is a common way this can occur. I've commented this code block out so it doesn't get run unintentionally. If you'd like to run it, uncomment the code by deleting the `#` symbols at the beginning of each line. But running it may crash your notebook.

```python
x = 0

while x <= 5:
  print(x)
x = x + 1

print("Done.")
```

> **Exercise**: Why does this result in an infinite loop? Take a moment to discuss.

##### `while` exercises

> **Exercise**: Print out every number between 10 and 20 (inclusive).
>
> **BONUS**: Adjust your code to print only even numbers between 10 and 20 (inclusive)


```python
# Your code here: print out every number between 10 and 20 (inclusive)
# BONUS: Edit your code so it only prints the even numbers between 10 and 20 (inclusive)

x = 10

while x <= 20:
  print(x)
  #x = x + 1
  x = x + 2 # Bonus solution
print("Done.")
```

> **Exercise**: For a colony with an initial population size of 1, write a program that prints out the population size for 10 generations given that it doubles every generation.
>
> *Hint: You will need to initialize two variables and then use a `while` loop to update them.*


```python
# Your code here: calculate the population size of a colony over 10 generations that
# doubles in size every generation.

generation = 1
pop_size = 1

while generation <= 10:
  pop_size *= 2
  print("Population size in generation", generation, "is:", pop_size)
  generation += 1;
```

#### `for` loops

`while` loops work by repeating a set of instructions (i.e. a block of code) until some condition is met.

`for` loops, on the other hand, work by taking a group of inputs and performing a set of instructions on them one at a time. The key concept here is the **group of multiple inputs**, which leads into **data structures**, which we'll cover tomorrow in depth. Up until now, every piece of code we've run has used single pieces of data. `x = 5` is a single integer. `my_string = "Hello world!" is a single string. `for` loops work by taking **lists** of integers or strings, or lines in a file, and performing actions on each one individually.

More on that tomorrow. For now, we can demonstrate `for` loops with **strings**. This is because **strings are essentially a group of characters**. This means we can use a `for` loop to iterate over each character individually. In other words, strings are **iterable**.

Here is how a `for` loop would work to print out every character in a string:


```python
my_string = "Hello world!"

for current_character in my_string:
  print(current_character)

```

We start by defining a string. Then we encounter the `for` line where the first thing we see after `for` is a new variable, `current_character`. This is the **loop** or **update** variable. It's name, like other variables, is determind by the programmer, so we could have called it something else: `cur_char`, `current_letter`, `akjhgak`. It's purpose is to be used only within the loop, and its value is assigned based on the current iteration of the loop. Then, after that iteration it is **automatically updated** to be the next object in the string (or other **iterable**) that we're looping over. For a string, each object is an individual character, so the result of the loop is one character being printed per line of output.

After the loop variable we see the keyword **`in`**. We talked about `in` before as the **inclusion operator**. Here, confusingly, it acts somewhat differently, simply as a keyword to denote that the loop variable on the left will take on values according to the iterable on the right.

Then, we have our string, `my_string`, which is the thing over which we are iterating.

Again, syntactically, the colon `:` and indenation are required.

> **Exercise**: Are infinite loops possible when using `for`?

> **Exercise**: Use a `for` loop to calculate the length of a string without using the `len()` function.


```python
# Your code here: replicate the functionality of the len() function

my_string = "Hello world!"
char_tally = 0

for char in my_string:
  char_tally += 1

print(char_tally)
print(len(my_string))
```

We will cover `for` loops much more tomorrow when we learn about other **iterable** data structures.

### Review of loops

We've learned about the two types of loops in Python `while` and `for`. Loops are used for the most important and useful computational purposes: automatic repetition of tasks.

1.   `while` loops, like `if` statements run a block of code depending on a condition. However, they repeat that block of code until the condition is no longer met.
2.   `for` loops repeat blocks of code for different inputs given in an **iterable**.
3. In Python, indentation defines code blocks for loops (and conditional statements). If your line of code isn't indented at the same level of the loop, it will not be evaluated in the loop. Sometimes this can cause errors, and sometimes the program will run but with undesired output. It's up to the programmer to catch this.



## End day 1

Thanks! Let us know if you have any questions.

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

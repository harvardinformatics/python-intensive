---
title: "[Workshop] Python intensive, part 1"
description: "Introduction to programming concepts such as functions, data types, operators, logic, and control flow."
authors:
    - Gregg Thomas
    - Tim Sackton
---

# Python intensive, part 1

## Introduction

Welcome to the first part of the Harvard Informatics Python intensive workshop. This is a six day workshop intended to give a quick, yet thorough, introduction to programming concepts, the Python programming language, and how to use Python to facilitate data analysis.

Programmatic analysis of data allows scientist to have full control over how their data is parsed, assessed, and presented, unlike using third party programs (like Excel) which may make unwanted assumptions about how you want to read your data. The upside of this is that one could conceivably perform any analysis imaginable on their data, assuming they have enough coding skills. The downside is that one must know how to program. But that is the goal of this workshop: to give you the understanding of programming concepts and underlying skills such that you can see a problem or question in your work and then be able to understand how you would code the solution.

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

<details markdown>
<summary>Click to show instructions for loading the notebook locally</summary>

**See above for the recommended way to participate in this workshop. Only follow these instructions if Google Colab isn't working**

If for some reason Google Colab isn't working, or you prefer to run this locally, you will need to install Python, Anaconda, and the necessary libraries. You will have to follow these steps to do so. Note that some steps are only meant for specific operating systems.

0. If you are on Windows, [install WSL :octicons-link-external-24:](https://learn.microsoft.com/en-us/windows/wsl/install){:target="_blank"}. Once WSL is installed, you'll have a Linux terminal available to you in Windows. You can open this terminal by typing "wsl" in the search bar and clicking the app that appears. You'll also find your Linux distribution as a mounted drive in your file explorer.

1. Install mamba, a package manager using the command line - Terminal for Mac or WSL for Windows.

    1.1. For Mac, if you already have brew installed, install mamba using `brew install miniforge` and initialize it using `conda init zsh`. Then restart your terminal. If you don't have homebrew (i.e. the brew command doesn't exist), install brew first using `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
    
    1.2. For Windows, download the Linux (x86_64) installer from the miniforge repository [here :octicons-link-external-24:](https://github.com/conda-forge/miniforge){:target="_blank"} and install with `bash Miniforge3-Linux-x86_64.sh`.

2. Create a new environment using mamba with `mamba create -n pyworkshop numpy pandas matplotlib seaborn jupyter` and activate it with `conda activate pyworkshop`.

3. You can now run the jupyter notebook by typing `jupyter notebook` in the terminal. This will open a browser window with the jupyter notebook interface. You can navigate to the folder where you saved this notebook and open it.

4. Alternatively, install [VSCode :octicons-link-external-24:](https://code.visualstudio.com/){:target="_blank"} and the Python extension. Then open this notebook in VSCode and run it with the kernel that belongs to the pyworkshop environment. [How to guide here :octicons-link-external-24:](https://code.visualstudio.com/docs/datascience/jupyter-notebooks){:target="_blank"}

</details>

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

Let's go back to our detailed recipe. I mentioned before that certain actions, like **Walk** are invoked multiple times. To me, Walk seems like a **function**. That is, we should be able to say "Walk" in our recipe, and somewhere in our recipe book, some other recipe is looked up that looks something like this:

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

We'll take the Step function and put it somewhere else in our recipe book, so that everytime it is called in Walk_anywhere, we can go find the Step recipe to follow those instructions. And it just generally looks a lot cleaner typed out. Hopefully we'll be able to get this robot to bake us some nice cookies soon.

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

Using the **=** operator simply means that the **thing on the left side assumes the value of the thing on the right side**. In programming, the thing on the left side is always a **variable** (and in this case an argument to our function). Variables can be re-used later on in our program with the last value they were assigned. Importantly, the thing on the right side of the **=** operator can be another variable or a **literal**, that is a raw piece of information like a number or a character.

In our case, we're saying that we're setting the value of the variable *distance* to be the literal 2 meters and the value of the variable *angle* to be the literal 40°. And when we refer to *distance* and *angle* later on, we'll actually be referring to the values of 2 meters and 40°.

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

(Double click here to type your solution)


<details markdown>
<summary>Solution</summary>

```
Walk_anywhere(distance=1 meter and angle=180°)
```

</details>

### Pseudocode and syntax

What we've shown above a is a "program" in the sense that it lays out the instructions one step at a time. However, it does this in mostly plain English. This is called **pseudocode** and is a good way to get started when you're presented with a new problem you have to code.

The concepts conveyed about **functions** here directly translate into how functions work in computer programs. They are blocks of code (recipes) available in your recipe book (sometimes called a **library**) that are available to you even if you are on a different page in the recipe book or writing your own recipe. In other words, you can tell the robot to Walk_anywhere without you yourself having to know the exact text of the Walk_anywhere recipe.

> **Exercise**: Write out pseudocode for getting on the bus to go to the grocery store. Let's go around and have each person write one line.


```python
# Your pseudocode here
```

While the concepts are the same, the main difference between this pseudocode and an actual program is the **syntax**, which I've mentioned before is simply how things are typed or written. Each programming language has a unique syntax that provides structure and underlying instructions to the computer.

In an even more Pythonic syntax, we would call our Walk_anywhere function as:

```
Walk_anywhere(distance=2, angle=40)
```

Notice that we don't provide units (meters or °). Those things are useful for us to know as programmers and users of the program, but the program itself is mainly just interested in the data, in this case the two numbers.

### Programming in practice

Practically speaking, when we code, we type the instructions we wish the computer to carry out using the syntax of the language in which we are coding. In most cases, we type **one instruction per line**. The computer then reads the instructions one line at a time, from top to bottom, though the most powerful basic programming techniques can change this behavior. We'll learn about those later on.

We write our programs by typing in a text file using a **text editor**. Some text editors are designed for coding with useful features such as syntax highlighting and automatic formatting. However, even the most plain text editor (*e.g.* Notepad) could be used to write a computer program.

In this workshop, the text editor we're using is conveniently built-in to the Jupyter notebook as the code cells.

In Python, empty lines are ignored, as are lines that begin with the `#` character. These lines are called **comments** and are meant for notetaking and documenation.

Now that we know that a **function** is like another recipe in our recipe book of code, let's look at some actual Python functions.

## Functions in Python

There are a range of Python functions built-in to the language, as well as a multitude of external **libraries** that can be **imported** to be used, like getting another recipe book from your bookshelf or at the public library.

Let's look at a very basic function. What happens when you run the single line of code below?


```python
abs(-5)
```

<pre class="output-block">5
</pre>

The `abs()` function takes as input a single **integer** and **returns** its absolute value. In this case, the absolute value of -5 is 5. Under the hood, there is some block of code that Python has installed on your computer that is looked-up and run every time it sees that you've typed and run `abs()`. I don't know what this code looks like (though I could guess for such a simple function), and I don't even know where it is on the computer. But that's what's so great about functions: they simplify tasks that are repeated often, saving us programmers time and effort.

For instance, if we needed to know the absolute value of 10 numbers and the underlying code for `abs()` is 4 lines of code and we DIDN'T have it stored as a function, we would have to write out those 4 lines 10 times (recall the Walk_to_oven and Walk_to_cabinet problem). Now, with `abs()`, we only need to write that function call 10 times.



### Functions usually require input

What happens if you run this code block:


```python
abs()
```

<pre class="output-block">---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[6], line 1
----> 1 abs()

TypeError: abs() takes exactly one argument (0 given)
</pre>

You get an **error** (a very common occurrence when coding). Remember, almost all functions require additional information in the form of **arguments**. In the case of `abs()` it requires a single argument, a number. Without it, the underlying code doesn't work, so it stops the program and tells us before it even tries.

How about this:


```python
abs(-5, 7, -12)
```

<pre class="output-block">---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[7], line 1
----> 1 abs(-5, 7, -12)

TypeError: abs() takes exactly one argument (3 given)
</pre>

Still no good. In this case, the function takes EXACTLY one number and runs some code using it. This may not always be the case, and different functions are going to require different inputs.

Ok then, how would you know how many arguments a given function takes? Or if there even exists a function to do a particular task?

### Learning more about functions

If you know the name of the function and are coding in a notebook like this, you can conveniently use another function called `help()`. The `help()` function takes as an argument the name of another function and looks up some (hopefully helpful) documentation about it and prints it to the screen.

Try this:


```python
help(abs)
```

<pre class="output-block">Help on built-in function abs in module builtins:

abs(x, /)
    Return the absolute value of the argument.
</pre>

This tells us what `abs()` does and tells us that it requires one argument, `x`. (The `/` indicates that the argument is positional, but you can ignore that for now.)

What about if you know what you want to do, but you're not sure if there is a function to do it. This begins to touch a bit on a host of 'meta-skills' that one picks up as they start to code and work with computers more. It may seem obvious, but the first solution is to simply search the internet. The difficulty comes when you try to word your search, and unfortunately that will change depending on the task.

However, there are some resources that will pop-up that are generally pretty reliable. For instance, the official [Python documentation :octicons-link-external-24:](https://docs.python.org/3/){:target="_blank"} can be helpful, but is sometimes cryptic (e.g. the / above in the `abs()` `help()` output). StackExchange and [StackOverflow :octicons-link-external-24:](https://stackoverflow.com/){:target="_blank"} are great resources that provide community answers to programming problems. But sometimes it is difficult to find an answer to your specific problem unless you post it yourself.

Now, it is also feasible to ask a LLM chatbot (e.g. ChatGPT, CoPilot) to help with coding problems. While these bots have their issues with reliability for real world information, they tend to be quite accurate for basic programming problems. For instance, you could ask, "How do I get the largest number of a list of numbers in Python?" and it would probably reply with some answer related to the `max()` function.



#### Meta-skills and other Python tips

While we'll occasionally touch on some of these meta-programming skills, like getting help and debugging, we're sticking mostly to actual programming in our workshop. However, these skills are really important, so we've compiled a notebook of [Healthy Habits for Python](https://informatics.fas.harvard.edu/workshops/python-intensive/python-healthy-habits/) to accompany this workshop. Be sure to read through it and we can talk about any specific questions you have.

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

<pre class="output-block">---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[9], line 1
----> 1 abs("-5")

TypeError: bad operand type for abs(): 'str'
</pre>

It is more-or-less telling us that we gave it a string when this function only works for integers.

This may seem obvious with such a simple example, but later on, when data types are obfuscated behind variable names and data structures, you may start getting errors like this that may be harder to understand.



**One of the most important concepts in programming is to always know what data type you are working with.**

### More examples of functions

Let's say we have the following string: "Teach a robot to bake cookies."

And we've entered this data into our Python script and **stored it as a variable** using the **=** operator as in the code block below.



> **Exercise**: What function could we use to count the number of individual characters in our string? What happens if we use the same function to count the number of digits in a number? Enter your answer in the code below.




```python
my_string = "Teach a robot to bake cookies."

# Your code here: Find a function to put here that counts the number of characters in my_string
```

??? success "Solution"
    ```python
    my_string = "Teach a robot to bake cookies."
    len(my_string)
    ```

    <pre class="output-block">30
    </pre>


```python
my_integer = 124

# Your code here: Use the same function to count the number of digits in my_integer
```

??? success "Solution"
    ```python
    my_integer = 124
    len(my_integer)
    ```

    <pre class="output-block">---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call last)
    Cell In[13], line 3
          1 #@title Solution {display-mode: "form"}
          2 my_integer = 124
    ----> 3 len(my_integer)
    
    TypeError: object of type 'int' has no len()
    </pre>

#### print()

Another important function in Python is `print()`. This function takes any number of arguments and simply displays them on the screen. This may seem unnecesary in our Jupyter notebook, where function output is automatically displayed, but `print()` allows us to display **and format** output in other environments.

> **Exercise**: Use `print()` to display both `my_string` and `my_integer` on a single line.



```python
# Your code here: Display my_string and my_integer on a single line
```

??? success "Solution"
    ```python
    print(my_string, my_integer)
    ```

    <pre class="output-block">Teach a robot to bake cookies. 124
    </pre>

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

<pre class="output-block">The absolute value of -5 is 5
</pre>

This chunk demonstrates a few things:

1.   Instead of giving the `abs()` function our data directly, we've instead given it a variable in which we've stored our data.
2.   We used `=` to assign the result of `abs()` to another variable
3.   We used `print()` to format and display the result.

> **Exercise**: Using the function you looked up and learned about above (`len()`), write a few lines of code that store a string, look-up its length, and display both the string and the length using `print()`.


```python
# Your code here: Store a string, calculate its length, and print both
```

??? success "Solution"
    ```python
    my_string = "Teach a robot to bake cookies."
    my_string_length = len(my_string)
    print("The message: '", my_string, "' is", my_string_length, "characters long.")
    ```

    <pre class="output-block">The message: ' Teach a robot to bake cookies. ' is 30 characters long.
    </pre>

### Indirection

In programming, indirection is the use of one object to reference another. We've seen this a couple of times already, and we want to introduce this concept now because as we move to more advanced data structures, multiple levels of indirection can be used and may make things difficult to understand.

In Python, we can say that using anything other than a **literal** value is a level of indirection. Here is a simple example:


```python
x = 5
abs(x) # Here, we've indirectly referenced the literal of 5 by using the variable x.
```

<pre class="output-block">5
</pre>

This example seems pretty easy to understand, but this concept will be very important as we move forward. In fact, efficient and automated programs couldn't be written at all without indirection: indirection allows us to manipulate data within programs and accept different data when running the same program multiple times.

As such, we may also occasionally do some "code golf" or "code bowling" exercises to show the trade-offs between too much and too little indirection. For example, we could easily "code golf" this block:


```python
a = 3
b = 5
c = 8
d = 2
e = 1

print(a + b + c + d + e)
```

<pre class="output-block">19
</pre>

To just be:


```python
print(3 + 5 + 8 + 2 + 1)
```

<pre class="output-block">19
</pre>

Which is very succinct (1 line vs. 6 lines) and clear, but we lose the ability to manipulate the data easily elsewhere in our program, *e.g.*:


```python
a = 3
b = 5
c = 8
d = 2
e = 1

a = a + 6

print(a + b + c + d + e)
```

<pre class="output-block">25
</pre>

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

<pre class="output-block">  Cell In[24], line 3
    2_data = 7 # no good!
     ^
SyntaxError: invalid decimal literal
</pre>

2.   **Keywords**, like `if`, `while`, `in`, cannot be used as variable names because they are used for other operations. The following shows a list of keywords that cannot be used as variable names:


```python
import keyword
print(keyword.kwlist)
```

<pre class="output-block">['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
</pre>

3.   Variables are case sensitive, so the variables `count`, `Count`, and `COUNT` are all unique and can be used simultaneously, though this would not be a best practice since it makes the code harder to read.




```python
count = 5
Count = 6
COUNT = 7
print(count, Count, COUNT)
```

<pre class="output-block">5 6 7
</pre>

### Whitespace in Python, part 1

Whitespace refers to any part of a string that is not a visible character, such as a space, tab, or new line. In some cases, Python actually uses whitespace to interpret code, which we'll learn about later. But in most cases, it is very forgiving:


```python
x               =                   5








print(        x       
      
      )
```

<pre class="output-block">5
</pre>

Obviously, typing code like this is completely unreadable, but adding whitespace in certain spots can actually make things a bit easier to parse by eye:


```python
my_string = "Teach a robot to bake cookies."
my_string_length = len(my_string)

print("The message: '", 
      my_string, 
      "' is", 
      my_string_length, 
      "characters long."
    )
```

<pre class="output-block">The message: ' Teach a robot to bake cookies. ' is 30 characters long.
</pre>

The most important general rule (other than indented code blocks, which we'll learn about later), is that any individual command should be isolated to one line, but parts of that command contained within characters can be broken into multiple lines. As above, in the call to the `print()` function where we place the arguments of the function on separate lines and indent them.

However, lines of code that are not calls to functions or defining things separated by commas (generally) must be kept to one line:


```python
x =
5
```

<pre class="output-block">  Cell In[29], line 1
    x =
       ^
SyntaxError: invalid syntax
</pre>

Best advice: keep individual instructions to a single line, and only consider adding whitespace for legibility for difficult to read function calls or data structure definitions (more later).

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

<pre class="output-block">12
</pre>

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

<pre class="output-block">6
2
8
2.0
</pre>

Here, we've used a bit of indirection by giving the `print()` function a single argument: the result of the arithmetic operation, which it then displays.

Notice that, for division, we see that it has added a decimal place. It has converted our integers into **floating point** numbers, another numeric data type in Python, to deal with numbers that are not divisible:


```python
x = 3
y = 2

print(x / y)
```

<pre class="output-block">1.5
</pre>

A couple other arithmetic operators are:

*   `**` : called the **exponentiation** operator, this raises the number on the left side to the power on the right side
*   `%`  : called the **modulo** or **modulus** operator, this divides two numbers and returns the _remainder_ of the division
*   `//` : called the **floor division operator**, this divides and then rounds down

Let's take a look at some examples.


```python
x = 3
y = 2

print(x ** y)
print(x % y)
print(x // y)
```

<pre class="output-block">9
1
1
</pre>

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

<pre class="output-block">7
9
---
8
3
</pre>

### String operators, or why its important to know your data types

The above operators are useful for arithmetic on **integers** (or **floats**). However, some operators can also be used on strings.

#### Concatenate strings with `+`

The `+`, operator in particular, can be used to **concatenate**, or combine, strings together.


```python
x = "hello"
y = "world"

print(x + y)
```

<pre class="output-block">helloworld
</pre>

This can be very useful when formatting strings, either for processing or for output.

**Remember, certain functions expect certain data types** (strings or integers). In most cases, if the wrong data type is provided, an error will stop the program, like in our `abs()` example. However, in some cases, functions that accept both data types can produce unexpected results without informing you at all!


```python
important_data_point1 = "9"
important_data_point2 = "8"

sum_of_important_data = important_data_point1 + important_data_point2

print("I'm now showing my professor my important results:", sum_of_important_data)
```

<pre class="output-block">I'm now showing my professor my important results: 98
</pre>

Here, no error is displayed telling you you are concatenating two strings rather than adding together two integers. That's because both things are vaild to do with Python syntax: Python has no way of knowing that you wanted to add these numbers rather than concatenate them - that's up to you to tell it! Remember, every little step of a computer program has to be given, otherwise you will get errors (relatively easy to debug) or **logic errors**, which occur when the program runs, but gives unexpected results, and are generally harder to debug.

> **Exercise**: Correct the code so that it accurately prints the sum of the two data points.


```python
# Edit and correct the code here
important_data_point1 = "9"
important_data_point2 = "8"

sum_of_important_data = important_data_point1 + important_data_point2

print("I'm now showing my professor my important results:", sum_of_important_data)
```

<pre class="output-block">I'm now showing my professor my important results: 98
</pre>

??? success "Solution"
    ```python
    important_data_point1 = 9
    important_data_point2 = 8
    
    sum_of_important_data = important_data_point1 + important_data_point2
    
    print("I'm now showing my professor my important results:", sum_of_important_data)
    ```

    <pre class="output-block">I'm now showing my professor my important results: 17
    </pre>

Luckily, if we ever try to `+` a string and an integer together, it stops us with an error:


```python
x = "9" + 8
```

<pre class="output-block">---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[39], line 1
----> 1 x = "9" + 8

TypeError: can only concatenate str (not "int") to str
</pre>

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

<pre class="output-block">hahahaha
</pre>

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

<pre class="output-block">True
--- print True check ---
</pre>

<pre class="output-block">---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[41], line 3
      1 print(True)
      2 print("--- print True check ---")
----> 3 print(true)
      4 print("--- print true check ---")

NameError: name 'true' is not defined
</pre>

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

<pre class="output-block">bool() of a boolean:
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



??? success "Solution"
    ```python
    print(bool("False"))
    ```

    <pre class="output-block">True
    </pre>

### Logical operators: **and** and **or**

Sometimes, we want to test whether a combination of boolean values together evaluate to `True` or `False` in different ways. This allows us to make complex logical conclusions based on the state of variables in our program.

We do this with the logical operators **and** and **or**.

In both cases, the objects on the left and right of the operator are evaluated as booleans. For **and**, both objects must return `True` in order for the entire expression to be True:


```python
print(True and True)
print(True and False)
print(False and False)
```

<pre class="output-block">True
False
False
</pre>

For **or**, only one of the two booleans must be `True` for the whole expression to be True:


```python
print(True or True)
print(True or False)
print(False or False)
```

<pre class="output-block">True
True
False
</pre>

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


# Your code here: Two integers with or that returns False


# Your code here: Integer and string with and that returns True


# Your code here: Integer and string with and that returns False
```

??? success "Solution"
    ```python
    # Two integers with and that returns True
    print(1 and bool(573657))
    
    # Two integers with or that returns False
    print(bool(0) or bool(0))
    
    # Integer and string with and that returns True
    print(bool(235) and bool("hello"))
    
    # Integer and string with and that returns False
    print(bool(0) and bool(""))
    ```

    <pre class="output-block">True
    False
    True
    False
    </pre>

#### Complex logical statements and order of operations

Using `and` and `or`, we can evaluate multiple boolean values.


```python
print(True or True and False)
```

<pre class="output-block">True
</pre>

This statement returns `True`. Logical statements have their own order of operations, with **`and` taking precedence over `or`**. Given that, let's break the statement down.

1. We read the `and` comparison first. `True and False` evaluates to `False` - both sides of an `and` need to be True.
2. Given that, the expression reduces to `True or False`, which evaluates to `True` since only one side of an `or` statement needs to be True. This means the entire expression results in `True`.

The order of operations can be made more explicit with parentheses.


```python
print(True or (True and False))
```

<pre class="output-block">True
</pre>

This is the exact same logical expression as the one above, but we've added the parentheses to make things a little bit easier for us to parse. In logical expressions, **parentheses also affect the order of operations** as they do in mathematical expressions: they take precedence over anything else. In that way, we can change the result of this expression by moving the parentheses.


```python
print((True or True) and False)
```

<pre class="output-block">False
</pre>

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


# 2. Your answer here:
# 2. Your code here


# 3. Your answer here:
# 3. Your code here


# 4. Your answer here:
# 4. Your code here


# 5. Your answer here:
# 5. Your code here
```

??? success "Solution"
    ```python
    # 1. Your answer here: False
    # 1. Your code here
    print(False or False and True)
    
    # 2. Your answer here: False
    # 2. Your code here
    print((False or False) and True)
    
    # 3. Your answer here: True
    # 3. Your code here
    print(True and True or False and False)
    
    # 4. Your answer here: False
    # 4. Your code here for
    print(True and (True or False) and False)
    
    # 5. Your answer here: True
    # 5. Your code here for
    print(False or False or False or False or True or False)
    ```

    <pre class="output-block">False
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

<pre class="output-block">False
True
True
</pre>

Note that `not` works on individual parts of a logical expression, not the entire thing. So, `False or True` returns `True` and `not False or True` also returns `True`. This is because the `not` is only negating the first `False`, essentially making the statement `True or True`. To negate chunks of an expression, use parentheses. `not (False or True)` will indeed return `False`, since the expression itself is `True` and we are negating the whole thing.


```python
print(False or True)
print(not False or True)
print(not (False or True))
```

<pre class="output-block">True
True
False
</pre>

> **Exercise:** Fill out the following truth table. We will go from left to right. Double click on the table to edit.

A   | B   | A and B | not B | A and not B | A and B or A and not B | A and (B or A) and not B |
--- | --- | ------- | ----- | ----------- | ---------------------- | ------------------------ |
T   | T   |         |       |             |                        |                          |
T   | F   |         |       |             |                        |                          |
F   | T   |         |       |             |                        |                          |
F   | F   |         |       |             |                        |                          |

<details markdown><summary>Solution</summary>

A   | B   | A and B | not B | A and not B | A and B or A and not B | A and (B or A) and not B |
--- | --- | ------- | ----- | ----------- | ---------------------- | ------------------------ |
T   | T   |    T    |   F   |      F      |           T            |             F            |
T   | F   |    F    |   T   |      T      |           T            |             T            |
F   | T   |    F    |   F   |      F      |           F            |             F            |
F   | F   |    F    |   T   |      F      |           F            |             F            |

</details>

What do you notice about the second to last column of the truth table representing the full expression?

### Comparison operators for integers

One can also compare two objects in Python and return a boolean value, either `True` or `False`. Doing this can help the program make decisions about the next instructions to execute, based on how it has been programmed.

In order to compare two numbers and return either a `True` or `False` boolean value, there are several operators one can use depending on the situation. These will all seem relatively familiar based on how they are used in arithmetic.

*   `>` : Greater than. Returns `True` if the number on the left is larger than the number on the right. Returns `False` otherwise.
*   `>=` : Greater than or equal to. Returns `True` if the number on the left is larger or the same as the number on the right. Returns `False` otherwise.
*   `<` : Less than. Returns `True` if the number on the left is smaller than the number on the right. Returns `False` otherwise.
*   `<=` : Less than or equal to. Returns `True` if the number on the left is smaller or the same as the number on the right. Returns `False` otherwise.
*   `==` : Is equal to. Returns `True` if the numbers on the left and the right are the same. Returns `False` otherwise.
*   `!=` : Is not equal to. Returns `True` if the numbers on the left and right are different. Returns `False` otherwise (*i.e.* if they are the same).

Here are some examples.


```python
print(8 > 9)
print(9 > 9)
print(9 >= 9)
print(8 != 9)
```

<pre class="output-block">False
False
True
True
</pre>

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

<pre class="output-block">True
False
---
False
True
4
</pre>



> **Exercise**: In the code block below, do the following:
> 1.   Assign any integer value to a variable called my_int1
> 2.   Assign any other integer value to a variable called my_int2
> 3.   Use a comparison to print out whether the two numbers are equal.


```python
# Your code here: Assign any two integers to variables my_int1 and my_int2
my_int1 = 5 ### SL
my_int2 = 5 ### SL

# Your code here: Print out whether the integers stored in your variables are equal to each other
print(my_int1 == my_int2) ### SL
```

<pre class="output-block">True
</pre>

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

<pre class="output-block">True
False
True
</pre>

Importantly, case matters for these comparisons:


```python
print("Hello" == "hello")
```

<pre class="output-block">False
</pre>

Like we said above, the other operators (e.g. `>`, `<=`, etc.) do indeed work on strings, but that use-case is not common for most programmers.

### The inclusion operator for strings: `in`

The final operator we'll be learning about is the **inclusion**, or **membership**, operator for strings, `in`. It works as follows:

*   `in` : The inclusion operator for strings. Returns `True` if the string on the left is contained within (is a sub-string of) the string on the right. Returns `False` otherwise.



```python
print("lo" in "hello")
print("cookies" in "robot")
```

<pre class="output-block">True
False
</pre>

Checking for exact sub-strings with `in` is the most basic of pattern matching, which is extremely useful in programming.

> **Exercise**: *CODE BOWLING*: Re-write the two lines of code using variables to indirectly refer to each of the four strings in the print statment.


```python
# Edit this code to use variables instead of literal strings
print("lo" in "hello")
print("cookies" in "robot")
```

<pre class="output-block">True
False
</pre>

??? success "Solution"
    ```python
    string1 = "lo"
    string2 = "hello"
    print(string1 in string2)
    
    string3 = "cookies"
    string4 = "robot"
    print(string3 in string4)
    ```

    <pre class="output-block">True
    False
    </pre>

## Metaprogramming skills and debugging

Recall that there are a host of meta-skills that we won't have time to discuss formally during the workshop. We've prepared the [Python Healthy Habits notebook](https://informatics.fas.harvard.edu/workshops/python-intensive/python-healthy-habits/) as a supplement for you to go through on your own, and we'll be happy to discuss any topics you have questions about!

### Pair programming

One meta-skill we want to touch on today though is **pair programming**. Pair programming is a technique where two programmers work together on the same code. One person is the "driver" who writes the code, while the other person is the "navigator" who reviews the code as it is written. This can be a very effective way to catch errors early and to learn from each other. Let's practice by "code golfing" the following block of code. 

> **Exercise**: *CODE GOLF*. Pair up with someone, and then try to make this code run with as few lines as possible, while achieving the same result.


```python
## Edit the to run with the same result using as few lines as possible
first_str = "robot"
second_str = "baking"
third_str = "cookies"

length_first_str = len(first_str)
length_second_str = len(second_str)
length_third_str = len(third_str)

total_length = length_first_str + length_second_str + length_third_str
print("The total length of the strings is:", total_length)
```

<pre class="output-block">The total length of the strings is: 18
</pre>

??? success "Solution"
    ```python
    first_str = "robot"
    second_str = "baking"
    third_str = "cookies"
    
    total_length = len(first_str) + len(second_str) + len(third_str)
    print("The total length of the strings is:", total_length)
    ```

    <pre class="output-block">The total length of the strings is: 18
    </pre>

??? success "Solution"
    ```python
    print("The total length of the strings is:", len("robot") + len("baking") + len("cookies"))
    ```

    <pre class="output-block">The total length of the strings is: 18
    </pre>

## Review

So far, we've learned a few main things:

1. Functions are little sub-recipes of code that perform specific tasks given the appropriate input. They are usually typed as `function_name(input1, input2, ...)`.
2. Operators (*e.g.* `+`, `and`) can be thought of as special functions that instead take input based on what is place on either side of them.
3. Different data types exist in programming, notably **integers** and **strings** in Python. **Functions and operators may only work for a given data type**.
4. Complex logical statements can be constructed with **boolean** values (`True`, `False`) and the associated operators (*e.g.* `>`, `not`, `in`). Again, some of these operators only work for specific data types.

These concepts form the basis of programming in any language (though the syntax will vary), however one cannot make more than very simple programs using these types of instructions alone.

In order to write complex programs that take these basic concepts and allow them to be executed based on the **conditions** of the data within a program, and to automate the **repetition** of certain instructions, we need to learn the syntax that allows us to control the flow of the program. That is where we will begin in Part 2 of the workshop!

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

## End Part 1

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

    /* Hide all 2nd-level navs */
    .md-nav--secondary .md-nav__item .md-nav {
        display: none !important;
    }

    /* Show when parent has .expanded class */
    .md-nav--secondary .md-nav__item.expanded > .md-nav {
        display: block !important;
    }
  

</style>

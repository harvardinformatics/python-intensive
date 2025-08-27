---
title: "[Workshop] Python intensive, part 3"
description: "More on writing your own functions, debugging strategies, and exception handling in Python."
authors:
    - Lei Ma
    - Tim Sackton
---

# Python intensive, part 3

## Review of Parts 1 + 2

Welcome to Part 3 of our python intensive course. This is the last part of the "introduction to programming" part of the course, after which we will move on to the "introduction to data science" part. Let's review what we have learned so far:

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


### Jokes

To re-iterate some of the concepts we talked about in the previous parts of the workshop, let's start with a joke about computer programmers.

Sam asks their computer programmer spouse to go get some groceries. Sam tells him, "Please go to the store to get some groceries. Buy a loaf of bread. If they have eggs, get a dozen." The spouse comes back with 13 loaves of bread.

Below is some pseudocode that represents what the computer programmer did.

```
go to the store

loaf_of_bread = 1
if eggs:
    loaf_of_bread += 12
```

This joke illustrates that what may make sense in natural language does not immediately translate to computer language. And therefore we have to be really specific, giving every instruction even, when we're programming.

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

<pre class="output-block">---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[1], line 1
----> 1 print(log(100))

NameError: name 'log' is not defined
</pre>

However, there is a `math` library with a a `log()` function that you can import!


```python
import math
print(math.log(100))
```

<pre class="output-block">4.605170185988092
</pre>

Note that by default it does natural log.

Also, notice that, in order for Python to know where to find the function even though we've imported it, we have to tell it explicitly with `math.`. This helps in the circumstance that you import multiple libraries that happen to have a function with the same name.

However, you can also directly import a function from a library with the `from` keyword:


```python
from math import log
print(log(100))
```

<pre class="output-block">4.605170185988092
</pre>

One could also declare an **alias** for the library if you want to still import the whole library but not have to type the the complete name of it every time:


```python
import math as m
print(m.log(100))
```

<pre class="output-block">4.605170185988092
</pre>

This means `m` exists as an object in your program (just as if you'd assigned it with `=`). But of course, this means you can't use `m` as an object name anywhere else in the program:


```python
import math as m

m = "hello world!"

print(m.log(100))
```

<pre class="output-block">---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
Cell In[5], line 5
      1 import math as m
      3 m = "hello world!"
----> 5 print(m.log(100))

AttributeError: 'str' object has no attribute 'log'
</pre>

There are many, many libraries out there. Some are pre-installed with Python (like `math`), but others you may find and have to install for yourself. Hopefully the authors have easy and clear instructions for installation...

In later days, we'll work with some libraries meant for data analysis and visualization, `pandas` and `seaborn`.

## Writing functions

Of course, there may come a time when you're coding and you notice you're repeating the same set of instructions on different inputs a lot. This, of course, is the perfect use-case for a function, and like the people that write the libraries you import, you can also write your own functions!

**Write lots of functions! Functionalize everything!**

There are many reasons to write functions, even if you think you might only use it once in your notebook or workflow. Using functions in your code improves the readability of the code, because rather than puzzle through many lines trying to interpret what was going on, you can just read the function name/description and understand what happened. It also improves readability by allowing the reader to focus on the important parts of the code rather than functions that may perform rote tasks.

Functions make your code more modular and reproducible. By breaking down the analysis into discrete chunks, you can easily swap out functions to test things or move sections of code around because functions are very portable.

Functions also make your code more testable. When you encounter a bug or an unexpected outcome, you can more easily trace the source of the problem if you have functions that are well-documented and do one thing. Think of it like mixing smaller batches of reagents that you use at a time rather than one big container.

**Functions should do ONE thing**

Functions are meant to do one thing, just like a sentence is meant to express a complete thought. If you bundle your entire analysis into a single function, it's akin to writing a run-on sentence by abusing colons, semi-colons, etc. It might be correct and it might run, but it will be hard to read and also hard to debug. Make liberal use of calling functions within functions and making your code modular.


### Function syntax

When writing a function, you must start the line with the `def` keyword, which stands for *define*. Then you can give the function a name. The name can be anything, as long as the name abides by the standard object naming conventions (see Part 1). Then you type parentheses `()` followed by a colon `:`:

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

<pre class="output-block">hello world!
</pre>

Great! Now anytime we want to print "hello world!" all we have to do is type `my_function()`!

Well, ok so that's not very useful. Let's make a more interesting function.

> **Exercise**: Below, we've provided the code for a magic 8 ball type response. It randomly selects an answer from a list of answers. This code is not in a function. Put it in a function called `magic_8_ball()` and call it a few times in the code block. Remember, every line of code you want to be included in the function must be indented!


```python
import random # This is a built-in Python library for random-number generation tasks (such as randomly selecting an element from a list)

# List of possible responses
responses = [
    "Yes", "No", "Maybe", "Ask again later", "Definitely",
    "I have no idea", "Very doubtful", "Without a doubt", "Outlook not so good"
]

# Select a random response
answer = random.choice(responses)

# Print the response
print("The Magic 8-Ball says:", answer)

# When your function is ready, call it a few times by uncommenting these lines:
# magic_8_ball()
# magic_8_ball()
# magic_8_ball()
```

<pre class="output-block">The Magic 8-Ball says: Outlook not so good
</pre>

??? success "Solution"
    ```python
    
    import random # This is a built-in Python library for random-number generation tasks (such as randomly selecting an element from a list)
    
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

    <pre class="output-block">The Magic 8-Ball says: I have no idea
    The Magic 8-Ball says: I have no idea
    The Magic 8-Ball says: Without a doubt
    </pre>

### Handling arguments

Of course, just like the built-in functions, our functions are a lot more versatile and useful if they **accept input in the form of arguments**.

We know how to provide arguments by placing them in the parentheses during the function call (e.g. with `abs(-5)`, `-5` is the argument).

When writing a function, we must also define which arguments are accepted within the parentheses of our function definition:

```
def my_function(arg1, arg2, ...)
```

You can name the arguments anything you'd like, as long as the names conform to the object naming conventions we've gone over (see Part 1). And in this example, the `...` indicates that you can define more arguments for your function if they are needed. Of course, as we saw above with the hello world! and `magic_8_ball()` functions, a function doesn't have to have arguments at all.

Here is an example of a simple function with one argument, a number:


```python
def square(num):
  print(num * num)

square(2)

my_other_num = 4
square(my_other_num)
```

<pre class="output-block">4
16
</pre>

Here, we've told the function to expect a single number as an argument. Within the function, we call this number object `num`. The function then simply prints out the square of the number. And we've shown a couple of ways to call the function.

Just like with built-in functions, if we don't provide the expected number of arguments to our function, the program will stop with an error:


```python
square(2, 4)
```

<pre class="output-block">---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[11], line 1
----> 1 square(2, 4)

TypeError: square() takes 1 positional argument but 2 were given
</pre>

> **Exercise**: Edit the `magic_8_ball()` function to take a question (a single string) as an argument and print it out before the response.


```python
import random # This is a built-in Python library for random-number generation tasks (such as randomly selecting an element from a list)

# Your code here: edit the magic_8_ball function to accept a question string as an argument
# and to print out the question in addition to the answer.

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
# magic_8_ball("Will it snow tomorrow?")
```

??? success "Solution"
    ```python
    
    import random # This is a built-in Python library for random-number generation tasks (such as randomly selecting an element from a list)
    
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

    <pre class="output-block">Will it snow tomorrow? : I have no idea
    </pre>

#### Default arguments

It is also possible to define default values for a particular argument, in which case they do not necessarily need to be provided when the function is called:


```python
def square(num=2):
  print(num * num)

square()
square(3)
```

<pre class="output-block">4
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

<pre class="output-block">4
---
4
8
</pre>

> **Exercise**: Write a function that takes two numbers: one to be the base and another to be the exponent. By default, this function should square the provided base number. However, if an exponent is provided, it will raise the base to that power. Provide use cases that show the function being used both with its default behavior (squaring the base) and with another exponent.


```python
# Your code here

# Provide test cases for your function below
```

??? success "Solution"
    ```python
    
    def power(base, exponent=2):
      print(base ** exponent)
    
    # Provide test cases for your function below
    power(2)
    power(2, 3)
    ```

    <pre class="output-block">4
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

<pre class="output-block">  Cell In[18], line 1
    def add_2_nums(num1, also_multiply=False, num2):
                                              ^
SyntaxError: non-default argument follows default argument
</pre>

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

<pre class="output-block">4
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

<pre class="output-block">4
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

<pre class="output-block">Hello Alice ?
</pre>

Here, we only provided values for `person` and `puncutation`, skipping over `greeting` in our function call, which uses it's default value. The combined use of default values for our arguments in the function and calling the function with named arguments makes our function call clearer and less error-prone.

### Writing functions exercise

> **Exercise**: Write a function that takes a **list of numbers** as an argument and prints out the tally (number of numbers), and the min, max, sum, and average of the numbers in the list. Call this function `num_summary()`. Run it on the lists provided below.
>
> *Hint: While you could code these simple tasks yourself with a `for` loop and some `if` statements, remember there are functions that do these tasks for us that you can call in your own function. See the List functions section from Part 2.*


```python
# Your code here: a num_summary() function
```

??? success "Solution"
    ```python
    
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

    <pre class="output-block">There are 6 numbers in the list.
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

<pre class="output-block">4
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

<pre class="output-block">{'apple': 2, 'banana': 5, 'orange': 3}
</pre>

For instance, this function, which takes a **list of tuples** and converts them into a **dictionary**. This dictionary is returned and printed to the screen.

> **Exercise:** Write a function called `in_list` that takes a number and a list of numbers and checks if that number already exists in the list. If it does, print "number already exists!" or something similar. If it doesn't, add that number to the list. In both cases, return the list.


```python
# Your code here

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

<pre class="output-block">Original: [1, 2, 3, 4, 5]
---
</pre>

<pre class="output-block">---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[26], line 8
      5 print("Original:", my_list)
      6 print("---")
----> 8 my_list = in_list(3, my_list)
      9 print("After first call:", my_list)
     10 print("---")

NameError: name 'in_list' is not defined
</pre>

??? success "Solution"
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

    <pre class="output-block">Original: [1, 2, 3, 4, 5]
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

<pre class="output-block">(9, 27)
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

<pre class="output-block">9
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

<pre class="output-block">1
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

  print("There are", num_nums, "numbers in the list.")
  print("The largest number is:", max_num)
  print("The smallest number is:", min_num)
  print("The sum of all the numbers is:", sum_nums)
  print("The average of the numbers is:", avg_num)

# Run your modified function on these lists 
nums1 = [23, 85, 56, 34, 78, 22]
nums2 = [17, 48, 92, 55, 83, 24, 63, 7, 31, 89]
nums3 = [59, 44, 66, 12, 5, 95, 23, 37]

# Add your function calls here

# Print only the highest of the averages
print("The highest average number is:", )
```

<pre class="output-block">The highest average number is:
</pre>

??? success "Solution"
    ```python
    
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
    
    avgs = []
    for num_list in [nums1, nums2, nums3]:
      cur_result = num_summary(num_list)
      avgs.append(cur_result[4])
    
    # Print only the highest of the averages
    print("The highest average number is:", max(avgs))
    ```

    <pre class="output-block">The highest average number is: 50.9
    </pre>

#### `None`

In Python, in order for the language to function consistently, all functions return a value, even those without an explicit `return` statement. The default return value for a Python function is `None`:


```python
def greet():
  print("hello world!")

result = greet()
print(result)
```

<pre class="output-block">hello world!
None
</pre>

In Python, `None` is actually its own data type, meant to indicate the absence of information or as a placeholder. `None` is most often seen when trying to use the result of a function, as shown above, but it can actually be a useful initial or default data value, since it evaluates to `False` as a boolean:


```python
data = None
print(data)
print(bool(data))

if data:
  process_data(data) # made up function for this example
else:
  print("No data has been provided")
```

<pre class="output-block">None
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

## f-strings

One quick string concept to cover before we move on to other topics is **f-strings**. F-strings are a way to format strings in Python. The way they work is to start a string with the keyword `f`, preceding the first quotation mark. Then, whenever you need to insert a variable within the string that has previously been assigned, you surround that variable name with `{}`. Think of `{}` as a carve-out from the string where code is valid again.

They are a way to embed variables into strings. Here's an example:


```python
my_num = 1004210.52049

print(f"my number is: {my_num}. Hooray!")
print(f"twice my number is: {my_num * 2}. Hooray!")
print(f"my original number, {my_num}, did not change")
```

<pre class="output-block">my number is: 1004210.52049. Hooray!
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

<pre class="output-block">my number is: 1004210.52
my number is: 1004211
my number is: 1,004,210.52049
my number is: 1,004,210.52
1004210.52049
</pre>

## Functions to Programs

Now that we know a bit about writing functions, we'll learn how to write code that uses multiple functions to perform certain tasks. We will create a simulation of a random walk. Given the inputs of a step size and boundary size, it will simulate a walk from the middle of a defined space (represented by `-`) until the object runs into a wall. Here's what it might look like to use this function: 

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

Besides learning the syntax and logic of coding itself, there are a lot of skills that go into programming that you may need while we're doing this. We've compiled a supplementary notebook about [Healthy Habits for Python coding](https://informatics.fas.harvard.edu/workshops/python-intensive/python-healthy-habits/) and we hope you'll read that to help you figure out how to proceed when you get stuck.

One of the best things to do while coding up more complex problems is to break them down into sub-problems. Let's do that here with our random walk program. Let's focus on just displaying an individual step of the walk. And let's make this a **pair programming exercise**: pair up with one (or more) people to complete this exericse.

> **Exercise:** Write a function called `display_walk` that takes a walk size and position argument and prints a string of dashes with an 'O' at the position. For example, `display_walk(size = 10, position = 3)` should print `---O------`. If the position is outside the walk size, it should print an 'X' at the end. For example, `display_walk(size = 10, position = 12)` should print `----------X`.
> 
> 1. Work together to write out pseudocode for this function. Make sure to check in on any potential logic errors. 
> 2. One person should write the code while the other person dictates out the pseudocode. 
> **Important** One line in your pseudocode could correspond to one line of code, but that may or may not be the case
> 3. For each line of code, **PAUSE** and both of you should check to make sure it matches the pseudocode.
> 
> You are allowed to use LLMs or the internet to look up how to do specific parts of your code, but try not to look up the entire solution. 


```python
# Your code here
```

??? success "Solution"
    ```python
    
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
# Test your function with these inputs
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

<pre class="output-block">X---------
O---------
-----O----
---------O
---------X
</pre>

Another important aspect of writing longer (or any) programs is code documentation and annotation. We cover this in our [healthy habits notebook](https://informatics.fas.harvard.edu/workshops/python-intensive/python-healthy-habits/), but you can expand the block below to see a brief example using the `display_walk` function. Here we've both annotated the individual lines of code with comments (denoted by `#`) and added a **docstring** to the function with `"""`. The docstring is what is read by Python's `help()` function, so now we can call `help()` on our own function! You can use LLMs to write your docstring. Usually they do pretty well.



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

<pre class="output-block">Help on function display_walk in module __main__:

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

<pre class="output-block">heads
</pre>

Write your code below. If you get stuck, check out your concept map, work with a neighbor, or review the topics we learned today. And of course, remember to use your debugging skills!

!!! Note
    If you are reading the completed solution to this exercise, you will notice extra code that **raise exceptions** in **try ... except** blocks. To learn more about how to use exceptions, check out our companion notebook [Python Healthy Habits](https://informatics.fas.harvard.edu/workshops/python-intensive/python-healthy-habits/) which covers some more advanced function writing. 


```python
# Your code here
```

??? success "Solution"
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

## Sample output:
# Starting random walk with boundary size: 10 and step size: 2
# -----O----
# -------O--
# -----O----
# -------O--
# ---------O
# -------O--
# -----O----
# -------O--
# ---------O
# ---------X
# Reached boundary!
```

<pre class="output-block">Starting random walk with boundary size: 10 and step size: 2
-----O----
-------O--
---------O
-------O--
-----O----
-------O--
---------O
-------O--
-----O----
-------O--
---------O
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

    /* Hide all 2nd-level navs */
    .md-nav--secondary .md-nav__item .md-nav {
        display: none !important;
    }

    /* Show when parent has .expanded class */
    .md-nav--secondary .md-nav__item.expanded > .md-nav {
        display: block !important;
    }
  

</style>

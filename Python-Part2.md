---
title: "[Workshop] Python intensive, part 2"
description: "Introduction to Python data structures, including lists and dictionaries, loops, libraries, and writing functions."
authors:
    - Gregg Thomas
    - Danielle Khost
---

# Python intensive, part 2

## Introduction

Welcome (back) to the Harvard Informatics Python workshop. This is part two of six, where we aim to give a whirlwind, yet thorough, introduction to programming concepts, the Python programming language, and how to use Python and some popular libaries to facilitate data analyses.

In the last part, we learned some foundational programming concepts and how they are implemented in Python. Specifically, we learned about:

1.   How computers need every single step given to them in order to complete a task with programming. This requires the programmer to conceptualize a problem at a high level, perhaps with **pseudocode**, and then break down that problem in every single step.
2.   Data can be stored and manipulated in a program by assigning it to an internal **variable** name with the assignment operator (`=`).
3.   **Functions** are blocks of code that perform a specific task and can be "looked up" from another program - like another recipe in a recipe book. Functions require input in the form of **arguments** and **return** output.
4.   **Operators** are functions that perform universal tasks, such as `+` for the addition of integers.
5.   Functions and operators may work on specific **data types**, such as **strings** or **integers**. It is important to remember what data type your function expects.
6.   **Boolean** (`True` or `False`) is a data type that allows programmers to express and evaluate complex logical statements. Booleans have operators that work on them, such as `and`, `or`, and `not`.

Today we will build on this by learning how to control the flow of a program based on the state of the data within it with **Conditional** (`if`, `elif`, `else`) statements and **Loops** (`while`, `for`). We'll also learn about **iterable data structures**, which will enhance what we can do with `for` loops.

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

Now, we've given the robot's location and we've said in step 1, only execute `Walk_anywhere()` **if** it isn't already at our oven. Now our robot knows not to bother looking up and running `Walk_anywhere()` in this case. We could change the location accordingly in the recipe and the robot would know whether or not it needed to `Walk_anywhere()`. For instance:

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

(Double click here to type your solution)

<details><summary>Solution</summary>

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

</details>

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

<pre class="output-block">The number is smaller than 10
Done.
</pre>

Here, we have set the value of `x` to be 5, then used the keyword `if` along with a logical expression (`x < 10`). Since the logical expression evaluates to `True`, the indented code block is executed.

Code blocks can be more than one line. After an **if statement** that returns `True`, every subsequent line that is indented one more level than the **if statement** itself will be executed.


```python
x = 5

if x < 10:
  print("Your number is", x)
  print("The number is smaller than 10")

print("Done.")
```

<pre class="output-block">Your number is 5
The number is smaller than 10
Done.
</pre>

This indentation syntax is required by Python, as that is how it knows which instructions to execute after an if statement. If the indentation is incorrect, you will see an error, such as the following:


```python
x = 5

if x < 10:
print("Your number is", x)
print("The number is smaller than 10")

print("Done.")
```

<pre class="output-block">  Cell In[3], line 4
    print("Your number is", x)
    ^
IndentationError: expected an indented block after 'if' statement on line 3
</pre>


```python
x = 5

if x < 10:
  print("Your number is", x)
    print("The number is smaller than 10")

print("Done.")
```

<pre class="output-block">  Cell In[4], line 5
    print("The number is smaller than 10")
    ^
IndentationError: unexpected indent
</pre>

In addition to syntax errors, which Python will catch, mis-placed indentation can also lead to **logic errors**, where the code will run, but with unexpected results.

Here, we will change the value of `x` so that the if statement is no longer `True`, but we will make a mistake with our indentation.


```python
x = 12

if x < 10:
  print("Your number is", x)
print("The number is smaller than 10")

print("Done.")
```

<pre class="output-block">The number is smaller than 10
Done.
</pre>

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

<pre class="output-block">  Cell In[6], line 3
    if x < 10
             ^
SyntaxError: expected ':'
</pre>

> **Exercise**: Pick a message and store it as a string. Print the message only if the string has at least 10 characters. This will require you to use the built-in `len()` function that we learned about before.


```python
# Your code here


print("Done.")
```

<pre class="output-block">Done.
</pre>

??? success "Solution"
    ```python
    my_msg = "the quick brown fox jumped over the lazy dog"
    my_msg_length = len(my_msg)
    
    if my_msg_length > 10:
      print("'", my_msg, "' has", my_msg_length, "characters.")
      print("This is more than 10 characters.")
    
    print("Done.")
    ```

    <pre class="output-block">' the quick brown fox jumped over the lazy dog ' has 44 characters.
    This is more than 10 characters.
    Done.
    </pre>

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

<pre class="output-block">Your number is 12
The number is equal to or larger than 10
Done.
</pre>

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

<pre class="output-block">  Cell In[10], line 5
    else:
    ^
SyntaxError: invalid syntax
</pre>

`else` will also not work on its own, because it has no logical expression to evaluate:


```python
x = 12

print("Your number is", x)

else:
  print("The number is equal to or larger than 10")

print("Done.")
```

<pre class="output-block">  Cell In[11], line 5
    else:
    ^
SyntaxError: invalid syntax
</pre>



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

<pre class="output-block">  Cell In[12], line 9
    else:
    ^
SyntaxError: invalid syntax
</pre>

??? success "Solution"
    ```python
    x = 12
    
    print("Your number is", x)
    
    if x < 10:
      print("The number is smaller than 10")
      print("You will have to find a larger number.") # Indented correctly
    else:
      print("The number is equal to or larger than 10")
    
    print("Done.")
    ```

    <pre class="output-block">Your number is 12
    The number is equal to or larger than 10
    Done.
    </pre>

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

<pre class="output-block">Your number is 12
The number is larger than 10 but smaller than 20
Done.
</pre>

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

<pre class="output-block">Your number is 16
The number is larger than 15 but smaller than 20
Done.
</pre>

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

<pre class="output-block">The temperature is 72 degrees Fahrenheit and the weather is rainy.
Wear a raincoat and boots.
</pre>

Here, our very basic weather bot checks a couple of conditions based on the temperature and precipiation and gives clothing recommendations. Obviously, there are many more combinations of temperature and weather we could test.

> **Exercise**: Add another `elif` statement that checks any other combination of conditions and gives a recommendation. Change the temperature and weather so these new conditions are met.


```python
temperature = 72
weather = "rainy"

print("The temperature is", temperature, "degrees Fahrenheit and the weather is", weather + ".")

if temperature <= 32 and weather == "snowy":
  print("Wear a heavy coat and snow boots.")
elif temperature > 32 and weather == "rainy":
  print("Wear a raincoat and boots.")

# Add your elif here


else:
  print("Your guess is as good as mine!")
```

<pre class="output-block">The temperature is 72 degrees Fahrenheit and the weather is rainy.
Wear a raincoat and boots.
</pre>

??? success "Solution"
    ```python
    temperature = 72
    weather = "sunny"
    
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

    <pre class="output-block">The temperature is 72 degrees Fahrenheit and the weather is sunny.
    Wear shorts and a t-shirt.
    </pre>

> **Exercise**: Initialize two integer variables called `x` and `y`, give them whatever values you like. Write a series of conditional statements that check the following:
> 1. `x` and `y` are both even
> 2. one is even and the other isn't
> 3. `x` and `y` are both odd
>
> *Hint: If a number is even and you divide it by 2, what will the remainder be? Which operator returns the remainder of a division?*


```python
# Your code here
```

??? success "Solution"
    ```python
    x = 5
    y = 8
    
    if x % 2 == 0 and y % 2 == 0:
        print("x and y are both even")
    elif (x % 2 == 0 and y % 2 != 0) or (x % 2 != 0 and y % 2 == 0):
        print("one of the numbers is even, one of the numbers is odd")
    elif x % 2 != 0 and y % 2 != 0:
        print("x and y are both odd")
    ```

    <pre class="output-block">one of the numbers is even, one of the numbers is odd
    </pre>

---

Recall also the `in` operator for strings. You can use it to check if one string is contained within the other. It will return `True` if it is and `False` if it isn't:


```python
my_string = "1234"
print("2" in my_string)
```

<pre class="output-block">True
</pre>

Since this returns a boolean value (`True` or `False`), it can also be used when checking conditions with `if` or `elif`:


```python
my_string = "1234"

if "2" in my_string:
  print("In the if statement.")
else:
  print("In the else statement.")

print("Done.")
```

<pre class="output-block">In the if statement.
Done.
</pre>

Likewise, the `not` operator can be used to negate a logical condition in `if` statements:


```python
my_string = "1234"

if not "2" in my_string:
  print("In the if statement.")
else:
  print("In the else statement.")

print("Done.")
```

<pre class="output-block">In the else statement.
Done.
</pre>

> **Exercise:** Store a string (`my_string`) and store two other smaller strings (`my_substr1`, `my_substr2`). Then use a series of `if` and `elif` statements to:

*   Print a message indicating if both sub-strings are contained within `my_string`
*   Otherwise, print a message if only one of the sub-strings is contained within `my_string`. The message should indicate which sub-string was found, so you will need two `elif`s.
*   Finally, use an `else` statement to print a different string if neither sub-string is contained within `my_string`


```python
# Your code here: Pick your string and sub-strings

# Your code here: Fill in the conditional statements
if : # An if statement if both sub-strings are found
  print("Both substrings found:", my_substr1, ",", my_substr2)
elif : # An elif statement if only sub-string 1 is found
  print("Substring 1 found:", my_substr1)
elif : # An elif statement if only sub-string 2 is found
  print("Substring 2 found:", my_substr2)
else: # Else handles if neither sub-strings are found
  print("Neither substring found.")

print("Done.")
```

<pre class="output-block">  Cell In[24], line 4
    if : # An if statement if both sub-strings are found
       ^
SyntaxError: invalid syntax
</pre>

??? success "Solution"
    ```python
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

    <pre class="output-block">Substring 1 found: fire nation
    Done.
    </pre>

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

<pre class="output-block">Go
</pre>

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

<pre class="output-block">Go
</pre>

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

<pre class="output-block">The temperature is 72 degrees Fahrenheit and the weather is rainy.
Wear a raincoat and boots.
</pre>

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

<pre class="output-block">The temperature is 72 degrees Fahrenheit and the weather is precipitating.
Your guess is as good as mine!
</pre>

??? success "Solution"
    ```python
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

    <pre class="output-block">The temperature is 72 degrees Fahrenheit and the weather is precipitating.
    Wear a light raincoat and rain shoes.
    Leave your umbrella at home.
    </pre>

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

<pre class="output-block">0
1
2
3
4
Done.
</pre>

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

while x < 5:
  print(x)
  x = x + 1

print("Done.")
```

<pre class="output-block">0
1
2
3
4
Done.
</pre>

??? success "Solution"
    ```python
    x = 0
    
    while x <= 5: # Change condition to <=
      print(x)
      x = x + 1
    
    print("Done.")
    ```

    <pre class="output-block">0
    1
    2
    3
    4
    5
    Done.
    </pre>

??? success "Solution"
    ```python
    x = 0
    
    while x < 5:
      print(x)
      x = x + 1
    
    print(x) # x remains in the program's memory as its last value in the loop, so print x after the loop
    print("Done.")
    ```

    <pre class="output-block">0
    1
    2
    3
    4
    5
    Done.
    </pre>

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
  x = x + 1

print("Done.")
```

<pre class="output-block">0
1
2
3
4
Done.
</pre>

??? success "Solution"
    ```python
    x = 0
    
    while x < 5:
      print(x)
      x += 1
    
    print("Done.")
    ```

    <pre class="output-block">0
    1
    2
    3
    4
    Done.
    </pre>

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

```

??? success "Solution"
    ```python
    x = 10
    
    while x <= 20:
      print(x)
      #x = x + 1
      x = x + 2 # Bonus solution
    print("Done.")
    ```

    <pre class="output-block">10
    12
    14
    16
    18
    20
    Done.
    </pre>

> **Exercise**: For a colony with an initial population size of 1, write a program that prints out the population size for 10 generations given that it doubles every generation.
>
> *Hint: You will need to initialize two variables and then use a `while` loop to update them.*


```python
# Your code here: calculate the population size of a colony over 10 generations that
# doubles in size every generation.
```

??? success "Solution"
    ```python
    generation = 1
    pop_size = 1
    
    while generation <= 10:
      print("Population size in generation", generation, "is:", pop_size)
      pop_size *= 2
      generation += 1
    ```

    <pre class="output-block">Population size in generation 1 is: 1
    Population size in generation 2 is: 2
    Population size in generation 3 is: 4
    Population size in generation 4 is: 8
    Population size in generation 5 is: 16
    Population size in generation 6 is: 32
    Population size in generation 7 is: 64
    Population size in generation 8 is: 128
    Population size in generation 9 is: 256
    Population size in generation 10 is: 512
    </pre>

#### `for` loops

`while` loops work by repeating a set of instructions (i.e. a block of code) until some condition is met.

`for` loops, on the other hand, work by taking a group of inputs and performing a set of instructions on them one at a time. The key concept here is the **group of multiple inputs**, which leads into **data structures**. Up until now, every piece of code we've run has used single pieces of data. `x = 5` is a single integer. `my_string = "Hello world!"` is a single string. `for` loops work by taking **lists** of integers or strings, or lines in a file, and performing actions on each one individually.

More on that in a bit. For now, we can demonstrate `for` loops with **strings**. This is because **strings are essentially a group of characters**. This means we can use a `for` loop to iterate over each character individually. In other words, strings are **iterable**.

Here is how a `for` loop would work to print out every character in a string:


```python
my_string = "Hello world!"

for current_character in my_string:
  print(current_character)
```

<pre class="output-block">H
e
l
l
o
 
w
o
r
l
d
!
</pre>

We start by defining a string. Then we encounter the `for` line where the first thing we see after `for` is a new variable, `current_character`. This is the **loop** or **update** variable. It's name, like other variables, is determind by the programmer, so we could have called it something else: `cur_char`, `current_letter`, `akjhgak`. It's purpose is to be used only within the loop, and its value is assigned based on the current iteration of the loop. Then, after that iteration it is **automatically updated** to be the next object in the string (or other **iterable**) that we're looping over. For a string, each object is an individual character, so the result of the loop is one character being printed per line of output.

After the loop variable we see the keyword **`in`**. We talked about `in` before as the **inclusion operator**. Here, confusingly, it acts somewhat differently, simply as a keyword to denote that the loop variable on the left will take on values according to the iterable on the right.

Then, we have our string, `my_string`, which is the thing over which we are iterating.

Again, syntactically, the colon `:` and indenation are required.

> **Exercise**: Are infinite loops possible when using `for`?

> **Exercise**: Use a `for` loop to calculate the length of a string without using the `len()` function.


```python
# Your code here: replicate the functionality of the len() function
```

??? success "Solution"
    ```python
    my_string = "Hello world!"
    char_tally = 0
    
    for char in my_string:
      char_tally += 1
    
    print(char_tally)
    print(len(my_string))
    ```

    <pre class="output-block">12
    12
    </pre>

We will cover `for` loops much more when we learn about other **iterable** data structures.

### Review of loops

We've learned about the two types of loops in Python `while` and `for`. Loops are used for the most important and useful computational purposes: automatic repetition of tasks.

1.   `while` loops, like `if` statements run a block of code depending on a condition. However, they repeat that block of code until the condition is no longer met.
2.   `for` loops repeat blocks of code for different inputs given in an **iterable**.
3. In Python, indentation defines code blocks for loops (and conditional statements). If your line of code isn't indented at the same level of the loop, it will not be evaluated in the loop. Sometimes this can cause errors, and sometimes the program will run but with undesired output. It's up to the programmer to catch this.



## Iterables

`for` loops work by performing a set of instructions (block of code) on every item in a **sequence of items**. We talked about looping over the characters in a string:


```python
my_string = "Hello!"

for current_character in my_string:
  print(current_character)
```

<pre class="output-block">H
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

<pre class="output-block">---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[45], line 1
----> 1 for x in 1048:
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

<pre class="output-block">l
---
h
</pre>

Strings can also be indexed in reverse by providing a negative index:


```python
my_string = "hello world!"
print(my_string[-2])
```

<pre class="output-block">d
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

<pre class="output-block">0 h
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

We learned about the `len()` function in Part 1. It takes as input a string argument and returns the number of characters in that string.

`range()` is another function that returns **an object containing the indices**. The `for` loop directly takes that object and loops over it, assigning `cur_index` the value of the index for the current iteration of the loop. Inside the loop, we've printed out both the index and the corresponding character in the string using string indexing with `[]`.

> **Exercise**: Store a string in a variable. Print out the characters of the string in reverse. No palindromes allowed! This will require you to use a `for` loop and reverse indexing.
>
> **BONUS**: Instead of printing each character out in reverse one at a time, print the whole string in reverse at once. *Hint: remember the string concatenation operator `+`*.


```python
# Your code here: reverse a string

```

??? success "Solution"
    ```python
    my_string = "stressed"
    my_rev_string = "" # For bonus
    
    for str_ind in range(len(my_string)):
      rev_ind = str_ind + 1
      rev_char = my_string[-rev_ind]
      my_rev_string += rev_char # For bonus
      print(rev_char)
    
    print(my_rev_string) # For bonus
    ```

    <pre class="output-block">d
    e
    s
    s
    e
    r
    t
    s
    desserts
    </pre>

??? success "Solution"
    ```python
    my_string = "stressed"
    my_rev_string = ""
    
    for char in my_string:
      my_rev_string = char + my_rev_string
    print(my_rev_string)
    ```

    <pre class="output-block">desserts
    </pre>

### Slicing strings

In addition to indexing to retrieve one character from a string at a time, you can also **slice** strings to get chunks of them.

Slicing is again done by giving the name of the string followed by square brackets `[]`. But this time, instead of a single number in the brackets, you provide two numbers, a start index and an end index, separated by a colon `:`.

For example, to get the 2nd to 5th characters from a string:


```python
my_string = "hello_world!"
print(my_string[1:6])
```

<pre class="output-block">ello_
</pre>

Remember, Python strings are **0-based indexed**, so to get the second character, you give the index `1`.

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

<pre class="output-block">hello_
lo_world!
el_
</pre>

String slicing also works in reverse with negative indices:


```python
print(my_string[:-3])   # Gets every character from the beginning to the third from last
print(my_string[2:-4])  # Gets every character from the 3rd to the 4th from last
```

<pre class="output-block">hello_wor
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

> **Exercise**: *CODE GOLF*. Using what we've learned about slicing, reduce the below code to 2 lines. This is tricky, *but should only take one line of code to do using slicing* (and then possibly another line to print the result). Remember the shortcuts for the beginning and end of strings and the negative steps to go backwards when slicing.


```python
# Your code here: reverse a string with slicing only
my_string = "stressed"
my_rev_string = ""

for char in my_string:
  my_rev_string = char + my_rev_string
print(my_rev_string)
```

<pre class="output-block">desserts
</pre>

??? success "Solution"
    ```python
    my_string = "stressed"
    print(my_string[::-1])
    ```

    <pre class="output-block">desserts
    </pre>

### Strings are immutable

An important note. Though we can access individual characters within a string with **indexing**, we cannot change individual parts of a string. In other words, strings are **immutable**.


```python
my_string = "hello_world!"
print(my_string[1])
my_string[1] = "a" # This is not permitted because strings are immutable!
```

<pre class="output-block">e
</pre>

<pre class="output-block">---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[58], line 3
      1 my_string = "hello_world!"
      2 print(my_string[1])
----> 3 my_string[1] = "a" # This is not permitted because strings are immutable!

TypeError: 'str' object does not support item assignment
</pre>

So, strings are **iterable** but **immutable**.

### Indirection, part 2

If you recall, we introduced the concept of indirection in Part 1. **Indirection** occurs when you use one object to reference another one, rather than using the object directly:


```python
x = 5
abs(x) # Here we are using the variable x to reference the value 5, rather than using the value directly
```

<pre class="output-block">5
</pre>

With the introduction of iterables and indexing, you may begin to see how complicated this can get:


```python
my_string = "12345"
my_index = 4

print(my_string[my_index])
```

<pre class="output-block">5
</pre>

Here are two levels of indirection: the string itself and the index of the character we're accessing.

> **Exercise**: *CODE GOLF*. Re-write the code to be only one line and produce the same result. This will require removing all indirection.


```python
my_string = "12345"
my_index = 4

print(my_string[my_index])
```

<pre class="output-block">5
</pre>

??? success "Solution"
    ```python
    print("12345"[4])
    ```

    <pre class="output-block">5
    </pre>

While this code without indirection is very succinct and efficient, it is also very inflexible. This works for one case and one case only. If we want to access the first character of the string, or index a different string, we'd have to write additional code. These trade-offs will become more obvious as we introduce more data structures. And we'll re-visit indirection again!

#### The `range()` function

We often use the range function in our `for` loop definitions with a certain level of indirection that can be confusing (`range(len())`), so I wanted to spend a second to explain it a bit more. `range()` takes as input an integer and returns a special **range object**.


```python
range(10)
```

<pre class="output-block">range(0, 10)
</pre>

This object specifies a start, stop, and (optionally) a step for a range, and can be looped over. The above, `range(0, 10)` object means that the range starts from 0 and goes to 10 (non-inclusive) with a step of 1 (the default). This is especially helpful for looping over objects by index! `range()` does NOT work on strings or other data types:


```python
range("hello") # This will fail because the range function expects an integer, not a string
```

<pre class="output-block">---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[64], line 1
----> 1 range("hello") # This will fail because the range function expects an integer, not a string

TypeError: 'str' object cannot be interpreted as an integer
</pre>

This is why you will almost always see this paired with `len()` in `for` loops:


```python
my_string = "hello world!"

print(range(len(my_string)))

for string_index in range(len(my_string)):
  print(string_index, my_string[string_index])
```

<pre class="output-block">range(0, 12)
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

We will use this `range(len())` pairing often for other iterables as well.

### Lists

Up to now, we've dealt with individual data types, **integers** and **strings**. However, to really scale up the power of our programming in order to manipulate and analyze a lot of data, we'll want to group lots of strings and/or integers together and perform operations on them in a loop or all at once. For this, programming languages typically have higher-order **data structures** in which individual instances of other data types can be stored, organized, and accessed.

For Python, the most adaptable data structure is the **list**. Lists are exactly what they sound like they are: lists of other objects, grouped together in a single object.

#### List properties

*   Lists are **iterable**, meaning we can use a `for` loop to go over each individual item one at a time and perform computations.
*   Lists are **indexed** which means, like strings, individual elements of a list can be accessed by an integer value based on their ordering in the list. Lists can also be **sliced** by index like strings.
*   Lists are **mutable**, unlike strings, meaning that they can be changed by index on the fly. But be careful doing this while looping over the list! This can have unexpected consequences.
*   Lists can contain mixed data types.

Lists are defined, confusingly, also with square brackets `[]`, and individual items in the list are separated by a comma `,`. Lists can be indexed and sliced just like strings.


```python
my_list = [1, 2, 3, 4, 5]
print(my_list)
print(my_list[1])

print("---")

my_list2 = ["hello", -12, "world", 985, "adshgadk"]
print(my_list2[2])
print(my_list2[::-1])
```

<pre class="output-block">[1, 2, 3, 4, 5]
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

# Initialize these variables with sensible values
list_tally = 
list_sum = 
list_max = 
list_min = 

# Your code here

# Print out the results
print("There are", list_tally, "numbers in the list.")
print("The largest number is:", list_max)
print("The smallest number is:", list_min)
print("The sum of all the numbers is:", list_sum)
print("The average of the numbers is:", list_avg)
```

<pre class="output-block">  Cell In[67], line 4
    list_tally =
                 ^
SyntaxError: invalid syntax
</pre>

??? success "Solution"
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

    <pre class="output-block">There are 5 numbers in the list.
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

<pre class="output-block">5
5
1
15
</pre>

Sorry! But you can see here why functions are so nice. We've compacted all that code down to four lines.

Notice that there is no built-in mean() function. There are external libraries that have mean() functions, but more on those later.

> **Exercise**: Calculate the average of your list using the functions provided above. This should only require one line of code (and potentially a `print()` statement).


```python
# Your code here
```

??? success "Solution"
    ```python
    print(sum(my_list) / len(my_list))
    ```

    <pre class="output-block">3.0
    </pre>

Also, recall lists can contain **mixed data types**. Again, remembering your data types is important because some functions may expect a list with only integers, or a list with only strings.


```python
my_mixed_list = [1, 2, "hello", 3, 4, 5]
print(sum(my_mixed_list))
```

<pre class="output-block">---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[72], line 2
      1 my_mixed_list = [1, 2, "hello", 3, 4, 5]
----> 2 print(sum(my_mixed_list))

TypeError: unsupported operand type(s) for +: 'int' and 'str'
</pre>

Internally, `sum()` is probably doing exactly what we did above with the `for` loop, adding each number in the list to a variable with `+=`. However, when it comes to the third element of the list, `"hello"`, it is trying to add a string to an integer and we run into a data type error for the `+` operator.

#### List inclusion with `in`

As with **strings** and other **iterables**, the `in` operator works on lists:


```python
my_string_list = ["with", "cat", "like", "tread"]
print("cat" in my_string_list)
```

<pre class="output-block">True
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
```

??? success "Solution"
    ```python
    beach_tourists=["Alice","Mason","Emma","Liam","Olivia","Walden","Ethan","Sophia","Oliver","Ava","Mia","William","Logan","Lucas","Charlotte","Amelia","Harper","James"]
    music_festival_attendees=["Jackson","Sophia","Aiden","Isabella","Lucas","Noah","Levi","Benjamin","Elijah","Mason","Elena","Eliana","Mateo","Jack","Luna","Eleanor","Ezra","Willow","Henry"]
    history_class_students=["Emily","James","Wally","Ella","Jacob","Amelia","Michael","Evelyn","Alexander","Avery","Mila","Aria","Ella","Layla","Scarlett","Grace","Wyatt","Ellie","Paisley","Daniel"]
    office_building_employees=["Walter","Charlotte","Alexander","Scarlett","Michael","Victoria","Samuel","Aubrey","Olive","Nathan","Camila","Gabriel","Isaac","Waldo","Savannah","Gabriella","Nora","Chloe","Zoe","Stella","Riley"]
    marathon_participants=["Daniel","Harper","Henry","Grace","Sebastian","Hannah","Victoria","Archer","Aurora","Brooklyn","Parker","Elias","Adeline","Julia","David","Liam","Josie","Carter","Jaxon"]
    
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

    <pre class="output-block">Waldo is at the office!
    </pre>

#### List concatenation with `+`

Just like with strings, the concatenation `+` operator works on lists to combine them:


```python
my_list1 = [1,2,3]
my_list2 = [4,5,6]

print(my_list1 + my_list2)
```

<pre class="output-block">[1, 2, 3, 4, 5, 6]
</pre>

> **Exercise**: Use list concatenation with `+` to more succinctly determine if Waldo is at one of the locations above. Note that we won't be able to tell *which* location he is in with this method.


```python
beach_tourists=["Alice","Mason","Emma","Liam","Olivia","Walden","Ethan","Sophia","Oliver","Ava","Mia","William","Logan","Lucas","Charlotte","Amelia","Harper","James"]
music_festival_attendees=["Jackson","Sophia","Aiden","Isabella","Lucas","Noah","Levi","Benjamin","Elijah","Mason","Elena","Eliana","Mateo","Jack","Luna","Eleanor","Ezra","Willow","Henry"]
history_class_students=["Emily","James","Wally","Ella","Jacob","Amelia","Michael","Evelyn","Alexander","Avery","Mila","Aria","Ella","Layla","Scarlett","Grace","Wyatt","Ellie","Paisley","Daniel"]
office_building_employees=["Walter","Charlotte","Alexander","Scarlett","Michael","Victoria","Samuel","Aubrey","Olive","Nathan","Camila","Gabriel","Isaac","Waldo","Savannah","Gabriella","Nora","Chloe","Zoe","Stella","Riley"]
marathon_participants=["Daniel","Harper","Henry","Grace","Sebastian","Hannah","Victoria","Archer","Aurora","Brooklyn","Parker","Elias","Adeline","Julia","David","Liam","Josie","Carter","Jaxon"]

# Your code here to concatenate lists and check if Waldo is in any
```

??? success "Solution"
    ```python
    beach_tourists=["Alice","Mason","Emma","Liam","Olivia","Walden","Ethan","Sophia","Oliver","Ava","Mia","William","Logan","Lucas","Charlotte","Amelia","Harper","James"]
    music_festival_attendees=["Jackson","Sophia","Aiden","Isabella","Lucas","Noah","Levi","Benjamin","Elijah","Mason","Elena","Eliana","Mateo","Jack","Luna","Eleanor","Ezra","Willow","Henry"]
    history_class_students=["Emily","James","Wally","Ella","Jacob","Amelia","Michael","Evelyn","Alexander","Avery","Mila","Aria","Ella","Layla","Scarlett","Grace","Wyatt","Ellie","Paisley","Daniel"]
    office_building_employees=["Walter","Charlotte","Alexander","Scarlett","Michael","Victoria","Samuel","Aubrey","Olive","Nathan","Camila","Gabriel","Isaac","Waldo","Savannah","Gabriella","Nora","Chloe","Zoe","Stella","Riley"]
    marathon_participants=["Daniel","Harper","Henry","Grace","Sebastian","Hannah","Victoria","Archer","Aurora","Brooklyn","Parker","Elias","Adeline","Julia","David","Liam","Josie","Carter","Jaxon"]
    
    all_names = beach_tourists + music_festival_attendees + history_class_students + office_building_employees + marathon_participants
    
    if "Waldo" in all_names:
      print("Waldo is in one of these locations!")
    else:
      print("Waldo is NOT in any of these locations!")
    ```

    <pre class="output-block">Waldo is in one of these locations!
    </pre>

While this is a much shorter bit of code, it is telling us less specific information.

#### Nested lists

Lists are an extremely open and flexible data structure. They can contain any type of data, mixed data types, and even other data structures, including other lists! In other words, you can have a list of lists, or a **nested list**:


```python
list_of_lists = [ [1,2,3], [4,5,6] ]
print(list_of_lists)
print("---")

# OR, with a bit of indirection #

my_list1 = [1,2,3]
my_list2 = [4,5,6]

list_of_lists = [ my_list1, my_list2 ]
print(list_of_lists)
```

<pre class="output-block">[[1, 2, 3], [4, 5, 6]]
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

<pre class="output-block">1
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
```

??? success "Solution"
    ```python
    beach_tourists=["Alice","Mason","Emma","Liam","Olivia","Walden","Ethan","Sophia","Oliver","Ava","Mia","William","Logan","Lucas","Charlotte","Amelia","Harper","James"]
    music_festival_attendees=["Jackson","Sophia","Aiden","Isabella","Lucas","Noah","Levi","Benjamin","Elijah","Mason","Elena","Eliana","Mateo","Jack","Luna","Eleanor","Ezra","Willow","Henry"]
    history_class_students=["Emily","James","Wally","Ella","Jacob","Amelia","Michael","Evelyn","Alexander","Avery","Mila","Aria","Ella","Layla","Scarlett","Grace","Wyatt","Ellie","Paisley","Daniel"]
    office_building_employees=["Walter","Charlotte","Alexander","Scarlett","Michael","Victoria","Samuel","Aubrey","Olive","Nathan","Camila","Gabriel","Isaac","Waldo","Savannah","Gabriella","Nora","Chloe","Zoe","Stella","Riley"]
    marathon_participants=["Daniel","Harper","Henry","Grace","Sebastian","Hannah","Victoria","Archer","Aurora","Brooklyn","Parker","Elias","Adeline","Julia","David","Liam","Josie","Carter","Jaxon"]
    
    all_names = [ beach_tourists, music_festival_attendees, history_class_students, office_building_employees, marathon_participants ]
    waldo_found = False
    
    for location_list in all_names:
      if "Waldo" in location_list:
        print("Waldo is in one of these locations!")
        waldo_found = True
    
    if not waldo_found:
      print("Waldo is NOT in any of these locations!")
    ```

    <pre class="output-block">Waldo is in one of these locations!
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

<pre class="output-block">All lists:                            [[1, 2, 3], [4, 5, 6]]
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

<pre class="output-block">All lists:                            [[1, 2, 3], [4, 5, 6]]
The second list:                      [4, 5, 6]
The third element of the second list: 6
</pre>

All of this involves more confusing indirection for indexing. For instance, when we do:


```python
my_list1 = [1,2,3]
my_list2 = [4,5,6]

list_of_lists = [ my_list1, my_list2 ]
print("The third element of the second list:", list_of_lists[1][2])
```

<pre class="output-block">The third element of the second list: 6
</pre>

We could equivalently type:


```python
print("The third element of the second list:", [ [1,2,3], [4,5,6] ][1][2])
```

<pre class="output-block">The third element of the second list: 6
</pre>

So while indirection can obfuscate some aspects of the code, you can also see how in a way they make it more readable.

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

<pre class="output-block">[1, 2, 3]
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
beach_tourists=["Alice","Mason","Emma","Liam","Olivia","Walden","Ethan","Sophia","Oliver","Ava","Mia","William","Logan","Lucas","Charlotte","Amelia","Harper","James"]
music_festival_attendees=["Jackson","Sophia","Aiden","Isabella","Lucas","Noah","Levi","Benjamin","Elijah","Mason","Elena","Eliana","Mateo","Jack","Luna","Eleanor","Ezra","Willow","Henry"]
history_class_students=["Emily","James","Wally","Ella","Jacob","Amelia","Michael","Evelyn","Alexander","Avery","Mila","Aria","Ella","Layla","Scarlett","Grace","Wyatt","Ellie","Paisley","Daniel"]
office_building_employees=["Walter","Charlotte","Alexander","Scarlett","Michael","Victoria","Samuel","Aubrey","Olive","Nathan","Camila","Gabriel","Isaac","Waldo","Savannah","Gabriella","Nora","Chloe","Zoe","Stella","Riley"]
marathon_participants=["Daniel","Harper","Henry","Grace","Sebastian","Hannah","Victoria","Archer","Aurora","Brooklyn","Parker","Elias","Adeline","Julia","David","Liam","Josie","Carter","Jaxon"]

all_names = [ beach_tourists, music_festival_attendees, history_class_students, office_building_employees, marathon_participants ]

## Your code here to find the index of Waldo's name
```

??? success "Solution"
    ```python
    beach_tourists=["Alice","Mason","Emma","Liam","Olivia","Walden","Ethan","Sophia","Oliver","Ava","Mia","William","Logan","Lucas","Charlotte","Amelia","Harper","James"]
    music_festival_attendees=["Jackson","Sophia","Aiden","Isabella","Lucas","Noah","Levi","Benjamin","Elijah","Mason","Elena","Eliana","Mateo","Jack","Luna","Eleanor","Ezra","Willow","Henry"]
    history_class_students=["Emily","James","Wally","Ella","Jacob","Amelia","Michael","Evelyn","Alexander","Avery","Mila","Aria","Ella","Layla","Scarlett","Grace","Wyatt","Ellie","Paisley","Daniel"]
    office_building_employees=["Walter","Charlotte","Alexander","Scarlett","Michael","Victoria","Samuel","Aubrey","Olive","Nathan","Camila","Gabriel","Isaac","Waldo","Savannah","Gabriella","Nora","Chloe","Zoe","Stella","Riley"]
    marathon_participants=["Daniel","Harper","Henry","Grace","Sebastian","Hannah","Victoria","Archer","Aurora","Brooklyn","Parker","Elias","Adeline","Julia","David","Liam","Josie","Carter","Jaxon"]
    
    all_names = [ beach_tourists, music_festival_attendees, history_class_students, office_building_employees, marathon_participants ]
    
    for location_list in all_names:
      for name_index in range(len(location_list)):
        if location_list[name_index] == "Waldo":
          print("Waldo's index in one of the lists is:", name_index, "!")
    
        # Bonus solution
        if "Wal" in location_list[name_index]:
          print("A name starting with 'Wal' is at index", name_index, "in one of the lists!")
    ```

    <pre class="output-block">A name starting with 'Wal' is at index 5 in one of the lists!
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

<pre class="output-block">unsorted: [5, 8, 3, 6, 1]
sorted: [1, 3, 5, 6, 8]
</pre>

What else do you notice about this that is different about using a function?

In this case, the method works **in place**. That means that it modifies the object directly, rather than returning a new object.

There are also methods that **return** objects. Unfortunately, there is no obvious way to tell which methods work in place and which return objects.

Functions can operate **in place**, **return** objects, or both. 

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

<pre class="output-block">unsorted: [5, 8, 3, 6, 1]
original still unsorted: [5, 8, 3, 6, 1]
sorted new list: [1, 3, 5, 6, 8]
---
in place method doesn't return anything: None
but we've still sorted the original list: [1, 3, 5, 6, 8]
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

<pre class="output-block">unsorted: [5, 8, 3, 6, 1]
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

<pre class="output-block">original: [1, 2, 3, 4]
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

<pre class="output-block">original: [1, 2, 3, 4, 5]
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

print("The list is", len(my_list), "elements long and the number", to_remove, "appears", my_list.count(to_remove), "times.")
```

<pre class="output-block">The list is 20 elements long and the number 10 appears 7 times.
The list is 20 elements long and the number 10 appears 7 times.
</pre>

??? success "Solution"
    ```python
    my_list = [4, 10, 22, 15, 10, 8, 10, 37, 12, 10, 19, 10, 5, 27, 18, 10, 30, 7, 10, 14]
    to_remove = 10
    print("The list is", len(my_list), "elements long and the number", to_remove, "appears", my_list.count(to_remove), "times.")
    
    while to_remove in my_list:
      my_list.remove(to_remove)
    
    print("The list is", len(my_list), "elements long and the number", to_remove, "appears", my_list.count(to_remove), "times.")
    ```

    <pre class="output-block">The list is 20 elements long and the number 10 appears 7 times.
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
my_index = my_list.index(2, 2) # Find the first occurrence of 2, starting from index 2
print(my_index)
```

<pre class="output-block">1
---
4
</pre>

3.   `.pop([i])` : Removes and returns the element at index `i` from the list. Note that the argument `i` is given in square brackets. This means that it is optional. If no index is given, `.pop` removes and returns the last element in the list. This function both modifies the list **in place** and **returns** an object.



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

<pre class="output-block">original: [1, 2, 3, 4, 5, 6]
modified: [1, 3, 4, 5, 6]
the element it removed: 2
---
modified again: [1, 3, 4, 5]
the last element from the list: 6
</pre>

#### List method BONUS exercise

> **BONUS Exercise**: Use what we've learned about lists to move Waldo from his current location to `beach_tourists`.


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

# Write your code above to move Waldo

# Check and print if Waldo is at the beach after the move
if "Waldo" in beach_tourists:
    print("Waldo is now at the beach.")
else:
    print("Waldo is not yet at the beach.")
```

<pre class="output-block">Waldo is not at the beach.
Waldo is not yet at the beach.
</pre>

??? success "Solution"
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
    
    # Check and print if Waldo is at the beach after the move
    if "Waldo" in beach_tourists:
        print("Waldo is now at the beach.")
    else:
        print("Waldo is not yet at the beach.")
    ```

    <pre class="output-block">Waldo is not at the beach.
    Waldo found in one of the locations. Moving him to the beach.
    Waldo is now at the beach.
    </pre>

There are many ways to do this. However, they all have some problems. For instance, as we've mentioned, we have no way of knowing *which* location Waldo was in initially. This and other organizational tasks is what our next iterable data structure, **dictionaries**, try to solve.

#### Indirection, part 3

Before we move to dictionaries, lets do another code golf exercise.

> **Exercise**: *CODE GOLF*. Re-write the code block below such that, other than the initializations of the lists, only one line of code is used. However, you must still reference each of the three lists.


```python
a = ["nope", "nope", "nope", "correct!", "nah"]
b = [3, 0, 2, 4, 1]
c = [3, 2, 4, 0, 5]

num_from_c = c[3]
num_from_b = b[num_from_c]
answer = a[num_from_b]

print("The answer is:", answer)
```

<pre class="output-block">The answer is: correct!
</pre>

??? success "Solution"
    ```python
    a = ["nope", "nope", "nope", "correct!", "nah"]
    b = [3, 0, 2, 4, 1]
    c = [3, 2, 4, 0, 5]
    
    print("The answer is:", a[b[c[3]]])
    ```

    <pre class="output-block">The answer is: correct!
    </pre>

### Dictionaries

While lists are flexible and intuitive and useful in many cases, one of their main drawbacks is in accessing specific parts of the data. To look up and use a particular list element (e.g. the name "Waldo"), you have to know that element's position(s) within the list, or its **index**. An element's index may not always be easily knowable, especially for large datasets or data that has been generated or parsed programmatically.

**Dictionaries** solve this by associating two pieces of information together, allowing you to label your data and look it up by name. The term for this is a **key-value pairing**. The **key** being the data's label or name, and the **value** being the data itself.

In Python, dictionaries are declared using curly brackets `{}`, inside of which are different key-value pairs, with the keys and values separated by colons `:` and the pairs separated by commas `,` (just like list elements):


```python
my_dictionary = { 'key1' : 1, 'key2' : 3, 'key3' : 6 }
print(my_dictionary)
```

<pre class="output-block">{'key1': 1, 'key2': 3, 'key3': 6}
</pre>

In this example, the keys are strings and the values are integers. The string `'key1'` is associated with the value `1` and so forth.

Then, individual data values can be accessed directly by their key! This is done using square brackets `[]`, just like when indexing a string or a list, but inside of the brackets instead of an index, you put the key:


```python
my_dictionary = { 'key1' : 1, 'key2' : 3, 'key3' : 6 }
print("The value of key 'key2' is:", my_dictionary['key2'])
```

<pre class="output-block">The value of key 'key2' is: 3
</pre>

#### Keys

Importantly, **keys themselves can be any immutable data type or structure** and **can even be mixed data types**:


```python
my_dictionary = { 123 : 1, 'key2' : 3, 7 : 6 }
print("The value of key 123 is:", my_dictionary[123])
print("The value of key 'key2' is:", my_dictionary['key2'])
print("The value of key 7 is:", my_dictionary[7])
```

<pre class="output-block">The value of key 123 is: 1
The value of key 'key2' is: 3
The value of key 7 is: 6
</pre>

If you try to assign a mutable object, like a list as a key, you will get an error:


```python
my_incorrect_dictionary = { ['key1'] : 1, 'key2' : 3, 'key3' : 6 }
```

<pre class="output-block">---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[106], line 1
----> 1 my_incorrect_dictionary = { ['key1'] : 1, 'key2' : 3, 'key3' : 6 }

TypeError: unhashable type: 'list'
</pre>

Above, we've just added square brackets `[]` to `'key1'` to make it a single element list, however this isn't allowed for dictionary keys.

Also importantly, **keys must be unique**. If multiple identical keys exist and you try to look up that key, only one of the values of that key will be returned:


```python
my_incorrect_dictionary = { 'key1' : 1, 'key1': 2, 'key3' : 6}
print("The value of key 'key1' is:", my_incorrect_dictionary['key1'])
print(my_incorrect_dictionary)
```

<pre class="output-block">The value of key 'key1' is: 2
{'key1': 2, 'key3': 6}
</pre>

This is because the value from first instance of `key1` has actually been overwritten by the second instance. This is another **logic error**, in which the program runs, but with unexpected or unwanted results. It is up to the programmer to catch these, or else they may affect the conclusions drawn from the program!

Given the above description of dictionaries, it may be apparent that the most useful way to use keys is as string labels for your data for easy access and lookup.



##### KeyError

One more note on dictionary keys: one of the most common errors you'll see when coding in Python is `KeyError`. This happens when you try to access a key in a dictionary, but that key doesn't exist:


```python
my_dictionary = { 'key1' : 1, 'key2' : 3, 'key3' : 6 }
print("Value of key 'key7':", my_dictionary['key7'])
```

<pre class="output-block">---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
Cell In[108], line 2
      1 my_dictionary = { 'key1' : 1, 'key2' : 3, 'key3' : 6 }
----> 2 print("Value of key 'key7':", my_dictionary['key7'])

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

<pre class="output-block">[1, 1, 0.93]
0.94
---
This dataset is made up to show the flexibility of dictionary values.
</pre>

#### Whitespace, part 2

Recall our discussion of whitespace in Part 1 of the workshop. Remember that whitespace refers to any part of a string that is not a visible character, such as a space, tab, or new line. We said that our best advice is keep individual instructions to a single line, and only consider adding whitespace for legibility for difficult to read function calls or data structure definitions (more later).

Well, we're now at later, and as you can see above, we used a lot of whitespace to define `my_mixed_dictionary`. Now that you know a bit more about control flow and data structures, we can be a bit more specific with this advice:

1. Individual instructions must be kept to one line of code.
2. Indentation is used to define blocks of code that are executed conditionally (`if`/`else`) or loops (`while`/`for`). In this case, Python is using the whitespace in order to interpret the code.
3. Exceptions to use of whitespace, including indentation, are function calls and data structure definitions. Basically, anything within `()`, `[]`, or `{}` can have whitespace inserted into it. Here, Python is using those symbols to denote the beginning and end of its instructions rather than the end of a line.

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

<pre class="output-block">Original: {'key1': 1, 'key2': 3, 'key3': 6}
We added a key using square brackets and the assignment operator: {'key1': 1, 'key2': 3, 'key3': 6, 'key4': 10}
And we can access the value directly by key, e.g. 'key4': 10
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

<pre class="output-block">Last state of dict: {'key1': 'NA', 'key2': 3, 'key3': 6, 'key4': 10}
After removing key 'key1' with del: {'key2': 3, 'key3': 6, 'key4': 10}
</pre>

> **Exercise**: Create a dictionary named `student_grades` with three students and their corresponding grades. The keys should be student names (e.g., "Alice", "Bob") and the values should be their grades (e.g., 85, 90). Then do the following:
>
> 1. Print the grade of one specific student by accessing it through the key.
> 2. Add a new student with their grade to the `student_grades` dictionary and print out their grade.
> 3. One student moved away, so remove them from your grade book and print out the dictionary to show they have left.


```python
## Your code goes here
```

??? success "Solution"
    ```python
    
    student_grades = { 'Alice' : 85, 'Bob' : 90, 'Wesley' : 100 }
    print("Original grades:", student_grades)
    print("---")
    student_grades["Gregg"] = 95
    print("New student 'Gregg':", student_grades['Gregg'])
    print("---")
    del(student_grades["Alice"])
    print("Alice moved:", student_grades)
    ```

    <pre class="output-block">Original grades: {'Alice': 85, 'Bob': 90, 'Wesley': 100}
    ---
    New student 'Gregg': 95
    ---
    Alice moved: {'Bob': 90, 'Wesley': 100, 'Gregg': 95}
    </pre>

2.   Dictionaries are **iterable**, meaning you can loop over them with a `for` loop. More specifically, the **dictionary keys are iterable**, meaning when you loop over a dictionary, you are actually looping over the keys of the dictionary:




```python
print("Last state of dict:", my_dictionary)

for key in my_dictionary:
  print(key, ":", my_dictionary[key])
```

<pre class="output-block">Last state of dict: {'key2': 3, 'key3': 6, 'key4': 10}
key2 : 3
key3 : 6
key4 : 10
</pre>

You may also **loop over key-value pairs** by using the `.items()` **method**:


```python
print("Last state of dict:", my_dictionary)

for key, value in my_dictionary.items():
  print(key, ":", value)
```

<pre class="output-block">Last state of dict: {'key2': 3, 'key3': 6, 'key4': 10}
key2 : 3
key3 : 6
key4 : 10
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

<pre class="output-block">Original state of dict: {'key1': 1, 'key2': 3, 'key3': 6}
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
```

??? success "Solution"
    ```python
    
    # Original lists
    beach_tourists=["Alice","Mason","Emma","Liam","Olivia","Walden","Ethan","Sophia","Oliver","Ava","Mia","William","Logan","Lucas","Charlotte","Amelia","Harper","James"]
    music_festival_attendees=["Jackson","Sophia","Aiden","Isabella","Lucas","Noah","Levi","Benjamin","Elijah","Mason","Elena","Eliana","Mateo","Jack","Luna","Eleanor","Ezra","Willow","Henry"]
    history_class_students=["Emily","James","Wally","Ella","Jacob","Amelia","Michael","Evelyn","Alexander","Avery","Mila","Aria","Ella","Layla","Scarlett","Grace","Wyatt","Waldo","Ellie","Paisley","Daniel"]
    office_building_employees=["Walter","Charlotte","Alexander","Scarlett","Michael","Victoria","Samuel","Aubrey","Olive","Nathan","Camila","Gabriel","Isaac","Savannah","Gabriella","Nora","Chloe","Zoe","Stella","Riley"]
    marathon_participants=["Daniel","Harper","Henry","Grace","Sebastian","Hannah","Victoria","Archer","Aurora","Brooklyn","Parker","Elias","Adeline","Julia","David","Liam","Josie","Carter","Jaxon"]
    
    locations = {
        "beach" : beach_tourists,
        "music-fesitval" : music_festival_attendees,
        "history-class" : history_class_students,
        "office" : office_building_employees,
        "marathon" : marathon_participants
    }
    
    print(locations["office"][2])
    ```

    <pre class="output-block">Alexander
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
```

??? success "Solution"
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
    
    locations = {}
    
    for i in range(len(key_names)):
      cur_key = key_names[i]
      cur_names = all_names[i]
    
      locations[cur_key] = cur_names
    
    print(locations["office"][2])
    ```

    <pre class="output-block">Alexander
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

<pre class="output-block">Found sample1
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
```

??? success "Solution"
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
    
    for location in locations:
      print("Searching for Waldo at the", location)
      if "Waldo" in locations[location]:
        print("Found Waldo at the", location, "!!")
    ```

    <pre class="output-block">Searching for Waldo at the beach
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

<pre class="output-block">key1 : 1
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

<pre class="output-block">['key1', 'key2', 'key3']
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

<pre class="output-block">Original: {'key1': 1, 'key2': 3, 'key3': 6}
Updated: {'key1': 1, 'key2': 3, 'key3': 6, 'key4': 9, 'key5': 2}
---
key1: 1
Updated with overwitten key1: {'key1': 99, 'key2': 3, 'key3': 6, 'key4': 9, 'key5': 2}
updated key1: 99
</pre>

4.   `len(dictionary)` : the trusty `len()` function can also be passed a dictionary, in which case it returns the number of keys in the dictionary:




```python
my_dictionary = { 'key1' : 1, 'key2' : 3, 'key3' : 6 }

num_keys = len(my_dictionary)

print("There are", num_keys, "keys in the dictionary")
```

<pre class="output-block">There are 3 keys in the dictionary
</pre>

#### Dictionary BONUS exercise

**BONUS Exercise**: Use what we've learned about dictionaries and lists to move Waldo from his current location to the marathon. Careful, he might have moved since last time!


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

# Your code above to move Waldo to the marathon

# Check and print if Waldo has been moved to the marathon
if "Waldo" in locations['marathon']:
    print("Waldo is now at the marathon.")
else:
    print("Waldo is not at the marathon.")
```

<pre class="output-block">Waldo is not at the marathon.
Waldo is not at the marathon.
</pre>

??? success "Solution"
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
    
    # Check and print if Waldo has been moved to the marathon
    if "Waldo" in locations['marathon']:
        print("Waldo is now at the marathon.")
    else:
        print("Waldo is not at the marathon.")
    ```

    <pre class="output-block">Waldo is not at the marathon.
    Waldo found at the music-festival - Moving him to the marathon.
    Waldo is now at the marathon.
    </pre>

#### Indirection, part 4

With lists and strings, we can indirectly reference elements within them by index. For dictionaries we can of course indirectly reference elements within the dictionary by key.


```python
my_dictionary = { 'key1' : 1, 'key2' : 3, 'key3' : 6 }
current_key = 'key2'

print("The value of", current_key, "is:", my_dictionary[current_key]) # Here we use the variable current_key to reference the value of 'key2'
```

<pre class="output-block">The value of key2 is: 3
</pre>

This is valuable when looping over dictionaries:


```python
my_dictionary = { 'key1' : 1, 'key2' : 3, 'key3' : 6 }

for current_key in my_dictionary:
    print("The value of", current_key, "is:", my_dictionary[current_key]) # Here we use the variable current_key to reference each key in the dictionary
```

<pre class="output-block">The value of key1 is: 1
The value of key2 is: 3
The value of key3 is: 6
</pre>

But what if the values of the dictionary are lists, and we want to access a specific index within them? Another level of indirection for convenience and confusion:


```python
my_dictionary = { 'key1' : [1,2,3], 'key2' : [2,3,4], 'key3' : [3,4,5] }
current_key = 'key2'
current_index = 1

print("The value at index", current_index, "of", current_key, "is:", my_dictionary[current_key][current_index]) # Here we use the variable current_key to reference the value of 'key2' and then access the second element in that list
```

<pre class="output-block">The value at index 1 of key2 is: 3
</pre>

> **Exercise**: *CODE GOLF*. Reduce this block of code to 3 lines (the dictionary initialization + 2 lines of code) and have it produce the same result.


```python
my_dictionary = { 'key1' : [1,2,3], 'key2' : [2,3,4], 'key3' : [3,4,5] }

key1_sum = my_dictionary['key1'][0] + my_dictionary['key1'][1] + my_dictionary['key1'][2]
key2_sum = my_dictionary['key2'][0] + my_dictionary['key2'][1] + my_dictionary['key2'][2]
key3_sum = my_dictionary['key3'][0] + my_dictionary['key3'][1] + my_dictionary['key3'][2]

print('key1:', key1_sum)
print('key2:', key2_sum)
print('key3:', key3_sum)
```

<pre class="output-block">key1: 6
key2: 9
key3: 12
</pre>

??? success "Solution"
    ```python
    
    my_dictionary = { 'key1' : [1,2,3], 'key2' : [2,3,4], 'key3' : [3,4,5] }
    for k in my_dictionary:
        print(k + ':', sum(my_dictionary[k]))
    ```

    <pre class="output-block">key1: 6
    key2: 9
    key3: 12
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

<pre class="output-block">(1, 2, 3, 4, 5)
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

<pre class="output-block">(1, 2, 3, 4, 5)
2
</pre>

<pre class="output-block">---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[136], line 5
      2 print(my_tuple)
      3 print(my_tuple[1])
----> 5 my_tuple[1] = 7

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

<pre class="output-block">(1, 2, 3, 4, 5)
[1, 2, 3, 4, 5]
</pre>

And, unlike lists, tuples can be used as keys in dictionaries:


```python
my_dictionary = { 'key1' : 1, ('key2') : 3, ('k', 'e', 'y', 3) : 6 }
print(my_dictionary)
```

<pre class="output-block">{'key1': 1, 'key2': 3, ('k', 'e', 'y', 3): 6}
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

<pre class="output-block">{1, 2, 3, 4, 5}
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



## Commenting your code

You've probably seen the lines of code starting with the `#` symbol (known as a number sign, hashtag, pound sign, or octothorp) throughout our workshop. These lines are called **comments**. Comments must start with `#` but afterwards can contain anything, even python keywords like `in`, `if`, `for`, etc. This is because that Python is programmed such that if the interpreter encounters a line starting with `#`, it simply ignores it. It does not try to execute it as a line of code.

This allows programmers to document their code in fine detail, section-by-section or even line-by-line. A good rule of thumb is to write a comment for every chunk of code that does something specific, or if it is not obvious why you had to write code that way. These comments will primarily benefit yourself for when you go back to your code and ask yourself, "Why did I do it this way?". It is also good practice to have comments exist on their own line rather than in-line with your code.

## Part 2 review

We covered a lot of ground in Part 2. Since we learned about `for` loops, we needed to learn about all the **iterables** in Python so that we know everything we can loop over.

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

    /* Hide all 2nd-level navs */
    .md-nav--secondary .md-nav__item .md-nav {
        display: none !important;
    }

    /* Show when parent has .expanded class */
    .md-nav--secondary .md-nav__item.expanded > .md-nav {
        display: block !important;
    }
  

</style>

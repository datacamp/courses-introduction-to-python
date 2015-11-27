---
title_meta  : Chapter 3
title       : Functions and packages
description : Add chapter description here.

--- type:VideoExercise lang:python xp:50 skills:2
## Functions

*** =video_link
//player.vimeo.com/video/146994267

--- type:NormalExercise lang:python xp:100 skills:2
## Familiar functions

Out of the box, Python offers a bunch of built-in functions to make your life as a data scientist easier. You already know two such functions: `print()` and `type()`. Also the functions `str()`, `int()`, `bool()` and `float()` to switch between data types are built-in functions.

Calling a function is easy. To get the type of `3.0` and store the output as a new variable, `result`, you can use the following:

```
result = type(3.0)
```

The general recipe for calling functions is thus:

```
output = function_name(input)
```

*** =instructions
- Use `type()` to get the type of `var1`; store the result as `out1`.
- Print out `out1` using the `print()` function. This function doesn't return anything, so there's no need to store the output in a new variable.
- Use `int()` to convert `var2` to an integer. Store the output as `out2`.

*** =hint
- Call the `type()` function like this: `type(var1)`.
- Call `print()` like you did so many times before. Simply put the variable you want to print in parentheses.
- `int(x)` will convert `x` to an integer.

*** =pre_exercise_code
```{python}
# pec
```

*** =sample_code
```{python}
# Create variables var1 and var2
var1 = [1, 2, 3, 4]
var2 = True

# Store the type of var1 in out1


# Print out out1


# Convert var2 to an integer: out2

```

*** =solution
```{python}
# Create variables var1 and var2
var1 = [1, 2, 3, 4]
var2 = True

# Store the type of var1 in out1
out1 = type(var1)

# Print out out1
print(out1)

# Convert var2 to an integer: out2
out2 = int(var2)
```

*** =sct
```{python}
# TODO VINCENT SCT MAGIC
success_msg("Great job!")
```

--- type:MultipleChoiceExercise lang:python xp:50 skills:2
## Help!

Once you know the name of the Python function you want to know, you still have to figure out how you will use it. Ironically, you have to ask for information on function with another function: `help()`.

To get help on the `type()` function, for example, you'll want to use this call:

```
type(max)
```

You typically ask for help interactively, so in the IPython Shell. IPython also offers a more concise way to ask for help:

```
?type
```

Use the Shell on the right to open up the documentation on `complex()`. Which of the following statements is true?

*** =instructions
- `complex()` takes two arguments: `real` and `[, image]`.
- `complex()` takes two arguments: `real` and `imag`. Both these arguments are required.
- `complex()` takes two arguments: `real` and `imag`. `real` is a required argument, `imag` is an optional argument.
- `complex()` takes two arguments: `real` and `imag`. If you don't specify `imag`, it is set to 1 by Python.

*** =hint
The help file shows `complex(real[, imag])`. Do you remember what Filip told you about these square brackets?

*** =pre_exercise_code
```{python}
# pec
```

*** =sct
```{python}
msg1 = "Incorrect. `[, arg_name]` is a syntax to specify optional arguments. TODO VINCENT IS THIS CORRECT?"
msg2 = "This statement is false. `imag` is not a required argument."
msg3 = "Perfect!"
msg4 = "This is almost true, but not entirely. If you don't specify `image`, it is set to 0."
test_mc("replace me")
```

--- type:NormalExercise lang:python xp:100 skills:2
## Multiple arguments

The built-in function `sorted()` also takes multiple arguments. Have a look at its documentation by typing `help(sorted)` in the IPython Shell.

You'll see that `sorted()` takes three arguments: `iterable`, `key` and `reverse`. The last two arguments are optional.

In this exercise, you'll only have to specify `iterable` and `inverse`, not `key`. The first input you pass to `sorted()` will obviously be matched to the `iterable` argument, but what about the second input. How can you tell Python that you want to specify `reverse` without changing anything about `key`? Well, you use the `=` for that, inside parenthesis:

```
sorted(input1, reverse = input2)
```

Two lists have been created for you on the right. Can you paste them together and sort them in descending order?

*** =instructions
- Use `+` to merge the contents of `first` and `second` into a new list: `full`.
- Call `sorted()` on `full` and specify the `reverse` argument to be `True`. Save the sorted list as `full_sorted`.
- Finish off by printing out `full_sorted`.

*** =hint
- Simply sum `first` and `second` as if they are two numbers, and assign the result to `full`.
- Use `sorted()` with two inputs: `full` and `reverse = True`.
- To print out a variable, use `print()`.

*** =pre_exercise_code
```{python}
# pec
```

*** =sample_code
```{python}
# Create lists first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# Paste together first and second: full


# Sort full in descending order: full_sorted


# Print out full_sorted

```

*** =solution
```{python}
# Create lists first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# Paste together first and second: full
full = first + second

# Sort full in descending order: full_sorted
full_sorted = sorted(full, reverse = True)

# Print out full_sorted
print(full_sorted)
```

*** =sct
```{python}
# TODO VINCENT SCT MAGIC
success_msg("Cool! Head over to the video on Python methods.")
```

--- type:VideoExercise lang:python xp:50 skills:2
## Methods

*** =video_link
//player.vimeo.com/video/146994269

--- type:NormalExercise lang:python xp:100 skills:2
## List Methods

From the video, you now know that the `+` operator is actually the `__add__` method that belongs to lists. However, there are tons of other methods. In this exercise, you'll be experimenting with:

- `append()`, to add elements to a list,
- `index()`, to get the index of the first element of a list that matches its input and
- `remove()`, to remove an the first element of a list that matches the input.

Before you start, try these examples in the IPython Shell:

```
x = ["a", "b", "c", "d"]
x.append("e")
x.index("b")
x.remove("c")
print(x)
```

You'll be working on the list with the area of different parts of the house: `areas`.

*** =instructions
- Use `append()` twice to add the size of the poolhouse and the garage again: `24.5` and `15.45`, respectively. Make sure to add them in this order.
- Print out the index of the element in `areas` that is equal to `20.0`.
- Use `remove()` to delete the number `18.0` from the `areas` list.
- After all these operations, print `areas` to see what it contains.

*** =hint
- Use the same syntax as the code samples: `areas.append(___)`
- To print out the index, wrap the `areas.index(___)` call in a `print()` function.
- `remove()` works differently than `del`. With `remove()` you have to pass the actual value of the element you want to remove, not the index.
- To print out a variable `x`, simply write `print(x)`.

*** =pre_exercise_code
```{python}
# pec
```

*** =sample_code
```{python}
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Use append twice to add poolhouse and garage size



# Print out the index of the element 20.0


# Remove the number 18.0 from areas


# Print areas
```

*** =solution
```{python}
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Use append twice to add poolhouse and garage size
areas.append(24.5)
areas.append(15.45)

# Print out the index of the room that has area 20.0
print(areas.index(20.0))

# Remove the number 18.0 from areas
areas.remove(18.0)

# Print areas
print(areas)
```

*** =sct
```{python}
# TODO VINCENT SCT MAGIC
success_msg("Great!")
```

--- type:NormalExercise lang:python xp:100 skills:2
## String Methods

Lists are not the only Python types that have methods associated. Strings, floats, integers and booleans, are also types, and also come prepacked with a bunch of useful methods. Follow the instructions closely to discover some string methods. If you want to discover them in more detail, you can always type `help(str)` in the IPython Shell.

A string `room` has already been created to do some experimentation with.

*** =instructions
- Use the `upper()` method on `room` and store the result in `room_up`.
- Print out `room` and `room_up`. Did both change?
- Print out the number of o's on the variable `room`: call `count()` on `room` and pass the letter `"o"` as an input to the method. We're talking about the variable `room`, not the word `"room"`!

*** =hint
- You can call the `upper()` method an `room` without additional inputs.
- To print out a variable `x`, you can write `print(x)`.
- Make sure to wrap your `room.count(___)` call in a `print()` function so that you print it out.

*** =pre_exercise_code
```{python}
# pec
```

*** =sample_code
```{python}
# string to experiment with: room
room = "poolhouse"

# Use upper() on room: room_up


# Print out room and room_up


# Print out the number of o's in room

```

*** =solution
```{python}
# string to experiment with: room
room = "poolhouse"

# Use upper() on room: room_up
room_up = room.upper()

# Print out room and room_up
print(room)
print(room_up)

# Print out the number of o's in room
print(room.count("o"))
```

*** =sct
```{python}
# TODO VINCENT SCT MAGIC
success_msg("Nice! Notice the difference: the `append()` method changed the list it was called on, while the `upper()` method doesn't change the string it was called on. It depends on the method you're using.")
```

--- type:MultipleChoiceExercise lang:python xp:50 skills:2
## Valid Method Calls

As you saw from the previous exercise, a call like this:

```
"poolhouse".upper()
```

produces `"POOLHOUSE"`. But it doesn't end here. It's super-easy to chain your method calls:

```
"poolhouse".upper().center("20")
```

Here, you're first converting `"poolhouse"` to upper case letters, and on the result, you call the `center()` method, that centers `"POOLHOUSE"` in a string of length 20. 

Apart from that, there are also other ways of calling Python methods. Instead of explaining these in detail, I suggest you experiment with the calls below. Can you tell which one is invalid, so which one generates an error?

*** =instructions
- `(["a", "b", "c"] + ["d"]).index("b")`
- `list.__add__(["a", "b", "c"], ["d"]).index("b")`
- `remove(["a", "b", "c"], "b")`
- `list.remove(["a", "b", "c"], "b")`

*** =hint
Copy the different options and paste them into the IPython Shell and indicate which one generates an error.

*** =pre_exercise_code
```{python}
# pec
```

*** =sct
```{python}
msg1 = "Incorrect; this call works perfectly fine. First you create a list by pasting together two lists, and then you call the `index()` method on it."
msg2 = "Incorrect, this call gives no error. `list.__add__(["a", "b", "c"], ["d"])` is equivalent to `["a", "b", "c"] + ["d"]`.
msg3 = "Correct! This call generates an error. If you use methods without calling them _on_ a Python object, you have to use the name of the type followed by a dot, like it option 2 and 4."
msg4 = "Incorrect, this call works perfectly fine. `list.remove(["a", "b", "c"], "b")` is equivalent to `["a", "b", "c"].remove("b")`.
success_msg("replace me")
```

--- type:VideoExercise lang:python xp:50 skills:2
## Packages

*** =video_link
//player.vimeo.com/video/146994272


--- type:NormalExercise lang:python xp:100 skills:2
## Import package

As a data scientist, you'll often be confronted with multi-dimension feature spaces to describe your data. As a refresher, let's do some basic geometry.

For a fancy clustering algorithms, you want to find the circumference $C$ and area $A$ of a circle. When the radius of the circle is `r`, you can calculate $C$ and $A$ as:

$$C = 2 \times \pi \times r$$
$$A = \pi \times r^2 $$

To use the constant `pi`, you'll need the `math` package. A variable `r` is already coded in the script. Fill in the code to calculate `C` and `A` and see how the `print()` functions create some nice printouts.

*** =instructions
- Import the `math` package.
- Calculate the circumference of the circle and store it in `C`.
- Calculate the area of the circle and store it in `A`.

*** =hint
- You can simply use `import math`, and then refer to `pi` with `math.pi`.
- Use the equation in the assignment to find `C`. Use `*`
- Use the equation in the assignment to find `A`. Use `*` and `**`.

*** =pre_exercise_code
```{python}
# pec
```

*** =sample_code
```{python}
# Import the math package


# Definition of radius
r = 0.43

# Calculate C
C = 0

# Calculate A
A = 0

# Build printout
print("Circumference: " + str(C))
print("Area: " + str(A))
```

*** =solution
```{python}
# Import the math package
import math

# Definition of radius
r = 0.43

# Calculate C
C = 2 * r * math.pi 

# Calculate A
A = math.pi * r ** 2

# Build printout
print("Circumference: " + str(C))
print("Area: " + str(A))
```

*** =sct
```{python}
# TODO VINCENT SCT MAGIC
success_msg("Nice!")
```

--- type:NormalExercise lang:python xp:100 skills:2
## Specific import

I - from math import radians. let them do something with radians() (3)
Assume you’re playing baseball on a field which can be approached by a circle. You hit the ball and from the center of the field it seemed you ran over an angle of 12 degrees. The field has a diameter of 50 meters. How far did you run? Use (50/2)*rad(12)

*** =instructions
- instruction 1
- instruction 2

*** =hint
hint comes here

*** =pre_exercise_code
```{python}
# pec
```

*** =sample_code
```{python}
# sample code
```

*** =solution
```{python}
# solution code
```

*** =sct
```{python}
# sct code
```

--- type:NormalExercise lang:python xp:100 skills:2
## Import package with local name

I - import math as m. let them do something with m.sin(), m.cos() and m.tan() (3)
TODO: Come up with a nice exercise on these concepts.

*** =instructions
- instruction 1
- instruction 2

*** =hint
hint comes here

*** =pre_exercise_code
```{python}
# pec
```

*** =sample_code
```{python}
# sample code
```

*** =solution
```{python}
# solution code
```

*** =sct
```{python}
# sct code
```

--- type:MultipleChoiceExercise lang:python xp:50 skills:2
## Different ways of importing

There are several ways to import packages and modules into Python. Depending on the import call, you'll have to use different Python code. Suppose I want to u

*** =instructions
- option 1
- option 2
- option 3

*** =hint
hint

*** =pre_exercise_code
```{python}
# pec
```

*** =sct
```{python}
test_mc(2) # if 2 is the correct option.
```


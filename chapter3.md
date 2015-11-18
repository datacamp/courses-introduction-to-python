---
title_meta  : Chapter 3
title       : Functions and packages
description : Add chapter description here.

--- type:VideoExercise lang:python xp:50 skills:2
## Functions

*** =video_link
```{python}
//player.vimeo.com/video/108225030
```

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

--- type:MultipleChoiceExercise lang:py xp:50 skills:2
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
hint comes here

*** =pre_exercise_code
```{py}
# pec
```

*** =sct
```{py}
msg1 = "Incorrect. `[, arg_name]` is a syntax to specify optional arguments. TODO VINCENT IS THIS CORRECT?"
msg2 = "This statement is false. `imag` is not a required argument."
msg3 = "Perfect!"
msg4 = "This is almost true, but not entirely. If you don't specify `image`, it is set to 0."
test_mc("replace me")
```

--- type:NormalExercise lang:py xp:100 skills:0
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
hint comes here

*** =pre_exercise_code
```{py}
# pec
```

*** =sample_code
```{py}
# Create lists first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# Paste together first and second: full


# Sort full in descending order: full_sorted


# Print out full_sorted

```

*** =solution
```{py}
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
```{py}
# TODO VINCENT SCT MAGIC
success_msg("Cool! Head over to the video on Methods.")
```

--- type:VideoExercise lang:python xp:50 skills:2
## Methods

*** =video_link
```{python}
//player.vimeo.com/video/108225030
```

--- type:VideoExercise lang:python xp:50 skills:2
## Packages

*** =video_link
```{python}
//player.vimeo.com/video/108225030
```

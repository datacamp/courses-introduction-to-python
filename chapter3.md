---
title_meta: Chapter 3
title: Functions and Packages
description: >-
  You'll learn how to use functions, methods, and packages to efficiently
  leverage the code that brilliant Python developers have written. The goal is
  to reduce the amount of code you need to solve challenging problems!
attachments:
  slides_link: 'https://projector-video-pdf-converter.datacamp.com/735/chapter3.pdf'
lessons:
  - nb_of_exercises: 4
    title: Functions
  - nb_of_exercises: 4
    title: Methods
  - nb_of_exercises: 4
    title: Packages
---

## Functions

```yaml
type: VideoExercise
key: 5c5f365930
xp: 50
```

`@projector_key`
1204d914b0e53100529827e07441ee6c

---

## Familiar functions

```yaml
type: NormalExercise
key: c422ee929b
lang: python
xp: 100
skills:
  - 2
```

Out of the box, Python offers a bunch of built-in functions to make your life as a data scientist easier. You already know two such functions: `print()` and `type()`. There are also functions like `str()`, `int()`, `bool()` and `float()` to switch between data types. You can find out about them [here.](https://docs.python.org/3/library/functions.html) These are built-in functions as well.

Calling a function is easy. To get the type of `3.0` and store the output as a new variable, `result`, you can use the following:

```
result = type(3.0)
```

`@instructions`
- Use `print()` in combination with `type()` to print out the type of `var1`.
- Use `len()` to get the [length of the list](https://docs.python.org/3/library/functions.html#len) `var1`. Wrap it in a `print()` call to directly print it out.
- Use `int()` to convert `var2` to an [integer](https://docs.python.org/3/library/functions.html#int). Store the output as `out2`.

`@hint`
- Call the `type()` function like this: `type(var1)`.
- Call `print()` like you did so many times before. Simply put the variable you want to print in parentheses.
- `int(x)` will convert `x` to an integer.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create variables var1 and var2
var1 = [1, 2, 3, 4]
var2 = True

# Print out type of var1
____

# Print out length of var1
____

# Convert var2 to an integer: out2
out2 = ____
```

`@solution`
```{python}
# Create variables var1 and var2
var1 = [1, 2, 3, 4]
var2 = True

# Print out type of var1
print(type(var1))

# Print out length of var1
print(len(var1))

# Convert var2 to an integer: out2
out2 = int(var2)
```

`@sct`
```{python}
msg = "You don't have to change or remove the predefined variables."
Ex().check_object("var1", missing_msg=msg).has_equal_value(incorrect_msg=msg)
Ex().check_object("var2", missing_msg=msg).has_equal_value(incorrect_msg=msg)

patt = "__JINJA__:Make sure to print out the %s of `var1` with `{{sol_call}}`."
Ex().has_printout(0, not_printed_msg = patt % 'type')
Ex().has_printout(1, not_printed_msg = patt % 'length')

int_miss_msg = "Have you used `int()` to make an integer of `var2`?"
int_incorr_msg = "Have you passed `var2` to `int()`?"
Ex().check_correct(
  check_object("out2").has_equal_value(incorrect_msg="You called `int()` correctly; now make sure to assign the result of this call to `out2`."),
  check_function("int", missing_msg=int_miss_msg).has_equal_value(incorrect_msg=int_incorr_msg)
)
success_msg("Great job! The `len()` function is extremely useful; it also works on strings to count the number of characters!")
```

---

## Help!

```yaml
type: MultipleChoiceExercise
key: 679b852978
lang: python
xp: 50
skills:
  - 2
```

Maybe you already know the name of a Python function, but you still have to figure out how to use it. Ironically, you have to ask for information about a function with another function: `help()`. In IPython specifically, you can also use `?` before the function name.

To get help on the `max()` function, for example, you can use one of these calls:

```
help(max)
?max
```

Use the IPython Shell to open up the [documentation](https://docs.python.org/3/library/functions.html#pow) on `pow()`. Do this by typing `?pow` or `help(pow)` and hitting **Enter**.

Which of the following statements is true?

`@possible_answers`
- `pow()` takes three arguments: `base`, `exp`, and `mod`. Without `mod`, the function will return an error.
- `pow()` takes three required arguments: `base`, `exp`, and `None`.
- `pow()` requires `base` and `exp` arguments; `mod` is optional.
- `pow()` takes two arguments: `exp` and `mod`. Missing `exp` results in an error.

`@hint`
- Optional arguments are set `=` to a default value, which the function will use if that argument is not specified.

`@pre_exercise_code`
```{python}

```

`@sct`
```{python}
msg1 = "Not quite. `mod` has a default value that will be used if you don't specify a value."
msg2 = "Incorrect. `None` is the default value for the `mod` argument."
msg3 = "Perfect! Using `help()` can help you understand how functions work, unleashing their full potential!"
msg4 = "Incorrect. `pow()` takes three arguments, one of which has a default value."
Ex().has_chosen(3, [msg1, msg2, msg3, msg4])
```

---

## Multiple arguments

```yaml
type: NormalExercise
key: e30486d7c1
lang: python
xp: 100
skills:
  - 2
```

In the previous exercise, you identified optional arguments by viewing the documentation with `help()`. You'll now apply this to change the behavior of the `sorted()` function.

Have a look at the [documentation](https://docs.python.org/3/library/functions.html#sorted) of `sorted()` by typing `help(sorted)` in the IPython Shell.

You'll see that `sorted()` takes three arguments: `iterable`, `key`, and `reverse`. In this exercise, you'll only have to specify `iterable` and `reverse`, not `key`.

Two lists have been created for you.

Can you paste them together and sort them in descending order?

`@instructions`
- Use `+` to merge the contents of `first` and `second` into a new list: `full`.
- Call `sorted()` and on `full` and specify the `reverse` argument to be `True`. Save the sorted list as `full_sorted`.
- Finish off by printing out `full_sorted`.

`@hint`
- Sum `first` and `second` as if they are two numbers and assign the result to `full`.
- Use `sorted()` with two inputs: `full` and `reverse=True`.
- To print out a variable, use `print()`.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create lists first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# Paste together first and second: full
full = ____ + ____

# Sort full in descending order: full_sorted
full_sorted = ____

# Print out full_sorted
____
```

`@solution`
```{python}
# Create lists first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# Paste together first and second: full
full = first + second

# Sort full in descending order: full_sorted
full_sorted = sorted(full, reverse=True)

# Print out full_sorted
print(full_sorted)
```

`@sct`
```{python}
msg = "You don't have to change or remove the already variables `first` and `second`."
Ex().multi(
  check_object("first", missing_msg=msg).has_equal_value(incorrect_msg=msg),
  check_object("second", missing_msg=msg).has_equal_value(incorrect_msg=msg)
)
Ex().check_correct(
  check_object("full_sorted").has_equal_value(incorrect_msg="Make sure you assign the result of calling `sorted()` to `full_sorted`."),
  check_function("sorted").multi(
    check_args(0).has_equal_value(),
    check_args('reverse').has_equal_value()
  )
)

success_msg("Cool! Head over to the video on Python methods.")
```

---

## Methods

```yaml
type: VideoExercise
key: 2b66cb66b1
xp: 50
```

`@projector_key`
8e387776f3a264a745128b68aa8d8f83

---

## String Methods

```yaml
type: NormalExercise
key: 4039302ee0
lang: python
xp: 100
skills:
  - 2
```

Strings come with a bunch of methods. Follow the instructions closely to discover some of them. If you want to discover them in more detail, you can always type `help(str)` in the IPython Shell.

A string `place` has already been created for you to experiment with.

`@instructions`
- Use the `.upper()` [method](https://docs.python.org/3/library/stdtypes.html#str.upper) on `place` and store the result in `place_up`. Use the syntax for calling methods that you learned in the previous video.
- Print out `place` and `place_up`. Did both change?
- Print out the number of o's on the variable `place` by calling `.count()` on `place` and passing the letter `'o'` as an input to the method. We're talking about the variable `place`, not the word `"place"`!

`@hint`
- You can call the `.upper()` method on `place` without any additional inputs.
- To print out a variable `x`, you can write `print(x)`.
- Make sure to wrap your `place.count(____)` call in a `print()` function so that you print it out.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# string to experiment with: place
place = "poolhouse"

# Use upper() on place
place_up = 

# Print out place and place_up



# Print out the number of o's in place

```

`@solution`
```{python}
# string to experiment with: place
place = "poolhouse"

# Use upper() on place
place_up = place.upper()

# Print out place and place_up
print(place)
print(place_up)

# Print out the number of o's in place
print(place.count('o'))
```

`@sct`
```{python}
msg = "You don't have to change or remove the predefined variables."
Ex().check_object("place", missing_msg=msg).has_equal_value(incorrect_msg=msg)

patt = "Don't forget to print out `%s`."
Ex().has_printout(0, not_printed_msg=patt % "place")
Ex().check_correct(
    has_printout(1, not_printed_msg=patt % "place_up"),
    check_correct(
        check_object("place_up").has_equal_value(incorrect_msg="Assign the result of your `place.upper()` call to `place_up`."),
        check_function("place.upper", signature=False)
    )
)    

# check count of place
Ex().check_correct(
  has_printout(2, not_printed_msg = "You have calculated the number of o's in `place` fine; now make sure to wrap `place.count('o')` call in a `print()` function to print out the result."),
  check_function("place.count", signature=False).check_args(0).has_equal_value()
)

success_msg("Nice! Notice from the printouts that the `upper()` method does not change the object it is called on. This will be different for lists in the next exercise!")
```

---

## List Methods

```yaml
type: NormalExercise
key: 0dbe8ed695
lang: python
xp: 100
skills:
  - 2
```

Strings are not the only Python types that have methods associated with them. Lists, floats, integers and booleans are also types that come packaged with a bunch of useful methods. In this exercise, you'll be experimenting with:

- `.index()`, to get the index of the first element of a list that matches its input and
- `.count()`, to get the number of times an element appears in a list.

You'll be working on the list with the area of different parts of a house: `areas`.

`@instructions`
- Use the `.index()` method to get the index of the element in `areas` that is equal to `20.0`. Print out this index.
- Call `.count()` on `areas` to find out how many times `9.50` appears in the list. Again, simply print out this number.

`@hint`
- To print out the index, wrap the `areas.index(___)` call in a `print()` function.
- To print out the number of times an element `x` occurs in the list, wrap the `areas.count(___)` call in a `print()` function.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Print out the index of the element 20.0


# Print out how often 9.50 appears in areas

```

`@solution`
```{python}
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Print out the index of the element 20.0
print(areas.index(20.0))

# Print out how often 9.50 appears in areas
print(areas.count(9.50))
```

`@sct`
```{python}
predef_msg = "You don't have to change or remove the predefined list `areas`."

Ex().check_object("areas", missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg)

Ex().check_function("print", index=0).check_args(0).check_function('areas.index', signature=False).check_args(0).has_equal_value()


Ex().check_function("print", index=1).check_args(0).check_function('areas.count', signature=False).has_equal_value()

success_msg("Nice! These were examples of `list` methods that did not change the list they were called on.")
```

---

## List Methods (2)

```yaml
type: NormalExercise
key: 1fbeab82d0
lang: python
xp: 100
skills:
  - 2
```

Most list methods will change the list they're called on. Examples are:

- `.append()`, that adds an element to the list it is called on,
- `.remove()`, that removes the first element of a list that matches the input, and
- `.reverse()`, that reverses the order of the elements in the list it is called on.

You'll be working on the list with the area of different parts of the house: `areas`.

`@instructions`
- Use `.append()` twice to add the size of the poolhouse and the garage again: `24.5` and `15.45`, respectively. Make sure to add them in this order.
- Print out `areas`
- Use the `.reverse()` method to reverse the order of the elements in `areas`.
- Print out `areas` once more.

`@hint`
- For the first instruction, use the `areas.append(___)` call twice.
- To print out a variable `x`, simply write `print(x)`.
- The `.reverse()` method does not require additional inputs; just use the dot notation and empty parentheses: `.reverse()`.
- To print out a variable `x`, simply write `print(x)`.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Use append twice to add poolhouse and garage size



# Print out areas


# Reverse the orders of the elements in areas


# Print out areas

```

`@solution`
```{python}
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Use append twice to add poolhouse and garage size
areas.append(24.5)
areas.append(15.45)

# Print out areas
print(areas)

# Reverse the orders of the elements in areas
areas.reverse()

# Print out areas
print(areas)
```

`@sct`
```{python}
Ex().multi(
  check_function("areas.append", index=0, signature=False).check_args(0).has_equal_value(),
  check_function("areas.append", index=1, signature=False).check_args(0).has_equal_value(),
  check_function("print", index=0).check_args(0).has_equal_ast(),
  check_function("areas.reverse", index=0, signature=False),
  check_function("print", index=1).check_args(0).has_equal_ast()
)

success_msg("Great!")
```

---

## Packages

```yaml
type: VideoExercise
key: ab96a17c5e
xp: 50
```

`@projector_key`
cedcfb34350be8545599768f96695cdd

---

## Import package

```yaml
type: NormalExercise
key: 7432a6376f
lang: python
xp: 100
skills:
  - 2
```

Let's say you wanted to calculate the circumference and area of a circle. Here's what those formulas look like:

$$C = 2 \pi r$$
$$A = \pi r^2 $$

Rather than typing the number for `pi`, you can use the `math` package that contains the number

For reference, `**` is the symbol for exponentiation. For example `3**4` is `3` to the power of `4` and will give `81`.

`@instructions`
- Import the `math` package.
- Use `math.pi` to calculate the circumference of the circle and store it in `C`.
- Use `math.pi` to calculate the area of the circle and store it in `A`.

`@hint`
- You can simply use `import math`, and then refer to `pi` with `math.pi`.
- Use the equation in the assignment text to find `C`. Use `*`
- Use the equation in the assignment text to find `A`. Use `*` and `**`.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Import the math package
import ____

# Calculate C
C = 2 * 0.43 * ____

# Calculate A
A = ____ * 0.43 ** 2

print("Circumference: " + str(C))
print("Area: " + str(A))
```

`@solution`
```{python}
# Import the math package
import math

# Calculate C
C = 2 * 0.43 * math.pi

# Calculate A
A = math.pi * 0.43 ** 2

print("Circumference: " + str(C))
print("Area: " + str(A))
```

`@sct`
```{python}
patt = "Your calculation of `%s` is not quite correct. Make sure to use `math.pi`."
Ex().multi(
  has_import('math', same_as=False),
  check_object('C').has_equal_value(incorrect_msg=patt%'C'),
  check_object('A').has_equal_value(incorrect_msg=patt%'A')
)

Ex().multi(
  has_printout(0, not_printed_msg = "__JINJA__:Keep `{{sol_call}}` in there to print out the circumference."),
  has_printout(1, not_printed_msg = "__JINJA__:Keep `{{sol_call}}` in there to print out the area.")
)

success_msg("Nice! If you know how to deal with functions from packages, the power of _a lot_ of Python programmers is at your fingertips!")
```

---

## Selective import

```yaml
type: NormalExercise
key: fe65eff50a
lang: python
xp: 100
skills:
  - 2
```

General imports, like `import math`, make **all** functionality from the `math` package available to you. However, if you decide to only use a specific part of a package, you can always make your import more selective:

```
from math import pi
```

Try the same thing again, but this time only use `pi`.

`@instructions`
- Perform a selective import from the `math` package where you only import the `pi` function.
- Use `math.pi` to calculate the circumference of the circle and store it in `C`.
- Use `math.pi` to calculate the area of the circle and store it in `A`.

`@hint`
- Use `from math import pi` to do the selective import.
- Now, you can use `pi` on it's own!

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Import pi function of math package
from math import ____

# Calculate C
C = 2 * 0.43 * ____

# Calculate A
A = ____ * 0.43 ** 2

print("Circumference: " + str(C))
print("Area: " + str(A))
```

`@solution`
```{python}
# Import pi function of math package
from math import pi

# Calculate C
C = 2 * 0.43 * pi

# Calculate A
A = pi * 0.43 ** 2

print("Circumference: " + str(C))
print("Area: " + str(A))
```

`@sct`
```{python}
patt = "Your calculation of `%s` is not quite correct. Make sure to use only `pi`."

Ex().has_import("math.pi", not_imported_msg = "Be sure to import `pi` from the `math` package. You should use the `from ___ import ___` notation.",)

Ex().multi(
  check_object('C').has_equal_value(incorrect_msg=patt%'C'),
  check_object('A').has_equal_value(incorrect_msg=patt%'A')
)

Ex().multi(
  has_printout(0, not_printed_msg = "__JINJA__:Keep `{{sol_call}}` in there to print out the circumference."),
  has_printout(1, not_printed_msg = "__JINJA__:Keep `{{sol_call}}` in there to print out the area.")
)

success_msg("Nice! Head over to the next exercise.")
```

---

## Different ways of importing

```yaml
type: MultipleChoiceExercise
key: f1b2675a2a
lang: python
xp: 50
skills:
  - 2
```

There are several ways to import packages and modules into Python. Depending on the import call, you'll have to use different Python code.

Suppose you want to use the function `inv()`, which is in the `linalg` subpackage of the `scipy` package. You want to be able to use this function as follows:

```
my_inv([[1,2], [3,4]])
```

Which `import` statement will you need in order to run the above code without an error?

`@possible_answers`
- `import scipy`
- `import scipy.linalg`
- `from scipy.linalg import my_inv`
- `from scipy.linalg import inv as my_inv`

`@hint`
- Try the different import statements in the shell and see which one causes the line `my_inv([[1, 2], [3, 4]])` to run without errors. Hit **enter** to run the code you have typed.

`@pre_exercise_code`
```{python}

```

`@sct`
```{python}
msg1 = msg2 = msg3 = "Incorrect, try again. Try the different import statements in the shell and see which one causes the line `my_inv([[1, 2], [3, 4]])` to run without errors."
msg4 = "Correct! The `as` word allows you to create a local name for the function you're importing: `inv()` is now available as `my_inv()`."
Ex().has_chosen(4, [msg1, msg2, msg3, msg4])
```

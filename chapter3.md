---
title_meta  : Chapter 3
title       : Functions and Packages
description : To leverage the code that brilliant Python developers have written, you'll learn about using functions, methods and packages. This will help you to reduce the amount of code you need to solve challenging problems!
attachments :
  slides_link : https://s3.amazonaws.com/assets.datacamp.com/course/intro_to_python/ch3_slides.pdf


---
## Functions

```yaml
type: VideoExercise
lang: python
xp: 50
skills: 2
key: 2dde2f90b8
```

`@video_link`
//player.vimeo.com/video/154563189

`@video_hls`
//videos.datacamp.com/transcoded/735_intro_to_python/v3/hls-ch3_1.master.m3u8

*** =projector_key
abe8835964fe3385a3f0283b7a605f5f

---
## Familiar functions

```yaml
type: NormalExercise
lang: python
xp: 100
skills: 2
key: c422ee929b
```

Out of the box, Python offers a bunch of built-in functions to make your life as a data scientist easier. You already know two such functions: [`print()`](https://docs.python.org/3/library/functions.html#print) and [`type()`](https://docs.python.org/3/library/functions.html#type). You've also used the functions [`str()`](https://docs.python.org/3/library/functions.html#func-str), [`int()`](https://docs.python.org/3/library/functions.html#int), [`bool()`](https://docs.python.org/3/library/functions.html#bool) and [`float()`](https://docs.python.org/3/library/functions.html#float) to switch between data types. These are built-in functions as well.

Calling a function is easy. To get the type of `3.0` and store the output as a new variable, `result`, you can use the following:

```
result = type(3.0)
```

The general recipe for calling functions and saving the result to a variable is thus:

```
output = function_name(input)
```

`@instructions`
- Use [`print()`](https://docs.python.org/3/library/functions.html#print) in combination with [`type()`](https://docs.python.org/3/library/functions.html#type) to print out the type of `var1`.
- Use [`len()`](https://docs.python.org/3/library/functions.html#len) to get the length of the list `var1`. Wrap it in a [`print()`](https://docs.python.org/3/library/functions.html#print) call to directly print it out.
- Use [`int()`](https://docs.python.org/3/library/functions.html#int) to convert `var2` to an integer. Store the output as `out2`.

`@hint`
- Call the [`type()`](https://docs.python.org/3/library/functions.html#type) function like this: `type(var1)`.
- Call [`print()`](https://docs.python.org/3/library/functions.html#print) like you did so many times before. Simply put the variable you want to print in parentheses.
- `int(x)` will convert `x` to an integer.

`@pre_exercise_code`
```{python}
# pec
```

`@sample_code`
```{python}
# Create variables var1 and var2
var1 = [1, 2, 3, 4]
var2 = True

# Print out type of var1


# Print out length of var1


# Convert var2 to an integer: out2

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
test_object("var1", undefined_msg = msg, incorrect_msg = msg)
test_object("var2", undefined_msg = msg, incorrect_msg = msg)

msg = "Make sure to print out the type of `var1` like this: `print(type(var1))`."
test_function("type", 1, incorrect_msg = msg)
test_function("print", 1, incorrect_msg = msg)

msg = "Make sure to print out the length of `var1` like this: `print(len(var1))`."
test_function("len", 1, incorrect_msg = msg)
test_function("print", 2, incorrect_msg = msg)

test_object("out2", do_eval = False)

test_function("int", not_called_msg = "Use [`int()`](https://docs.python.org/3/library/functions.html#int) to make an integer of `var2` and assign to `out2`.",
                     incorrect_msg = "Use [`int()`](https://docs.python.org/3/library/functions.html#int) with the correct variables. You should pass `var2` to it."
)
test_object("out2", incorrect_msg = "Make sure to assign the correct value to `out2`.")
success_msg("Great job! The [`len()`](https://docs.python.org/3/library/functions.html#len) function is extremely useful; it also works on strings to count the number of characters!")
```


---
## Help!

```yaml
type: MultipleChoiceExercise
lang: python
xp: 50
skills: 2
key: 679b852978
```

Maybe you already know the name of a Python function, but you still have to figure out how to use it. Ironically, you have to ask for information about a function with another function: [`help()`](https://docs.python.org/3/library/functions.html#help). In IPython specifically, you can also use `?` before the function name.

To get help on the [`max()`](https://docs.python.org/3/library/functions.html#max) function, for example, you can use one of these calls:

```
help(max)
?max
```

Use the Shell on the right to open up the documentation on [`complex()`](https://docs.python.org/3/library/functions.html#complex). Which of the following statements is true?

`@instructions`
- [`complex()`](https://docs.python.org/3/library/functions.html#complex) takes exactly two arguments: `real` and `[, imag]`.
- [`complex()`](https://docs.python.org/3/library/functions.html#complex) takes two arguments: `real` and `imag`. Both these arguments are required.
- [`complex()`](https://docs.python.org/3/library/functions.html#complex) takes two arguments: `real` and `imag`. `real` is a required argument, `imag` is an optional argument.
- [`complex()`](https://docs.python.org/3/library/functions.html#complex) takes two arguments: `real` and `imag`. If you don't specify `imag`, it is set to 1 by Python.

`@hint`
The help file shows `complex(real[, imag])`. Do you remember what Filip told you about these square brackets?

`@pre_exercise_code`
```{python}
# pec
```

`@sct`
```{python}
msg1 = "Incorrect. `[, imag]` shows that `imag` is an optional argument."
msg2 = "This statement is false. `imag` is not a required argument."
msg3 = "Perfect!"
msg4 = "This is almost true, but not entirely. If you don't specify `image`, it is set to 0."
test_mc(3, [msg1, msg2, msg3, msg4])
```

---
## Multiple arguments

```yaml
type: NormalExercise
lang: python
xp: 100
skills: 2
key: e30486d7c1
```

In the previous exercise, the square brackets around `imag` in the documentation showed us that the `imag` argument is optional. But Python also uses a different way to tell users about arguments being optional.

Have a look at the documentation of [`sorted()`](https://docs.python.org/3/library/functions.html#sorted) by typing `help(sorted)` in the IPython Shell.

You'll see that [`sorted()`](https://docs.python.org/3/library/functions.html#sorted) takes three arguments: `iterable`, `key` and `reverse`.

`key=None` means that if you don't specify the `key` argument, it will be `None`. `reverse=False` means that if you don't specify the `reverse` argument, it will be `False`.

In this exercise, you'll only have to specify `iterable` and `reverse`, not `key`. The first input you pass to [`sorted()`](https://docs.python.org/3/library/functions.html#sorted) will be matched to the `iterable` argument, but what about the second input? To tell Python you want to specify `reverse` without changing anything about `key`, you can use `=`:

```
sorted(___, reverse = ___)
```

Two lists have been created for you on the right. Can you paste them together and sort them in descending order?

Note: For now, we can understand an [_iterable_](https://docs.python.org/2/glossary.html#term-iterable) as being any collection of objects, e.g. a List.

`@instructions`
- Use `+` to merge the contents of `first` and `second` into a new list: `full`.
- Call [`sorted()`](https://docs.python.org/3/library/functions.html#sorted) on `full` and specify the `reverse` argument to be `True`. Save the sorted list as `full_sorted`.
- Finish off by printing out `full_sorted`.

`@hint`
- Simply sum `first` and `second` as if they are two numbers and assign the result to `full`.
- Use [`sorted()`](https://docs.python.org/3/library/functions.html#sorted) with two inputs: `full` and `reverse = True`.
- To print out a variable, use [`print()`](https://docs.python.org/3/library/functions.html#print).

`@pre_exercise_code`
```{python}
# pec
```

`@sample_code`
```{python}
# Create lists first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# Paste together first and second: full


# Sort full in descending order: full_sorted


# Print out full_sorted

```

`@solution`
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

`@sct`
```{python}
msg = "You don't have to change or remove the predefined variables."
test_object("first", undefined_msg = msg, incorrect_msg = msg)
test_object("second", undefined_msg = msg, incorrect_msg = msg)
test_object("full")
test_function_v2("sorted", params = ['iterable', 'reverse'])
test_object("full_sorted", incorrect_msg = "Assign the result of the `sorted()` function to `full_sorted`.")
success_msg("Cool! Head over to the video on Python methods.")
```

---
## Methods

```yaml
type: VideoExercise
lang: python
xp: 50
skills: 2
key: e1aaeb300b
```

`@video_link`
//player.vimeo.com/video/154563307

`@video_hls`
//videos.datacamp.com/transcoded/735_intro_to_python/v1/hls-ch3_2.master.m3u8

*** =projector_key
cf2471efdf2df82d911fb0cfcf0466f6

---
## String Methods

```yaml
type: NormalExercise
lang: python
xp: 100
skills: 2
key: 4039302ee0
```

Strings come with a bunch of methods. Follow the instructions closely to discover some of them. If you want to discover them in more detail, you can always type `help(str)` in the IPython Shell.

A string `room` has already been created for you to experiment with.

`@instructions`
- Use the [`upper()`](https://docs.python.org/3/library/stdtypes.html#str.upper) method on `room` and store the result in `room_up`. Use the syntax for calling methods that you learned in the previous video.
- Print out `room` and `room_up`. Did both change?
- Print out the number of o's on the variable `room` by calling [`count()`](https://docs.python.org/3/library/stdtypes.html#str.count) on `room` and passing the letter `"o"` as an input to the method. We're talking about the variable `room`, not the word `"room"`!

`@hint`
- You can call the [`upper()`](https://docs.python.org/3/library/stdtypes.html#str.upper) method on `room` without any additional inputs.
- To print out a variable `x`, you can write `print(x)`.
- Make sure to wrap your `room.count(___)` call in a [`print()`](https://docs.python.org/3/library/functions.html#print) function so that you print it out.

`@pre_exercise_code`
```{python}
# pec
```

`@sample_code`
```{python}
# string to experiment with: room
room = "poolhouse"

# Use upper() on room: room_up


# Print out room and room_up


# Print out the number of o's in room

```

`@solution`
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

`@sct`
```{python}
msg = "You don't have to change or remove the predefined variables."
test_object("room", undefined_msg = msg, incorrect_msg = msg)

test_function("room.upper", not_called_msg = "Don't forget to call the [`upper()`](https://docs.python.org/3/library/stdtypes.html#str.upper) method of the `room` object using the `.` notation. Watch out here, don't forget the parentheses after upper: `room.upper()`.")
test_object("room_up", incorrect_msg = "Assign the result of your `room.upper()` call to `room_up`.")

msg = "For the second instruction, print out `%s` using [`print()`](https://docs.python.org/3/library/functions.html#print)"
test_function("print", 1, incorrect_msg = msg % "room")
test_function("print", 2, incorrect_msg = msg % "room_up")

msg = "Don't forget to count the o's in `room` by calling the [`count()`](https://docs.python.org/3/library/functions.html#count) method on it with the correct argument. Make sure to place the `\"o\"` between double quotes."
test_function("room.count",
              not_called_msg = msg,
              incorrect_msg = msg)
test_function("print", 3, not_called_msg = "Don't forget to print out the number of o's in `room`.")


success_msg("Nice! Notice from the printouts that the [`upper()`](https://docs.python.org/3/library/stdtypes.html#str.upper) method does not change the object it is called on. This will be different for lists in the next exercise!")
```


---
## List Methods

```yaml
type: NormalExercise
lang: python
xp: 100
skills: 2
key: 0dbe8ed695
```

Strings are not the only Python types that have methods associated with them. Lists, floats, integers and booleans are also types that come packaged with a bunch of useful methods. In this exercise, you'll be experimenting with:

- [`index()`](https://docs.python.org/3/library/stdtypes.html#str.index), to get the index of the first element of a list that matches its input and
- [`count()`](https://docs.python.org/3/library/stdtypes.html#str.count), to get the number of times an element appears in a list.

You'll be working on the list with the area of different parts of a house: `areas`.

`@instructions`
- Use the [`index()`](https://docs.python.org/3/library/stdtypes.html#str.index) method to get the index of the element in `areas` that is equal to `20.0`. Print out this index.
- Call [`count()`](https://docs.python.org/3/library/stdtypes.html#str.count) on `areas` to find out how many times `14.5` appears in the list. Again, simply print out this number.

`@hint`
- To print out the index, wrap the `areas.index(___)` call in a [`print()`](https://docs.python.org/3/library/functions.html#print) function.
- To print out the number of times an element `x` occurs in the list, wrap the `areas.count(___)` call in a [`print()`](https://docs.python.org/3/library/functions.html#print) function.

`@pre_exercise_code`
```{python}
# pec
```

`@sample_code`
```{python}
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Print out the index of the element 20.0


# Print out how often 14.5 appears in areas


```

`@solution`
```{python}
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Print out the index of the element 20.0
print(areas.index(20.0))

# Print out how often 14.5 appears in areas
print(areas.count(14.5))
```

`@sct`
```{python}
msg = "You don't have to change or remove the predefined variables."
test_object("areas", undefined_msg = msg, incorrect_msg = msg)

msg = "Don't forget to find the index of `20.0` in `areas` by calling the [`index()`](https://docs.python.org/3/library/functions.html#index) method on it with the correct argument."
test_function("areas.index",
              not_called_msg = msg,
              incorrect_msg = msg)
test_function("print", 1, not_called_msg = "Don't forget to print out the index of `20.0` in `areas`.", incorrect_msg = "For the first printout, you should use `print(areas.index(20.0))`.")

msg = "Don't forget to count the number of times `14.5` appears in `areas` by calling the [`count()`](https://docs.python.org/3/library/functions.html#count) method on it with the correct argument."
test_function("areas.count",
              not_called_msg = msg,
              incorrect_msg = msg)
test_function("print", 2, not_called_msg = "Don't forget to print out the count of `14.5` in `areas`.", incorrect_msg = "For the second printout, you should use `print(areas.count(14.5))`.")

success_msg("Nice! These were examples of `list` methods that did not change the list they were called on.")
```

---
## List Methods (2)

```yaml
type: NormalExercise
lang: python
xp: 100
skills: 2
key: 1fbeab82d0
```

Most list methods will change the list they're called on. Examples are:

- [`append()`](https://docs.python.org/3/library/stdtypes.html#typesseq-mutable), that adds an element to the list it is called on,
- [`remove()`](https://docs.python.org/3/library/stdtypes.html#typesseq-mutable), that removes the first element of a list that matches the input, and
- [`reverse()`](https://docs.python.org/3/library/stdtypes.html#typesseq-mutable), that reverses the order of the elements in the list it is called on.

You'll be working on the list with the area of different parts of the house: `areas`.

`@instructions`
- Use [`append()`](https://docs.python.org/3/library/stdtypes.html#typesseq-mutable) twice to add the size of the poolhouse and the garage again: `24.5` and `15.45`, respectively. Make sure to add them in this order.
- Print out `areas`
- Use the [`reverse()`](https://docs.python.org/3/library/stdtypes.html#typesseq-mutable) method to reverse the order of the elements in `areas`.
- Print out `areas` once more.

`@hint`
- For the first instruction, use the `areas.append(___)` call twice.
- To print out a variable `x`, simply write `print(x)`.
- The [`reverse()`](https://docs.python.org/3/library/stdtypes.html#typesseq-mutable) method does not require additional inputs; just use the dot notation and empty parentheses: `.reverse()`.
- To print out a variable `x`, simply write `print(x)`.

`@pre_exercise_code`
```{python}
# pec
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
msg = "Use the `append()` method on `areas` to expand with `%s` the %s time."
test_function("areas.append", 1,
              not_called_msg = msg % ( "24.5", "first"),
              incorrect_msg = msg % ( "24.5", "first"))
test_function("areas.append", 2,
              not_called_msg = msg % ("15.45", "second"),
              incorrect_msg = msg % ("15.45", "second"))

msg = "Use the `reverse()` method on `areas` to reverse it. Don't forget the parantheses!"
test_function("areas.reverse",
              not_called_msg = msg,
              incorrect_msg = msg)

test_function("print", 1, incorrect_msg = "Don't forget to print out `areas` two times using `print(areas)`.")



test_function("print", 2, incorrect_msg = "Don't forget to print out `areas` two times using `print(areas)`.")

test_object("areas", incorrect_msg = "The final value of `areas` is not correct although you did the correct operations. Did you change the predefined variables?", undefined_msg = "Don't remove `areas`.")

success_msg("Great!")
```

---
## Packages

```yaml
type: VideoExercise
lang: python
xp: 50
skills: 2
key: 2b89c5a9d8
```

`@video_link`
//player.vimeo.com/video/146994272

`@video_hls`
//videos.datacamp.com/transcoded/735_intro_to_python/v1/hls-ch3_3.master.m3u8

*** =projector_key
c550d2f388d2718361d55e101c6c3887

---
## Import package

```yaml
type: NormalExercise
lang: python
xp: 100
skills: 2
key: 7432a6376f
```

As a data scientist, some notions of geometry never hurt. Let's refresh some of the basics.

For a fancy clustering algorithm, you want to find the circumference, $C$, and area, $A$, of a circle. When the radius of the circle is `r`, you can calculate $C$ and $A$ as:

$$C = 2 \pi r$$
$$A = \pi r^2 $$

To use the constant `pi`, you'll need the `math` package. A variable `r` is already coded in the script. Fill in the code to calculate `C` and `A` and see how the [`print()`](https://docs.python.org/3/library/functions.html#print) functions create some nice printouts.

`@instructions`
- Import the `math` package. Now you can access the constant `pi` with `math.pi`.
- Calculate the circumference of the circle and store it in `C`.
- Calculate the area of the circle and store it in `A`.

`@hint`
- You can simply use `import math`, and then refer to `pi` with `math.pi`.
- Use the equation in the assignment to find `C`. Use `*`
- Use the equation in the assignment to find `A`. Use `*` and `**`.

`@pre_exercise_code`
```{python}
# pec
```

`@sample_code`
```{python}
# Definition of radius
r = 0.43

# Import the math package


# Calculate C
C = 0

# Calculate A
A = 0

# Build printout
print("Circumference: " + str(C))
print("Area: " + str(A))
```

`@solution`
```{python}
# Definition of radius
r = 0.43

# Import the math package
import math

# Calculate C
C = 2 * r * math.pi

# Calculate A
A = math.pi * r ** 2

# Build printout
print("Circumference: " + str(C))
print("Area: " + str(A))
```

`@sct`
```{python}
msg = "You don't have to change or remove the predefined variables."
test_object("r", undefined_msg = msg, incorrect_msg = msg)
test_import("math", same_as = False)
test_object("C", incorrect_msg = "Your calculation of `C` is not quite correct. You should use `pi` of the `math` package using the dot notation (`.`).")
test_object("A", incorrect_msg = "Your calculation of `A` is not quite correct. You should use `pi` of the `math` package using the dot notation (`.`).")
msg = "You don't have to change or remove the predefined `print()` functions at the end."
test_function("print", 1, not_called_msg = msg, incorrect_msg = msg)
test_function("print", 2, not_called_msg = msg, incorrect_msg = msg)
success_msg("Nice!")
```

---
## Selective import

```yaml
type: NormalExercise
lang: python
xp: 100
skills: 2
key: fe65eff50a
```

General imports, like `import math`, make **all** functionality from the `math` package available to you. However, if you decide to only use a specific part of a package, you can always make your import more selective:

```
from math import pi
```

Let's say the Moon's orbit around planet Earth is a perfect circle, with a radius `r` (in km) that is defined in the script.

`@instructions`
- Perform a selective import from the `math` package where you only import the `radians` function.
- Calculate the distance travelled by the Moon over 12 degrees of its orbit. Assign the result to `dist`. You can calculate this as `r * phi`, where `r` is the radius and `phi` is the angle in radians. To convert an angle in degrees to an angle in radians, use the [`radians()`](https://docs.python.org/3/library/math.html#math.radians) function, which you just imported.
- Print out `dist`.

`@hint`
- Use `from math import radians` to do the selective import.
- You can simply use the [`radians()`](https://docs.python.org/3/library/math.html#math.radians) function now. Pass the function the number 12 to get the angle in radians.
- To print out a variable `x`, simply type `print(x)`.

`@pre_exercise_code`
```{python}
# pec
```

`@sample_code`
```{python}
# Definition of radius
r = 192500

# Import radians function of math package


# Travel distance of Moon over 12 degrees. Store in dist.


# Print out dist

```

`@solution`
```{python}
# Definition of radius
r = 192500

# Import radians function of math package
from math import radians

# Travel distance of Moon over 12 degrees. Store in dist.
dist = r * radians(12)

# Print out dist
print(dist)
```

`@sct`
```{python}
msg = "You don't have to change or remove the predefined variables."
test_object("r", undefined_msg = msg, incorrect_msg = msg)

test_import("math.radians", not_imported_msg = "Be sure to import [`radians()`](https://docs.python.org/3/library/math.html#math.radians) from the `math` package. You should use the `from ___ import ___` notation.", incorrect_as_msg = "Don't set any alias for [`radians()`](https://docs.python.org/3/library/math.html#math.radians). Just type `from math import radians`.")

test_object("dist", do_eval = False)
test_function("math.radians", 1, incorrect_msg = "Call [`radians()`](https://docs.python.org/3/library/math.html#math.radians) with argument `12`.", not_called_msg = "Your calculation of `dist` is not quite correct. You should use [`radians()`](https://docs.python.org/3/library/math.html#math.radians) from the `math` package. If you imported correctly, you don't have to use the dot (`.`) notation.")
test_object("dist", incorrect_msg = "Assign the result of your calculations to `dist`.")

test_function("print", incorrect_msg = "Make sure to print out `dist` using `print(dist)`.")

success_msg("Nice! Head over to the next exercise.")
```

---
## Different ways of importing

```yaml
type: MultipleChoiceExercise
lang: python
xp: 50
skills: 2
key: f1b2675a2a
```

There are several ways to import packages and modules into Python. Depending on the import call, you'll have to use different Python code.

Suppose you want to use the function [`inv()`](http://docs.scipy.org/doc/numpy-1.10.0/reference/generated/numpy.linalg.inv.html), which is in the `linalg` subpackage of the `scipy` package. You want to be able to use this function as follows:

```
my_inv([[1,2], [3,4]])
```

Which `import` statement will you need in order to run the above code without an error?

`@instructions`
- `import scipy`
- `import scipy.linalg`
- `from scipy.linalg import my_inv`
- `from scipy.linalg import inv as my_inv`

`@hint`
Try the different import statements in the IPython shell and see which one causes the line `my_inv([[1, 2], [3, 4]])` to run without errors.

`@pre_exercise_code`
```{python}
# pec
```

`@sct`
```{python}
msg1 = msg2 = msg3 = "Incorrect, try again. Try the different import statements in the IPython shell and see which one causes the line `my_inv([[1, 2], [3, 4]])` to run without errors."
msg4 = "Correct! The `as` word allows you to create a local name for the function you're importing: [`inv()`](https://docs.python.org/3/library/functions.html#inv) is now available as `my_inv()`."
test_mc(4, [msg1, msg2, msg3, msg4])
```

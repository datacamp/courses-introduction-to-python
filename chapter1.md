---
title_meta  : Chapter 1
title       : Python Basics
description : An introduction to the basic concepts of Python. Learn how to use Python both interactively and through a script. Create your first variables and acquaint yourself with Python's basic data types.
attachments :
  slides_link : https://s3.amazonaws.com/assets.datacamp.com/course/intro_to_python/ch1_slides.pdf


---
## Hello Python!

```yaml
type: VideoExercise
lang: python
xp: 50
skills: 2
key: d5509896f7
```

`@video_link`
//player.vimeo.com/video/146994261

`@video_hls`
//videos.datacamp.com/transcoded/735_intro_to_python/v2/hls-ch1_1.master.m3u8

*** =projector_key
5f61a677bf62c17b450465ee849823ee

---

## The Python Interface

```yaml
type: NormalExercise
lang: python
xp: 100
skills: 2
key: bdc52f0e19
```

In the Python script on the right, you can type Python code to solve the exercises. If you hit _Submit Answer_, your python script (`script.py`) is executed and the output is shown in the IPython Shell. DataCamp checks whether your submission is correct and gives you feedback.

You can hit _Submit Answer_ as often as you want. If you're stuck, you can click _Get Hint_, and ultimately _Get Solution_.

You can also use the IPython Shell interactively by simply typing commands and hitting Enter. When you work in the shell directly, your code will not be checked for correctness so it is a great way to experiment.

`@instructions`
- Experiment in the IPython Shell; type `5 / 8`, for example.
- Add another line of code to the Python script: `print(7 + 10)`.
- Hit _Submit Answer_ to execute the Python script and receive feedback.

`@hint`
Simply add `print(7 + 10)` in the script on the right and hit 'Submit Answer'.

`@pre_exercise_code`
```{python}
# pec comes here
```

`@sample_code`
```{python}
# Example, do not modify!
print(5 / 8)

# Put code below here

```

`@solution`
```{python}
# Example, do not modify!
print(5 / 8)

# Put code below here
print(7 + 10)
```

`@sct`
```{python}
msg = "Don't remove the first statement. It is an example which is coded for you!"
test_function("print", 1, not_called_msg = msg, incorrect_msg = msg)

msg = "Have you added `print(7 + 10)` to the script, in addition to the `print()` command that was already there?"
test_function("print", 2, not_called_msg = msg, incorrect_msg = msg)
success_msg("Great!")
```

---
## When to use Python?

```yaml
type: MultipleChoiceExercise
lang: python
xp: 50
skills: 2
key: 9703b117fb
```

Python is a pretty versatile language. For which applications can you use Python?

`@instructions`
- You want to do some quick calculations.
- For your new business, you want to develop a database-driven website.
- Your boss asks you to clean and analyze the results of the latest satisfaction survey.
- All of the above.

`@hint`
Filip mentioned in the video that Python can be used to build practically any piece of software.

`@pre_exercise_code`
```{python}
# pec comes here
```

`@sct`
```{python}
msg1 = "Incorrect. Python can do simple and quick calculations, but it is much more than that!"
msg2 = "Incorrect. There is a very popular framework to build database-driven websites (Django), but Python can do much more."
msg3 = "Incorrect. Python is a powerful tool to do data analysis, but you can also use it for other ends."
msg4 = "Correct! Python is an extremely versatile language."
test_mc(4, [msg1, msg2, msg3, msg4])

```

---
## Any comments?

```yaml
type: NormalExercise
lang: python
xp: 100
skills: 2
key: 7c4a738a13
```

Something that Filip didn't mention in his videos is that you can add **comments** to your Python scripts. Comments are important to make sure that you and others can understand what your code is about.

To add comments to your Python script, you can use the `#` tag. These comments are not run as Python code, so they will not influence your result. As an example, take the comment on the right, `# Just testing division`; it is completely ignored during execution.

`@instructions`
Above the `print(7 + 10)`, add the comment `# Addition works too`.

`@hint`
For this exercise you only have to add one line of comments. It won't run as Python code. Add `# Addition works too` right above `print(7 + 10)`.

`@pre_exercise_code`
```{python}
# pec comes here
```

`@sample_code`
```{python}
# Just testing division
print(5 / 8)


print(7 + 10)
```

`@solution`
```{python}
# Just testing division
print(5 / 8)

# Addition works too
print(7 + 10)
```

`@sct`
```{python}
test_student_typed("#\s*(\w+) works (\w+)[\s.!?]*print\(7", not_typed_msg = "Make sure to add the instructed comment right before `print(7+10)`.")
success_msg("Great!")
```

---
## Python as a calculator

```yaml
type: NormalExercise
lang: python
xp: 100
skills: 2
key: 0f7c039428
```

Python is perfectly suited to do basic calculations. Apart from addition, subtraction, multiplication and division, there is also support for more advanced operations such as:

- Exponentiation: `**`. This operator raises the number to its left to the power of the number to its right. For example `4**2` will give `16`.
- Modulo: `%`. This operator returns the remainder of the division of the number to the left by the number on its right. For example `18 % 7` equals `4`.

The code in the script on the right gives some examples.

`@instructions`
Suppose you have $100, which you can invest with a 10% return each year. After one year, it's $100 \times 1.1 = 110$ dollars, and after two years it's $100 \times 1.1 \times 1.1 = 121$. Add code on the right to calculate how much money you end up with after 7 years.

`@hint`
After two years you have $100 \times 1.1 \times 1.1 = 100 \times 1.1^2$. How much do you have after 7 years than? Use `*` and `**`.

`@pre_exercise_code`
```{python}
# pec comes here
```

`@sample_code`
```{python}
# Addition and subtraction
print(5 + 5)
print(5 - 5)

# Multiplication and division
print(3 * 5)
print(10 / 2)

# Exponentiation
print(4 ** 2)

# Modulo
print(18 % 7)

# How much is your $100 worth after 7 years?

```

`@solution`
```{python}
# Addition and subtraction
print(5 + 5)
print(5 - 5)

# Multiplication and division
print(3 * 5)
print(10 / 2)

# Exponentiation
print(4 ** 2)

# Modulo
print(18 % 7)

# How much is your $100 worth after 7 years?
print(100 * 1.1 ** 7)
```

`@sct`
```{python}
test_output_contains("194\\.8", no_output_msg = "Have you used the operation `100 * 1.1 ** 7` in a `print()` call?")
success_msg("Time for another video!")
```

---
## Variables & Types

```yaml
type: VideoExercise
lang: python
xp: 50
skills: 2
key: ef8356fb92
```

`@video_link`
//player.vimeo.com/video/154561704

`@video_hls`
//videos.datacamp.com/transcoded/735_intro_to_python/v1/hls-ch1_2.master.m3u8

*** =projector_key
7df0925250c5fb2a647cd76fb09d446e

---

## Variable Assignment

```yaml
type: NormalExercise
lang: python
xp: 100
skills: 2
key: 4bf65ad83e
```

In Python, a variable allows you to refer to a value with a name. To create a variable use `=`, like this example:

```
x = 5
```

You can now use the name of this variable, `x`, instead of the actual value, `5`.

Remember, `=` in Python means _assignment_, it doesn't test equality!

`@instructions`
- Create a variable `savings` with the value 100.
- Check out this variable by typing `print(savings)` in the script.

`@hint`
- Type `savings = 100` to create the variable `savings`.
- After creating the variable `savings`, you can type `print(savings)`.

`@pre_exercise_code`
```{python}
# pec
```

`@sample_code`
```{python}
# Create a variable savings


# Print out savings

```

`@solution`
```{python}
# Create a variable savings
savings = 100

# Print out savings
print(savings)
```

`@sct`
```{python}
test_object("savings", incorrect_msg = "Assign `100` to the variable `savings`.")
test_function("print", incorrect_msg = "Print out `savings`, the variable you created, using `print(savings)`.")
success_msg("Great! Let's try to do some calculations with this variable now!")
```

---
## Calculations with variables

```yaml
type: NormalExercise
lang: python
xp: 100
skills: 2
key: ff06cedeb4
```

Remember how you calculated the money you ended up with after 7 years of investing $100? You did something like this:

```
100 * 1.10 ** 7
```

Instead of calculating with the actual values, you can use variables instead. The `savings` variable you've created in the previous exercise represents the $100 you started with. It's up to you to create a new variable to represent `1.10` and then redo the calculations!

`@instructions`
- Create a variable `factor`, equal to `1.10`.
- Use `savings` and `factor` to calculate the amount of money you end up with after 7 years. Store the result in a new variable, `result`.
- Print out the value of `result`.

`@hint`
- To create the variable `factor`, use `factor = 1.10`.
- In the example code block of the assignment, replace `100` with `savings` and `1.10` with `factor`: `savings * factor ** 7`.
- Use the [`print()`](https://docs.python.org/3/library/functions.html#print) function to print the value of a variable.

`@pre_exercise_code`
```{python}
# pec
```

`@sample_code`
```{python}
# Create a variable savings
savings = 100

# Create a variable factor


# Calculate result


# Print out result
```

`@solution`
```{python}
# Create a variable savings
savings = 100

# Create a variable factor
factor = 1.1

# Calculate result
result = savings * factor ** 7

# Print out result
print(result)
```

`@sct`
```{python}
test_object("savings", undefined_msg = "The variable `savings` was defined for you, don't remove it!",
                       incorrect_msg = "The variable `savings` should be `100`, like it was defined for you.")
test_object("factor", incorrect_msg = "The value of `factor` should be `1.1`.")
test_object("result", incorrect_msg = "Have you used `*` and `**` to calculate `result`?")
msg = "Don't forget to print out `result` after assigning it."
test_print(not_called_msg = msg, incorrect_msg = msg)
success_msg("Great!")
```

---
## Other variable types

```yaml
type: NormalExercise
lang: python
xp: 100
skills: 2
key: 006b48561f
```

In the previous exercise, you worked with two Python data types:

- `int`, or integer: a number without a fractional part. `savings`, with the value `100`, is an example of an integer.
- `float`, or floating point: a number that has both an integer and fractional part, separated by a point. `factor`, with the value `1.10`, is an example of a float.

Next to numerical data types, there are two other very common data types:

- `str`, or string: a type to represent text. You can use single or double quotes to build a string.
- `bool`, or boolean: a type to represent logical values. Can only be `True` or `False` (the capitalization is important!).

`@instructions`
- Create a new string, `desc`, with the value `"compound interest"`.
- Create a new boolean, `profitable`, with the value `True`.

`@hint`
- To create a variable in Python, use `=`. Make sure to wrap your string in single or double quotes.
- Only two boolean values exist in Python: `True` and `False`. `TRUE`, `true`, `FALSE`, `false` and other versions will not be accepted.

`@pre_exercise_code`
```{python}
# pec
```

`@sample_code`
```{python}
# Create a variable desc


# Create a variable profitable

```

`@solution`
```{python}
# Create a variable desc
desc = "compound interest"

# Create a variable profitable
profitable = True
```

`@sct`
```{python}
test_object("desc", incorrect_msg = "Assign the value `\"compound interest\"` to the variable `desc`.")
test_object("profitable", incorrect_msg = "Assign the value `True` to the variable `profitable`.")

success_msg("Nice!")
```

---
## Guess the type

```yaml
type: MultipleChoiceExercise
lang: python
xp: 50
skills: 2
key: b35f67514c
```

To find out the type of a value or a variable that refers to that value, you can use the [`type()`](https://docs.python.org/3/library/functions.html#type) function. Suppose you've defined a variable `a`, but you forgot the type of this variable. To determine the type of `a`, simply execute:

```
type(a)
```

We already went ahead and created three variables: `a`, `b` and `c`. You can use the IPython shell on the right to discover their type. Which of the following options is correct?

`@instructions`
- `a` is of type `int`, `b` is of type `str`, `c` is of type `bool`
- `a` is of type `float`, `b` is of type `bool`, `c` is of type `str`
- `a` is of type `float`, `b` is of type `str`, `c` is of type `bool`
- `a` is of type `int`, `b` is of type `bool`, `c` is of type `str`

`@hint`
Use `type(a)`, `type(b)` and `type(c)` inside the IPython Shell to find out about the variables' types.

`@pre_exercise_code`
```{python}
a = 100*1.1**7
b = "True"
c = False
```

`@sct`
```{python}
msg1 = "The type of `a` is not `int`. Try out `type(a)` and see for yourself."
msg2 = "`b` is not a `bool`, it's a `str`! The fact that `True` is wrapped in double quotes makes it a string."
msg3 = "Correcto perfecto!"
msg4 = "None of the variable's types is correct here. Try `type(a)` and see what type this variable is."
test_mc(3,[msg1, msg2, msg3, msg4])
```

---
## Operations with other types

```yaml
type: NormalExercise
lang: python
xp: 100
skills: 2
key: 4d0d83cc02
```

Filip mentioned that different types behave differently in Python.

When you sum two strings, for example, you'll get different behavior than when you sum two integers or two booleans.

In the script some variables with different types have already been created. It's up to you to use them.

`@instructions`
- Calculate the product of `savings` and `factor`. Store the result in `year1`.
- What do you think the resulting type will be? Find out by printing out the type of `year1`.
- Calculate the sum of `desc` and `desc` and store the result in a new variable `doubledesc`.
- Print out `doubledesc`. Did you expect this?

`@hint`
- Assign `factor * savings` to a new variable, `year1`.
- To print the type of a variable `x`, use `print(type(x))`.
- Assign `desc + desc` to a new variable, `doubledesc`.
- To print a variable `x`, write `print(x)` in the script.

`@pre_exercise_code`
```{python}
# no pec
```

`@sample_code`
```{python}
# Several variables to experiment with
savings = 100
factor = 1.1
desc = "compound interest"

# Assign product of factor and savings to year1


# Print the type of year1


# Assign sum of desc and desc to doubledesc


# Print out doubledesc

```

`@solution`
```{python}
# Several variables to experiment with
savings = 100
factor = 1.1
desc = "compound interest"

# Assign product of savings and factor to year1
year1 = savings * factor

# Print the type of year1
print(type(year1))

# Assign sum of desc and desc to doubledesc
doubledesc = desc + desc

# Print out doubledesc
print(doubledesc)
```

`@sct`
```{python}
msg = "You don't have to change or remove the predefined variables."
test_object("savings", undefined_msg = msg, incorrect_msg = msg)
test_object("factor", undefined_msg = msg, incorrect_msg = msg)
test_object("desc", undefined_msg = msg, incorrect_msg = msg)
test_object("year1", incorrect_msg = "Multiply `savings` and `factor` to create the `year1` variable.")
msg = "Make sure to print out the type of `year1` like this: `print(type(year1))`."
test_function("print", 1, incorrect_msg = msg)
test_function("type", incorrect_msg = msg)
test_object("doubledesc", incorrect_msg  = "Have you stored the result of `desc + desc` in `doubledesc`?")
test_function("print", 2, incorrect_msg = "Be sure to print out `doubledesc`.")
success_msg("Nice. Notice how `desc + desc` causes `\"compound interest\"` and `\"compound interest\"` to be pasted together.")
```

---
## Type conversion

```yaml
type: NormalExercise
lang: python
xp: 100
skills: 2
key: 085bb602b9
```

Using the `+` operator to paste together two strings can be very useful in building custom messages.

Suppose, for example, that you've calculated the return of your investment and want to summarize the results in a string. Assuming the floats `savings` and `result` are defined, you can try something like this:

```
print("I started with $" + savings + " and now have $" + result + ". Awesome!")
```

This will not work, though, as you cannot simply sum strings and floats.

To fix the error, you'll need to explicitly convert the types of your variables. More specifically, you'll need [`str()`](https://docs.python.org/3/library/functions.html#func-str), to convert a value into a string. `str(savings)`, for example, will convert the float `savings` to a string.

Similar functions such as [`int()`](https://docs.python.org/3/library/functions.html#int), [`float()`](https://docs.python.org/3/library/functions.html#float) and [`bool()`](https://docs.python.org/3/library/functions.html#bool) will help you convert Python values into any type.

`@instructions`
- Hit _Submit Answer_ to run the code on the right. Try to understand the error message.
- Fix the code on the right such that the printout runs without errors; use the function [`str()`](https://docs.python.org/3/library/functions.html#func-str) to convert the variables to strings.
- Convert the variable `pi_string` to a float and store this float as a new variable, `pi_float`.

`@hint`
- You should use [`str()`](https://docs.python.org/3/library/functions.html#func-str) twice!
- Use [`float()`](https://docs.python.org/3/library/functions.html#float) on `pi_string` and store the result in `pi_float`.

`@pre_exercise_code`
```{python}
# pec
```

`@sample_code`
```{python}
# Definition of savings and result
savings = 100
result = 100 * 1.10 ** 7

# Fix the printout
print("I started with $" + savings + " and now have $" + result + ". Awesome!")

# Definition of pi_string
pi_string = "3.1415926"

# Convert pi_string into float: pi_float

```

`@solution`
```{python}
# Definition of savings and result
savings = 100
result = 100 * 1.10 ** 7

# Fix the printout
print("I started with $" + str(savings) + " and now have $" + str(result) + ". Awesome!")

# Definition of pi_string
pi_string = "3.1415926"

# Convert pi_string into float: pi_float
pi_float = float(pi_string)
```

`@sct`
```{python}

# ensure predefined values are unmodified
msg = "You don't have to change or remove the predefined variables."
test_object("savings", undefined_msg = msg, incorrect_msg = msg)
test_object("result", undefined_msg = msg, incorrect_msg = msg)

# check correctly converted `result` and `savings` in printed string.
test_function("str", 1, incorrect_msg = "On the line with `print()`, make sure to change `savings` to `str(savings)`.")
test_function("str", 2, incorrect_msg = "On the line with `print()`, make sure to changed `result` to  `str(result)`.")
test_function("print", incorrect_msg = "The string you're trying to print is not quite right. Have another look at the description of this problem.")

# ensure predefined pi_string is unmodified
msg = "You shouldn't have to change or remove the predefined variable `pi_string`."
test_object("pi_string", undefined_msg = msg, incorrect_msg = msg)

# check pi_float
test_function("float",
              not_called_msg = "In order to convert `pi_string` to a float, be sure to use the `float()` function.",
              incorrect_msg = "Pass `pi_string` to [`float()`](https://docs.python.org/3/library/functions.html#float) in order to convert it to a float.")
test_object("pi_float",
             incorrect_msg = "It looks like you used `float` correctly, but the value of `pi_float` is incorrect.",
             undefined_msg = "It looks like you used `float` correctly, but did not assign the result to `pi_float`")

success_msg("Great! You have a profit of around $95; that's pretty awesome indeed!")
```

---
## Can Python handle everything?

```yaml
type: MultipleChoiceExercise
lang: python
xp: 50
skills: 2
key: 3e5f0bdf3a
```

Now that you know something more about combining different sources of information, have a look at the four Python expressions below.
Which one of these will throw an error? You can always copy and paste this code in the IPython Shell to find out!

`@instructions`
- `"I can add integers, like "  + str(5) + " to strings."`
- `"I said " + ("Hey " * 2) + "Hey!"`
- `"The correct answer to this multiple choice exercise is answer number " + 2`
- `True + False`

`@hint`
Copy and paste the different expressions into the IPython Shell and try to figure out which one throws an error.

`@pre_exercise_code`
```{python}
# pec
```

`@sct`
```{python}
msg1 = msg2 = msg4 = "Incorrect, this command runs perfectly fine."
msg3 = "Correct! Because you're not converting `2` to a string with [`str()`](https://docs.python.org/3/library/functions.html#func-str), this will give an error."
test_mc(3, [msg1, msg2, msg3, msg4])
```

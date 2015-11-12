---
title_meta  : Chapter 1
title       : Python Basics
description : An introduction to the basic concepts of Python and its place in the Data Science community

--- type:VideoExercise lang:python xp:50 skills:2
## First steps into Python

*** =video_link
```{python}
//player.vimeo.com/video/108225030
```

--- type:NormalExercise lang:python xp:100 skills:2
## The Python Interface

In the Python script on the right, you can type Python code to solve the exercises. If you hit _Submit Answer_, your python script is executed and the output is shown in the IPython Shell. DataCamp checks whether your submission is correct and gives you feedback.

You can hit _Submit Answer_ as often as you want: you will not loose any experience points. If you're stuck, you can ask for the Hint, and ultimately the Solution. This will cost you XP points, though.

You can also use the IPython Shell interactively: simply type commands and hit Enter. When you work in the shell directly, your code will not be checked for correctness: a great way to experiment.

*** =instructions
- Experiment in the IPython Shell: type 5 / 8, for example.
- Add another line of code to the Python script that prints out the sum of `7 and 10`.
- Hit _Submit Answer_ to execute the python script and receive feedback.

*** =hint
- Simply add `print(7 + 10)` in the script on the right and hit 'Submit Answer'.

*** =pre_exercise_code
```{python}
# pec comes here
```

*** =sample_code
```{python}
print(5 / 8)
```

*** =solution
```{python}
print(5 / 8)
print(7 + 10)
```

*** =sct
```{python}
# TODO VINCENT SCT MAGIC
success_msg("Well done!")
```

--- type:MultipleChoiceExercise lang:python xp:50 skills:2
## When to use Python?

Python is a pretty versatile language. For what applications can you use Python?

*** =instructions
- You want to do some quick calculations.
- For your new business, you want to develop a database-driven website.
- Your boss asks you to clean and analyze the results of the latest satisfaction survey.
- All of the above

*** =hint
- Filip mentioned in the video that Python can be used to build practically any piece of software.

*** =pre_exercise_code
```{python}
# pec comes here
```

*** =sct
```{python}
# TODO VINCENT SCT MAGIC
msg1 = "Incorrect. Python can do simple and quick calculations, but it is much more than that!" 
msg2 = "Incorrect. There is a very popular framework to build database-driven websites (Django), but Python can do much more."
msg3 = "Incorrect. Python is a powerful tool to do data analysis, but you can also use it for other ends."
msg4 = "Correct! Python is an extremely versatile language."
success_msg("Replace me")
```

--- type:NormalExercise lang:python xp:100 skills:2
## Any comments?

Something that Filip didn't mention in his videos, is that you can add comments to your Python scripts. Comments are important to make sure that you and others can understand what your code is about.

To add comments to your Python script, you can use the `#` tag. These comments are not run as Python code, so they will not influence your result. As an example, take the comment on the right, `# Just testing division`: it is completely ignored during execution.

*** =instructions
- Above the `print(7 + 10)`, add the comment `Addition works too`.

*** =hint
hint comes here

*** =pre_exercise_code
```{python}
# pec comes here
```

*** =sample_code
```{python}
# Just testing division
print(5 / 8)


print(7 + 10)
```

*** =solution
```{python}
# Just testing division
print(5 / 8)

# Addition works too
print(7 + 10)
```

*** =sct
```{python}
# TODO VINCENT SCT MAGIC - MAKE SURE THAT ALL KINDS ARE ACCEPTED: 
# lowercase, uppercase, 2 instead of too, to instead of too and so on.
success_msg("Great!")
```

--- type:NormalExercise lang:python xp:100 skills:2
## Python as a calculator

Python is perfectly suited to do basic calculations. Apart from addition, subtraction, multiplication and division, there is also support for more advanced operations:

- Exponentiation: `**`. This operator raises the number to its left to the power of the number to its right: for example `4**2` will give `16`.
- Modulo: `%%`. It returns the remainder of the division of the number to the left by the number on its right, for example `18 %% 7` equals `4`.

The code in the script on the right gives some examples.

*** =instructions
- Suppose you have `$100`, which you can invest with a 10\% return each year. After one year, it's $100 \times 1.1 = 110$ dollars, and after two years it's $100 \times 1.1 \times 1.1 = 121$. Add code on the right to calculate how much money you end up with after 7 years.

*** =hint
- After two years you have $100 \times 1.1 \times 1.1 = 100 \times 1.1 ** 2$. How much do you have after 7 years than? Use `*` and `**`.

*** =pre_exercise_code
```{python}
# pec comes here
```

*** =sample_code
```{python}
# Addition and subtraction
5 + 5 
5 - 5 

# Multiplication and division
3 * 5
10 / 2 

# Exponentiation
4 ** 2

# Modulo
18 %% 7

# How much is your $100 worth after 7 years?
```

*** =solution
```{python}
# Addition and subtraction
5 + 5 
5 - 5 

# Multiplication and division
3 * 5
10 / 2 

# Exponentiation
4 ** 2

# Modulo
18 %% 7

# How much is your $100 worth after 7 years?
100 * 1.1 ** 7
```

*** =sct
```{python}
# TODO VINCENT SCT MAGIC
success_msg("Time for another video!")
```

--- type:VideoExercise lang:python xp:50 skills:2
## Variables and types

*** =video_link
```{python}
//player.vimeo.com/video/108225030
```

--- type:NormalExercise lang:python xp:100 skills:2
## Variable Assignment

In Python, a variable allows you to refer to a value with a name. To create a variable, use `=`:

```
x = 5
```

You can now use the name of this variable, `x`, instead of the actual value, `5`.

*** =instructions
- Create a variable `begin` with the value 100.
- Check out this variable by typing `print(begin)` in the script.

*** =hint
- Type `begin = 100`.
- After creating the variable `begin`, you can type `print(begin)`.

*** =pre_exercise_code
```{python}
# pec
```

*** =sample_code
```{python}
# Create a variable begin


# Print out begin

```

*** =solution
```{python}
# Create a variable begin
begin = 100

# Print out begin
print(begin)
```

*** =sct
```{python}
# TODO VINCENT SCT MAGIC
success_msg("Great! Let's try to do some calculations with this variable now!")
```

--- type:NormalExercise lang:python xp:100 skills:2
## Calculations with variables

Remember how you calculated the money you ended up with after 7 years of investing \$100? You did something like this:

```
100 * 1.10 ** 7
```

Instead of calculating with the actual values, you can use variables instead. The `begin` variable you've created in the previous exercise represents the \$100 you started with. Up to you to create a new variable to represent `1.10` and then redo the calculations!

*** =instructions
- Create a variable `mult`, equal to `1.10`. 
- Use `begin` and `mult` to calculate the amount of money you end up with after 7 years. Store the result in a new variable, `result`.
- Print out the value of `result`.

*** =hint
- To create the variable `mult`, use `mult = 1.10`.
- In the example code block of the assignment, replace `100` with `begin` and `1.10` with `mult`: `begin * mult ** 7`.
- Use the `print()` function to print the value of a variable.

*** =pre_exercise_code
```{python}
# pec
```

*** =sample_code
```{python}
# Create a variable begin
begin = 100

# Create a variable mult


# Calculate result

```

*** =solution
```{python}
# Create a variable begin
begin = 100

# Create a variable mult
mult = 1.1

# Calculate result
result = begin * mult ** 7

# Print out result
print(result)
```

*** =sct
```{python}
# TODO VINCENT SCT MAGIC
success_msg("Awesome! If you now change `begin` and submit your script again, `result` will change as well.")
```

--- type:NormalExercise lang:python xp:100 skills:2
## Other variable types

In the previous exercise, you have worked with two Python data types:

- `int`, or integer: numerical value without a decimal part. `begin`, with the value `100` is an example.
- `float`: numerical value that has both an integer and decimal part. `mult`, with the value `1.10` is a float.

Next to numerical data types, there are two other very common data types:

- `str`, or string: type to represent text. You use double quotes to build a string.
- `bool`, or boolean: type to represent logical values. Can only be `True` or `False`.

*** =instructions
- Create a new string, `desc`, with the value `"compound interest"`.
- Create a new boolean, `profitable`, with the value `True`.

*** =hint
- To create a variable in Python, use `=`. Make sure to wrap your string in single or double quotes.
- Only two boolean values exist in Python: `True` and `False`. `TRUE`, `true`, `FALSE`, `false` and other versions will not be accepted.

*** =pre_exercise_code
```{python}
# pec
```

*** =sample_code
```{python}
# Create a variable desc


# Create a variable profitable

```

*** =solution
```{python}
# Create a variable desc
desc = "compound interest"

# Create a variable profitable
profitable = True
```

*** =sct
```{python}
# TODO VINCENT SCT MAGIC
success_msg("Nice!")
```

--- type:MultipleChoiceExercise lang:python xp:50 skills:2
## What's that type?

To found out the class of a value or a variable that refers to that value, you can use the `type()` function. Suppose you've defined a variable `a`, but you forgot the type of this variable. Simply executing

```
type(a)
```

will tell you the type of `a`.

We already went ahead and created three variables: `result`, `better` and `worse`. You can use the IPython shell on the right to discover their type. Which of the following options is correct?

*** =instructions
- `result` is of type `int`, `better` is of type `str`, `worse` is of type `bool`
- `result` is of type `float`, `better` is of type `bool`, `worse` is of type `str`
- `result` is of type `float`, `better` is of type `str`, `worse` is of type `bool`
- `result` is of type `int`, `better` is of type `bool`, `worse` is of type `str`

*** =hint
Use `type(result)`, `type(better)` and `type(worse)` inside the IPython Shell to find out about the variables' types.

*** =pre_exercise_code
```{python}
result = 100*1.1**7
better = "True"
worse = False
```

*** =sct
```{python}
msg1 = "The type of `result` is not `int`. Try out `type(result)` and see for yourself."
msg2 = "`better` is not a `bool`, it's a `str`! The fact that `True` is wrapped in double quotes makes it a string."
msg3 = "Correcto perfecto!"
msg4 = "None of the variable's types is correct here. Try `type(result)` and see what type this variable is."
success_msg("Replace me")
```

--- type:NormalExercise lang:python xp:100 skills:2
## Operations with other types

Filip mentioned that differnt types behave differently when you work with them.

When you sum two strings for example, you'll get different behavior then when you sum two integers or two booleans.

In the script, some variables with different types have already been created. Up to you get operational on them.

*** =instructions
- Print out the result of `2 * begin`.
- Print out the result of `mult * begin`.
- Print out the result of `desc + desc`
- Print out the result of `profitable * 5`

*** =hint
- Inside the python script, write `print(2 * begin)`.
- Put `mult * begin` inside the `print()` function.
- Put `desc + desc` inside the `print()` function.
- Put `profitable * 5` inside the `print()` function.

*** =pre_exercise_code
```{python}
# no pec
```

*** =sample_code
```{python}
# Several variables to experiment with
begin = 100
mult = 1.1
desc = "compound interest"
profitable = True

# Print out result of 2 * begin


# Print out result of mult * begin


# Print out result of desc + desc


# Print out result of profitable * 5
```

*** =solution
```{python}
# Several variables to experiment with
begin = 100
mult = 1.1
desc = "compound interest"
profitable = True

# Print out result of 2 * begin
print(2 * begin)

# Print out result of mult * begin
print(mult * begin)

# Print out result of desc + desc
print(desc + desc)

# Print out result of profitable * 5
print(profitable * 5)
```

*** =sct
```{python}
# TODO VINCENT SCT MAGIC
success_msg("Nice. Notice how `desc + desc` causes the strings to be pasted together. The boolean `True` is treated as 1 if you try to do calculations.")
```

--- type:NormalExercise lang:python xp:100 skills:2
## Type conversion

The `+` operator to paste together two strings can be very useful in building up custom messages.

Suppose for example that you've calculated the return of your investment, and want to summarise the results in a string. Assuming the floats `begin` and `result` are defined, you can try something like this:

```
print("I started with $" + begin + " and now have $" + result + ". Awesome!")
```

This will not work, though, as you cannot simply sum strings and floats. To do this, you'll need to explicitly convert the types of your variables. You can use the functions `str()`, `int()`, `float()` and `bool()` for this. `str(begin)`, for example, will convert the float `begin` to a string.

*** =instructions
- Fix the code on the right such that the printout runs without errors.
- Convert the variable `pi_string` to a float, and store this float a new varialbe, `pi_float`.

*** =hint
- You should use `str()` twice!
- Use `float()` on `pi_string` and store the result in `pi_float`.

*** =pre_exercise_code
```{python}
# pec
```

*** =sample_code
```{python}
# Definition of begin and result
begin = 100
result = 100 * 1.10 ** 7

# Fix the printout
print("I started with $" + begin + " and now have $" + result + ". Awesome!")

# Definition of pi_string
pi_string = "3.1415926"

# Convert pi_string into float: pi_float

```

*** =solution
```{python}
# Definition of begin and result
begin = 100
result = 100 * 1.10 ** 7

# Fix the printout
print("I started with $" + str(begin) + " and now have $" + str(result) + ". Awesome!")

# Definition of pi_string
pi_string = "3.1415926"

# Convert pi_string into float: pi_float
pi_float = str(pi_string)
```

*** =sct
```{python}
# TODO VINCENT SCT MAGIC
success_msg("Great! You have a profit of around \$95, that's pretty awesome indeed!")
```

--- type:MultipleChoiceExercise lang:python xp:50 skills:2
## Can Python handle everything?

Now that you know something more about combining different sources of information, have a look at the 4 Python expressions below.
Which one of these will throw an error? You can always copy and paste this code in the IPython Shell to find out!

*** =instructions
- `"The correct answer to this multiple choice exercise is answer number " + 2`
- `"I can add integers, like "  + str(5) + " to strings."`
- `"I said " + ("Hey " * 2) + "Hey!"`
- `True + False`

*** =hint
- Copy and paste the different expressions into the IPython Shell and try to figure out which one throws an error.

*** =pre_exercise_code
```{python}
# pec
```

*** =sct
```{python}
msg1 = "Correct! Because you're not converting `2` to a string with `str()`, this will give an error."
msg2 = msg3 = msg4 = "Incorrect, this command runs perfectly fine."
success_msg("Replace me")
```


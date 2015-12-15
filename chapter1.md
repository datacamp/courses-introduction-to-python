---
title_meta  : Chapter 1
title       : Python Basics
description : An introduction to the basic concepts of Python. Learn to use Python both interatively and through a script. Create your first variables and acquaint yourself with Python's basic data types.
attachments :
  slides_link : https://s3.amazonaws.com/assets.datacamp.com/course/intro_to_python/ch1_slides.pdf
  
--- type:VideoExercise lang:python xp:50 skills:2
## Hello Python!

*** =video_link
//player.vimeo.com/video/146994261

--- type:NormalExercise lang:python xp:100 skills:2
## The Python Interface

In the Python script on the right, you can type Python code to solve the exercises. If you hit _Submit Answer_, your python script (`my_script.py`) is executed and the output is shown in the IPython Shell. DataCamp checks whether your submission is correct and gives you feedback.

You can hit _Submit Answer_ as often as you want: you will not loose any experience points. If you're stuck, you can click _Get Hint_, and ultimately _Get Solution_.

You can also use the IPython Shell interactively: simply type commands and hit Enter. When you work in the shell directly, your code will not be checked for correctness: a great way to experiment.

*** =instructions
- Experiment in the IPython Shell: type 5 / 8, for example.
- Add another line of code to the Python script (`my_script.py`) that prints out the sum of `7` and `10`.
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
msg = "Don't remove the first statement. It is an example which is coded for you!"
test_operator(1, incorrect_op_msg = msg, incorrect_result_msg = msg, not_found_msg = msg)
test_function("print", 1, not_called_msg = msg, incorrect_msg = msg)

test_operator(2, not_found_msg = "You should add a second operation, as instructed.", 
  incorrect_op_msg = "Your second operation is wrong, be sure to add `7` to `10`.",
  incorrect_result_msg = "The operation you added should add up to `17`.")
test_function("print", 2,
  not_called_msg = "Remember that you should call `print()` to print out the result of your calculation.",
  incorrect_msg = "You should type `print(7 + 10)` to print out the result of your calculation.")

success_msg("Great!")
```

--- type:MultipleChoiceExercise lang:python xp:50 skills:2
## When to use Python?

Python is a pretty versatile language. For what applications can you use Python?

*** =instructions
- You want to do some quick calculations.
- For your new business, you want to develop a database-driven website.
- Your boss asks you to clean and analyze the results of the latest satisfaction survey.
- All of the above.

*** =hint
- Filip mentioned in the video that Python can be used to build practically any piece of software.

*** =pre_exercise_code
```{python}
# pec comes here
```

*** =sct
```{python}
msg1 = "Incorrect. Python can do simple and quick calculations, but it is much more than that!" 
msg2 = "Incorrect. There is a very popular framework to build database-driven websites (Django), but Python can do much more."
msg3 = "Incorrect. Python is a powerful tool to do data analysis, but you can also use it for other ends."
msg4 = "Correct! Python is an extremely versatile language."
test_mc(4, [msg1, msg2, msg3, msg4])

```

--- type:NormalExercise lang:python xp:100 skills:2
## Any comments?

Something that Filip didn't mention in his videos, is that you can add comments to your Python scripts. Comments are important to make sure that you and others can understand what your code is about.

To add comments to your Python script, you can use the `#` tag. These comments are not run as Python code, so they will not influence your result. As an example, take the comment on the right, `# Just testing division`: it is completely ignored during execution.

*** =instructions
- Above the `print(7 + 10)`, add the comment `# Addition works too`.

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
test_student_typed("#\s*(\w+) works (\w+)\s*print\(7", not_typed_msg = "Make sure to add the instructed comment right before `print(7+10)`.")
success_msg("Great!")
```

--- type:NormalExercise lang:python xp:100 skills:2
## Python as a calculator

Python is perfectly suited to do basic calculations. Apart from addition, subtraction, multiplication and division, there is also support for more advanced operations:

- Exponentiation: `**`. This operator raises the number to its left to the power of the number to its right: for example `4**2` will give `16`.
- Modulo: `%`. It returns the remainder of the division of the number to the left by the number on its right, for example `18 % 7` equals `4`.

The code in the script on the right gives some examples.

*** =instructions
Suppose you have $100, which you can invest with a 10% return each year. After one year, it's $100 \times 1.1 = 110$ dollars, and after two years it's $100 \times 1.1 \times 1.1 = 121$. Add code on the right to calculate how much money you end up with after 7 years.

*** =hint
- After two years you have $100 \times 1.1 \times 1.1 = 100 \times 1.1^2$. How much do you have after 7 years than? Use `*` and `**`.

*** =pre_exercise_code
```{python}
# pec comes here
```

*** =sample_code
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

*** =solution
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

*** =sct
```{python}
msg = "You don't have to change the predefined code. Just add one line at the bottom!"
for i in range(1,7):
  test_operator(i, not_found_msg = msg, incorrect_op_msg = msg, incorrect_result_msg = msg)
  test_function("print", index = i, not_called_msg = msg, incorrect_msg = msg)

test_operator(7, not_found_msg = "Add an operation to calculate what's instructed.", 
  incorrect_op_msg = "You should use at least one '*' and one '**' operator to calculate what's instructed.",
  incorrect_result_msg = "You should calculate the total interest on 100 dollar after 7 years given a 10% rate.")
test_function("print", index = 7, 
  not_called_msg = "Don't forget to print out your result with `print()`.",
  incorrect_msg = "Print out your result using `print(100 * 1.1 ** 7)`.")

success_msg("Time for another video!")
```

--- type:VideoExercise lang:python xp:50 skills:2
## Variables & Types

*** =video_link
//player.vimeo.com/video/146994263

--- type:NormalExercise lang:python xp:100 skills:2
## Variable Assignment

In Python, a variable allows you to refer to a value with a name. To create a variable, use `=`, like this example:

```
x = 5
```

You can now use the name of this variable, `x`, instead of the actual value, `5`.

*** =instructions
- Create a variable `savings` with the value 100.
- Check out this variable by typing `print(savings)` in the script.

*** =hint
- Type `savings = 100` to create the variable `savings`.
- After creating the variable `savings`, you can type `print(savings)`.

*** =pre_exercise_code
```{python}
# pec
```

*** =sample_code
```{python}
# Create a variable savings


# Print out savings

```

*** =solution
```{python}
# Create a variable savings
savings = 100

# Print out savings
print(savings)
```

*** =sct
```{python}
test_object("savings", incorrect_msg = "Assign `100` to the variable `savings`.")
test_function("print", incorrect_msg = "Print out `savings`, the variable you created, using `print(savings)`.")
success_msg("Great! Let's try to do some calculations with this variable now!")
```

--- type:NormalExercise lang:python xp:100 skills:2
## Calculations with variables

Remember how you calculated the money you ended up with after 7 years of investing \$100? You did something like this:

```
100 * 1.10 ** 7
```

Instead of calculating with the actual values, you can use variables instead. The `savings` variable you've created in the previous exercise represents the \$100 you started with. Up to you to create a new variable to represent `1.10` and then redo the calculations!

*** =instructions
- Create a variable `factor`, equal to `1.10`. 
- Use `savings` and `factor` to calculate the amount of money you end up with after 7 years. Store the result in a new variable, `result`.
- Print out the value of `result`.

*** =hint
- To create the variable `factor`, use `factor = 1.10`.
- In the example code block of the assignment, replace `100` with `savings` and `1.10` with `factor`: `savings * factor ** 7`.
- Use the `print()` function to print the value of a variable.

*** =pre_exercise_code
```{python}
# pec
```

*** =sample_code
```{python}
# Create a variable savings
savings = 100

# Create a variable factor


# Calculate result


# Print out result
```

*** =solution
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

*** =sct
```{python}
test_object("savings", undefined_msg = "The variable `savings` was defined for you, don't remove it!",
                       incorrect_msg = "The variable `savings` should be `100`, like it was defined for you.")
                       
test_object("factor", incorrect_msg = "The value of `factor` should be `1.1`.")
test_object("result", do_eval = False)
test_operator(3, not_found_msg = "Have you used the correct calculations to calculate `result`?",
                 incorrect_op_msg = "Use '*' and '**' to calculate result.",
                 incorrect_result_msg = "Have you used to correct variables to calculate result?")
test_object("result", incorrect_msg = "Assign the correct value to `result`.")
test_function("print", incorrect_msg = "You should print out the result using `print(result)`.")
success_msg("Great!")
```

--- type:NormalExercise lang:python xp:100 skills:2
## Other variable types

In the previous exercise, you have worked with two Python data types:

- `int`, or integer: number without a fractional part. `savings`, with the value `100` is an example.
- `float`, or floating point: number that has both an integer and fractional part, separated by a point. `factor`, with the value `1.10` is a float.

Next to numerical data types, there are two other very common data types:

- `str`, or string: type to represent text. You can use single and double quotes to build a string.
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
test_object("desc", incorrect_msg = "Assign the value `\"compound interest\"` to the variable `desc`.")
test_object("profitable", incorrect_msg = "Assign the value `True` to the variable `profitable`.")

success_msg("Nice!")
```

--- type:MultipleChoiceExercise lang:python xp:50 skills:2
## Guess the type

To find out the type of a value or a variable that refers to that value, you can use the `type()` function. Suppose you've defined a variable `a`, but you forgot the type of this variable. Simply executing

```
type(a)
```

will tell you the type of `a`.

We already went ahead and created three variables: `a`, `b` and `c`. You can use the IPython shell on the right to discover their type. Which of the following options is correct?

*** =instructions
- `a` is of type `int`, `b` is of type `str`, `c` is of type `bool`
- `a` is of type `float`, `b` is of type `bool`, `c` is of type `str`
- `a` is of type `float`, `b` is of type `str`, `c` is of type `bool`
- `a` is of type `int`, `b` is of type `bool`, `c` is of type `str`

*** =hint
Use `type(a)`, `type(b)` and `type(c)` inside the IPython Shell to find out about the variables' types.

*** =pre_exercise_code
```{python}
a = 100*1.1**7
b = "True"
c = False
```

*** =sct
```{python}
msg1 = "The type of `a` is not `int`. Try out `type(a)` and see for yourself."
msg2 = "`b` is not a `bool`, it's a `str`! The fact that `True` is wrapped in double quotes makes it a string."
msg3 = "Correcto perfecto!"
msg4 = "None of the variable's types is correct here. Try `type(a)` and see what type this variable is."
test_mc(3,[msg1, msg2, msg3, msg4])
```

--- type:NormalExercise lang:python xp:100 skills:2
## Operations with other types

Filip mentioned that different types behave differently in Python.

When you sum two strings for example, you'll get different behavior than when you sum two integers or two booleans.

In the script, some variables with different types have already been created. Up to you to use them.

*** =instructions
- Calculate the product of `savings` and `factor`. Store the result in `year1`.
- What do you think the resulting type will be? Find out by printing the type of `year1`.
- Calculate the sum of `desc` and `desc` and store the result in a new variable `doubledesc`.
- Print out `doubledesc`. Did you expect this?

*** =hint
- Assign `factor * savings` to a new variable, `year1`.
- To print the type of a variable `x`, use `print(type(x))`.
- Assign `desc + desc` to a new variable, `doubledesc`.
- To print a variable `x`, write `print(x)` in the script.

*** =pre_exercise_code
```{python}
# no pec
```

*** =sample_code
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

*** =solution
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

*** =sct
```{python}
msg = "You don't have to change or remove the predefined variables."
test_object("savings", undefined_msg = msg, incorrect_msg = msg)
test_operator(1, not_found_msg = msg, incorrect_op_msg = msg, incorrect_result_msg = msg)
test_object("factor", undefined_msg = msg, incorrect_msg = msg)
test_operator(2, not_found_msg = msg, incorrect_op_msg = msg, incorrect_result_msg = msg)
test_object("desc", undefined_msg = msg, incorrect_msg = msg)


test_object("year1", do_eval = False)
test_operator(3, not_found_msg = "Calculate `year1` using the `*` operator.",
                 incorrect_op_msg = "To calculate `year1`, you should use `*` once.",
                 incorrect_result_msg = "You should use `savings` and `factor` to calculate `year1`. Take a look at the hint if you're stuck.")
test_object("year1", incorrect_msg = "Assign the correct value you calculated to `year1`.")

msg = "Make sure to print out the type of `year1` like this: `print(type(year1))`."
test_function("type", incorrect_msg = msg)
test_function("print", 1, incorrect_msg = msg)

test_object("doubledesc", do_eval = False)
msg = "You can add up a string to another string, just type `desc + desc`."
test_operator(4, not_found_msg = msg, incorrect_op_msg = msg, incorrect_result_msg = msg)
test_object("doubledesc", incorrect_msg  = "Assign the resulting string to `doubledesc`.")

test_function("print", 2, incorrect_msg = "Be sure to print out `double_desc`.")
success_msg("Nice. Notice how `desc + desc` causes `\"compound interest\"` and `\"compound interest\"` to be pasted together.")
```

--- type:NormalExercise lang:python xp:100 skills:2
## Type conversion

The `+` operator to paste together two strings can be very useful in building up custom messages.

Suppose for example that you've calculated the return of your investment, and want to summarize the results in a string. Assuming the floats `savings` and `result` are defined, you can try something like this:

```
print("I started with $" + savings + " and now have $" + result + ". Awesome!")
```

This will not work, though, as you cannot simply sum strings and floats. 

To fix the error, you'll need to explicitly convert the types of your variables. More specifically, you'll need `str()`, to convert a value into a string. `str(savings)`, for example, will convert the float `savings` to a string. 

Similar functions such as `int()`, `float()` and `bool()` will help you convert Python values into any type.

*** =instructions
- Hit _Submit Answer_ to run the code on the right. Try to understand the error message.
- Fix the code on the right such that the printout runs without errors; use the function `str()` to convert the variables to strings.
- Convert the variable `pi_string` to a float, and store this float as a new variable, `pi_float`.

*** =hint
- You should use `str()` twice!
- Use `float()` on `pi_string` and store the result in `pi_float`.

*** =pre_exercise_code
```{python}
# pec
```

*** =sample_code
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

*** =solution
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

*** =sct
```{python}
msg = "You don't have to change or remove the predefined variables."
test_object("savings", undefined_msg = msg, incorrect_msg = msg)
test_operator(1, not_found_msg = msg, incorrect_op_msg = msg, incorrect_result_msg = msg)
test_object("result", undefined_msg = msg, incorrect_msg = msg)
test_operator(2, not_found_msg = msg, incorrect_op_msg = msg, incorrect_result_msg = msg)

test_function("str", 1, incorrect_msg = "You should use `str(savings)` first.")
test_function("str", 2, incorrect_msg = "You should use `str(result)` the second time.")
msg = "To form the long string, you can use the `+` operator. The only thing you have to edit in the printout is that you have to convert `savings` and `result` to strings."
test_operator(3, not_found_msg = msg, incorrect_op_msg = msg, incorrect_result_msg = msg)
test_function("print", incorrect_msg = "The string you're trying to print is not quite right. Have another look at the description of this problem.")

msg = "You don't have to change or remove the predefined variables."
test_object("pi_string", undefined_msg = msg, incorrect_msg = msg)

test_object("pi_float", do_eval = False)
test_function("float", incorrect_msg = "Pass `pi_string` to `float()` in order to convert it to a float.")
test_object("pi_float", incorrect_msg = "Assign the correct value to `pi_float`.")

success_msg("Great! You have a profit of around $95; that's pretty awesome indeed!")
```

--- type:MultipleChoiceExercise lang:python xp:50 skills:2
## Can Python handle everything?

Now that you know something more about combining different sources of information, have a look at the 4 Python expressions below.
Which one of these will throw an error? You can always copy and paste this code in the IPython Shell to find out!

*** =instructions
- `"I can add integers, like "  + str(5) + " to strings."`
- `"I said " + ("Hey " * 2) + "Hey!"`
- `"The correct answer to this multiple choice exercise is answer number " + 2`
- `True + False`

*** =hint
- Copy and paste the different expressions into the IPython Shell and try to figure out which one throws an error.

*** =pre_exercise_code
```{python}
# pec
```

*** =sct
```{python}
msg1 = msg2 = msg4 = "Incorrect, this command runs perfectly fine."
msg3 = "Correct! Because you're not converting `2` to a string with `str()`, this will give an error."
test_mc(3, [msg1, msg2, msg3, msg4])
```


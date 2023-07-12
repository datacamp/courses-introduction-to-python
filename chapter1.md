---
title_meta: Chapter 1
title: Python Basics
description: >-
  An introduction to the basic concepts of Python. Learn how to use Python
  interactively and by using a script. Create your first variables and acquaint
  yourself with Python's basic data types.
attachments:
  slides_link: 'https://projector-video-pdf-converter.datacamp.com/735/chapter1.pdf'
free_preview: true
lessons:
  - nb_of_exercises: 5
    title: Hello Python!
  - nb_of_exercises: 8
    title: Variables and Types
---

## Hello Python!

```yaml
type: VideoExercise
key: f644a48d5d
xp: 50
```

`@projector_key`
d8fcd4c930027fa4e1c3870c7e7e0ff1

---

## When to use Python?

```yaml
type: MultipleChoiceExercise
key: 9703b117fb
lang: python
xp: 50
skills:
  - 2
```

Python is a **flexible** language. For which applications can you use Python?

`@possible_answers`
- For quick calculations.
- Develop a database-driven website.
- Clean and analyze data.
- All of the above.

`@hint`
- Practically any piece of software can be built using Python.

`@pre_exercise_code`
```{python}

```

`@sct`
```{python}
msg1 = "Python can do more than quick calculations!"
msg2 = "There is a very popular Python framework to build database-driven websites, but it can do much more."
msg3 = "Python is a powerful tool for data analysis, but it has other uses, too."
msg4 = "Correct! Python is an extremely flexible language."
Ex().has_chosen(4, [msg1, msg2, msg3, msg4])
```

---

## The Python Interface

```yaml
type: NormalExercise
key: bdc52f0e19
lang: python
xp: 100
skills:
  - 2
```

Hit _Run Code_ to run your first Python code with Datacamp and see the output!

Notice the `script.py` window; this is where you can type Python code to solve exercises. You can hit _Run Code_ and _Submit Answer_ as often as you want. If you're stuck, you can click _Get Hint_, and ultimately _Get Solution_.

You can also use the IPython Shell interactively by typing commands and hitting Enter. Here, your code will not be checked for correctness so it is a great way to experiment.

`@instructions`
- Experiment in the IPython Shell; type `5 / 8`, for example.
- Add another line of code to `script.py`, `print(7 + 10)`, to be checked for correctness.
- Hit _Submit Answer_ to execute the Python script and receive feedback.

`@hint`
- Add `print(7 + 10)` under `# Print the sum of 7 and 10` and hit _Submit Answer_ to check if your code is correct.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Example, do not modify!
print(5 / 8)

# Print the sum of 7 and 10
____
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
Ex().has_printout(1, not_printed_msg = "__JINJA__:Have you used `{{sol_call}}` to print out the sum of 7 and 10?")
success_msg("Great! On to the next one!")
```

---

## Any comments?

```yaml
type: NormalExercise
key: 7c4a738a13
lang: python
xp: 100
skills:
  - 2
```

Something that Hugo didn't mention in his videos is that you can add **comments** to your Python scripts. Comments are important to make sure that you and others can understand what your code is about.

To add comments to your Python script, you can use the `#` tag. These comments are not run as Python code, so they will not influence your result. As an example, take the comment in the editor, `# Division`; it is completely ignored during execution.

`@instructions`
Above the `print(7 + 10)`, add the comment 
```
# Addition
```

`@hint`
For this exercise you only have to add one line of comments. It won't run as Python code. Add `# Addition` right above `print(7 + 10)`.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Division
print(5 / 8)


print(7 + 10)
```

`@solution`
```{python}
# Division
print(5 / 8)

# Addition
print(7 + 10)
```

`@sct`
```{python}
Ex().has_code("#\s*(\w+)[\s.!?]*print\s*\(\s*7", not_typed_msg = "Make sure to add the comment right before `print(7 + 10)`.")
success_msg("Great!")
```

---

## Python as a calculator

```yaml
type: NormalExercise
key: 0f7c039428
lang: python
xp: 100
skills:
  - 2
```

Python is perfectly suited to do basic calculations. It can do addition, subtraction, multiplication and division.

The code in the script gives some examples.

Now it's your turn to practice!

`@instructions`
- Print the sum of `4 + 5`.
- Print the result of subtracting `5` from `5`.
- Multiply `3` by `5`.
- Divide `10` by `2`.

`@hint`
- You'll need to use `print()` to generate an output.

`@pre_exercise_code`
```{python}
 
```

`@sample_code`
```{python}
# Addition


# Subtraction


# Multiplication


# Division

```

`@solution`
```{python}
# Addition
print(4 + 5)

# Subtraction
print(5 - 5)

# Multiplication
print(3 * 5)

# Division
print(10 / 2)
```

`@sct`
```{python}
Ex().has_printout(0, not_printed_msg = "Have you used `print(4 + 5)` to print out the result of your sum?")

Ex().has_printout(1, not_printed_msg = "Have you used `print(5 - 5)` to print out the result of your subtration?")

Ex().has_printout(2, not_printed_msg = "Have you used `print(3 * 5)` to print out the result of your multiplication?")

Ex().has_printout(3, not_printed_msg = "Have you used `print(10 / 2)` to print out the result of your division?")

success_msg("That's correct! Python can help you do the math, a characteristic that will be helpful for analysis as we grow our data skills.")
```

---

## Variables and Types

```yaml
type: VideoExercise
key: c2e396792e
xp: 50
```

`@projector_key`
433dcfcfedaee070cbf440491c402e3b

---

## Variable Assignment

```yaml
type: NormalExercise
key: 4bf65ad83e
lang: python
xp: 100
skills:
  - 2
```

In Python, a variable allows you to refer to a value with a name. To create a variable `x` with a value of `5`, you use `=`, like this example:

```
x = 5
```

You can now use the name of this variable, `x`, instead of the actual value, `5`.

Remember, `=` in Python means _assignment_, it doesn't test equality!

`@instructions`
- Create a variable `savings` with the value of `100`.
- Check out this variable by typing `print(savings)` in the script.

`@hint`
- Type `savings = 100` to create the variable `savings`.
- After creating the variable `savings`, you can type `print(savings)`.

`@pre_exercise_code`
```{python}
 
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
Ex().check_object("savings").has_equal_value(incorrect_msg="Assign `100` to the variable `savings`.")
Ex().has_printout(0, not_printed_msg = "Print out `savings`, the variable you created, with `print(savings)`.")
success_msg("Great! Let's try to do some calculations with this variable now!")
```

---

## Calculations with variables

```yaml
type: NormalExercise
key: ff06cedeb4
lang: python
xp: 100
skills:
  - 2
```

You've now created a savings variable, so let's start saving!

Instead of calculating with the actual values, you can use variables instead. The `savings` variable you created in the previous exercise with a value of `100` is available to you.

How much money would you have saved four months from now, if you saved $10 each month?

`@instructions`
- Create a variable `monthly_savings`, equal to `10` and `num_months`, equal to `4`.
- Multiply `monthly_savings` by `num_months` and save it to `new_savings`.
- Add `new_savings` to `savings`, saving the sum as `total_savings`.
- Print the value of `total_savings`.

`@hint`
- You can do calculations with variables the same way as with numbers so instead of `10 * 4`, replace the numbers with the variables!
- Use `print()` to see the amount in `total_savings`.

`@pre_exercise_code`
```{python}
savings = 100
```

`@sample_code`
```{python}
# Create the variables monthly_savings and num_months



# Multiply monthly_savings and num_months
new_savings = ____

# Add new_savings to your savings
total_savings = ____

# Print total_savings

```

`@solution`
```{python}
# Create the variables monthly_savings and num_months
monthly_savings = 10
num_months = 4

# Multiply monthly_savings and num_months
new_savings = monthly_savings * num_months

# Add new_savings to your savings
total_savings = savings + new_savings

# Print total_savings
print(total_savings)
```

`@sct`
```{python}
Ex().check_object("monthly_savings").has_equal_value(incorrect_msg = "Did you save `10` to `monthly_savings` using `monthly_savings = 10`?")
Ex().check_object("num_months").has_equal_value(incorrect_msg = "Did you save `4` to `num_months` using `num_months = 4`?")
Ex().check_object("new_savings").has_equal_value(incorrect_msg = "Did you use the correct variables and symbols to multiply? Expected `monthly_savings * num_months` but got something else.")
Ex().check_object("total_savings").has_equal_value(incorrect_msg = "Did you use the correct variables and symbols to add? Expected `savings + new_savings` but got something else.")

Ex().has_printout(0, not_printed_msg="Remember to print out `total_savings` at the end of your script.")

success_msg("You now have $140 in savings!")
```

---

## Other variable types

```yaml
type: NormalExercise
key: 006b48561f
lang: python
xp: 100
skills:
  - 2
```

In the previous exercise, you worked with two Python data types:

- `int`, or integer: a number without a fractional part. `savings`, with the value `100`, is an example of an integer.
- `float`, or floating point: a number that has both an integer and fractional part, separated by a point. `growth_multiplier`, with the value `1.1`, is an example of a float.

Next to numerical data types, there are two other very common data types:

- `str`, or string: a type to represent text. You can use single or double quotes to build a string.
- `bool`, or boolean: a type to represent logical values. It can only be `True` or `False` (the capitalization is important!).

`@instructions`
- Create a new string, `desc`, with the value `"compound interest"`.
- Create a new boolean, `profitable`, with the value `True`.

`@hint`
- To create a variable in Python, use `=`. Make sure to wrap your string in single or double quotes.
- Only two boolean values exist in Python: `True` and `False`. `TRUE`, `true`, `FALSE`, `false` and other versions will not be accepted.

`@pre_exercise_code`
```{python}

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
Ex().check_object("desc").has_equal_value(incorrect_msg = "Hmm, something is incorrect in your `desc` variable. Double check the spelling and make sure you've used quotation marks.")
Ex().check_object("profitable").has_equal_value(incorrect_msg = "Did you capitalize the boolean value? Remember you don't need to use quotation marks here.")
success_msg("Nice!")
```

---

## Guess the type

```yaml
type: MultipleChoiceExercise
key: b35f67514c
lang: python
xp: 50
skills:
  - 2
```

To find out the type of a value or a variable that refers to that value, you can use the [`type()`](https://docs.python.org/3/library/functions.html#type) function. Suppose you've defined a variable `a`, but you forgot the type of this variable. To determine the type of `a`, simply execute:

```
type(a)
```

We already went ahead and created three variables: `a`, `b` and `c`. You can use the IPython shell to discover their type. Which of the following options is correct?

`@possible_answers`
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
Ex().has_chosen(3,[msg1, msg2, msg3, msg4])
```

---

## Operations with other types

```yaml
type: NormalExercise
key: 4d0d83cc02
lang: python
xp: 100
skills:
  - 2
```

Hugo mentioned that different types behave differently in Python.

When you sum two strings, for example, you'll get different behavior than when you sum two integers or two booleans.

In the script some variables with different types have already been created. It's up to you to use them.

`@instructions`
- Calculate the product of `savings` and `growth_multiplier`. Store the result in `year1`.
- What do you think the resulting type will be? Find out by printing out the type of `year1`.
- Calculate the sum of `desc` and `desc` and store the result in a new variable `doubledesc`.
- Print out `doubledesc`. Did you expect this?

`@hint`
- Assign `growth_multiplier * savings` to a new variable, `year1`.
- To print the type of a variable `x`, use `print(type(x))`.
- Assign `desc + desc` to a new variable, `doubledesc`.
- To print a variable `x`, write `print(x)` in the script.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
savings = 100
growth_multiplier = 1.1
desc = "compound interest"

# Assign product of savings and growth_multiplier to year1


# Print the type of year1


# Assign sum of desc and desc to doubledesc


# Print out doubledesc

```

`@solution`
```{python}
savings = 100
growth_multiplier = 1.1
desc = "compound interest"

# Assign product of savings and growth_multiplier to year1
year1 = savings * growth_multiplier

# Print the type of year1
print(type(year1))

# Assign sum of desc and desc to doubledesc
doubledesc = desc + desc

# Print out doubledesc
print(doubledesc)
```

`@sct`
```{python}
# predefined
msg = "You don't have to change or remove the predefined variables."

Ex().multi(
    check_object('savings', missing_msg=msg).has_equal_value(incorrect_msg=msg),
    check_object('growth_multiplier', missing_msg=msg).has_equal_value(incorrect_msg=msg),
    check_object('desc', missing_msg=msg).has_equal_value(incorrect_msg=msg)
)

# check year1 and printout
Ex().multi(
    check_object("year1").has_equal_value(incorrect_msg="Multiply `savings` and `growth_multiplier` to create the `year1` variable."),
    has_printout(0, not_printed_msg = "__JINJA__:Use `{{sol_call}}` to print out the type of `year1`.")
)

# check doubledesc and printout
Ex().multi(
    check_object("doubledesc").has_equal_value(incorrect_msg  = "Have you stored the result of `desc + desc` in `doubledesc`?"),
    has_printout(1, not_printed_msg = "Don't forget to print out `doubledesc`.")
)

success_msg("Nice. Notice how `desc + desc` causes `\"compound interest\"` and `\"compound interest\"` to be pasted together.")
```

---

## Type conversion

```yaml
type: NormalExercise
key: 085bb602b9
lang: python
xp: 100
skills:
  - 2
```

Using the `+` operator to paste together two strings can be very useful in building custom messages.

Suppose, for example, that you've calculated the return of your investment and want to summarize the results in a string.

To do this, you'll need to explicitly convert the types of your variables so that they are all strings. More specifically, you'll need [`str()`](https://docs.python.org/3/library/functions.html#func-str), to convert a value into a string. `str(savings)`, for example, will convert the integer `savings` to a string.

Similar functions such as [`int()`](https://docs.python.org/3/library/functions.html#int), [`float()`](https://docs.python.org/3/library/functions.html#float) and [`bool()`](https://docs.python.org/3/library/functions.html#bool) will help you convert Python values into any type.

`@instructions`
- Hit _Run Code_ to run the code. Try to understand the error message.
- Fix the code such that the printout runs without errors; use the function [`str()`](https://docs.python.org/3/library/functions.html#func-str) to convert the variables `savings` and `results` to strings.
- Convert the variable `pi_string` to a float and store this float as a new variable, `pi_float`.

`@hint`
- The error message when you _Run Code_ for the first time is telling you that you have an error in line 6 where at least one of your variables is not a string.
- You should use [`str()`](https://docs.python.org/3/library/functions.html#func-str) twice!
- Use [`float()`](https://docs.python.org/3/library/functions.html#float) on `pi_string` and store the result in `pi_float`.

`@pre_exercise_code`
```{python}

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
pi_float = 
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
Ex().multi(
    check_object("savings", missing_msg=msg).has_equal_value(incorrect_msg=msg),
    check_object("result", missing_msg=msg).has_equal_value(incorrect_msg=msg)
)

Ex().check_correct(
    has_printout(0),
    multi(
        check_function("str", 0).check_args(0).has_equal_value(incorrect_msg="Inside the `print()` command, make sure to convert `savings` into a string with `str(savings)`."),
        check_function("str", 1).check_args(0).has_equal_value(incorrect_msg="Inside the `print()` command, make sure to convert `result` into a string `str(result)`.")
    )
)

# check pi_float
Ex().check_correct(
    check_object("pi_float").has_equal_value(),
    multi(
        check_object("pi_string").has_equal_value(),
        check_function("float", missing_msg = "In order to convert `pi_string` to a float, be sure to use the `float()` function.").has_equal_value(incorrect_msg="Use `float(pi_string) to create the variable `pi_float`.")
    )
)

success_msg("Great! You have a profit of around $95; that's pretty awesome indeed!")
```

---

## Can Python handle everything?

```yaml
type: MultipleChoiceExercise
key: 3e5f0bdf3a
lang: python
xp: 50
skills:
  - 2
```

Now that you know something more about combining different sources of information, have a look at the four Python expressions below.
Which one of these will throw an error? You can always copy and paste this code in the IPython Shell to find out!

`@possible_answers`
- `"I can add integers, like "  + str(5) + " to strings."`
- `"I said " + ("Hey " * 2) + "Hey!"`
- `"The correct answer to this multiple choice exercise is answer number " + 2`
- `True + False`

`@hint`
Copy and paste the different expressions into the IPython Shell and try to figure out which one throws an error.

`@pre_exercise_code`
```{python}

```

`@sct`
```{python}
msg1 = "Incorrect, this command runs perfectly fine."
msg2 = "It's perfectly possible to 'multiply strings' in Python..."
msg3 = "Correct! Because you're not converting `2` to a string with [str()](https://docs.python.org/3/library/functions.html#func-str), this will give an error."
msg4 = "`True + False` doesn't error out. Feel free to try it in the console to confirm!"
Ex().has_chosen(3, [msg1, msg2, msg3, msg4])
```

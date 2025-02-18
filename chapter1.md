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
  - nb_of_exercises: 3
    title: Hello Python!
  - nb_of_exercises: 5
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

## Your first Python code

```yaml
type: NormalExercise
key: bdc52f0e19
lang: python
xp: 100
skills:
  - 2
```

It's time to run your first Python code!

Head to the code and hit the run code button to see the output.

`@instructions`
- Hit the run code button to see the output of `print(5 / 8)`.

`@hint`
- Run the code first before submitting your answer so you have time to explore the output.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Hit run code to see the output!
print(5 / 8)
```

`@solution`
```{python}
# Hit run code to see the output!
print(5 / 8)
```

`@sct`
```{python}
Ex().has_printout(0, not_printed_msg = "__JINJA__:Have you used `{{sol_call}}` to print out `5 / 8`?")
success_msg("Great! On to the next one!")
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

Now it's your turn to practice by writing some code yourself.

`@instructions`
- Fill in `print()` to subtract `5` from `5`.
- Now, write `print()` to fill it in to print the result of multiplying `3` by `5`.

`@hint`
- Write the calculation within the parentheses, `()`; e.g. `print(2-2)`.
- You can subtract with `-` and multiply with `*`.

`@pre_exercise_code`
```{python}
 
```

`@sample_code`
```{python}
# Examples of addition and division
print(4 + 5)
print(10 / 2)

# Fill in print() to subtract 5 - 5
print()

# Write print() and fill it in to multiply 3 * 5

```

`@solution`
```{python}
# Examples of addition and division
print(4 + 5)
print(10 / 2)

# Fill in print() to subtract 5 - 5
print(5 - 5)

# Write print() and fill it in to multiply 3 * 5
print(3 * 5)
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

Remember, `=` in Python means _assignment_, it doesn't test equality! Try it in the exercise by replacing `____` with your code.

`@instructions`
- Create a variable `savings` with the value of `100`.
- Check out this variable by typing `print(savings)` in the script.

`@hint`
- Type `savings = 100` to create the variable `savings`.
- After creating the variable `savings`, you can type `print(savings)`.
- Your final code should not include any `____`.

`@pre_exercise_code`
```{python}
 
```

`@sample_code`
```{python}
# Create a variable savings
____

# Print out savings
____
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

Instead of calculating with the actual values, you can use variables instead.

How much money would you have saved four months from now, if you saved $10 each month?

`@instructions`
- Create a variable `monthly_savings`, equal to `10` and `num_months`, equal to `4`.
- Multiply `monthly_savings` by `num_months` and assign it to `new_savings`.
- Print the value of `new_savings`.

`@hint`
- You can do calculations with variables the same way as with numbers so instead of `10 * 4`, replace the numbers with the variables!
- Use `print()` to see the amount in `new_savings`.
- Take care to spell the variables correctly!

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create the variables monthly_savings and num_months



# Multiply monthly_savings and num_months
new_savings = ____

# Print new_savings

```

`@solution`
```{python}
# Create the variables monthly_savings and num_months
monthly_savings = 10
num_months = 4

# Multiply monthly_savings and num_months
new_savings = monthly_savings * num_months

# Print new_savings
print(new_savings)
```

`@sct`
```{python}
Ex().check_object("monthly_savings").has_equal_value(incorrect_msg = "Did you save `10` to `monthly_savings` using `monthly_savings = 10`?")
Ex().check_object("num_months").has_equal_value(incorrect_msg = "Did you save `4` to `num_months` using `num_months = 4`?")
Ex().check_object("new_savings").has_equal_value(incorrect_msg = "Did you use the correct variables and symbols to multiply? Expected `monthly_savings * num_months` but got something else.")
# Ex().check_object("total_savings").has_equal_value(incorrect_msg = "Did you use the correct variables and symbols to add? Expected `savings + new_savings` but got something else.")

Ex().has_printout(0, not_printed_msg="Remember to print out `new_savings` at the end of your script.")

success_msg("You have $40 in new savings!")
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

In the previous exercise, you worked with the integer Python data type:

- `int`, or integer: a number without a fractional part. `savings`, with the value `100`, is an example of an integer.

Next to numerical data types, there are three other very common data types:

- `float`, or floating point: a number that has both an integer and fractional part, separated by a point. `1.1`, is an example of a float.
- `str`, or string: a type to represent text. You can use single or double quotes to build a string.
- `bool`, or boolean: a type to represent logical values. It can only be `True` or `False` (the capitalization is important!).

`@instructions`
- Create a new float, `half`, with the value `0.5`.
- Create a new string, `intro`, with the value `"Hello! How are you?"`.
- Create a new boolean, `is_good`, with the value `True`.

`@hint`
- To create a variable in Python, use `=`. Make sure to wrap your string in single or double quotes.
- Only two boolean values exist in Python: `True` and `False`. `TRUE`, `true`, `FALSE`, `false` and other versions will not be accepted.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create a variable half


# Create a variable intro


# Create a variable is_good

```

`@solution`
```{python}
# Create a variable half
half = 0.5

# Create a variable intro
intro = "Hello! How are you?"

# Create a variable is_good
is_good = True
```

`@sct`
```{python}
Ex().check_object("half").has_equal_value(incorrect_msg = "Did you save the float, `0.5` to `half`?")

Ex().check_object("intro").has_equal_value(incorrect_msg = "Hmm, something is incorrect in your `intro` variable. Double check the spelling and make sure you've used quotation marks.")

Ex().check_object("is_good").has_equal_value(incorrect_msg = "Did you capitalize the boolean value? Remember you don't need to use quotation marks here.")

success_msg("Nice!")
```

---

## Operations with other types

```yaml
type: BulletExercise
key: 4d0d83cc02
xp: 100
```

Variables come in different types in Python. You can see the type of a variable by using `type()`. For example, to see type of `a`, execute: `type(a)`.

Different types behave differently in Python. When you sum two strings, for example, you'll get different behavior than when you sum two integers or two booleans.

Time for you to test this out.

`@pre_exercise_code`
```{python}

```

***

```yaml
type: NormalExercise
key: f4e91c4ae9
xp: 50
```

`@instructions`
- Add `savings` and `new_savings` and assign it to `total_savings`.
- Use `type()` to print the resulting type of `total_savings`.

`@hint`
- Assign `savings + new_savings` to a new variable, `total_savings`.
- To print the type of a variable `x`, use `print(type(x))`.

`@sample_code`
```{python}
savings = 100
new_savings = 40

# Calculate total_savings using savings and new_savings
____
print(total_savings)

# Print the type of total_savings
print(____)
```

`@solution`
```{python}
savings = 100
new_savings = 40

# Calculate total_savings using savings and new_savings
total_savings = savings + new_savings
print(total_savings)

# Print the type of total_savings
print(type(total_savings))
```

`@sct`
```{python}
# predefined
msg = "You don't have to change or remove the predefined variables."

Ex().multi(
    check_object('savings', missing_msg=msg).has_equal_value(incorrect_msg=msg),
    check_object('new_savings', missing_msg=msg).has_equal_value(incorrect_msg=msg)
)

Ex().multi(
    check_object("total_savings").has_equal_value(incorrect_msg="Add `savings` and `new_savings` to create the `total_savings` variable."),
    has_printout(0, not_printed_msg = "__JINJA__:Use `{{sol_call}}` to print out the type of `total_savings`.")
)
```

***

```yaml
type: NormalExercise
key: f54fbf9bd9
xp: 50
```

`@instructions`
- Calculate the sum of `intro` and `intro` and assign the result to `doubleintro`.
- Print out `doubleintro`. Did you expect this?

`@hint`
- Assign `intro + intro` to a new variable, `doubleintro`.
- To print a variable `x`, write `print(x)` in the script.

`@sample_code`
```{python}
intro = "Hello! How are you?"

# Assign sum of intro and intro to doubleintro
____

# Print out doubleintro
print(____)
```

`@solution`
```{python}
intro = "Hello! How are you?"

# Assign sum of intro and intro to doubleintro
doubleintro = intro + intro

# Print out doubleintro
print(doubleintro)
```

`@sct`
```{python}
# predefined
msg = "You don't have to change or remove the predefined variables."

Ex().check_object('intro', missing_msg=msg).has_equal_value(incorrect_msg=msg)

Ex().multi(
    check_object("doubleintro").has_equal_value(incorrect_msg  = "Have you stored the result of `intro + intro` in `doubleintro`?"),
    has_printout(0, not_printed_msg = "Don't forget to print out `doubleintro`.")
)

success_msg("Nice. Notice how `intro + intro` causes `\"Hello! How are you?\"` and `\"Hello! How are you?\"` to be pasted together.")
```

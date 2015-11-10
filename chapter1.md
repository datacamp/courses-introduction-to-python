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

--- type:NormalExercise lang:python xp:50 skills:2
## The Python Interface

In the Python script editor on the right, you can type Python code to solve the exercises. If you hit _Submit Answer_, your python script is executed and the output is shown in the IPython Shell. DataCamp checks whether your submission is correct and gives you feedback.

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
success_msg("Great!")
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

- Exponentiation: `^`. The `^` operator raises the number to its left to the power of the number to its right: for example `4^2` will give `16`.
- Modulo: `%%`. `%%` returns the remainder of the division of the number to the left by the number on its right, for example `18 %% 7` equals `4`.

The code in the editor on the right gives some examples.

*** =instructions
- Suppose you have `$100`, which you can invest with a 10\% return each year. After one year, it's $100 \times 1.1 = 110$ dollars, and after two years it's $100 \times 1.1 \times 1.1 = 121$. Add code on the right to calculate how much money you end up with after 7 years.

*** =hint
- After two years you have $100 \times 1.1 \times 1.1 = 100 \times 1.1 ^ 2$.
- How much do you have after 7 years than? Use `*` and `^`.

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
100 * 1.1 ^ 7
```

*** =sct
```{python}
# TODO VINCENT SCT MAGIC
success_msg("Time for another video!")
```

--- type:VideoExercise lang:python xp:50 skills:2
## Variables and types

Introducing variables and variable assignment. The difference between types of variables (using strings and booleans).

*** =video_link
```{python}
//player.vimeo.com/video/108225030
```

--- type:MultipleChoiceExercise lang:python xp:50 skills:2
## Which is what

A list of variables is given with a value. Choose the choice which correctly lists their types.

*** =instructions
- option 1
- option 2
- option 3

*** =hint
hint comes here

*** =pre_exercise_code
```{python}
# pec comes here
```

*** =sct
```{python}
test_mc(2) # if 2 is the correct option.
```

--- type:NormalExercise lang:python xp:100 skills:2
## Assign all the variables

Instead of remembering the cost of the tab you decide to assign it to a variable for later use. There is one new person whos name you can't seem to remember so you decide to decide his name to a variable as well. Finally you decide to assign a boolean variable to remember the fact whether you were drunk or not.

*** =instructions
- instruction 1
- instruction 2

*** =hint
hint comes here

*** =pre_exercise_code
```{python}
# pec comes here
```

*** =sample_code
```{python}
# sample code comes here
```

*** =solution
```{python}
# Solution code
```

*** =sct
```{python}
# sct code comes here
```


--- type:NormalExercise lang:python xp:100 skills:2
## Calculations with variables

You wake up the next morning with the variables still in your memory. You decide to calculate how much you should pay Josh who paid the whole tab. You decide to give him somewhat extra based on that amount.

*** =instructions
- instruction 1
- instruction 2

*** =hint
hint comes here

*** =pre_exercise_code
```{python}
# pec comes here
```

*** =sample_code
```{python}
# sample code comes here
```

*** =solution
```{python}
# Solution code
```

*** =sct
```{python}
# sct code comes here
```


--- type:NormalExercise lang:python xp:100 skills:2
## Invalid calculations

You find some other variables in your memory of which you have little memory. You decide to check out what their type is. After finding out their type you decide to experiment with them a little bit.

*** =instructions
- instruction 1
- instruction 2

*** =hint
hint comes here

*** =pre_exercise_code
```{python}
# pec comes here
```

*** =sample_code
```{python}
# sample code comes here
```

*** =solution
```{python}
# Solution code
```

*** =sct
```{python}
# sct code comes here
```


--- type:MultipleChoiceExercise lang:python xp:50 skills:2
## Which are valid and which aren't

You are given a list of variables and operations on them. Select which one will result in an error.

*** =instructions
- option 1
- option 2
- option 3

*** =hint
hint comes here

*** =pre_exercise_code
```{python}
# pec comes here
```

*** =sct
```{python}
test_mc(2) # if 2 is the correct option.
```

--- type:NormalExercise lang:python xp:100 skills:2
## Did we pay everything? 

Given the total amount of the tab. Also given - an amount that everyone wants to pay. Do they sum up to the total amount?

*** =instructions
- instruction 1
- instruction 2

*** =hint
hint comes here

*** =pre_exercise_code
```{python}
# pec comes here
```

*** =sample_code
```{python}
# sample code comes here
```

*** =solution
```{python}
# Solution code
```

*** =sct
```{python}
# sct code comes here
```



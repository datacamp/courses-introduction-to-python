---
title_meta  : Chapter 2
title       : Lists
description : Add chapter description here.

--- type:VideoExercise lang:python xp:50 skills:2
## Lists, what are they?

*** =video_link
//player.vimeo.com/video/108225030

--- type:NormalExercise lang:python xp:100 skills:2
## Create a list

As opposed to `int`, `bool` etc, a list is a _compound data type_: you can group together values.

To create a list you use square brackets and commas, like this:

```
my_list = ["my", "first", "list"]
```

You can also use variables you've created beforehand:

```
a = 2
b = 4
my_list = [a, b]
```

After measuring the height of your family, you decide to collect some information on the house you're living in. The areas of the different parts of your crib are stored in separate variables for now, as shown in the script.

*** =instructions
- Create a list, `areas`, that contains the area of the hallway, kitchen, living room, bedroom and bathroom, in this order.
- Print `areas` with the `print()` function.

*** =hint
- You can use the variables that have already been created to build the list: `areas = [hallway, kitchen, ...]`.
- Put `print(areas)` in your script to print out the list when submitting.

*** =pre_exercise_code
```{python}
# pec
```

*** =sample_code
```{python}
# area variables (in square meters)
hallway = 11.25
kitchen = 18.0
living = 20.0
bedroom = 10.75
bathroom = 9.50

# Create list areas


# Print areas


```

*** =solution
```{python}
# area variables (in square meters)
hallway = 11.25
kitchen = 18.0
living = 20.0
bedroom = 10.75
bathroom = 9.50

# Create list areas
areas = [hallway, kitchen, living, bedroom, bathroom]

# Print areas
print(areas)
```

*** =sct
```{python}
#TODO VINCENT SCT MAGIC
success_msg("Nice! A list is way better here, isn't it?")
```

--- type:NormalExercise lang:python xp:100 skills:2
## Create list with different types

A list can contain any Python type. Although it's not really common, a list can also contain different types: you can strings, floats and booleans, all in the same list. 

The printout of the previous exercise wasn't really satisfying: it's just a list of numbers representing the areas, but you can't tell which area corresponds to which part of your house.

*** =instructions
- Finish the line of code that creates the `areas` list such that the list first contains the name of each room as a string, and then its area.
- Print `areas` again; is the printout more informative this time?

*** =hint
- The strings `"living room"` and `"bathroom"` have already been placed into the list. Do the same thing for `"hallway"`, `"kitchen"` and `"bedroom"`.
- To print `areas`, simply type `print(areas)`.

*** =pre_exercise_code
```{python}
# pec
```

*** =sample_code
```{python}
# area variables (in square meters)
hallway = 11.25
kitchen = 18.0
living = 20.0
bedroom = 10.75
bathroom = 9.50

# Adapt list areas
areas = [hallway, kitchen, "living room", living, bedroom, "bathroom", bathroom]

# Print areas

```

*** =solution
```{python}
# area variables (in square meters)
hallway = 11.25
kitchen = 18.0
living = 20.0
bedroom = 10.75
bathroom = 9.50

# Adapt list areas
areas = ["hallway", hallway, "kitchen", kitchen, "living room", living, "bedroom", bedroom, "bathroom", bathroom]

# Print areas
print(areas)
```

*** =sct
```{python}
# TODO VINCENT SCT MAGIC
success_msg("Nice! This list contains both strings and floats, but that's not a problem for Python!")
```

--- type:MultipleChoiceExercise lang:python xp:50 skills:2
## Select the valid list

A list can contain any Python type. But a list itself is also a Python type. That means that a list can also contain a list! Python is getting funkier by the minute, but fear not, just remember the list syntax:

```
my_list = [el1, el2, el3]
```

Can you tell which ones of the following lines of Python code are valid ways to build a list?

A. `[1 3 4 2]`  
B. `[[1, 2, 3], [4, 5, 7]]`  
C. `[1 + 2, "a" * 5, 3]`  


*** =instructions
- A, B and C
- B
- B and C
- C

*** =hint
Try out all the different lines in the Python shell and see which ones generate an error. Maybe none of them go wrong?

*** =pre_exercise_code
```{python}
# pec
```

*** =sct
```{python}
# TODO VINCENT SCT MAGIC
msg1 = "Correct! As funny as they may look, all these commands are valid ways to build a Python list."
msg2 = "Command B is valid, but it's not the only one!"
msg3 = "Both command B and C are valid; what about command A? Try it out in the console."
msg4 = "Command C is valid, but it's not the only one!"
success_msg("Replace me")
```

--- type:NormalExercise lang:python xp:100 skills:2
## List of lists

As a data scientst, you'll often be dealing with a lot of data, and it will make sense to group some of this data.

Instead of creating a flat list containing strings and floats, representing the names and areas of the rooms in your house, you can create a list of lists. The script on the right can already give you an idea. 

Don't get confused here: `"hallway"` is a string, while `hallway` is a variable, that refers to a float that you've specified earlier. Python will understand `["hallway", hallway]` as `["hallway", 11.25]`.

*** =instructions
- Finish the list of lists, so that it also contains the bedroom and bathroom data.
- Print out `house`; does this way of structuring your data make more sense?
- Print out the type of `house`. Are you still dealing with a list?

*** =hint
- Add _sublists_ to the `house` list by adding `["bedroom", bedroom]` and `["bathroom", bathroom]` inside the square brackets.
- To print a variable `x`, write `print(x)` on a new line in the Python script.
- To print out the type of a variable `x`, you can use `print(type(x))`.

*** =pre_exercise_code
```{python}
# pec
```

*** =sample_code
```{python}
# area variables (in square meters)
hallway = 11.25
kitchen = 18.0
living = 20.0
bedroom = 10.75
bathroom = 9.50

# house information as list of lists
house = [["hallway", hallway], ["kitchen", kitchen], ["living room", living]]

# Print out house


# Print out the type of house

```

*** =solution
```{python}
# area variables (in square meters)
hallway = 11.25
kitchen = 18.0
living = 20.0
bedroom = 10.75
bathroom = 9.50

# house information as list of lists
house = [["hallway", hallway], ["kitchen", kitchen], ["living room", living], 
         ["bedroom", bedroom], ["bathroom", bathroom]]

# Print out house
print(house)

# Print out the type of house
print(type(house))
```

*** =sct
```{python}
# TODO VINCENT SCT MAGIC
success_msg("Great! Get ready to learn about list subsetting!")
```


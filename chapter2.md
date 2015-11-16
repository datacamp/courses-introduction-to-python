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

The code on the right is the start of solution: for same of the ares, the name of the corresponding room is placed in front. Pay attention here. `"bahtroom"` is a string, while `bathroom` is a variable, representing the float `9.50` that you've specified earliers.

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

Don't get confused here: `"hallway"` is a string, while `hallway` is a variable, representing the float `11.25` that you've specified earlier.

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
house = [["hallway", hallway],
         ["kitchen", kitchen],
         ["living room", living]]

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
house = [["hallway", hallway],
         ["kitchen", kitchen],
         ["living room", living],
         ["bedroom", bedroom],
         ["bathroom", bathroom]]

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

--- type:VideoExercise lang:python xp:50 skills:2
## Subsetting lists

*** =video_link
//player.vimeo.com/video/108225030

--- type:NormalExercise lang:python xp:100 skills:2
## Subset and conquer

Subsetting Python lists is a piece of cake. Take the code sample below, that creates a list `x` and then selects "b" from it; this is the second element, so with index 1. You can also use negative subsetting.

```
x = list["a", "b", "c", "d"]
x[1]
x[-3] # same result!
```

Remember the `areas` list from before, containing both strings and floats? Its definition is already in the script. Can you add the correct code to do some Python subsetting?

*** =instructions
- Print out the second element from the `areas` list, so `11.25`.
- Subset and print out the last element of `areas`, being `9.50`. Using a negative index makes sense here!
- Select the element representing the area of the living room and print it out.

*** =hint
- Use `x[1]` to select the second element of a list `x`. Make sure to wrap your subsetting operation in a `print()` call.
- Use `x[-1]` to select the last element of a list `x`. Make sure to wrap your subsetting operation in a `print()` call.
- The element representing the area of the living room is the 6th element in the list, so you'll need `[5]` here.

*** =pre_exercise_code
```{python}
# pec
```

*** =sample_code
```{python}
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Select the second element from areas


# Select the last element from areas


# Select the element representing the area of the living room

```

*** =solution
```{python}
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Select the second element from areas
print(areas[1])

# Select the last element from areas
print(areas[-1])

# Select the element representing the area of the living room
print(areas[5])
```

*** =sct
```{python}
# TODO VINCENT SCT MAGIC
success_msg("Good job!")
```

--- type:NormalExercise lang:python xp:100 skills:2
## Subset and calculate

After you've extracted values from a list, you can use them to perform additional calculations. Take this example, were the second and fourth element of a list `x` are extracted and pasted together using the `+` operator:

```
x = ["a", "b", "c", "d"]
el2 = x[1]
el4 = x[3]
print(el2 + el4)
```

*** =instructions
- Using a combination of list subsetting and variable assignment, create new variable `eat_sleep`, that contains the sum of the area of the kitchen and the area of the bedroom.
- Print this new variable `eat_sleep`.

*** =hint
hint comes here

*** =pre_exercise_code
```{python}
# pec
```

*** =sample_code
```{python}
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Create the variable eat_sleep: sum of kitchen and bedroom area


# Print the variable eat_sleep

```

*** =solution
```{python}
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Create the variable eat_sleep: sum of kitchen and bedroom area
eat_sleep = areas[3] + areas[-3]

# Print the variable eat_sleep
print(eatslaap)
```

*** =sct
```{python}
# TODO VINCENT SCT MAGIC
success_msg("Bellissimo!")
```

--- type:NormalExercise lang:python xp:100 skills:2
## Slicing and dicing

Selecting single values of a list is just one part of the story. It's also possible to _slice_ your list, which comes down to selecting multiple elements from your list. Use the following syntax:

```
my_list[begin:end]
```

The `begin` index will be included, while the `end` index is _not_.

The code sample below shows an example, where the second and third element, corresponding to indices 1 and 2, are selected from a list `x`:

```
x = ["a", "b", "c", "d"]
x[1:3]
```

The elements with index 1 and 2 are included, while the element with index three is not.

*** =instructions
- Use slicing to create a list, `ground_floor`, that contains the first 6 elements of `areas`.
- Do a similar thing to create a new variable, `first_floor`, that contains the last 4 elements of `areas`.
- Print both `ground_floor` and `first_floor` using `print()`.

*** =hint
- Use the brackets `[0:6]` to build `ground_floor`.
- Use the barckets `[6:10]` to build `first_floor`.
- Simply add two `print()` calls to the script to print out `ground_floor` and `first_floor`.

*** =pre_exercise_code
```{python}
# no pec
```

*** =sample_code
```{python}
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Use slicing to create ground_floor


# Use slicing to create first_floor


# Print out ground_floor and first_floor
```

*** =solution
```{python}
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Use slicing to create ground_floor
ground_floor = areas[0:6]

# Use slicing to create first_floor
first_floor = areas[6:10]

# Print out ground_floor and first_floor
print(ground_floor)
print(first_floor)
```

*** =sct
```{python}

```

--- type:NormalExercise lang:python xp:100 skills:2
## Slicing and dicing (2)

In the video, Filip only discussed the syntax where you specify both where to begin and end the slice of your list:

```
my_list[begin:end]
```

However, it's also possible not to specify these indices. If you don't specify the `begin` index, Python figures out that you want to start your slice at the beginning of your list. If you don't specify the `end` index, the slice will go all the way to the last element of your list. To experiment with this, try the following commands in the IPython Shell:

```
x = ["a", "b", "c", "d"]
x[:2]
x[2:]
x[:]
```

*** =instructions
- Use slicing to create the lists `ground_floor` and `first_floor` again, this time without using indices if it's not necessary.
- Print out the sum of the areas of the bedroom and the bathroom. You can subset `areas` or `first_floor` to do this, that's up to you.

*** =hint
- To build `ground_floor`, you can use `[:6]`. To build `first_floor`, you can use `[6:]`.
- You can use standard subsetting techniques to extract the list elements and perform calculations.

*** =pre_exercise_code
```{python}
# pec
```

*** =sample_code
```{python}
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Alternative slicing to create ground_floor


# Alternative slicing to create first_floor


# Sum of bedroom and bathroom area

```

*** =solution
```{python}
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Alternative slicing to create ground_floor
ground_floor = areas[:6]

# Alternative slicing to create first_floor
first_floor = areas[6:]

# Sum of bedroom and bathroom area
print(first_floor[1] + first_floor[3])
```

*** =sct
```{python}
# TODO VINCENT SCT MAGIC
success_msg("Wonderful!")
```

--- type:MultipleChoiceExercise lang:python xp:50 skills:2
## Subsetting lists of lists

You saw before that a Python list can contain practically anything; even other lists. To subset lists of lists, you can use the same techniques as before: square brackets. Try out the commands in the following code sample in the IPython Shell:

```
x = [["a", "b", "c"], 
     ["d", "e", "f"], 
     ["g", "h", "i"]]
x[2][0]
x[2][:2]
```

`x[2]` results in a list, that you can subset again by adding additional square brackets.

What will `house[-1][1]` return? `house`, the list of lists you've created before, is already defined for you, so you can experiment with it in the IPython Shell.

*** =instructions
- A float: the kitchen area
- A string: "kitchen"
- A float: the bathroom area
- A string: "bathroom"

*** =hint
`house[-1]` selects the last element of `house`, which is the list `["bathroom", 9.50]`. What's the result if you then subset this sublist with `[1]`? You can always try out the command in the IPython Shell!

*** =pre_exercise_code
```{python}
house = [["hallway", 11.25], 
         ["kitchen", 18.0], 
         ["living room", 20.0], 
         ["bedroom", 10.75], 
         ["bathroom", 9.50]]
```

*** =sct
```{python}
# TODO VINCENT SCT MAGIC
msg1 = msg2 = "Wrong. `house[-1]` selects the last element of `house`, which is the list `["bathroom", 9.50]`."
msg3 = "Correcto perfecto! The last piece of the list puzzle is manipulation."
msg4 = "Incorrect. `house[-1]` indeed selects the list that represents the bathroom information, but `[1]` selects the second element of the sublist, not the first. Python uses zero-based indexing!"
success_msg("replace me")
```

--- type:VideoExercise lang:python xp:50 skills:2
## List Manipulation

*** =video_link
//player.vimeo.com/video/108225030

--- type:NormalExercise lang:python xp:100 skills:2
## Replace list elements

Replacing list elements is pretty easy: subset the list and assign new values to the subset. You can select single elements, but also change entire list slices at once.

Use the IPython Shell to experiment with the commands below. Can you tell what's happening and why?

```
x = ["a", "b", "c", "d"]
x[1] = "r"
x[2:] = ["s", "t"]
```

For this and the following exercises, you'll continue working on the `areas` list, that contains the names and areas of different rooms in a house.

*** =instructions
- You did a miscalculation when determining the area of the bathroom; it's 10.50 square meters instead of 9.50. Can you make the changes?
- Make the `areas` list more trendy: Change "living room" to "chill zone".

*** =hint
- To select the bathroom area, you can use `[-1]`.
- To select the `"living room"` element, you can use `[4]`. Next, use `= "chill zone"` to change this element.

*** =pre_exercise_code
```{python}
# pec
```

*** =sample_code
```{python}
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Correct the bathroom area


# Change "living room" to "chill zone"

```

*** =solution
```{python}
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Correct the bathroom area
areas[-1] = 10.50

# Change "living room" to "chill zone"
areas[4]= "chill zone"
```

*** =sct
```{python}
# TODO VINCENT SCT MAGIC
success_msg("Sweet! As the code sample showed, you can also slice a list and replace it with another list, to update multiple elements in a single command.")
```

--- type:NormalExercise lang:python xp:100 skills:2
## Extend a list

Assignment comes here. Use Markdown for text formatting.

*** =instructions
- instruction 1
- instruction 2

*** =hint
hint comes here

*** =pre_exercise_code
```{python}
# pec
```

*** =sample_code
```{python}
# sample code
```

*** =solution
```{python}
# solution code
```

*** =sct
```{python}
# sct code
```

--- type:NormalExercise lang:python xp:100 skills:2
## Delete list elements

Assignment comes here. Use Markdown for text formatting.

*** =instructions
- instruction 1
- instruction 2

*** =hint
hint comes here

*** =pre_exercise_code
```{python}
# pec
```

*** =sample_code
```{python}
# sample code
```

*** =solution
```{python}
# solution code
```

*** =sct
```{python}
# sct code
```

--- type:MultipleChoiceExercise lang:python xp:50 skills:2
## Inner workings of lists

Assignment comes here. Use Markdown for text formatting.

*** =instructions
- option 1
- option 2
- option 3

*** =hint
hint

*** =pre_exercise_code
```{python}
# pec
```

*** =sct
```{python}
test_mc(2) # if 2 is the correct option.
```


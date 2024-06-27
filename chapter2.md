---
title_meta: Chapter 2
title: Python Lists
description: >-
  Learn to store, access, and manipulate data in lists: the first step toward
  efficiently working with huge amounts of data.
attachments:
  slides_link: 'https://projector-video-pdf-converter.datacamp.com/735/chapter2.pdf'
lessons:
  - nb_of_exercises: 4
    title: Python Lists
  - nb_of_exercises: 4
    title: Subsetting Lists
  - nb_of_exercises: 5
    title: Manipulating Lists
---

## Python Lists

```yaml
type: VideoExercise
key: a5886d213f
xp: 50
```

`@projector_key`
a0530c4542f10988847b2dbb91f717c3

---

## Create a list

```yaml
type: NormalExercise
key: e6c527bf41
lang: python
xp: 100
skills:
  - 2
```

A list is a **compound data type**; you can group values together, like this:

```
a = "is"
b = "nice"
my_list = ["my", "list", a, b]
```

After measuring the height of your family, you decide to collect some information on the house you're living in. The areas of the different parts of your house are stored in separate variables in the exercise.

`@instructions`
- Create a list, `areas`, that contains the area of the hallway (`hall`), kitchen (`kit`), living room (`liv`), bedroom (`bed`) and bathroom (`bath`), in this order. Use the predefined variables.
- Print `areas` with the `print()` function.

`@hint`
- You can use the variables that have already been created to build the list: `areas = [hall, kit, ...]`.
- Make sure to use square brackets `[]` rather than parentheses `()`.
- You don't need to use quotation marks when storing variables within a list.
- Type `print(areas)` to print out the list when submitting.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Create list areas


# Print areas

```

`@solution`
```{python}
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Create list areas
areas = [hall, kit, liv, bed, bath]

# Print areas
print(areas)
```

`@sct`
```{python}
predef_msg = "Don't remove or edit the predefined variables!"
areas_msg = "Define `areas` as the list containing all the area variables, in the correct order: `[hall, kit, liv, bed, bath]`. Watch out for typos. The list shouldn't contain anything else!"

Ex().check_correct(
    has_printout(0, not_printed_msg = "__JINJA__:Have you used `{{sol_call}}` to print out the `areas` list at the end of your script?"),
    check_correct(
        check_object("areas").has_equal_value(incorrect_msg = areas_msg),
        multi(
            check_object('hall', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
            check_object('kit', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
            check_object('liv', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
            check_object('bed', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
            check_object('bath', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg)
        )
    )
)

success_msg("Nice! A list is way better here, isn't it?")
```

---

## Create lists with different types

```yaml
type: NormalExercise
key: 1702a8bcdc
lang: python
xp: 100
skills:
  - 2
```

Although it's not really common, a list can also contain a mix of Python types including strings, floats, and booleans.

You're now going to add the room names to your list, so you can easily see both the room name and size together.

Some of the code has been provided for you to get you started. Pay attention here! `"bathroom"` is a string, while `bath` is a variable that represents the float `9.50` you specified earlier.

`@instructions`
- Finish the code that creates the `areas` list. Build the list so that the list first contains the name of each room as a string and then its area. In other words, add the strings `"hallway"`, `"kitchen"` and `"bedroom"` at the appropriate locations.
- Print `areas` again; is the printout more informative this time?

`@hint`
- The first four elements of the list `areas` are coded as `["hallway", hall, "kitchen", kit, ...`.
- A string will need to be in quotation marks `""`.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Adapt list areas
areas = [____, hall, ____, kit, "living room", liv, ____, bed, "bathroom", bath]

# Print areas
____
```

`@solution`
```{python}
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Adapt list areas
areas = ["hallway", hall, "kitchen", kit, "living room", liv, "bedroom", bed, "bathroom", bath]

# Print areas
print(areas)
```

`@sct`
```{python}
objs = ["hall", "kit", "liv", "bed", "bath"]
predef_msg = "Don't remove or edit the predefined variables!"
areas_msg = "You didn't assign the correct value to `areas`. Have another look at the instructions. Make sure to place the room name before the variable containing the area each time. The order matters here! Watch out for typos."

Ex().check_correct(
  check_object("areas").has_equal_value(incorrect_msg = areas_msg),
  multi([ check_object(obj, missing_msg = predef_msg).has_equal_value(incorrect_msg = predef_msg) for obj in objs])
)

Ex().has_printout(0, not_printed_msg = "__JINJA__:Have you used `{{sol_call}}` to print out the `areas` list at the end of your script?")

success_msg("Nice! This list contains both strings and floats, but that's not a problem for Python!")
```

---

## List of lists

```yaml
type: NormalExercise
key: 9158c577b0
lang: python
xp: 100
skills:
  - 2
```

As a data scientist, you'll often be dealing with a lot of data, and it will make sense to group some of this data.

Instead of creating a list containing strings and floats, representing the names and areas of the rooms in your house, you can create a list of lists.

Remember: `"hallway"` is a string, while `hall` is a variable that represents the float `11.25` you specified earlier.

`@instructions`
- Finish the list of lists so that it also contains the bedroom and bathroom data. Make sure you enter these in order!
- Print out `house`; does this way of structuring your data make more sense?

`@hint`
- Add _sublists_ to the `house` list by adding `["bedroom", bed]` and `["bathroom", bath]` inside the square brackets.
- To print a variable `x`, write `print(x)` on a new line.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# House information as list of lists
house = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv],
        ____,
        ____]

# Print out house
____
```

`@solution`
```{python}
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# House information as list of lists
house = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv],
         ["bedroom", bed],
         ["bathroom", bath]]

# Print out house
print(house)
```

`@sct`
```{python}
predef_msg = "Don't remove or edit the predefined variables!"
house_msg = "You didn't assign the correct value to `house`. Have another look at the instructions. Extend the list of lists so it incorporates a list for each pair of room name and room area. Mind the order and typos!"

Ex().check_correct(
    check_object("house").has_equal_value(incorrect_msg = house_msg),
    multi(
        check_object('hall', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
        check_object('kit', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
        check_object('liv', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
        check_object('bed', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
        check_object('bath', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg)
    )
)

Ex().has_printout(0, not_printed_msg = "__JINJA__:Have you used `{{sol_call}}` to print out the contents of `house`?")

success_msg("Great! Get ready to learn about list subsetting!")
```

---

## Subsetting Lists

```yaml
type: VideoExercise
key: c076b5a69c
xp: 50
```

`@projector_key`
fc15ba5cb9485456df8589130b519ea3

---

## Subset and conquer

```yaml
type: NormalExercise
key: c3ce582e32
lang: python
xp: 100
skills:
  - 2
```

Subsetting Python lists is a piece of cake. Take the code sample below, which creates a list `x` and then selects "b" from it. Remember that this is the second element, so it has index 1. You can also use negative indexing.

```
x = ["a", "b", "c", "d"]
x[1]
x[-3] # same result!
```

Remember the `areas` list from before, containing both strings and floats? Its definition is already in the script. Can you add the correct code to do some Python subsetting?

`@instructions`
- Print out the second element from the `areas` list (it has the value `11.25`).
- Subset and print out the last element of `areas`, being `9.50`. Using a negative index makes sense here!
- Select the number representing the area of the living room (`20.0`) and print it out.

`@hint`
- Use `x[1]` to select the second element of a list `x`.
- Use `x[-1]` to select the last element of a list `x`.
- Make sure to wrap your subsetting operations in a `print()` call.
- The number representing the area of the living room is the 6th element in the list, so you'll need `[5]` here. `area[4]` would show the string!

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Print out second element from areas
print(areas[____])

# Print out last element from areas
print(areas[____])

# Print out the area of the living room
print(areas[____])
```

`@solution`
```{python}
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Print out second element from areas
print(areas[1])

# Print out last element from areas
print(areas[-1])

# Print out the area of the living room
print(areas[5])
```

`@sct`
```{python}
msg = "Don't remove or edit the predefined `areas` list."
Ex().check_object("areas", missing_msg = msg).has_equal_value(incorrect_msg = msg)
Ex().has_printout(0, not_printed_msg = "Have another look at your code to print out the second element in `areas`, which is at index `1`.")
Ex().has_printout(1, not_printed_msg = "Have another look at your code to print out the last element in `areas`, which is at index `-1`.")
Ex().has_printout(2, not_printed_msg = "Have another look at your code to print out the area of the living room. It's at index `5`.")
success_msg("Good job!")
```

---

## Slicing and dicing

```yaml
type: NormalExercise
key: 7f08642d18
lang: python
xp: 100
skills:
  - 2
```

Selecting single values from a list is just one part of the story. It's also possible to _slice_ your list, which means selecting multiple elements from your list. Use the following syntax:

```
my_list[start:end]
```

The `start` index will be included, while the `end` index is _not_. However, it's also possible not to specify these indexes. If you don't specify the `start` index, Python figures out that you want to start your slice at the beginning of your list.

`@instructions`
- Use slicing to create a list, `downstairs`, that contains the first 6 elements of `areas`.
- Create `upstairs`, as the last `4` elements of `areas`. This time, simplify the slicing by omitting the `end` index.
- Print both `downstairs` and `upstairs` using `print()`.

`@hint`
- Use the brackets `[0:6]` to get the first six elements of a list.
- To get everything except the first 5 elements of a list, `l`, you would use `l[5:]`.
- Add two `print()` calls to print out `downstairs` and `upstairs`.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Use slicing to create downstairs
downstairs = areas[____]

# Use slicing to create upstairs
upstairs = areas[____]

# Print out downstairs and upstairs
____
____
```

`@solution`
```{python}
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Use slicing to create downstairs
downstairs = areas[0:6]

# Use slicing to create upstairs
upstairs = areas[6:]

# Print out downstairs and upstairs
print(downstairs)
print(upstairs)
```

`@sct`
```{python}
msg = "Don't remove or edit the predefined `areas` list."
Ex().check_object("areas", missing_msg = msg).has_equal_value(incorrect_msg = msg)

patt = "`%s` is incorrect. Use `areas[%s]` and slicing to select the elements you want, or something equivalent."
Ex().check_object("downstairs").has_equal_value(incorrect_msg = patt % ('downstairs', '0:6'))
Ex().check_object("upstairs").has_equal_value(incorrect_msg = patt % ("upstairs",":6"))

Ex().has_printout(0, not_printed_msg="Have you printed out `downstairs` after calculating it?")
Ex().has_printout(1, not_printed_msg="Have you printed out `upstairs` after calculating it?")

success_msg("Great!")
```

---

## Subsetting lists of lists

```yaml
type: NormalExercise
key: dbbbd306cf
xp: 100
```

A Python list can also contain other lists.

To subset lists of lists, you can use the same technique as before: square brackets. This would like something like this for a list, `x`:

```
x[2][0]
```

`@instructions`
- Subset the `house` list to get the float `9.5`.

`@hint`
- Break this down step by step. First you want to get to the last element of the list, `["bathroom", 9.50]`. Recall the index of the last element is `-1`.
- Next you want to get the second element of `["bathroom", 9.50]`, which is at index `1`.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
house = [["hallway", 11.25],
         ["kitchen", 18.0],
         ["living room", 20.0],
         ["bedroom", 10.75],
         ["bathroom", 9.50]]

# Subset the house list
house___
```

`@solution`
```{python}
house = [["hallway", 11.25],
         ["kitchen", 18.0],
         ["living room", 20.0],
         ["bedroom", 10.75],
         ["bathroom", 9.50]]

# Subset the house list
house[-1][1]
```

`@sct`
```{python}
Ex().has_code("house[-1][1]", pattern=False)

success_msg("Correctomundo! The last piece of the list puzzle is manipulation.")
```

---

## Manipulating Lists

```yaml
type: VideoExercise
key: d7fe818b3a
xp: 50
```

`@projector_key`
355ed52d2fb0d67508c6a311b7cbc6d3

---

## Replace list elements

```yaml
type: NormalExercise
key: 4e1bba1b55
lang: python
xp: 100
skills:
  - 2
```

To replace list elements, you subset the list and assign new values to the subset. You can select single elements or you can change entire list slices at once.

For this and the following exercises, you'll continue working on the `areas` list that contains the names and areas of different rooms in a house.

`@instructions`
- Update the area of the bathroom to be `10.50` square meters instead of `9.50`.
- Make the `areas` list more trendy! Change `"living room"` to `"chill zone"`.

`@hint`
- To update the bathroom area, identify the subset of the bathroom area (it's the last item of the list!).
- Then, replace the value with the new bathroom area by assigning it to this subset.
- Do the same to update the `"living room"` name, which is at index 4.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Correct the bathroom area


# Change "living room" to "chill zone"

```

`@solution`
```{python}
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Correct the bathroom area
areas[-1] = 10.50

# Change "living room" to "chill zone"
areas[4] = "chill zone"
```

`@sct`
```{python}
bathroom_msg = 'You can use `areas[-1] = 10.50` to update the bathroom area.'
chillzone_msg = 'You can use `areas[4] = "chill zone"` to update the living room name.'
Ex().check_correct(
  check_object('areas').has_equal_value(incorrect_msg = 'Your changes to `areas` did not result in the correct list. Are you sure you used the correct subset operations? When in doubt, you can use a hint!'),
  multi(
    has_equal_value(expr_code='areas[-1]', override=10.50, incorrect_msg = bathroom_msg),
    has_equal_value(expr_code='areas[4]', override='chill zone', incorrect_msg = chillzone_msg),
  )
)
success_msg('Sweet! As the code sample showed, you can also slice a list and replace it with another list to update multiple elements in a single command.')
```

---

## Extend a list

```yaml
type: NormalExercise
key: ff0fe8d967
lang: python
xp: 100
skills:
  - 2
```

If you can change elements in a list, you sure want to be able to add elements to it, right? You can use the `+` operator:

```
x = ["a", "b", "c", "d"]
y = x + ["e", "f"]
```

You just won the lottery, awesome! You decide to build a poolhouse and a garage. Can you add the information to the `areas` list?

`@instructions`
- Use the `+` operator to paste the list `["poolhouse", 24.5]` to the end of the `areas` list. Store the resulting list as `areas_1`.
- Further extend `areas_1` by adding data on your garage. Add the string `"garage"` and float `15.45`. Name the resulting list `areas_2`.

`@hint`
- Follow the code sample in the assignment. `x` is `areas` here, and `["e", "f"]` is `["poolhouse", 24.5]`.
- To add more elements to `areas_1`, use `areas_1 + ["element", 123]`.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create the areas list and make some changes
areas = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0,
         "bedroom", 10.75, "bathroom", 10.50]

# Add poolhouse data to areas, new list is areas_1
areas_1 = ____

# Add garage data to areas_1, new list is areas_2
areas_2 = ____
```

`@solution`
```{python}
# Create the areas list (updated version)
areas = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0,
         "bedroom", 10.75, "bathroom", 10.50]

# Add poolhouse data to areas, new list is areas_1
areas_1 = areas + ["poolhouse", 24.5]

# Add garage data to areas_1, new list is areas_2
areas_2 = areas_1 + ["garage", 15.45]
```

`@sct`
```{python}
msg = "Don't remove or edit the predefined `areas` list."
Ex().check_object("areas", missing_msg = msg).has_equal_value(incorrect_msg = msg)
Ex().check_object("areas_1").has_equal_value(incorrect_msg = "Use `areas + [\"poolhouse\", 24.5]` to create `areas_1`. Watch out for typos!")
Ex().check_object("areas_2").has_equal_value(incorrect_msg = "Use `areas_1 + [\"garage\", 15.45]` to create `areas_2`. Watch out for typos!")
success_msg("Cool! The list is shaping up nicely!")
```

---

## Delete list elements

```yaml
type: NormalExercise
key: 85f792356e
xp: 100
```

Finally, you can also remove elements from your list. You can do this with the `del` statement:

```
x = ["a", "b", "c", "d"]
del x[1]
```

Pay attention here: as soon as you remove an element from a list, the indexes of the elements that come after the deleted element all change!

Unfortunately, he amount you won with the lottery is not that big after all and it looks like the poolhouse isn't going to happen. You'll need to remove it from the list. decide to remove the corresponding string and float from the `areas` list.

`@instructions`
- Delete the string and float for the `"poolhouse"` from your `areas` list.
- Print the updated `areas` list.

`@hint`
- You'll need to use `del` twice to delete two elements. Be careful about changing indexes though!

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
areas = ["hallway", 11.25, "kitchen", 18.0,
        "chill zone", 20.0, "bedroom", 10.75,
         "bathroom", 10.50, "poolhouse", 24.5,
         "garage", 15.45]

# Delete the poolhouse from the list


# Print the updated list

```

`@solution`
```{python}
areas = ["hallway", 11.25, "kitchen", 18.0,
        "chill zone", 20.0, "bedroom", 10.75,
         "bathroom", 10.50, "poolhouse", 24.5,
         "garage", 15.45]

# Delete the poolhouse from the list
del areas[10]
del areas[10]

# Print the updated list
print(areas)
```

`@sct`
```{python}
Ex().multi(
  has_code("del areas[10]", pattern=False),
  has_code("del areas[10]", pattern=False)
)

Ex().has_printout(0, not_printed_msg="Have you printed out `areas` after removing the poolhouse string and float?")
success_msg("Correct! You'll learn about easier ways to remove specific elements from Python lists later on.")
```

---

## Inner workings of lists

```yaml
type: NormalExercise
key: af72db9915
lang: python
xp: 100
skills:
  - 2
```

Some code has been provided for you in this exercise: a list with the name `areas` and a copy named `areas_copy`.

Currently, the first element in the `areas_copy` list is changed and the `areas` list is printed out. If you hit _Run Code_ you'll see that, although you've changed `areas_copy`, the change also takes effect in the `areas` list. That's because `areas` and `areas_copy` point to the same list.

If you want to prevent changes in `areas_copy` from also taking effect in `areas`, you'll have to do a more explicit copy of the `areas` list with `list()` or by using `[:]`.

`@instructions`
- Change the second command, that creates the variable `areas_copy`, such that `areas_copy` is an explicit copy of `areas`. After your edit, changes made to `areas_copy` shouldn't affect `areas`. Submit the answer to check this.

`@hint`
- Change the `areas_copy = areas` call. Instead of assigning `areas`, you can assign `list(areas)` or `areas[:]`.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Change this command
areas_copy = areas

# Change areas_copy
areas_copy[0] = 5.0

# Print areas
print(areas)
```

`@solution`
```{python}
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Change this command
areas_copy = list(areas)

# Change areas_copy
areas_copy[0] = 5.0

# Print areas
print(areas)
```

`@sct`
```{python}
Ex().check_correct(
  check_object("areas_copy").has_equal_value(incorrect_msg = "It seems that `areas_copy` has not been updated correctly."),
  check_function("list", missing_msg = "Make sure to use `list(areas)` to create an `areas_copy`.")
)

mmsg = "Don't remove the predefined `areas` list."
imsg = "Be sure to edit ONLY the copy, not the original `areas` list. Have another look at the exercise description if you're unsure how to create a copy."
Ex().check_correct(
  check_object("areas", missing_msg = mmsg).has_equal_value(incorrect_msg = imsg),
  check_function("list", missing_msg = "Make sure to use `list(areas)` to create an `areas_copy`.")
)

success_msg("Nice! The difference between explicit and reference-based copies is subtle, but can be really important. Try to keep in mind how a list is stored in the computer's memory.")
```

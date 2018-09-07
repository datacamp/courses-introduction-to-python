---
title_meta  : Chapter 2
title       : Python Lists
description : "Learn to store, access and manipulate data in lists: the first step towards efficiently working with huge amounts of data."
attachments :
  slides_link : https://s3.amazonaws.com/assets.datacamp.com/course/intro_to_python/ch2_slides.pdf

---
## Lists, what are they?

```yaml
type: VideoExercise
lang: python
xp: 50
skills: 2
key: f366e876d8
```

`@video_link`
//player.vimeo.com/video/154563059

`@video_hls`
//videos.datacamp.com/transcoded/735_intro_to_python/v2/hls-ch2_1.master.m3u8

*** =projector_key
84258dc00ac8e6f277086d60255e8244

---
## Create a list

```yaml
type: NormalExercise
lang: python
xp: 100
skills: 2
key: e6c527bf41
```

As opposed to `int`, `bool` etc., a list is a **compound data type**; you can group values together:

```
a = "is"
b = "nice"
my_list = ["my", "list", a, b]
```

After measuring the height of your family, you decide to collect some information on the house you're living in. The areas of the different parts of your house are stored in separate variables for now, as shown in the script.

`@instructions`
- Create a list, `areas`, that contains the area of the hallway (`hall`), kitchen (`kit`), living room (`liv`), bedroom (`bed`) and bathroom (`bath`), in this order. Use the predefined variables.
- Print `areas` with the [`print()`](https://docs.python.org/3/library/functions.html#print) function.

`@hint`
- You can use the variables that have already been created to build the list: `areas = [hall, kit, ...]`.
- Put `print(areas)` in your script to print out the list when submitting.

`@sample_code`
```{python}
# area variables (in square meters)
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
# Area variables (in square meters)
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
## Create list with different types

```yaml
type: NormalExercise
lang: python
xp: 100
skills: 2
key: 1702a8bcdc
```

A list can contain any Python type. Although it's not really common, a list can also contain a mix of Python types including strings, floats, booleans, etc.

The printout of the previous exercise wasn't really satisfying. It's just a list of numbers representing the areas, but you can't tell which area corresponds to which part of your house.

The code on the right is the start of a solution. For some of the areas, the name of the corresponding room is already placed in front. Pay attention here! `"bathroom"` is a string, while `bath` is a variable that represents the float `9.50` you specified earlier.

`@instructions`
- Finish the line of code that creates the `areas` list. Build the list so that the list first contains the name of each room as a string and then its area. In other words, add the strings `"hallway"`, `"kitchen"` and `"bedroom"` at the appropriate locations.
- Print `areas` again; is the printout more informative this time?

`@hint`
The first three 4 elements of the list `areas` are coded as `["hallway", hall, "kitchen", kit, ...`.

`@sample_code`
```{python}
# area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Adapt list areas
areas = [hall, kit, "living room", liv, bed, "bathroom", bath]

# Print areas

```

`@solution`
```{python}
# area variables (in square meters)
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
## Select the valid list

```yaml
type: MultipleChoiceExercise
lang: python
xp: 50
skills: 2
key: 416b80a405
```

A list can contain any Python type. But a list itself is also a Python type. That means that a list can also contain a list! Python is getting funkier by the minute, but fear not, just remember the list syntax:

```
my_list = [el1, el2, el3]
```

Can you tell which ones of the following lines of Python code are valid ways to build a list?

A. `[1, 3, 4, 2]`
B. `[[1, 2, 3], [4, 5, 7]]`
C. `[1 + 2, "a" * 5, 3]`


`@instructions`
- A, B and C
- B
- B and C
- C

`@hint`
Try out all the different lines in the Python shell and see which ones generate an error. Maybe none of them go wrong?

`@sct`
```{python}
msg1 = "Correct! As funny as they may look, all these commands are valid ways to build a Python list."
msg2 = "Command B is valid, but it's not the only one!"
msg3 = "Both command B and C are valid; what about command A? Try it out in the console."
msg4 = "Command C is valid, but it's not the only one!"
Ex().has_chosen(1,[msg1,msg2,msg3,msg4])
```

---
## List of lists

```yaml
type: NormalExercise
lang: python
xp: 100
skills: 2
key: 9158c577b0
```

As a data scientist, you'll often be dealing with a lot of data, and it will make sense to group some of this data.

Instead of creating a flat list containing strings and floats, representing the names and areas of the rooms in your house, you can create a list of lists. The script on the right can already give you an idea.

Don't get confused here: `"hallway"` is a string, while `hall` is a variable that represents the float `11.25` you specified earlier.

`@instructions`
- Finish the list of lists so that it also contains the bedroom and bathroom data. Make sure you enter these in order!
- Print out `house`; does this way of structuring your data make more sense?
- Print out the type of `house`. Are you still dealing with a list?

`@hint`
- Add _sublists_ to the `house` list by adding `["bedroom", bed]` and `["bathroom", bath]` inside the square brackets.
- To print a variable `x`, write `print(x)` on a new line in the Python script.
- To print out the type of a variable `x`, you can use `print(type(x))`.

`@sample_code`
```{python}
# area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# house information as list of lists
house = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv]]

# Print out house


# Print out the type of house

```

`@solution`
```{python}
# area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# house information as list of lists
house = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv],
         ["bedroom", bed],
         ["bathroom", bath]]

# Print out house
print(house)

# Print out the type of house
print(type(house))
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
Ex().has_printout(1, not_printed_msg = "__JINJA__:Have you used `{{sol_call}}` to print out the type of the `house` variable?")

success_msg("Great! Get ready to learn about list subsetting!")
```

---
## Subsetting lists

```yaml
type: VideoExercise
lang: python
xp: 50
skills: 2
key: 9e15e5b8a0
```

`@video_link`
//player.vimeo.com/video/146994264

`@video_hls`
//videos.datacamp.com/transcoded/735_intro_to_python/v1/hls-ch2_2.master.m3u8

*** =projector_key
47e0948980f8c77be2071a892b32ec8b

---
## Subset and conquer

```yaml
type: NormalExercise
lang: python
xp: 100
skills: 2
key: c3ce582e32
```

Subsetting Python lists is a piece of cake. Take the code sample below, which creates a list `x` and then selects "b" from it. Remember that this is the second element, so it has index 1. You can also use negative indexing.

```
x = ["a", "b", "c", "d"]
x[1]
x[-3] # same result!
```

Remember the `areas` list from before, containing both strings and floats? Its definition is already in the script. Can you add the correct code to do some Python subsetting?

`@instructions`
- Print out the second element from the `areas` list, so `11.25`.
- Subset and print out the last element of `areas`, being `9.50`. Using a negative index makes sense here!
- Select the number representing the area of the living room and print it out.

`@hint`
- Use `x[1]` to select the second element of a list `x`. Make sure to wrap your subsetting operation in a [`print()`](https://docs.python.org/3/library/functions.html#print) call.
- Use `x[-1]` to select the last element of a list `x`. Make sure to wrap your subsetting operation in a [`print()`](https://docs.python.org/3/library/functions.html#print) call.
- The number representing the area of the living room is the 6th element in the list, so you'll need `[5]` here.

`@sample_code`
```{python}
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Print out second element from areas
print(areas[_])

# Print out last element from areas
print(areas[__])

# Print out the area of the living room
print(areas[_])
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
## Subset and calculate

```yaml
type: NormalExercise
lang: python
xp: 100
skills: 2
key: 58c969f11f
```

After you've extracted values from a list, you can use them to perform additional calculations. Take this example, where the second and fourth element of a list `x` are extracted. The strings that result are pasted together using the `+` operator:

```
x = ["a", "b", "c", "d"]
print(x[1] + x[3])
```

`@instructions`
- Using a combination of list subsetting and variable assignment, create a new variable, `eat_sleep_area`, that contains the sum of the area of the kitchen and the area of the bedroom.
- Print the new variable `eat_sleep_area`.

`@hint`
- Add `areas[3]` to `areas[-3]` to calculate `eat_sleep_area`.
- Print out `eat_sleep_area`: `print(eat_sleep_area)`.

`@sample_code`
```{python}
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Sum of kitchen and bedroom area: eat_sleep_area


# Print the variable eat_sleep_area

```

`@solution`
```{python}
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Sum of kitchen and bedroom area: eat_sleep_area
eat_sleep_area = areas[3] + areas[-3]

# Print the variable eat_sleep_area
print(eat_sleep_area)
```

`@sct`
```{python}
msg = "Don't remove or edit the predefined `areas` list."
Ex().check_object("areas", missing_msg = msg).has_equal_value(incorrect_msg = msg)
Ex().check_object("eat_sleep_area").has_equal_value(incorrect_msg = "Be sure to assign the correct value to `eat_sleep_area`. You'll need to sum `areas[3]` and `areas[-3]`.")
Ex().has_printout(0, not_printed_msg = "Don't forget to print out `eat_sleap_area` after calculating it!")
success_msg("Bellissimo!")
```

---
## Slicing and dicing

```yaml
type: NormalExercise
lang: python
xp: 100
skills: 2
key: 7f08642d18
```

Selecting single values from a list is just one part of the story. It's also possible to _slice_ your list, which means selecting multiple elements from your list. Use the following syntax:

```
my_list[start:end]
```

The `start` index will be included, while the `end` index is _not_.

The code sample below shows an example. A list with `"b"` and `"c"`, corresponding to indexes 1 and 2, are selected from a list `x`:

```
x = ["a", "b", "c", "d"]
x[1:3]
```

The elements with index 1 and 2 are included, while the element with index 3 is not.

`@instructions`
- Use slicing to create a list, `downstairs`, that contains the first 6 elements of `areas`.
- Do a similar thing to create a new variable, `upstairs`, that contains the last 4 elements of `areas`.
- Print both `downstairs` and `upstairs` using [`print()`](https://docs.python.org/3/library/functions.html#print).

`@hint`
- Use the brackets `[0:6]` to build `downstairs`.
- Use the brackets `[6:10]` to build `upstairs`.
- Simply add two [`print()`](https://docs.python.org/3/library/functions.html#print) calls to the script to print out `downstairs` and `upstairs`.

`@sample_code`
```{python}
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Use slicing to create downstairs


# Use slicing to create upstairs


# Print out downstairs and upstairs
```

`@solution`
```{python}
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Use slicing to create downstairs
downstairs = areas[0:6]

# Use slicing to create upstairs
upstairs = areas[6:10]

# Print out downstairs and upstairs
print(downstairs)
print(upstairs)
```

`@sct`
```{python}
msg = "Don't remove or edit the predefined `areas` list."
Ex().check_object("areas", missing_msg = msg).has_equal_value(incorrect_msg = msg)

patt = "`%s` is incorrect. Use `areas[%s]` and slicing to select the elements you want, or something equivalnent."
Ex().check_object("downstairs").has_equal_value(incorrect_msg = patt % ('downstairs', '0:6'))
Ex().check_object("upstairs").has_equal_value(incorrect_msg = patt % ('upstairs', '6:10'))

Ex().has_printout(0, not_printed_msg="Have you printed out `downstairs` after calculating it?")
Ex().has_printout(1, not_printed_msg="Have you printed out `upstairs` after calculating it?")

success_msg("Great!")
```

---
## Slicing and dicing (2)

```yaml
type: NormalExercise
lang: python
xp: 100
skills: 2
key: dfc9a168a3
```

In the video, Filip first discussed the syntax where you specify both where to begin and end the slice of your list:

```
my_list[begin:end]
```

However, it's also possible not to specify these indexes. If you don't specify the `begin` index, Python figures out that you want to start your slice at the beginning of your list. If you don't specify the `end` index, the slice will go all the way to the last element of your list. To experiment with this, try the following commands in the IPython Shell:

```
x = ["a", "b", "c", "d"]
x[:2]
x[2:]
x[:]
```

`@instructions`
Use slicing to create the lists `downstairs` and `upstairs` again, but this time without using indexes if it's not necessary. Remember `downstairs` is the first 6 elements of `areas` and `upstairs` is the last 4 elements of `areas`.

`@hint`
To build `downstairs`, you can use `[:6]`. To build `upstairs`, you can use `[6:]`.

`@sample_code`
```{python}
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Alternative slicing to create downstairs


# Alternative slicing to create upstairs

```

`@solution`
```{python}
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Alternative slicing to create downstairs
downstairs = areas[:6]

# Alternative slicing to create upstairs
upstairs = areas[6:]
```

`@sct`
```{python}
msg = "Don't remove or edit the predefined `areas` list."
Ex().check_object("areas", missing_msg = msg).has_equal_value(incorrect_msg = msg)

patt = "Your definition of `%s` is incorrect. Use the `areas[...]` and slicing to select the elements you want. You could use `%s` where the dots are, for example."
Ex().check_object("downstairs").has_equal_value(incorrect_msg = patt % ("downstairs",":6"))
Ex().check_object("upstairs").has_equal_value(incorrect_msg = patt % ("downstairs",":6"))

success_msg("Wonderful!")
```

---
## Subsetting lists of lists

```yaml
type: MultipleChoiceExercise
lang: python
xp: 50
skills: 2
key: dbbbd306cf
```

You saw before that a Python list can contain practically anything; even other lists! To subset lists of lists, you can use the same technique as before: square brackets. Try out the commands in the following code sample in the IPython Shell:

```
x = [["a", "b", "c"],
     ["d", "e", "f"],
     ["g", "h", "i"]]
x[2][0]
x[2][:2]
```

`x[2]` results in a list, that you can subset again by adding additional square brackets.

What will `house[-1][1]` return? `house`, the list of lists that you created before, is already defined for you in the workspace. You can experiment with it in the IPython Shell.

`@instructions`
- A float: the kitchen area
- A string: `"kitchen"`
- A float: the bathroom area
- A string: `"bathroom"`

`@hint`
`house[-1]` selects the last element of `house`, which is the list `["bathroom", 9.50]`. What's the result if you then subset this sublist with `[1]`? You can always try out the command in the IPython Shell!

`@pre_exercise_code`
```{python}
house = [["hallway", 11.25],
         ["kitchen", 18.0],
         ["living room", 20.0],
         ["bedroom", 10.75],
         ["bathroom", 9.50]]
```

`@sct`
```{python}
msg1 = msg2 = "Wrong. `house[-1]` selects the last element of `house`, which is the list `[\"bathroom\", 9.50]`."
msg3 = "Correctomundo! The last piece of the list puzzle is manipulation."
msg4 = "Incorrect. `house[-1]` indeed selects the list that represents the bathroom information, but `[1]` selects the second element of the sublist, not the first. Python uses zero-based indexing!"
Ex().has_chosen(3, [msg1, msg2, msg3, msg4])
```

---
## List Manipulation

```yaml
type: VideoExercise
lang: python
xp: 50
skills: 2
key: fbdaaec22a
```

`@video_link`
//player.vimeo.com/video/149289041

`@video_hls`
//videos.datacamp.com/transcoded/735_intro_to_python/v1/hls-ch2_3.master.m3u8

*** =projector_key
823af3a8a05cb88df3f2b0dca71cec7f

---
## Replace list elements

```yaml
type: NormalExercise
lang: python
xp: 100
skills: 2
key: 4e1bba1b55
```

Replacing list elements is pretty easy. Simply subset the list and assign new values to the subset. You can select single elements or you can change entire list slices at once.

Use the IPython Shell to experiment with the commands below. Can you tell what's happening and why?

```
x = ["a", "b", "c", "d"]
x[1] = "r"
x[2:] = ["s", "t"]
```

For this and the following exercises, you'll continue working on the `areas` list that contains the names and areas of different rooms in a house.

`@instructions`
- Update the area of the bathroom area to be 10.50 square meters instead of 9.50.
- Make the `areas` list more trendy! Change `"living room"` to `"chill zone"`.

`@hint`
- Use `areas[-1] = ___` to update the bathroom area. Can you fill in the blanks?
- Similarly, you can use `areas[4] = ___` to update the element `"living room"`.

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
chillzone_msg = 'You can use `areas[4] = "chill zone"` to update the bathroom area.'
Ex().check_correct(
  check_object('areas').has_equal_value(incorrect_msg = 'Your changes to `areas` did not result in the correct list. Are you sure you used the correct subset operations? When in doubt, you can use a hint!'),
  multi(
    has_equal_ast(code = 'areas[-1]', incorrect_msg = bathroom_msg),
    has_equal_ast(code = '10.5', incorrect_msg = bathroom_msg),
    has_equal_ast(code = 'areas[4]', incorrect_msg = chillzone_msg),
    has_equal_ast(code = '"chill zone"', incorrect_msg = chillzone_msg)
  )
)
success_msg('Sweet! As the code sample showed, you can also slice a list and replace it with another list to update multiple elements in a single command.')
```

---
## Extend a list

```yaml
type: NormalExercise
lang: python
xp: 100
skills: 2
key: ff0fe8d967
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

`@sample_code`
```{python}
# Create the areas list and make some changes
areas = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0,
         "bedroom", 10.75, "bathroom", 10.50]

# Add poolhouse data to areas, new list is areas_1


# Add garage data to areas_1, new list is areas_2

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
type: MultipleChoiceExercise
lang: python
xp: 50
skills: 2
key: 85f792356e
```

Finally, you can also remove elements from your list. You can do this with the `del` statement:

```
x = ["a", "b", "c", "d"]
del(x[1])
```

Pay attention here: as soon as you remove an element from a list, the indexes of the elements that come after the deleted element all change!

The updated and extended version of `areas` that you've built in the previous exercises is coded below. You can copy and paste this into the IPython Shell to play around with the result.

```
areas = ["hallway", 11.25, "kitchen", 18.0,
        "chill zone", 20.0, "bedroom", 10.75,
         "bathroom", 10.50, "poolhouse", 24.5,
         "garage", 15.45]
```

There was a mistake! The amount you won with the lottery is not that big after all and it looks like the poolhouse isn't going to happen. You decide to remove the corresponding string and float from the `areas` list.

The `;` sign is used to place commands on the same line. The following two code chunks are equivalent:

```
# Same line
command1; command2

# Separate lines
command1
command2
```

Which of the code chunks will do the job for us?

`@instructions`

- `del(areas[10]); del(areas[11])`
- `del(areas[10:11])`
- `del(areas[-4:-2])`
- `del(areas[-3]); del(areas[-4])`

`@hint`
You can simply try all the different options to see if they work. Just make sure to re-initialize the `areas` list again before you try a new option.

`@pre_exercise_code`
```{python}
areas = ["hallway", 11.25, "kitchen", 18.0,
        "chill zone", 20.0, "bedroom", 10.75,
         "bathroom", 10.50, "poolhouse", 24.5,
         "garage", 15.45]
```

`@sct`
```{python}
msg1 = "If you first remove `areas[10]`, all elements after index 10 move up a spot. If you then do `del(areas[11])`, you are deleting the element that was originally at index `12`."
msg2 = "`areas[10:11])` will only select the element at index `10`."
msg3 = "Correct! You'll learn about easier ways to remove specific elements from Python lists later on."
msg4 = "This code chunk will not correctly remove the poolhouse-related information. Try again."
Ex().has_chosen(3, [msg1, msg2, msg3, msg4])
```

---
## Inner workings of lists

```yaml
type: NormalExercise
lang: python
xp: 100
skills: 2
key: af72db9915
```

At the end of the video, Filip explained how Python lists work behind the scenes. In this exercise you'll get some hands-on experience with this.

The Python code in the script already creates a list with the name `areas` and a copy named `areas_copy`. Next, the first element in the `areas_copy` list is changed and the `areas` list is printed out. If you hit _Run Code_ you'll see that, although you've changed `areas_copy`, the change also takes effect in the `areas` list. That's because `areas` and `areas_copy` point to the same list.

If you want to prevent changes in `areas_copy` from also taking effect in `areas`, you'll have to do a more explicit copy of the `areas` list. You can do this with [`list()`](https://docs.python.org/3/library/functions.html#func-list) or by using `[:]`.

`@instructions`
Change the second command, that creates the variable `areas_copy`, such that `areas_copy` is an explicit copy of `areas`. After your edit, changes made to `areas_copy` shouldn't affect `areas`. Hit _Submit Answer_ to check this.

`@hint`
Change the `areas_copy = areas` call. Instead of assigning `areas`, you can assign `list(areas)` or `areas[:]`.

`@sample_code`
```{python}
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Create areas_copy
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

# Create areas_copy
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


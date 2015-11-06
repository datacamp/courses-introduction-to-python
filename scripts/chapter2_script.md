## Lists

Before, you've played around with all kinds of data types. Each variable referenced to a single value, such as a float or a boolean. In data science, you'll often want to work with more than that. If you for example want to measure the height of everybody in your family, and store this information in python, it would be pretty bothersome to create a new python variable for each data point you collected right?

What you can do instead, is store all this information in a python list. You can build such a list with square brackets. Suppose you asked your two sisters and parents for their height, in centimeters. You can build the list as follows:

```
[173, 168, 171, 189]
```

Of course, also this data structure can be referenced to with a variable. Simply put the variable name and the equals sign in in front, like here:

```
fam_height = [173, 168, 171, 189]
```

More formally, a list is simply a data structure that can hold an arbitrary number of elements, and these elements can have any type; they can be floats, integer, booleans, but also more advanced Python types and even other lists. Also, it's perfectly possible to have a list containing different types. Suppose that you want to add the names of your sisters and parents to the list, so that you know which height belongs to who. You can throw in some strings without issues:

```
fam_height = ["elise", 173, "emma", 168, "mom", 171, "dad", 189]
```

_Notice here that I put in a space after each comma; I did this to enhance the readability of your Python command. I'm following the official python style guide here, that ev_

Now that we have a list that we're satisfied with, let's check out its type with the `type()` function. 

```
type(fam_height)
```

The list is an object with the type list. This is thus a new Python type next to the strings, booleans, integers and floats you already know. I told you before that each type has special functionality built in to work them, remember? Well, for lists, this is also true. Python lists host a bunch of tools to subset, extend and adapt them. But let's take this step by step, and have you experiment with list creation first!

## Subsetting a list



## Manipulate those lists

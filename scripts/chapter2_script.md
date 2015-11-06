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

## Subsetting lists

After you've created your very own Python list, you might wonder how you can access information in the list. Suppose you want to select the height of your youngest sister, emma. As you can see from fam_height here, her height is 168 centimers, and this integer is the fourth element in the list. To access this element, you'll need this line of code:

```
fam_height[3]
```

The number three refers to the index of the list element. Because python uses so-called zero-based indexing, the first element in the list has index 0, the second element has index 1, and so on. This means that the fourth element, the integer 168, has index 3. To select the string "dad" from the list, which is sevent element in the list, you'll need to put the index 6 inside square brackets:

```
fam_height[6]
```

You can also count backwards, using negative indices. If you want to have the last element in the list, the height of dad, you can use the index -1. _NEED MORE EXPLANATION HERE?_

```
fam_height[-1]
```

This means that this line and this line, return the same result:

```
fam_height[6]
fam_height[-2]
```

Apart from selecting only single elements from lists, you can also subset multiple elements in a list, thus creating a new list. You can do this by specifying a range, using a colon. Take this piece of code:

```
fam_height[3:5]
```

Can you guess what it'll return? A list with the the integer 168, he integer "mom", and the integer 171, corresponding to the 4th, 5th and 6th element in the list maybe? Let's see what the output is.

```
[168, 'mom']
```

Apparently, only the elements with index 3 and 4, get returned. The index you specify before the colon is included, the index you specify after the colon is not. Now that you know this, can you tell what this call will return?

```
fam_height[1:4]
```

You probably guessed correctly that this call gives you a list with three elements, corresponding to the elements with index 1, 2 and 3 of the fam_height list. You can use this colon operator in many other ways, but I'll save that for the exercises. You'll continue to work on the list you've created yourself before and use different subsetting methods to get exactly the piece of information you need!

## Manipulating lists

After creation and subsetting, the final piece of the Python lists puzzle is manipulation.

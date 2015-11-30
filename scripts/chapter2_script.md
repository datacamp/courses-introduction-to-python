## Lists

By now, you've played around with different data types. On the numbers side, there's the `float`, to represent a real number, and the `int`, to represent an integer. Next, we also have `str`, short for string, to represent text in Python, and `bool`, which can be either `True` or `False`. You can store values with these different types in a variable, like this. But in this case, each variable represents a single value.

As a data scientist, you'll often want to work with more than that. If you for example want to measure the height of everybody in your family, and store this information in python, it would be pretty stupid to create a new python variable for each data point you collected right?

What you can do instead, is store all this information in a python _list_. You can build such a list with square brackets. Suppose you asked your two sisters and parents for their height, in meters. You can build the list as follows:

Of course, also this data structure can be referenced to with a variable. Simply put the variable name and the equals sign in front, like here:

More formally, a list is a so-called compound data type, used to group together other values. These values, or elements, can have any type; they can be floats, integer, booleans, strings, but also more advanced Python types, even lists. 

It's perfectly possible for a list to contain different types. Suppose, for example, that you want to add the names of your sisters and parents to the list, so that you know which height belongs to who. You can throw in some strings without issues:

I you check out the type of this list, you will see that it is simply "list":

This means we're dealing with a new Python type next to the strings, booleans, integers and floats you already know about. Remember that I told you that each type has specific functionality and behavior associated? Well, for lists, this is also true. Python lists host a bunch of tools to subset and adapt them. But let's take this step by step, and have you experiment with list creation first!

```
[1.73, 1.68, 1.71, 1.89]
fam_height = [1.73, 1.68, 1.71, 1.89]
fam_height
fam_height = ["elise", 1.73, "emma", 1.68, "mom", 1.71, "dad", 1.89]
fam_height
type(fam_height)
```

## Subsetting lists

After you've created your very own Python list, you might wonder how you can access information in the list. Suppose you want to select the height of your youngest sister, emma. As you can see from fam_height here, her height is 1.68 meters, and this integer is the fourth element in the list. To access this element, you'll need this line of code.

The number three refers to the _index_ of the list element. Because python uses so-called zero-based indexing, the first element in the list has index 0, the second element has index 1, and so on. This means that the fourth element, the float 1.68, has index 3. To select the string "dad" from the list, which is the sevent element in the list, you'll need to put the index 6 inside square brackets:

You can also count backwards, using negative ubdexes. This is useful if you want to get some elements at the end of your list. To get your dad's height, for example, you'll need the index -1. These are the negative indexes for all list elements.

This means that this line and this line, return the same result:

Apart from indexing, there's also something called slicing, which allows you to select multiple elements from a list, thus creating a new list. You can do this by specifying a range, using a colon. Let's first have another look at the list, and then try this piece of code:

Can you guess what it'll return? A list with the the float 1.68, the string "mom", and the float 1.71, corresponding to the 4th, 5th and 6th element in the list maybe? Let's see what the output is.

Apparently, only the elements with index 3 and 4, get returned. In general, this is the syntax: the index you specify before the colon, so where the slice begins, is included, while the index you specify after the colon, where the slice ends, is not.

With this in mind, can you tell what this call will return? <PAUSE>

You probably guessed correctly that this call gives you a list with three elements, corresponding to the elements with index 1, 2 and 3 of the fam_height list. 

You can use this colon operator in many other ways, but I'll save that for the exercises. There, you'll continue to work on the list you've created yourself before and use different subsetting methods to get exactly the piece of information you need!


```
fam_height = ["elise", 1.73, "emma", 1.68, "mom", 1.71, "dad", 1.89]
fam_height
fam_height[3]
fam_height[-1]
fam_height[6]
fam_height[-2]

fam_height
fam_height[3:5]
fam_height[1:4]
```



## Manipulating lists

After creation and subsetting, the final piece of the Python lists puzzle is manipulation, so ways to change elements in your list, or to add elements to and remove elements from your list.

Changing list elements is pretty straightforward. You use the same square brackets that we've used to subset lists, and then assign new elements to it using the equals sign. Suppose that after another look at `fam_height`, you realize that your dad's height is not up to date anymore as he's shrinking with age. Instead of 1.89 meters, it should be 1.86 meters. To change this list element, which is at index 7, you can use this line:

If you now check out fam_height, you'll see that the value is updated:

You can even change an entire list slice at once. To change the elements "elise" and 1.73, you can do something like this:

Notice here, that your resulting subset is a list, so you have to pass a list with the same length to make the replacement.

Do you still remember how the plus operator was different for strings and integers? Well, it's again different for lists. If you use the plus sign with two lists, Python simply pastes together their contents in a single list. Suppose you want to add your own name and height to the fam height list. This will do the trick:

Of course, you can also store this new list in a variable, `fam_height_ext` for example.

Finally, deleting a list is also pretty straightforward, you'll have to use `del` here. Take this line, for example, that deletes the element with index 2, so "emma", from the list:

If you check out fam_height now, you'll see that the "emma" string is gone now. Because you've removed an index, all elements that came after "emma" scooted over by one index. If you again run the same line, you're again removing the element at index 2, which is emma's length, 1.68 centimeters:

Understanding how Python lists actually work behind the scenes becomes pretty important now. What actually happens when you create a new list, `x`, like this?

Well, in a simplified sense, you're storing a list in your computer memory, and store the 'address' of that list, so where the list is in your computer memory, in `x`. This means that `x` does not actually contain all the list elements, it rather contains a reference to the list. For basic operations, the difference is not that important, but it becomes more so when you start copying lists. Let me clarify this with an example.

Let's store the list `x` as a new variable `y`, by simply using the equals sign:

Let's now change the element with index one in the list `y`, as follows:

The funky thing is that if you now check out `x` again, also here the second element was changed:

That's because when you copied x to y with the equals sign, you copied the reference to the list, not the actual values themselves. When you're updating an element the list, though, it's one and the same list in the computer memory your changing.Both `x` and `y` point to this list, so the update is visible from both.

If you want to create a list `y` that points to a new list in the memory with the same variables, you'll need to use something else than the equals sign. You can use the `list()` function, like this, or use slicing to select all list elements explicitly.

If you now make a change to the list `y` points to, `x` is not affected:

If this was a bit too much to take in, don't worry. The exercises will help you understand list manipulation and the subtle inner workings of lists. I'm sure you'll do great!

```
fam_height = ["elise", 1.73, "emma", 1.68, "mom", 1.71, "dad", 1.89]
fam_height
fam_height[7] = 1.86
fam_height
fam_height[0:1] = ["ellie", 1.74]
fam_height + ["me", 1.79]
fam_height_ext = fam_height + ["me", 1.79]
del(fam_height[2])
fam_height
del(fam_height[2])
fam_height

x = ["a", "b", "c"]
y = x
y[1] = "z"
y
x

x = ["a", "b", "c"]
y = list(x)
y = x[:]
y[1] = "z"
x
```


## MUTABLE VS IMMUTABLE STUFF

You can do all of this because a Python list is a so-called mutable type. After you've created a list, you can make changes to it. Types like strings, integers and booleans, on the other hand, are not mutable, or immutable: You can't tell integer 3 to become 7:

```
3 = 7
```

This is different than creating a variable, say `x`, that pionts to the value 3:

```
x = 3
```

And afterwards changing `x`:

```
x = 7
```

This call didn't change 3 to be 7. instead, Python stored the value 7 in memory, and now has `x` pointing to 7, not to three.

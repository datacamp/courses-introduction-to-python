## Lists

Before, you've played around with all kinds of data types. Each variable referenced to a single value, such as a float or a boolean. As a data scientist, you'll often want to work with more than that. If you for example want to measure the height of everybody in your family, and store this information in python, it would be pretty bothersome to create a new python variable for each data point you collected right?

What you can do instead, is store all this information in a python list. You can build such a list with square brackets. Suppose you asked your two sisters and parents for their height, in centimeters. You can build the list as follows:

```
[173, 168, 171, 189]
```

Of course, also this data structure can be referenced to with a variable. Simply put the variable name and the equals sign in front, like here:

```
fam_height = [173, 168, 171, 189]
```

More formally, a list is simply a data structure that can hold an arbitrary number of elements, and these elements can have any type; they can be floats, integer, booleans, but also more advanced Python types. It's perfectly possible to have a list containing different types. Suppose, for example, that you want to add the names of your sisters and parents to the list, so that you know which height belongs to who. You can throw in some strings without issues:

```
fam_height = ["elise", 173, "emma", 168, "mom", 171, "dad", 189]
```

Now that we have a list that we're satisfied with, let's check out its type with the `type()` function. 

```
type(fam_height)
```

The list is an object of the type list. This is thus a new Python type next to the strings, booleans, integers and floats you already know. Remember that I told you that each type has specific functionality and behavior associated? Well, for lists, this is also true. Python lists host a bunch of tools to subset and adapt them. But let's take this step by step, and have you experiment with list creation first!

## Subsetting lists

After you've created your very own Python list, you might wonder how you can access information in the list. Suppose you want to select the height of your youngest sister, emma. As you can see from fam_height here, her height is 168 centimers, and this integer is the fourth element in the list. To access this element, you'll need this line of code:

```
fam_height[3]
```

The number three refers to the index of the list element. Because python uses so-called zero-based indexing, the first element in the list has index 0, the second element has index 1, and so on. This means that the fourth element, the integer 168, has index 3. To select the string "dad" from the list, which is sevent element in the list, you'll need to put the index 6 inside square brackets:

```
fam_height[6]
```

You can also count backwards, using negative indices. If you want to have the last element in the list, the height of dad, you can use the index -1. _NEED NICE ANIMATIONS HERE!_

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

Can you guess what it'll return? A list with the the integer 168, the integer "mom", and the integer 171, corresponding to the 4th, 5th and 6th element in the list maybe? Let's see what the output is.

```
[168, 'mom']
```

Apparently, only the elements with index 3 and 4, get returned. The index you specify before the colon is included, the index you specify after the colon is not. Now that you know this, can you tell what this call will return?

```
fam_height[1:4]
```

You probably guessed correctly that this call gives you a list with three elements, corresponding to the elements with index 1, 2 and 3 of the fam_height list. You can use this colon operator in many other ways, but I'll save that for the exercises. There, you'll continue to work on the list you've created yourself before and use different subsetting methods to get exactly the piece of information you need!

## Manipulating lists

After creation and subsetting, the final piece of the Python lists puzzle is manipulation, so ways to change elements in your list, or to add elements to and remove elements from your list. All of this is possible because in Python, a list is a so-called mutable object: after you've created it, you can make changes to it. This contrasts with immutable objects in Python: once they're created, there's no way to make changes to them anymore.

Changing list elements is pretty straightforward. You use the same square brackets that we've used to subset lists, and then assign new elements to it using the equals sign. Suppose that you wrongly measure your dad's height; it's not up to date as he's shrinking with age. Instead of 189 centimers, it should be 186 centimters. To change this list elements, which is at index 7, you can use this line:

```
fam_height[7] = 186
```

Remember that you can also use a negative index here, like this:

```
fam_height[-1] = 186
```

If you now check out fam_height, you'll see that the value is updated:

```
fam_height
```

You can even change a range of elements in a list at once. To change the elements "elise" and 173, you can do something like this:

```
fam_height[0:1] <- ["ellie", 174]
```

Notice here, that your resulting subset is a list, so you have to pass a list with the same length to make the replacement.

Do you still remember how the plus operator was different for strings and integers? Well, it's again different for lists. If you add use the plus sign with two lists, Python simply pasting together their contents in a single list. Suppose you want to add your own name and height to the fam height list. This will do the trick:

```
fam_height + ["me", 185]
```

Of course, you can also store this new list in a variable, `fam_height_ext` for example:

```
fam_height_ext = fam_height + ["me", 185]
```

This approach, where you first store the list you want to add in a variable, works fine as well:

```
my_height = ["me", 185]
fam_height_ext = fam_height + my_height
```

Finally, deleting a list is also pretty straightforward, but you'll have to use the `del()` function here. Take this line, for example, that deletes the element with index 2, so "emma", from the list:

```
del(fam_height[2])
```

If you check out fam_height now, you'll see that the "emma" string is gone now. But watch out here. The fact that you've removed an index, means that all elements after "emma" have shifted up one spot. If you again run the same line, you're again removing the element at index 2, which is emma's length, 168 centimeters:

```
del(fam_height[2])
fam_height
```

_THIS STUFF IS SUPERHARD TO EXPLAIN!_

Understanding how Python lists actually work behind the scenes becomes pretty important now. A list is not really an array of elements of different types. It's actualy an array of _references_ to elements of different types. The actual data, so the strings and the integers, is stored on your computer somewhere, and the "address" to that data is stored in your list. This subtle difference becomes importing when you start copying lists. Let me clarify this with an example.

Suppose you have a list, `x`, with three strings in it, like this:

```
x = ["a", "b", "c"]
```

This list "x" is actually an array of references to these values. Let's now store this list as a new variable `y`, by simply using the equals sign:

```
y = x
```

`y` contains the exact reference to elements as `x`.

Let's now change the element with index one in the list `y`, as follows:

```
y[1] = 2
y
```

The funky thing is that if you now check out `x` again, also here the second element was changed. That's because your update of the list element has actually changed the value of the data stored on your system, but not the reference to it. BLABLA DISCUSS WITH VINCENT!!!

To do a 'hard copy' of a list, you'll need to explicitly ask for all the list elements, and then put them in a new list, like this:

```
y = x[:]
```

If this was a bit too much to take in, don't worry. The exercises will help you understand list manipulation and the subtle inner workings of lists. I'm sure you'll do great!
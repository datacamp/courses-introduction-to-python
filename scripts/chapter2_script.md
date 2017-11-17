--- video_exercise_key:f366e876d8

## Lists

By now, you've played around with different data types. On the numbers side, there's the float, to represent a real number, and the int, to represent an integer. Next, we also have str, short for string, to represent text in Python, and bool, which can be either True or False. You can save these values as a variable, like these examples show. Each variable then represents a single value.

As a data scientist, you'll often want to work with many data points. If you for example want to measure the height of everybody in your family, and store this information in Python, it would be inconvenient to create a new python variable for each point you collected right?

What you can do instead, is store all this information in a Python list. You can build such a list with square brackets. Suppose you asked your two sisters and parents for their height, in meters. You can build the list as follows:

Of course, also this data structure can be referenced to with a variable. Simply put the variable name and the equals sign in front, like here.

A list is a way to give a single name to a collection of values. These values, or elements, can have any type; they can be floats, integer, booleans, strings, but also more advanced Python types, even lists.

It's perfectly possible for a list to contain different types as well. Suppose, for example, that you want to add the names of your sisters and parents to the list, so that you know which height belongs to who. You can throw in some strings without issues.

But that's not all. I just told you that lists can also contain lists themselves. Instead of putting the strings in between the numbers, you can create little sublists for each member of the family. One for liz, one for emma and so on. Now, you can tell Python that these sublists are the elements of another list, that I named fam2: the little lists are wrapped in square brackets and separated with commas. If you now print out fam2, you see that we have a list of lists. The main list contains 4 sub-lists.

We're dealing with a new Python type here, next to the strings, booleans, integers and floats you already know about: the list. These calls show that both fam and fam2 are lists. Remember that I told you that each type has specific functionality and behavior associated? Well, for lists, this is also true. Python lists host a bunch of tools to subset and adapt them. But let's take this step by step, and have you experiment with list creation first!

--- video_exercise_key:9e15e5b8a0

## Subsetting lists

After you've created your very own Python list, you might wonder how you can access information in the list. Python uses the index to do this. Have a look at the fam list again here. The first element in the list has index 0, the second element has index 1, and so on. Suppose that you want to select the height of emma, the float 1.68. It's the fourth element, so it has index 3. To select it, you use 3 inside square brackets.

Similarly, to select the string "dad" from the list, which is the seventh element in the list, you'll need to put the index 6 inside square brackets.

You can also count backwards, using negative indexes. This is useful if you want to get some elements at the end of your list. To get your dad's height, for example, you'll need the index -1. These are the negative indexes for all list elements.

This means that this line and this line, return the exact same result.

Apart from indexing, there's also something called slicing, which allows you to select multiple elements from a list, thus creating a new list. You can do this by specifying a range, using a colon. Let's first have another look at the list, and then try this piece of code.

Can you guess what it'll return? A list with the the float 1.68, the string "mom", and the float 1.71, corresponding to the 4th, 5th and 6th element in the list maybe? Let's see what the output is.

Apparently, only the elements with index 3 and 4, get returned. The element with index 5 is not included. In general, this is the syntax: the index you specify before the colon, so where the slice starts, is included, while the index you specify after the colon, where the slice ends, is not.

With this in mind, can you tell what this call will return?

You probably guessed correctly that this call gives you a list with three elements, corresponding to the elements with index 1, 2 and 3 of the fam list. 

You can also choose to just leave out the index before or after the colon. If you leave out the index where the slice should begin, you're telling Python to start the slice from index 0, like this example.

If you leave out the index where the slice should end, you include all elements up to and including the last element in the list, like here.

Now it's time to head over to the exercises, where you will continue to work on the list you've created yourself before. You'll use different subsetting methods to get exactly the piece of information you need!

--- video_exercise_key:fbdaaec22a

## Manipulating lists

After creation and subsetting, the final piece of the Python lists puzzle is manipulation, so ways to change elements in your list, or to add elements to and remove elements from your list.

Changing list elements is pretty straightforward. You use the same square brackets that we've used to subset lists, and then assign new elements to it using the equals sign. Suppose that after another look at `fam`, you realize that your dad's height is not up to date anymore, as he's shrinking with age. Instead of 1.89 meters, it should be 1.86 meters. To change this list element, which is at index 7, you can use this line of code.

If you now check out fam, you'll see that the value is updated.

You can even change an entire list slice at once. To change the elements "liz" and 1.73, you access the first two elements with 0:2, and then assign a new list to it.

Do you still remember how the plus operator was different for strings and integers? Well, it's again different for lists. If you use the plus sign with two lists, Python simply pastes together their contents in a single list. Suppose you want to add your own name and height to the fam height list. This will do the trick.

Of course, you can also store this new list in a variable, `fam_ext` for example.

Finally, deleting elements from a list is also pretty straightforward, you'll have to use `del` here. Take this line, for example, that deletes the element with index 2, so "emma", from the list.

If you check out fam now, you'll see that the "emma" string is gone. Because you've removed an index, all elements that came after "emma" scooted over by one index. If you again run the same line, you're again removing the element at index 2, which is emma's height, 1.68 meters now.

Understanding how Python lists actually work behind the scenes becomes pretty important now. What actually happens when you create a new list, `x`, like this?

Well, in a simplified sense, you're storing a list in your computer memory, and store the 'address' of that list, so where the list is in your computer memory, in `x`. This means that `x` does not actually contain all the list elements, it rather contains a reference to the list. For basic operations, the difference is not that important, but it becomes more so when you start copying lists. Let me clarify this with an example.

Let's store the list `x` as a new variable `y`, by simply using the equals sign.

Let's now change the element with index one in the list `y`, as follows.

The funky thing is that if you now check out `x` again, also here the second element was changed.

That's because when you copied x to y with the equals sign, you copied the reference to the list, not the actual values themselves. When you're updating an element the list, it's one and the same list in the computer memory your changing. Both `x` and `y` point to this list, so the update is visible from both variables.

If you want to create a list `y` that points to a new list in the memory with the same values, you'll need to use something else than the equals sign. You can use the `list()` function, like this, or use slicing to select all list elements explicitly.

If you now make a change to the list `y` points to, `x` is not affected.

If this was a bit too much to take in, don't worry. The exercises will help you understand list manipulation and the subtle inner workings of lists. I'm sure you'll do great!

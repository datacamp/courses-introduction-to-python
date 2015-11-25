## Functions, what are they?

In this video, I'm going to introduce you to functions. Functions aren't entirely new for you actually: you've already used them. Print, for example, is a function to print out values when your executing a script. But what is a function? Simply put, a function is a piece of reusable code that is aimed at solving a particular task. You can call functions instead of having to write code yourself. Maybe an example can clarify things here.

Suppose you have the list containing only the heights of your family, fam_height:

Say that you want to get the maximum value in this list. Instead of writing your own piece of Python code that goes through the list and finds the highest value, you can also use Python's `max()` function. This is one of Python's built-in functions, just like `print()`. We simply pass `fam_height` to `max()` inside parentheses:

The output makes sense: 1.89, the highest number in the list. 

`max()` worked kind of like a black box here: you passed it a list, then the implementation of `max()`, that you don't know, did its magic, and produced an output. How `max()` actually did this, is not important to you, it just does what it's supposed to, and you didn't have to write your own implementation, which made your life easier.

Of course, it's possible to also assign the result of a function call to a new variable, like here:

Another one of these built-in functions is `round()`. It takes a float and rounds it to 0 digits after the decimal point, as this example shows:


You can tell from the .0 part that the result is still a float. You can also choose the number of digits after the decimal point, by passing   `round()` a second input, 1 for example. You separate different inputs with a comma.

If you don't know how to use the `round()` function, you can use the `help()` function to open up the documentation on the function, as follows; 

It appears that `round()` takes two inputs, also called arguments: `number` and `ndigits`. The first argument you pass has to be a numerical value. From the square brackets around the comma and `ndigits`, you can tell that the second argument is optional. If you don't specify this argument, `round()` automatically rounds your number to zero digits. So this call <PAUSE> and this call <PAUSE> are equivalent.

Now you know how to use `round()`, but how could you know that a function such as `round()` exists in Python in the first place? Well, this is something you will learn with time. Whenever you are doing a pretty standard task in Python, you can be pretty sure that there's already a function that can do this for you. A quick internet search will help you out.

Off to the exercises now, where you'll learn about interesting functions and how to call them to supercharge your Python code!


```
fam_height = [1.73, 1.68, 1.71, 1.89]
fam_height
max(fam_height)

tallest = max(fam_height)
tallest

round(1.73)
round(1.73, 1)

help(round)
round(1.73)
round(1.73, 0)
```

## Methods

Calling built-in functions is only one part of the story. In Python, you also have something called methods, which are functions that "belong to" Python objects. Every string, boolean, list, and so on, is a Python object, and depending type, each python object has a bunch of methods associated with them. You can call these methods with the dot notation. Lists, for example, have the append() method, to add elements. 

Here's the fam_height list again:

To add new elements to it, you can write fam_height, dot, append, with the value you want to add to the list as input in parentheses, like this.

`fam_height` was updated and now also contains the string "me":

You can also add your actual lenght, 1.79, like so:

The append method is thus called "on" the fam_height list and this list is then extended. Again, how on earth could you know that this function existed? Well, you can simply type help(list) - list is the type of Python lists - and start browsing through all the methods that are associated with the list type.

The first method that shows here is __add__ by the way, which is Python slang for the plus operator. This means that the plus operator is also a method available for lists. The only strange thing is that the + operator is an inline version of the __add__ moethod. These two calls do the exact same thing. Other types also have this add method, but the implementation is different. That's the thing: different types can have the same method name, but these methods can behave differently.

Of course, there are also methods that are specific to the Python object you're dealing with. Booleans for example, which have type `bool`, don't offer the `append()` method. That's why this line of nonsense throws an error:

Let's take a step back here and summarise this: 

you have Python functions, like `print()`, `type()` and `max()`, that you can call like this:

There's also methods, which are functions that are specific to Python objects. Depending on the type of the Python object you're dealing with, you'll be able to use different methods and they behave differently. You can call methods _on_ the objects with the dot notation, like this for example.

Here, we asked for the index of the string `"dad"` in the `fam_height` list.
It's time to head over to the exercises and add methods to your evergrowing skill set!

```
fam_height = ["elise", 1.73, "emma", 1.68, "mom", 1.71, "dad", 1.89]
fam_height
fam_height.append("me")
fam_height
fam_height.append(1.79)
fam_height
# help(list)
[1, 2, 3] + [4]
[1, 2, 3].__add__([4])
True.append(False)

type(fam_height)
fam_height.index("dad")
```

## Packages

By now, I hope you're convinced that python functions and methods are extremely powerful: you can basically use other people's code to solve your own problems. That's the real open source spirit. However, making available all functions and methods written by all Python developers in the universe in the Python distribution would be a mess. There would be tons and tons of code in there, that you'll never use.

This is where packages come into play. A python package is basically a directory of Python scripts, which are called modules, that specify functions, methods and other Python objects aimed at solving particular problems. There are hundreds, if not thousands of Python packages available from the internet, also for data science related tasks: there's numpy to efficiently work with arrays, matplotlib for data visualization, scikit-learn for machine learning, and many others.

All these packages are not available in Python by default. To use Python packages, you'll have to install them on your system, and then put code in your script to tell Python that you want to use these packages. This is fairly easy, so let's get to it!








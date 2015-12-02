## Functions, what are they?

In this video, I'm going to introduce you to functions. Functions aren't entirely new for you actually: you've already used them. Print, for example, is a function to print out values when your executing a script. But what is a function? Simply put, a function is a piece of reusable code that is aimed at solving a particular task. You can call functions instead of having to write code yourself. Maybe an example can clarify things here.

Suppose you have the list containing only the heights of your family, fam:

Say that you want to get the maximum value in this list. Instead of writing your own piece of Python code that goes through the list and finds the highest value, you can also use Python's `max()` function. This is one of Python's built-in functions, just like `print()`. We simply pass `fam` to `max()` inside parentheses:

The output makes sense: 1.89, the highest number in the list. 

`max()` worked kind of like a black box here: you passed it a list, then the implementation of `max()`, that you don't know, did its magic, and produced an output. How `max()` actually did this, is not important to you, it just does what it's supposed to, and you didn't have to write your own implementation, which made your life easier.

Of course, it's possible to also assign the result of a function call to a new variable, like here:

Another one of these built-in functions is `round()`. It takes a float and rounds it to 0 digits after the decimal point, as this example shows:


You can tell from the .0 part that the result is still a float. You can also choose the number of digits after the decimal point, by passing   `round()` a second input, 1 for example. You separate different inputs with a comma.

If you don't know how to use the `round()` function, you can use the `help()` function to open up the documentation on the function, as follows; 

It appears that `round()` takes two inputs, also called arguments: `number` and `ndigits`. The first argument you pass has to be a numerical value. From the square brackets around the comma and `ndigits`, you can tell that the second argument is optional. If you don't specify this argument, `round()` automatically rounds your number to zero digits. So this call <PAUSE> and this call <PAUSE> are equivalent.

Now you know how to use `round()`, but how could you know that a function such as `round()` exists in Python in the first place? Well, this is something you will learn with time. Whenever you are doing a pretty standard task in Python, you can be pretty sure that there's already a function that can do this for you. A quick internet search will help you out.

Head over to the interactive exercises, to learn about interesting functions and how to call them to supercharge your Python code!

```
fam = [1.73, 1.68, 1.71, 1.89]
fam
max(fam)

tallest = max(fam)
tallest

round(1.73)
round(1.73, 1)

help(round)
round(1.73)
round(1.73, 0)
```

## Methods

Calling built-in functions is only one part of the story. In Python, you also have something called methods, which are functions that "belong to" Python objects. Every string, boolean, list, and so on, is a Python object, and depending type, each python object has a bunch of methods associated with them. You can call these methods with the dot notation. Lists, for example, have the append() method, to add elements. 

Here's the fam list again:

To add new elements to it, you can write fam, dot, append, with the value you want to add to the list as input in parentheses, like this.

`fam` was updated and now also contains the string "me":

You can also add your actual lenght, 1.79, like so:

The append method is thus called "on" the fam list and this list is then extended. Again, how on earth could you know that this function existed? Well, you can simply type help(list) - list is the type of Python lists - and start browsing through all the methods that are associated with the list type.

The first method that shows here is __add__ by the way, which is Python slang for the plus operator. This means that the plus operator is also a method available for lists. The only strange thing is that the + operator is an inline version of the __add__ moethod. These two calls do the exact same thing. Other types also have this add method, but the implementation is different. That's the thing: different types can have the same method name, but these methods can behave differently.

Of course, there are also methods that are specific to the Python object you're dealing with. Booleans for example, which have type `bool`, don't offer the `append()` method. That's why this line of nonsense throws an error:

Let's take a step back here and summarise this: 

you have Python functions, like `print()`, `type()` and `max()`, that you can call like this:

There's also methods, which are functions that are specific to Python objects. Depending on the type of the Python object you're dealing with, you'll be able to use different methods and they behave differently. You can call methods _on_ the objects with the dot notation, like this for example.

Here, we asked for the index of the string `"dad"` in the `fam` list.
It's time to get some exercise and add methods to your evergrowing skill set!

```
fam = ["liz", 1.73, "emma", 1.68, "mom", 1.71, "dad", 1.89]
fam
fam.append("me")
fam
fam.append(1.79)
fam
# help(list)
[1, 2, 3] + [4]
[1, 2, 3].__add__([4])
True.append(False)

type(fam)
fam.index("dad")
```

## Packages

By now, I hope you're convinced that python functions and methods are extremely powerful: you can basically use other people's code to solve your own problems. However, adding all functions and methods written by all Python developers in the universe to the Python distribution would be a mess. There would be tons and tons of code in there, that you'll never use. Maintaining all this code would also be a real pain.

This is where packages come into play. You can think of package as a directory of Python scripts. Each such script is a so-called module. These module specify functions, methods and new Python types aimed at solving particular problems. There are thousands of Python packages available from the internet. Among them are packages for data science: there's numpy to efficiently work with arrays, matplotlib for data visualization, scikit-learn for machine learning, and many others.

All these packages are not available in Python by default. To use Python packages, you'll first have to install them on your system, and then put code in your script to tell Python that you want to use these packages.

To install a package, we'll use pip, a package maintenance system for Python. If you go to this URL, you can download the file `get-pip.py`. Next, you go to the terminal, and execute `python3 get-pip.py`. Now you can use pip to actually install a Python package of your choosing. Suppose we want to install the numpy package, which you'll learn about in the next chapter. You type `pip3 install numpy`. You have to use the commands python3 and pip3 here to tell our system that we want to work with Python version 3.

Now that the package is installed, you can actually start using it in one of your Python scripts. Before you can do this, you should import the package, or a specific module of the package. You can do this with the `import` statement.

To install the entire numpy package, you can do import numpy, like this.

A commonly used function in Numpy is `array()`. It takes a list as input. Simply calling the array function like this, will generate an error.

To refer to the array function from the numpy package, you'll need this:

Now it works. In the next chapter you'll learn what this function actually does, let's stick to details about importing packages and modules here.

Using this numpy dot prefix all the time can become pretty tiring, so you can also import the package and refer to it with a different name. You can do this by extending your import statement with as, like this:

Now, instead of numpy.array(), you'll have to use np.array() to use Numpy's array function:

As I told you before, a package is a collection of modules. For big packages, these modules are typically organized into several subpackages, which are again directories. Numpy, for example, has the `linalg` subpackage, which then contains the linalg submodule. Among many others, this module contains the `norm()` function. Because `numpy` is imported as `np`, you can already call it like this:

If you only plan to use the `linalg` subpackage and not the entire `numpy` package, you can make your import statement more specific, like this:

and then use this line of code to use the norm() function. You're explicitly naming the package, subpackage and function you're using with dots in between.

You can do a similar import with this line of code:

With this `from import` version, though, you don't have to include the numpy part anymore:

There's even a third way to go about this, where you explicitly import only the `norm()` function of the linalg subpackage:

Now, you don't need any prefix to call the norm function:

There's no clear reason to use only import statements, or only from import statements, both have their pros and cons. The import version makes it easy to import the entire module, but you have to write more code. If you're using from import, you make it very clear which items of a module you're using, but you lose context about the function. It's clearer what numpy.linarg.norm() does, instead of just using norm(), right?

Off to the exercises now, where you can practice on different ways of importing packages and modules yourself!

```
import numpy
array([1, 2, 3])
numpy.array([1, 2, 3])
import numpy as np
np.array([1, 2, 3])
np.linalg.norm([3, 4])
import numpy.linalg
numpy.linalg.norm([3, 4])
from numpy import linalg
linalg.norm([3, 4])
from numpy.linalg import norm
norm([3, 4])
```



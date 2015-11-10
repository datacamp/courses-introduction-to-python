## Functions, what are they?

Before, we've often used the `type()` function to get the type of any Python object, remember? But what is a function? Simply put, a function is a piece of readable code that is aimed at solving a particular task. You can then call this function instead of having to write this code yourself.

Suppose you have the same list from before, containing only the heights of your family:

```
fam_height = [173, 168, 171, 189]
```

Suppose you want to programmatically get the maximum value in this list. Instead of writing your own Python code that goes through the list and keeps the highest value, you can also use the `max()` function. This is one of Python's built-in functions, just like `type()`. We simply pass `fam_height` to `max()` inside parentheses:

```
max(fam_height)
```

The output makes sense: 189, the highest number in the list. `max()` worked kind of like a black box here: you passed it a list, the implementatino of `max()`, that you don't know, did its magic, and produced an output. How `max()` actually did this, is not important to you, it just does what it's supposed to, and you didn't have to write your own implementation, which can save you time.

Of course, it's possible to also assign the result of a function call to a new variable, like here:

```
tallest = max(fam_height)
```

Another one of these built-in functions is `round()`. It takes a float and rounds it to 0 digits after the decimal point, as this example shows:

```
round(7.316)
```

The result is stil a float, as you can see from the tracing .0 part. It would also be nice if you could choose the number of digits after the decimal point, right? `round()` allows you to this, by passing a second argument, 2 for example:

```
round(7.316, 2)
```

How did I know about these `max()` and `round()` functions? Well, it's something you learn with experience. Whenever you are doing something that you think is already built into python, I suggest you do a quick internet search to see if there's a function that does it for you. If you know the name of the function to use, but not how to use it, you can use the `help()` function, like this:

```
help(round)

Help on built-in function round in module builtins:

round(...)
    round(number[, ndigits]) -> number

    Round a number to a given precision in decimal digits (default 0 digits).
    This returns an int when called with one argument, otherwise the
    same type as the number. ndigits may be negative.
```

The description here perfectly summarizes it. It's also clear that the function only takes numerical values. What if you call this function with the list `fam_height` from before as an input? Python raises an error:

```
round(fam_height)
```

WRAP UP

## Methods

Calling built-in functions is only a part of the story. In Python, you also have something called methods, which are functions that "belong to" Python objects. Every string, boolean, list, and so on, comes with a bunch of methods that you can call. You do this with the dot notation. Let's try to add elements to the list of family heights, this time with the `append()` method.

```
fam_height = ["elise", 173, "emma", 168, "mom", 171, "dad", 189]
```

Simply type fam_height, dot, append, and then pass the value you want to add to the list between parentheses, like this:

```
fam_height.append("me")
```

`fam_height` now contains the string "me". to additionally your actual lenght, 179, you can again call the append method:

```
x = fam_height.append(179)
```

The append method is thus called "on" the fam_height list and this list is then extended. Again, how on earth could you know that this function existed? Well, simply typing help(list) - list is the type of Python lists - and browsing through all the methods mentioned there already gives you an idea.

The first method that shows here is __add__ by the way, which represents the plus operator. Remember how the the plus operator was different for strings, integers and lists? Well, the plus operator is actually also a method that was defined for the list object. The only strange thing is that the + operator is an inline version of the __add__ function. These two calls do the exact same thing:

```
[1, 2, 3] + [4]
[1, 2, 3].__add__([4])
```


Some of these methods that belong to Python objects exist for different types, such as the plus operator. Other methods are specific to the Python object you're dealing with. Booleans for example, which have type `bool`, don't offer the `append()` method, as this line of nonsense shows:

```
True.append(False)
```



## Packages

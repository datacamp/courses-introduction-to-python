## Hello Python!

Hi, my name is Filip, I'm a data scientist at DataCamp and I've been working on the _Introduction to Python for Data Science_ course. It's a long name, but that's to stress something: this course is not just another Python tutorial. Instead, the focus will be on using Python specifically for data science. By the end of this course, you'll know about powerful ways to store and manipulate data and to deploy powerful data science tools for your own analyses.

You will learn Python for Data Science through video lessons, like this one, that are followed by interactive exercises. You get your own Python session where you can experiment and try to come up with the correct code to solve the instructions. You're learning by doing, while receiving customized and instant feedback on your work.

Python is originally conceived by Guido Van Rossum. What started as a hobby project, soon became a general purpose programming language: you can use Python to build practically any piece of software you can think of. That's because it's very easy to build packages in Python, which is code that you can share with other people to solve specific problems. Throughout time, more and more of these package specifically built for data science have been developed. Suppose you want to make some fancy visualizations of your company's sales? There's a package for that. Or what about connecting to a database to analyze sensor measurements? There's also a package for that. 

Currently, there are two common versions of Python, version 2.7 and 3.5 and later. Apart from some syntactical differences, they are pretty similar, but as support for version 2 will fade over time, our courses focus on Python 3. To install Python 3 on your own system, follow the steps at this URL.

Now that you're all eyes and ears for Python, let's start experimenting. I'll start with the Python shell, a place where you can simply type Python code and immediately see the results. In DataCamp's exercise interface, this shell is embedded here. Let's start off simple and use Python as a fancy calculator. Let me type 4 + 5 and hit Enter. Python interprets what you typed and prints the result of your calculation, 9. What about mutliplying 2.3 and 6? The shell can handle it. The Python shell that's used here is not actually the original one; we're using IPython, short for Interactive Python, which is some kind of juiced up version of regular Python.

```
4 + 5
2.3 * 6
```

Apart from interactively working with Python, you can also have Python run so called python scripts. These python scripts are ordinary text files with the extension _dot py_. It's basically a list of Python commands that are compiled and executed, similar to when you type them in the shell yourself. Let's put the commands from before in a script now, that can be found here in DataCamp's interface. The next step is executing the script. You do this with 'Submit Answer'.

If you run this line of code in the DataCamp interface, no output will be shown. That's because you have to explicitly use `print()` inside scripts if you want to generate output during executing. Let's wrap our previous calculations in `print()` calls, and rerun the code. This time, the same output as before is generated, great!

Putting your code in Python scripts instead of manually retyping every step interactively will help you to keep structure and avoid retyping everything over and over again if you want to make a change; you simply make the change in the script, and rerun the entire thing. 

Now that you've got an idea about different ways of working with Python, I suggest you head over to the exercises. Have fun!


## Variables and types

A hugely important concept in practically every programming language, is the variable. Python isn't different: variables are used literally all the time. You can think of a variable as a way to reference to values in your program for later use. Not sure what I mean? Maybe an example can clarify. Suppose you measure your height and weight, in metric units: you are 1 point 79 meters tall, and weigh 68.7 kilograms. You can assign these values to two variables, called `height` and `weight`. You can do this with the equals sign, like this:

```
height = 1.79
```

For weight, you can do a similar thing:

```
weight = 68.7
```

If you now type the name of the variable,

```
height
```

Python looks for the value that goes behind the variable, and prints it out. Notice that when you create a variable, you don't generate an output, because Python assumes you'll be using this variable later on.

Let's now calculate the Body Mass Index, or BMI, which is your weight in kilograms divided by the square of your height in meters. You can do this with the actual values, like this,

```
68.7 / 1.79 ** 2
```

but you can just as well use the variables height and weight, like this.

```
weight / height ** 2
```

Finally, this version has Python store the result in a new variable, `bmi`. `bmi` now contains the same value as the one you calculated earlier.

```
bmi = weight / height ** 2
```

So far, we've only worked with numerical values, such as height and weight. In Python, these numbers all have a specific type. You can check out the type of a value with the `type()` function. To see the type of our bmi value, simply write type and then bmi between parentheses. You can see that it's a float, which is python's way of representing a real number, so a number which can have both an integer part and a decimal part. Python als has a type for integers: `int`, like this example:

```
day_of_week = 5
```

To do data science, you'll need more than ints and floats, though. Python features tons of other data types. The most common ones are strings and booleans. 

A string is Python's way to represent text. You can use both double and single quotes to build a string, as you can see from these examples. If you print the type of the last variable here, you see that it's str, short for string.

```
x = "body mass index"
y = 'this works too'
type(y)
```

The Boolean is a type that can either by True or False. You can think of it as 'Yes' and 'No' in everyday language. Booleans will be very useful in the future, to perform filtering operations on your data for example.

There's something special about Python data types. Have a look at this line of code, that sums two integers, and then this line of code, that sums two strings. 

```
2 + 3
"ab" + "cd"
```

For the integers, the values were summed, while for the strings, Python pasted the strings together. The plus operator behaved differently for different data types. This is a general principle: the functionality and behavior of this functionality depends on the types you're working with.

In the exercises that follow, you'll create your very first variables and experiment with some of Python's data types. I'll see you in the next video to explain all about lists.
















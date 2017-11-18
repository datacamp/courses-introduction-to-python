--- video_exercise_key:d5509896f7

## Hello Python!

Hi, my name is Filip and I'll be your host for Introduction to Python for Data Science. It's a long name, but that's to stress something: this is not just another Python tutorial. Instead, the focus will be on using Python specifically for data science. By the end of this course, you'll know about powerful ways to store and manipulate data and to deploy cool data science tools for your own analyses.

You will learn Python for Data Science through video lessons, like this one, and interactive exercises. You get your own Python session where you can experiment and try to come up with the correct code to solve the instructions. You're learning by doing, while receiving customized and instant feedback on your work.

Python was conceived by Guido Van Rossum. What started as a hobby project, soon became a general purpose programming language: nowadays, you can use Python to build practically any piece of software. But how did this happen? Well, first of all, Python is open source. It's free to use. Second, it's very easy to build packages in Python, which is code that you can share with other people to solve specific problems. Throughout time, more and more of these packages specifically built for data science have been developed. Suppose you want to make some fancy visualizations of your company's sales. There's a package for that. Or what about connecting to a database to analyze sensor measurements? There's also a package for that. 

Currently, there are two common versions of Python, version 2.7 and 3.5 and later. Apart from some syntactical differences, they are pretty similar, but as support for version 2 will fade over time, our courses focus on Python 3. To install Python 3 on your own system, follow the steps at this URL.

Now that you're all eyes and ears for Python, let's start experimenting. I'll start with the Python shell, a place where you can type Python code and immediately see the results. In DataCamp's exercise interface, this shell is embedded here. Let's start off simple and use Python as a calculator. Let me type 4 + 5 and hit Enter. Python interprets what you typed and prints the result of your calculation, 9. The Python shell that's used here is actually not the original one; we're using IPython, short for Interactive Python, which is some kind of juiced up version of regular Python that'll be useful later on.

Apart from interactively working with Python, you can also have Python run so called python scripts. These python scripts are simply text files with the extension (dot) py. It's basically a list of Python commands that are executed, almost as if you where typing the commands in the shell yourself, line by line. Let's put the command from before in a script now, that can be found here in DataCamp's interface. The next step is executing the script, by clicking 'Submit Answer'.

If you execute this script in the DataCamp interface, there's nothing in the output pane. That's because you have to explicitly use print() inside scripts if you want to generate output during execution. Let's wrap our previous calculation in a print() call, and rerun the script. This time, the same output as before is generated, great!

Putting your code in Python scripts instead of manually retyping every step interactively will help you to keep structure and avoid retyping everything over and over again if you want to make a change; you simply make the change in the script, and rerun the entire thing.

Now that you've got an idea about different ways of working with Python, I suggest you head over to the exercises. Use the IPython Shell for experimentation, and use the Python script editor to code the actual answer. If you click Submit Answer, your script will be executed and checked for correctness. Have fun!

--- video_exercise_key:ef8356fb92

## Variables and types

It's clear that Python is a great calculator. If you want to do more complex calculations though, you will want to "save" values while you're coding along. You can do this by defining a variable, with a specific, case-sensitive name. Once you create (or declare) such a variable, you can later call up its value by typing the variable name.

Suppose you measure your height and weight, in metric units: you are 1.79 meters tall, and weigh 68.7 kilograms. You can assign these values to two variables, named height and weight, with an equals sign:

If you now type the name of the variable, height,

Python looks for the variable name, retrieves its value, and prints it out.

Let's now calculate the Body Mass Index, or BMI, which is calculated as follows, with weight in kilograms and height in meters. You can do this with the actual values, but you can just as well use the variables height and weight, like in here. Every time you type the variable's name, you are asking Python to change it with the actual value of the variable. weight corresponds to 68.7, and height to 1.79.

Finally, this version has Python store the result in a new variable, bmi. bmi now contains the same value as the one you calculated earlier.

In Python, variables are used all the time. They help to make your code reproducible. Suppose the code to create the height, weight and bmi variable are in a script, like this. If you now want to recalculate the bmi for another weight, you can simply change the declaration of the weight variable, and rerun the script. The bmi changes accordingly, because the value of the variable weight has changed as well.

So far, we've only worked with numerical values, such as height and weight. In Python, these numbers all have a specific type. You can check out the type of a value with the type() function. To see the type of our bmi value, simply write type and then bmi inside parentheses. You can see that it's a float, which is python's way of representing a real number, so a number which can have both an integer part and a fractional part. Python also has a type for integers: int, like this example.

To do data science, you'll need more than ints and floats, though. Python features tons of other data types. The most common ones are strings and booleans. 

A string is Python's way to represent text. You can use both double and single quotes to build a string, as you can see from these examples. If you print the type of the last variable here, you see that it's str, short for string.

The Boolean is a type that can either be True or False. You can think of it as 'Yes' and 'No' in everyday language. Booleans will be very useful in the future, to perform filtering operations on your data for example.

There's something special about Python data types. Have a look at this line of code, that sums two integers, and then this line of code, that sums two strings. 

For the integers, the values were summed, while for the strings, the strings were pasted together. The plus operator behaved differently for different data types. This is a general principle: how the code behaves depends on the types you're working with.

In the exercises that follow, you'll create your first variables and experiment with some of Python's data types. I'll see you in the next video to explain all about lists.

## First steps into Python

Hi, my name is Filip, and I'm a data scientist at DataCamp. Together with Vincent, I've been working on the _Introduction to Python for Data Science_ course. It's a long name, I know, but that's to stress something: this course is not just another Python tutorial. Instead, we will focus on using Python specifically for data science. By the end of this course, you'll know about the basics to get started with your own data analyses in Python.

You will learn Python for Data Science through video lessons, like this one, that are followed by interactive exercises. You get your own Python session where you can experiment and try to come up with the correct code to solve the challenge. You're learning by doing, while receiving customized and instant feedback on your work.

Python is originally conceived by Guido Van Rossum, a Dutch programmer and big fan of Monty Python's flying circus, hence the name. What started as a hobby project, soon became a general purpose programming language. Nowadays, Python can be used to build practically any piece of software you can think of. It's very easy to build packages in Python, which is code that you can share with other people to solve specific problems. Suppose you want to make some fancy visualizations of your company's sales? There's a package for that. Or what about connecting to a database to analyze sensor measurements? There's also a package for that. Throughout time, more and more of these package specifically built for data science have been developed. Currently, there are two common version of Python, version 2.7 and 3.5 and later. For some syntactical differences, they are pretty similar, but as support for version 2 will fade over time, we are going to work solely with Python 3. To install Python 3 on your own system, follow the steps at this URL.

Now that you're all eyes and ears for Python, let's start experimenting. I'll start with the Python shell, a place where you can simply type Python code and immediately see the results. In DataCamp's exercise interface, this shell can be found here. Let's start off simple and use Python as a fancy calculator. Let me type 4 + 5 and hit Enter. Python interprets what you typed and prints the result of your calculation, 9. What about mutliplying 2.3 and 6? The shell can handle it. The Python shell we use here is not actually the original one; we're using IPython, short for Interactive Python. It's a package that enhances your Python experience when you're working directly in the shell. Think of it as Python on steroids.

Apart from interactively working with Python, you can also have Python run so called python scripts. These python scripts are ordinary text files with the extension _dot py_. It's basically a list of Python commands that have to be executed one after the other, as if you are typing in these things yourself in the shell. Let's put the commands from before in a script now, my_code.py. In DataCamp's interface, you can use this pane for that. The next step is of course running the script. You do this with the 'Submit Answer' button on DataCamp. On your own system, you'll have to type python followed by the path to your .py file in the console, like this for example.

```
python ~/python_scripts/my_code.py
```

The output you get when running the script in DataCamp and on your own system differs slightly. TODO ASK GLENN. WHAT'S DIFFERENCE AND WHY

Putting your code in Python scripts instead of manually retyping every step interactively will help you to keep structure and avoid retyping everything over and over again if you want to make a change; you simply make the change in the script, and rerun the entire thing. 

Now that you've got an idea about different ways of working with Python, I suggest you head over to the exercises. Have fun!


## Variables and their types

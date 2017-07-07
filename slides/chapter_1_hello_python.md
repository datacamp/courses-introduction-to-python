---
title: Hello Python!
key: 0a65626bc1ba0847ea5808aa4c5fdeca
video_link:
    hls: https://videos.datacamp.com/transcoded/735_intro_to_python/wb1/hls-ch1_1.master.m3u8
    mp4: https://videos.datacamp.com/transcoded_mp4/735_intro_to_python/wb1/ch1_1.mp4

transformations:
    translateX: 55
    translateY: 0
    scale: 0.8

--- type:TitleSlide key:e41cf5e0e7
## Hello Python!


*** =lower_third
name: Filip Schouwenaars
title: Instructor, DataCamp

*** =script
Hi, my name is Filip and I'll be your host for Introduction to Python for Data Science. 


--- type:FullSlide key:682d7a9e44
## What you will learn

*** =part1
- Python {{1}}
- Specifically for Data Science {{2}}
- Store data {{3}}
- Manipulate data {{4}}
- Tools for data analysis {{5}}

*** =script
 It's a long name, but that's to stress something: this is not just another Python tutorial. Instead, the focus will be on using Python specifically for data science. By the end of this course, you'll know about powerful ways to store and manipulate data and to deploy powerful data science tools for your own analyses.


--- type:FullSlide key:1f3666247e
## How you will learn

*** =part1
![](https://s3.amazonaws.com/assets.datacamp.com/production/course_4550/datasets/interface.png)

*** =script
You will learn Python for Data Science through video lessons, like this one, and interactive exercises. You get your own Python session where you can experiment and try to come up with the correct code to solve the instructions. You're learning by doing, while receiving customized and instant feedback on your work.


--- type:FullSlide key:59b1fc393d
## Python

*** =part1
- Guido Van Rossum {{1}}
- General Purpose: build anything {{2}}
- Open Source! Free! {{3}}
- Python Packages, also for Data Science {{4}}
    - Many applications and fields {{5}}
- Version 3.x - [https://www.python.org/downloads/]() {{6}}

*** =script
Python was conceived by Guido Van Rossum. What started as a hobby project, soon became a general purpose programming language: nowadays, you can use Python to build practically any piece of software. How did this happen? Well, first of all, Python is open source. It's free to use. Second, it's very easy to build packages in Python, which is code that you can share with other people to solve specific problems. Throughout time, more and more of these package specifically built for data science have been developed. Suppose you want to make some fancy visualizations of your company's sales? There's a package for that. Or what about connecting to a database to analyze sensor measurements? There's also a package for that.

Currently, there are two common versions of Python, version 2.7 and 3.5 and later. Apart from some syntactical differences, they are pretty similar, but as support for version 2 will fade over time, our courses focus on Python 3. To install Python 3 on your own system, follow the steps at this URL.




--- type:FullSlide key:f49521c587
## IPython Shell

*** =part1
Execute Python commands

![](https://s3.amazonaws.com/assets.datacamp.com/production/course_4550/datasets/interface.png)

*** =script
Now that you're all eyes and ears for Python, let's start experimenting. I'll start with the Python shell, a place where you can type Python code and immediately see the results. In DataCamp's exercise interface, 


--- type:FullSlide key:721121678e disable_transition:true
## IPython Shell

*** =part1
Execute Python commands 

![](https://s3.amazonaws.com/assets.datacamp.com/production/course_4550/datasets/shell_1.png)

*** =script
this shell is embedded here. Let's start off simple and use Python as a calculator.




--- type:FullSlide key:329ac0607f
## IPython Shell

*** =part1
![](https://s3.amazonaws.com/assets.datacamp.com/production/course_4550/datasets/shell_2.png) {{1}}

*** =script
Let me type 4 + 5 and hit Enter


--- type:FullSlide key:674c8dcb94 disable_transition:true
## IPython Shell

*** =part1
![](https://s3.amazonaws.com/assets.datacamp.com/production/course_4550/datasets/shell_3.png)

*** =script
Python interprets what you typed and prints the result of your calculation, 9. The Python shell that's used here is actually not the original one; we're using IPython, short for Interactive Python, which is some kind of juiced up version of regular Python that'll be useful later on.




--- type:FullSlide key:9cc7825ab9
## Python Script

*** =part1
- Text Files - .py {{1}}
- List of Python Commands {{2}}
- Similar to typing in IPython Shell {{3}}

*** =script
Apart from interactively working with Python, you can also have Python run so called python scripts. These python scripts are simply text files with the extension dot p y. It's basically a list of Python commands that are executed, almost as if you where typing the commands in the shell yourself, line by line. 


--- type:FullSlide key:e21c5f871c
## Python Script

*** =part1
![](https://s3.amazonaws.com/assets.datacamp.com/production/course_4550/datasets/script_1.png)

*** =script
Let's put the command from before in a script now, that can be found here in DataCamp's interface. 



--- type:FullSlide key:2c98d562aa disable_transition:true
## Python Script

*** =part1
![](https://s3.amazonaws.com/assets.datacamp.com/production/course_4550/datasets/script_2.png)

*** =script
The next step is executing the script, by clicking 'Submit Answer'.



--- type:FullSlide key:b880a5b60c disable_transition:true
## Python Script

*** =part1
![](https://s3.amazonaws.com/assets.datacamp.com/production/course_4550/datasets/script_3.png)

*** =script
If you execute this script in the DataCamp interface, there's nothing in the output pane.. That's because you have to explicitly use print() inside scripts if you want to generate output during execution.


--- type:FullSlide key:f3c3cace98 disable_transition:true
## Python Script

*** =part1
![](https://s3.amazonaws.com/assets.datacamp.com/production/course_4550/datasets/script_4.png)

*** =script
Let's wrap our previous calculation a in print() call, and rerun the script.


--- type:FullSlide key:9d474a1460 disable_transition:true
## Python Script

*** =part1
![](https://s3.amazonaws.com/assets.datacamp.com/production/course_4550/datasets/script_5.png)

*** =script
 This time, the same output as before is generated, great!
 Putting your code in Python scripts instead of manually retyping every step interactively will help you to keep structure and avoid retyping everything over and over again if you want to make a change; you simply make the change in the script, and rerun the entire thing.
 


--- type:FullSlide key:ea764a1cb3
## DataCamp Interface

*** =part1
![](https://s3.amazonaws.com/assets.datacamp.com/production/course_4550/datasets/interface_1.png)

*** =script
Now that you've got an idea about different ways of working with Python, I suggest you head over to the exercises. Use the IPython Shell for experimentation, and use the Python sript editor to code the actual answer. If you click Submit Answer, your script will be executed and checked for correctness. Have fun!




--- type:FinalSlide key:a42f5abc6a
## Let's practice!


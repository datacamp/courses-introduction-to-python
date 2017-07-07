---
title: Variables & Types
key: 4a64ab063ba2e9c0bd83e35e9f6c4b24

video_link:
    hls: https://videos.datacamp.com/transcoded/735_intro_to_python/wb1/hls-ch1_2.master.m3u8
    mp4: https://videos.datacamp.com/transcoded_mp4/735_intro_to_python/wb1/ch1_2.mp4

transformations:
    translateX: 55
    translateY: 0
    scale: 0.8
--- type:TitleSlide key:5edd34113f
## Variables & Types


*** =lower_third
name: Filip Schouwenaars
title: Instructor, DataCamp

*** =script
It's clear that Python is a great calculator. If you want to do more complex calculations though, you will want to "save" values while you're coding along. 


--- type:FullSlide key:e45c9632c5
## Variables

*** =part1
- Specific, case-sensitive name {{1}}
- Call up value through variable name {{2}}
- 1.79 m - 68.7 kg {{3}}

```
In [1]: height = 1.79

In [2]: weight = 68.7
``` {{4}}
```
In [3]: height
Out[3]: 1.79
``` {{5}}

*** =script
Suppose you measure your height and weight, in metric units: you are 1 point 79 meters tall, and weigh 68.7 kilograms. You can assign these values to two variables, named height and weight, with an equals sign:

If you now type the name of the variable, height

Python looks for the variable name, retrieves its value, and prints it out.




--- type:FullSlide key:28908063ae
## Calculate BMI

*** =part1
$$BMI = \frac\{weight\}\{height^2\}$$ {{1}}
```
In [1]: height = 1.79

In [2]: weight = 68.7

In [3]: height
Out[3]: 1.79
```
```
In [4]: 68.7 / 1.79 ** 2
Out[4]: 21.4413
``` {{2}}
```
In [5]: weight / height ** 2
Out[5]: 21.4413
``` {{3}}
```
In [6]: bmi = weight / height ** 2

In [7]: bmi
Out[7]: 21.4413
``` {{4}}

*** =script
Let's now calculate the Body Mass Index, or BMI, which is calculated as follows, with weight in kilograms and height in meter. You can do this with the actual values but you can just as well use the variables height and weight, like in here. Every time you type the variable's name, you are asking Python to change it with the actual value of the variable. weight corresponds to 68.7, and height to 1.79.

Finally, this version has Python store the result in a new variable, bmi. bmi now contains the same value as the one you calculated earlier.




--- type:FullSlide key:40e4c0aa19
## Reproducibility

*** =part1
`Script.py`:
```
height = 1.79
weight = 68.7
bmi = weight / height ** 2
print(bmi)
```


`Output`:
```
21.4413
``` {{1}}

*** =script
In Python, variables are used all the time. They help to make your code reproducible. Suppose the code to create the height, weight and bmi variable are in a script, like this.


--- type:FullSlide key:d4d3467ce1 disable_transition:false
## Reproducibility

*** =part1
`Script.py`: {{1}}
```
height = 1.79
weight = 74.2
bmi = weight / height ** 2
print(bmi)
``` {{1}}
`Output`: {{2}}
```
23.1578
``` {{2}}

*** =script
If you now want to recalculate the bmi for another weight, you can simply change the declaration of the weight variable, and rerun the script. The bmi changes accordingly, because the value of the variable weight has changed.


--- type:FullSlide key:c53886c084
## Python Types

*** =part1

  ```
  In [8]: type(bmi)
  Out[8]: float
  ``` {{1}}
  ```
  In [9]: day_of_week = 5
  
  In [10]: type(day_of_week)
  Out[10]: int
  ``` {{2}}

*** =script
So far, we've only worked with numerical values, such as height and weight. In Python, these numbers all have a specific type. You can check out the type of a value with the type() function. To see the type of our bmi value, simply write type and then bmi inside parentheses. You can see that it's a float, which is python's way of representing a real number, so a number which can have both an integer part and a fractional part. Python als has a type for integers: int, like this example.
To do data science, you'll need more than ints and floats, though. 




--- type:FullSlide key:8942b3b299
## Python Types (2)

*** =part1

```
In [11]: x = "body mass index"

In [12]: y = 'this works too'
```{{1}}
```
In [13]: type(y)
Out[13]: str
```{{2}}
```
In [14]: z = True
```{{3}}
```
In [15]: type(z)
Out[15]: bool
``` {{4}}

*** =script
Python features tons of other data types. The most common ones are strings and booleans.

A string is Python's way to represent text. You can use both double and single quotes to build a string, as you can see from these examples. If you print the type of the last variable here, you see that it's str, short for string.

The Boolean is a type that can either be True or False. You can think of it as 'Yes' and 'No' in everyday language. Booleans will be very useful in the future, to perform filtering operations on your data for example.


--- type:FullSlide key:d2da70935f
## Python Types (3)

*** =part1
```
In [16]: 2 + 3
Out[16]: 5
``` {{1}}
```
In [17]: 'ab' + 'cd'
Out[17]: 'abcd'
``` {{2}}

*** =script
There's something special about Python data types. Have a look at this line of code, that sums two integers, and then this line of code, that sums two strings.

For the integers, the values were summed, while for the strings, the strings were pasted together. The plus operator behaved differently for different data types. This is a general principle: how the code behaves depends on the types you're working with.


--- type:FinalSlide key:341351efd6
## Let's practice!

*** =script
In the exercises that follow, you'll create your very first variables and experiment with some of Python's data types. I'll see you in the next video to explain all about lists.
---
title: Lists, what are they?
key: c3b2fa47d2eae2ae1bebf99a0d1ced98
video_link:
    hls: https://videos.datacamp.com/transcoded/735_intro_to_python/wb1/hls-ch2_1.master.m3u8
    mp4: https://videos.datacamp.com/transcoded_mp4/735_intro_to_python/wb1/ch2_1.mp4

transformations:
    translateX: 55
    translateY: 0
    scale: 0.8

--- type:TitleSlide key:3d4e1b442c
## Python Lists


*** =lower_third
name: Filip Schouwenaars
title: Instructor, DataCamp

*** =script
By now, you've played around with different data types.




--- type:FullSlide key:4835c5d7b1
## Python Data Types

*** =part1
- `float` - real numbers {{1}}
- `int` - integer numbers {{2}}
- `str` - string, text {{3}}
- `bool` - True, False {{4}}


```
In [1]: height = 1.73

In [2]: tall = True
``` {{5}}
- Each variable represents **single** value {{6}}

*** =script
On the numbers side, there's the float, to represent a real number, and the int, to represent an integer. Next, we also have str, short for string, to represent text in Python, and bool, which can be either True or False. You can save these values as a variable, like these examples show. Each variable then represents a single value.


--- type:FullSlide key:c7ff2e05ee
## Problem

*** =part1
- Data Science: many data points {{1}}
- Height of entire family {{2}}

```
In [3]: height1 = 1.73

In [4]: height2 = 1.68

In [5]: height3 = 1.71

In [6]: height4 = 1.89
``` {{3}}
- Inconvenient {{4}}

*** =script
As a data scientist, you'll often want to work with many data points. If you for example want to measure the height of everybody in your family, and store this information in python, it would be inconvenient to create a new python variable for each data point you collected right?




--- type:FullSlide key:af85553803
## Python List

*** =part1

```
In [7]: [1.73, 1.68, 1.71, 1.89]
Out[7]: [1.73, 1.68, 1.71, 1.89]
``` {{1}}
```
In [8]: fam = [1.73, 1.68, 1.71, 1.89]

In [9]: fam
Out[9]: [1.73, 1.68, 1.71, 1.89]
``` {{2}}

- Name a collection of values {{3}}
- Contain any type {{4}}
- Contain different types {{5}}

*** =script
What you can do instead, is store all this information in a python list. You can build such a list with square brackets. Suppose you asked your two sisters and parents for their height, in meters. You can build the list as follows:

Of course, also this data structure can be referenced to with a variable. Simply put the variable name and the equals sign in front, like here:

A list is a way to give a single name to a collection of values. These values, or elements, can have any type; they can be floats, integer, booleans, strings, but also more advanced Python types, even lists.

It's perfectly possible for a list to contain different types. Suppose, for example, that you want to add the names of your sisters and parents to the list, so that you know which height belongs to who. You can throw in some strings without issues.



--- type:FullSlide key:c60676f1b5 disable_transition:true
## Python List

*** =part1

```
In [10]: fam = ["liz", 1.73, "emma", 1.68, "mom", 1.71, "dad", 1.89]

In [11]: fam
Out[11]: ['liz', 1.73, 'emma', 1.68, 'mom', 1.71, 'dad', 1.89]
``` {{1}}

```
In [11]: fam2 = [["liz", 1.73],
                 ["emma", 1.68],
                 ["mom", 1.71],
                 ["dad", 1.89]]
``` {{2}}
```
In [12]: fam2
Out[12]: [['liz', 1.73], ['emma', 1.68], ['mom', 1.71], ['dad', 1.89]]
``` {{3}}


*** =script
It's perfectly possible for a list to contain different types. Suppose, for example, that you want to add the names of your sisters and parents to the list, so that you know which height belongs to who. You can throw in some strings without issues.

But that's not all. I just told you that lists can also contain lists themselves. Instead of putting the strings in between the numbers, you can create little sublists for each member of the family. One for liz, one for emma and so on. Now, you can tell Python that these sublists are the elements of another list, that I named fam2: the little lists are wrapped in square brackets and separated with commas. If you now print out fam2, you see that we have a list of lists. The main list contains 4 sub lists.


--- type:FullSlide key:f1b5a1306a
## List type

*** =part1
```
In [13]: type(fam)
Out[13]: list

In [14]: type(fam2)
Out[14]: list
``` {{1}}
- Specific functionality {{2}}
- Specific behavior {{2}}

*** =script
We're dealing with a new Python type here, next to the strings, booleans, integers and floats you already know about: the list. These calls show that both fam and fam2 are lists. Remember that I told you that each type has specific functionality and behavior associated? Well, for lists, this is also true. Python lists host a bunch of tools to subset and adapt them.




--- type:FinalSlide key:110e580a51
## Let's practice!

*** =script

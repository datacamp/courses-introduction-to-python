---
title: NumPy Basic Statistics
key: ba4a68cd9db130bf7850b0710684ade8
video_link:
    hls: https://videos.datacamp.com/transcoded/735_intro_to_python/wb1/hls-ch4_3.master.m3u8
    mp4: https://videos.datacamp.com/transcoded_mp4/735_intro_to_python/wb1/ch4_3.mp4

transformations:
    translateX: 55
    translateY: 0
    scale: 0.8

--- type:TitleSlide key:a607c26f0d
## NumPy: Basic Statistics

*** =lower_third
name: Filip Schouwenaars
title: Instructor, DataCamp

*** =script


--- type:FullSlide key:e10b8a7f55
## Data Analysis

*** =part1
- Get to know your data {{1}}
- Little data $\rightarrow$ simply look at it {{2}}
- Big data $\rightarrow$ ? {{3}}

*** =script
A typical first step in analyzing your data, is getting to know your data in the first place. For the Numpy arrays from before, this is pretty easy, because it isn't a lot of data. However, as a data scientist, you'll be crunching thousands, if not millions or billions of numbers.



--- type:FullSlide key:27538e89f0
## <<<New Slide>>>

*** =part1

*** =script


--- type:FullSlide key:4bc42d2011
## City-wide survey

*** =part1
```
In [1]: import numpy as np

# In [2]: np_city = ... # Implementation left out

In [3]: np_city
Out[3]:
array([[  1.64,  71.78],
       [  1.37,  63.35],
       [  1.6 ,  55.09],
       ...,
       [  2.04,  74.85],
       [  2.04,  68.72],
       [  2.01,  73.57]])
```{{1}}
*** =script
Imagine you conduct a city-wide survey where you ask 5000 adults about their height and weight. You end up with something like this: a 2D numpy array, which I named np_city, that has 5000 rows, corresponding to the 5000 people, and two columns, corresponding to the height and the weight.

Simply staring at these numbers like a zombie won't give you any insights. What you can do, though, is generating summarizing statistics about your data. Aside from an efficient data structure for number crunching, it happens that Numpy is also good at doing these kinds of things.

--- type:FullSlide key:0268db77ee
## NumPy

*** =part1
```
In [4]: np.mean(np_city[:,0])
Out[4]: 1.7472
```{{1}}
```
In [5]: np.median(np_city[:,0])
Out[5]: 1.75
```{{2}}
```
In [6]: np.corrcoef(np_city[:,0], np_city[:,1])
Out[6]:
array([[ 1.     , -0.01802],
       [-0.01803,  1.     ]])
```{{3}}
```
In [7]: np.std(np_city[:,0])
Out[7]: 0.1992
```{{4}}
- `sum()`, `sort()`, ... {{5}}
- Enforce single data type: speed! {{6}}

*** =script
For starters, you can try to find out the average height of these 5000 people, with Numpy's mean function. Because it's a function from the Numpy package, don't forget to start with "np dot".

Of course, I first had to do a subsetting operation to get the height column from the 2D array. It appears that on average, people are 1.75 meters tall. What about the median height? This is the height of the middle person if you sort all persons from small to tall. Instead of writing complicated python code to figure this out, you can simply use Numpy's median() function:

You can do similar things for the weight column in np_city. Often, these summarizing statistics will provide you with a "sanity check" of the data. If you end up with a average weight of 2000 kilograms, you're measurements are most likely incorrect.

Apart from mean() and median(), there's also other functions, like corrcoeff() to check if for example height and weight are correlated,

and std(), for standard deviation.

Numpy also features more basic functions, such as sum() and sort(), which also exist in the basic Python distribution. However, the big difference here is speed. Because Numpy enforces a single data type in an array, it can drastically speed up the calculations.


--- type:FullSlide key:a294bd6c73
## Generate data

*** =part1
```
#                                         mean  std dev  n samples
In [8]: height = np.round(np.random.normal(1.75,  0.20,    5000),   2)

In [9]: weight = np.round(np.random.normal(60.32, 15, 5000), 2)
```{{1}}
```
In [10]: np_city = np.column_stack((height, weight))
```{{2}}

*** =script
Just a sidenote here: If you're wondering how I came up with the data in this video: I simulated it with Numpy functions! I sampled two random distributions 5000 times to create the height and weight arrays, and then used column_stack to paste them together as two columns. Another thing that Numpy can do!

--- type:FinalSlide key:f62e244b69
## Let's practice!

*** =script
Another great tool to get some sense of your data is to visualize it, but that's something for later. First, head over to the exercises to learn how to explore your Numpy arrays!



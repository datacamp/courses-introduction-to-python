---
title: NumPy
key: f1578ad8cecfa295a876ebc3ddf60cbf
video_link:
    hls: https://videos.datacamp.com/transcoded/735_intro_to_python/wb1/hls-ch4_1.master.m3u8
    mp4: https://videos.datacamp.com/transcoded_mp4/735_intro_to_python/wb1/ch4_1.mp4

transformations:
    translateX: 55
    translateY: 0
    scale: 0.8

--- type:TitleSlide key:b4b3a47316
## NumPy


*** =lower_third
name: Filip Schouwenaars
title: Instructor, DataCamp

*** =script



--- type:FullSlide key:75599dbe56
## Lists recap

*** =part1
- Powerful {{1}}
- Collection of values {{2}}
- Hold different types {{3}}
- Change, add, remove {{4}}
- Need for Data Science {{5}}
    - Mathematical operations over collections {{6}}
    - Speed {{7}}

*** =script
By now, you are aware that the Python list is pretty powerful: A list can hold any type and can hold different types at the same time. You can also change, add and remove elements. This is wonderful, but one feature is missing, a feature that is super important for aspiring data scientists as yourself. When analyzing data, you'll often want to carry out operations over entire collections of values, and you want to do this fast. With lists, this is a problem.



--- type:FullSlide key:d2594119de
## Illustration

*** =part1
```
In [1]: height = [1.73, 1.68, 1.71, 1.89, 1.79]

In [2]: height
Out[2]: [1.73, 1.68, 1.71, 1.89, 1.79]
``` {{1}}
```
In [3]: weight = [65.4, 59.2, 63.6, 88.4, 68.7]

In [4]: weight
Out[4]: [65.4, 59.2, 63.6, 88.4, 68.7]
``` {{2}}
```
In [5]: weight / height ** 2
# TypeError: unsupported operand type(s) for **: 'list' and 'int'
``` {{3}}

*** =script
Let's retake the heights of your family and yourself. Suppose you've also asked for everybody's weight. It's not very polite, but everything for science, right? You end up with two lists, height, and weight. The first person is 1.73 meters tall and weighs 65.4 kilograms.

If you now want to calculate the Body Mass Index for each family member, you'd hope that this call can work, making the calculations element-wise.

Unfortunately, Python throws an error, because it has no idea how to do calculations with lists. You could solve this by going through each list element one after the other, and calculating the BMI for each person separately, but this is terribly inefficient and tiresome to write.



--- type:FullSlide key:6525b2888c
## Solution: NumPy

*** =part1
- Numeric Python {{1}}
- Alternative to Python List: NumPy Array {{2}}
- Calculations over entire arrays {{3}}
- Easy and Fast {{4}}
- Installation {{5}}
    - In the terminal: `pip3 install numpy` {{5}}

*** =script
A way more elegant solution is to use NumPy, or Numeric Python. It's a Python package that, among others, provides a alternative to the regular python list: the Numpy array. The Numpy array is pretty similar to a regular Python list, but has one additional feature: you can perform calculations over all entire arrays. It's really easy, and super-fast as well.

The Numpy package is already installed on DataCamp's servers, but if you want to work with it on your own system, go to the command line and execute pip3 install numpy.



--- type:FullSlide key:5564f54155
## NumPy

*** =part1
```
In [6]: import numpy as np
```{{1}}
```
In [7]: np_height = np.array(height)

In [8]: np_height
Out[8]: array([ 1.73,  1.68,  1.71,  1.89,  1.79])

In [9]: np_weight = np.array(weight)

In [10]: np_weight
Out[10]: array([ 65.4,  59.2,  63.6,  88.4,  68.7])
```{{2}}
```
In [11]: bmi = np_weight / np_height ** 2

In [12]: bmi
Out[12]: array([ 21.852,  20.975,  21.75 ,  24.747,  21.441])
```{{3}}

*** =script
Next, to actually use Numpy in your Python session, you can import the numpy package in your session, like this.

Let's start with creating a numpy array. You do this with Numpy's array() function: the input is a regular Python list. I'm using array() twice here, to create Numpy versions of the height and weight lists from before: np_height and np_weight:

Let's try to calculate everybody's BMI with a single call again:

This time, it worked fine: the calculations were performed element-wise. The first person's BMI was calculated by dividing the first element in np_weight by the square of the first element in np_height, the second person's BMI was calculated with the second height and weight elements, and so on.



--- type:FullSlide key:52784e5b80
## Comparison

*** =part1
```
In [13]: height = [1.73, 1.68, 1.71, 1.89, 1.79]

In [14]: weight = [65.4, 59.2, 63.6, 88.4, 68.7]

In [15]: weight / height ** 2
# TypeError: unsupported operand type(s) for **: 'list' and 'int'
``` {{1}}

```
In [16]: np_height = np.array(height)

In [17]: np_weight = np.array(weight)

In [18]: np_weight / np_height ** 2
Out[18]: array([ 21.852,  20.975,  21.75 ,  24.747,  21.441])
``` {{2}}

*** =script
Let's do a quick comparison here. First, we tried to do calculations with regular lists, like this, but this gave us an error, because Python doesn't now how to do calculations with lists like we want them to. Next, these regular lists where converted to Numpy arrays. The same operations now work without any problem: Numpy knows how to work with arrays as if they are single values, which is pretty awesome if you ask me.



--- type:FullSlide key:55099298e3
## NumPy: remarks

*** =part1
NumPy `arrays`: contain only one type {{2}}
```
In [19]: np.array([1.0, "is", True])
Out[19]: array(['1.0', 'is', 'True'],
               dtype='<U32')
```{{1}}

Different types: different behavior! {{6}}
```
In [20]: python_list = [1, 2, 3]

In [21]: numpy_array = np.array([1, 2, 3])
```{{3}}
```
In [22]: python_list + python_list
Out[22]: [1, 2, 3, 1, 2, 3]
```{{4}}
```
In [23]: numpy_array + numpy_array
Out[23]: array([2, 4, 6])
```{{5}}

*** =script
You should still pay attention, though. First of all, Numpy can do all of this so easily because it assumes that your Numpy array can only contain values of a single type. It's either an array of floats, either an array of booleans, and so on. If you do try to create an array with different types, like this for example, The resulting Numpy array will contain a single type, string in this case. The boolean and the float were both converted to strings.

Second, you should know that a Numpy array is simply a new kind of Python type, like the float, string and list types from before. This means that it comes with its own methods, which can behave differently than you'd expect. Take this Python list and this numpy array, for example:

If you do python_list + python_list, the list elements are pasted together, generating a list with 6 elements. If you do this with the numpy arrays, on the other hand, Python will do an element-wise sum of the array:

Just make sure to pay attention when you're juggling around with different Python types, because the outcome can differ a lot!


--- type:FullSlide key:9bf1bd1893
## NumPy subsetting

*** =part1
```
In [24]: bmi
Out[24]: array([ 21.852,  20.975,  21.75 ,  24.747,  21.441])
``` {{1}}
```
In [25]: bmi[1]
Out[25]: 20.975
``` {{2}}
```
In [26]: bmi > 23
Out[26]: array([False, False, False,  True, False], dtype=bool)
``` {{3}}
```
In [27]: bmi[bmi > 23]
Out[27]: array([24.747])
``` {{4}}
*** =script
Apart from these subtleties, you can work with Numpy arrays pretty much the same as you can with regular Python lists. When you want to get elements from your array, for example, you can again use square brackets. Suppose you want to get the bmi for the second person, so at index 1. This will od the trick:

Specifically for Numpy, there's also another way to do list subsetting: using an array of booleans. Say you want to get all BMI values in the bmi array that are over 23. A first step is using the greater than sign, like this:

The result is a Numpy array containing booleans: True if the corresponding bmi is above 23, False if it's below. Next, you can use this boolean array inside square brackets to do subsetting. Only the elements in bmi that are above 23, so for which the corresponding boolean value is True, is selected. There's only one BMI that's above 23, so we end up with a Numpy array with a single value, that BMI.

Using the result of a comparison to make a selection of your data is a very common way to get surprising insights. 



--- type:FinalSlide key:2723575524
## Let's practice!

*** =script

Learn all about it and the other Numpy basics in the exercises!
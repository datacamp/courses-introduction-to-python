---
title: 2D NumPy Arrays
key: df344e94ca54940c02e7ee03db39499c
video_link:
    hls: https://videos.datacamp.com/transcoded/735_intro_to_python/wb1/hls-ch4_2.master.m3u8
    mp4: https://videos.datacamp.com/transcoded_mp4/735_intro_to_python/wb1/ch4_2.mp4

transformations:
    translateX: 55
    translateY: 0
    scale: 0.8

--- type:TitleSlide key:3c37c966a4
## 2D NumPy Arrays

*** =lower_third
name: Filip Schouwenaars
title: Instructor, DataCamp

*** =script


--- type:FullSlide key:2662457d8b
## Type of NumPy Arrays

*** =part1
```
In [1]: import numpy as np

In [2]: np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])

In [3]: np_weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])
```{{1}}
```
In [4]: type(np_height)
Out[4]: numpy.ndarray

In [5]: type(np_weight)
Out[5]: numpy.ndarray
```{{2}}

`ndarray` = N-dimensional array {{3}}

*** =script
Let's recreate the numpy arrays from the previous video:

If you ask for the type of these arrays, , Python tells you that they are numpy dot ndarray. numpy dot tells you it's a type that was defined in the numpy package. ndarray stands for n-dimensional array. The arrays np_height and np_weight are one-dimensional arrays, but it's perfectly possible to create 2 dimensional, three dimensional, heck even seven dimensional arrays! Let's stick to 2 in this video though.

--- type:FullSlide key:888b03888d
## 2D NumPy Arrays

*** =part1
```
In [6]: np_2d = np.array([[1.73, 1.68, 1.71, 1.89, 1.79],
                          [65.4, 59.2, 63.6, 88.4, 68.7]])
``` {{1}}
```
In [7]: np_2d
Out[7]:
array([[  1.73,   1.68,   1.71,   1.89,   1.79],
       [ 65.4 ,  59.2 ,  63.6 ,  88.4 ,  68.7 ]])
```{{2}}
```
In [8]: np_2d.shape
Out[8]: (2, 5)    # 2 rows, 5 columns
```{{3}}
```
In [9]: np.array([[1.73, 1.68, 1.71, 1.89, 1.79],
                  [65.4, 59.2, 63.6, 88.4, "68.7"]])
Out[9]:
array([['1.73', '1.68', '1.71', '1.89', '1.79'],
       ['65.4', '59.2', '63.6', '88.4', '68.7']],     # single type!
      dtype='<U32')
```{{4}}


*** =script
You can create a 2D numpy array from a regular Python list of lists. Let's try to create one numpy array for all height and weight data of your family, like this:

If you print out np_2d now, you'll see that it is a rectangular data structure: Each sublist in the list, corresponds to a row in the two dimensional numpy array. From np_2d.shape, you can see that we indeed have 2 rows and 5 columns. shape is a so-called attribute of the np2d array, that can give you more information about what the data structure looks like.

Also for 2D arrays, the Numpy rule applies: an array can only contain a single type. If you change one float to be string, all the array elements will be coerced to strings, to end up with a homogenous array.

You can think of the 2D numpy array as an improved list of lists: you can perform calculations on the arrays, like I showed before, and you can do more advanced ways of subsetting.

--- type:FullSlide key:4cc1b78209
## Subsetting

*** =part1
```
#           1       2       3       4       5
array([[  1.73,   1.68,   1.71,   1.89,   1.79],   # 1
       [  65.4,   59.2,   63.6,   88.4,   68.7]])  # 2
```

```
In [10]: np_2d[0]
Out[10]: array([ 1.73,  1.68,  1.71,  1.89,  1.79])
```{{1}}
```
In [11]: np_2d[0][2]
Out[11]: 1.71
```{{2}}
```
In [12]: np_2d[0,2]
Out[12]: 1.71
```{{3}}
```
In [13]: np_2d[:,1:3]
Out[13]: array([[  1.68,   1.71],
                [ 59.2 ,  63.6 ]])
```{{4}}
```
In [14]: np_2d[1,:]
Out[14]: array([ 65.4,  59.2,  63.6,  88.4,  68.7])
``` {{5}}

*** =script
Suppose you want the first row, and then the third element in that row. To select the row, you need the index 0 in square brackets.

To then select the third element, you can extend the same call with another pair of brackets, this time with the index 2, like this. Basically you're selecting the row, and then from that row do another selection.

There's also an alternative way of subsetting, using single square brackets and a comma. This call returns the exact same value as before. The value before the comma specifies the row, the value after the comma specifies the column. The intersection of the rows and columns you specified, are returned.
Once you get used to it, this syntax is more intuitive and opens up more possibilities. Suppose you want to select the height and weight of the second and third family member. You want both rows, so you put in a colon before the comma. You only want the second and third column, so you put in the indices 1 to 3 after the comma. Remember that the third index is not included here. The intersection gives us a 2D array with 2 rows and 2 columns:

Similarly, you can select the weight of all family members like this: you only want the second row, so put 1 before the comma. You want all columns, so you use a colon after the comma. The intersection gives us the entire second row.

Finally, 2D numpy arrays enable you to do element-wise calculations, the same way you did it with 1D numpy arrays.
--- type:FinalSlide key:0e391747e6
## Let's practice!

*** =script

 That's something you can experiment with in the exercises, along with creating and subsetting 2D numpy arrays! Exciting...
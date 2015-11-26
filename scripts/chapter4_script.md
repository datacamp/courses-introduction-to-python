## Intro to Numpy

By now, you are aware that the Python list is pretty powerful: A list can hold any type and can hold different types at the same time. You can also change, add and remove elements. This is wonderful, but one feature is missing, a feature that is super important for aspiring data scientists as yourself. When analyzing data, you'll often want to carry out mathematical operations over entire collections of values, and you want to do this fast. With lists, this is a problem.

To show this, let's retake the heights of your family and yourself. In addition, suppose you've also asked for everybody's weight. It's not very polite, but everything for science, right? You end up with two lists, `fam_height`, and `fam_weight`. The first person is 1.78 meters tall and weighs 75 kilograms.

To calculate the Body Mass Index for each family member in a single call this time, you might want to try something like this.

Python throws an error, because it has no idea how to do calculations with lists. You could solve this by going through each list element one after the other, and calculating the BMI for each person separately, but this is terribly inefficient and tiresome to write.

A way more elegant solution is to use NumPy, or Numeric Python. It's a Python package that, among others, provides a alternative to the regular python list, the numpy array. Where the Python list is simply a compound data type to store python values, you can think of the numpy array more of an actual vector, in the mathematical sense. It becomes easy to perform calculations on entire datasets, and it's pretty fast as well. To start using numpy, you first have to install the package. We already did that in the previous video, by executing `pip3 install numpy` in the command line.

To actually start using it in python, you can import the numpy package in your session, like this.

The first step is of course creating a numpy array. You do this with Numpy's `array()` function: the input is a regular Python list. Let's create Numpy version of the `fam_height` and `fam_weight` lists from before: `np_height` and `np_weight`:

Let's now try to calculate everybody's BMI with a single call:

This time, it worked fine: the calculations were performed element wise. The first person's BMI was calculated by dividing the first element in `np_weight` by the square of the first element in `np_height`, the second person's BMI was calculated with the second height and weight elements, and so on. A next step could be to find out whose BMI is over 23. You can do this with the greater than sign:

This time, the result is a Numpy array containing booleans: True if the corresponding bmi is above 23, False if it's below. You can do all of this with remarkable ease: Numpy knows how to work with vectors just how Python works with single values, which is pretty awesome if you ask me.

Of course, you should pay attention. First of all, Numpy can do all of this easily and quickly because it assumes that your Numpy array can only contain values of a single type. It's either an array of booleans, either an array of floats, and so on. If you do try to create an array with different types, like this for example;

The Numpy array that results will contain a single type, string in this case. The boolean and the float were both converted, or coerced, as this is called, to strings.

Second, you should know that a Numpy array is simply a new kind of Python type, like the float, string and list types from before. This means that it comes with its own methods, which can behave differently than you'd expect. Take this Python list and this numpy array, for example:

If you do `python_list + python_list`, the list elements are pasted together, generating a list with 6 elements. If you do this with the numpy arrays, on the other hand, Python will do an element-wise sum of the array:

Make sure to pay attention when you're juggling around with different Python types, because the outcome can differ a lot! Now head over to the exercises, to get your own numpy arrays rolling.


```
fam_height = [1.73, 1.68, 1.71, 1.89, 1.79]
fam_height
fam_weight = [65.4, 59.2, 63.6, 88.4, 68.7]
fam_weight
fam_weight / fam_height ** 2

import numpy as np
np_height = np.array(fam_height)
np_height
np_weight = np.array(fam_weight)
np_weight
bmi = np_weight / np_height ** 2
bmi
bmi > 23

np.array([1.0, "is", True])
python_list = [1, 2, 3]
numpy_array = np.array([1, 2, 3])
python_list + python_list
numpy_array + numpy_array
```

## 2D Numpy arrays

Let's recreate the numpy arrays from the previous video:

If you ask for the type of these arrays, <PAUSE>, Python tells you that they are `numpy` dot `ndarray`. `numpy` dot tells you it's a type that was defined in the numpy package. `ndarray` stands for n-dimensional array. The arrays `np_height` and `np_weight` are one-dimensional arrays, but it's perfectly possible to create 2 dimensional, three dimensional, heck even seven dimensional arrays! Let's stick to 2 in this video though.

You can create a 2D numpy array from a regular Python list of lists. Let's try to create one numpy array for all height and weight data of your family, like this:

If you print out `np_2d` now, you'll see that it is a rectangular data structure: Each sublist in the list, corresponds to a row in the two dimensional numpy array. From `np_2d.shape`, you can see that we indeed have 2 rows and 5 columns. Shape is a so-called attribute of the ndarray `np2d` here. 

Also for 2D arrays, the Numpy rule applies: an array can only contain a single type. If you change one float to be numeric, all the array elements will be coerced to characters, to end up with a homogenous array.

You can think of the 2D numpy array as an improved list of lists: you can perform calculations on the arrays, like I showed before, and you can do more advanced ways of subsetting.

Suppose you want the first row, and then the third element in that row. To select the row, you need index 0 in square brackets. To then select the third element, you put 2 in square brackets, like this:

There's also an alternative way of subsetting, using single square brackets and a comma. This call returns the exact same value as before:

This syntax opens much more possibilities though: you can create both row-wise and column-wise subsets. This call, for example, selects the first row of the 2d array:

The colon tells Python to include a slice going from beginning to end, remember? So you're telling Python to take the first row, and then all columns. Just the same, you can do this for columns too. This call selects the entire column with index 2, so the height and weight of the third family member:

Finally, 2D numpy arrays enable you to do element-wise calculations, the same way you did it with 1D numpy arrays. That's something you can experiment with in the exercises, along with creating and subsetting 2D numpy arrays! Exciting...

```
import numpy as np
np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
np_weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])
type(np_height)
type(np_weight)
np_2d = np.array([[1.73, 1.68, 1.71, 1.89, 1.79],
                  [65.4, 59.2, 63.6, 88.4, 68.7]])
np_2d
np_2d.shape
np.array([[1.73, 1.68, 1.71, 1.89, 1.79],
          [65.4, 59.2, 63.6, 88.4, "68.7"]])
          
np_2d[0][2]
np_2d[0,2]
np_2d[0,:]
np_2d[:,2]
```

## Basic Statistics with Numpy

A typical first step in analyzing your data, is getting to know your data in the first place. For the Numpy arrays from before, this is pretty easy, because it isn't a lot of data. However, as a data scientist, you'll be crunching thousands, if not millions or billions of numbers.

Imagine you conduct a city-wide survey where you ask 5000 adults about their height and weight. You end up with something like this: a 2D numpy array, which I named `np_city`, that has 5000 rows, corresponding to the 5000 people, and two columns, corresponding to the height and the weight.

Simply staring at these numbers like a zombie won't give you any insights. What you _can_ do, though, is generating summarizing statistics about your data. Aside from an efficient data structure for number crunching, it happens that Numpy is also good at doing these kinds of things. 

For starters, you can try to find out the average height of these 5000 people, with Numpy's mean function. Because it's a function from the Numpy package, don't forget to start with "np dot".

Of course, I first had to do a subsetting operation to get the height column from the matrix. It appears that on average, people are 1.75 meters tall. What about the median height? This is the height of the middle person if you sort all persons from small to tall. Instead of writing complicated python code to figure this out, you can simply use Numpy's `median()` function:

You can do similar things for the weight column in `np_city`. Often, these summarizing statistics will provide you with a "sanity check" of the data. If you end up with a average weight of 2000 kilograms, you're measurements are most likely incorrect.

Apart from `mean()` and `median()`, there's also other functions, like `correlate()` to check if for example height and weight are correlated,

and `std()`, for standard deviation. 

Numpy also features more basic functions, such as `sum()` and `sort()`, which also exist in the basic Python distribution. However, the big difference here is speed. Because Numpy enforces a single data type in an array, it can use optimized C code behind the scenes, making your analysis superfast. 

By the way, the data we started with, `np_city`, was simulated using numpy function as well: I created 5000 samples of a random distribution to create the `heights` and `weights` arrays, and then used `column_stack` to paste them together as two columns. Another thing that Numpy can do!

Another great tool to get some sense of your data is to visualize it, but that's something for later. First, head over to the exercises to learn how to explore your Numpy arrays!

```
import numpy as np
np_city = np.column_stack((np.random.normal(1.75, 0.20, 5000), np.random.normal(60.32, 15, 5000)))
np_city
np.mean(np_city[:,0])
np.median(np_city[:,0])
np.correlate(np_city[:,0], np_city[:,1])
np.std(np_city[:,0])

heights = np.round(np.random.normal(1.75, 0.20, 5000), 2)
weights = np.round(np.random.normal(60.32, 15, 5000), 2)
np_city = np.column_stack((heights, weights))
```
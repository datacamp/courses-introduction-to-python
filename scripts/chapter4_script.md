## Introduction to Numpy

By now, you are aware that the Python list is pretty powerful: A list can hold any type and can hold different types at the same time. You can also change, add and remove elements. This is wonderful, but one feature is missing, a feature that is super important for aspiring data scientists as yourself. The thing is, when analyzing data, you'll often want to carry out mathematical operations over entire arrays of values, and you want to do this fast. 

To show this, let's retake the heights of your family and yourself. In addition, suppose you've also asked for everybody's weight. It's not very polite, but everything for science, right? You end up with two lists, `fam_height`, and `fam_weight`. The first person is 1.78 meters tall and weighs 75 kilograms.

```
fam_height = [1.73, 1.68, 1.71, 1.89, 1.79]
fam_weight = [65.4, 59.2, 63.6, 88.4, 68.7]
```

To calculate the Body Mass Index for each family member in a single call this time, you might want to try something like this.

```
fam_height / fam_weight ** 2
```

Python throws an error, because it has no idea how to do calculations with lists. You could solve this by going through each list element one after the other, and calculating the BMI for each person separately, but this sounds terribly inefficient to be.

A way more elegant solution is to use NumPy, or Numeric Python. It's a Python package that provides a alternative to the regular python list, the numpy array. Where the Python list is simply a compound data type to store python values, you can think of the numpy array more of an actual vector, in the mathematical sense. It becomes easy to perform calculations on entire datasets, and it's pretty fast as well.

To start using numpy, you first have to install the package, and then import it:

```
pip install numpy ## CHECK WITH VINCENT
import numpy as np
```

The first step is of course creating a numpy array. You do this with Numpy's `array()` function: the input is a regular Python list. Let's create Numpy version of the `fam_height` and `fam_weight` lists from before: `np_height` and `np_weight`:

```
np_height = np.array(fam_height)
np_weight = np.array(fam_weight)
```

Let's now try to calculate everybody's BMI with a single call:

```
np_weight / np_height ** 2
```

This time, it worked fine: the calculations were performed element wise. The first person's BMI was calculated by dividing the first element in `np_weight` by the square of the first element in `np_height`, the second person's BMI was calculated with the second height and weight elements, and so on. A next step could be to found out whose BMI is over 23. You can do this with the greater than sign:

```
bmi = np_weight / np_height ** 2
bmi > 23
```

This time, the result is a Numpy array containing booleans: True if the corresponding bmi is above 25, False if it's below. You can do all of this with remarkable ease: Numpy knows how to work with vectors just how Python works with single values, which is pretty awesome if you ask me.

Of course, you should pay attention. First of all, Numpy can do all of this easily and quickly because it assumes that your Numpy array can only contain values of a single type. It's either an array of booleans, either an array of floats, and so on. If you do try to create an array with different types, like this for example;

```
np.array([1.0, "is", True])
```

The Numpy array that results will contain a single type, string in this case. The boolean and the float were both converted, or coerced, as this is called, to strings.

Second, you should know that a Numpy array is simply a new kind of Python type, like the float, string and list types from before. This means that it has comes with its own methods, which can behave differently that you'd expect. Take this Python list and this numpy array, for example:

```
python_list = [1, 2, 3]
numpy_array = np.array([1, 2, 3])
```

If you do `python_list + python_list`, the list elements are pasted together, generating a list with 6 elements. If you do this with the numpy arrays, on the other hand, Python will do an element-wise sum of the array:

```
python_list + python_list
numpy_array + numpy_array
```

Make sure to pay attention when you're working juggling around with different Python types, because the outcome can differ a lot! Now head over to the exercises, to get your own numpy arrays rolling.

## Numpy and 2D arrays

Let's have another look at the python lists we've created in the previous video:

```
np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
np_weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])
```

If you ask for the type of these lists,

```
type(np_height)
type(np_weight)
```

Python tells you that they are `numpy` dot `ndarray`. `numpy` dot tells you that the type comes from the numpy package. `ndarray` stands for n-dimensional array. The arrays `np_height` and `np_weights` are one-dimensional arrays, but it's perfectly possible to create 2 dimensional, three dimensional, heck even seven dimensional arrays! Let's stick to 2 though.

You can create a 2D numpy array from a regular Python list of lists. Let's try to create one numpy array for all height and weight data of your family, like this:

```
np_hw = np.array([[1.73, 1.68, 1.71, 1.89, 1.79],
                  [65.4, 59.2, 63.6, 88.4, 68.7]])
```

If you print out `np_hw` now, you'll see that it is a rectangular data structure: Each sublist in the list, corresponds to a row in the two dimensional numpy array.

```
np_hw
```

shape is a so-called attribute of the ndarray. Also here, the same Numpy rule applies: an array can contain a single type. If you change one float to be numeric, all the array elements will be coerced to characters, to end up with a homogenous array:

```
np.array([[1.73, 1.68, 1.71, 1.89, 1.79],
          [65.4, 59.2, 63.6, 88.4, "68.7"]])
```

You can think of the 2D numpy array as an improved list of lists: you can subset it as a regular list of lists, but you can also do more advanced subsetting and perform calculations directly on the arrays. 

Suppose you want the first row, and then the third element in that row. To select the row, you need index 0 in square brackets. To then select the third element, you put 2 in square brackets, like this:

```
np_hw[0][2]
```

There's also an alternative way of subsetting, using single square brackets and a comma. This call returns the exact same value as before:

```
np_hw[0,2]
```

This syntax opens much more possibilities though: you can create both row-wise and column-wise subsets. This call, for example, selects the first row of the 2d array:

```
np_hw[0,:]
```

The colon tells Python to include a slice going from beginning to end, remember? Here, you're telling Python to take the first row, and then all columns. Just the same, you can do this for columns too. This call selects the entire column with index 2, so the height and weight of the third family member:

```
np_hw[:,2]
```

Finally, 2D numpy arrays enable you to element-wise calculations, the same way you did it with 1D numpy arrays. That's something you can experiment out in the exercises, along with creating and subsetting 2D numpy arrays! Exciting, isn't it?!


## Basic Statistics with Numpy

If Numpy was only about efficient data structures in Python 


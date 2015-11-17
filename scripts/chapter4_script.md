## Introduction to Numpy

By now, you've had quite some hands-on experience with Python lists. They're pretty versatile data structures: you can store any Python type in a list, you can store different types, you can change, add and remove elemnts from lists, and what not. This is wonderful, but there's one thing missing that's especially for an aspiring data scientist as yourself. When analyzing data, you'll often want to carry out mathematical operations over entire arrays of values, and you want to do this fast. As an example, suppose you have two lists, with the heights and weights of all the people living in your neighborhood, in meters and kilograms respectively. The lists contain 314 values each. The first person is 1.78 meters tall and weighs 75 kilograms, for example.

```
heights = [1.78, 1.54, 1.63, 1.86]
weights = [75, 57, 68, 86]
```

Remember how we calculated the BMI for a single person? We simply used this formula:

```
insert formula
```

What if you want to calculate the BMI with the variables `heights` and `weights` this time?

```
weights / heights ** 2
```

Python throws an error, because it has no idea how to divide two lists. You can solve this by going through each list element one after the other, and calculating the BMI for each person separately, but this seems like a terribly inefficient way to do this.

A way more elegant solution is to use NumPy. It's a Python package that provides a 'better version' of the list, the numpy array. Where the Python list is simply a compound data type to store python values, you can think of the numpy array as an actual vector in the mathematical sense. It becomes easy to perform calculations on entire datasets, and it's pretty fast as well.

To start using numpy, you first have to install the package, and then import it:

```
Add commands here
```

The first step is creating a `python` array. You do this with the `array()` function: the input is a regular Python list. Let's create Numpy version of the `heights` and `weights` lists from before: `np_heights` and `np_weights`:

```
np_heights = np.array(heights)
np_weights = np.array(weights)
```

Let's now try to calculate the BMI of all people with a single call:

```
np_weights / np_heights ** 2
```

This time, it worked fine: the calculations were performed element wise. The first person's BMI was calculated by dividing the first element in `np_weights` by the square of the first element in `np_heights`, the second person's BMI was calculated with the second height and weight elements, and so on. A next step could be to found out whose BMI is over 25. You can do this with the greater than sign:

```
bmi = np_weights / np_heights ** 2
bmi > 25
```

We get a Numpy array containing booleans: True if the corresponding bmi is above 25, False if it's below. You can do all of this with remarkable easy: Numpy nows how to work with vectors just how Python can work with single values, which is pretty awesome if you ask me.

You can think of a Numpy array as a juiced up version of python list, but not all functionality that you have in lists is availabe in Python lists. Take this Python list and this numpy array, for example:

```
python_list = [1, 2, 3]
numpy_array = np.array([1, 2, 3])
```

If you do `python_list + python_list`, the list elements are pasted together, generating a list with 6 elements. If you do this with the numpy arrays, on the other hand, Python will do an element-wise sum of the array:

```
python_list + python_list
numpy_array + numpy_array
```

That's once again because a Numpy array is a new kind of Python type, that has its own methods and implementations associated. Using the plus operator on strings, lists, numpy arrays, all behave differently!

Now head over to the exercises, to get your own numpy arrays rolling and learn more about how to work them.

## Numpy and 2D arrays


## Basic Statistics with Numpy

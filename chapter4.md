---
title_meta  : Chapter 4
title       : NumPy
description : NumPy is a Python package to efficiently do data science. Learn to work with the NumPy array, a faster and more powerful alternative to the list, and take your first steps in data exploration.
attachments :
  slides_link : https://s3.amazonaws.com/assets.datacamp.com/production/course_4527/slides/ch4_slides.pdf

---
## NumPy

```yaml
type: VideoExercise
lang: python
xp: 50
skills: 2
key: ed471f4b00
```

`@video_link`
//player.vimeo.com/video/154563364

`@video_hls`
//videos.datacamp.com/transcoded/735_intro_to_python/v3/hls-ch4_1.master.m3u8

*** =projector_key
cbf80c2cf12e5a3b971598e252e9cb9d

---
## Your First NumPy Array

```yaml
type: NormalExercise
lang: python
xp: 100
skills: 2
key: 84cab9d170
```

In this chapter, we're going to dive into the world of baseball. Along the way, you'll get comfortable with the basics of `numpy`, a powerful package to do data science.

A list `baseball` has already been defined in the Python script, representing the height of some baseball players in centimeters. Can you add some code here and there to create a `numpy` array from it?

`@instructions`
- Import the `numpy` package as `np`, so that you can refer to `numpy` with `np`.
- Use [`np.array()`](http://docs.scipy.org/doc/numpy-1.10.0/glossary.html#term-array) to create a `numpy` array from `baseball`. Name this array `np_baseball`.
- Print out the type of `np_baseball` to check that you got it right.

`@hint`
- `import numpy as np` will do the trick. Now, you have to use `np.fun_name()` whenever you want to use a `numpy` function.
- [`np.array()`](http://docs.scipy.org/doc/numpy-1.10.0/glossary.html#term-array) should take on input `baseball`. Assign the result of the function call to `np_baseball`.
- To print out the type of a variable `x`, simply type `print(type(x))`.

`@pre_exercise_code`
```{python}
import numpy as np
```

`@sample_code`
```{python}
# Create list baseball
baseball = [180, 215, 210, 210, 188, 176, 209, 200]

# Import the numpy package as np


# Create a numpy array from baseball: np_baseball


# Print out type of np_baseball

```

`@solution`
```{python}
# Create list baseball
baseball = [180, 215, 210, 210, 188, 176, 209, 200]

# Import the numpy package as np
import numpy as np

# Create a Numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out type of np_baseball
print(type(np_baseball))
```

`@sct`
```{python}
msg = "You don't have to change or remove the predefined variables."
test_object("baseball", undefined_msg = msg, incorrect_msg = msg)

test_import("numpy")

test_object("np_baseball", do_eval = False)
test_function("numpy.array", not_called_msg = "Be sure to call [`np.array()`](http://docs.scipy.org/doc/numpy-1.10.0/glossary.html#term-array).",
                             incorrect_msg = "You should call [`np.array()`](http://docs.scipy.org/doc/numpy-1.10.0/glossary.html#term-array) as follows: `np.array(baseball)`.")
test_object("np_baseball", incorrect_msg = "Assign the correct value to `np_baseball`.")

msg = "Make sure to print out the type of `np_baseball` like this: `print(type(np_baseball))`."
test_function("type", 1, incorrect_msg = msg)
test_function("print", 1, incorrect_msg = msg)

success_msg("Great job!")
```

---
## Baseball players' height

```yaml
type: NormalExercise
lang: python
xp: 100
skills: 2
key: e7e25a89ea
```

You are a huge baseball fan. You decide to call the MLB (Major League Baseball) and ask around for some more statistics on the height of the main players. They pass along data on more than a thousand players, which is stored as a regular Python list: `height`. The height is expressed in inches. Can you make a `numpy` array out of it and convert the units to meters?

`height` is already available and the `numpy` package is loaded, so you can start straight away (Source: [stat.ucla.edu](http://wiki.stat.ucla.edu/socr/index.php/SOCR_Data_MLB_HeightsWeights)).

`@instructions`
- Create a `numpy` array from `height`. Name this new array `np_height`.
- Print `np_height`.
- Multiply `np_height` with `0.0254` to convert all height measurements from inches to meters. Store the new values in a new array, `np_height_m`.
- Print out `np_height_m` and check if the output makes sense.

`@hint`
- Use [`np.array()`](http://docs.scipy.org/doc/numpy-1.10.0/glossary.html#term-array) and pass it `height`. Store the result in `np_height`.
- To print out a variable `x`, type `print(x)` in the Python script.
- Perform calculations as if `np_height` is a single number: `np_height * factor` is part of the answer.
- To print out a variable `x`, type `print(x)` in the Python script.

`@pre_exercise_code`
```{python}
import pandas as pd
mlb = pd.read_csv("http://s3.amazonaws.com/assets.datacamp.com/course/intro_to_python/baseball.csv")
height = mlb['Height'].tolist()
import numpy as np
```

`@sample_code`
```{python}
# height is available as a regular list

# Import numpy
import numpy as np

# Create a numpy array from height: np_height


# Print out np_height


# Convert np_height to m: np_height_m


# Print np_height_m

```

`@solution`
```{python}
# height is available as a regular list

# Import numpy
import numpy as np

# Create a numpy array from height: np_height
np_height = np.array(height)

# Print out np_height
print(np_height)

# Convert np_height to m: np_height_m
np_height_m = np_height * 0.0254

# Print np_height_m
print(np_height_m)
```

`@sct`
```{python}
# sct code
test_import("numpy", same_as = False)

test_object("np_height", do_eval = False)
test_function("numpy.array", not_called_msg = "Be sure to call [`np.array()`](http://docs.scipy.org/doc/numpy-1.10.0/glossary.html#term-array).",
                             incorrect_msg = "You should call [`np.array()`](http://docs.scipy.org/doc/numpy-1.10.0/glossary.html#term-array) as follows: `np.array(np_height)`.")
test_object("np_height", incorrect_msg = "Assign the correct value to `np_height`.")

test_function("print", 1, incorrect_msg = "Print out `np_height` with `print(np_height)`.")

test_object("np_height_m", incorrect_msg = "Your calculation of `np_height_m` is not quite correct, be sure to multiply `np_height` with `0.0254`.")

test_function("print", 2, incorrect_msg = "Print out `np_height_m` with `print(np_height_m)`.")

success_msg("Nice! In the blink of an eye, `numpy` performs multiplications on more than 1000 height measurements.")
```

---
## Baseball player's BMI

```yaml
type: NormalExercise
lang: python
xp: 100
skills: 2
key: 689fdbc950
```

The MLB also offers to let you analyze their weight data. Again, both are available as regular Python lists: `height` and `weight`. `height` is in inches and `weight` is in pounds.

It's now possible to calculate the BMI of each baseball player. Python code to convert `height` to a `numpy` array with the correct units is already available in the workspace. Follow the instructions step by step and finish the game!

`@instructions`
- Create a `numpy` array from the `weight` list with the correct units. Multiply by `0.453592` to go from pounds to kilograms. Store the resulting `numpy` array as `np_weight_kg`.
- Use `np_height_m` and `np_weight_kg` to calculate the BMI of each player. Use the following equation: $$ \mathrm{BMI} = \frac{\mathrm{weight (kg)}}{\mathrm{height (m)}^2}$$ Save the resulting `numpy` array as `bmi`.
- Print out `bmi`.

`@hint`
- Use a similar approach as the code that calculates `np_height_m`. This time, though, the you have to work with `weight` and multiply with `0.453592`.
- To calculate the `bmi`, you will need the `/` and `**` operators.
- To print out a variable `x`, type `print(x)` in the script.

`@pre_exercise_code`
```{python}
import pandas as pd
mlb = pd.read_csv("http://s3.amazonaws.com/assets.datacamp.com/course/intro_to_python/baseball.csv")
height = mlb['Height'].tolist()
weight = mlb['Weight'].tolist()
import numpy as np
```

`@sample_code`
```{python}
# height and weight are available as a regular lists

# Import numpy
import numpy as np

# Create array from height with correct units: np_height_m
np_height_m = np.array(height) * 0.0254

# Create array from weight with correct units: np_weight_kg


# Calculate the BMI: bmi


# Print out bmi

```

`@solution`
```{python}
# height and weight are available as a regular lists

# Import numpy
import numpy as np

# Create array from height with correct units: np_height_m
np_height_m = np.array(height) * 0.0254

# Create array from weight with correct units: np_weight_kg
np_weight_kg = np.array(weight) * 0.453592

# Calculate the BMI: bmi
bmi = np_weight_kg / np_height_m ** 2

# Print out bmi
print(bmi)
```

`@sct`
```{python}
test_import("numpy", same_as = False)

# check np_height_m
msg = "The variable `np_height_m` was defined for you. You don't have to change or remove it!"
test_object("np_height_m", incorrect_msg = msg, undefined_msg = msg)

# test np_weight
test_object("np_weight_kg", do_eval = False)
test_function("numpy.array", 2, not_called_msg = "Be sure to call [`np.array()`](http://docs.scipy.org/doc/numpy-1.10.0/glossary.html#term-array).",
                                incorrect_msg = "To assign `np_weight_kg`, use `np.array(weight)`.")
test_object("np_weight_kg", incorrect_msg = "Are you calculating `np_weight_kg` correctly? Be sure to multiply `np.array(weight)` with `0.453592`.")

# check bmi
test_object("bmi", incorrect_msg = "Are you calculating `bmi` correctly? You can use `np_weight_kg / np_height_m ** 2` for this.")

test_function("print", 1, incorrect_msg = "Don't forget to print out `bmi`!")
success_msg("Cool! Time to step up your game!")
```

---
## Lightweight baseball players

```yaml
type: NormalExercise
lang: python
xp: 100
skills: 2
key: ef6add980e
```

To subset both regular Python lists and `numpy` arrays, you can use square brackets:

```
x = [4 , 9 , 6, 3, 1]
x[1]
import numpy as np
y = np.array(x)
y[1]
```

For `numpy` specifically, you can also use boolean `numpy` arrays:

```
high = y > 5
y[high]
```

The code that calculates the BMI of all baseball players is already included. Follow the instructions and reveal interesting things from the data!

`@instructions`
- Create a boolean `numpy` array: the element of the array should be `True` if the corresponding baseball player's BMI is below 21. You can use the `<` operator for this. Name the array `light`.
- Print the array `light`.
- Print out a `numpy` array with the BMIs of all baseball players whose BMI is below 21. Use `light` inside square brackets to do a selection on the `bmi` array.

`@hint`
- `bmi > 30` will give you a boolean `numpy` array in which the elements are `True` if the corresponding player's BMI is over 30.
- To print out a variable `x`, type `print(x)` in the Python script.
- `bmi[light]` will return the array you need. Don't forget to wrap a [`print()`](https://docs.python.org/3/library/functions.html#print) call around it!

`@pre_exercise_code`
```{python}
import pandas as pd
mlb = pd.read_csv("http://s3.amazonaws.com/assets.datacamp.com/course/intro_to_python/baseball.csv")
height = mlb['Height'].tolist()
weight = mlb['Weight'].tolist()
import numpy as np
```

`@sample_code`
```{python}
# height and weight are available as a regular lists

# Import numpy
import numpy as np

# Calculate the BMI: bmi
np_height_m = np.array(height) * 0.0254
np_weight_kg = np.array(weight) * 0.453592
bmi = np_weight_kg / np_height_m ** 2

# Create the light array


# Print out light


# Print out BMIs of all baseball players whose BMI is below 21

```

`@solution`
```{python}
# height and weight are available as a regular lists

# Import numpy
import numpy as np

# Calculate the BMI: bmi
np_height_m = np.array(height) * 0.0254
np_weight_kg = np.array(weight) * 0.453592
bmi = np_weight_kg / np_height_m ** 2

# Create the light array
light = bmi < 21

# Print out light
print(light)

# Print out BMIs of all baseball players whose BMI is below 21
print(bmi[light])
```

`@sct`
```{python}
msg = "You don't have to change or remove the predefined variables."
test_object("np_height_m", undefined_msg = msg, incorrect_msg = msg)
test_object("np_weight_kg", undefined_msg = msg, incorrect_msg = msg)
test_object("bmi", undefined_msg = msg, incorrect_msg = msg)

test_object("light", incorrect_msg = "Use the `<` boolean operator to define `light`. `bmi` should be smaller than `21`.")

test_function("print", 1, incorrect_msg = "Print out `light` with `print(light)`.")

test_function("print", 2, incorrect_msg = "For the second printout, use `light` as an index for `bmi`.")

success_msg("Wow! It appears that only 11 of the more than 1000 baseball players have a BMI under 21!")
```


---
## NumPy Side Effects

```yaml
type: MultipleChoiceExercise
lang: python
xp: 50
skills: 2
key: 3662ff6637
```

As Filip explained before, `numpy` is great for doing vector arithmetic. If you compare its functionality with regular Python lists, however, some things have changed.

First of all, `numpy` arrays cannot contain elements with different types. If you try to build such a list, some of the elements' types are changed to end up with a homogeneous list. This is known as _type coercion_.

Second, the typical arithmetic operators, such as `+`, `-`, `*` and `/` have a different meaning for regular Python lists and `numpy` arrays.

Have a look at this line of code:

```
np.array([True, 1, 2]) + np.array([3, 4, False])
```

Can you tell which code chunk builds the exact same Python object? The `numpy` package is already imported as `np`, so you can start experimenting in the IPython Shell straight away!

`@instructions`
- `np.array([True, 1, 2, 3, 4, False])`
- `np.array([4, 3, 0]) + np.array([0, 2, 2])`
- `np.array([1, 1, 2]) + np.array([3, 4, -1])`
- `np.array([0, 1, 2, 3, 4, 5])`


`@hint`
Copy the different code chunks and paste them in the IPython Shell. See which output matches the one generated by `np.array([True, 1, 2]) + np.array([3, 4, False])`.

`@pre_exercise_code`
```{python}
import numpy as np
```

`@sct`
```{python}
msg1 = msg3 = msg4 = "Incorrect. Try out the different code chunks and see which one matches the target code chunk."
msg2 = "Great job! `True` is converted to 1, `False` is converted to 0."
test_mc(2, [msg1, msg2, msg3, msg4])
```

---
## Subsetting NumPy Arrays

```yaml
type: NormalExercise
lang: python
xp: 100
skills: 2
key: fcb2a9007b
```

You've seen it with your own eyes: Python lists and `numpy` arrays sometimes behave differently. Luckily, there are still certainties in this world. For example, subsetting (using the square bracket notation on lists or arrays) works exactly the same. To see this for yourself, try the following lines of code in the IPython Shell:

```
x = ["a", "b", "c"]
x[1]

np_x = np.array(x)
np_x[1]
```

The script on the right already contains code that imports `numpy` as `np`, and stores both the height and weight of the MLB players as `numpy` arrays.

`@instructions`
- Subset `np_weight`: print out the element at index 50.
- Print out a sub-array of `np_height`: It contains the elements at index 100 up to **and including** index 110

`@hint`
- Make sure to wrap a [`print()`](https://docs.python.org/3/library/functions.html#print) call around your subsetting operations.
- Use `[100:111]` to get the elements from index 100 up to and including index 110.

`@pre_exercise_code`
```{python}
import pandas as pd
mlb = pd.read_csv("http://s3.amazonaws.com/assets.datacamp.com/course/intro_to_python/baseball.csv")
height = mlb['Height'].tolist()
weight = mlb['Weight'].tolist()
import numpy as np
```

`@sample_code`
```{python}
# height and weight are available as a regular lists

# Import numpy
import numpy as np

# Store weight and height lists as numpy arrays
np_weight = np.array(weight)
np_height = np.array(height)

# Print out the weight at index 50


# Print out sub-array of np_height: index 100 up to and including index 110

```

`@solution`
```{python}
# height and weight are available as a regular lists

# Import numpy
import numpy as np

# Store weight and height lists as numpy arrays
np_weight = np.array(weight)
np_height = np.array(height)

# Print out the weight at index 50
print(np_weight[50])

# Print out sub-array of np_height: index 100 up to and including index 110
print(np_height[100:111])
```

`@sct`
```{python}

test_import("numpy", same_as = False)

msg = "You don't have to change or remove the predefined variables."
test_object("np_height", undefined_msg = msg, incorrect_msg = msg)
test_object("np_weight", undefined_msg = msg, incorrect_msg = msg)

test_function("print", 1,
              incorrect_msg = "For the first printout, subset `np_weight` to select the 50th element.")

test_function("print", 2,
              incorrect_msg = "For the second printout, subset `np_height` to select the 100th to 110th element, included. You can use the slicing operator: `:`, just make sure to put in the correct ending index.")

success_msg("Nice! Time to learn something new: 2D Numpy arrays!")
```

---
## 2D NumPy Arrays

```yaml
type: VideoExercise
lang: python
xp: 50
skills: 2
key: 84e9f3c38d
```

`@video_link`
//player.vimeo.com/video/146994270

`@video_hls`
//videos.datacamp.com/transcoded/735_intro_to_python/v3/hls-ch4_2.master.m3u8

*** =projector_key
e6a2fb8649e4ba94d8a0dc7b03a6de62

---
## Your First 2D NumPy Array

```yaml
type: NormalExercise
lang: python
xp: 100
skills: 2
key: 5cb045bb13
```

Before working on the actual MLB data, let's try to create a 2D `numpy` array from a small list of lists.

In this exercise, `baseball` is a list of lists. The main list contains 4 elements. Each of these elements is a list containing the height and the weight of 4 baseball players, in this order. `baseball` is already coded for you in the script.

`@instructions`
- Use [`np.array()`](http://docs.scipy.org/doc/numpy-1.10.0/glossary.html#term-array) to create a 2D `numpy` array from `baseball`. Name it `np_baseball`.
- Print out the type of `np_baseball`.
- Print out the `shape` attribute of `np_baseball`. Use `np_baseball.shape`.

`@hint`
- `baseball` is already coded for you in the script. Call [`np.array()`](http://docs.scipy.org/doc/numpy-1.10.0/glossary.html#term-array) on it and store the resulting 2D `numpy` array in `np_baseball`.
- Use [`print()`](https://docs.python.org/3/library/functions.html#print) in combination with [`type()`](https://docs.python.org/3/library/functions.html#type) for the second instruction.
- `np_baseball.shape` will give you the dimensions of the `np_baseball`. Make sure to wrap a [`print()`](https://docs.python.org/3/library/functions.html#print) call around it.

`@pre_exercise_code`
```{python}
import numpy as np
```

`@sample_code`
```{python}
# Create baseball, a list of lists
baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

# Import numpy
import numpy as np

# Create a 2D numpy array from baseball: np_baseball


# Print out the type of np_baseball


# Print out the shape of np_baseball

```

`@solution`
```{python}
# Create baseball, a list of lists
baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

# Import numpy
import numpy as np

# Create a 2D numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out the type of np_baseball
print(type(np_baseball))

# Print out the shape of np_baseball
print(np_baseball.shape)
```

`@sct`
```{python}
msg = "You don't have to change or remove the predefined variables."
test_object("baseball", undefined_msg = msg, incorrect_msg = msg)

test_import("numpy", same_as = False)

test_object("np_baseball", do_eval = False)
test_function("numpy.array", not_called_msg = "Be sure to call [`np.array()`](http://docs.scipy.org/doc/numpy-1.10.0/glossary.html#term-array).",
                             incorrect_msg = "You should call `np.array(baseball)` to make a 2D `numpy` array out of `baseball`.")
test_object("np_baseball", incorrect_msg = "Assign the correct value to `np_baseball`.")

msg = "Make sure to print out the type of `np_baseball` like this: `print(type(np_baseball))`."
test_function("type", 1, incorrect_msg = msg)
test_function("print", 1, incorrect_msg = msg)

test_function("print", 2, incorrect_msg = "You can print the shape of `np_baseball` like this: `np_baseball.shape`.")

success_msg("Great! You're ready to convert the actual MLB data to a 2D `numpy` array now!")
```


---
## Baseball data in 2D form

```yaml
type: NormalExercise
lang: python
xp: 100
skills: 2
key: 5df25d0b7b
```

You have another look at the MLB data and realize that it makes more sense to restructure all this information in a 2D `numpy` array. This array should have 1015 rows, corresponding to the 1015 baseball players you have information on, and 2 columns (for height and weight).

The MLB was, again, very helpful and passed you the data in a different structure, a Python list of lists. In this list of lists, each sublist represents the height and weight of a single baseball player. The name of this embedded list is `baseball`.

Can you store the data as a 2D array to unlock `numpy`'s extra functionality?

`@instructions`
- Use [`np.array()`](http://docs.scipy.org/doc/numpy-1.10.0/glossary.html#term-array) to create a 2D `numpy` array from `baseball`. Name it `np_baseball`.
- Print out the `shape` attribute of `np_baseball`.

`@hint`
- `baseball` is already available in the Python environment. Call [`np.array()`](http://docs.scipy.org/doc/numpy-1.10.0/glossary.html#term-array) on it and store the resulting 2D `numpy` array in `np_baseball`.
- `np_baseball.shape` will give the dimensions of the `np_baseball`. Make sure to wrap a [`print()`](https://docs.python.org/3/library/functions.html#print) call around it.

`@pre_exercise_code`
```{python}
import pandas as pd
baseball = pd.read_csv("http://s3.amazonaws.com/assets.datacamp.com/course/intro_to_python/baseball.csv")[['Height', 'Weight']].as_matrix().tolist()
import numpy as np
```

`@sample_code`
```{python}
# baseball is available as a regular list of lists

# Import numpy package
import numpy as np

# Create a 2D numpy array from baseball: np_baseball


# Print out the shape of np_baseball

```

`@solution`
```{python}
# baseball is available as a regular list of lists

# Import numpy package
import numpy as np

# Create a 2D numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out the shape of np_baseball
print(np_baseball.shape)
```

`@sct`
```{python}
test_import("numpy", same_as = False)

test_object("np_baseball", do_eval = False)
test_function("numpy.array", not_called_msg = "Be sure to call [`np.array()`](http://docs.scipy.org/doc/numpy-1.10.0/glossary.html#term-array).",
                             incorrect_msg = "You should call `np.array(baseball)` to make a 2D `numpy` array out of `baseball`.")
test_object("np_baseball", incorrect_msg = "Assign the `numpy` array you created to `np_baseball`.")

test_function("print", incorrect_msg = "Print the `shape` field of the `np_baseball` object using the dot notation: `.`.")

success_msg("Slick! Time to show off some killer features of multi-dimensional `numpy` arrays!")
```

---
## Subsetting 2D NumPy Arrays

```yaml
type: NormalExercise
lang: python
xp: 100
skills: 2
key: aeca4977f0
```

If your 2D `numpy` array has a regular structure, i.e. each row and column has a fixed number of values, complicated ways of subsetting become very easy. Have a look at the code below where the elements `"a"` and `"c"` are extracted from a list of lists.

```
# regular list of lists
x = [["a", "b"], ["c", "d"]]
[x[0][0], x[1][0]]

# numpy
import numpy as np
np_x = np.array(x)
np_x[:,0]
```

For regular Python lists, this is a real pain. For 2D `numpy` arrays, however, it's pretty intuitive! The indexes before the comma refer to the rows, while those after the comma refer to the columns. The `:` is for slicing; in this example, it tells Python to include all rows.

The code that converts the pre-loaded `baseball` list to a 2D `numpy` array is already in the script. The first column contains the players' height in inches and the second column holds player weight, in pounds. Add some lines to make the correct selections. Remember that in Python, the first element is at index 0!

`@instructions`
- Print out the 50th row of `np_baseball`.
- Make a new variable, `np_weight`, containing the entire second column of `np_baseball`.
- Select the height (first column) of the 124th baseball player in `np_baseball` and print it out.

`@hint`
- You need row index 49 in the first instruction! More specifically, you'll want to use `[49,:]`.
- To select the entire second column, you'll need `[:,1]`.
- For the last instruction, use `[123, 0]`; don't forget to wrap it all in a [`print()`](https://docs.python.org/3/library/functions.html#print) statement.

`@pre_exercise_code`
```{python}
import pandas as pd
baseball = pd.read_csv("http://s3.amazonaws.com/assets.datacamp.com/course/intro_to_python/baseball.csv")[['Height', 'Weight']].as_matrix().tolist()
import numpy as np
```

`@sample_code`
```{python}
# baseball is available as a regular list of lists

# Import numpy package
import numpy as np

# Create np_baseball (2 cols)
np_baseball = np.array(baseball)

# Print out the 50th row of np_baseball


# Select the entire second column of np_baseball: np_weight


# Print out height of 124th player

```

`@solution`
```{python}
# baseball is available as a regular list of lists

# Import numpy package
import numpy as np

# Create np_baseball (2 cols)
np_baseball = np.array(baseball)

# Print out the 50th row of np_baseball
print(np_baseball[49,:])

# Select the entire second column of np_baseball: np_weight
np_weight = np_baseball[:,1]

# Print out height of 124th player
print(np_baseball[123, 0])
```

`@sct`
```{python}
test_import("numpy", same_as = False)

msg = "You don't have to change or remove the predefined variables."
test_object("np_baseball", undefined_msg = msg, incorrect_msg = msg)

test_function("print", 1, incorrect_msg = "For the first printout, subset the `np_baseball` object using `[49,:]`. This will select the 50th row completely.")

test_object("np_weight", incorrect_msg = "Define `np_weight` by subsetting the `np_baseball` object with `[:,1]`. This will select the first column, completely.")

test_function("print", 2, incorrect_msg = "For the second printout, subset the `np_baseball` object using `[123,0]`. This will select the first column of the 124th row.")
success_msg("This is going well!")
```

---
## 2D Arithmetic

```yaml
type: NormalExercise
lang: python
xp: 100
skills: 2
key: 1c2378b677
```

Remember how you calculated the Body Mass Index for all baseball players? `numpy` was able to perform all calculations element-wise (i.e. element by element). For 2D `numpy` arrays this isn't any different! You can combine matrices with single numbers, with vectors, and with other matrices.

Execute the code below in the IPython shell and see if you understand:

```
import numpy as np
np_mat = np.array([[1, 2],
                   [3, 4],
                   [5, 6]])
np_mat * 2
np_mat + np.array([10, 10])
np_mat + np_mat
```

`np_baseball` is coded for you; it's again a 2D `numpy` array with 3 columns representing height, weight and age.

`@instructions`
- You managed to get hold of the changes in weight, height and age of all baseball players. It is available as a 2D `numpy` array, `updated`. Add `np_baseball` and `updated` and print out the result.
- You want to convert the units of height and weight. As a first step, create a `numpy` array with three values: `0.0254`, `0.453592` and `1`. Name this array `conversion`.
- Multiply `np_baseball` with `conversion` and print out the result.

`@hint`
- `np_baseball + updated` will do an element-wise summation of the two `numpy` arrays.
- Create a `numpy` array with [`np.array()`](http://docs.scipy.org/doc/numpy-1.10.0/glossary.html#term-array); the input is a regular Python list with three elements.
- `np_baseball * conversion` will work, without extra work. Try out it! Make sure to wrap it in a [`print()`](https://docs.python.org/3/library/functions.html#print) call.

`@pre_exercise_code`
```{python}
import pandas as pd
import numpy as np
baseball = pd.read_csv("http://s3.amazonaws.com/assets.datacamp.com/course/intro_to_python/baseball.csv")[['Height', 'Weight', 'Age']].as_matrix().tolist()
n = len(baseball)
updated = np.array(pd.read_csv("http://s3.amazonaws.com/assets.datacamp.com/course/intro_to_python/update.csv", header = None))
import numpy as np
```

`@sample_code`
```{python}
# baseball is available as a regular list of lists
# updated is available as 2D numpy array

# Import numpy package
import numpy as np

# Create np_baseball (3 cols)
np_baseball = np.array(baseball)

# Print out addition of np_baseball and updated


# Create numpy array: conversion


# Print out product of np_baseball and conversion

```

`@solution`
```{python}
# baseball is available as a regular list of lists
# updated is available as 2D numpy array

# Import numpy package
import numpy as np

# Create np_baseball (3 cols)
np_baseball = np.array(baseball)

# Print out addition of np_baseball and updated
print(np_baseball + updated)

# Create numpy array: conversion
conversion = np.array([0.0254, 0.453592, 1])

# Print out product of np_baseball and conversion
print(np_baseball * conversion)
```

`@sct`
```{python}
test_import("numpy")

msg = "You don't have to change or remove the predefined variables."
test_object("np_baseball", undefined_msg = msg, incorrect_msg = msg)

test_function("print", 1, incorrect_msg = "Print out the result of `np_baseball + updated` using `print(np_baseball + updated)`.")

msg = "Create the `conversion` object using `np.array(...)`. Fill in the correct list on the dots."
test_function("numpy.array", not_called_msg = msg, incorrect_msg = msg)
test_object("conversion", incorrect_msg = "Assign the object you created with [`np.array()`](http://docs.scipy.org/doc/numpy-1.10.0/glossary.html#term-array) to `conversion`.")

test_function("print", 2, incorrect_msg = "Print out the result of `np_baseball * conversion` using `print(np_baseball * conversion)`.")

success_msg("Great job! Notice how with very little code, you can change all values in your `numpy` data structure in a very specific way. This will be very useful in your future as a data scientist!")
```

---
## NumPy: Basic Statistics

```yaml
type: VideoExercise
lang: python
xp: 50
skills: 2
key: 16403c5a74
```

`@video_link`
//player.vimeo.com/video/146994271

`@video_hls`
//videos.datacamp.com/transcoded/735_intro_to_python/v3/hls-ch4_3.master.m3u8

*** =projector_key
3c397bce7e44f4631520d5e5eb7e9433

---
## Average versus median

```yaml
type: NormalExercise
lang: python
xp: 100
skills: 2
key: 509c588eb6
```

You now know how to use `numpy` functions to get a better feeling for your data. It basically comes down to importing `numpy` and then calling several simple functions on the `numpy` arrays:

```
import numpy as np
x = [1, 4, 8, 10, 12]
np.mean(x)
np.median(x)
```

The baseball data is available as a 2D `numpy` array with 3 columns (height, weight, age) and 1015 rows. The name of this `numpy` array is `np_baseball`. After restructuring the data, however, you notice that some height values are abnormally high. Follow the instructions and discover which summary statistic is best suited if you're dealing with so-called _outliers_.

`@instructions`
- Create `numpy` array `np_height` that is equal to first column of `np_baseball`.
- Print out the mean of `np_height`.
- Print out the median of `np_height`.

`@hint`
- Use 2D `numpy` subsetting: `[:,0]` is a part of the solution.
- If `numpy` is imported as `np`, you can use [`np.mean()`](http://docs.scipy.org/doc/numpy-1.10.0/reference/generated/numpy.mean.html) to get the mean of a Numpy array. Don't forget to throw in a [`print()`](https://docs.python.org/3/library/functions.html#print) call.
- For the last instruction, use [`np.median()`](http://docs.scipy.org/doc/numpy-1.10.0/reference/generated/numpy.median.html).

`@pre_exercise_code`
```{python}
import pandas as pd
np_baseball = pd.read_csv("http://s3.amazonaws.com/assets.datacamp.com/course/intro_to_python/baseball.csv")[['Height', 'Weight', 'Age']].as_matrix()
np_baseball[slice(0, 1015, 50), 0] = np_baseball[slice(0, 1015, 50), 0]*1000
import numpy as np
```

`@sample_code`
```{python}
# np_baseball is available

# Import numpy
import numpy as np

# Create np_height from np_baseball


# Print out the mean of np_height


# Print out the median of np_height

```

`@solution`
```{python}
# np_baseball is available

# Import numpy
import numpy as np

# Create np_height from np_baseball
np_height = np_baseball[:,0]

# Print out the mean of np_height
print(np.mean(np_height))

# Print out the median of np_height
print(np.median(np_height))
```

`@sct`
```{python}
test_import("numpy", same_as = False)

test_object("np_height", incorrect_msg = "Make sure to use the correct subsetting operation to define `np_height`.")

test_function("numpy.mean", not_called_msg = "Don't forget to call [`np.mean()`](http://docs.scipy.org/doc/numpy-1.10.0/reference/generated/numpy.mean.html).", incorrect_msg = "Pass `np_height` as an argument to the `mean` function of `np` to print out the correct value for the first printout. Don't forget to use the dot notation: `.`.")

test_function("print", 1, incorrect_msg = "Print out the result of your calculations using `print(np.mean(np_height))`.")

test_function("numpy.median", not_called_msg = "Don't forget to call [`np.median()`](http://docs.scipy.org/doc/numpy-1.10.0/reference/generated/numpy.median.html).", incorrect_msg = "Pass `np_height` as an argument to the `median` function of `np` to print out the correct value for the second printout. Don't forget to use the dot notation: `.`.")

test_function("print", 2, incorrect_msg = "Print out the result of your calculations using `print(np.median(np_height))`.")

success_msg("An average height of 1586 inches, that doesn't sound right, does it? However, the median does not seem affected by the outliers: 74 inches makes perfect sense. It's always a good idea to check both the median and the mean, to get a first hunch for the overall distribution of the entire dataset.")
```

---
## Explore the baseball data

```yaml
type: NormalExercise
lang: python
xp: 100
skills: 2
key: 4409948807
```

Because the mean and median are so far apart, you decide to complain to the MLB. They find the error and send the corrected data over to you. It's again available as a 2D Numpy array `np_baseball`, with three columns.

The Python script on the right already includes code to print out informative messages with the different summary statistics. Can you finish the job?

`@instructions`
- The code to print out the mean height is already included. Complete the code for the median height. Replace `None` with the correct code.
- Use [`np.std()`](http://docs.scipy.org/doc/numpy-1.10.0/reference/generated/numpy.std.html) on the first column of `np_baseball` to calculate `stddev`. Replace `None` with the correct code.
- Do big players tend to be heavier? Use [`np.corrcoef()`](http://docs.scipy.org/doc/numpy-1.10.0/reference/generated/numpy.corrcoef.html) to store the correlation between the first and second column of `np_baseball` in `corr`. Replace `None` with the correct code.

`@hint`
- Use [`np.median()`](http://docs.scipy.org/doc/numpy-1.10.0/reference/generated/numpy.median.html) to calculate the median. Make sure to select to correct column first!
- Subset the same column when calculating the standard deviation with [`np.std()`](http://docs.scipy.org/doc/numpy-1.10.0/reference/generated/numpy.std.html).
- Use `np_baseball[:,0]` and `np_baseball[:,1]` to select the first and second columns; these are the inputs to [`np.corrcoef()`](http://docs.scipy.org/doc/numpy-1.10.0/reference/generated/numpy.corrcoef.html).

`@pre_exercise_code`
```{python}
import pandas as pd
np_baseball = pd.read_csv("http://s3.amazonaws.com/assets.datacamp.com/course/intro_to_python/baseball.csv")[['Height', 'Weight', 'Age']].as_matrix()
import numpy as np
```

`@sample_code`
```{python}
# np_baseball is available

# Import numpy
import numpy as np

# Print mean height (first column)
avg = np.mean(np_baseball[:,0])
print("Average: " + str(avg))

# Print median height. Replace 'None'
med = None
print("Median: " + str(med))

# Print out the standard deviation on height. Replace 'None'
stddev = None
print("Standard Deviation: " + str(stddev))

# Print out correlation between first and second column. Replace 'None'
corr = None
print("Correlation: " + str(corr))
```

`@solution`
```{python}
# np_baseball is available

# Import numpy
import numpy as np

# Print mean height (first column)
avg = np.mean(np_baseball[:,0])
print("Average: " + str(avg))

# Print median height. Replace 'None'
med = np.median(np_baseball[:,0])
print("Median: " + str(med))

# Print out the standard deviation on height. Replace 'None'
stddev = np.std(np_baseball[:,0])
print("Standard Deviation: " + str(stddev))

# Print out correlation between first and second column. Replace 'None'
corr = np.corrcoef(np_baseball[:,0], np_baseball[:,1])
print("Correlation: " + str(corr))
```

`@sct`
```{python}
# sct code
test_import("numpy")

msg = "You don't have to change or remove the predefined variables."
test_object("avg", undefined_msg = msg, incorrect_msg = msg)
test_function("print", 1, not_called_msg = msg, incorrect_msg = msg)

test_function("numpy.median", 1, not_called_msg = "Don't forget to call [`np.median()`](http://docs.scipy.org/doc/numpy-1.10.0/reference/generated/numpy.median.html).", incorrect_msg = "To assign `med`, use [`np.median()`](http://docs.scipy.org/doc/numpy-1.10.0/reference/generated/numpy.median.html). Make sure to pass it the correct column of `np_baseball`.")
test_object("med")
test_function("print", 2, not_called_msg = msg, incorrect_msg = msg)

test_function("numpy.std", 1, not_called_msg = "Don't forget to call [`np.std()`](http://docs.scipy.org/doc/numpy-1.10.0/reference/generated/numpy.std.html).", incorrect_msg = "To assign `stddev`, use [`np.std()`](http://docs.scipy.org/doc/numpy-1.10.0/reference/generated/numpy.std.html). Make sure to pass it the correct column of `np_baseball`.")
test_object("stddev")
test_function("print", 3, not_called_msg = msg, incorrect_msg = msg)

test_object("corr", incorrect_msg = "To assign `corr`, use [`np.corrcoef()`](http://docs.scipy.org/doc/numpy-1.10.0/reference/generated/numpy.corrcoef.html). Make sure to pass it the correct columns of `np_baseball`. You can pass it two columns.")
test_function("print", 4, not_called_msg = msg, incorrect_msg = msg)

success_msg("Great! Time to use all of your new data science skills in the last exercise!")
```

---
## Blend it all together

```yaml
type: NormalExercise
lang: python
xp: 100
skills: 2
key: e125cad8a5
```

In the last few exercises you've learned everything there is to know about heights and weights of baseball players. Now it's time to dive into another sport: soccer.

You've contacted FIFA for some data and they handed you two lists. The lists are the following:
```
positions = ['GK', 'M', 'A', 'D', ...]
heights = [191, 184, 185, 180, ...]
```
Each element in the lists corresponds to a player. The first list, `positions`, contains strings representing each player's position. The possible positions are: `'GK'` (goalkeeper), `'M'` (midfield), `'A'` (attack) and `'D'` (defense). The second list, `heights`, contains integers representing the height of the player in cm. The first player in the lists is a goalkeeper and is pretty tall (191 cm).

You're fairly confident that the median height of goalkeepers is higher than that of other players on the soccer field. Some of your friends don't believe you, so you are determined to show them using the data you received from FIFA and your newly acquired Python skills.

`@instructions`
- Convert `heights` and `positions`, which are regular lists, to numpy arrays. Call them `np_heights` and `np_positions`.
- Extract all the heights of the goalkeepers. You can use a little trick here: use `np_positions == 'GK'` as an index for `np_heights`. Assign the result to `gk_heights`.
- Extract all the heights of all the other players. This time use `np_positions != 'GK'` as an index for `np_heights`. Assign the result to `other_heights`.
- Print out the median height of the goalkeepers using [`np.median()`](http://docs.scipy.org/doc/numpy-1.10.0/reference/generated/numpy.median.html). Replace `None` with the correct code.
- Do the same for the other players. Print out their median height. Replace `None` with the correct code.

`@hint`
- Use [`np.array()`](http://docs.scipy.org/doc/numpy-1.10.0/glossary.html#term-array) to convert the lists to numpy arrays.
- You should use `np_heights[np_positions == 'GK']` to extract the heights of all goalkeepers. Don't forget to assign the result to `gk_heights`.
- You should use `np_heights[np_positions != 'GK']` to extract the heights of all other players. Don't forget to assign the result to `other_heights`.
- Print out the median height of the goalkeepers using `np.median(gk_heights)`.
- Print out the median height of the other players using `np.median(other_heights)`.

`@pre_exercise_code`
```{python}
import pandas as pd
fifa =  pd.read_csv("http://s3.amazonaws.com/assets.datacamp.com/course/intro_to_python/fifa.csv", skipinitialspace=True, usecols=['position', 'height'])
positions = list(fifa.position)
heights = list(fifa.height)
```

`@sample_code`
```{python}
# heights and positions are available as lists

# Import numpy
import numpy as np

# Convert positions and heights to numpy arrays: np_positions, np_heights



# Heights of the goalkeepers: gk_heights


# Heights of the other players: other_heights


# Print out the median height of goalkeepers. Replace 'None'
print("Median height of goalkeepers: " + str(None))

# Print out the median height of other players. Replace 'None'
print("Median height of other players: " + str(None))
```

`@solution`
```{python}
# heights and positions are available as lists

# Import numpy
import numpy as np

# Convert positions and heights to numpy arrays: np_positions, np_heights
np_positions = np.array(positions)
np_heights = np.array(heights)

# Heights of the goalkeepers: gk_heights
gk_heights = np_heights[np_positions == 'GK']

# Heights of the other players: other_heights
other_heights = np_heights[np_positions != 'GK']

# Print out the median height of goalkeepers. Replace 'None'
print("Median height of goalkeepers: " + str(np.median(gk_heights)))

# Print out the median height of other players. Replace 'None'
print("Median height of other players: " + str(np.median(other_heights)))
```

`@sct`
```{python}
test_import("numpy")

msg = "Convert the regular lists to numpy lists using [`np.array()`](http://docs.scipy.org/doc/numpy-1.10.0/glossary.html#term-array). This function takes one argument: the regular list itself!"
test_object("np_positions", do_eval = False)
test_function("numpy.array", 1, not_called_msg = msg, incorrect_msg = msg)
test_object("np_positions", incorrect_msg = "Assign the converted numpy array of `positions` to `np_positions`.")

test_object("np_heights", do_eval = False)
test_function("numpy.array", 2, not_called_msg = msg, incorrect_msg = msg)
test_object("np_heights", incorrect_msg = "Assign the converted numpy array of `heights` to `np_heights`.")

test_object("gk_heights", incorrect_msg = "You can use `[np_positions == 'GK']` as an index of `np_heights` to find the heights of all goalkeepers, `gk_heights`. You can use a hint if you're stuck!")
test_object("other_heights", incorrect_msg = "You can use `[np_positions != 'GK']` as an index of `np_heights` to find the heights of all other players, `other_heights`. You can use a hint if you're stuck!")

msg = "Use `np.median(%s)` to find the median height of %s."

gk_msg = msg % ("gk_heights", "goalkeepers")
test_function("numpy.median", 1, not_called_msg = gk_msg, incorrect_msg = gk_msg)
test_function("print", 1, incorrect_msg = "Don't forget to print out the result for the goalkeepers.")

other_msg = msg % ("other_heights", "other players")
test_function("numpy.median", 2, not_called_msg = other_msg, incorrect_msg = other_msg)
test_function("print", 2, incorrect_msg = "Don't forget to print out the result for the other players.")

success_msg("Wonderful! You were right and the disbelievers were wrong! This exercise marks the end of the Intro to Python for Data Science course. See you in another course!")
```

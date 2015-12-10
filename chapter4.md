---
title_meta  : Chapter 4
title       : Numpy
description : Numpy is a Python package to efficiently do data science. Learn to work with the Numpy array, a faster and more powerful alternative to the list, and take your first steps in data exploration.

--- type:VideoExercise lang:python xp:50 skills:2
## Numpy

*** =video_link
//player.vimeo.com/video/146994268

--- type:NormalExercise lang:python xp:100 skills:2
## Your First Numpy Array

In this chapter, we're going to dive into the world of baseball. Along the way, you'll get comfortable with the basics of Numpy, a powerful package to do data science.

A list `baseball` has already been defined in the Python script, representing the height of some baseball players in centimeters. Can you add some code here and there to create a Numpy array from it?

*** =instructions
- Import the `numpy` package as `np`, so that you can refer to `numpy` with `np`.
- Use `np.array()` to create a Numpy array from `baseball`. Name this array `np_baseball`.
- Print out the type of `np_baseball` to check that you got it right.

*** =hint
- `import numpy as np` will do the trick. Now, you have to use `np.fun_name()` whenever you want to use a Numpy function.
- `np.array()` should take on input `baseball`. Assign the result of the function call to `np_baseball`.
- To print out the type of a variable `x`, simply type `print(type(x))`.

*** =pre_exercise_code
```{python}
import numpy as np
```

*** =sample_code
```{python}
# Create list baseball 
baseball = [180, 215, 210, 210, 188, 176, 209, 200]

# Import the numpy package as np


# Create a Numpy array from baseball: np_baseball


# Print out type of np_baseball

```

*** =solution
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

*** =sct
```{python}
msg = "You don't have to change or edit the predefined variables."
test_object("baseball", undefined_msg = msg, incorrect_msg = msg)

test_import("numpy", same_as = False)

test_object("np_baseball", do_eval = False)
test_function("numpy.array")
test_object("np_baseball")

test_function("type")
test_function("print")
success_msg("Great job!")
```

--- type:NormalExercise lang:python xp:100 skills:2
## Baseball players' height

Being a huge baseball fan, you call the MLB, the Major League of Baseball, and ask around for more statistics on the height of the main players. They pass you along more data on more than a thousand players, which is stored as a regular Python list: `height`. The height is expressed in inches. Can you make a Numpy array out of it, and convert the units to centimeters?

`height` is already available and the `numpy` package is loaded, so you can start straight away (Source: [stat.ucla.edu](http://wiki.stat.ucla.edu/socr/index.php/SOCR_Data_MLB_HeightsWeights)).

*** =instructions
- Create a Numpy array from `height`. Name this new array `np_height`.
- Multiply `np_height` with `2.54` to convert all weight measurements from inches to centimeters. Store the new values in a new array, `np_height_cm`.
- Print out `np_height_cm` and check if the output makes sense.

*** =hint
- Use `np.array()` and pass it `height`. Store the result in `np_height`.
- Perform calculations as if `np_height` is a single number: `np_height * factor` is part of the answer.
- To print out a variable `x`, type `print(x)` in the Python script.

*** =pre_exercise_code
```{python}
import pandas as pd
mlb = pd.read_csv("http://s3.amazonaws.com/assets.datacamp.com/course/intro_to_python/baseball.csv")
height = mlb['Height'].tolist()
import numpy as np
```

*** =sample_code
```{python}
# height is available as a regular list

# Import numpy
import numpy as np

# Create a Numpy array from height: np_height


# Print out np_height


# Convert np_height to cm: np_height_cm


# Print np_height_cm

```

*** =solution
```{python}
# height is available as a regular list

# Import numpy
import numpy as np

# Create a Numpy array from height: np_height
np_height = np.array(height)

# Print out np_height
print(np_height)

# Convert np_height to cm: np_height_cm
np_height_cm = np_height * 2.54

# Print np_height_cm
print(np_height_cm)
```

*** =sct
```{python}
# sct code
test_import("numpy", same_as = False)

test_object("np_height", do_eval = False)
test_function("numpy.array")
test_object("np_height")

test_function("print", 1)

test_object("np_height_cm", do_eval = False)
test_operator(1)
test_object("np_height_cm")

test_function("print", 2)

success_msg("Nice! In the blink of an eye, Numpy performs multiplications on more than 1000 height measurements.")
```

--- type:NormalExercise lang:python xp:100 skills:2
## Baseball player's BMI

Next to height, the MLB also offers you to analyze their weight data. Again, both are available as regular Python lists: `height` and `weight`; height is in inches, weight is in pounds.

It's now possible to calculate the BMI of each baseball player. Python code to convert `height` to a Numpy array with the correct units is already available. Follow the instructions step by step and finish the game!

*** =instructions
- Create a Numpy array from the `weight` list with the correct units: multiply with `0.453592` to go from pounds to kilograms. Store the resulting Numpy array as `np_weight_kg`.
- Use `np_height_m` and `np_weight_kg` to calculate the BMI of each player. Use the following equation: $$ \mathrm{BMI} = \frac{\mathrm{weight (kg)}}{\mathrm{height (m)}^2}$$ Save the resulting numpy array as `bmi`.
- Print out `bmi`.

*** =hint
- Use a similar approach as the code that calculates `np_height_m`. This time, though, the you have to work with `height` and multiply with `0.453592`.
- To calculate the `bmi`, you will need the `\` and `**` operators.
- To print out a variable `x`, type `print(x)` in the script.

*** =pre_exercise_code
```{python}
import pandas as pd
mlb = pd.read_csv("http://s3.amazonaws.com/assets.datacamp.com/course/intro_to_python/baseball.csv")
height = mlb['Height'].tolist()
weight = mlb['Weight'].tolist()
import numpy as np
```

*** =sample_code
```{python}
# height and weight are available as a regular lists

# Import numpy
import numpy as np

# Create array from height with correct units: np_height_m


# Create array from weight with correct units: np_weight_kg 


# Calculate the BMI: bmi
bmi = np_weight_kg / np_height_m ** 2

# Print out bmi
print(bmi)
```

*** =solution
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

*** =sct
```{python}
test_import("numpy", same_as = False)

test_object("np_height_m", do_eval = False)
test_function("numpy.array", 1, incorrect_msg = "For assigning <code>np_height_m</code>, use <code>np.array(height)</code>.")
test_operator(1)
test_object("np_height_m")

test_object("np_weight_kg", do_eval = False)
test_function("numpy.array", 2, incorrect_msg = "For assigning <code>np_weight_kg</code>, use <code>np.array(weight)</code>.")
test_operator(2)
test_object("np_weight_kg")

test_object("bmi", do_eval = False)
test_operator(3)
test_object("bmi")

test_function("print")
success_msg("Cool! Time to step up your game!")
```

--- type:NormalExercise lang:python xp:100 skills:2
## Lightweight baseball players

To subset both regular Python lists and Numpy arrays, you can use square brackets:

```
x = [4 , 9 , 6, 3, 1]
x[1]
import numpy as np
y = np.array(x)
y[1]
```

For Numpy specifically, you can also use boolean Numpy arrays:

```
high = y > 5
y[high]
```

The code that calculates the BMI of all baseball players is already included. Follow the instructions and reveal interesting things from the data!

*** =instructions
- Create a boolean Numpy array: the element of the array should be `True` if the corresponding baseball player's BMI is below 21. You can use the `<` operator for this. Name the array `light`.
- Print the array `light`.
- Print out a Numpy array with the BMIs of all baseball players whose BMI is below 21. Use `light` inside square brackets to do a selection on the `bmi` array.

*** =hint
- `bmi > 30` will give you a boolean Numpy array in which the elements are `True` if the corresponding player's BMI is over 30.
- To print out a variable `x`, type `print(x)` in the Python script.
- `bmi[light]` will return the array you need. Don't forget to wrap a `print()` call around it!

*** =pre_exercise_code
```{python}
import pandas as pd
mlb = pd.read_csv("http://s3.amazonaws.com/assets.datacamp.com/course/intro_to_python/baseball.csv")
height = mlb['Height'].tolist()
weight = mlb['Weight'].tolist()
import numpy as np
```

*** =sample_code
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

*** =solution
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

*** =sct
```{python}
msg = "You don't have to change or edit the predefined variables."
test_object("np_height_m", undefined_msg = msg, incorrect_msg = msg)
test_object("np_weight_kg", undefined_msg = msg, incorrect_msg = msg)
test_object("bmi", undefined_msg = msg, incorrect_msg = msg)

test_object("light", incorrect_msg = "Use the <code><</code> boolean operator to define <code>light</code>. <code>bmi</code> should be smaller than <code>21</code>.")

test_function("print", 1)

test_function("print", 2, incorrect_msg = "For the second printout, use <code>light</code> as an index for <code>bmi</code>.")

success_msg("Wow! It appears that only 11 of the more than 1000 baseball players have a BMI under 21!")
```


--- type:MultipleChoiceExercise lang:python xp:50 skills:2
## Numpy Side Effects

As Filip explained before, Numpy is great to do vector arithmetic. However, if you compare its functionality with regular Python lists, some things have changed. 

First of all, Numpy arrays cannot contain elements with different types. If you try to build such a list, some of the elments' types are changed to end up with a homogenous list. This is known as _type coercion_. 

Second, the typical arithmetic operators, such as `+`, `-`, `*` and `/` have a different meaning for regular Python lists and Numpy arrays.

Have a look at this line of code:

```
np.array([True, 1, 2]) + np.array([3, 4, False])
```

Can you tell which code chunk builds the exact same Python data structure? `numpy` is already imported as `np`, so you can start experimenting in the IPython Shell straight away!

*** =instructions
- `np.array([True, 1, 2, 3, 4, False])`
- `np.array([4, 3, 0]) + np.array([0, 2, 2])`
- `np.array([1, 1, 2]) + np.array([3, 4, -1])`
- `np.array([0, 1, 2, 3, 4, 5])`


*** =hint
Copy the different code chunks and paste them in the IPython Shell. See which output matches the one generated by `np.array([True, 1, 2]) + np.array([3, 4, False])`.

*** =pre_exercise_code
```{python}
import numpy as np
```

*** =sct
```{python}
msg1 = msg3 = msg4 = "Incorrect. Try out the different code chunks and see which one matches the target code chunk."
msg2 = "Great job!"
test_mc(2, [msg1, msg2, msg3, msg4])
```

--- type:NormalExercise lang:python xp:100 skills:2
## Subsetting Numpy Arrays

You've seen it with your own eyes: Python lists and Numpy arrays sometimes behave differently. Luckily, there are still certainties in this world. Subsetting for example: Using the square bracket notation on lists or arrays works exactly the same. To see this for yourself, try the following lines of code in the IPython Shell:

```
x = ["a", "b", "c"]
x[1]
np_x = np.array(x)
np_x[1]
```

The script on the right already contains code that imports `numpy` as `np`, and stores both the height and weight of the MLB players as Numpy arrays.

*** =instructions
- Subset `np_weight`: print out the element at index 50.
- Print out a sub-array of `np_height`: It contains the elements at index 100 up to **and including** index 110

*** =hint
- Make sure to wrap a `print()` call around your subsetting operations.
- Use `[100:111]` to get the elements from index 100 up to and including index 110.

*** =pre_exercise_code
```{python}
import pandas as pd
mlb = pd.read_csv("http://s3.amazonaws.com/assets.datacamp.com/course/intro_to_python/baseball.csv")
height = mlb['Height'].tolist()
weight = mlb['Weight'].tolist()
import numpy as np
```

*** =sample_code
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

*** =solution
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

*** =sct
```{python}

test_import("numpy", same_as = False)

msg = "You don't have to change or edit the predefined variables."
test_object("np_height", undefined_msg = msg, incorrect_msg = msg)
test_object("np_weight", undefined_msg = msg, incorrect_msg = msg)

test_function("print", 1,
              incorrect_msg = "For the first printout, subset <code>np_weight</code> to select the 50th element.")

test_function("print", 2,
              incorrect_msg = "For the second printout, subset <code>np_height</code> to select the 100th to 110th element, included. You can use the slicing operator: <code>:</code>, just make sure to put in the correct ending index.")

success_msg("Nice! Time to learn something new: 2D Numpy arrays!")
```

--- type:VideoExercise lang:python xp:50 skills:2
## 2D Numpy Arrays

*** =video_link
//player.vimeo.com/video/146994270

--- type:NormalExercise lang:python xp:100 skills:2
## Build a 2D Numpy array

Previously, you've worked with the height and weight of Major League Baseball players. Maybe it makes more sense to restructure all this information in a 2D Numpy array. This array should have 1015 rows, corresponding to the 1015 baseball players you have information on, and 2 columns, for height and weight.

The MLB was again very helpful and passed you the data in a different structure: as a Python list of lists, where each sublist represents the height and weight of a single baseball player. The name of this embedded list is `baseball`.

Can you store the data as a 2D array to unlock the extra functionality?

*** =instructions
- Use `np.array()` to create a 2D Numpy array from `baseball`. Name it `np_baseball`.
- Print out the type of `np_baseball`.
- Print out the `shape` attribute of `np_baseball`. Use `.shape`.

*** =hint
- `baseball` is already available in the Python environment. Call `np.array()` on it and store the resulting 2D Numpy array in `np_baseball`.
- Use `print()` in combination with `type()` for the second instruction.
- `np_baseball.shape` will give the dimensions of the `np_baseball`. Make sure to wrap a `print()` call around it.

*** =pre_exercise_code
```{python}
import pandas as pd
baseball = pd.read_csv("http://s3.amazonaws.com/assets.datacamp.com/course/intro_to_python/baseball.csv")[['Height', 'Weight']].as_matrix().tolist()
import numpy as np
```

*** =sample_code
```{python}
# baseball is available as a regular list of lists

# Import numpy package
import numpy as np

# Create a 2D Numpy array from baseball: np_baseball


# Print out the type of np_baseball


# Print out the shape of np_baseball

```

*** =solution
```{python}
# baseball is available as a regular list of lists

# Import numpy package
import numpy as np

# Create a 2D Numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out the type of np_baseball
print(type(np_baseball))

# Print out the shape of np_baseball
print(np_baseball.shape)
```

*** =sct
```{python}
test_import("numpy", same_as = False)

test_object("np_baseball", do_eval = False)
test_function("numpy.array")
test_object("np_baseball")

test_function("type")
test_function("print", 1)

test_function("print", 2, incorrect_msg = "For the second printout, print the <code>shape</code> field of the <code>np_baseball</code> object using the dot notation: <code>.</code>.")

success_msg("Slick! Time to show off some killer features of multi-dimensional Numpy arrays!")
```

--- type:NormalExercise lang:python xp:100 skills:2
## Subsetting 2D Numpy Arrays

If your 2D Numpy arrays has a regular structure, i.e. each row and column has a fixed number of values, complicated ways of subsetting become very easy. Have a look at the code below, where the elements `"a"` and `"c"` are extracted from a list of lists. 

```
# regular list of lists
x = [["a", "b"], ["c", "d"]]
[x[0][0], x[1][0]]

# numpy
import numpy as np
np_x = np.array(x)
np_x[:,0]
```

For the regular Python lists, this is a real pain. For 2D Numpy arrays, it's pretty intuitive: the indexes before the column refer to the rows, those after the column refer to the columns. The `:` is for slicing: in this example, it tells Python to include all rows.

The code that converts the pre-loaded `baseball` list to a 2D Numpy array is already in the script. Add some lines to make the correct selections. Remember that in Python, the first element is at index 0!

*** =instructions
- Print out the 50th row of `np_baseball`.
- Make a new variable, `np_weight`, containing the entire second column of `np_baseball`.
- Select the height (first column) of the 124th baseball player in `np_baseball` and print it out.

*** =hint
- You need row index 49 in the first instruction! More specifically, you'll want to use `[49,:]`.
- To select the entire second column, you'll need `[:,1]`.
- For the last instruction, use `[123, 0]`; don't forget to wrap it all in a `print()` statement.

*** =pre_exercise_code
```{python}
import pandas as pd
baseball = pd.read_csv("http://s3.amazonaws.com/assets.datacamp.com/course/intro_to_python/baseball.csv")[['Height', 'Weight']].as_matrix().tolist()
import numpy as np
```

*** =sample_code
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

*** =solution
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
print(np_baseball[123, 1])
```

*** =sct
```{python}
test_import("numpy", same_as = False)

msg = "You don't have to change or edit the predefined variables."
test_object("np_baseball", undefined_msg = msg, incorrect_msg = msg)

test_function("print", 1, incorrect_msg = "For the first printout, subset the <code>np_baseball</code> object using <code>[49,:]</code>. This will select the 49th row completely.")

test_object("np_weight", incorrect_msg = "Define <code>np_weight</code> by subsetting the <code>np_baseball</code> object with <code>[:,1]</code>. This will select the first column, completely.")

test_function("print", 2, incorrect_msg = "For the first printout, subset the <code>np_baseball</code> object using <code>[123,1]</code>. This will select the first column of the 123th row.")
success_msg("This is going well!")
```

--- type:NormalExercise lang:python xp:100 skills:2
## Subsetting 2D Numpy Arrays (2)

Apart from selecting single elements, entire columns or entire rows from a 2D Numpy array, it's also perfectly possible to create a "sub 2d array" of the 2D array you started with. You can do this with slicing. 

As an example, check out the following calls, that builds a 3-by-3 Numpy array and then select the lower right 2-by-2 corner from it:

```
import numpy as np
x = [["a", "b", "c"],
     ["d", "e", "f"],
     ["g", "h", "i"]]
np_x = np.array(x)
np_x[1:, 1:]
```

Still remember the principle? The slice is written as `begin:end`: The `begin` is included, the `end` index is not.

The code to build the 2D Numpy array `np_baseball` from the `baseball` lists of lists is already included. This time, `np_baseball` contains three columns, corresponding to height, weight and age of the Major Baseball League players. Can you do the correct subsetting operations?

*** =instructions
- Print out the first first and second column of the first ten rows, so row index 0 up to and including row index 9
- Print out a sub-array containing all three columns in the row indexes 205 up to __and including__ 235. These are all the players of the *New York Yankees* (NYY).

*** =hint
- For the first instruction, you can use `[:10, :].
- For the second instruction, you can use `[:, 205:236]`.

*** =pre_exercise_code
```{python}
import pandas as pd
baseball = pd.read_csv("http://s3.amazonaws.com/assets.datacamp.com/course/intro_to_python/baseball.csv")[['Height', 'Weight', 'Age']].as_matrix().tolist()
import numpy as np
```

*** =sample_code
```{python}
# baseball is available as a regular list of lists

# Import numpy package
import numpy as np

# Create np_baseball (3 cols)
np_baseball = np.array(baseball)

# Print out first and second column of first ten rows


# Print out all three columns for row indexes 205 up to and including 235

```

*** =solution
```{python}
# baseball is available as a regular list of lists

# Import numpy package
import numpy as np

# Create np_baseball (3 cols)
np_baseball = np.array(baseball)

# Print out first and second column of first ten rows
print(baseball[:2, :10])

# Print out all three columns for row indexes 205 up to and including 235
print(baseball[:, 205:236])
```

*** =sct
```{python}
test_import("numpy", same_as = False)

msg = "You don't have to change or edit the predefined variables."
test_object("np_baseball", undefined_msg = msg, incorrect_msg = msg)

test_function("print", 1, incorrect_msg = "For the first printout, subset the <code>np_baseball</code> object using <code>[:2,:10]</code>. This will select the first and the second column and the first ten rows.")

test_function("print", 2, incorrect_msg = "For the second printout, subset the <code>np_baseball</code> object using <code>[205,236]</code>. This will select the all columns of row 205 to and including 235.")

success_msg("Great job!")
```

--- type:NormalExercise lang:python xp:100 skills:2
## 2D Arithmetic

Remember how you calculated the Body Mass Index for all baseball players? Numpy was able to perform all calculations element-wise. For 2D Numpy arrays this isn't any different: you can combine matrices with single numbers, with vectors, and with other matrices.

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

`np_baseball` is coded for you; it's again a 2D Numpy array with 3 columns, representing height, weight and age.

*** =instructions
- You managed to get hold on the changes in weight, height and age of all baseball players. It is available as a 2D Numpy array, `update`. Add `np_baseball` and `update` and print out the result.
- You want to convert the units of height and weight. As a first step, create a Numpy array with three values: `0.0254`, `0.453592` and `1`. Name this array `conversion`.
- Multiply `np_baseball` with `conversion` and print out the result.

*** =hint
- `np_baseball + update` will do a element-wise summation of the two Numpy arrays.
- Create a Numpy array with `np.array()`; the input is a regular Python list with three elements.
- `np_baseball * conversion` will work, without extra work. Try out it! Make sure to wrap it in a `print()` call.

*** =pre_exercise_code
```{python}
import pandas as pd
import numpy as np
baseball = pd.read_csv("http://s3.amazonaws.com/assets.datacamp.com/course/intro_to_python/baseball.csv")[['Height', 'Weight', 'Age']].as_matrix().tolist()
n = len(baseball)
update = np.column_stack((np.random.normal(1, 0.20, n), 
                          np.random.normal(0, 10, n), 
                          np.ones(n)))
import numpy as np
```

*** =sample_code
```{python}
# baseball is available as a regular list of lists
# update is available as 2D Numpy array

# Import numpy package
import numpy as np

# Create np_baseball (3 cols)
np_baseball = np.array(baseball)

# Print out addition of np_baseball and update


# Create Numpy array: conversion


# Print out product of np_baseball and conversion

```

*** =solution
```{python}
# baseball is available as a regular list of lists
# update is available as 2D Numpy array

# Import numpy package
import numpy as np

# Create np_baseball (3 cols)
np_baseball = np.array(baseball)

# Print out addition of np_baseball and update
print(np_baseball + update)

# Create Numpy array: conversion
conversion = np.array([0.0254, 0.453592, 1])

# Print out product of np_baseball and conversion
print(np_baseball * conversion)
```

*** =sct
```{python}
test_import("numpy")

msg = "You don't have to change or edit the predefined variables."
test_object("np_baseball", undefined_msg = msg, incorrect_msg = msg)

test_operator(1, not_found_msg = "Use the <code>+</code> operator to add <code>update</code> to <code>np_baseball</code>.",
                 incorrect_result_msg = "Are you sure you correctly added <code>update</code> to <code>np_baseball</code>? The resulting numpy array seems to be incorrect.")
                 
test_function("print", 1)

test_object("conversion", do_eval = False)
test_function("numpy.array")
test_object("conversion")


test_operator(2, not_found_msg = "Use the <code>*</code> operator to multiply <code>np_baseball</code> with <code>conversion</code>.",
                 incorrect_result_msg = "Are you sure you correctly miltiplied <code>np_baseball</code> with <code>conversion</code>? The resulting numpy array seems to be incorrect.")
                 
test_function("print", 2)

success_msg("Great job! Notice how with very little code, you can change all values in your Numpy data structure in a very specific way. This will be very useful in your future as a data scientist!")
```

--- type:VideoExercise lang:python xp:50 skills:2
## Numpy: Basic Statistics

*** =video_link
//player.vimeo.com/video/146994271

--- type:NormalExercise lang:python xp:100 skills:2
## Average versus median

You now know about Numpy functions to a get a better feeling for your data. It basically comes down to importing Numpy, and then calling several simple functions on the Numpy arrays:

```
import numpy as np
x = [1, 4, 8, 10, 12]
np.mean(x)
np.median(x)
```

The baseball data is available as a 2D Numpy array with 3 columns (height, weight, age) and 1015 rows. The name of this Numpy array is `np_baseball`. However, when restructuring the data, something went wrong: some height values are abnormally high. Follow the instructions and discover which summary statistic is most suited if you're dealing with so-called _outliers_.

*** =instructions
- Create Numpy array `np_height`, that is equal to first column of `np_baseball`.
- Print out the mean of `np_height`.
- Print out the median of `np_height`.

*** =hint
- Use 2D Numpy subsetting: `[:,0]` is a part of the solution.
- If `numpy` is imported as `np`, you can use `np.mean()` to get the mean of a Numpy array. Don't forget to throw in a `print()` call.
- For the last instruction, use `np.median()`.

*** =pre_exercise_code
```{python}
import pandas as pd
np_baseball = pd.read_csv("http://s3.amazonaws.com/assets.datacamp.com/course/intro_to_python/baseball.csv")[['Height', 'Weight', 'Age']].as_matrix()
np_baseball[slice(0, 1015, 50), 0] = np_baseball[slice(0, 1015, 50), 0]*1000
import numpy as np
```

*** =sample_code
```{python}
# np_baseball is available

# Import numpy
import numpy as np

# Create np_height from np_baseball


# Print out the mean of np_height


# Print out the median of np_width

```

*** =solution
```{python}
# np_baseball is available

# Import numpy
import numpy as np

# Create np_height from np_baseball
np_height = np_baseball[:,0]

# Print out the mean of np_height
print(np.mean(np_height))

# Print out the median of np_width
print(np.median(np_height))
```

*** =sct
```{python}
test_import("numpy", same_as = False)

test_object("np_height", incorrect_msg = "Make sure to use the correct subsetting operation to define <code>np_height</code>.")

test_function("numpy.mean", incorrect_msg = "Pass <code>np_height</code> as an argument to the <code>mean</code> function of <code>numpy</code> to print out the correct value for the first printout. Don't forget to use the dot notation: <code>.</code>.")

test_function("print", 1)

test_function("numpy.median", incorrect_msg = "Pass <code>np_height</code> as an argument to the <code>median</code> function of <code>numpy</code> to print out the correct value for the second printout. Don't forget to use the dot notation: <code>.</code>.")

test_function("print", 2)

success_msg("An average length of 1586 inches, that doesn't sound right, does it? However, the median does not seem affected by the outliers: 74 inches makes perfect sense. It's always a good idea to check both the median and the mean, to get a first hunch for the overall distribution of the entire dataset.")
```

--- type:NormalExercise lang:python xp:100 skills:2
## Explore the baseball data

Because the mean and median are so far apart, you decide to complain with the MLB. They found the error and send the corrected data over to you. It's again available as a 2D Numpy array `np_baseball`, with three columns. 

The Python script on the right already includes code to print out informative messages with the different summary statistics. Can you finish the job?

*** =instructions
- The code to print out the mean height is already included. Complete the code for the median height.
- Use `np.std()` on the first column of `np_baseball` to calculate `stddev`.
- Do big players tend to be heavier? Use `np.corrcoef()` to store the correlation between the first and second column of `np_baseball` in `corr`.

*** =hint
- Use `np.median()` to calculate the median. Make sure to select to correct column first!
- Subset the same column when calculating the standard deviation with `np.std()`.
- Use `np_baseball[:,0]` and `np_baseball[:,1]` to select the first and second columns; these are the inputs to `np.corrcoef()`.

*** =pre_exercise_code
```{python}
import pandas as pd
np_baseball = pd.read_csv("http://s3.amazonaws.com/assets.datacamp.com/course/intro_to_python/baseball.csv")[['Height', 'Weight', 'Age']].as_matrix()
import numpy as np
__REPLACE_THIS__ = 0
```

*** =sample_code
```{python}
# np_baseball is available

# Import numpy
import numpy as np

# Print mean height (first column)
avg = np.mean(np_baseball[:,0])
print("Average: " + str(avg))

# Print median height
med = __REPLACE_THIS__
print("Median: " + str(med))

# Print out the standard deviation on height
stddev = __REPLACE_THIS__
print("Standard Deviation: " + str(stddev))

# Print out correlation between first and second column
corr = __REPLACE_THIS__
print("Correlation: " + str(corr))
```

*** =solution
```{python}
# np_baseball is available

# Import numpy
import numpy as np

# Print mean height (first column)
avg = np.mean(np_baseball[:,0])
print("Average: " + str(avg))

# Print median height
med = np.median(np_baseball[:,0])
print("Median: " + str(med))

# Print out the standard deviation on height
stddev = np.std(np_baseball[:,0])
print("Standard Deviation: " + str(stddev))

# Print out correlation between first and second column
corr = np.corrcoef(np_baseball[:,0], np_baseball[:,1])
print("Correlation: " + str(corr))
```

*** =sct
```{python}
# sct code
test_import("numpy")

msg = "You don't have to change or edit the predefined variables."
test_object("avg", undefined_msg = msg, incorrect_msg = msg)
test_function("print", 1, not_called_msg = msg, incorrect_msg = msg)

test_object("med", do_eval = False)
test_function("numpy.median", 1, incorrect_msg = "For assigning <code>med</code>, use <code>np.median()</code>. Make sure to pass it the correct column of <code>np_baseball</code>.")
test_object("med")
test_function("print", 2, not_called_msg = msg, incorrect_msg = msg)

test_object("stddev", do_eval = False)
test_function("numpy.std", 1, incorrect_msg = "For assigning <code>stddev</code>, use <code>np.std()</code>. Make sure to pass it the correct column of <code>np_baseball</code>.")
test_object("stddev")
test_function("print", 3, not_called_msg = msg, incorrect_msg = msg)

test_object("corr", do_eval = False)
test_function("numpy.corrcoef", 1, incorrect_msg = "For assigning <code>med</code>, use <code>np.corrcoef()</code>. Make sure to pass it the correct column of <code>np_baseball</code>.")
test_object("corr")
test_function("print", 4, not_called_msg = msg, incorrect_msg = msg)

success_msg("Great! Time to use all of your new data science skills in the last exercise!")
```

--- type:NormalExercise lang:python xp:100 skills:2
## Blend it all together

To wrap up on this chapter, you're going through the entire process: you'll convert regular Python lists to Numpy arrays, combine them into a 2D Numpy array, and generate some summary statistics on them!

Todo vincent, no inspiration for super-awesome example ;-)

*** =instructions
- instruction 1
- instruction 2

*** =hint
hint comes here

*** =pre_exercise_code
```{python}
import numpy as np
```

*** =sample_code
```{python}
# sample code
```

*** =solution
```{python}
# solution code
```

*** =sct
```{python}
# sct code
success_msg("Wonderful! This exercise marks the end of the intro to python for data science course. See you in a later course!")
```


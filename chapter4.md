---
title_meta  : Chapter 4
title       : Numpy
description : Add chapter description here.

--- type:VideoExercise lang:python xp:50 skills:2
## Intro to Numpy

*** =video_link
```{python}
//player.vimeo.com/video/108225030
```

--- type:NormalExercise lang:python xp:100 skills:2
## Your First Numpy Array

In this chapter, we're going to dive into the world of baseball. Along the way, you'll get comfortable with the basics of Numpy, a powerful package to do data science.

A list `baseball` has already been defined in the Python script, representing the height of some baseballers in centimeters. Can you add some code here and there to create a Numpy array from it?

*** =instructions
- Import the `numpy` package as `np`, so that you can refer to `numpy` with `np`.
- Use `np.array()` to create a Numpy array from `baseball`. Name this array `np_baseball`.
- Print out the type of `np_baseball` to check that you got it right.

*** =hint
- `import numpy as np` will do the trick. Now, you have to use `np.fun_name()` whenever you want to use a numpy function.
- `np.array()` should take on input `baseball`. Assign the result of the function call to `np_baseball`.
- To print out the type of a variable `x`, simply type `print(type(x))`.

*** =pre_exercise_code
```{python}
# pec
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
success_msg("Great job!")
```

--- type:NormalExercise lang:python xp:100 skills:2
## Baseballers' height

Being a huge baseball fan, you call the MLB, the Major League of Baseball, and ask around for more statistics on the height of the main players. They pass you along more data on more than a thousand players, which is stored as a regular Python list: `height`. The height is expressed in inches. Can you make a Numpy array out of it, and convert the unit to centimeters?

`height` is already available and the `numpy` package is loaded, so you can start straight away. (Source: [stat.ucla.edu](http://wiki.stat.ucla.edu/socr/index.php/SOCR_Data_MLB_HeightsWeights))

*** =instructions
- Create a Numpy array from `height`. Name this new array `np_height`.
- Print out `np_height`.
- Multiply `np_height` with `2.54` to convert all weight measurements from inches to centimeters. Store the new values in a new array, `np_height_cm`.
- Print out `np_height_cm` and check if the output makes sense.

*** =hint
- Use `np.array()` and pass it `height`. Store the result in `np_height`.
- To print out a variable `x`, simply type `print(x)` in the Python script.
- Perform calculations as if `np_height` is a single number: `np_height * factor` is part of the answer.
- Use `print()` a second time, to print out `np_height_cm` this time.

*** =pre_exercise_code
```{python}
import pandas as pd
mlb = pd.read_csv("https://s3.amazonaws.com/assets.datacamp.com/course/intro_to_python/baseball.csv")
height = mlb['Height'].tolist()
```

*** =sample_code
```{python}
# height is available as a regular list

# Import numpy
import numpy as np

# Create a Numpy array from height: np_height


# Print out np_height


# Convert np_height to feet: np_height_cm


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

# Convert np_height to feet: np_height_cm
np_height_cm = np_height * 2.54

# Print np_height_cm
print(np_height_cm)
```

*** =sct
```{python}
# sct code
success_msg("Nice! In the blink of an eye, Numpy performs multiplications on more than 1000 height measurements.")
```

--- type:NormalExercise lang:python xp:100 skills:2
## Lightweight baseballers

Next to height, the MLB also offers you to analyze their weight data.. Again, both are available as regular Python lists: `height` and `weight`; height is in inches, weight is in pounds.

It's now possible to calculate the BMI of each baseball player. Python code to convert `height` to a Numpy array with the correct units is already available. Follow the instructions step by step and finish the game!

*** =instructions
- Create a Numpy array from the `weights` list with the correct units: multiply with `0.453592` to go from pounds to kilograms. Store the resulting Numpy array as `np_weight_kg`.
- Use `np_height_m` and `np_weight_kg` to calculate the BMI of each player. Use the following equation: $$ \mathrm{BMI} = \frac{\mathrm{weight (kg)}}{\mathrm{height (m)}^2}$$ Save the resulting numpy array as `bmi`.
- Write `print(sum(bmi < 20))` to count the number of baseball players with a low BMI.

*** =hint
- Use a similar approach as the code that calculates `np_height_m`. This time, though, the you have to work with `height` and multiply with `0.453592`.
- To calculate the `bmi`, you will need the `\` and `**` operators.
- Copy the code from the third instruction to the Python script.

*** =pre_exercise_code
```{python}
import pandas as pd
mlb = pd.read_csv("https://s3.amazonaws.com/assets.datacamp.com/course/intro_to_python/baseball.csv")
height = mlb['Height'].tolist()
weight = mlb['Weight'].tolist()
```

*** =sample_code
```{python}
# sample code
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

# Print the number of lightweight baseball players
print(sum(bmi < 20))
```

*** =sct
```{python}
success_msg("Wow! It appears that only 1 of the more than 1000 baseball players has a BMI under 20!")
```

--- type:MultipleChoiceExercise lang:python xp:50 skills:2
## Numpy Side Effects

As Filip explained before, Numpy is great to do vector arithmetic. However, if you compare its functionality with regular Python lists, some things have changed. 

First of all, Numpy arrays cannot contain elements with different types. If you try do try to build such a list, coercion takes place. Next, the typical arithmetic operators, such as `+`, `-`, `*` and `/` have a different meaning for regular Python lists and Numpy arrays.

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
success_msg("replace me")
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
- Subset `np_weights`: print out the element at index 50.
- Print out a sub-array of `np_heights`: It contains the elements at index 100 up to **and including** index 110

*** =hint
- Make sure to wrap a `print()` call around your subsetting operations.
- Use `[100:111]` to get the elements from index 100 up to and including index 110.

*** =pre_exercise_code
```{python}
import pandas as pd
mlb = pd.read_csv("https://s3.amazonaws.com/assets.datacamp.com/course/intro_to_python/baseball.csv")
height = mlb['Height'].tolist()
weight = mlb['Weight'].tolist()
```

*** =sample_code
```{python}
# height and weight are available as a regular lists

# Import numpy
import numpy as np

# Store weight and heights lists as numpy arrays
np_weight = np.array(weight)
np_height = np.array(height)

# Print out the weight at index 50


# Print out sub-array of np_heights: index 100 up to and including index 110

```

*** =solution
```{python}
# height and weight are available as a regular lists

# Import numpy
import numpy as np

# Store weight and heights lists as numpy arrays
np_weight = np.array(weight)
np_height = np.array(height)

# Print out the weight at index 50
print(np_weight[50])

# Print out sub-array of np_heights: index 100 up to and including index 110
print(np_height[100:110])
```

*** =sct
```{python}
# sct code
success_msg("Nice! Time to learn something new: 2D Numpy arrays!")
```

--- type:VideoExercise lang:python xp:50 skills:2
## Numpy 2D array

*** =video_link
```{python}
//player.vimeo.com/video/108225030
```

--- type:NormalExercise lang:python xp:100 skills:2
## Build a 2D Numpy array

Previously, you've worked with the height and weight of Major League Baseball players. Maybe it makes more sense to restructure all this information in a 2D Numpy array, or a matrix if you will. This matrix should have 1015 rows, corresponding to the 1015 baseball players you have information on, and 2 columns, for height and weight.

The MLB was again very helpful and passed you the data in a different structure: as a Python list of lists, where each sublist represents the height and weight of a single baseball player. The name of this embedded list is `baseball`.

Can you store the data as a 2D array to unlock the extra functionality?

*** =instructions
- Use `np.array()` to create a 2D Numpy array from `baseball`. Name this Numpy matrix `np_baseball`.
- Print out the type of `np_baseball`.
- Print out the `shape` attribute of `np_baseball`. Use `.shape`.

*** =hint
- `baseball` is already available in the Python environment. Call `np.array()` on it and store the resulting 2D Numpy array in `np_baseball`.
- Use `print()` in combination with `type()` for the second instruction.
- `np_baseball.shape` will give the dimensions of the `np_baseball`. Make sure to wrap a `print()` call around it.

*** =pre_exercise_code
```{python}
import pandas as pd
baseball = pd.read_csv("~/courses/courses-introduction-to-python/datasets/baseball.csv")[['Height', 'Weight']].as_matrix().tolist()
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
# TO DO VINCENT SCT MAGIC
success_msg("Slick! Time to show off some killer features of multi-dimensional Numpy arrays!")
```

--- type:NormalExercise lang:python xp:100 skills:2
## Subsetting 2D Numpy Array

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

For the regular Python lists, this is a real pain. For 2D Numpy arrays, it's pretty intuitive: the indices before the column refer to the rows, those after the column refer to the columns. The `:` tells Python to include all rows, or all columns, respectively.

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
baseball = pd.read_csv("~/courses/courses-introduction-to-python/datasets/baseball.csv")[['Height', 'Weight']].as_matrix().tolist()
```

*** =sample_code
```{python}
# baseball is available as a regular list of lists

# Import numpy package
import numpy as np

# Create np_baseball (2 cols)
np_baseball = np.array(baseball)

# Print out the 50th row of np_baseball


# Select the entire second colum of np_baseball: np_weight


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
np_baseball[49,:]

# Select the entire second colum of np_baseball: np_weight
np_weight = np_baseball[:,1]

# Print out height of 124th player
np_baseball[123, 1]
```

*** =sct
```{python}
#TODO VINCENT SCT MAGIC
success_msg("This is going well!")
```

--- type:NormalExercise lang:python xp:100 skills:2
## Subsetting 2D Numpy Array (2)

Apart from selecting single elements, entire columns or entire rows from a 2D Numpy array, it's also perfectly possible to create a "sub-matrix" of the matrix you started with. You can do this with slicing. 

As an example, check out the following calls, that builds a 3-by-3 Numpy matrix and then select the lower right 2-by-2 corner from it:

```
import numpy as np
x = [["a", "b", "c"],
     ["d", "e", "f"],
     ["g", "h", "i"]]
np_x = np.array(x)
np_x[1:, 1:]
```

Still remember the principle? The slice is written as `begin:end`: The `begin` is included, the `end` index is not.

The code to build the Numpy matrix `np_baseball` from the `baseball` lists of lists is already included. This time, `np_baseball` contains three columns, corresponding to height, weight and age of the Major Baseball League players. Can you do the correct subsetting operations?

*** =instructions
- Print out the first first and second column of the first ten rows, so row index 0 up to and including row index 9
- Print out a sub-matrix containing all three columns in the row indexes XXX up to __and including__ XXX. These are all the players of the XXX.

*** =hint
- For the first instruction, you can use `[:10, :].
- For the second instruction, you can use XXX.

*** =pre_exercise_code
```{python}
import pandas as pd
baseball = pd.read_csv("~/courses/courses-introduction-to-python/datasets/baseball.csv")[['Height', 'Weight', 'Age']].as_matrix().tolist()
```

*** =sample_code
```{python}
# baseball is available as a regular list of lists

# Import numpy package
import numpy as np

# Create np_baseball (3 cols)
np_baseball = np.array(baseball)

# Print out first and second column of first ten rows


# Print out all three columns for row indexes XXX up to and including XXX

```

*** =solution
```{python}
# baseball is available as a regular list of lists

# Import numpy package
import numpy as np

# Create np_baseball (3 cols)
np_baseball = np.array(baseball)

# Print out first and second column of first ten rows
np_baseball = baseball[:1, :10]

# Print out all three columns for row indexes XXX up to and including XXX
print(baseball[:, XXX:XXX])
```

*** =sct
```{python}
# TODO VINCENT SCT MAGIC
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
- You managed to get hold on updates for weight, height and age of all baseball players. It is available as a Numpy matrix, `update`. Add `np_baseball` and `update` and print out the result.
- You want to convert the units of height and weight. As a first step, create a Numpy array with three values: `0.0254`, `0.453592` and `1`. Name this array `conversion`.
- Multiply `np_baseball` with `conversion` and print out the result.

*** =hint


*** =pre_exercise_code
```{python}
import pandas as pd
import numpy as np
baseball = pd.read_csv("~/courses/courses-introduction-to-python/datasets/baseball.csv")[['Height', 'Weight', 'Age']].as_matrix().tolist()
n = len(baseball)
update = np.column_stack((np.random.normal(1, 0.20, n), 
                          np.random.normal(0, 10, n), 
                          np.ones(n)))
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
success_msg("Great job! Notice how with very little code, you can change all values in your Numpy data structure in a very specific way. This will be very useful in your future as a data scientist!")
```

--- type:VideoExercise lang:python xp:50 skills:2
## Basic Statistics with Numpy

*** =video_link
```{python}
//player.vimeo.com/video/108225030
```

--- type:NormalExercise lang:python xp:100 skills:2
## Average versus median

Assignment comes here. Use Markdown for text formatting.

*** =instructions
- instruction 1
- instruction 2

*** =hint
hint comes here

*** =pre_exercise_code
```{python}
# pec
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
```

--- type:NormalExercise lang:python xp:100 skills:2
## Explore the baseball data

Assignment comes here. Use Markdown for text formatting.

*** =instructions
- instruction 1
- instruction 2

*** =hint
hint comes here

*** =pre_exercise_code
```{python}
# pec
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
```

--- type:NormalExercise lang:python xp:100 skills:2
## Explore the baseball data (2)

Assignment comes here. Use Markdown for text formatting.

*** =instructions
- instruction 1
- instruction 2

*** =hint
hint comes here

*** =pre_exercise_code
```{python}
# pec
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
```


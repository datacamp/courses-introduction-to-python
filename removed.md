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
- Print out the first and second column of the first ten rows, so row index 0 up to and including row index 9
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
print(np_baseball[:2, :10])

# Print out all three columns for row indexes 205 up to and including 235
print(np_baseball[:, 205:236])
```

*** =sct
```{python}
test_import("numpy", same_as = False)

msg = "You don't have to change or remove the predefined variables."
test_object("np_baseball", undefined_msg = msg, incorrect_msg = msg)

test_function("print", 1, incorrect_msg = "For the first printout, subset the `np_baseball` object using `[:2,:10]`. This will select the first and the second column and the first ten rows.")

test_function("print", 2, incorrect_msg = "For the second printout, subset the `np_baseball` object using `[205,236]`. This will select the all columns of row 205 to and including 235.")

success_msg("Great job!")
```

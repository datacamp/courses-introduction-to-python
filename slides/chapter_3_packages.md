---
title: Packages
key: 63b7bc6f2e990ce00a89e5d2960573ec
video_link:
    hls: https://videos.datacamp.com/transcoded/735_intro_to_python/wb1/hls-ch3_3.master.m3u8
    mp4: https://videos.datacamp.com/transcoded_mp4/735_intro_to_python/wb1/ch3_3.mp4

transformations:
    translateX: 55
    translateY: 0
    scale: 0.8

--- type:TitleSlide key:e533c8ca51
## Packages

*** =lower_third
name: Filip Schouwenaars
title: Instructor, DataCamp

*** =script


--- type:FullSlide key:b150c6153c
## Motivation

*** =part1
- Functions and methods are powerful {{1}}
- All code in Python distribution? {{2}}
    - Huge code base: messy {{3}}
    - Lots of code you won’t use {{4}}
    - Maintenance problem {{5}}
*** =script
By now, I hope you're convinced that python functions and methods are extremely powerful: you can basically use other people's code to solve your own problems. However, adding all functions and methods that have been written up to now to the same Python distribution would be a mess. There would be tons and tons of code in there, that you'll never use. Also, maintaining all of this code would be a real pain.


--- type:TwoColumns key:5b7c28bd47
## Packages

*** =part1
- Directory of Python Scripts {{1}}
- Each script = module {{2}}
- Specify functions, methods, types {{3}}
- Thousands of packages available {{4}}
    - NumPy {{5}}
    - Matplotlib {{6}}
    - Scikit-learn {{7}}

*** =part2
```
pkg/
  mod1.py
  mod2.py
  ...
```

*** =script
This is where packages come into play. You can think of package as a directory of Python scripts. Each such script is a so-called module. These modules specify functions, methods and new Python types aimed at solving particular problems. There are thousands of Python packages available from the internet. Among them are packages for data science: there's numpy to efficiently work with arrays, matplotlib for data visualization, scikit-learn for machine learning, and many others.

Not all these packages are available in Python by default. To use Python packages, you'll first have to install them on your system, and then put code in your script to tell Python that you want to use these packages.



--- type:FullSlide key:603d6497cc
## Install package

*** =part1
- [http://pip.readthedocs.org/en/stable/installing/]() {{1}}
- Download `get-pip.py` {{2}}
- Terminal: {{3}}
    - `python3 get-pip.py` {{4}}
    - `pip3 install numpy` {{5}}

*** =script
Datacamp already has all necessary packages installed for you, but if you want to install them on your own system, you'll want to use pip, a package maintenance system for Python. If you go to this URL, you can download the file get-pip.py. Next, you go to the terminal, and execute python3 get-pip.py. Now you can use pip to actually install a Python package of your choosing. Suppose we want to install the numpy package, which you'll learn about in the next chapter. You type pip3 install numpy. You have to use the commands python3 and pip3 here to tell our system that we're working with Python version 3.

--- type:FullSlide key:552acf1454
## Import package

*** =part1
```
In [1]: import numpy
```{{1}}
```
In [2]: array([1, 2, 3])
# NameError: name 'array' is not defined
```{{2}}
```
In [3]: numpy.array([1, 2, 3])
Out[3]: array([1, 2, 3])
```{{3}}
```
In [4]: import numpy as np
``` {{4}}
```
In [5]: np.array([1, 2, 3])
Out[5]: array([1, 2, 3])
```{{5}}
```
In [6]: from numpy import array
```{{6}}
```
In [7]: array([1, 2, 3])
Out[7]: array([1, 2, 3])
```{{7}}

*** =script
Now that the package is installed, you can actually start using it in one of your Python scripts. Before you can do this, you should import the package, or a specific module of the package. You can do this with the import statement.

To import the entire numpy package, you can do import numpy, like this.

A commonly used function in Numpy is array(). It takes a list as input. Simply calling the array function like this, will generate an error.

To refer to the array function from the numpy package, you'll need this:

This time it works. The Numpy array is very useful to do data science, but more on that later.

Using this numpy dot prefix all the time can become pretty tiring, so you can also import the package and refer to it with a different name. You can do this by extending your import statement with as, like this:

Now, instead of numpy.array(), you'll have to use np.array() to use Numpy's array function:

There are cases in which you only need one specific function of a package. Python allows you to make this explicit in your code. Suppose that we only want to use the array() function from the Numpy package. Instead of doing import numpy, you can instead do from numpy import array, like this:

This time, you can simply call the array function like this, no need to use numpy dot here.



--- type:FullSlide key:b5032b9a9d
## `from numpy import array`

*** =part1
**`my_script.py`**
```
from numpy import array

...
``` {{1}}

```
fam = ["liz", 1.73, "emma", 1.68, "mom", 1.71, "dad", 1.89]

...

fam_ext = fam + ["me", 1.79]

...

print(str(len(fam_ext)) + " elements in fam_ext")

...

```

```
np_fam = array(fam_ext)   # using Numpy, but not very clear
``` {{2}}

*** =script

This from import version to use specific parts of a package can be useful to limit the amount of coding, but you're also loosing some of the context. Suppose you're working in a long Python script. You import the array function from numpy at the very top, and way later, you actually use this array function. Somebody else who's reading your code might have forgotten that this array function is a specific Numpy function; it's not clear from the function call.


--- type:FullSlide key:3f2791906c disable_transition:true
## `import numpy`

*** =part1
**`my_script.py`**
```
import numpy

...
``` {{2}}

```
fam = ["liz", 1.73, "emma", 1.68, "mom", 1.71, "dad", 1.89]

...

fam_ext = fam + ["me", 1.79]

...

print(str(len(fam_ext)) + " elements in fam_ext")

...

```

```
np_fam = numpy.array(fam_ext)   # clearly using Numpy
``` {{3}}


*** =script
In that respect, the more standard import numpy call is preferred: In this case, your function call is numpy.array(), making it very clear that you're working with Numpy. At the end of the day, it's a matter of personal preference; up to you to decide what you think is most convenient!



--- type:FinalSlide key:65f8fe6e51
## Let's practice!

*** =script

Off to the exercises now, where you can practice on different ways of importing packages and modules yourself!

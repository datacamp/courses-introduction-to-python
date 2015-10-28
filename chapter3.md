---
title_meta  : Chapter 3
title       : Functions and packages
description : Add chapter description here.

--- type:VideoExercise lang:python xp:50 skills:2
## Functions, what are they?

Begin by explaining that some of basic motivation of functions: you want to do a sequence of commands. Put it in a function! () notation. Some you already used: print(), type() -> make abstraction of some often used sequence of commands. Explain arguments (don't go into detail about keywords and stuff; it's confusing). Some basic python functions: min(), max(), sum(can have 2 arguments!)

*** =video_link
```{python}
//player.vimeo.com/video/108225030
```

--- type:NormalExercise lang:python xp:100 skills:2
## Calling a function

Call print without () -> you don't call the function. Use print() without argument -> prints empty string. Call print with 'Hello World!, it works!'

*** =instructions
- instruction 1
- instruction 2

*** =hint
hint comes here

*** =pre_exercise_code
```{python}
# pec comes here
```

*** =sample_code
```{python}
# sample code comes here
```

*** =solution
```{python}
# Solution code
```

*** =sct
```{python}
# sct code comes here
```


--- type:NormalExercise lang:python xp:100 skills:2
## Need some help

Explain how to use the help() function -> would be nice to point to the online help files here.

*** =instructions
- instruction 1
- instruction 2

*** =hint
hint comes here

*** =pre_exercise_code
```{python}
# pec comes here
```

*** =sample_code
```{python}
# sample code comes here
```

*** =solution
```{python}
# Solution code
```

*** =sct
```{python}
# sct code comes here
```


--- type:NormalExercise lang:python xp:100 skills:2
## List as argument

Given the prices you spend on dinner for the last week. Find the minimum and maximum using built-in functions min and max.

*** =instructions
- instruction 1
- instruction 2

*** =hint
hint comes here

*** =pre_exercise_code
```{python}
# pec comes here
```

*** =sample_code
```{python}
# sample code comes here
```

*** =solution
```{python}
# Solution code
```

*** =sct
```{python}
# sct code comes here
```


--- type:NormalExercise lang:python xp:100 skills:2
## Use two arguments

Given the same list, calculate the total by adding them all and by using sum. You want to start counting from -30, as this is what you spared out last week. Use sum(list, -30)

*** =instructions
- instruction 1
- instruction 2

*** =hint
hint comes here

*** =pre_exercise_code
```{python}
# pec comes here
```

*** =sample_code
```{python}
# sample code comes here
```

*** =solution
```{python}
# Solution code
```

*** =sct
```{python}
# sct code comes here
```


--- type:VideoExercise lang:python xp:50 skills:2
## Packages

A lot of code has been written for python, as it is open source. Don't reinvent the wheel. Solution: Packages!!! Packages contain predefined functions which you can use, written by other people. Some examples: math, numpy, scipy. Import package using import math. Now you can use math.<function>. Explain as and from ... import ... to use functions without math. .

*** =video_link
```{python}
//player.vimeo.com/video/108225030
```

--- type:MultipleChoiceExercise lang:python xp:50 skills:2
## Importing the package

An import statement is given. Which subsequent command will succeed (will not result in an error).

*** =instructions
- option 1
- option 2
- option 3

*** =hint
hint comes here

*** =pre_exercise_code
```{python}
# pec comes here
```

*** =sct
```{python}
test_mc(2) # if 2 is the correct option.
```

--- type:NormalExercise lang:python xp:100 skills:2
## Have some pi

You boasted with your friends about how you know pi until the 10th decimal. However, disaster struck and for the live of you, you can not remember the digits. Luckily, shortly before meeting your friends you have access to a python console. Import math. print(math.pi). Learn first 10 digits.

*** =instructions
- instruction 1
- instruction 2

*** =hint
hint comes here

*** =pre_exercise_code
```{python}
# pec comes here
```

*** =sample_code
```{python}
# sample code comes here
```

*** =solution
```{python}
# Solution code
```

*** =sct
```{python}
# sct code comes here
```


--- type:NormalExercise lang:python xp:100 skills:2
## How far to run

You have to a 30 degrees of a circle-shaped track. The diameter is 100 meters. Use from math import radians.

*** =instructions
- instruction 1
- instruction 2

*** =hint
hint comes here

*** =pre_exercise_code
```{python}
# pec comes here
```

*** =sample_code
```{python}
# sample code comes here
```

*** =solution
```{python}
# Solution code
```

*** =sct
```{python}
# sct code comes here
```


--- type:NormalExercise lang:python xp:100 skills:2
## Math teachers...

Your math teacher wants you to give the sine, cosine AND tangens of 32 degrees. Use import math as m to save some typing time!

*** =instructions
- instruction 1
- instruction 2

*** =hint
hint comes here

*** =pre_exercise_code
```{python}
# pec comes here
```

*** =sample_code
```{python}
# sample code comes here
```

*** =solution
```{python}
# Solution code
```

*** =sct
```{python}
# sct code comes here
```



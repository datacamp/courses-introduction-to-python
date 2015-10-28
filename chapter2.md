---
title_meta  : Chapter 2
title       : Lists
description : Add chapter description here.

--- type:VideoExercise lang:python xp:50 skills:2
## Lists, what are they?

How to create a list and what's the difference with a normal object. What can be contained in a list. Introduce several examples of lists

*** =video_link
```{python}
//player.vimeo.com/video/108225030
```

--- type:MultipleChoiceExercise lang:python xp:50 skills:2
## Which is valid, which isn't?

A few examples of lists are given, the student must select which are valid lists.

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
## Picking up the tab

You're out with friends again, this time for food. This time you want keep track of what you're eating. Your entree was a Caesar Salade which costed 18 dollars, which was healthy. The main dish was ribs for 35 dollars, which was unhealthy. For drinks, you had a coke for 3 dollars, which was unhealthy. Keep them all in seperate variables (no list yet).

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
## Picking up the tab (2)

In the last exercise you had to define a seperate variable for all the things you wanted to keep in your memory. This time put them in a list -> ['Ceasar Salade', 18, True, 'Ribs', 35, False, 'Coke', 3, False]. Use type() on this.

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
## Subsetting a list

You know how to create lists. But what if you want to check the content of one element of the list. Introduce simple subsetting using [..] notation. List start indexing at 0. Negative indexes count from the right. Slices using : (with or without left and right elements: `1:5`, `1:`, `:5`, `:` all valid)

*** =video_link
```{python}
//player.vimeo.com/video/108225030
```

--- type:MultipleChoiceExercise lang:python xp:50 skills:2
## Which element will it return?

A list and an index operation is given; choose which element(s) it will return.

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
## Basic indexing

You are given same list as before (Picking up teh tab (2)). Select the name of the main dish and whether it was healthy. You also want to know the price of the coke (Use right indexing).

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
## Working with elements of the list

Working with the same list. Select the price of the salad and assign it to a variable, same for ribs and cola. Check the types of the assigned variables. Calculate the total cost.

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
## Slicing makes the world go round

Working with the same list. You want to retrieve all information about the main dish [3:6]. All information about the entree [:3]. All information about the coke [6:]. What about [:]?

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
## Manipulate those lists

A great thing about lists is that you can change them. First explain setting using [..] = . Then explain append and remove. Explain how assigning a list to a variable will assign a reference and how to use the copy [:] operator to prevent this. Maybe explain sort()

*** =video_link
```{python}
//player.vimeo.com/video/108225030
```

--- type:NormalExercise lang:python xp:100 skills:2
## Changing elements in the list

Working with dinner list. You remember you put a lot of sauce on the salade, so it was not quite healthy. Change the list using subsetting [..]. Cola was 2.5 instead of 3, use right subsetting this time [-..] = 3. You remember you didn't order a Caesar Salad for 18 dollar as an entree. Instead you ate bacon, which was not healthy and costed 13 dollars. Use slice subsetting and = to change the entree: dinner[:3] = [...]

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
## Appending and removing

You suddenly remember you should remove the main dish from the list, as you didn't really liked it so you didn't eat it. Instead, you ate desert, which you want to append to the end of the list.

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


--- type:MultipleChoiceExercise lang:python xp:50 skills:2
## Deleting splices

You want to delete the entree from the list. What command will you use to do it in a one liner? del(dinner[:3])

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
## Effect of changing the list

Make a new variable which refers to the list dinner_ref = dinner. Change dinner_ref, see what it does. Repeat but now with copy [:].

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
## Sorting the list

Given a list with the prices, sort the list using .sort()

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



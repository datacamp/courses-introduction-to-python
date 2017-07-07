---
title: Subsetting lists
key: 120c081330aef6035a78d74e9ef8ee8c
video_link:
    hls: https://videos.datacamp.com/transcoded/735_intro_to_python/wb1/hls-ch2_2.master.m3u8
    mp4: https://videos.datacamp.com/transcoded_mp4/735_intro_to_python/wb1/ch2_2.mp4

transformations:
    translateX: 55
    translateY: 0
    scale: 0.8

--- type:TitleSlide key:1873fd5ad9
## Subsetting lists


*** =lower_third
name: Filip Schouwenaars
title: Instructor, DataCamp

*** =script
After you've created your very own Python list, you might wonder how you can access information in the list. 




--- type:FullSlide key:b8ba447581
## Subsetting Lists

*** =part1
```
In [1]: fam = ["liz", 1.73, "emma", 1.68, "mom", 1.71, "dad", 1.89]

In [2]: fam
Out[2]: ['liz', 1.73, 'emma', 1.68, 'mom', 1.71, 'dad', 1.89]
```
```
#          0      1      2      3     4     5      6      7
```{{1}}
```
#         -8     -7     -6     -5    -4    -3     -2     -1
 
```{{4}}

```
In [3]: fam[3]
Out[3]: 1.68
```{{2}}
```
In [4]: fam[6]
Out[4]: 'dad'
```{{3}}
```
In [5]: fam[-1]
Out[5]: 1.89
```{{5}}
```
In [6]: fam[-2]
Out[6]: 'dad'
```{{6}}

*** =script
Python uses the index to do this. Have a look at fam again here. The first element in the list has index 0, the second element has index 1, and so on. Suppose that you want to select the height of emma, the float 1.68. It's the fourth element, so it has index 3. To select it, you use 3 inside square brackets:

Similarly, to select the string "dad" from the list, which is the sevent element in the list, you'll need to put the index 6 inside square brackets:

You can also count backwards, using negative indexes. This is useful if you want to get some elements at the end of your list. To get your dad's height, for example, you'll need the index -1. These are the negative indexes for all list elements.

This means that this line and this line, return the same result:




--- type:FullSlide key:137290f1dc
## List Slicing

*** =part1
```
In [7]: fam
Out[7]: ['liz', 1.73, 'emma', 1.68, 'mom', 1.71, 'dad', 1.89]
#          0      1      2      3     4     5      6      7
```

```
In [8]: fam[3:5]
Out[8]: [1.68, 'mom']
```{{1}}

`[start : end]` $\rightarrow$ [inclusive : exclusive] {{2}}


*** =script
Apart from indexing, there's also something called slicing, which allows you to select multiple elements from a list, thus creating a new list. You can do this by specifying a range, using a colon. Let's first have another look at the list, and then try this piece of code:

Can you guess what it'll return? A list with the the float 1.68, the string "mom", and the float 1.71, corresponding to the 4th, 5th and 6th element in the list maybe? Let's see what the output is.

Apparently, only the elements with index 3 and 4, get returned. The element with index 5 is not included. In general, this is the syntax: the index you specify before the colon, so where the slice starts, is included, while the index you specify after the colon, where the slice ends, is not.




--- type:FullSlide key:446ace9bcb
## List Slicing

*** =part1
```
In [7]: fam
Out[7]: ['liz', 1.73, 'emma', 1.68, 'mom', 1.71, 'dad', 1.89]
#          0      1      2      3     4     5      6      7

In [8]: fam[3:5]
Out[8]: [1.68, 'mom']
```
```
In [9]: fam[1:4]
Out[9]: [1.73, 'emma', 1.68]
``` {{1}}
```
In [10]: fam[:4]
Out[10]: ['liz', 1.73, 'emma', 1.68]
``` {{2}}
```
In [11]: fam[5:]
Out[11]: [1.71, 'dad', 1.89]
``` {{3}}


*** =script

With this in mind, can you tell what this call will return?

You probably guessed correctly that this call gives you a list with three elements, corresponding to the elements with index 1, 2 and 3 of the fam list.

You can also choose to just leave out the index before or after the colon. If you leave out the index where the slice should begin, you're telling Python to start the slice from index 0, like this example.

If you leave out the index where the slice should end, you include all elements up to and including the last element in the list, like here:


--- type:FinalSlide key:ea0bf3fb83
## Let's practice!

*** =script
Now it's time to head over to the exercises, where you will continue to work on the list you've created yourself before. You'll use different subsetting methods to get exactly the piece of information you need!
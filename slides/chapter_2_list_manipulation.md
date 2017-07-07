---
title: List Manipulation
key: 4d710eb071441989e00e5133eb18af06
video_link:
    hls: https://videos.datacamp.com/transcoded/735_intro_to_python/wb1/hls-ch2_3.master.m3u8
    mp4: https://videos.datacamp.com/transcoded_mp4/735_intro_to_python/wb1/ch2_3.mp4

transformations:
    translateX: 55
    translateY: 0
    scale: 0.8

--- type:TitleSlide key:b159d80fb3
## List Manipulation


*** =lower_third
name: Filip Schouwenaars
title: Instructor, DataCamp

*** =script
After creation and subsetting, the final piece of the Python lists puzzle is manipulation




--- type:FullSlide key:c7036234ef
## List Manipulation

*** =part1
- Change list elements
- Add list elements
- Remove list elements

*** =script
so ways to change elements in your list, or to add elements to and remove elements from your list.




--- type:FullSlide key:fefde9787e
## Changing list elements

*** =part1
```
In [1]: fam = ["liz", 1.73, "emma", 1.68, "mom", 1.71, "dad", 1.89]

In [2]: fam
Out[2]: ['liz', 1.73, 'emma', 1.68, 'mom', 1.71, 'dad', 1.89]
```{{1}}
```
In [3]: fam[7] = 1.86
```{{2}}
```
In [4]: fam
Out[4]: ['liz', 1.73, 'emma', 1.68, 'mom', 1.71, 'dad', 1.86]
```{{3}}
```
In [5]: fam[0:2] = ["lisa", 1.74]
```{{4}}
```
In [6]: fam
Out[6]: ['lisa', 1.74, 'emma', 1.68, 'mom', 1.71, 'dad', 1.86]
``` {{5}}

*** =script
Changing list elements is pretty straightforward. You use the same square brackets that we've used to subset lists, and then assign new elements to it using the equals sign. Suppose that after another look at fam, you realize that your dad's height is not up to date anymore as he's shrinking with age. Instead of 1.89 meters, it should be 1.86 meters. To change this list element, which is at index 7, you can use this line:

If you now check out fam, you'll see that the value is updated:

You can even change an entire list slice at once. To change the elements "liz" and 1.73, you access the first two elements with zero colon 2, and then assign a new list to it.




--- type:FullSlide key:47816cc981
## Adding and removing elements

*** =part1
```
In [7]: fam + ["me", 1.79]
Out[7]: ['lisa', 1.74,'emma', 1.68, 'mom', 1.71, 'dad', 1.86, 'me', 1.79]
```{{1}}
```
In [8]: fam_ext = fam + ["me", 1.79]
```{{2}}
```
In [9]: del(fam[2])
```{{3}}
```
In [10]: fam
Out[10]: ['lisa', 1.74, 1.68, 'mom', 1.71, 'dad', 1.86]
```{{4}}
```
In [11]: del(fam[2])
```{{5}}
```
In [12]: fam
Out[12]: ['lisa', 1.74, 'mom', 1.71, 'dad', 1.86]
``` {{6}}

*** =script
Do you still remember how the plus operator was different for strings and integers? Well, it's again different for lists. If you use the plus sign with two lists, Python simply pastes together their contents in a single list. Suppose you want to add your own name and height to the fam height list. This will do the trick:

Of course, you can also store this new list in a variable, fam_ext for example.

Finally, deleting elements from a list is also pretty straightforward, you'll have to use del here. Take this line, for example, that deletes the element with index 2, so "emma", from the list:

If you check out fam now, you'll see that the "emma" string is gone now. Because you've removed an index, all elements that came after "emma" scooted over by one index. If you again run the same line, you're again removing the element at index 2, which is emma's height, 1.68 centimeters:



--- type:TwoColumns key:578f3c304f
## Behind the scenes (1)

*** =part1
```
In [13]: x = ["a", "b", "c"]
``` {{1}}
```
In [14]: y = x
``` {{2}}
```
In [15]: y[1] = "z"

In [16]: y
Out[16]: ['a', 'z', 'c']
``` {{4}}
```
In [17]: x
Out[17]: ['a', 'z', 'c']
``` {{5}}

*** =part2
![](https://s3.amazonaws.com/assets.datacamp.com/production/course_4550/datasets/bts_1.png) {{3}}

*** =script
Understanding how Python lists actually work behind the scenes becomes pretty important now. What actually happens when you create a new list, x, like this?

Well, in a simplified sense, you're storing a list in your computer memory, and store the 'address' of that list, so where the list is in your computer memory, in x. This means that x does not actually contain all the list elements, it rather contains a reference to the list. For basic operations, the difference is not that important, but it becomes more so when you start copying lists. Let me clarify this with an example.


--- type:TwoColumns key:523178f788 disable_transition:true
## Behind the scenes (1)

*** =part1
```
In [13]: x = ["a", "b", "c"]
```
```
In [14]: y = x
```
```
In [15]: y[1] = "z"

In [16]: y
Out[16]: ['a', 'z', 'c']
```
```
In [17]: x
Out[17]: ['a', 'z', 'c']
```


*** =part2
![](https://s3.amazonaws.com/assets.datacamp.com/production/course_4550/datasets/bts_2.png)

*** =script
Let's store the list x as a new variable y, by simply using the equals sign:

Let's now change the element with index one in the list y, as follows:

The funky thing is that if you now check out x again, also here the second element was changed:
That's because when you copied x to y with the equals sign, you copied the reference to the list, not the actual values themselves.

--- type:TwoColumns key:15d1cad937 disable_transition:true
## Behind the scenes (1)

*** =part1
```
In [13]: x = ["a", "b", "c"]
```
```
In [14]: y = x
```
```
In [15]: y[1] = "z"

In [16]: y
Out[16]: ['a', 'z', 'c']
```
```
In [17]: x
Out[17]: ['a', 'z', 'c']
```


*** =part2
![](https://s3.amazonaws.com/assets.datacamp.com/production/course_4550/datasets/bts_3.png)

*** =script
 When you're updating an element the list, though, it's one and the same list in the computer memory your changing. Both x and y point to this list, so the update is visible from both.


--- type:TwoColumns key:078a21eebd
## Behind the scenes (2)

*** =part1
```
In [18]: x = ["a", "b", "c"]
```
```
In [19]: y = list(x)
``` {{1}}
```
In [20]: y = x[:]
``` {{2}}

*** =part2
![](https://s3.amazonaws.com/assets.datacamp.com/production/course_4550/datasets/bts_4.png)

*** =script
If you want to create a list y that points to a new list in the memory with the same variables, you'll need to use something else than the equals sign. You can use the list() function, like this, or use slicing to select all list elements explicitly.


--- type:TwoColumns key:14bd730c77 disable_transition:true
## Behind the scenes (2)

*** =part1
```
In [18]: x = ["a", "b", "c"]
```
```
In [19]: y = list(x)
``` 
```
In [20]: y = x[:]
``` 

*** =part2
![](https://s3.amazonaws.com/assets.datacamp.com/production/course_4550/datasets/bts_5.png)

*** =script



--- type:TwoColumns key:46617c838b disable_transition:true
## Behind the scenes (2)

*** =part1
```
In [18]: x = ["a", "b", "c"]
```
```
In [19]: y = list(x)
``` 
```
In [20]: y = x[:]
``` 
```
In [21]: y[1] = "z"
```
```
In [22]: x
Out[22]: ['a', 'b', 'c']
``` {{1}}

*** =part2
![](https://s3.amazonaws.com/assets.datacamp.com/production/course_4550/datasets/bts_6.png)

*** =script
If you now make a change to the list y points to, x is not affected:


--- type:FinalSlide key:885d8936f4
## Let's practice!

*** =script
If this was a bit too much to take in, don't worry. The exercises will help you understand list manipulation and the subtle inner workings of lists. I'm sure you'll do great!
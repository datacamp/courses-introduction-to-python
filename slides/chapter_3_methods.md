---
title: Methods
key: 8e3b3ba9da59b2e27e08ead291826bee
video_link:
    hls: https://videos.datacamp.com/transcoded/735_intro_to_python/wb1/hls-ch3_2.master.m3u8
    mp4: https://videos.datacamp.com/transcoded_mp4/735_intro_to_python/wb1/ch3_2.mp4

transformations:
    translateX: 55
    translateY: 0
    scale: 0.8

--- type:TitleSlide key:49b518a699
## Methods

*** =lower_third
name: Filip Schouwenaars
title: Instructor, DataCamp

*** =script
Built-in functions are only one part of the Python story.

--- type:FullSlide key:25d2f5cc61
## Built-in Functions

*** =part1
- Maximum of list: `max()` {{1}}
- Length of list or string: `len()` {{2}}
- Get index in list: ? {{3}}
- Reversing a list: ? {{4}}

*** =script
You already know about functions such as max(), to get the maximum of a list, len(), to get the length of a list or a string, and so on. But what about other basic things, such getting the index of a specific element in the list, or reversing a list? You can look very hard for built-in functions that do this, but you won't find them.



--- type:TwoRowsTwoColumns key:114ce97242 disable_transition:true

## Back 2 Basics

*** =part1
**`str`** {{1}} 
```
In [1]: sister = "liz"
``` 
- `captialize()`, `replace()` {{5}}

*** =part3
**`float`** {{2}}
```
In [2]: height = 1.73
```
- `bit_length()`, `conjugate()` {{6}}

*** =part2
**`list`** {{3}}
```
In [3]: fam = ["liz", 1.73, 
                "emma", 1.68, 
                "mom", 1.71, 
                "dad", 1.89]
```
- `index()`, `count()` {{7}}

*** =part4
Methods - {{4}}

functions that belong to objects {{4}}

*** =script

In the past exercises, you've already created a bunch of variables. Among other Python types, you've created strings, floats and lists, like the ones you see here. Each one of these values or data structures are so-called Python object. This string is an object, this float is an object, but this list is also an object. These objects have a specific type, that you already know: string, float, and list, and of course they represent the values you gave them, such as "liz", 1.73 and an entire list. But next to that, Python objects also come with a bunch of so-called "methods". You can think of methods as functions that "belong to" Python objects. A Python object of type string has methods, such as capitalize and replace, but also objects of type float and list have specific methods depending on the type.


--- type:FullSlide key:f34fd32397
## `list` methods

*** =part1
```
In [4]: fam
Out[4]: ['liz', 1.73, 'emma', 1.68, 'mom', 1.71, 'dad', 1.89]
```{{1}}

```
In [5]: fam.index("mom")   # "call method index() on fam"
Out[5]: 4
```{{2}}

```
In [6]: fam.count(1.73)
Out[6]: 1
```{{3}}


*** =script
Enough for the theory now; let's try to use a method! Suppose you want to get the index of the string "mom" in the fam list. fam is an Python object with the type list, and has a method named index(). To call the method, you use the dot notation, like this. The only input is the string "mom", the element you want to get the index for.

Python returns 4, which indeed is the index of the string "mom". I called the index() method "on" the fam list here, and the output was 4. Similarly, I can use the count() method on the fam list to count the number of times 1.73 occurs in the list:

Python gives me 1, which makes sense, because only liz is 1.73 meters tall.



--- type:FullSlide key:01b6604112
## `str` methods

*** =part1
```
In [7]: sister
Out[7]: 'liz'
```{{1}}

```
In [8]: sister.capitalize()
Out[8]: 'Liz'
```{{2}}

```
In [9]: sister.replace("z", "sa")
Out[9]: 'lisa'
```{{3}}

*** =script
But lists are not the only Python objects that have methods associated. Also floats, integers, booleans and strings are Python objects that have specific methods associated. Take the variable sister for example, that represents a string.

You can call the method capitalize() on sister, without any inputs. It returns a string where the first letter is capitalized now:

Or what if you want to replace some parts of the string with other parts: not a problem. Just call the method replace on sister, with two appropriate inputs:

In the output, "z" is replaced with "sa".



--- type:FullSlide key:03177cf5d7
## Methods

*** =part1
- Everything = object {{1}}
- Object have methods associated, depending on type {{2}}

```
In [10]: sister.replace("z", "sa")
Out[10]: 'lisa'
``` {{3}}
```
In [11]: fam.replace("mom", "mommy")
# AttributeError: 'list' object has no attribute 'replace'
``` {{4}}
```
In [12]: sister.index("z")
Out[12]: 2
``` {{5}}
```
In [13]: fam.index("mom")
Out[13]: 4
```{{6}}

*** =script
I guess it's clear by now: in Python, everything is an object, and each object has specific methods associated. Depending on the type of the object, list, string, float, whatever, the available methods are different. A string object like sister has a replace method, but a list like fam doesn't have this, as you can see from this error. Objects of different types can have methods with the same name: Take the index() method. It's available for both strings and lists. If you call it on a string, you get the index of the letters in the string; If you call it on a list, you get the index of the element in the list. This means that, depending on the type of the object, the methods behave differently.



--- type:FullSlide key:2faed3554b
## Methods (2)

*** =part1
```
In [14]: fam
Out[14]: ['liz', 1.73, 'emma', 1.68, 'mom', 1.71, 'dad', 1.89]
```{{1}}
```
In [15]: fam.append("me")
``` {{2}}
```
In [16]: fam
Out[16]: ['liz', 1.73, 'emma', 1.68, 'mom', 1.71, 'dad', 1.89, 'me']
```{{3}}
```
In [17]: fam.append(1.79)
```{{4}}
```
In [18]: fam
Out[18]: ['liz', 1.73, 'emma', 1.68, 'mom', 1.71, 'dad', 1.89, 'me', 1.79]
```{{5}}

*** =script
Before I unleash you on some exercises on methods, there's one more thing I want to tell you. Some methods can change the objects they are called on. Let's retake the fam list, and call the append() method on it. As the input, we pass a string we want to add to the list:

Python doesn't generate an output, but if we check the fam list again, we see that it has been extended with the string "me":

Let's do this again, this time to add my length to the list:

Again, the fam list was extended:

This is pretty cool, because you can write very concise code to update your data structures on the fly, but it can also be pretty dangerous. Some method calls don't change the object they're called on, while others do, so watch out.



--- type:FullSlide key:725cc25c37
## Summary

*** =part1
Functions {{1}}
```
In [11]: type(fam)
Out[11]: list
``` {{2}}

Methods: call functions *on* objects {{3}}
```
In [12]: fam.index("dad")
Out[12]: 6
``` {{4}}

*** =script
Let's take a step back here and summarise this. you have Python functions, like type(), max() and round(), that you can call like this: There's also methods, which are functions that are specific to Python objects. Depending on the type of the Python object you're dealing with, you'll be able to use different methods and they behave differently. You can call methods on the objects with the dot notation, like this for example.

There's much more to tell about Python objects, methods and how Python works internally, but for now, let's stick to what I've talked about here. 


--- type:FinalSlide key:f7b566d5a8
## Let's practice!

*** =script
It's time to get some exercises and add methods to your evergrowing skillset!


---
title: Insert title here
key: 433dcfcfedaee070cbf440491c402e3b
video_link:
  mp4: >-
    https://s3.amazonaws.com/videos.datacamp.com/raw/735_intro_to_python/v6/735_ch1_2.mp4
  hls: >-
    https://s3.amazonaws.com/videos.datacamp.com/transcoded/735_intro_to_python/v6/hls-735_ch1_2.master.m3u8
transformations:
  translateX: 50
  translateY: 0
  scale: 1
---

## Variables and Types

```yaml
type: TitleSlide
key: dc8b62f1c8
```

`@lower_third`
name: Hugo Bowne-Anderson
title: Data Scientist at DataCamp

`@script`
Well done and welcome back! It's clear that Python is a great calculator. If you want to do more complex calculations though, you will want to "save" values while you're coding along.

---

## Variable

```yaml
type: FullSlide
key: 36ec318b41
```

`@part1`
- Specific, case-sensitive name

- Call up value through variable name{{1}}

- 1.79 m - 68.7 kg{{2}}

```py
height = 1.79
weight = 68.7
```{{3}}
```py
height
```{{4}}

```out
1.79
```{{4}}

`@script`
You can do this by defining a variable, with a specific, case-sensitive name. Once you create (or declare) such a variable, you can later call up its value by typing the variable name.

Suppose you measure your height and weight, in metric units: you are 1-point-79 meters tall, and weigh 68-point-7 kilograms. You can assign these values to two variables, named height and weight, with an equals sign:

If you now type the name of the variable, height,

Python looks for the variable name, retrieves its value, and prints it out.

---

## Calculate BMI

```yaml
type: TwoColumns
key: fe1b10a93b
code_zoom: 80
```

`@part1`
```py
height = 1.79
weight = 68.7
```
```py
height
```

```out
1.79
```

$$ \text{BMI} = \frac{\text{weight}}{\text{height}^2} $${{1}}

`@part2`
```py
68.7 / 1.79 ** 2
```{{2}}

```out
21.4413
```{{2}}

```py
weight / height ** 2
```{{3}}

```out
21.4413
```{{3}}

```py
bmi = weight / height ** 2
bmi
```{{4}}

```out
21.4413
```{{4}}

`@script`
Let's now calculate the Body Mass Index, or BMI, which is calculated as follows, with weight in kilograms and height in meters. You can do this with the actual values, but you can just as well use the variables height and weight, like in here. Every time you type the variable's name, you are asking Python to change it with the actual value of the variable. weight corresponds to 68-point-7, and height to 1-point-79.

Finally, this version has Python store the result in a new variable, bmi. bmi now contains the same value as the one you calculated earlier.

In Python, variables are used all the time. They help to make your code reproducible.

---

## Reproducibility

```yaml
type: FullSlide
key: 9980f47f9d
```

`@part1`
```py
height = 1.79
weight = 68.7
bmi = weight / height ** 2
print(bmi)
```

```out
21.4413
```

`@script`
Suppose the code to create the height, weight and bmi variable are in a script, like this. If you now want to recalculate the bmi for another weight,

---

## Reproducibility

```yaml
type: FullSlide
key: a4e899f00f
disable_transition: true
```

`@part1`
```py
height = 1.79
weight = 74.2 # <-
bmi = weight / height ** 2
print(bmi)
```

```out
23.1578
```

`@script`
you can simply change the declaration of the weight variable, and rerun the script. The bmi changes accordingly, because the value of the variable weight has changed as well.

So far, we've only worked with numerical values, such as height and weight.

---

## Python Types

```yaml
type: FullSlide
key: 9d86084ad4
```

`@part1`
```py
type(bmi)
```{{1}}

```out
float
```{{1}}

```py
day_of_week = 5
type(day_of_week)
```{{2}}

```out
int
```{{2}}

`@script`
In Python, these numbers all have a specific type. You can check out the type of a value with the type function. To see the type of our bmi value, simply write type and then bmi inside parentheses. You can see that it's a float, which is python's way of representing a real number, so a number which can have both an integer part and a fractional part. Python also has a type for integers: int, like this example.

To do data science, you'll need more than ints and floats, though.

---

## Python Types (2)

```yaml
type: FullSlide
key: d971d34e6a
```

`@part1`
```py
x = "body mass index"
y = 'this works too'
```{{1}}
```py
type(y)
```{{2}}

```out
str
```{{2}}

```py
z = True
type(z)
```{{3}}

```out
bool
```{{3}}

`@script`
Python features tons of other data types. The most common ones are strings and booleans.

A string is Python's way to represent text. You can use both double and single quotes to build a string, as you can see from these examples. If you print the type of the last variable here, you see that it's str, short for string.

The Boolean is a type that can either be True or False. You can think of it as 'Yes' and 'No' in everyday language. Booleans will be very useful in the future, to perform filtering operations on your data for example.

There's something special about Python data types.

---

## Python Types (3)

```yaml
type: FullSlide
key: 24601e2af0
```

`@part1`
```py
2 + 3
```{{1}}

```out
5
```{{1}}

```py
'ab' + 'cd'
```{{2}}

```out
'abcd'
```{{2}}

- Different type = different behavior!{{3}}

`@script`
Have a look at this line of code, that sums two integers, and then this line of code, that sums two strings.

For the integers, the values were summed, while for the strings, the strings were pasted together. The plus operator behaved differently for different data types. This is a general principle: how the code behaves depends on the types you're working with.

In the exercises that follow, you'll create your first variables and experiment with some of Python's data types. I'll see you in the next video to explain all about lists.

---

## Let's practice!

```yaml
type: FinalSlide
key: b7fc40db4d
```

`@script`
Let's get you coding and I can't wait to see you in the next chapter where you'll build even more awesome python charts.

---
title: 'Insert title here'
key: d8fcd4c930027fa4e1c3870c7e7e0ff1
video_link:
    mp4: 'https://s3.amazonaws.com/videos.datacamp.com/raw/735_intro_to_python/v6/735_ch1_1.mp4'
    hls: 'https://s3.amazonaws.com/videos.datacamp.com/transcoded/735_intro_to_python/v6/hls-735_ch1_1.master.m3u8'
transformations:
    translateX: 50
    translateY: 0
    scale: 1
---

## Hello Python!

```yaml
type: TitleSlide
key: f743ca8c41
```

`@lower_third`
name: Hugo Bowne-Anderson
title: Data Scientist at DataCamp

`@script`
Hi, my name is Hugo and I'll be your host for Introduction to Python for Data Science.

I'm a data scientist and educator at DataCamp and host of the DataFramed podcast, which you must check out.

---

## How you will learn

```yaml
type: FullSlide
key: 30ee08a725
disable_transition: true
```

`@part1`
![im1.png](https://assets.datacamp.com/production/repositories/288/datasets/855eb1b4bc76c5adc2372bbd2f1575d1b75079cc/im1.png)

![v2_im1.png](https://assets.datacamp.com/production/repositories/288/datasets/b05b2904f73909da21b2f22652ce114d196f7041/v2_im1.png)

`@script`
In this course,

---

## How you will learn

```yaml
type: FullSlide
key: a093f0b659
disable_transition: true
```

`@part1`
![v2_im2.png](https://assets.datacamp.com/production/repositories/288/datasets/3abe63cb44314a94f7ee62f65caa19074edd31ab/v2_im2.png)

`@script`
you will learn Python for Data Science through video lessons,

---

## How you will learn

```yaml
type: FullSlide
key: cff110c262
disable_transition: true
```

`@part1`
![v2_im3.png](https://assets.datacamp.com/production/repositories/288/datasets/d0e58c2a475062673219e4200a6e962001e35f71/v2_im3.png)

`@script`
like this one, and interactive exercises.

---

## How you will learn

```yaml
type: FullSlide
key: 42962f0d17
disable_transition: true
```

`@part1`
![v2_im4.png](https://assets.datacamp.com/production/repositories/288/datasets/f0b0039d206746083f06e16f6d1adb99b6cbb087/v2_im4.png)

`@script`
You get your own Python session where you can experiment and

---

## How you will learn

```yaml
type: FullSlide
key: 3262829f32
disable_transition: true
```

`@part1`
![v2_im5.png](https://assets.datacamp.com/production/repositories/288/datasets/fcd1643b0f3a9d8cbe3139dd277e31f153ca887d/v2_im5.png)

`@script`
try to come up with the correct code to solve the instructions.

---

## How you will learn

```yaml
type: FullSlide
key: fde7ff1ea9
disable_transition: true
```

`@part1`
![v2_im6.png](https://assets.datacamp.com/production/repositories/288/datasets/33849bdc917d30124a9935842898ffef158c77a2/v2_im6.png)

`@script`
You're learning by doing,

---

## How you will learn

```yaml
type: FullSlide
key: c9dd1edd75
disable_transition: true
```

`@part1`
![v2_im7.png](https://assets.datacamp.com/production/repositories/288/datasets/1afe1c43d1a7277fa333637266fdb36630723462/v2_im7.png)

`@script`
while receiving customized

---

## How you will learn

```yaml
type: FullSlide
key: b6b5c151b9
disable_transition: true
```

`@part1`
![v2_im8.png](https://assets.datacamp.com/production/repositories/288/datasets/7871bfa81d5f84bf56e1d89c20bdfab86beb3f89/v2_im8.png)

`@script`
and instant feedback on your work.

---

## Python

```yaml
type: TwoColumns
key: 3f23b93572
```

`@part1`
- Guido Van Rossum{{1}}

- General Purpose: build anything{{3}}

- Open Source! Free!{{4}}

- Python Packages, also for Data Science{{5}}

	- Many applications and fields{{6}}

- Version 3.x - https://www.python.org/downloads/{{7}}

`@part2`
![guido-hba.png](https://assets.datacamp.com/production/repositories/288/datasets/fb3e4b8dc114529dafffb37d33f2b2244210d40f/guido-hba.png){{2}}

`@script`
Python was conceived by Guido Van Rossum. Here, you can see a photo of me with Guido. What started as a hobby project, soon became a general purpose programming language: nowadays, you can use Python to build practically any piece of software. But how did this happen? Well, first of all, Python is open source. It's free to use. Second, it's very easy to build packages in Python, which is code that you can share with other people to solve specific problems. Throughout time, more and more of these packages specifically built for data science have been developed. Suppose you want to make some fancy visualizations of your company's sales. There's a package for that. Or what about connecting to a database to analyze sensor measurements? There's also a package for that.
People often refer to python as the swiss army knife of programming languages as you can do almost anything with it.
In this course, we'll start to build up your data science coding skills bit by bit, so make sure to stick around to see how powerful the language can be.

Currently, there are two common versions of Python, version 2-point-7 and 3-point-5 and later. Apart from some syntactical differences, they are pretty similar, but as support for version 2 will fade over time, our courses focus on Python 3. To install Python 3 on your own system, follow the steps at this URL.

---

## IPython Shell

```yaml
type: FullSlide
key: 43a91a7217
```

`@part1`
Execute Python commands

![im_interface.png](https://assets.datacamp.com/production/repositories/288/datasets/baae2c2c02551284c4253583b4396307b3561a15/im_interface.png)

`@script`
Now that you're all eyes and ears for Python, let's start experimenting. I'll start with the Python shell, a place where you can type Python code and immediately see the results. In DataCamp's exercise interface, this shell is embedded here.

---

## IPython Shell

```yaml
type: FullSlide
key: 524e4c20a7
disable_transition: true
```

`@part1`
![v2_im_1.png](https://assets.datacamp.com/production/repositories/288/datasets/92b564ad29678d3f128399ceed9cde4350c7a885/v2_im_1.png)

`@script`
Let's start off simple and use Python as a calculator. Let me type 4 + 5

---

## IPython Shell

```yaml
type: FullSlide
key: a4f0f4cf69
disable_transition: true
```

`@part1`
![v2_im_2.png](https://assets.datacamp.com/production/repositories/288/datasets/70799d49563b79a8709b2edb325462760a22d204/v2_im_2.png)

`@script`
and hit Enter.

---

## IPython Shell

```yaml
type: FullSlide
key: b1718925d8
disable_transition: true
```

`@part1`
![im_3.png](https://assets.datacamp.com/production/repositories/288/datasets/17e1bf08fd2111fe2fd0f2c31ad2b505b1198461/im_3.png)

![v2_im_3.png](https://assets.datacamp.com/production/repositories/288/datasets/61055aa5adf6d3181fa46274f74059d42e1bea91/v2_im_3.png)

`@script`
Python interprets what you typed and prints the result of your calculation, 9. The Python shell that's used here is actually not the original one; we're using IPython, short for Interactive Python, which is some kind of juiced up version of regular Python that'll be useful later on.

IPython was created by Fernando Pérez and is part of the broader Jupyter ecosystem. Apart from interactively working with Python, you can also have Python run so called

---

## Python Script

```yaml
type: FullSlide
key: 78ef256bc0
```

`@part1`
- Text Files - .py{{1}}

- List of Python Commands{{2}}

- Similar to typing in IPython Shell{{3}}

`@script`
python scripts. These python scripts are simply text files with the extension (dot) py. It's basically a list of Python commands that are executed, almost as if you where typing the commands in the shell yourself, line by line. Let's put the command from before in a script now,

---

## Python Script

```yaml
type: FullSlide
key: 719d500511
```

`@part1`
![v2_im_2.png](https://assets.datacamp.com/production/repositories/288/datasets/70799d49563b79a8709b2edb325462760a22d204/v2_im_2.png)

`@script`
that can be found here in DataCamp's interface.

---

## Python Script

```yaml
type: FullSlide
key: 717d124175
disable_transition: true
```

`@part1`
![v2_im_4.png](https://assets.datacamp.com/production/repositories/288/datasets/02376d8fcd175c8fef1e16c65688e385ebca68ea/v2_im_4.png)

`@script`
The next step is executing the script, by clicking 'Submit Answer'.

---

## Python Script

```yaml
type: FullSlide
key: 373fd0a03d
disable_transition: true
```

`@part1`
![v2_im_5.png](https://assets.datacamp.com/production/repositories/288/datasets/719ede3350f29b3a159f3c63c325657589874537/v2_im_5.png)

`@script`
If you execute this script in the DataCamp interface, there's nothing in the output pane. That's because you have to explicitly use print inside scripts if you want to generate output during execution. Let's wrap our previous calculation in a print call,

---

## Python Script

```yaml
type: FullSlide
key: c7a9d02fb6
disable_transition: true
```

`@part1`
![v2_im_6.png](https://assets.datacamp.com/production/repositories/288/datasets/730a523d51d9d67476a0d0f139a8024fcbc29ce8/v2_im_6.png)

`@script`
and rerun the script.

---

## Python Script

```yaml
type: FullSlide
key: 65dc2d6b9c
disable_transition: true
```

`@part1`
![v2_im_7.png](https://assets.datacamp.com/production/repositories/288/datasets/d91c419b565eaa2626b69b2ddad7c68e5438dd48/v2_im_7.png)

`@script`
This time, the same output as before is generated, great! Putting your code in Python scripts instead of manually retyping every step interactively will help you to keep structure and avoid retyping everything over and over again if you want to make a change; you simply make the change in the script, and rerun the entire thing.

---

## DataCamp Interface

```yaml
type: FullSlide
key: 693ba1cd14
```

`@part1`
![im_interface.png](https://assets.datacamp.com/production/repositories/288/datasets/baae2c2c02551284c4253583b4396307b3561a15/im_interface.png)

`@script`
Now that you've got an idea about different ways of working with Python, I suggest you head over to the exercises. Use the IPython Shell for experimentation, and use the Python script editor to code the actual answer. If you click Submit Answer, your script will be executed and checked for correctness.

---

## Let's practice!

```yaml
type: FinalSlide
key: 7445cd202e
```

`@script`
Get coding and don't forget to have fun!

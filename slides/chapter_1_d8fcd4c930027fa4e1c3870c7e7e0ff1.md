---
title: Insert title here
key: d8fcd4c930027fa4e1c3870c7e7e0ff1
video_link:
  mp4: >-
    https://s3.amazonaws.com/videos.datacamp.com/raw/735_intro_to_python/v6/735_ch1_1.mp4
  hls: >-
    https://s3.amazonaws.com/videos.datacamp.com/transcoded/735_intro_to_python/v6/hls-735_ch1_1.master.m3u8
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
![v2_im1.png](https://assets.datacamp.com/production/repositories/288/datasets/1a484bc99a2af22d7f24b70c9054443a371f66c9/intro_gif.gif)

`@script`
In this course, you will learn Python for Data Science through video lessons, like this one, and interactive exercises. You get your own Python session where you can experiment and try to come up with the correct code to solve the instructions. You're learning by doing, while receiving customized and instant feedback on your work.

---

## Python

```yaml
type: FullSlide
key: 3f23b93572
```

`@part1`
![guido-hba.png](https://assets.datacamp.com/production/repositories/288/datasets/fb3e4b8dc114529dafffb37d33f2b2244210d40f/guido-hba.png = 38){{1}}

- General purpose: build anything{{2}}

- Open source! Free!{{3}}

- Python packages, also for data science{{4}}

	- Many applications and fields{{5}}

- Version 3.x - https://www.python.org/downloads/{{6}}

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
**Execute Python commands**

![im_interface.png](https://assets.datacamp.com/production/repositories/288/datasets/6d7582936bef6e37a9d7c8631a331eb82c288cbb/shell_selected.png)

`@script`
Now that you're all eyes and ears for Python, let's start experimenting. I'll start with the Python shell, a place where you can type Python code and immediately see the results. In DataCamp's exercise interface, this shell is embedded here. Let's start off simple and use Python as a calculator.

---

## IPython Shell

```yaml
type: FullSlide
key: 524e4c20a7
disable_transition: true
```

`@part1`
![v2_im_1.png](https://assets.datacamp.com/production/repositories/288/datasets/fdab8fd3b088d6514d3f9a34326f47792bc50d64/shell_gif.gif)

`@script`
Let me type 4 + 5, and hit Enter. Python interprets what you typed and prints the result of your calculation, 9. The Python shell that's used here is actually not the original one; we're using IPython, short for Interactive Python, which is some kind of juiced up version of regular Python that'll be useful later on.

IPython was created by Fernando Pérez and is part of the broader Jupyter ecosystem. Apart from interactively working with Python, you can also have Python run so called

---

## Python Script

```yaml
type: FullSlide
key: 78ef256bc0
```

`@part1`
- Text files - .py{{1}}

- List of Python commands{{2}}

- Similar to typing in IPython Shell{{3}}

![](https://assets.datacamp.com/production/repositories/288/datasets/e796d683f23a93859149146a91c884e0ff6990ec/script_0_selected.png) {{3}}

`@script`
python scripts. These python scripts are simply text files with the extension (dot) py. It's basically a list of Python commands that are executed, almost as if you where typing the commands in the shell yourself, line by line.

---

## Python Script

```yaml
type: FullSlide
key: 717d124175
disable_transition: true
```

`@part1`
![v2_im_4.png](https://assets.datacamp.com/production/repositories/288/datasets/1815bd762e807095f2e6ddaf529556a6fa8117b5/script_1.gif)

`@script`
Let's put the command from before in a script now, that can be found here in DataCamp's interface. The next step is executing the script, by clicking 'Submit Answer'. If you execute this script in the DataCamp interface, there's nothing in the output pane. That's because you have to explicitly use print inside scripts if you want to generate output during execution.

---

## Python Script

```yaml
type: FullSlide
key: c7a9d02fb6
disable_transition: true
code_zoom: 90
```

`@part1`
![v2_im_6.png](https://assets.datacamp.com/production/repositories/288/datasets/c3db89a4e008471ce1c4a80ed7abf39036635fec/script_2.gif = 96)
- Use `print()` to generate output from script

`@script`
Let's wrap our previous calculation in a print call, and rerun the script. This time, the same output as before is generated, great! Putting your code in Python scripts instead of manually retyping every step interactively will help you to keep structure and avoid retyping everything over and over again if you want to make a change; you simply make the change in the script, and rerun the entire thing.

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

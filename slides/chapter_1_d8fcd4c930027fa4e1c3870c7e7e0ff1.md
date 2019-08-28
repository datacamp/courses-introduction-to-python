---
title: 'Insert title here'
key: d8fcd4c930027fa4e1c3870c7e7e0ff1
video_link:
    mp4: 'https://s3.amazonaws.com/videos.datacamp.com/raw/735_intro_to_python/v6/735_ch1_1.mp4'
    hls: 'https://s3.amazonaws.com/videos.datacamp.com/transcoded/735_intro_to_python/v6/hls-735_ch1_1.master.m3u8'
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
![im2.png](https://assets.datacamp.com/production/repositories/288/datasets/17f43b4f62280f29b8b4d8351a014fae10e4227b/im2.png)

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
![im3.png](https://assets.datacamp.com/production/repositories/288/datasets/99a374c5ee5855662c2c0bde73cc9a0d0c7faaf4/im3.png)

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
![im4.png](https://assets.datacamp.com/production/repositories/288/datasets/0f7f11a8f122eccf859f6f5d48b8288db0b050f5/im4.png)

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
![im5.png](https://assets.datacamp.com/production/repositories/288/datasets/a756a72331b81ae53dbbf2c6a5bd20a6a7e0b579/im5.png)

`@script`
try to come up with the correct code to solve the instructions. You're learning by doing, while receiving customized and instant feedback on your work.

---

## How you will learn

```yaml
type: FullSlide
key: fde7ff1ea9
disable_transition: true
```

`@part1`
![im6.png](https://assets.datacamp.com/production/repositories/288/datasets/4d0e0d9307b116dd76030735c1413fab9a4a152e/im6.png)

`@script`
You're learning by doing, while receiving customized and instant feedback on your work.

---

## How you will learn

```yaml
type: FullSlide
key: c9dd1edd75
disable_transition: true
```

`@part1`
![im7.png](https://assets.datacamp.com/production/repositories/288/datasets/72fa767e3001998d758adb3c31776eb099955902/im7.png)

`@script`
while receiving customized and instant feedback on your work.

---

## How you will learn

```yaml
type: FullSlide
key: b6b5c151b9
disable_transition: true
```

`@part1`
![im8.png](https://assets.datacamp.com/production/repositories/288/datasets/134217f52690e2a0aad8cbadb95e3d91a83f1d3f/im8.png)

`@script`
and instant feedback on your work.

---

## Python

```yaml
type: FullSlide
key: 3f23b93572
```

`@part1`
- Guido Van Rossum{{1}}

- General Purpose: build anything{{2}}

- Open Source! Free!{{3}}

- Python Packages, also for Data Science{{4}}

	- Many applications and fields{{5}}

- Version 3.x - https://www.python.org/downloads/{{6}}

`@script`
Python was conceived by Guido Van Rossum. What started as a hobby project, soon became a general purpose programming language: nowadays, you can use Python to build practically any piece of software. But how did this happen? Well, first of all, Python is open source. It's free to use. Second, it's very easy to build packages in Python, which is code that you can share with other people to solve specific problems. Throughout time, more and more of these packages specifically built for data science have been developed. Suppose you want to make some fancy visualizations of your company's sales. There's a package for that. Or what about connecting to a database to analyze sensor measurements? There's also a package for that.

Currently, there are two common versions of Python, version 2-point-7 and 3-point-5 and later. Apart from some syntactical differences, they are pretty similar, but as support for version 2 will fade over time, our courses focus on Python 3. To install Python 3 on your own system, follow the steps at this URL.

---

## IPython Shell

```yaml
type: FullSlide
key: 43a91a7217
```

`@part1`
Execute Python commands

![ch_1_1_slides.002.png](https://assets.datacamp.com/production/repositories/288/datasets/cb6182b201754f60f34c183b1fc90fcacfa2eaf3/ch_1_1_slides.002.png)

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
![im_1.png](https://assets.datacamp.com/production/repositories/288/datasets/ca1d916c81bbf54c3ba1e0deb3706783f3556c4b/im_1.png)

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
![im_2.png](https://assets.datacamp.com/production/repositories/288/datasets/c82051c3a5857c7bc8077ec05004e6639cc0580e/im_2.png)

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
![im_2.png](https://assets.datacamp.com/production/repositories/288/datasets/c82051c3a5857c7bc8077ec05004e6639cc0580e/im_2.png)

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
![im_4.png](https://assets.datacamp.com/production/repositories/288/datasets/2504cc9b039dd4b8d59406e49b7321b1ecde4646/im_4.png)

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
![im_5.png](https://assets.datacamp.com/production/repositories/288/datasets/703e4622c7207a86742b3b5cc3c6267fbd2530ab/im_5.png)

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
![im_6.png](https://assets.datacamp.com/production/repositories/288/datasets/10d02b979555223b15a058ce7d70b64176d70efd/im_6.png)

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
![im_7.png](https://assets.datacamp.com/production/repositories/288/datasets/1194f04fed22a8350de661431655c15d2c7ff6bb/im_7.png)

`@script`
This time, the

---

## Python Script

```yaml
type: FullSlide
key: 7a8790e347
```

`@part1`
![im_9.png](https://assets.datacamp.com/production/repositories/288/datasets/a80a8f82d55a3baa3e29e7c0471b7eab2aa9201b/im_9.png)

`@script`
same output as before is generated, great! Putting your code in Python scripts instead of manually retyping every step interactively will help you to keep structure and avoid retyping everything over and over again if you want to make a change; you simply make the change in the script, and rerun the entire thing.

---

## DataCamp Interface

```yaml
type: FullSlide
key: 693ba1cd14
```

`@part1`
![ch_1_1_slides.001.png](https://assets.datacamp.com/production/repositories/288/datasets/f70371d1d3dcc8eb318c30132c95a6189e85726a/ch_1_1_slides.001.png)

`@script`
Now that you've got an idea about different ways of working with Python, I suggest you head over to the exercises.

---

## DataCamp Interface

```yaml
type: FullSlide
key: 0ee37fba22
disable_transition: true
```

`@part1`
![ch_1_1_slides.002.png](https://assets.datacamp.com/production/repositories/288/datasets/cb6182b201754f60f34c183b1fc90fcacfa2eaf3/ch_1_1_slides.002.png)

`@script`
Use the IPython Shell for experimentation,

---

## DataCamp Interface

```yaml
type: FullSlide
key: a88cc5ac35
disable_transition: true
```

`@part1`
![ch_1_1_slides.003.png](https://assets.datacamp.com/production/repositories/288/datasets/358eec4f33b609c324279c6b0c51017c3d598d86/ch_1_1_slides.003.png)

`@script`
and use the Python script editor to code the actual answer. If you click Submit Answer, your script will be executed and checked for correctness.

---

## Let's practice!

```yaml
type: FinalSlide
key: 7445cd202e
```

`@script`
Get coding and don't forget to have fun!

---
title: Insert title here
key: d8fcd4c930027fa4e1c3870c7e7e0ff1
video_link:
  mp3: >-
    https://videos.datacamp.com/raw/735_intro_to_python/v8/735_ch1_1.mp4
---

## 파이썬에 오신 것을 환영합니다!

```yaml
type: TitleSlide
key: f743ca8c41
```

`@lower_third`
name: Hugo Bowne-Anderson
title: Data Scientist at DataCamp

`@script`
Hi, my name is Hugo and I'll be your host for Introduction to Python for Data Science.

I'm a data scientist and educator at DataCamp.

---

## 학습 방식

```yaml
type: FullSlide
key: 30ee08a725
disable_transition: true
```

`@part1`
![DataCamp 인터페이스](https://assets.datacamp.com/img/translations/ko-KR/production/repositories/288/datasets/729574d2168960686381caefe79baf5978e27d0d/liveexercise.gif)

`@script`
In this course, you will learn Python for Data Science through video lessons, like this one, and interactive exercises. You get your own Python session where you can experiment and try to come up with the correct code to solve the instructions. You're learning by doing, while receiving customized and instant feedback on your work.

---

## 파이썬

```yaml
type: FullSlide
key: 3f23b93572
```

`@part1`
![guido-hba.png](https://assets.datacamp.com/img/translations/ko-KR/production/repositories/288/datasets/fb3e4b8dc114529dafffb37d33f2b2244210d40f/guido-hba.png = 38){{1}}

- 범용: 무엇이든 구축{{2}}

- 오픈 소스, 무료{{3}}

- 데이터 과학용 포함 패키지 풍부{{4}}

	- 다양한 응용 분야{{5}}

`@script`
Python was conceived by Guido Van Rossum. Here, you can see a photo of me with Guido. What started as a hobby project, soon became a general purpose programming language: nowadays, you can use Python to build practically any piece of software. But how did this happen? Well, first of all, Python is open source. It's free to use. Second, it's very easy to build packages in Python, which is code that you can share with other people to solve specific problems. Throughout time, more and more of these packages specifically built for data science have been developed. Suppose you want to make some fancy visualizations of your company's sales. There's a package for that. Or what about connecting to a database to analyze sensor measurements? There's also a package for that.
People often refer to Python as the swiss army knife of programming languages as you can do almost anything with it.
In this course, we'll start to build up your data science coding skills bit by bit, so make sure to stick around to see how powerful the language can be.

---

## IPython 셸

```yaml
type: FullSlide
key: 43a91a7217
```

`@part1`
**파이썬 명령 실행**

![ipython_shell.png](https://assets.datacamp.com/img/translations/ko-KR/production/repositories/288/datasets/a9e8440bb8fbd49e4a73e4c36ef1cd677c0dd55f/pyexercise.png = 95)

`@script`
Now that you're all eyes and ears for Python, let's start experimenting. I'll start with the

---

## IPython 셸

```yaml
type: FullSlide
key: 9c51ee700d
disable_transition: true
```

`@part1`
**파이썬 명령 실행**

![ipython_shell_highlighted.png](https://assets.datacamp.com/img/translations/ko-KR/production/repositories/288/datasets/dd43cc0183b15b43a072eb0fbab4caa72dee9250/pyexercise_shell.jpg = 95)

`@script`
Python shell, a place where you can type Python code and immediately see the results. In DataCamp's exercise interface, this shell is embedded here. Let's start off simple and use Python as a calculator.

---

## IPython 셸

```yaml
type: FullSlide
key: 524e4c20a7
disable_transition: true
```

`@part1`
&nbsp;

![DataCamp의 IPython 셸에서 계산](https://assets.datacamp.com/img/translations/ko-KR/production/repositories/288/datasets/cee32b788a62e4b9a1234ccde56ac9ebb49cfa72/shelladdition.gif = 95)

`@script`
Let me type 4 + 5, and hit Enter. Python interprets what you typed and prints the result of your calculation, 9. The Python shell that's used here is actually not the original one; we're using IPython, short for Interactive Python, which is some kind of juiced up version of regular Python that'll be useful later on.

IPython was created by Fernando Pérez and is part of the broader Jupyter ecosystem. Apart from interactively working with Python, you can also have Python run so called

---

## 파이썬 스크립트

```yaml
type: FullSlide
key: 78ef256bc0
```

`@part1`
- 텍스트 파일 - `.py`{{1}}

- 파이썬 명령어 목록{{2}}

- IPython 셸에서 타이핑하는 것과 유사{{3}}

![DataCamp의 파이썬 스크립트](https://assets.datacamp.com/img/translations/ko-KR/production/repositories/288/datasets/59f196e96536543a4fb8801228019fc4106f3791/pyexercise_script.jpg = 78){{3}}

`@script`
python scripts. These python scripts are simply text files with the extension (dot) py. It's basically a list of Python commands that are executed, almost as if you where typing the commands in the shell yourself, line by line.

---

## 파이썬 스크립트

```yaml
type: FullSlide
key: 717d124175
disable_transition: true
```

`@part1`
![GIF: 스크립트에 4 + 5를 입력하고 제출을 누름. 출력은 없음.](https://assets.datacamp.com/img/translations/ko-KR/production/repositories/288/datasets/2f96e979012e15329cc158d1e0f496aac3539f45/scriptnoprint.gif = 95)

`@script`
Let's put the command from before in a script now, which can be found here in DataCamp's interface. The next step is executing the script, by clicking 'Submit Answer'. If you execute this script in the DataCamp interface, there's nothing in the output pane. That's because you have to explicitly use print inside scripts if you want to generate output during execution.

---

## 파이썬 스크립트

```yaml
type: FullSlide
key: c7a9d02fb6
disable_transition: true
code_zoom: 90
```

`@part1`
![python_script_print.gif](https://assets.datacamp.com/img/translations/ko-KR/production/repositories/288/datasets/8b13d046bb54dcb11aa49f0da7363781129d1561/scriptwithprint.gif = 95)

- 스크립트에서 출력하려면 `print()` 사용

`@script`
Let's wrap our previous calculation in a print call, and rerun the script. This time, the same output as before is generated, great! Putting your code in Python scripts instead of manually retyping every step interactively will help you to keep structure and avoid retyping everything over and over again if you want to make a change; you simply make the change in the script, and rerun the entire thing.

---

## DataCamp 인터페이스

```yaml
type: FullSlide
key: 693ba1cd14
```

`@part1`
![DataCamp 인터페이스 스크린샷](https://assets.datacamp.com/img/translations/ko-KR/production/repositories/288/datasets/a9e8440bb8fbd49e4a73e4c36ef1cd677c0dd55f/pyexercise.png)

`@script`
Now that you've got an idea about different ways of working with Python, I suggest you head over to the exercises. Use the IPython Shell for experimentation, and use the Python script editor to code the actual answer. If you click Submit Answer, your script will be executed and checked for correctness.

---

## 연습해 봅시다!

```yaml
type: FinalSlide
key: 7445cd202e
```

`@script`
Get coding and don't forget to have fun!

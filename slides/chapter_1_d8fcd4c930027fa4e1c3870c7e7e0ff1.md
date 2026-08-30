---
title: Insert title here
key: d8fcd4c930027fa4e1c3870c7e7e0ff1
video_link:
  mp3: >-
    https://videos.datacamp.com/mp3/translations/course_735/zh-CN/f37109b9-0727-46c4-9165-d6b31c4ce999-a66e22f8a79e3a376a9ba6c2d3cdaa90.mp3
---

## 你好，Python！
```yaml
type: TitleSlide
key: f743ca8c41
```

`@lower_third`
name: Hugo Bowne-Anderson
title: Data Scientist at DataCamp

`@script`
大家好！我是 Hugo，也是“数据科学 Python 入门”这门课程的主讲人。

我是 DataCamp 的一名数据科学家和讲师。

---

## 学习方式

```yaml
type: FullSlide
key: 30ee08a725
disable_transition: true
```

`@part1`
![DataCamp 界面](https://assets.datacamp.com/img/translations/zh-CN/production/repositories/288/datasets/729574d2168960686381caefe79baf5978e27d0d/liveexercise.jpg)

`@script`
在这门课程中，你将通过类似这样的视频讲解和互动练习来学习有关数据科学的 Python 知识。课程中提供了独立的 Python 编程环境，你可以自由尝试并编写出符合指令要求的正确代码。通过这种边做边学的方式，你还能即时获得个性化反馈指导。

---

## Python

```yaml
type: FullSlide
key: 3f23b93572
```

`@part1`
![guido-hba.png](https://assets.datacamp.com/img/translations/zh-CN/production/repositories/288/datasets/fb3e4b8dc114529dafffb37d33f2b2244210d40f/guido-hba.jpg = 38){{1}}

- 通用编程：构建任何内容{{2}}

- 开源！免费！{{3}}

- Python 包，也适用于数据科学{{4}}

	- 许多应用和领域{{5}}

`@script`
Python 最初由 Guido van Rossum 构想并创立。这张照片就是我和 Guido 的合影。它起初只是一个业余项目，但很快便发展成为了一种通用编程语言：如今，你几乎可以用 Python 来开发任何软件。这是怎么做到的呢？首先，Python 是开源且完全免费的。其次，在 Python 中开发“包”非常简单 — 你可以把这些代码共享给他人，用来解决特定的问题。久而久之，越来越多专门针对数据科学的扩展包应运而生。假设你想为公司的销售数据制作炫酷的可视化图表，一般都有现成的包可用；如果你想连接数据库来分析传感器测量数据？同样有对应的包。
人们经常把 Python 比作编程界的“瑞士军刀”，因为你几乎能用它做任何事。
在这门课程中，我们将带你一步步掌握数据科学编程技能，务必坚持学习，感受这门语言的强大魅力。

---

## IPython Shell

```yaml
type: FullSlide
key: 43a91a7217
```

`@part1`
**执行 Python 命令**

![ipython_shell.png](https://assets.datacamp.com/img/translations/zh-CN/production/repositories/288/datasets/a9e8440bb8fbd49e4a73e4c36ef1cd677c0dd55f/pyexercise.jpg = 95)

`@script`
现在，既然你对 Python 充满兴趣，那就让我们开始动手尝试吧！我先从 Python Shell 讲起，

---

## IPython Shell

```yaml
type: FullSlide
key: 9c51ee700d
disable_transition: true
```

`@part1`
**执行 Python 命令**

![ipython_shell_highlighted.png](https://assets.datacamp.com/img/translations/zh-CN/production/repositories/288/datasets/dd43cc0183b15b43a072eb0fbab4caa72dee9250/pyexercise_shell.jpg = 95)

`@script`
在这里输入 Python 代码能实时看到运行结果。在 DataCamp 的练习界面中，Shell 就嵌套在这里。我们先从简单的开始，把 Python 当作计算器来使用。

---

## IPython Shell

```yaml
type: FullSlide
key: 524e4c20a7
disable_transition: true
```

`@part1`
 

![在 DataCamp 的 IPython Shell 中执行计算](https://assets.datacamp.com/img/translations/zh-CN/production/repositories/288/datasets/cee32b788a62e4b9a1234ccde56ac9ebb49cfa72/shelladdition.jpg = 95)

`@script`
输入 4 加 5，然后按回车，Python 就会解析你输入的内容，并打印出计算结果 9。这里用到的 Python Shell 其实不是原生版本，而是 IPython，也就是 Interactive Python 的缩写。它是常规 Python 的“加强版”，在后面会大有用处。

IPython 由 Fernando Pérez 开发，隶属于更庞大的 Jupyter 生态系统。除了进行交互式操作外，你还可以用 Python 来运行所谓的 Python 脚本。

---

## Python 脚本

```yaml
type: FullSlide
key: 78ef256bc0
```

`@part1`
- 文本文件 - `.py`{{1}}

- Python 命令列表{{2}}

- 类似于在 IPython Shell 中输入{{3}}

![DataCamp 平台上的 Python 脚本](https://assets.datacamp.com/img/translations/zh-CN/production/repositories/288/datasets/59f196e96536543a4fb8801228019fc4106f3791/pyexercise_script.jpg = 78){{3}}

`@script`
这些 Python 脚本在本质上就是后缀名为 .py 的文本文件。它记录了一连串按顺序执行的 Python 指令，就像你自己手动在 Shell 窗口里逐行输入并运行一样。

---

## Python 脚本

```yaml
type: FullSlide
key: 717d124175
disable_transition: true
```

`@part1`
![GIF：在脚本中输入 4 + 5 并点击提交答案。 未显示输出。](https://assets.datacamp.com/img/translations/zh-CN/production/repositories/288/datasets/2f96e979012e15329cc158d1e0f496aac3539f45/scriptnoprint.jpg = 95)

`@script`
现在，我们把刚才的指令添加到脚本里，脚本就在 DataCamp 界面上的这个位置。下一步是点击“提交答案”来运行脚本。不过，如果在 DataCamp 界面里运行这个脚本，输出窗口中不会有任何内容。这是因为要想在脚本执行时显示输出结果，还必须在代码中明确使用 print() 函数。

---

## Python 脚本

```yaml
type: FullSlide
key: c7a9d02fb6
disable_transition: true
code_zoom: 90
```

`@part1`
![python_script_print.gif](https://assets.datacamp.com/img/translations/zh-CN/production/repositories/288/datasets/8b13d046bb54dcb11aa49f0da7363781129d1561/scriptwithprint.jpg = 95)

- 使用 `print()` 从脚本生成输出

`@script`
我们把刚才的计算放入 print() 函数中，再重新运行一次脚本。这次，输出的结果和之前一模一样，太棒了！我们可以把代码保存到 Python 脚本中，而不是每次都在命令行里手动重复输入，这不仅能让代码结构更清晰，还能省去修改代码时重复输入的麻烦 — 你只需在脚本里完成修改，重新整体运行一遍就行。

---

## DataCamp 界面

```yaml
type: FullSlide
key: 693ba1cd14
```

`@part1`
![DataCamp 界面截图](https://assets.datacamp.com/img/translations/zh-CN/production/repositories/288/datasets/a9e8440bb8fbd49e4a73e4c36ef1cd677c0dd55f/pyexercise.jpg)

`@script`
现在你已经熟悉了 Python 的不同使用方式，不妨去练习一下。你可以用 IPython Shell 来进行测试和摸索，并在 Python 脚本编辑器中编写最终的解答代码。点击“提交答案”后，系统就会执行你的脚本并自动校验结果。

---

##   动手练一练！
```yaml
type: FinalSlide
key: 7445cd202e
```

`@script`
开始编写代码吧，好好享受学习的乐趣！

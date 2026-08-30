---
title: Insert title here
key: 433dcfcfedaee070cbf440491c402e3b
video_link:
  mp3: >-
    https://videos.datacamp.com/mp3/translations/course_735/zh-CN/4f73d46a-4a04-46ee-bdc2-d8d20eac1533-742bdb69f207f55d4c2132b79c6aec39.mp3
---

## 变量与类型

```yaml
type: TitleSlide
key: dc8b62f1c8
```

`@lower_third`
name: Hugo Bowne-Anderson
title: Data Scientist at DataCamp

`@script`
表现不错，欢迎回来！毫无疑问，Python 是一个强大的计算工具。但如果你想进行更复杂的计算，就会希望在编写代码时把一些数值“保存”起来。

---

## 变量

```yaml
type: FullSlide
key: 36ec318b41
```

`@part1`
- 区分大小写的特定名称

- 通过变量名调用值{{1}}

- 1.79 米 - 68.7 千克{{2}}

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
只需定义一个区分大小写的特定变量名，就能轻松保存数值。创建或声明变量后，随时可以通过输入变量名来调用它的值。

假设你测得的身高是 1.79 米，体重是 68.7 公斤。那么，你可以用等号把这两个数值分别赋值给 height 和 weight 变量：

这时只要输入变量名 height，

Python 就会找到这个变量，提取并打印出它的值。

---

## 计算 BMI

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
接下来计算体质指数 (BMI)。计算公式如下，其中体重单位为公斤，身高单位为米。你可以直接用具体数值计算，但我更推荐使用变量 height 和 weight，就像示例中那样。每次输入变量名，Python 都会将其替换为该变量的实际数值。这里的 weight 是 68.7，height 是 1.79。

最后，将计算结果存入一个新变量 bmi 中。此时 bmi 保存的数值就与刚才计算得到的结果完全一致。

Python 编程经常会用到变量，它能大幅提升代码的可复现性。

---

## 可再现

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
假设创建 height、weight 和 bmi 变量的代码都在一个脚本里，如下所示。如果你想根据另一个体重重新计算 bmi，

---

## 可复现性

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
那么，只需修改 weight 变量的声明并重新运行脚本。因为 weight 变量的值变了，bmi 也会相应地发生改变。

到目前为止，我们操作的还都是数值，比如身高和体重。

---

## Python 类型

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
在 Python 中，每个数字都有对应的类型。你可以用 type() 函数来查看某个值的类型。想要知道 bmi 的类型，只需在 type 后面的括号里填入 bmi 即可。你会发现它的类型是浮点数 float，也就是 Python 用来表示既有整数部分又有小数部分的实数类型。此外，Python 还有专门表示整数的类型 int，就像这个示例一样。

不过，在数据科学领域，只有 int 和 float 还不够。

---

## Python 类型 (2)

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
Python 还有许多其他数据类型，其中最常见的是字符串和布尔值。

字符串是 Python 用来表示文本的数据类型，使用单引号和双引号都可以构建字符串，如示例所示。如果你查看最后一个变量的类型，会发现它显示为 str，也就是 string 的缩写。

布尔值 (Boolean) 只有 True 和 False 两种取值，这相当于我们日常说的“是”和“否”。在后续的数据筛选等操作中，布尔值会非常实用。

另外，Python 的数据类型还有一些非常特别的地方。

---

## Python 类型 (3)

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

- 不同类型 = 不同行为！{{3}}

`@script`
看看这行对两个整数求和的代码，再看看这行将两个字符串连接起来的代码。

对于整数，+ 运算符会执行加法计算；对于字符串，它会把两段文本拼接在一起。对于不同的数据类型，同一个加号运算符的行为是不一样的。这是一条通用原则：代码如何运行，取决于使用的数据类型。

在接下来的练习中，你将创建自己的第一组变量，亲自体验一下 Python 的各种数据类型。我们下一个视频见，到时候，我会详细介绍有关列表的全部知识。

---

##   动手练一练！
```yaml
type: FinalSlide
key: b7fc40db4d
```

`@script`
我们开始动手编写代码吧！期待在下一章与你相见，届时你会构建出更棒的 Python 图表。

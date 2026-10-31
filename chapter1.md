---
title_meta: 第 1 章
title: Python 基础知识
description: Python 基础概念简介。学习如何以交互方式或通过脚本来使用 Python。你将创建自己的第一个变量，并熟悉 Python 的基本数据类型。
attachments:
  slides_link: 'https://projector-video-pdf-converter.datacamp.com/735/chapter1.pdf'
free_preview: true
lessons:
  - nb_of_exercises: 3
    title: 你好，Python！
  - nb_of_exercises: 5
    title: 变量和数据类型
---

## 你好，Python！

```yaml
type: VideoExercise
key: f644a48d5d
xp: 50
```

`@projector_key`
d8fcd4c930027fa4e1c3870c7e7e0ff1

---

## 你的第一段 Python 代码

```yaml
type: NormalExercise
key: bdc52f0e19
lang: python
xp: 100
skills:
  - 2
```

是时候运行你的第一段 Python 代码了！

前往代码编辑区域，点击"运行代码"按钮以查看输出结果。

`@instructions`
- 点击"运行代码"按钮，查看 `print(5 / 8)` 的输出结果。

`@hint`
- 在提交答案前先运行代码，以便有时间研究输出结果。

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Hit run code to see the output!
print(5 / 8)
```

`@solution`
```{python}
# Hit run code to see the output!
print(5 / 8)
```

`@sct`
```{python}
Ex().has_printout(0, not_printed_msg = "__JINJA__:您是否使用了 `{{sol_call}}` 来打印 `5 / 8`？")
success_msg("太好了！继续下一个！")
```

---

## 把 Python 当计算器使用

```yaml
type: NormalExercise
key: 0f7c039428
lang: python
xp: 100
skills:
  - 2
```

Python 非常适合进行基本计算。它可以实现加、减、乘、除运算。

脚本代码中提供了几个示例。

现在轮到你编写一些代码来练习一下了。

`@instructions`
- 在 `# Subtraction` 下使用 `print()` 打印 `5` 减去 `5` 的结果。
- 在 `# Multiplication` 下打印 `3` 乘以 `5` 的结果。

`@hint`
- 你需要使用 `print()` 来生成输出。
- 你可以分别使用 `-` 进行减法运算，使用 `*` 进行乘法运算。

`@pre_exercise_code`
```{python}
 
```

`@sample_code`
```{python}
# Addition and division
print(4 + 5)
print(10 / 2)

# Subtraction
print()

# Multiplication

```

`@solution`
```{python}
# Addition and division
print(4 + 5)
print(10 / 2)

# Subtraction
print(5 - 5)

# Multiplication
print(3 * 5)
```

`@sct`
```{python}
Ex().has_printout(0, not_printed_msg = "您是否使用了 `print(4 + 5)` 来打印出您的加法结果？")

Ex().has_printout(1, not_printed_msg = "您是否使用了 `print(5 - 5)` 来打印出您的减法结果？")

Ex().has_printout(2, not_printed_msg = "您是否使用了 `print(3 * 5)` 来打印出您的乘法结果？")

Ex().has_printout(3, not_printed_msg = "您是否使用了 `print(10 / 2)` 来打印出您的除法结果？")

success_msg("正确！Python 可以帮助您进行数学运算，这一特性将在我们提高数据技能时对分析非常有帮助。")
```

---

## 变量与数据类型

```yaml
type: VideoExercise
key: c2e396792e
xp: 50
```

`@projector_key`
433dcfcfedaee070cbf440491c402e3b

---

## 变量赋值

```yaml
type: NormalExercise
key: 4bf65ad83e
lang: python
xp: 100
skills:
  - 2
```

在 Python 中，你可以使用名称来引用一个值，这就是变量。要创建值为 `5` 的变量 `x`，你可以使用 `=`，示例如下：

```
x = 5
```

现在你就可以使用变量名 `x` 来代替具体的数值 `5` 了。

请记住，Python 中的 `=` 表示赋值，而不是用来判断“相等关系”的！请试试在练习中将 `____` 替换成你编写的代码。

`@instructions`
- 创建一个变量 `savings`，并为其赋值 `100`。
- 在脚本中输入 `print(savings)` 来查看该变量。

`@hint`
- 输入 `savings = 100` 来创建变量 `savings`。
- 创建变量 `savings` 之后，你可以输入 `print(savings)`。
- 最终代码不应包含任何 `____`。

`@pre_exercise_code`
```{python}
 
```

`@sample_code`
```{python}
# Create a variable savings
____

# Print out savings
____
```

`@solution`
```{python}
# Create a variable savings
savings = 100

# Print out savings
print(savings)
```

`@sct`
```{python}
Ex().check_object("savings").has_equal_value(incorrect_msg="将 `100` 赋值给变量 `savings`。")
Ex().has_printout(0, not_printed_msg = "使用 `print(savings)` 打印出您创建的变量 `savings`。")
success_msg("很好！现在让我们尝试用这个变量进行一些计算！")
```

---

## 对变量进行计算

```yaml
type: NormalExercise
key: ff06cedeb4
lang: python
xp: 100
skills:
  - 2
```

现在，你已经创建了一个 savings 变量，准备开始存钱吧！

你可以使用变量进行计算，而不是使用具体的数值。

如果你每月存 $10，4 个月后你会存下多少钱？

`@instructions`
- 创建一个变量 `monthly_savings`，使其等于 `10`，并创建一个 `num_months`，使其等于 `4`。
- 将 `monthly_savings` 乘以 `num_months`，并将结果复制给 `new_savings`。
- 打印 `new_savings` 的值。

`@hint`
- 你可以像对待数字一样对变量进行计算。因此，你可以把 `10 * 4` 中的数字替换成相应的变量！
- 使用 `print()` 查看 `new_savings` 的金额。
- 注意变量名拼写要正确！

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create the variables monthly_savings and num_months



# Multiply monthly_savings and num_months
new_savings = ____

# Print new_savings

```

`@solution`
```{python}
# Create the variables monthly_savings and num_months
monthly_savings = 10
num_months = 4

# Multiply monthly_savings and num_months
new_savings = monthly_savings * num_months

# Print new_savings
print(new_savings)
```

`@sct`
```{python}
Ex().check_object("monthly_savings").has_equal_value(incorrect_msg = "您是否使用 `monthly_savings = 10` 将 `10` 保存到 `monthly_savings`？")
Ex().check_object("num_months").has_equal_value(incorrect_msg = "您是否使用 `num_months = 4` 将 `4` 保存到 `num_months`？")
Ex().check_object("new_savings").has_equal_value(incorrect_msg = "您是否使用了正确的变量和符号进行乘法？预期为 `monthly_savings * num_months`，但得到了其他结果。")
# Ex().check_object("total_savings").has_equal_value(incorrect_msg = "您是否使用了正确的变量和符号进行加法？预期为 `savings + new_savings`，但得到了其他结果。")

Ex().has_printout(0, not_printed_msg="请记得在脚本末尾打印出 `new_savings`。")

success_msg("您有 $40 的新储蓄！")
```

---

## 其他变量类型

```yaml
type: NormalExercise
key: 006b48561f
lang: python
xp: 100
skills:
  - 2
```

在上一个练习中，你使用了 Python 的整数数据类型：

- `int`（即整数）：没有小数部分的数值。值为 `100` 的 `savings` 就是整数的一个示例。

除了数值数据类型外，还有另外三种很常见的数据类型：

- `float`（即浮点数）：同时包含整数部分和小数部分（由点分隔）的数字。`1.1` 就是浮点数的一个示例。
- `str`（即字符串）：用于表示文本的数据类型。你可以使用单引号或双引号来构建字符串。
- `bool`（即布尔值）：用于表示逻辑值的数据类型。只能是 `True` 或 `False`（务必正确区分大小写！）。

`@instructions`
- 创建一个新的浮点数 `half`，值为 `0.5`。
- 创建一个新的字符串 `intro`，值为 `"Hello! How are you?"`。
- 创建一个新的布尔值 `is_good`，值为 `True`。

`@hint`
- 在 Python 中可使用 `=` 创建变量。务必记得给字符串加上单引号或双引号。
- Python 只有两个布尔值：`True` 和 `False`。`TRUE`、`true`、`FALSE`、`false` 等其他写法都无效。

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create a variable half


# Create a variable intro


# Create a variable is_good

```

`@solution`
```{python}
# Create a variable half
half = 0.5

# Create a variable intro
intro = "Hello! How are you?"

# Create a variable is_good
is_good = True
```

`@sct`
```{python}
Ex().check_object("half").has_equal_value(incorrect_msg = "您是否将浮点数 `0.5` 保存到 `half`？")

Ex().check_object("intro").has_equal_value(incorrect_msg = "嗯，您的 `intro` 变量中有些不正确的地方。请仔细检查拼写，并确保您使用了引号。")

Ex().check_object("is_good").has_equal_value(incorrect_msg = "您是否将布尔值大写？请记住，这里不需要使用引号。")

success_msg("做得好！")
```

---

## 与其他数据类型的运算

```yaml
type: BulletExercise
key: 4d0d83cc02
xp: 100
```

Python 中的变量有不同的数据类型。你可以使用 `type()` 查看变量的类型。比如，要查看 `a` 的类型，可运行：`type(a)`。

不同数据类型在 Python 中的行为也不同。比如，将两个字符串相加，与将两个整数或两个布尔值相加，它们的表现是不一样的。

现在，你可以动手试一试。

`@pre_exercise_code`
```{python}

```

***

```yaml
type: NormalExercise
key: f4e91c4ae9
xp: 50
```

`@instructions`
- 将 `savings` 与 `new_savings` 相加，并将结果赋值给 `total_savings`。
- 使用 `type()` 打印 `total_savings` 的类型。

`@hint`
- 将 `savings + new_savings` 赋值给一个新变量 `total_savings`。
- 要打印变量 `x` 的类型，请使用 `print(type(x))`。

`@sample_code`
```{python}
savings = 100
new_savings = 40

# Calculate total_savings using savings and new_savings
____
print(total_savings)

# Print the type of total_savings
print(____)
```

`@solution`
```{python}
savings = 100
new_savings = 40

# Calculate total_savings using savings and new_savings
total_savings = savings + new_savings
print(total_savings)

# Print the type of total_savings
print(type(total_savings))
```

`@sct`
```{python}
# predefined
msg = "您不必更改或删除预定义变量。"

Ex().multi(
    check_object('savings', missing_msg=msg).has_equal_value(incorrect_msg=msg),
    check_object('new_savings', missing_msg=msg).has_equal_value(incorrect_msg=msg)
)

Ex().multi(
    check_object("total_savings").has_equal_value(incorrect_msg="将 `savings` 和 `new_savings` 相加以创建 `total_savings` 变量。"),
    has_printout(1, not_printed_msg = "__JINJA__:使用 `{{sol_call}}` 打印出 `total_savings` 的类型。")
)
```

***

```yaml
type: NormalExercise
key: f54fbf9bd9
xp: 50
```

`@instructions`
- 计算 `intro` 与 `intro` 的和，并将结果赋值给 `doubleintro`。
- 打印 `doubleintro`。结果是否符合你的预想？

`@hint`
- 将 `intro + intro` 赋值给一个新变量 `doubleintro`。
- 要打印变量 `x`，请在脚本中加入 `print(x)`。

`@sample_code`
```{python}
intro = "Hello! How are you?"

# Assign sum of intro and intro to doubleintro
____

# Print out doubleintro
print(____)
```

`@solution`
```{python}
intro = "Hello! How are you?"

# Assign sum of intro and intro to doubleintro
doubleintro = intro + intro

# Print out doubleintro
print(doubleintro)
```

`@sct`
```{python}
# predefined
msg = "您不必更改或删除预定义变量。"

Ex().check_object('intro', missing_msg=msg).has_equal_value(incorrect_msg=msg)

Ex().multi(
    check_object("doubleintro").has_equal_value(incorrect_msg  = "您是否已将 `intro + intro` 的结果存储在 `doubleintro` 中？"),
    has_printout(0, not_printed_msg = "别忘了打印出 `doubleintro`。")
)

success_msg("很好。注意 `intro + intro` 如何使 `\"Hello! How are you?\"` 和 `\"Hello! How are you?\"` 拼接在一起。")
```

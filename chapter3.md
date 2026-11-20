---
title_meta: 第 3 章
title: 函数和包
description: 你将学习如何使用函数、方法和包，高效复用优秀 Python 开发者编写的代码。目标是减少为解决复杂问题而需编写的代码量。
attachments:
  slides_link: 'https://projector-video-pdf-converter.datacamp.com/735/chapter3.pdf'
lessons:
  - nb_of_exercises: 4
    title: 函数
  - nb_of_exercises: 4
    title: 方法
  - nb_of_exercises: 4
    title: 包
---

## 函数

```yaml
type: VideoExercise
key: 5c5f365930
xp: 50
```

`@projector_key`
1204d914b0e53100529827e07441ee6c

---

## 常用函数

```yaml
type: NormalExercise
key: c422ee929b
lang: python
xp: 100
skills:
  - 2
```

Python 提供了许多开箱即用的内置函数。作为一名数据科学家，这些函数可以让你的工作更加轻松。你已经了解了两个这样的函数：`print()` 和 `type()`。还有像 `str()`、`int()`、`bool()` 和 `float()` 这样用于转换数据类型的函数。你可以在[此处](https://docs.python.org/3/library/functions.html)了解它们。这些都是内置函数。

函数调用很简单。要获取 `3.0` 的类型并将输出存储到新变量 `result` 中，可以使用以下代码：

```
result = type(3.0)
```

`@instructions`
- 将 `type()` 嵌套在 `print()` 内，打印输出 `var1` 的数据类型。
- 对于列表 `var1`，使用 `len()` 获取[列表长度](https://docs.python.org/3/library/functions.html#len)。将其包含在 `print()` 调用中即可直接打印出来。
- 使用 `int()` 将 `var2` 转换为[整数](https://docs.python.org/3/library/functions.html#int)。将输出结果存储为 `out2`。

`@hint`
- 像这样调用 `type()` 函数：`type(var1)`。
- 像你之前多次做过的那样调用 `print()`。只需把你想打印的变量放入括号里。
- `int(x)` 会将 `x` 转换为整数。

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create variables var1 and var2
var1 = [1, 2, 3, 4]
var2 = True

# Print out type of var1
____

# Print out length of var1
____

# Convert var2 to an integer: out2
out2 = ____
```

`@solution`
```{python}
# Create variables var1 and var2
var1 = [1, 2, 3, 4]
var2 = True

# Print out type of var1
print(type(var1))

# Print out length of var1
print(len(var1))

# Convert var2 to an integer: out2
out2 = int(var2)
```

`@sct`
```{python}
msg = "您不需要更改或删除预定义的变量。"
Ex().check_object("var1", missing_msg=msg).has_equal_value(incorrect_msg=msg)
Ex().check_object("var2", missing_msg=msg).has_equal_value(incorrect_msg=msg)

patt = "__JINJA__:请确保使用 `{{sol_call}}` 打印出 `var1` 的 %s。"
Ex().has_printout(0, not_printed_msg = patt % '类型')
Ex().has_printout(1, not_printed_msg = patt % '长度')

int_miss_msg = "您是否使用了 `int()` 将 `var2` 转换为整数？"
int_incorr_msg = "您是否将 `var2` 传递给了 `int()`？"
Ex().check_correct(
  check_object("out2").has_equal_value(incorrect_msg="您正确调用了 `int()`；现在请确保将此调用的结果赋值给 `out2`。"),
  check_function("int", missing_msg=int_miss_msg).has_equal_value(incorrect_msg=int_incorr_msg)
)
success_msg("做得好！`len()` 函数非常有用；它也可以用于字符串以计算字符的数量！")
```

---

## help() 函数

```yaml
type: MultipleChoiceExercise
key: 679b852978
lang: python
xp: 50
skills:
  - 2
```

也许你刚好知道某个 Python 函数的名称，但不知道具体如何使用。有趣的是，你需要使用另一个函数来查询这个函数的信息：`help()`。在 IPython 中，你也可以在函数名前加上 `?`。

例如，要查看函数 `max()` 的帮助，你可以使用以下任一调用：

```
help(max)
?max
```

在 IPython Shell 中打开有关 `pow()` 的[文档](https://docs.python.org/3/library/functions.html#pow)。输入 `?pow` 或 `help(pow)`，然后按 **Enter** 即可将其打开。

以下哪一项说法是正确的？

`@possible_answers`
- `pow()` 需要 3 个参数：`base`、`exp` 和 `mod`。如果不提供 `mod`，该函数将返回错误。
- `pow()` 需要 3 个必填参数：`base`、`exp` 和 `None`。
- `pow()` 需要 `base` 和 `exp` 参数；`mod` 是可选的。
- `pow()` 需要 2 个参数：`exp` 和 `mod`。缺少 `exp` 会导致错误。

`@hint`
- 可选参数会使用 `=` 设定默认值；如果没有为该参数赋值，函数会使用其默认值。

`@pre_exercise_code`
```{python}

```

`@sct`
```{python}
msg1 = "不完全正确。`mod` 有一个默认值，如果您不指定值，将使用该默认值。"
msg2 = "不正确。`None` 是 `mod` 参数的默认值。"
msg3 = "完美！使用 `help()` 可以帮助您理解函数的工作原理，释放其全部潜力！"
msg4 = "不正确。`pow()` 接受三个参数，其中一个具有默认值。"
Ex().has_chosen(3, [msg1, msg2, msg3, msg4])
```

---

## 多个参数

```yaml
type: NormalExercise
key: e30486d7c1
lang: python
xp: 100
skills:
  - 2
```

在上一个练习中，你通过使用 `help()` 查看文档，掌握了什么是可选参数。现在，你将动手试试，使用参数来修改 `sorted()` 函数的行为。

在 IPython Shell 中输入 `help(sorted)`，查看 `sorted()` 的[文档](https://docs.python.org/3/library/functions.html#sorted)。

你会发现 `sorted()` 需要 3 个参数：`iterable`、`key` 和 `reverse`。在本练习中，你只需指定 `iterable` 和 `reverse`，无需指定 `key`。

我们已为你创建了两个列表。

你能把它们合并在一起并按降序排序吗？

`@instructions`
- 使用 `+` 将 `first` 和 `second` 的内容合并为一个新列表：`full`。
- 对 `full` 调用 `sorted()`，并将 `reverse` 参数设为 `True`。将排序后的列表保存为 `full_sorted`。
- 最后打印 `full_sorted` 的输出结果。

`@hint`
- 将 `first` 和 `second` 相加（就像对两个数字求和一样），并把结果赋值给 `full`。
- 调用 `sorted()` 并传入两个参数：`full` 和 `reverse=True`。
- 使用 `print()` 打印变量的输出结果。

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create lists first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# Paste together first and second: full
full = ____ + ____

# Sort full in descending order: full_sorted
full_sorted = ____

# Print out full_sorted
____
```

`@solution`
```{python}
# Create lists first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# Paste together first and second: full
full = first + second

# Sort full in descending order: full_sorted
full_sorted = sorted(full, reverse=True)

# Print out full_sorted
print(full_sorted)
```

`@sct`
```{python}
msg = "您不必更改或删除已存在的变量 `first` 和 `second`。"
Ex().multi(
  check_object("first", missing_msg=msg).has_equal_value(incorrect_msg=msg),
  check_object("second", missing_msg=msg).has_equal_value(incorrect_msg=msg)
)
Ex().check_correct(
  check_object("full_sorted").has_equal_value(incorrect_msg="确保您将调用 `sorted()` 的结果赋值给 `full_sorted`。"),
  check_function("sorted").multi(
    check_args(0).has_equal_value(),
    check_args('reverse').has_equal_value()
  )
)

success_msg("太棒了！请观看关于 Python 方法的视频。")
```

---

## 方法

```yaml
type: VideoExercise
key: 2b66cb66b1
xp: 50
```

`@projector_key`
8e387776f3a264a745128b68aa8d8f83

---

## 字符串方法

```yaml
type: NormalExercise
key: 4039302ee0
lang: python
xp: 100
skills:
  - 2
```

字符串自带了许多方法。请跟着指引操作，探索其中几个示例。如果你想了解更多细节，可以随时在 IPython Shell 终端内输入 `help(str)` 来进行查看。

我们已经提前为你创建好了一个名为 `place` 的字符串，方便你动手尝试。

`@instructions`
- 对 `place` 使用 `.upper()` [方法](https://docs.python.org/3/library/stdtypes.html#str.upper)，并将结果存储在 `place_up` 中。使用你在前一个视频中学到的调用方法的语法。
- 打印 `place` 和 `place_up`。看看这两个变量是不是都改变了？
- 通过对 `place` 调用 `.count()`，并将字母 `'o'` 作为输入传递给该方法，打印出 `place` 中字母 o 的数量。 注意，我们讨论的是变量 `place`，而不是单词 `"place"`！

`@hint`
- 你可以直接对 `place` 调用 `.upper()` 方法，无需任何额外的输入。
- 要打印变量 `x`，你可以编写 `print(x)`。
- 确保将 `place.count(____)` 调用嵌套在 `print()` 函数中，以便打印结果。

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# string to experiment with: place
place = "poolhouse"

# Use upper() on place
place_up = 

# Print out place and place_up



# Print out the number of o's in place

```

`@solution`
```{python}
# string to experiment with: place
place = "poolhouse"

# Use upper() on place
place_up = place.upper()

# Print out place and place_up
print(place)
print(place_up)

# Print out the number of o's in place
print(place.count('o'))
```

`@sct`
```{python}
msg = "您不需要更改或删除预定义的变量。"
Ex().check_object("place", missing_msg=msg).has_equal_value(incorrect_msg=msg)

patt = "别忘了打印出 `%s`。"
Ex().has_printout(0, not_printed_msg=patt % "place")
Ex().check_correct(
    has_printout(1, not_printed_msg=patt % "place_up"),
    check_correct(
        check_object("place_up").has_equal_value(incorrect_msg="将 `place.upper()` 调用的结果赋值给 `place_up`。"),
        check_function("place.upper", signature=False)
    )
)    

# check count of place
Ex().check_correct(
  has_printout(2, not_printed_msg = "您已经正确计算了 `place` 中字母 o 的数量；现在请确保将 `place.count('o')` 调用包裹在 `print()` 函数中以打印出结果。"),
  check_function("place.count", signature=False).check_args(0).has_equal_value()
)

success_msg("很好！请注意，从打印输出中可以看出，`upper()` 方法不会更改其调用的对象。在下一个练习中，这对于列表将会有所不同！")
```

---

## 列表方法

```yaml
type: NormalExercise
key: 0dbe8ed695
lang: python
xp: 100
skills:
  - 2
```

在 Python 中，并不是只有字符串才自带方法，列表、浮点数、整数和布尔值也都绑定了许多超实用的内置方法。在本练习中，你将尝试使用：

- `.index()`：用来查找列表中第一个匹配元素的索引位置；
- `.count()`：用来统计某个元素在列表中一共出现了多少次。

接下来，你将对记录房屋各区域面积的列表 `areas` 进行操作。

`@instructions`
- 使用 `.index()` 方法获取 `areas` 中等于 `20.0` 的元素的索引。打印该索引。
- 对 `areas` 调用 `.count()`，统计 `9.50` 在列表中出现了多少次。同样，将该数字打印出来。

`@hint`
- 要打印索引，请将 `areas.index(___)` 调用嵌套在 `print()` 函数中。
- 要打印元素 `x` 在列表中出现的次数，请将 `areas.count(___)` 调用嵌套在 `print()` 函数中。

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Print out the index of the element 20.0


# Print out how often 9.50 appears in areas

```

`@solution`
```{python}
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Print out the index of the element 20.0
print(areas.index(20.0))

# Print out how often 9.50 appears in areas
print(areas.count(9.50))
```

`@sct`
```{python}
predef_msg = "您不必更改或删除预定义列表 `areas`。"

Ex().check_object("areas", missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg)

Ex().check_function("print", index=0).check_args(0).check_function('areas.index', signature=False).check_args(0).has_equal_value()

Ex().check_function("print", index=1).check_args(0).check_function('areas.count', signature=False).has_equal_value()

success_msg("很好！这些是 `list` 方法的示例，它们不会更改调用它们的列表。")
```

---

## 列表方法 (2)

```yaml
type: NormalExercise
key: 1fbeab82d0
lang: python
xp: 100
skills:
  - 2
```

大多数列表方法都会修改调用它们的原列表。例如：

- `.append()`：向调用它的列表中添加一个元素；
- `.remove()`：从列表中[删除](https://docs.python.org/3/library/stdtypes.html#typesseq-mutable)第一个与输入匹配的元素；
- `.reverse()`：将所调用列表中元素的顺序[反转](https://docs.python.org/3/library/stdtypes.html#typesseq-mutable)。

接下来你将对记录房屋各区域面积的列表 `areas` 进行操作。

`@instructions`
- 调用 `.append()` 两次，依次加入泳池小屋和车库的面积：分别是 `24.5` 和 `15.45`。注意，务必要按上面的顺序添加。
- 打印 `areas`。
- 使用 `.reverse()` 方法将 `areas` 中元素的顺序反转。
- 再次打印 `areas`。

`@hint`
- 对于第一条指令，需要调用 `areas.append(___)` 两次。
- 要打印变量 `x`，只需加入 `print(x)`。
- `.reverse()` 方法不需要额外输入；只需使用点号加空括号：`.reverse()`。
- 要打印变量 `x`，只需加入 `print(x)`。

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Use append twice to add poolhouse and garage size



# Print out areas


# Reverse the orders of the elements in areas


# Print out areas

```

`@solution`
```{python}
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Use append twice to add poolhouse and garage size
areas.append(24.5)
areas.append(15.45)

# Print out areas
print(areas)

# Reverse the orders of the elements in areas
areas.reverse()

# Print out areas
print(areas)
```

`@sct`
```{python}
Ex().multi(
  check_function("areas.append", index=0, signature=False).check_args(0).has_equal_value(),
  check_function("areas.append", index=1, signature=False).check_args(0).has_equal_value(),
  check_function("print", index=0).check_args(0).has_equal_ast(),
  check_function("areas.reverse", index=0, signature=False),
  check_function("print", index=1).check_args(0).has_equal_ast()
)

success_msg("做得好！")
```

---

## 包

```yaml
type: VideoExercise
key: ab96a17c5e
xp: 50
```

`@projector_key`
cedcfb34350be8545599768f96695cdd

---

## 导入包

```yaml
type: NormalExercise
key: 7432a6376f
lang: python
xp: 100
skills:
  - 2
```

假设你想计算一个圆的周长和面积，公式如下：

$$C = 2 \pi r$$
$$A = \pi r^2 $$

你不需要手动输入 `pi` 的数值，可以直接使用包含圆周率数值的 `math` 包。

补充说明：`**` 代表幂运算。例如，`3**4` 表示 `3` 的 `4` 次幂，结果为 `81`。

`@instructions`
- 导入 `math` 包。
- 使用 `math.pi` 计算圆的周长，并将结果存储在 `C` 中。
- 使用 `math.pi` 计算圆的面积，并将结果存储在 `A` 中。

`@hint`
- 你可以直接使用 `import math`，然后使用 `math.pi` 来引用 `pi`。
- 按照题目中给出的公式计算 `C`。乘法使用 `*` 运算符。
- 按照题目中给出的公式计算 `A`。乘法和幂运算分别使用 `*` 和 `**` 运算符。

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Import the math package
import ____

# Calculate C
C = 2 * 0.43 * ____

# Calculate A
A = ____ * 0.43 ** 2

print("Circumference: " + str(C))
print("Area: " + str(A))
```

`@solution`
```{python}
# Import the math package
import math

# Calculate C
C = 2 * 0.43 * math.pi

# Calculate A
A = math.pi * 0.43 ** 2

print("Circumference: " + str(C))
print("Area: " + str(A))
```

`@sct`
```{python}
patt = "您对`%s`的计算不太正确。请确保使用`math.pi`。"
Ex().multi(
  has_import('math', same_as=False),
  check_object('C').has_equal_value(incorrect_msg=patt%'C'),
  check_object('A').has_equal_value(incorrect_msg=patt%'A')
)

Ex().multi(
  has_printout(0, not_printed_msg = "__JINJA__:请保留`{{sol_call}}`以打印出周长。"),
  has_printout(1, not_printed_msg = "__JINJA__:请保留`{{sol_call}}`以打印出面积。")
)

success_msg("很好！如果您知道如何处理来自包的函数，许多Python程序员的强大功能就触手可及！")
```

---

## 选择性导入

```yaml
type: NormalExercise
key: fe65eff50a
lang: python
xp: 100
skills:
  - 2
```

通用导入（如 `import math`）会使 `math` 包中的**所有**功能都可用。不过，如果你只打算使用包中的某个部分，也可以进行更有针对性的导入：

```
from math import pi
```

再试一下刚才的操作，不过这次仅使用 `pi`。

`@instructions`
- 从 `math` 包中执行选择性导入，仅导入 `pi` 函数。
- 使用 `pi` 计算圆的周长，并将结果存储在 `C` 中。
- 使用 `pi` 计算圆的面积，并将结果存储在 `A` 中。

`@hint`
- 使用 `from math import pi` 进行选择性导入。
- 现在，你可以直接使用 `pi` 了！

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Import pi function of math package
from math import ____

# Calculate C
C = 2 * 0.43 * ____

# Calculate A
A = ____ * 0.43 ** 2

print("Circumference: " + str(C))
print("Area: " + str(A))
```

`@solution`
```{python}
# Import pi function of math package
from math import pi

# Calculate C
C = 2 * 0.43 * pi

# Calculate A
A = pi * 0.43 ** 2

print("Circumference: " + str(C))
print("Area: " + str(A))
```

`@sct`
```{python}
patt = "您对`%s`的计算不太正确。请确保仅使用`pi`。"

Ex().has_import("math.pi", not_imported_msg = "请确保从`math`包中导入`pi`。您应该使用`from ___ import ___`的格式。",)

Ex().multi(
  check_object('C').has_equal_value(incorrect_msg=patt%'C'),
  check_object('A').has_equal_value(incorrect_msg=patt%'A')
)

Ex().multi(
  has_printout(0, not_printed_msg = "__JINJA__:请保留`{{sol_call}}`以打印出圆周长。"),
  has_printout(1, not_printed_msg = "__JINJA__:请保留`{{sol_call}}`以打印出面积。")
)

success_msg("很好！继续进行下一个练习。")
```

---

## 几种常见的导入方式

```yaml
type: MultipleChoiceExercise
key: f1b2675a2a
lang: python
xp: 50
skills:
  - 2
```

将包和模块导入 Python 有多种方式。根据导入方式的不同，编写的 Python 调用代码也不同。

假设你想使用 `inv()` [函数](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.inv.html)，该函数位于 `scipy` 包的子包 `linalg` 中。你希望能够按如下方式使用该函数：

```
my_inv([[1,2], [3,4]])
```

为了让上面的代码正常运行而不报错，你需要使用下面哪句 `import` 语句？

`@possible_answers`
- `import scipy`
- `import scipy.linalg`
- `from scipy.linalg import my_inv`
- `from scipy.linalg import inv as my_inv`

`@hint`
- 在 IPython Shell 中试试上面几种不同的 import 语句，看看哪一个能让 `my_inv([[1, 2], [3, 4]])` 这行代码正常运行而不报错。按 **enter** 即可运行输入的代码。

`@pre_exercise_code`
```{python}

```

`@sct`
```{python}
msg1 = msg2 = msg3 = "不正确，请重试。尝试在 IPython shell 中使用不同的导入语句，看看哪个语句能让 `my_inv([[1, 2], [3, 4]])` 这行代码运行而不出错。"
msg4 = "正确！`as` 关键字允许您为导入的函数创建一个本地名称：`inv()` 现在可以作为 `my_inv()` 使用。"
Ex().has_chosen(4, [msg1, msg2, msg3, msg4])
```

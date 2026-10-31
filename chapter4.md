---
title_meta: 第 4 章
title: NumPy
description: NumPy 是进行数据科学实践的基础 Python 包。学习使用强大的 NumPy 数组工具，并开始进行数据探索。
attachments:
  slides_link: 'https://projector-video-pdf-converter.datacamp.com/735/chapter4.pdf'
lessons:
  - nb_of_exercises: 5
    title: Numpy
  - nb_of_exercises: 5
    title: 二维 Numpy 数组
  - nb_of_exercises: 3
    title: Numpy：基础统计学
---

## NumPy

```yaml
type: VideoExercise
key: f4545baa53
xp: 50
```

`@projector_key`
a0487c26210f6b71ea98f917734cea3a

---

## 编写第一个 NumPy 数组

```yaml
type: NormalExercise
key: 84cab9d170
lang: python
xp: 100
skills:
  - 2
```

现在，你将深入探索棒球的数据世界。在此过程中，你会熟练掌握 `numpy` 的基础用法 — 这是数据科学领域一个极为强大的包。

Python 脚本中已经定义了一个列表 `baseball`，代表一些棒球球员的身高（厘米）。你能添加几行代码，将其转换成 `numpy` 数组吗？

`@instructions`
- 使用 `np` 导入 `numpy` 包，以便使用 `np` 来引用 `numpy`。
- 使用 `np.array()` 将 `numpy` 列表转换成 `baseball` 数组，并将其命名为 `np_baseball`。
- 打印 `np_baseball` 的数据类型，检查操作是否正确。

`@hint`
- 写成 `import numpy as np` 这样就能完成导入。以后只要你想要使用 `np.fun_name()` 中的函数，都要写成 `numpy` 形式。
- 将 `baseball` 传递给 `np.array()`，然后将函数调用返回的结果赋值给 `np_baseball`。
- 要打印变量 `x` 的数据类型，只需直接输入 `print(type(x))`。

`@pre_exercise_code`
```{python}
import numpy as np
```

`@sample_code`
```{python}
# Import the numpy package as np


baseball = [180, 215, 210, 210, 188, 176, 209, 200]

# Create a numpy array from baseball: np_baseball


# Print out type of np_baseball

```

`@solution`
```{python}
# Import the numpy package as np
import numpy as np

baseball = [180, 215, 210, 210, 188, 176, 209, 200]

# Create a NumPy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out type of np_baseball
print(type(np_baseball))
```

`@sct`
```{python}
predef_msg = "您不必更改或删除预定义变量。"
Ex().has_import("numpy")
Ex().check_correct(
  check_object("np_baseball"),
  multi(
    check_object("baseball", missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
    check_function("numpy.array").check_args(0).has_equal_ast()
  )
)

Ex().has_printout(0)
success_msg("做得好！")
```

---

## 棒球球员的身高

```yaml
type: NormalExercise
key: e7e25a89ea
lang: python
xp: 100
skills:
  - 2
```

你是一位超级棒球迷。你决定致电 MLB（美国职业棒球大联盟），询问有关主要球员身高的更多统计数据。他们提供了包含一千多名球员的数据，这些数据以普通 Python 列表的形式存储： `height_in`。球员的身高以英寸为单位。你能用它创建一个 `numpy` 数组并将单位转换为米吗？

`height_in` 已准备就绪，`numpy` 包也已加载完成，你可以直接上手了（数据来源：stat.ucla.edu）。

`@instructions`
- 使用 `height_in` 创建一个 `numpy` 数组。将这个新数组命名为 `np_height_in`。
- 打印 `np_height_in` 的输出结果。
- 将 `np_height_in` 乘以 `0.0254`，以便将所有身高测量值的单位从英寸转换为米。将新值保存到新数组 `np_height_m` 中。
- 打印 `np_height_m` 的输出结果，并检查输出是否合理。

`@hint`
- 使用 `np.array()` 并传入 `height`。将结果存储在 `np_height_in` 中。
- 要打印变量 `x` 的输出结果，只需在 Python 脚本中加上 `print(x)`。
- 像对待单个数值一样对 `np_height_in` 进行计算：`np_height_in * conversion_factor` 是解题的关键点之一。
- 要打印变量 `x` 的输出结果，只需在 Python 脚本中加上 `print(x)`。

`@pre_exercise_code`
```{python}
import pandas as pd
mlb = pd.read_csv("https://assets.datacamp.com/course/intro_to_python/baseball.csv")
height_in = mlb['Height'].tolist()
import numpy as np
```

`@sample_code`
```{python}
# Import numpy
import numpy as np

# Create a numpy array from height_in: np_height_in


# Print out np_height_in


# Convert np_height_in to m: np_height_m


# Print np_height_m

```

`@solution`
```{python}
# Import numpy
import numpy as np

# Create a numpy array from height_in: np_height_in
np_height_in = np.array(height_in)

# Print out np_height_in
print(np_height_in)

# Convert np_height_in to m: np_height_m
np_height_m = np_height_in * 0.0254

# Print np_height_m
print(np_height_m)
```

`@sct`
```{python}
Ex().has_import("numpy", same_as = False)

Ex().check_correct(
  has_printout(0),
  check_correct(
    check_object('np_height_in').has_equal_value(),
    check_function('numpy.array').check_args(0).has_equal_ast()
  )
)

Ex().check_correct(
  has_printout(1),
  check_object("np_height_m").has_equal_value(incorrect_msg = "使用 `np_height_in * 0.0254` 来计算 `np_height_m`。")
)

success_msg("很好！在眨眼之间，`numpy` 对超过 1000 个高度测量值进行了乘法运算。")
```

---

## NumPy 的一些"副作用"

```yaml
type: MultipleChoiceExercise
key: 3662ff6637
lang: python
xp: 50
skills:
  - 2
```

`numpy` 非常适合进行向量算术运算。但是，如果你将它的功能与常规 Python 列表进行比较，就会发现一些不同之处。

首先，`numpy` 数组不能包含不同类型的元素。如果你混用不同的数据类型（例如布尔值和整数），`numpy` 会自动将它们转换为通用类型。当布尔值（`True` 和 `False`）与数字结合运算时，它们会被视为 `1` 和 `0`，因此该数组最终会转换为整数类型。

其次，典型的算术运算符（例如 `+`、`-`、`*` 和 `/`）对于常规 Python 列表和 `numpy` 数组具有不同的含义。

请选择会得到以下输出的代码：

```
np.array([True, 1, 2]) + np.array([3, 4, False])
```

`numpy` 包已通过 `np` 导入。你可以在 IPython Shell 中运行每个选项，查看其输出。

`@possible_answers`
- `np.array([True, 1, 2, 3, 4, False])`
- `np.array([4, 3, 0]) + np.array([0, 2, 2])`
- `np.array([1, 1, 2]) + np.array([3, 4, -1])`
- `np.array([0, 1, 2, 3, 4, 5])`

`@hint`
- 复制不同的代码块并将其粘贴到 IPython Shell 中。按下回车键来运行代码，查看哪个输出与 `np.array([True, 1, 2]) + np.array([3, 4, False])` 所生成的输出相匹配。

`@pre_exercise_code`
```{python}
import numpy as np
```

`@sct`
```{python}
msg1 = msg3 = msg4 = "不正确。尝试不同的代码块，看看哪个与目标代码块匹配。"
msg2 = "做得好！`True` 被转换为 1，`False` 被转换为 0。"
Ex().has_chosen(2, [msg1, msg2, msg3, msg4])
```

---

## 提取 NumPy 数组子集

```yaml
type: NormalExercise
key: fcb2a9007b
lang: python
xp: 100
skills:
  - 2
```

子集提取操作（也就是在列表或数组后面使用方括号来取值）在列表和数组中的用法完全一样。

本练习已在后台加载 `height_in` 和 `weight_lb` 这两个列表。它们是普通列表，其中存放着 MLB 球员的身高和体重。练习还为你准备好了两个 `numpy` 数组：`np_weight_lb` 和 `np_height_in`。

`@instructions`
- 通过打印索引为 50 的元素来从 `np_weight_lb` 中提取子集。
- 打印 `np_height_in` 的一个子数组，其中包含从索引 100 到 110（包含索引 110）的元素。

`@hint`
- 确保将子集提取操作包含在 `print()` 调用中。
- 使用 `[100:111]` 来获取从索引 100 到 110（包含索引 110）的元素。

`@pre_exercise_code`
```{python}
import pandas as pd
mlb = pd.read_csv("https://assets.datacamp.com/course/intro_to_python/baseball.csv")
height_in = mlb['Height'].tolist()
weight_lb = mlb['Weight'].tolist()
```

`@sample_code`
```{python}
import numpy as np

np_weight_lb = np.array(weight_lb)
np_height_in = np.array(height_in)

# Print out the weight at index 50


# Print out sub-array of np_height_in: index 100 up to and including index 110

```

`@solution`
```{python}
import numpy as np

np_weight_lb = np.array(weight_lb)
np_height_in = np.array(height_in)

# Print out the weight at index 50
print(np_weight_lb[50])

# Print out sub-array of np_height_in: index 100 up to and including index 110
print(np_height_in[100:111])
```

`@sct`
```{python}
Ex().has_import("numpy", same_as=False)
msg = "您不必更改或删除预定义变量。"
Ex().multi(
    check_object("np_height_in", missing_msg=msg).has_equal_value(incorrect_msg = msg),
    check_object("np_weight_lb", missing_msg=msg).has_equal_value(incorrect_msg = msg)
)

Ex().has_printout(0)
Ex().has_printout(1)

success_msg("很好！是时候学习新内容了：二维 NumPy 数组！")
```

---

## 二维 NumPy 数组

```yaml
type: VideoExercise
key: 1241efac7a
xp: 50
```

`@projector_key`
ae3238dcc7feb9adecfee0c395fc8dc8

---

## 编写第一个二维 NumPy 数组

```yaml
type: NormalExercise
key: 5cb045bb13
lang: python
xp: 100
skills:
  - 2
```

在处理实际的 MLB 数据之前，我们先试着使用一个简短的“嵌套列表”来创建一个二维 `numpy` 数组。

在本练习中，`baseball` 就是一个嵌套列表。主列表包含 4 个元素。其中的每个元素都是一个依次包含 4 名棒球球员身高和体重的列表。脚本中已为你编写好了 `baseball`。

`@instructions`
- 使用 `np.array()` 将 `numpy` 转换为二维 `baseball` 数组，将其命名为 `np_baseball`。
- 打印 `np_baseball` 的数据类型。
- 打印 `np_baseball` 的 `shape` 属性。请使用 `np_baseball.shape`。

`@hint`
- 脚本中已为你编写好 `baseball`。对其调用 `np.array()`，并将得到的二维 `numpy` 数组存储在 `np_baseball` 中。
- 对于第二条指令，将 `print()` 与 `type()` 结合使用。
- 调用 `np_baseball.shape` 可获取 `np_baseball` 的维度。记得要将其包含在 `print()` 调用中。

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
import numpy as np

baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

# Create a 2D numpy array from baseball: np_baseball


# Print out the type of np_baseball


# Print out the shape of np_baseball

```

`@solution`
```{python}
import numpy as np

baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

# Create a 2D numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out the type of np_baseball
print(type(np_baseball))

# Print out the shape of np_baseball
print(np_baseball.shape)
```

`@sct`
```{python}
msg = "您不需要更改或删除预定义的变量。"
Ex().check_object("baseball", missing_msg=msg).has_equal_value(incorrect_msg = msg)
Ex().has_import("numpy", same_as = False)

Ex().check_correct(
    multi(
        has_printout(0),
        has_printout(1)
    ),
    check_correct(
        check_object('np_baseball').has_equal_value(),
        check_function('numpy.array').check_args(0).has_equal_ast()
    )
)

success_msg("太好了！您现在可以将实际的MLB数据转换为二维`numpy`数组了！")
```

---

## 二维形式的棒球数据

```yaml
type: NormalExercise
key: 5df25d0b7b
lang: python
xp: 100
skills:
  - 2
```

你发现，将这些信息重构成一个二维 `numpy` 数组更合理。

你有一个由列表组成的 Python 列表（嵌套列表）。在这个嵌套列表中，每个子列表分别代表一位棒球球员的身高和体重。该列表的名称为 `baseball`，并且已经提前加载好（虽然你看不到它）。

将数据存储为二维数组，以便使用 `numpy` 的更多功能。

`@instructions`
- 使用 `np.array()` 将 `baseball` 转换为二维 `numpy` 数组，并命名为 `np_baseball`。
- 打印 `np_baseball` 的 `shape` 属性。

`@hint`
- `baseball` 在 Python 环境中已经可用。对其调用 `np.array()`，并将得到的二维 `numpy` 数组存储在 `np_baseball` 中。
- 使用 `np_baseball.shape` 即可获得 `np_baseball` 的维度。记得将其包含在 `print()` 调用中。

`@pre_exercise_code`
```{python}
import pandas as pd
baseball = pd.read_csv("https://assets.datacamp.com/course/intro_to_python/baseball.csv")[['Height', 'Weight']].to_numpy().tolist()
import numpy as np
```

`@sample_code`
```{python}
import numpy as np

# Create a 2D numpy array from baseball: np_baseball
np_baseball = 

# Print out the shape of np_baseball

```

`@solution`
```{python}
import numpy as np

# Create a 2D numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out the shape of np_baseball
print(np_baseball.shape)
```

`@sct`
```{python}
Ex().has_import("numpy", same_as = False)

Ex().check_correct(
    has_printout(0),
    check_correct(
        check_object('np_baseball').has_equal_value(),
        check_function('numpy.array').check_args(0).has_equal_ast()
    )
)

success_msg("太棒了！是时候展示一些多维 `numpy` 数组的强大功能了！")
```

---

## 二维 NumPy 数组的子集提取

```yaml
type: NormalExercise
key: aeca4977f0
lang: python
xp: 100
skills:
  - 2
```

如果你的二维 `numpy` 数组结构规整，即每一行和每一列都包含固定数量的数值，复杂的子集提取操作就会变得非常简单。请看下面的代码，其中元素 `"a"` 和 `"c"` 是从一个嵌套列表中提取出来的。

```
# numpy
import numpy as np
np_x = np.array(x)
np_x[:, 0]
```

逗号前的索引代表“行”，逗号后的索引代表“列”。冒号 `:` 表示切片；在此示例中，它的意思是让 Python 选择所有行。

`@instructions`
- 打印 `np_baseball` 的第 50 行。
- 创建一个新变量 `np_weight_lb`，用来提取 `np_baseball` 的整个第二列。
- 选择 `np_baseball` 中第 124 位棒球球员的身高（第一列）并打印出来。

`@hint`
- 对于第一行指令，你需要使用行索引 49！更具体地说，你需要使用 `[49, :]`。
- 要选择整个第二列，你需要使用 `[:, 1]`。
- 对于最后一条指令，使用 `[123, 0]`；别忘记将整行代码包含在 `print()` 语句中。

`@pre_exercise_code`
```{python}
import pandas as pd
baseball = pd.read_csv("https://assets.datacamp.com/course/intro_to_python/baseball.csv")[['Height', 'Weight']].to_numpy().tolist()
import numpy as np
```

`@sample_code`
```{python}
import numpy as np

np_baseball = np.array(baseball)

# Print out the 50th row of np_baseball


# Select the entire second column of np_baseball: np_weight_lb


# Print out height of 124th player

```

`@solution`
```{python}
import numpy as np

np_baseball = np.array(baseball)

# Print out the 50th row of np_baseball
print(np_baseball[49,:])

# Select the entire second column of np_baseball: np_weight_lb
np_weight_lb = np_baseball[:,1]

# Print out height of 124th player
print(np_baseball[123, 0])
```

`@sct`
```{python}
msg = "您不必更改或删除预定义的变量。"
Ex().multi(
    has_import("numpy", same_as = False),
    check_object("np_baseball", missing_msg=msg).has_equal_value(incorrect_msg = msg)
)

Ex().has_printout(0)

Ex().check_object('np_weight_lb').has_equal_value(incorrect_msg = "您可以使用 `np_baseball[:,1]` 来定义 `np_weight_lb`。这将选择整个第一列。")

Ex().has_printout(1)

success_msg("进展顺利！")
```

---

## 二维数组的数学运算

```yaml
type: NormalExercise
key: 1c2378b677
lang: python
xp: 100
skills:
  - 2
```

二维 `numpy` 数组可以像一维 `numpy` 数组一样，逐元素执行计算。

`np_baseball` 已提前编写好；它是一个二维 `numpy` 数组，包含 3 列，分别代表身高（英寸）、体重（磅）和年龄（岁）。`baseball` 可作为常规嵌套列表使用，`updated` 可作为二维 numpy 数组使用。

`@instructions`
- 你已经成功获取了所有棒球球员身高、体重和年龄的变化数据。这些数据存储在二维 `numpy` 数组 `updated` 中。将 `np_baseball` 与 `updated` 相加并打印结果。
- 你想把身高和体重的单位转换为公制（分别为米和公斤）。第一步，创建一个包含三个数值 `0.0254`、`0.453592` 和 `1` 的 `numpy` 数组，将其命名为 `conversion`。
- 将 `np_baseball` 与 `conversion` 相乘并打印结果。

`@hint`
- `np_baseball + updated` 会对这两个 `numpy` 数组进行逐元素相加。
- 使用 `numpy` 创建一个 `np.array()` 数组；其输入是一个包含三个元素的常规 Python 列表。
- 你可以直接使用 `np_baseball * conversion`，无需额外操作。试试看！记得将其包含在 `print()` 调用中。

`@pre_exercise_code`
```{python}
import pandas as pd
import numpy as np
baseball = pd.read_csv("https://assets.datacamp.com/course/intro_to_python/baseball.csv")[['Height', 'Weight', 'Age']].to_numpy().tolist()
n = len(baseball)
updated = np.array(pd.read_csv("https://assets.datacamp.com/course/intro_to_python/update.csv", header = None))
import numpy as np
```

`@sample_code`
```{python}
import numpy as np

np_baseball = np.array(baseball)

# Print out addition of np_baseball and updated


# Create numpy array: conversion


# Print out product of np_baseball and conversion

```

`@solution`
```{python}
import numpy as np

np_baseball = np.array(baseball)

# Print out addition of np_baseball and updated
print(np_baseball + updated)

# Create numpy array: conversion
conversion = np.array([0.0254, 0.453592, 1])

# Print out product of np_baseball and conversion
print(np_baseball * conversion)
```

`@sct`
```{python}
Ex().has_import("numpy")

msg = "您不需要更改或删除预定义的变量。"
Ex().check_object("np_baseball", missing_msg=msg).has_equal_value(incorrect_msg = msg)

Ex().has_printout(0)

Ex().check_correct(
    has_printout(1),
    check_correct(
        check_object('conversion').has_equal_value(),
        check_function('numpy.array', index = 1).check_args(0).has_equal_value()
    )    
)

success_msg("做得好！请注意，使用很少的代码，您可以以非常具体的方式更改 `numpy` 数据结构中的所有值。这在您未来作为数据科学家的职业生涯中将非常有用！")
```

---

## NumPy：基础统计学

```yaml
type: VideoExercise
key: 287995e488
xp: 50
```

`@projector_key`
34495ba457d74296794d2a122c9b6e19

---

## 平均值与中位数

```yaml
type: NormalExercise
key: 509c588eb6
lang: python
xp: 100
skills:
  - 2
```

现在，你已经学会了怎么使用 `numpy` 的函数来更好地理解数据。

棒球数据存放在一个二维 `numpy` 数组中，共有 3 列（身高、体重、年龄）和 1015 行。该 `numpy` 数组名为 `np_baseball`。不过，在重构数据后，你发现有些身高值异常高。那么，你可以按照指令操作，探索在处理所谓的异常值 (_outliers_) 时，哪种汇总统计指标更合适。`np_baseball` 已提前准备好。

`@instructions`
- 创建 `numpy` 数组 `np_height_in`，它等于 `np_baseball` 的第一列。
- 打印输出 `np_height_in` 的平均值。
- 打印输出 `np_height_in` 的中位数。

`@hint`
- 使用二维 `numpy` 提取子集：`[:,0]` 是解题关键点之一。
- 如果将 `numpy` 导入为 `np`，可以使用 `np.mean()` 计算 NumPy 数组的平均值。别忘记将其包含在 `print()` 调用中。
- 对于最后一条指令，请使用 `np.median()`。

`@pre_exercise_code`
```{python}
import pandas as pd
np_baseball = pd.read_csv("https://assets.datacamp.com/course/intro_to_python/baseball.csv")[['Height', 'Weight', 'Age']].to_numpy()
np_baseball[slice(0, 1015, 50), 0] = np_baseball[slice(0, 1015, 50), 0]*1000
import numpy as np
```

`@sample_code`
```{python}
import numpy as np

# Create np_height_in from np_baseball


# Print out the mean of np_height_in


# Print out the median of np_height_in

```

`@solution`
```{python}
import numpy as np

# Create np_height_in from np_baseball
np_height_in = np_baseball[:,0]

# Print out the mean of np_height_in
print(np.mean(np_height_in))

# Print out the median of np_height_in
print(np.median(np_height_in))
```

`@sct`
```{python}
Ex().has_import("numpy", same_as = False)

Ex().check_object("np_height_in").has_equal_value(incorrect_msg = "您可以使用 `np_baseball[:,0]` 从 `np_baseball` 中选择第一列"),

Ex().check_correct(
    has_printout(0),
    check_function('numpy.mean').has_equal_value()
)

Ex().check_correct(
    has_printout(1),
    check_function('numpy.median').has_equal_value()
)

success_msg("平均身高为 1586 英寸，这听起来不太对，是吗？然而，中位数似乎不受异常值的影响：74 英寸非常合理。检查中位数和平均值以了解整个数据集的总体分布始终是个好主意。")
```

---

## 探索棒球数据

```yaml
type: NormalExercise
key: '4409948807'
lang: python
xp: 100
skills:
  - 2
```

由于均值和中位数相差甚远，您决定向 MLB 投诉。他们找到了错误并将更正后的数据发送给了你。这些数据同样以包含三列的二维 NumPy 数组 `np_baseball` 提供。

编辑器中的 Python 脚本已经编写好了用于打印包含不同汇总统计信息的提示代码，并且 `numpy` 也已经使用 `np` 导入。你能把剩下的代码补充完整吗？`np_baseball` 已准确就绪。

`@instructions`
- 打印平均身高的代码已包含在内。请把计算身高中位数的代码补充完整。
- 对 `np_baseball` 的第 1 列调用 `np.std()` 来计算 `stddev`。
- 身材高大的球员体重往往也更重吗？使用 `np.corrcoef()` 计算 `np_baseball` 第 1 列与第 2 列之间的相关系数，并将结果存储到 `corr` 中。

`@hint`
- 使用 `np.median()` 计算中位数。首先要确保选择正确的列！
- 使用 `np.std()` 计算标准差时，要对同一列提取子集。
- 使用 `np_baseball[:, 0]` 和 `np_baseball[:, 1]` 选择第 1 列和第 2 列；它们是传递给 `np.corrcoef()` 的输入。

`@pre_exercise_code`
```{python}
import pandas as pd
np_baseball = pd.read_csv("https://assets.datacamp.com/course/intro_to_python/baseball.csv")[['Height', 'Weight', 'Age']].to_numpy()
import numpy as np
```

`@sample_code`
```{python}
avg = np.mean(np_baseball[:,0])
print("Average: " + str(avg))

# Print median height
med = ____
print("Median: " + str(med))

# Print out the standard deviation on height
stddev = ____
print("Standard Deviation: " + str(stddev))

# Print out correlation between first and second column
corr = ____
print("Correlation: " + str(corr))
```

`@solution`
```{python}
avg = np.mean(np_baseball[:,0])
print("Average: " + str(avg))

# Print median height
med = np.median(np_baseball[:,0])
print("Median: " + str(med))

# Print out the standard deviation on height
stddev = np.std(np_baseball[:,0])
print("Standard Deviation: " + str(stddev))

# Print out correlation between first and second column
corr = np.corrcoef(np_baseball[:,0], np_baseball[:,1])
print("Correlation: " + str(corr))
```

`@sct`
```{python}
msg = "您不应更改或删除预定义的 `avg` 变量。"
Ex().check_object("avg", missing_msg=msg).has_equal_value(incorrect_msg=msg)

missing = "您是否使用了 `np.median()` 来计算中位数？"
incorrect = "要计算 `med`，请将 `np_baseball` 的第一列传递给 `numpy.median()`。`np.mean()` 的示例展示了如何完成此操作。"
Ex().check_correct(
  check_object("med").has_equal_value(),
  check_function("numpy.median", index=0, missing_msg=missing).check_args(0).has_equal_value(incorrect_msg=incorrect)
)

missing = "您是否使用了 `np.std()` 来计算标准差？"
incorrect = "要计算 `stddev`，请将 `np_baseball` 的第一列传递给 `numpy.std()`。`np.mean()` 的示例展示了如何完成此操作。"
Ex().check_correct(
  check_object("stddev").has_equal_value(),
  check_function("numpy.std", index=0, missing_msg=missing).check_args(0).has_equal_value(incorrect_msg=incorrect)
)

missing = "您是否使用了 `np.corrcoef()` 来计算相关性？"
incorrect1 = "要计算 `corr`，`np.corrcoef()` 的第一个参数应为 `np_baseball` 的第一列，类似于之前的操作。"
incorrect2 = "要计算 `corr`，`np.corrcoef()` 的第二个参数应为 `np_baseball` 的第二列。此时应使用 `[:,1]` 而不是 `[:,0]`。"
Ex().check_correct(
  check_object("corr").has_equal_value(),
  check_function("numpy.corrcoef", index=0, missing_msg=missing).multi(
    check_args(0, missing_msg=incorrect1).has_equal_value(incorrect_msg=incorrect1),
    check_args(1, missing_msg=incorrect2).has_equal_value(incorrect_msg=incorrect2)
  )
)

success_msg("干得好！您已经打下了坚实的基础——现在是时候运用您所有的新数据科学技能来解决更多挑战并产生影响了。")
```

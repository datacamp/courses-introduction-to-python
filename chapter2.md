---
title_meta: 第 2 章
title: Python 列表
description: 学习在列表中存储、访问和操作数据：这是高效处理海量数据的第一步。
attachments:
  slides_link: 'https://projector-video-pdf-converter.datacamp.com/735/chapter2.pdf'
lessons:
  - nb_of_exercises: 4
    title: Python 列表
  - nb_of_exercises: 4
    title: 获取列表子集
  - nb_of_exercises: 5
    title: 操作列表
---

## Python 列表

```yaml
type: VideoExercise
key: a5886d213f
xp: 50
```

`@projector_key`
a0530c4542f10988847b2dbb91f717c3

---

## 创建列表

```yaml
type: NormalExercise
key: e6c527bf41
lang: python
xp: 100
skills:
  - 2
```

列表是一种**复合数据类型**，你可以像下面这样把多个值组合在一起：

```
a = "is"
b = "nice"
my_list = ["my", "list", a, b]
```

在测量完家人的身高后，你决定收集一些关于你所居住房屋的信息。房子不同区域的面积已保存在本练习的不同变量中。

`@instructions`
- 使用预定义变量，按以下顺序创建包含门厅 (`hall`)、厨房 (`kit`)、客厅 (`liv`)、卧室 (`bed`) 和浴室 (`bath`) 面积的列表 (`areas`)。
- 使用 `print()` 函数打印 `areas`。

`@hint`
- 你可以使用之前已经创建好的变量来构建列表：`areas = [hall, kit, ...]`。
- 确保使用方括号 `[]`，而不是圆括号 `()`。
- 在列表中存储变量时不需要使用引号。
- 提交时输入 `print(areas)`，以便打印列表。

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Create list areas


# Print areas

```

`@solution`
```{python}
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Create list areas
areas = [hall, kit, liv, bed, bath]

# Print areas
print(areas)
```

`@sct`
```{python}
predef_msg = "不要删除或编辑预定义变量！"
areas_msg = "将 `areas` 定义为包含所有区域变量的列表，顺序正确：[hall, kit, liv, bed, bath]。注意拼写错误。列表不应包含其他内容！"

Ex().check_correct(
    has_printout(0, not_printed_msg = "__JINJA__:您是否在脚本末尾使用 `{{sol_call}}` 打印出 `areas` 列表？"),
    check_correct(
        check_object("areas").has_equal_value(incorrect_msg = areas_msg),
        multi(
            check_object('hall', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
            check_object('kit', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
            check_object('liv', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
            check_object('bed', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
            check_object('bath', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg)
        )
    )
)

success_msg("很好！在这里使用列表是不是更好？")
```

---

## 创建包含不同数据类型的列表

```yaml
type: NormalExercise
key: 1702a8bcdc
lang: python
xp: 100
skills:
  - 2
```

尽管不太常见，但在 Python 中，同一个列表其实可以混用多种不同的数据类型，比如字符串、浮点数和布尔值。

现在，你可以将房间名称添加到列表中，以便轻松将房间名称和大小放在一起查看。

我们已经为你写好了一部分代码。请留心这里：`"bathroom"` 是一个字符串，而 `bath` 是一个变量，代表你之前定义的浮点数 `9.50`。

`@instructions`
- 将创建 `areas` 列表的代码补充完整。构建列表时，按“房间名称（字符串）+ 对应面积”的顺序交替排列。也就是说，把 `"hallway"`、`"kitchen"` 和 `"bedroom"` 这几个字符串填入对应的位置。
- 再次打印 `areas`；这次的输出结果是不是更直观清晰了？

`@hint`
- 列表 `areas` 的前四个元素编码为 `["hallway", hall, "kitchen", kit, ...`。
- 字符串需要包含在引号 `""` 中。

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Adapt list areas
areas = [____, hall, ____, kit, "living room", liv, ____, bed, "bathroom", bath]

# Print areas
____
```

`@solution`
```{python}
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Adapt list areas
areas = ["hallway", hall, "kitchen", kit, "living room", liv, "bedroom", bed, "bathroom", bath]

# Print areas
print(areas)
```

`@sct`
```{python}
objs = ["hall", "kit", "liv", "bed", "bath"]
predef_msg = "不要删除或编辑预定义变量！"
areas_msg = "您没有为 `areas` 分配正确的值。请再看看说明。确保每次在包含面积的变量之前放置房间名称。顺序在这里很重要！注意拼写错误。"

Ex().check_correct(
  check_object("areas").has_equal_value(incorrect_msg = areas_msg),
  multi([ check_object(obj, missing_msg = predef_msg).has_equal_value(incorrect_msg = predef_msg) for obj in objs])
)

Ex().has_printout(0, not_printed_msg = "__JINJA__:您是否在脚本末尾使用了 `{{sol_call}}` 来打印 `areas` 列表？")

success_msg("很好！这个列表包含字符串和浮点数，但这对 Python 来说不是问题！")
```

---

## 列表的列表（嵌套列表）

```yaml
type: NormalExercise
key: 9158c577b0
lang: python
xp: 100
skills:
  - 2
```

作为一名数据科学家，你经常需要处理大量数据，将其中一些数据分组会带来很多方便。

你可以创建一个由列表组成的列表（嵌套列表），而不是创建一个包含字符串和浮点数（代表你房子内各个房间的名称和面积）的列表。

记住：`"hallway"` 是一个字符串，而 `hall` 是一个变量，表示你之前指定的浮点数 `11.25`。

`@instructions`
- 将这个嵌套列表补充完整，把卧室和浴室的数据加入进去。注意，务必要按顺序添加！
- 打印 `house`；用这种方式组织数据，是不是条理清晰多了？

`@hint`
- 通过在方括号内添加 `["bedroom", bed]` 和 `["bathroom", bath]`，将子列表 (_sublists_) 添加到 `house` 列表中。
- 记得在每个子列表后面加上逗号 `,`。
- 要打印变量 `x`，请在新的一行中加上 `print(x)`。

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# House information as list of lists
house = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv],
        ____,
        ____]

# Print out house
____
```

`@solution`
```{python}
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# House information as list of lists
house = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv],
         ["bedroom", bed],
         ["bathroom", bath]]

# Print out house
print(house)
```

`@sct`
```{python}
predef_msg = "不要删除或编辑预定义变量！"
house_msg = "您没有为 `house` 分配正确的值。请再看看说明。扩展列表以便为每对房间名称和房间面积包含一个列表。注意顺序和拼写错误！"

Ex().check_correct(
    check_object("house").has_equal_value(incorrect_msg = house_msg),
    multi(
        check_object('hall', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
        check_object('kit', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
        check_object('liv', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
        check_object('bed', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
        check_object('bath', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg)
    )
)

Ex().has_printout(0, not_printed_msg = "__JINJA__:您是否使用了 `{{sol_call}}` 来打印 `house` 的内容？")

success_msg("太棒了！准备学习列表子集！")
```

---

## 获取列表子集

```yaml
type: VideoExercise
key: c076b5a69c
xp: 50
```

`@projector_key`
fc15ba5cb9485456df8589130b519ea3

---

## 子集和切片

```yaml
type: NormalExercise
key: c3ce582e32
lang: python
xp: 100
skills:
  - 2
```

对 Python 列表进行子集提取非常简单。请参考下面的代码示例，它创建了一个列表 `x`，然后从中选择了 “b”。请记住，这是第二个元素，因此它的索引为 1。你也可以使用负索引。

```
x = ["a", "b", "c", "d"]
x[1]
x[-3] # same result!
```

还记得之前的 `areas` 列表吗？它同时包含字符串和浮点数。它已经在脚本中定义好了。你能添加适当的代码来进行 Python 子集提取吗？

`@instructions`
- 打印 `areas` 列表中的第二个元素（其值为 `11.25`）。
- 提取子集并打印 `areas` 的最后一个元素，即 `9.50`。这里更合适使用负索引！
- 选择代表客厅面积的数字 (`20.0`) 并将其打印出来。

`@hint`
- 使用 `x[1]` 选择列表 `x` 的第二个元素。
- 使用 `x[-1]` 选择列表 `x` 的最后一个元素。
- 将提取子集操作包含在 `print()` 调用中。
- 客厅面积对应的是列表中的第 6 个元素，因此这里需要使用 `[5]`。如果写成 `area[4]`，将显示一个字符串！

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Print out second element from areas
print(areas[____])

# Print out last element from areas
print(areas[____])

# Print out the area of the living room
print(areas[____])
```

`@solution`
```{python}
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Print out second element from areas
print(areas[1])

# Print out last element from areas
print(areas[-1])

# Print out the area of the living room
print(areas[5])
```

`@sct`
```{python}
msg = "不要删除或编辑预定义的 `areas` 列表。"
Ex().check_object("areas", missing_msg = msg).has_equal_value(incorrect_msg = msg)
Ex().has_printout(0, not_printed_msg = "再看看您的代码以打印出 `areas` 中的第二个元素，它位于索引 `1`。")
Ex().has_printout(1, not_printed_msg = "再看看您的代码以打印出 `areas` 中的最后一个元素，它位于索引 `-1`。")
Ex().has_printout(2, not_printed_msg = "再看看您的代码以打印出客厅的面积。它位于索引 `5`。")
success_msg("做得好！")
```

---

## 列表切片与分割

```yaml
type: NormalExercise
key: 7f08642d18
lang: python
xp: 100
skills:
  - 2
```

从列表里提取单个元素只是基本操作，你还可以对列表进行“切片”，也就是一次性从列表中选择多个元素。语法格式如下：

```
my_list[start:end]
```

`start` 索引包含在内，而 `end` 索引不包含在内。不过，这两个索引其实都可以省略。如果你不指定 `start` 索引，Python 会明白你是想从列表的开头开始切片。

`@instructions`
- 使用切片创建一个列表 `downstairs`，其中包含 `areas` 的前 6 个元素。
- 创建 `upstairs`，用于存放 `areas` 的后 `4` 个元素。这次记得省略 `end` 索引来简化切片语法。
- 使用 `print()` 打印 `downstairs` 和 `upstairs`。

`@hint`
- 使用方括号 `[0:6]` 来获取列表的前 6 个元素。
- 要获取列表 `l` 中除前 5 个元素外的所有元素，可使用 `l[5:]`。
- 添加两个 `print()` 调用来打印 `downstairs` 和 `upstairs`。

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Use slicing to create downstairs
downstairs = areas[____]

# Use slicing to create upstairs
upstairs = areas[____]

# Print out downstairs and upstairs
____
____
```

`@solution`
```{python}
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Use slicing to create downstairs
downstairs = areas[0:6]

# Use slicing to create upstairs
upstairs = areas[6:]

# Print out downstairs and upstairs
print(downstairs)
print(upstairs)
```

`@sct`
```{python}
msg = "请勿删除或编辑预定义的 `areas` 列表。"
Ex().check_object("areas", missing_msg = msg).has_equal_value(incorrect_msg = msg)

patt = "`%s` 不正确。请使用 `areas[%s]` 和切片来选择您想要的元素，或使用等效的方法。"
Ex().check_object("downstairs").has_equal_value(incorrect_msg = patt % ('downstairs', '0:6'))
Ex().check_object("upstairs").has_equal_value(incorrect_msg = patt % ("upstairs",":6"))

Ex().has_printout(0, not_printed_msg="您是否在计算 `downstairs` 后打印出来了？")
Ex().has_printout(1, not_printed_msg="您是否在计算 `upstairs` 后打印出来了？")

success_msg("做得好！")
```

---

## 对嵌套列表提取子集

```yaml
type: NormalExercise
key: dbbbd306cf
xp: 100
```

Python 列表可以包含其他列表，这就是所谓的嵌套列表。

要对嵌套列表提取子集，你同样可以使用方括号。对于列表 `house`，语法就像这样：

```
house[2][0]
```

`@instructions`
- 从 `house` 列表中获取浮点数 `9.5`。

`@hint`
- 我们一步步拆解这个问题。首先，你需要获取列表的最后一个元素 `["bathroom", 9.50]`。回忆一下，最后一个元素的索引是 `-1`。
- 接着，你需要获取 `["bathroom", 9.50]` 中的第二个元素，它的索引是 `1`。

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
house = [["hallway", 11.25],
         ["kitchen", 18.0],
         ["living room", 20.0],
         ["bedroom", 10.75],
         ["bathroom", 9.50]]

# Subset the house list
house___
```

`@solution`
```{python}
house = [["hallway", 11.25],
         ["kitchen", 18.0],
         ["living room", 20.0],
         ["bedroom", 10.75],
         ["bathroom", 9.50]]

# Subset the house list
house[-1][1]
```

`@sct`
```{python}
Ex().check_or(
  has_code("house[-1][1]", pattern=False),
  has_code("house[4][1]", pattern=False)
)

success_msg("正确！列表拼图的最后一块是操作。")
```

---

## 操作列表

```yaml
type: VideoExercise
key: d7fe818b3a
xp: 50
```

`@projector_key`
355ed52d2fb0d67508c6a311b7cbc6d3

---

## 替换列表元素

```yaml
type: NormalExercise
key: 4e1bba1b55
lang: python
xp: 100
skills:
  - 2
```

要替换列表元素，你可以对列表提取子集，然后向该子集分配新值。你可以选择单个元素，也可以一次性更改整个列表切片。

对于本练习以及后续练习，你将继续使用包含房屋内不同房间名称和面积的 `areas` 列表进行操作。

`@instructions`
- 使用负索引将浴室面积从 `9.50` 平方米更新为 `10.50` 平方米。
- 想让 `areas` 列表更潮一些？你可以把 `"living room"` 改为 `"chill zone"`。这次记得不要使用负索引。

`@hint`
- 要更新浴室面积，先找到它在列表中的对应位置（就是列表中的最后一项！）。
- 然后把新的浴室面积赋值给这个位置，完成值的替换。
- 执行相同的操作来更新位于索引 4 处的名称 `"living room"`。

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Correct the bathroom area


# Change "living room" to "chill zone"

```

`@solution`
```{python}
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Correct the bathroom area
areas[-1] = 10.50

# Change "living room" to "chill zone"
areas[4] = "chill zone"
```

`@sct`
```{python}
bathroom_msg = '您可以使用 `areas[-1] = 10.50` 来更新浴室面积。'
chillzone_msg = '您可以使用 `areas[4] = "chill zone"` 来更新客厅名称。'
Ex().check_correct(
  check_object('areas').has_equal_value(incorrect_msg = '您对 `areas` 的更改未能生成正确的列表。您确定使用了正确的子集操作吗？如有疑问，您可以使用提示！'),
  multi(
    has_equal_value(expr_code='areas[-1]', override=10.50, incorrect_msg = bathroom_msg),
    has_equal_value(expr_code='areas[4]', override='chill zone', incorrect_msg = chillzone_msg),
  )
)
success_msg('太棒了！正如代码示例所示，您还可以对列表进行切片，并用另一个列表替换它，以便在单个命令中更新多个元素。')
```

---

## 扩展列表

```yaml
type: NormalExercise
key: ff0fe8d967
lang: python
xp: 100
skills:
  - 2
```

既然你可以修改列表中的元素，那么自然也会希望能在列表中添加元素，对吧？使用 `+` 运算符就能实现：

```
x = ["a", "b", "c", "d"]
y = x + ["e", "f"]
```

你中了彩票，太棒了！你决定建一个泳池小屋 (poolhouse) 和一个车库 (garage)。你能把这些信息添加到 `areas` 列表中吗？

`@instructions`
- 使用 `+` 运算符将列表 `["poolhouse", 24.5]` 拼接到 `areas` 列表末尾。将结果列表存储到 `areas_1` 中。
- 继续扩展 `areas_1`，添加关于车库的数据。添加字符串 `"garage"` 和浮点数 `15.45`。将结果列表命名为 `areas_2`。

`@hint`
- 按题目中的示例代码来编写。这里的 `x` 就是 `areas`，而 `["e", "f"]` 就是 `["poolhouse", 24.5]`。
- 要向 `areas_1` 添加更多元素，请使用 `areas_1 + ["element", 123]`。

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create the areas list and make some changes
areas = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0,
         "bedroom", 10.75, "bathroom", 10.50]

# Add poolhouse data to areas, new list is areas_1
areas_1 = ____

# Add garage data to areas_1, new list is areas_2
areas_2 = ____
```

`@solution`
```{python}
# Create the areas list (updated version)
areas = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0,
         "bedroom", 10.75, "bathroom", 10.50]

# Add poolhouse data to areas, new list is areas_1
areas_1 = areas + ["poolhouse", 24.5]

# Add garage data to areas_1, new list is areas_2
areas_2 = areas_1 + ["garage", 15.45]
```

`@sct`
```{python}
msg = "不要删除或编辑预定义的 `areas` 列表。"
Ex().check_object("areas", missing_msg = msg).has_equal_value(incorrect_msg = msg)
Ex().check_object("areas_1").has_equal_value(incorrect_msg = "使用 `areas + [\"poolhouse\", 24.5]` 来创建 `areas_1`。注意拼写错误！")
Ex().check_object("areas_2").has_equal_value(incorrect_msg = "使用 `areas_1 + [\"garage\", 15.45]` 来创建 `areas_2`。注意拼写错误！")
success_msg("很好！列表正在成形！")
```

---

## 删除列表元素

```yaml
type: NormalExercise
key: 85f792356e
xp: 100
```

最后，你还可以从列表中删除元素。使用 `del` 语句即可实现：

```
x = ["a", "b", "c", "d"]
del x[1]
```

注意：一旦从列表中删除某个元素，该元素后所有元素的索引都会改变！

可惜的是，你中的彩票奖金并没有想象中那么多，看来建泳池小屋的计划要泡汤了。你需要把它从列表中删除。于是，你决定从 `areas` 列表中删除对应的字符串和浮点数。

`@instructions`
- 从你的 `areas` 列表中删除 `"poolhouse"` 对应的字符串和浮点数。
- 打印更新后的 `areas` 列表。

`@hint`
- 你需要调用 `del` 两次来删除两个元素。不过要注意：索引在删除元素后会发生变化！

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
areas = ["hallway", 11.25, "kitchen", 18.0,
        "chill zone", 20.0, "bedroom", 10.75,
         "bathroom", 10.50, "poolhouse", 24.5,
         "garage", 15.45]

# Delete the poolhouse items from the list


# Print the updated list

```

`@solution`
```{python}
areas = ["hallway", 11.25, "kitchen", 18.0,
        "chill zone", 20.0, "bedroom", 10.75,
         "bathroom", 10.50, "poolhouse", 24.5,
         "garage", 15.45]

# Delete the poolhouse items from the list
del areas[10]
del areas[10]

# Print the updated list
print(areas)
```

`@sct`
```{python}
Ex().check_or(
  multi(
    has_code("del areas[10]", pattern=False),
    has_code("del areas[10]", pattern=False)
  ),
  has_code("del areas[-4:-2]", pattern=False),
  has_code("del(areas[-4:-2])", pattern=False),
  multi(
    has_code("del(areas[10])", pattern=False),
    has_code("del(areas[10])", pattern=False)
  ),
  has_code("del areas[10:12]", pattern=False),
  has_code("del(areas[10:12])", pattern=False),
  multi(
    has_code("del areas[-4]", pattern=False),
    has_code("del areas[-3]", pattern=False)
  ),
  multi(
    has_code("del(areas[-4])", pattern=False),
    has_code("del(areas[-3])", pattern=False)
  )
)

Ex().has_printout(0, not_printed_msg="您是否在删除 poolhouse 字符串和浮点数后打印了 `areas`？")
success_msg("正确！稍后您将学习更简单的方法来从 Python 列表中删除特定元素。")
```

---

## 列表的底层机制

```yaml
type: NormalExercise
key: af72db9915
lang: python
xp: 100
skills:
  - 2
```

本练习为你提供了一些示例代码：一个名为 `areas` 的列表，以及一个名为 `areas_copy` 的副本。

目前的代码修改了 `areas_copy` 列表中的第一个元素，并打印出了 `areas` 列表。如果你点击运行代码按钮，就会发现虽然你修改的是 `areas_copy`，但这种修改在 `areas` 列表中也生效了。这是因为 `areas` 和 `areas_copy` 指向的是同一个列表。

如果你希望在修改 `areas_copy` 时不影响 `areas`，就必须使用 `list()` 或 `[:]` 来对 `areas` 列表进行更显式的复制。

`@instructions`
- 修改用于创建变量 `areas_copy` 的第二个命令，使 `areas_copy` 成为 `areas` 的显式副本。完成修改后，对 `areas_copy` 所做的更改就不会影响 `areas` 了。你可以提交答案来进行验证。

`@hint`
- 修改一下 `areas_copy = areas` 这行代码。不要直接赋值 `areas`，可以改为赋值 `list(areas)` 或 `areas[:]`。

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Change this command
areas_copy = areas

# Change areas_copy
areas_copy[0] = 5.0

# Print areas
print(areas)
```

`@solution`
```{python}
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Change this command
areas_copy = list(areas)

# Change areas_copy
areas_copy[0] = 5.0

# Print areas
print(areas)
```

`@sct`
```{python}
Ex().check_correct(
  check_object("areas_copy").has_equal_value(incorrect_msg = "看起来 `areas_copy` 没有被正确更新。"),
  check_function("list", missing_msg = "确保使用 `list(areas)` 来创建一个 `areas_copy`。")
)

mmsg = "不要移除预定义的 `areas` 列表。"
imsg = "确保只编辑副本，而不是原始的 `areas` 列表。如果不确定如何创建副本，请再看看练习描述。"
Ex().check_correct(
  check_object("areas", missing_msg = mmsg).has_equal_value(incorrect_msg = imsg),
  check_function("list", missing_msg = "确保使用 `list(areas)` 来创建一个 `areas_copy`。")
)

success_msg("很好！显式和基于引用的副本之间的区别很微妙，但可能非常重要。请记住列表在计算机内存中的存储方式。")
```

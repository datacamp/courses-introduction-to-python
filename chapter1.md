---
title_meta: 第 1 章
title: Python 基礎知識
description: Python 基礎概念簡介。學習如何以互動方式或透過腳本來使用 Python。你將建立自己的第一個變數，並熟悉 Python 的基本資料類型。
attachments:
  slides_link: 'https://projector-video-pdf-converter.datacamp.com/735/chapter1.pdf'
free_preview: true
lessons:
  - nb_of_exercises: 3
    title: 你好，Python！
  - nb_of_exercises: 5
    title: 變數與資料類型
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

## 你的第一段 Python 程式碼

```yaml
type: NormalExercise
key: bdc52f0e19
lang: python
xp: 100
skills:
  - 2
```

是時候執行你的第一段 Python 程式碼了！

前往程式碼編輯區域，按下「執行程式碼」按鈕以查看輸出結果。

`@instructions`
- 按下「執行程式碼」按鈕，查看 `print(5 / 8)` 的輸出結果。

`@hint`
- 在送出答案前先執行程式碼，以便有時間研究輸出結果。

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
Ex().has_printout(0, not_printed_msg = "__JINJA__:您是否使用 `{{sol_call}}` 來列印 `5 / 8`？")
success_msg("太好了！繼續下一題！")
```

---

## 把 Python 當計算器使用

```yaml
type: NormalExercise
key: 0f7c039428
lang: python
xp: 100
skills:
  - 2
```

Python 非常適合進行基本計算。它可以實現加、減、乘、除運算。

腳本程式碼中提供了幾個範例。

現在輪到你寫一些程式碼來練習一下了。

`@instructions`
- 在 `# Subtraction` 下使用 `print()` 印出 `5` 減去 `5` 的結果。
- 在 `# Multiplication` 下印出 `3` 乘以 `5` 的結果。

`@hint`
- 你需要使用 `print()` 來產生輸出。
- 你可以分別使用 `-` 進行減法運算，使用 `*` 進行乘法運算。

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
Ex().has_printout(0, not_printed_msg = "您是否使用 `print(4 + 5)` 來列印出您的加法結果？")

Ex().has_printout(1, not_printed_msg = "您是否使用 `print(5 - 5)` 來列印出您的減法結果？")

Ex().has_printout(2, not_printed_msg = "您是否使用 `print(3 * 5)` 來列印出您的乘法結果？")

Ex().has_printout(3, not_printed_msg = "您是否使用 `print(10 / 2)` 來列印出您的除法結果？")

success_msg("正確！Python 可以幫助您進行數學運算，這一特性在我們提升數據技能時將非常有用。")
```

---

## 變數與資料類型

```yaml
type: VideoExercise
key: c2e396792e
xp: 50
```

`@projector_key`
433dcfcfedaee070cbf440491c402e3b

---

## 變數賦值

```yaml
type: NormalExercise
key: 4bf65ad83e
lang: python
xp: 100
skills:
  - 2
```

在 Python 中，你可以使用名稱來引用一個值，這就是變數。要建立值為 `5` 的變數 `x`，你可以使用 `=`，範例如下：

```
x = 5
```

現在你就可以使用變數名 `x` 來代替具體的數值 `5` 了。

請記住，Python 中的 `=` 表示賦值，而不是用來判斷「相等關係」的！請試試在練習中將 `____` 替換成你寫的程式碼。

`@instructions`
- 建立一個變數 `savings`，並為其賦值 `100`。
- 在腳本中輸入 `print(savings)` 來查看該變數。

`@hint`
- 輸入 `savings = 100` 來建立變數 `savings`。
- 建立變數 `savings` 之後，你可以輸入 `print(savings)`。
- 最終程式碼不應包含任何 `____`。

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
Ex().check_object("savings").has_equal_value(incorrect_msg="將 `100` 指派給變數 `savings`。")
Ex().has_printout(0, not_printed_msg = "使用 `print(savings)` 印出您創建的變數 `savings`。")
success_msg("太好了！現在讓我們嘗試用這個變數進行一些計算吧！")
```

---

## 對變數進行計算

```yaml
type: NormalExercise
key: ff06cedeb4
lang: python
xp: 100
skills:
  - 2
```

現在，你已經建立了一個 savings 變數，準備開始存錢吧！

你可以使用變數進行計算，而不是使用具體的數值。

如果你每月存 $10，4 個月後你會存下多少錢？

`@instructions`
- 建立一個變數 `monthly_savings`，使其等於 `10`，並建立一個 `num_months`，使其等於 `4`。
- 將 `monthly_savings` 乘以 `num_months`，並將結果賦值給 `new_savings`。
- 印出 `new_savings` 的值。

`@hint`
- 你可以像對待數字一樣對變數進行計算。因此，你可以把 `10 * 4` 中的數字替換成相應的變數！
- 使用 `print()` 查看 `new_savings` 的金額。
- 注意變數名拼寫要正確！

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
Ex().check_object("monthly_savings").has_equal_value(incorrect_msg = "您是否使用 `monthly_savings = 10` 將 `10` 儲存到 `monthly_savings`？")
Ex().check_object("num_months").has_equal_value(incorrect_msg = "您是否使用 `num_months = 4` 將 `4` 儲存到 `num_months`？")
Ex().check_object("new_savings").has_equal_value(incorrect_msg = "您是否使用正確的變數和符號進行乘法運算？預期為 `monthly_savings * num_months`，但得到其他結果。")
# Ex().check_object("total_savings").has_equal_value(incorrect_msg = "您是否使用正確的變數和符號進行加法運算？預期為 `savings + new_savings`，但得到其他結果。")

Ex().has_printout(0, not_printed_msg="請記得在腳本結尾列印出 `new_savings`。")

success_msg("您有 $40 的新儲蓄！")
```

---

## 其他變數類型

```yaml
type: NormalExercise
key: 006b48561f
lang: python
xp: 100
skills:
  - 2
```

在上一個練習中，你使用了 Python 的整數資料類型：

- `int`（即整數）：沒有小數部分的數值。值為 `100` 的 `savings` 就是整數的一個範例。

除了數值資料類型外，還有另外三種非常常見的資料類型：

- `float`（即浮點數）：同時包含整數部分和小數部分（由點分隔）的數字。`1.1` 就是浮點數的一個範例。
- `str`（即字串）：用於表示文字的資料類型。你可以使用單引號或雙引號來建立字串。
- `bool`（即布林值）：用於表示邏輯值的資料類型。只能是 `True` 或 `False`（務必正確區分大小寫！）。

`@instructions`
- 建立一個新的浮點數 `half`，值為 `0.5`。
- 建立一個新的字串 `intro`，值為 `"Hello! How are you?"`。
- 建立一個新的布林值 `is_good`，值為 `True`。

`@hint`
- 在 Python 中可使用 `=` 建立變數。務必記得給字串加上單引號或雙引號。
- Python 只有兩個布林值：`True` 和 `False`。`TRUE`、`true`、`FALSE`、`false` 等其他寫法都無效。

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
Ex().check_object("half").has_equal_value(incorrect_msg = "您是否將浮點數 `0.5` 儲存到 `half`？")

Ex().check_object("intro").has_equal_value(incorrect_msg = "嗯，您的 `intro` 變數有些不正確。請仔細檢查拼寫，並確保您已使用引號。")

Ex().check_object("is_good").has_equal_value(incorrect_msg = "您是否將布林值大寫？請記住，這裡不需要使用引號。")

success_msg("很好！")
```

---

## 與其他資料類型的運算

```yaml
type: BulletExercise
key: 4d0d83cc02
xp: 100
```

Python 中的變數有不同的資料類型。你可以使用 `type()` 查看變數的類型。比如，要查看 `a` 的類型，可執行：`type(a)`。

不同資料類型在 Python 中的行為也不同。比如，將兩個字串相加，與將兩個整數或兩個布林值相加，它們的表現是不一樣的。

現在，你可以動手試一試。

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
- 將 `savings` 與 `new_savings` 相加，並將結果賦值給 `total_savings`。
- 使用 `type()` 印出 `total_savings` 的類型。

`@hint`
- 將 `savings + new_savings` 賦值給一個新變數 `total_savings`。
- 要印出變數 `x` 的類型，請使用 `print(type(x))`。

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
msg = "您不需要更改或刪除預定義的變數。"

Ex().multi(
    check_object('savings', missing_msg=msg).has_equal_value(incorrect_msg=msg),
    check_object('new_savings', missing_msg=msg).has_equal_value(incorrect_msg=msg)
)

Ex().multi(
    check_object("total_savings").has_equal_value(incorrect_msg="將 `savings` 和 `new_savings` 相加以創建 `total_savings` 變數。"),
    has_printout(1, not_printed_msg = "__JINJA__:使用 `{{sol_call}}` 來列印 `total_savings` 的類型。")
)
```

***

```yaml
type: NormalExercise
key: f54fbf9bd9
xp: 50
```

`@instructions`
- 計算 `intro` 與 `intro` 的和，並將結果賦值給 `doubleintro`。
- 印出 `doubleintro`。結果是否符合你的預期？

`@hint`
- 將 `intro + intro` 賦值給一個新變數 `doubleintro`。
- 要印出變數 `x`，請在腳本中加入 `print(x)`。

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
msg = "您不需要更改或刪除預定義的變數。"

Ex().check_object('intro', missing_msg=msg).has_equal_value(incorrect_msg=msg)

Ex().multi(
    check_object("doubleintro").has_equal_value(incorrect_msg  = "您是否已將 `intro + intro` 的結果儲存在 `doubleintro` 中？"),
    has_printout(0, not_printed_msg = "別忘了打印出 `doubleintro`。")
)

success_msg("很好。注意 `intro + intro` 如何使 `\"Hello! How are you?\"` 和 `\"Hello! How are you?\"` 被拼接在一起。")
```

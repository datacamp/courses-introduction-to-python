---
title_meta: 第 3 章
title: 函式和套件
description: 你將學習如何使用函式、方法和套件，高效複用優秀 Python 開發者撰寫的程式碼。目標是減少為解決複雜問題而需撰寫的程式碼量。
attachments:
  slides_link: 'https://projector-video-pdf-converter.datacamp.com/735/chapter3.pdf'
lessons:
  - nb_of_exercises: 4
    title: 函式
  - nb_of_exercises: 4
    title: 方法
  - nb_of_exercises: 4
    title: 套件
---

## 函式

```yaml
type: VideoExercise
key: 5c5f365930
xp: 50
```

`@projector_key`
1204d914b0e53100529827e07441ee6c

---

## 常用函式

```yaml
type: NormalExercise
key: c422ee929b
lang: python
xp: 100
skills:
  - 2
```

Python 提供了許多開箱即用的內建函式。作為一名資料科學家，這些函式可以讓你的工作更輕鬆。你已經了解了兩個這樣的函式：`print()` 和 `type()`。還有像 `str()`、`int()`、`bool()` 和 `float()` 這樣用於轉換資料類型的函式。你可以在[此處](https://docs.python.org/3/library/functions.html)了解它們。這些都是內建函式。

函式呼叫很簡單。要取得 `3.0` 的類型並將輸出儲存到新變數 `result` 中，可以使用以下程式碼：

```
result = type(3.0)
```

`@instructions`
- 將 `type()` 嵌套在 `print()` 內，印出 `var1` 的資料類型。
- 對於串列 `var1`，使用 `len()` 取得[串列長度](https://docs.python.org/3/library/functions.html#len)。將其包含在 `print()` 呼叫中即可直接印出。
- 使用 `int()` 將 `var2` 轉換為[整數](https://docs.python.org/3/library/functions.html#int)。將輸出結果儲存為 `out2`。

`@hint`
- 像這樣呼叫 `type()` 函式：`type(var1)`。
- 像你之前多次做過的那樣呼叫 `print()`。只需把你想印出的變數放入括號裡。
- `int(x)` 會將 `x` 轉換為整數。

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
msg = "您不需要更改或刪除預定義的變數。"
Ex().check_object("var1", missing_msg=msg).has_equal_value(incorrect_msg=msg)
Ex().check_object("var2", missing_msg=msg).has_equal_value(incorrect_msg=msg)

patt = "__JINJA__:請確保使用 `{{sol_call}}` 輸出 `var1` 的 %s。"
Ex().has_printout(0, not_printed_msg = patt % '類型')
Ex().has_printout(1, not_printed_msg = patt % '長度')

int_miss_msg = "您是否使用了 `int()` 將 `var2` 轉換為整數？"
int_incorr_msg = "您是否將 `var2` 傳遞給 `int()`？"
Ex().check_correct(
  check_object("out2").has_equal_value(incorrect_msg="您正確地調用了 `int()`；現在請確保將此調用的結果賦值給 `out2`。"),
  check_function("int", missing_msg=int_miss_msg).has_equal_value(incorrect_msg=int_incorr_msg)
)
success_msg("做得好！`len()` 函數非常有用；它也可以用於字符串以計算字符數！")
```

---

## help() 函式

```yaml
type: MultipleChoiceExercise
key: 679b852978
lang: python
xp: 50
skills:
  - 2
```

也許你剛好知道某個 Python 函式的名稱，但不知道具體如何使用。有趣的是，你需要使用另一個函式來查詢這個函式的資訊：`help()`。在 IPython 中，你也可以在函式名前加上 `?`。

例如，要查看函式 `max()` 的說明，你可以使用以下任一呼叫：

```
help(max)
?max
```

在 IPython Shell 中開啟有關 `pow()` 的[文件](https://docs.python.org/3/library/functions.html#pow)。輸入 `?pow` 或 `help(pow)`，然後按 **Enter** 即可將其開啟。

以下哪一項說法是正確的？

`@possible_answers`
- `pow()` 需要 3 個參數：`base`、`exp` 和 `mod`。如果不提供 `mod`，該函式將回傳錯誤。
- `pow()` 需要 3 個必填參數：`base`、`exp` 和 `None`。
- `pow()` 需要 `base` 和 `exp` 參數；`mod` 是可選的。
- `pow()` 需要 2 個參數：`exp` 和 `mod`。缺少 `exp` 會導致錯誤。

`@hint`
- 可選參數會使用 `=` 設定預設值；如果沒有為該參數賦值，函式會使用其預設值。

`@pre_exercise_code`
```{python}

```

`@sct`
```{python}
msg1 = "不完全正確。`mod` 有一個預設值，如果您不指定值，將使用該預設值。"
msg2 = "不正確。`None` 是 `mod` 參數的預設值。"
msg3 = "完美！使用 `help()` 可以幫助您了解函數的運作方式，釋放其全部潛力！"
msg4 = "不正確。`pow()` 接受三個參數，其中一個有預設值。"
Ex().has_chosen(3, [msg1, msg2, msg3, msg4])
```

---

## 多個參數

```yaml
type: NormalExercise
key: e30486d7c1
lang: python
xp: 100
skills:
  - 2
```

在上一個練習中，你透過使用 `help()` 查看文件，掌握了什麼是可選參數。現在，你將動手試試，使用參數來修改 `sorted()` 函式的行為。

在 IPython Shell 中輸入 `help(sorted)`，查看 `sorted()` 的[文件](https://docs.python.org/3/library/functions.html#sorted)。

你會發現 `sorted()` 需要 3 個參數：`iterable`、`key` 和 `reverse`。在本練習中，你只需指定 `iterable` 和 `reverse`，無需指定 `key`。

我們已為你建立了兩個串列。

你能把它們合併在一起並按降序排序嗎？

`@instructions`
- 使用 `+` 將 `first` 和 `second` 的內容合併為一個新串列：`full`。
- 對 `full` 呼叫 `sorted()`，並將 `reverse` 參數設為 `True`。將排序後的串列儲存為 `full_sorted`。
- 最後印出 `full_sorted` 的輸出結果。

`@hint`
- 將 `first` 和 `second` 相加（就像對兩個數字求和一樣），並把結果賦值給 `full`。
- 呼叫 `sorted()` 並傳入兩個參數：`full` 和 `reverse=True`。
- 使用 `print()` 印出變數的輸出結果。

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
msg = "您不必更改或刪除已經存在的變數 `first` 和 `second`。"
Ex().multi(
  check_object("first", missing_msg=msg).has_equal_value(incorrect_msg=msg),
  check_object("second", missing_msg=msg).has_equal_value(incorrect_msg=msg)
)
Ex().check_correct(
  check_object("full_sorted").has_equal_value(incorrect_msg="確保您將調用 `sorted()` 的結果賦值給 `full_sorted`。"),
  check_function("sorted").multi(
    check_args(0).has_equal_value(),
    check_args('reverse').has_equal_value()
  )
)

success_msg("太棒了！前往觀看有關 Python 方法的影片。")
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

## 字串方法

```yaml
type: NormalExercise
key: 4039302ee0
lang: python
xp: 100
skills:
  - 2
```

字串自帶了許多方法。請跟著指引操作，探索其中幾個範例。如果你想了解更多細節，可以隨時在 IPython Shell 終端內輸入 `help(str)` 來進行查看。

我們已經提前為你建立好了一個名為 `place` 的字串，方便你動手嘗試。

`@instructions`
- 對 `place` 使用 `.upper()` [方法](https://docs.python.org/3/library/stdtypes.html#str.upper)，並將結果儲存在 `place_up` 中。使用你在前一個影片中學到的呼叫方法的語法。
- 印出 `place` 和 `place_up`。看看這兩個變數是不是都改變了？
- 透過對 `place` 呼叫 `.count()`，並將字母 `'o'` 作為輸入傳遞給該方法，印出 `place` 中字母 o 的數量。 注意，我們討論的是變數 `place`，而不是單詞 `"place"`！

`@hint`
- 你可以直接對 `place` 呼叫 `.upper()` 方法，無需任何額外的輸入。
- 要印出變數 `x`，你可以寫 `print(x)`。
- 確保將 `place.count(____)` 呼叫嵌套在 `print()` 函式中，以便印出結果。

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
msg = "您不需要更改或移除預定義的變數。"
Ex().check_object("place", missing_msg=msg).has_equal_value(incorrect_msg=msg)

patt = "別忘了輸出 `%s`。"
Ex().has_printout(0, not_printed_msg=patt % "place")
Ex().check_correct(
    has_printout(1, not_printed_msg=patt % "place_up"),
    check_correct(
        check_object("place_up").has_equal_value(incorrect_msg="將 `place.upper()` 呼叫的結果賦值給 `place_up`。"),
        check_function("place.upper", signature=False)
    )
)    

# check count of place
Ex().check_correct(
  has_printout(2, not_printed_msg = "您已經正確計算了 `place` 中字母 o 的數量；現在請確保將 `place.count('o')` 呼叫包裝在 `print()` 函數中以輸出結果。"),
  check_function("place.count", signature=False).check_args(0).has_equal_value()
)

success_msg("很好！從輸出中注意到 `upper()` 方法不會改變其被調用的對象。在下一個練習中，這對於列表將會有所不同！")
```

---

## 串列方法

```yaml
type: NormalExercise
key: 0dbe8ed695
lang: python
xp: 100
skills:
  - 2
```

在 Python 中，並不是只有字串才自帶方法，串列、浮點數、整數和布林值也都綁定了許多超實用的內建方法。在本練習中，你將嘗試使用：

- `.index()`：用來查找串列中第一個匹配元素的索引位置；
- `.count()`：用來統計某個元素在串列中一共出現了多少次。

接下來，你將對記錄房屋各區域面積的串列 `areas` 進行操作。

`@instructions`
- 使用 `.index()` 方法取得 `areas` 中等於 `20.0` 的元素的索引。印出該索引。
- 對 `areas` 呼叫 `.count()`，統計 `9.50` 在串列中出現了多少次。同樣，將該數字印出。

`@hint`
- 要印出索引，請將 `areas.index(___)` 呼叫嵌套在 `print()` 函式中。
- 要印出元素 `x` 在串列中出現的次數，請將 `areas.count(___)` 呼叫嵌套在 `print()` 函式中。

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
predef_msg = "您不需要更改或移除預定義的列表 `areas`。"

Ex().check_object("areas", missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg)

Ex().check_function("print", index=0).check_args(0).check_function('areas.index', signature=False).check_args(0).has_equal_value()


Ex().check_function("print", index=1).check_args(0).check_function('areas.count', signature=False).has_equal_value()

success_msg("很好！這些是 `list` 方法的範例，這些方法不會改變它們所被調用的列表。")
```

---

## 串列方法 (2)

```yaml
type: NormalExercise
key: 1fbeab82d0
lang: python
xp: 100
skills:
  - 2
```

大多數串列方法都會修改呼叫它們的原串列。例如：

- `.append()`：向呼叫它的串列中新增一個元素；
- `.remove()`：從串列中[移除](https://docs.python.org/3/library/stdtypes.html#typesseq-mutable)第一個與輸入匹配的元素；
- `.reverse()`：將所呼叫串列中元素的順序[反轉](https://docs.python.org/3/library/stdtypes.html#typesseq-mutable)。

接下來你將對記錄房屋各區域面積的串列 `areas` 進行操作。

`@instructions`
- 使用 `.append()` 兩次，依次加入泳池小屋和車庫的面積：分別是 `24.5` 和 `15.45`。注意，務必要按上面的順序新增。
- 印出 `areas`。
- 使用 `.reverse()` 方法將 `areas` 中元素的順序反轉。
- 再次印出 `areas`。

`@hint`
- 對於第一條指令，需要呼叫 `areas.append(___)` 兩次。
- 要印出變數 `x`，只需加入 `print(x)`。
- `.reverse()` 方法不需要額外輸入；只需使用點號加空括號：`.reverse()`。
- 要印出變數 `x`，只需加入 `print(x)`。

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

## 套件

```yaml
type: VideoExercise
key: ab96a17c5e
xp: 50
```

`@projector_key`
cedcfb34350be8545599768f96695cdd

---

## 匯入套件

```yaml
type: NormalExercise
key: 7432a6376f
lang: python
xp: 100
skills:
  - 2
```

假設你想計算一個圓的周長和面積，公式如下：

$$C = 2 \pi r$$
$$A = \pi r^2 $$

你不需要手動輸入 `pi` 的數值，可以直接使用包含圓周率數值的 `math` 套件。

補充說明：`**` 代表次方運算。例如，`3**4` 表示 `3` 的 `4` 次方，結果為 `81`。

`@instructions`
- 匯入 `math` 套件。
- 使用 `math.pi` 計算圓的周長，並將結果儲存在 `C` 中。
- 使用 `math.pi` 計算圓的面積，並將結果儲存在 `A` 中。

`@hint`
- 你可以直接使用 `import math`，然後使用 `math.pi` 來引用 `pi`。
- 按照題目中給出的公式計算 `C`。乘法使用 `*` 運算子。
- 按照題目中給出的公式計算 `A`。乘法和次方運算分別使用 `*` 和 `**` 運算子。

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
patt = "您對 `%s` 的計算不太正確。請確保使用 `math.pi`。"
Ex().multi(
  has_import('math', same_as=False),
  check_object('C').has_equal_value(incorrect_msg=patt%'C'),
  check_object('A').has_equal_value(incorrect_msg=patt%'A')
)

Ex().multi(
  has_printout(0, not_printed_msg = "__JINJA__:保留 `{{sol_call}}` 以列印出圓周長。"),
  has_printout(1, not_printed_msg = "__JINJA__:保留 `{{sol_call}}` 以列印出面積。")
)

success_msg("很好！如果您知道如何處理來自套件的函數，許多 Python 程式設計師的力量就在您的指尖！")
```

---

## 選擇性匯入

```yaml
type: NormalExercise
key: fe65eff50a
lang: python
xp: 100
skills:
  - 2
```

通用匯入（如 `import math`）會使 `math` 套件中的**所有**功能都可用。不過，如果你只打算使用套件中的某個部分，也可以進行更有針對性的匯入：

```
from math import pi
```

再試一下剛才的操作，不過這次僅使用 `pi`。

`@instructions`
- 從 `math` 套件中執行選擇性匯入，僅匯入 `pi` 函式。
- 使用 `pi` 計算圓的周長，並將結果儲存在 `C` 中。
- 使用 `pi` 計算圓的面積，並將結果儲存在 `A` 中。

`@hint`
- 使用 `from math import pi` 進行選擇性匯入。
- 現在，你可以直接使用 `pi` 了！

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
patt = "您對 `%s` 的計算不太正確。請確保僅使用 `pi`。"

Ex().has_import("math.pi", not_imported_msg = "請確保從 `math` 套件中匯入 `pi`。您應該使用 `from ___ import ___` 的表示法。",)

Ex().multi(
  check_object('C').has_equal_value(incorrect_msg=patt%'C'),
  check_object('A').has_equal_value(incorrect_msg=patt%'A')
)

Ex().multi(
  has_printout(0, not_printed_msg = "__JINJA__:保留 `{{sol_call}}` 以列印出圓周長。"),
  has_printout(1, not_printed_msg = "__JINJA__:保留 `{{sol_call}}` 以列印出面積。")
)

success_msg("很好！繼續進行下一個練習。")
```

---

## 幾種常見的匯入方式

```yaml
type: MultipleChoiceExercise
key: f1b2675a2a
lang: python
xp: 50
skills:
  - 2
```

將套件和模組匯入 Python 有多種方式。根據匯入方式的不同，撰寫的 Python 呼叫程式碼也不同。

假設你想使用 `inv()` [函式](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.inv.html)，該函式位於 `scipy` 套件的子套件 `linalg` 中。你希望能夠按如下方式使用該函式：

```
my_inv([[1,2], [3,4]])
```

為了讓上面的程式碼正常執行而不出現錯誤，你需要使用下面哪句 `import` 陳述式？

`@possible_answers`
- `import scipy`
- `import scipy.linalg`
- `from scipy.linalg import my_inv`
- `from scipy.linalg import inv as my_inv`

`@hint`
- 在 IPython Shell 中試試上面幾種不同的 import 陳述式，看看哪一個能讓 `my_inv([[1, 2], [3, 4]])` 這行程式碼正常執行而不出現錯誤。按 **enter** 即可執行輸入的程式碼。

`@pre_exercise_code`
```{python}

```

`@sct`
```{python}
msg1 = msg2 = msg3 = "不正確，請再試一次。嘗試在 IPython shell 中使用不同的 import 語句，看看哪一個能讓 `my_inv([[1, 2], [3, 4]])` 這行程式碼運行而不出錯。"
msg4 = "正確！`as` 關鍵字允許您為匯入的函數創建一個本地名稱：`inv()` 現在可以作為 `my_inv()` 使用。"
Ex().has_chosen(4, [msg1, msg2, msg3, msg4])
```

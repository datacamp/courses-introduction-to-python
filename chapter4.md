---
title_meta: 第 4 章
title: NumPy
description: NumPy 是進行資料科學實踐的基礎 Python 套件。學習使用強大的 NumPy 陣列工具，並開始探索資料。
attachments:
  slides_link: 'https://projector-video-pdf-converter.datacamp.com/735/chapter4.pdf'
lessons:
  - nb_of_exercises: 5
    title: Numpy
  - nb_of_exercises: 5
    title: 二維 Numpy 陣列
  - nb_of_exercises: 3
    title: Numpy：基礎統計學
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

## 建立第一個 NumPy 陣列

```yaml
type: NormalExercise
key: 84cab9d170
lang: python
xp: 100
skills:
  - 2
```

現在，你將深入探索棒球的資料世界。在此過程中，你會熟練掌握 `numpy` 的基礎用法，這是資料科學領域一個極為強大的套件。

Python 腳本中已經定義了一個名為 `baseball` 的串列，其中包含一些棒球球員的身高（公分）。你能新增幾行程式碼，將其轉換成 `numpy` 陣列嗎？

`@instructions`
- 將 `numpy` 套件以 `np` 別名匯入，這樣就可以使用 `np` 來存取 `numpy`。
- 使用 `np.array()` 將 `baseball` 串列轉換成 `numpy` 陣列，並將其命名為 `np_baseball`。
- 輸出 `np_baseball` 的資料型別，檢查是否正確建立陣列。

`@hint`
- 使用 `import numpy as np` 這樣就能完成匯入。以後只要你想要使用 `numpy` 中的函式，都必須使用 `np.fun_name()` 呼叫。
- 將 `baseball` 傳入 `np.array()`，然後將函式呼叫回傳的結果指派給 `np_baseball`。
- 要輸出變數 `x` 的資料型別，只需輸入 `print(type(x))`。

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
predef_msg = "您不需要更改或刪除預定義的變數。"
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

## 棒球球員的身高

```yaml
type: NormalExercise
key: e7e25a89ea
lang: python
xp: 100
skills:
  - 2
```

你是一位超級棒球迷。你決定致電 MLB（美國職業棒球大聯盟），詢問有關主要球員的更多身高統計資料。他們提供了一千多名球員的資料，這些資料以一般 Python 串列的形式儲存：`height_in`。球員的身高以英吋為單位。你能將這些資料轉換成 `numpy` 陣列，並將單位換算成公尺嗎？

`height_in` 已準備就緒，`numpy` 套件也已載入完成，你可以直接上手了（資料來源：stat.ucla.edu）。

`@instructions`
- 使用 `height_in` 建立 `numpy` 陣列。將這個新陣列命名為 `np_height_in`。
- 輸出 `np_height_in` 的結果。
- 將 `np_height_in` 乘以 `0.0254`，以便將所有身高測量值的單位從英吋換算成公尺。將新值儲存到新陣列 `np_height_m` 中。
- 輸出 `np_height_m` 的結果，並檢查結果是否合理。

`@hint`
- 使用 `np.array()` 並傳入 `height`。將結果儲存在 `np_height_in` 中。
- 要輸出變數 `x` 的結果，只需在 Python 腳本中加上 `print(x)`。
- 像對待單個數值一樣對 `np_height_in` 進行計算：`np_height_in * conversion_factor` 是解題的關鍵之一。
- 要輸出變數 `x` 的結果，只需在 Python 腳本中加上 `print(x)`。

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
  check_object("np_height_m").has_equal_value(incorrect_msg = "使用 `np_height_in * 0.0254` 來計算 `np_height_m`。")
)

success_msg("很好！在眨眼之間，`numpy` 就能對超過 1000 個高度測量值進行乘法運算。")
```

---

## NumPy 的副作用

```yaml
type: MultipleChoiceExercise
key: 3662ff6637
lang: python
xp: 50
skills:
  - 2
```

`numpy` 非常適合進行向量運算。但是，與一般 Python 串列相比，你會發現它的運作不同。

首先，`numpy` 陣列不能包含不同型別的元素。如果你混用不同的資料型別（例如布林值和整數），`numpy` 會自動將它們轉換為共同的類型。當布林值（`True` 和 `False`）與數字混合時，它們會被視為 `1` 和 `0`，因此陣列中的元素最終都會是整數。

其次，常見的算術運算子（例如 `+`、`-`、`*` 和 `/`），在一般 Python 串列和 `numpy` 陣列中的作用也有所不同。

請選擇會得到以下輸出結果的程式碼：

```
np.array([True, 1, 2]) + np.array([3, 4, False])
```

`numpy` 套件已以 `np` 別名匯入。你可以在 IPython Shell 中執行每個選項，查看輸出結果。

`@possible_answers`
- `np.array([True, 1, 2, 3, 4, False])`
- `np.array([4, 3, 0]) + np.array([0, 2, 2])`
- `np.array([1, 1, 2]) + np.array([3, 4, -1])`
- `np.array([0, 1, 2, 3, 4, 5])`

`@hint`
- 複製不同的程式碼區塊，並將其貼到 IPython Shell 中。按下 Enter 鍵來執行程式碼，查看哪個輸出結果與 `np.array([True, 1, 2]) + np.array([3, 4, False])` 所產生的結果相符。

`@pre_exercise_code`
```{python}
import numpy as np
```

`@sct`
```{python}
msg1 = msg3 = msg4 = "不正確。請嘗試不同的程式碼區塊，看看哪一個與目標程式碼區塊相符。"
msg2 = "做得好！`True` 轉換為 1，`False` 轉換為 0。"
Ex().has_chosen(2, [msg1, msg2, msg3, msg4])
```

---

## 選取 NumPy 陣列元素

```yaml
type: NormalExercise
key: fcb2a9007b
lang: python
xp: 100
skills:
  - 2
```

選取元素（也就是在串列或陣列後面使用方括號來取值）在串列和陣列中的用法完全一樣。

本練習已在後台載入 `height_in` 和 `weight_lb` 這兩個串列，分別以一般串列的形式儲存 MLB 球員的身高和體重資料。練習還為你準備好了兩個 `numpy` 陣列：`np_weight_lb` 和 `np_height_in`。

`@instructions`
- 選取 `np_weight_lb` 中索引為 50 的元素，並將其輸出。
- 從 `np_height_in` 中選取索引 100 到 110（包含索引 110）的元素，並輸出這個子陣列。

`@hint`
- 確保將選取部分資料的運算式放進 `print()` 運算式中。
- 使用 `[100:111]` 選取索引 100 到 110（包含索引 110）的元素。

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
msg = "您不需要更改或刪除預定義的變數。"
Ex().multi(
    check_object("np_height_in", missing_msg=msg).has_equal_value(incorrect_msg = msg),
    check_object("np_weight_lb", missing_msg=msg).has_equal_value(incorrect_msg = msg)
)

Ex().has_printout(0)
Ex().has_printout(1)

success_msg("很好！是時候學習一些新東西了：2D NumPy 陣列！")
```

---

## 二維 NumPy 陣列

```yaml
type: VideoExercise
key: 1241efac7a
xp: 50
```

`@projector_key`
ae3238dcc7feb9adecfee0c395fc8dc8

---

## 建立第一個二維 NumPy 陣列

```yaml
type: NormalExercise
key: 5cb045bb13
lang: python
xp: 100
skills:
  - 2
```

在處理實際的 MLB 資料之前，我們先試著使用一個簡短的「巢狀串列」來建立一個二維 `numpy` 陣列。

在本練習中，`baseball` 就是一個巢狀串列。主串列包含 4 個元素。其中的每個元素都是一個依次包含 4 名棒球球員身高和體重的串列。腳本中已為你寫好了 `baseball`。

`@instructions`
- 使用 `np.array()` 將 `baseball` 轉換為二維 `numpy` 陣列，將其命名為 `np_baseball`。
- 輸出 `np_baseball` 的資料型別。
- 輸出 `np_baseball` 的 `shape` 屬性。請使用 `np_baseball.shape`。

`@hint`
- 腳本中已為你寫好 `baseball`。對其呼叫 `np.array()`，並將得到的二維 `numpy` 陣列儲存在 `np_baseball` 中。
- 第二條指令請搭配使用 `print()` 與 `type()`。
- 呼叫 `np_baseball.shape` 可取得 `np_baseball` 的維度。記得要將其包含在 `print()` 呼叫中。

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
msg = "您不需要更改或刪除預定義的變數。"
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

success_msg("太好了！您現在準備好將實際的 MLB 數據轉換為 2D `numpy` 陣列了！")
```

---

## 二維形式的棒球資料

```yaml
type: NormalExercise
key: 5df25d0b7b
lang: python
xp: 100
skills:
  - 2
```

你發現將這些資訊，重新整理成二維 `numpy` 陣列更合適。

現在，你有一個 Python 巢狀串列，其中每個子串列都包含一名棒球球員的身高和體重資料，該串列名為 `baseball`，系統已經事先為你載入（雖然你看不到）。

將資料儲存為二維陣列，以便使用 `numpy` 的更多功能。

`@instructions`
- 使用 `np.array()` 將 `baseball` 轉換為二維 `numpy` 陣列，並命名為 `np_baseball`。
- 輸出 `np_baseball` 的 `shape` 屬性。

`@hint`
- 已可在 Python 環境中使用 `baseball`。對其呼叫 `np.array()`，並將得到的二維 `numpy` 陣列儲存在 `np_baseball` 中。
- 使用 `np_baseball.shape` 即可取得 `np_baseball` 的維度。記得將其放進`print()` 呼叫中。

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

success_msg("太好了！是時候展示多維 `numpy` 陣列的一些絕佳功能了！")
```

---

## 選取二維 NumPy 陣列的元素

```yaml
type: NormalExercise
key: aeca4977f0
lang: python
xp: 100
skills:
  - 2
```

如果你的二維 `numpy` 陣列結構規整，即每一列和每一欄都包含固定數量的數值，複雜的選取元素操作就會變得非常簡單。請看下面的程式碼，示範如何從巢狀串列中選取元素 `"a"` 和 `"c"`。

```
# numpy
import numpy as np
np_x = np.array(x)
np_x[:, 0]
```

逗號前的索引代表「列」，逗號後的索引代表「欄」。冒號 `:` 表示切片；在此範例中，它告訴 Python 要選取所有列。

`@instructions`
- 輸出 `np_baseball` 的第 50 列。
- 建立新變數 `np_weight_lb`，用來選取 `np_baseball` 的整個第二欄。
- 選取 `np_baseball` 中第 124 位棒球球員的身高（第一欄）並將其輸出。

`@hint`
- 你需要在第一條指令中使用列索引 49！更具體地說，你需要使用 `[49, :]`。
- 要選取整個第二欄，你需要使用 `[:, 1]`。
- 撰寫最後一條指令時，使用 `[123, 0]`；別忘記將整行程式碼放在 `print()` 函式中。

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
msg = "您不需要更改或刪除預定義的變數。"
Ex().multi(
    has_import("numpy", same_as = False),
    check_object("np_baseball", missing_msg=msg).has_equal_value(incorrect_msg = msg)
)

Ex().has_printout(0)

Ex().check_object('np_weight_lb').has_equal_value(incorrect_msg = "您可以使用 `np_baseball[:,1]` 來定義 `np_weight_lb`。這將選擇整個第一列。")

Ex().has_printout(1)

success_msg("進展順利！")
```

---

## 二維陣列的數學運算

```yaml
type: NormalExercise
key: 1c2378b677
lang: python
xp: 100
skills:
  - 2
```

二維 `numpy` 陣列可以像一維 `numpy` 陣列一樣，逐元素執行計算。

`np_baseball` 已提前寫好，它是一個二維 `numpy` 陣列，包含 3 欄，分別代表身高（英吋）、體重（磅）和年齡（歲）。`baseball` 可作為常規巢狀串列使用，`updated` 可作為二維 numpy 陣列使用。

`@instructions`
- 你已經成功取得了所有棒球球員身高、體重和年齡的變化資料。這些資料儲存在二維 `numpy` 陣列 `updated` 中。將 `np_baseball` 與 `updated` 相加並輸出結果。
- 你想把身高和體重的單位轉換為公制（分別為公尺和公斤）。首先，建立一個包含三個數值 `0.0254`、`0.453592` 和 `1` 的 `numpy` 陣列，將其命名為 `conversion`。
- 將 `np_baseball` 與 `conversion` 相乘並輸出結果。

`@hint`
- `np_baseball + updated` 會對這兩個 `numpy` 陣列進行逐元素相加。
- 使用 `numpy` 建立 `np.array()` 陣列，並傳入一個包含三個元素的一般 Python 串列。
- 你可以直接使用 `np_baseball * conversion`，無需額外操作。試試看！記得將其放進 `print()` 呼叫中，以輸出結果。

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

msg = "您不需要更改或移除預定義的變數。"
Ex().check_object("np_baseball", missing_msg=msg).has_equal_value(incorrect_msg = msg)

Ex().has_printout(0)

Ex().check_correct(
    has_printout(1),
    check_correct(
        check_object('conversion').has_equal_value(),
        check_function('numpy.array', index = 1).check_args(0).has_equal_value()
    )    
)

success_msg("做得好！注意，通過很少的代碼，您可以以非常特定的方式更改 `numpy` 數據結構中的所有值。這在您未來作為數據科學家時將非常有用！")
```

---

## NumPy：基礎統計學

```yaml
type: VideoExercise
key: 287995e488
xp: 50
```

`@projector_key`
34495ba457d74296794d2a122c9b6e19

---

## 平均值與中位數

```yaml
type: NormalExercise
key: 509c588eb6
lang: python
xp: 100
skills:
  - 2
```

現在，你已經學會如何使用 `numpy` 函式，進一步瞭解你的資料。

棒球資料儲存在一個二維 `numpy` 陣列中，共有 3 欄（身高、體重、年齡）和 1015 列。該 `numpy` 陣列名為 `np_baseball`。不過，在重新整理資料後，你發現有些身高值異常高。請依照說明完成練習，找出處理所謂的離群值 (_outliers_) 時，最適合使用哪一種摘要統計量。你可以使用 `np_baseball`。

`@instructions`
- 建立 `numpy` 陣列 `np_height_in`，它等於 `np_baseball` 的第一欄。
- 輸出 `np_height_in` 的平均值。
- 輸出 `np_height_in` 的中位數。

`@hint`
- 使用二維 `numpy` 選取元素：`[:,0]` 是解題關鍵之一。
- 如果將 `numpy` 匯入為 `np`，可以使用 `np.mean()` 計算 NumPy 陣列的平均值。別忘了呼叫一次 `print()`。
- 最後一條指令請使用 `np.median()`。

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

Ex().check_object("np_height_in").has_equal_value(incorrect_msg = "您可以使用 `np_baseball[:,0]` 從 `np_baseball` 中選擇第一列"),

Ex().check_correct(
    has_printout(0),
    check_function('numpy.mean').has_equal_value()
)

Ex().check_correct(
    has_printout(1),
    check_function('numpy.median').has_equal_value()
)

success_msg("平均身高為 1586 英吋，這聽起來不太對，是嗎？然而，中位數似乎不受異常值的影響：74 英吋非常合理。檢查中位數和平均數以了解整個數據集的整體分佈總是一個好主意。")
```

---

## 探索棒球資料

```yaml
type: NormalExercise
key: '4409948807'
lang: python
xp: 100
skills:
  - 2
```

由於平均值和中位數相差甚遠，你決定向 MLB 投訴。他們找到了錯誤，並將更正後的資料傳送給了你。這些資料同樣以包含三欄的二維 NumPy 陣列 `np_baseball` 提供。

編輯器中的 Python 腳本已經寫好了用於輸出包含不同摘要統計資訊的提示程式碼，並且也已經使用 `np` 匯入 `numpy`。你能完成剩下的部分嗎？`np_baseball` 已準確就緒。

`@instructions`
- 輸出平均身高的程式碼已包含在內。請完成計算身高中位數的程式碼。
- 對 `np_baseball` 的第 1 欄呼叫 `np.std()` 來計算 `stddev`。
- 身材高大的球員體重往往也更重嗎？使用 `np.corrcoef()` 計算 `np_baseball` 第 1 欄與第 2 欄之間的相關係數，並將結果儲存到 `corr` 中。

`@hint`
- 使用 `np.median()` 計算中位數。首先要確保選取正確的欄！
- 選取同一欄資料，使用 `np.std()` 計算標準差。
- 使用 `np_baseball[:, 0]` 和 `np_baseball[:, 1]` 選取第 1 欄和第 2 欄，並將這兩欄資料作為 `np.corrcoef()` 的引數。

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
msg = "您不應更改或移除預定義的 `avg` 變數。"
Ex().check_object("avg", missing_msg=msg).has_equal_value(incorrect_msg=msg)

missing = "您是否使用了 `np.median()` 來計算中位數？"
incorrect = "要計算 `med`，請將 `np_baseball` 的第一列傳遞給 `numpy.median()`。`np.mean()` 的範例顯示了如何完成此操作。"
Ex().check_correct(
  check_object("med").has_equal_value(),
  check_function("numpy.median", index=0, missing_msg=missing).check_args(0).has_equal_value(incorrect_msg=incorrect)
)

missing = "您是否使用了 `np.std()` 來計算標準差？"
incorrect = "要計算 `stddev`，請將 `np_baseball` 的第一列傳遞給 `numpy.std()`。`np.mean()` 的範例顯示了如何完成此操作。"
Ex().check_correct(
  check_object("stddev").has_equal_value(),
  check_function("numpy.std", index=0, missing_msg=missing).check_args(0).has_equal_value(incorrect_msg=incorrect)
)

missing = "您是否使用了 `np.corrcoef()` 來計算相關性？"
incorrect1 = "要計算 `corr`，`np.corrcoef()` 的第一個參數應該是 `np_baseball` 的第一列，類似於之前的做法。"
incorrect2 = "要計算 `corr`，`np.corrcoef()` 的第二個參數應該是 `np_baseball` 的第二列。這次請使用 `[:,1]` 而不是 `[:,0]`。"
Ex().check_correct(
  check_object("corr").has_equal_value(),
  check_function("numpy.corrcoef", index=0, missing_msg=missing).multi(
    check_args(0, missing_msg=incorrect1).has_equal_value(incorrect_msg=incorrect1),
    check_args(1, missing_msg=incorrect2).has_equal_value(incorrect_msg=incorrect2)
  )
)

success_msg("做得好！您已經建立了堅實的基礎 - 現在是時候運用您所有的新數據科學技能來解決更多挑戰並產生影響。")
```

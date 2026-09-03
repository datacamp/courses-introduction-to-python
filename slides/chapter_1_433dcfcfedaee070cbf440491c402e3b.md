---
title: Insert title here
key: 433dcfcfedaee070cbf440491c402e3b
video_link:
  mp3: >-
    https://videos.datacamp.com/mp3/translations/course_735/zh-TW/bdc6e56e-c51b-4f38-924f-acb3738bdff0-28facff4e11984bb47c2f86335ab098a.mp3
---

## 變數與資料類型

```yaml
type: TitleSlide
key: dc8b62f1c8
```

`@lower_third`
name: Hugo Bowne-Anderson
title: Data Scientist at DataCamp

`@script`
表現不錯，歡迎回來！毫無疑問，Python 是一個強大的計算工具。但如果你想進行更複雜的計算，就會希望在撰寫程式碼時把一些數值「儲存」起來。

---

## 變數

```yaml
type: FullSlide
key: 36ec318b41
```

`@part1`
- 區分大小寫的特定名稱

- 透過變數名呼叫值{{1}}

- 1.79 公尺 - 68.7 公斤{{2}}

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
只需定義一個區分大小寫的特定變數名稱，就能輕鬆儲存數值。建立或宣告變數後，隨時可以透過輸入變數名稱來呼叫它的值。

假設你測得的身高是 1.79 公尺，體重是 68.7 公斤。那麼，你可以用等號把這兩個數值分別指派給 height 和 weight 變數：

這時只要輸入變數名稱 height，

Python 就會找到這個變數，提取並印出它的值。

---

## 計算 BMI

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
接下來計算體質指數 (BMI)。計算公式如下，其中體重單位為公斤，身高單位為米。你可以直接用具體數值計算，但我更推薦使用變數 height 和 weight，就像範例中那樣。每次輸入變數名，Python 都會將其替換為該變數的實際數值。這裡的 weight 是 68.7，height 是 1.79。

最後，將計算結果存入一個新變數 bmi 中。此時 bmi 儲存的數值就與剛才計算得到的結果完全一致。

Python 程式設計經常會用到變數，它能大幅提升程式碼的可復現性。

---

## 可復現性

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
假設建立 height、weight 和 bmi 變數的程式碼都在一個腳本裡，如下所示。如果你想根據另一個體重重新計算 bmi，

---

## 可復現性

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
那麼，只需修改 weight 變數的宣告並重新執行腳本。因為 weight 變數的值變了，bmi 也會相應地發生改變。

到目前為止，我們操作的還都是數值，比如身高和體重。

---

## Python 型別

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
在 Python 中，每個數字都有對應的型別。你可以用 type() 函式來檢視某個值的型別。想要知道 bmi 的型別，只需在 type 後面的括號裡填入 bmi 即可。你會發現它的型別是浮點數 float，也就是 Python 用來表示既有整數部分又有小數部分的實數型別。此外，Python 還有專門表示整數的型別 int，就像這個範例一樣。

不過，在資料科學領域，只有 int 和 float 還不夠。

---

## Python 型別 (2)

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
Python 還有許多其他資料型別，其中最常見的是字串和布林值。

字串是 Python 用來表示文字的資料型別，使用單引號和雙引號都可以構建字串，如範例所示。如果你檢視最後一個變數的型別，會發現它顯示為 str，也就是 string 的縮寫。

布林值 (Boolean) 只有 True 和 False 兩種取值，這相當於我們日常說的「是」和「否」。在後續的資料篩選等操作中，布林值會非常實用。

另外，Python 的資料型別還有一些非常特別的地方。

---

## Python 型別 (3)

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

- 不同型別 = 不同行為！{{3}}

`@script`
看看這行對兩個整數求和的程式碼，再看看這行將兩個字串連接起來的程式碼。

對於整數，+ 運算子會執行加法計算；對於字串，它會把兩段文字拼接在一起。對於不同的資料型別，同一個加號運算子的行為是不一樣的。這是一條通用原則：程式碼如何執行，取決於使用的資料型別。

在接下來的練習中，你將建立自己的第一組變數，親自體驗一下 Python 的各種資料型別。我們下一個影片見，到時候，我會詳細介紹有關串列的全部知識。

---

## 一起來練習吧！
```yaml
type: FinalSlide
key: b7fc40db4d
```

`@script`
我們開始動手編寫程式碼吧！期待在下一章與你相見，屆時你會構建出更棒的 Python 圖表。

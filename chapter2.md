---
title_meta: 第 2 章
title: Python 串列
description: 學習在串列中儲存、存取和操作資料：這是有效處理大量資料的第一步。
attachments:
  slides_link: 'https://projector-video-pdf-converter.datacamp.com/735/chapter2.pdf'
lessons:
  - nb_of_exercises: 4
    title: Python 串列
  - nb_of_exercises: 4
    title: 選取串列元素
  - nb_of_exercises: 5
    title: 操作串列
---

## Python 串列

```yaml
type: VideoExercise
key: a5886d213f
xp: 50
```

`@projector_key`
a0530c4542f10988847b2dbb91f717c3

---

## 建立串列

```yaml
type: NormalExercise
key: e6c527bf41
lang: python
xp: 100
skills:
  - 2
```

串列是一種**複合資料型別**，你可以像這樣將多個值組合在一起：

```
a = "is"
b = "nice"
my_list = ["my", "list", a, b]
```

在測量完家人的身高後，你決定收集一些關於自己住家的資訊。在這道練習題中，住家各個區域的面積已分別儲存在不同的變數中。

`@instructions`
- 使用預定義變數，按以下順序建立串列 (`areas`)，包含玄關 (`hall`)、廚房 (`kit`)、客廳 (`liv`)、臥室 (`bed`) 和浴室 (`bath`) 面積。
- 使用 `print()` 函式輸出 `areas`。

`@hint`
- 你可以使用先前建立的變數來建立串列：`areas = [hall, kit, ...]`。
- 確保使用方括號 `[]`，而不是圓括號 `()`。
- 在串列中儲存變數時不需要使用引號。
- 送出時輸入 `print(areas)`，以便輸出串列。

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
predef_msg = "不要移除或編輯預定義的變數！"
areas_msg = "將 `areas` 定義為包含所有面積變數的列表，順序正確：[hall, kit, liv, bed, bath]。注意拼寫錯誤。列表不應包含其他任何內容！"

Ex().check_correct(
    has_printout(0, not_printed_msg = "__JINJA__:您是否在腳本的末尾使用 `{{sol_call}}` 來列印出 `areas` 列表？"),
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

success_msg("很好！在這裡使用列表是不是更好呢？")
```

---

## 建立包含不同資料型別的串列

```yaml
type: NormalExercise
key: 1702a8bcdc
lang: python
xp: 100
skills:
  - 2
```

儘管不太常見，但串列也可以同時包含不同的 Python 資料型別，例如字串、浮點數和布林值。

現在，你要將房間名稱新增到串列中，以便輕鬆查看每個房間的名稱和面積。

為了幫助你開始練習，部分程式碼已經事先寫好了。請留心這裡：`"bathroom"` 是字串，而 `bath` 是變數，代表你之前指定的浮點數 `9.50`。

`@instructions`
- 完成建立 `areas` 串列的程式碼。建立串列時，讓每個房間的名稱（字串）後面緊接著對應的面積。換句話說，將 `"hallway"`、`"kitchen"` 和 `"bedroom"` 放入適當的位置。
- 再次輸出 `areas`，看看這次的輸出結果是否提供了更多資訊？

`@hint`
- 串列 `areas` 的前四個元素已寫成`["hallway", hall, "kitchen", kit, ...`。
- 字串必須用引號 `""` 括起來。

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
predef_msg = "不要移除或編輯預定義的變數！"
areas_msg = "您沒有為 `areas` 指派正確的值。請再看看說明。確保每次在包含面積的變數之前放置房間名稱。這裡的順序很重要！注意拼寫錯誤。"

Ex().check_correct(
  check_object("areas").has_equal_value(incorrect_msg = areas_msg),
  multi([ check_object(obj, missing_msg = predef_msg).has_equal_value(incorrect_msg = predef_msg) for obj in objs])
)

Ex().has_printout(0, not_printed_msg = "__JINJA__:您是否在腳本的最後使用 `{{sol_call}}` 來列印 `areas` 清單？")

success_msg("很好！這個清單包含字串和浮點數，但對於 Python 來說這不是問題！")
```

---

## 巢狀串列

```yaml
type: NormalExercise
key: 9158c577b0
lang: python
xp: 100
skills:
  - 2
```

身為資料科學家，你經常需要處理大量資料，因此將部分資料分組整理會更方便。

與其建立一個包含字串和浮點數，用來表示家中各個房間名稱與面積的串列，你也可以建立一個巢狀串列。

記住：`"hallway"` 是字串，而 `hall` 是變數，表示你之前指定的浮點數 `11.25`。

`@instructions`
- 完成這個巢狀串列，將臥室和浴室的資料加入進去。記得按順序新增！
- 輸出 `house`。用這種方式組織資料，是不是條理清晰多了？

`@hint`
- 透過在方括號內新增 `["bedroom", bed]` 和 `["bathroom", bath]`，將兩個子串列 (_sublists_) 新增到 `house` 串列中。
- 記得在每個子串列後面加上逗號 `,`。
- 要輸出變數 `x`，請在新的一行中加上 `print(x)`。

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
predef_msg = "請勿移除或編輯預定義的變數！"
house_msg = "您未將正確的值賦予 `house`。請再查看一下說明。擴展列表，使其包含每對房間名稱和房間面積的列表。注意順序和拼寫錯誤！"

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

Ex().has_printout(0, not_printed_msg = "__JINJA__:您是否使用了 `{{sol_call}}` 來列印出 `house` 的內容？")

success_msg("太棒了！準備好學習列表的子集了嗎？")
```

---

## 選取串列元素

```yaml
type: VideoExercise
key: c076b5a69c
xp: 50
```

`@projector_key`
fc15ba5cb9485456df8589130b519ea3

---

## 選取資料，逐一攻克

```yaml
type: NormalExercise
key: c3ce582e32
lang: python
xp: 100
skills:
  - 2
```

選取 Python 串列元素非常簡單。請參考下面的程式碼範例：先建立一個串列 `x`，然後從中選取「b」。請記住，這是第二個元素，因此索引值為 1。你也可以使用負數索引。

```
x = ["a", "b", "c", "d"]
x[1]
x[-3] # same result!
```

還記得之前包含字串和浮點數的 `areas` 串列嗎？腳本中已經定義好這個串列。你能加入正確的程式碼，練習選取 Python 串列中的元素嗎？

`@instructions`
- 輸出 `areas` 串列中的第二個元素（其值為 `11.25`）。
- 選取並輸出 `areas` 的最後一個元素，即 `9.50`。這裡更適合使用負數索引！
- 選取代表客廳面積的數值 (`20.0`) 並將其輸出。

`@hint`
- 使用 `x[1]` 選取串列 `x` 的第二個元素。
- 使用 `x[-1]` 選取串列 `x` 的最後一個元素。
- 將選取元素的操作放進 `print()` 呼叫中。
- 代表客廳面積的數值是串列中的第 6 個元素，因此這裡需要使用 `[5]`。如果寫成 `area[4]`，顯示的會是字串！

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
msg = "不要移除或編輯預定義的 `areas` 列表。"
Ex().check_object("areas", missing_msg = msg).has_equal_value(incorrect_msg = msg)
Ex().has_printout(0, not_printed_msg = "再看看您的代碼以打印出 `areas` 中的第二個元素，它位於索引 `1`。")
Ex().has_printout(1, not_printed_msg = "再看看您的代碼以打印出 `areas` 中的最後一個元素，它位於索引 `-1`。")
Ex().has_printout(2, not_printed_msg = "再看看您的代碼以打印出客廳的面積。它位於索引 `5`。")
success_msg("做得好！")
```

---

## 串列切片與資料選取

```yaml
type: NormalExercise
key: 7f08642d18
lang: python
xp: 100
skills:
  - 2
```

從串列中選取單個元素只是基本操作，你還可以對串列進行「切片」，也就是一次性從串列中選取多個元素。語法格式如下：

```
my_list[start:end]
```

`start` 索引包含在選取範圍內，而 `end` 索引則不包含。不過，這兩個索引其實都可以省略。如果你不指定 `start` 索引，Python 會明白你是想從串列的開頭開始切片。

`@instructions`
- 使用切片建立串列 `downstairs`，其中包含 `areas` 的前 6 個元素。
- 建立 `upstairs`，用於存放 `areas` 的後 `4` 個元素。這次請省略 `end` 索引，簡化切片語法。
- 使用 `print()` 輸出 `downstairs` 和 `upstairs`。

`@hint`
- 使用方括號 `[0:6]` 來取得串列的前 六個元素。
- 要取得串列 `l` 中除前五個元素外的所有元素，可使用 `l[5:]`。
- 新增兩個 `print()` 呼叫來輸出 `downstairs` 和 `upstairs`。

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
msg = "請勿移除或編輯預定義的 `areas` 列表。"
Ex().check_object("areas", missing_msg = msg).has_equal_value(incorrect_msg = msg)

patt = "`%s` 不正確。請使用 `areas[%s]` 和切片來選擇您想要的元素，或使用等效的方法。"
Ex().check_object("downstairs").has_equal_value(incorrect_msg = patt % ('downstairs', '0:6'))
Ex().check_object("upstairs").has_equal_value(incorrect_msg = patt % ("upstairs",":6"))

Ex().has_printout(0, not_printed_msg="您是否在計算 `downstairs` 後打印出來了？")
Ex().has_printout(1, not_printed_msg="您是否在計算 `upstairs` 後打印出來了？")

success_msg("做得好！")
```

---

## 選取巢狀串列的元素

```yaml
type: NormalExercise
key: dbbbd306cf
xp: 100
```

Python 串列可以包含其他串列，這就是所謂的巢狀串列。

要選取巢狀串列的元素，你同樣可以使用方括號。以串列 `house` 為例，寫法就像這樣：

```
house[2][0]
```

`@instructions`
- 從 `house` 串列中取得浮點數 `9.5`。

`@hint`
- 我們一步步拆解這個問題。首先，你需要取得串列的最後一個元素 `["bathroom", 9.50]`。回憶一下，最後一個元素的索引是 `-1`。
- 接著，你需要取得 `["bathroom", 9.50]` 中的第二個元素，它的索引是 `1`。

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

success_msg("正確！列表拼圖的最後一塊是操作。")
```

---

## 操作串列

```yaml
type: VideoExercise
key: d7fe818b3a
xp: 50
```

`@projector_key`
355ed52d2fb0d67508c6a311b7cbc6d3

---

## 替換串列元素

```yaml
type: NormalExercise
key: 4e1bba1b55
lang: python
xp: 100
skills:
  - 2
```

要替換串列元素，你可以選取串列元素，然後將新值指派給該元素。你可以選取單個元素，也可以一次性更改整個串列切片。

在本練習及後續練習中，你將繼續使用 `areas` 串列，其中包含房屋內不同房間的名稱和面積。

`@instructions`
- 使用負數索引將浴室面積從 `9.50` 平方公尺更新為 `10.50` 平方公尺。
- 想讓 `areas` 串列更潮一些？你可以將 `"living room"` 改為 `"chill zone"`。這次記得不要使用負數索引。

`@hint`
- 要更新浴室面積，先找到它在串列中的對應位置（就是最後一個元素！）。
- 然後將新的浴室面積指派給這個位置，取代原本的值。
- 使用相同的方式，更新位於索引 4 處的名稱 `"living room"`。

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
bathroom_msg = '您可以使用 `areas[-1] = 10.50` 來更新浴室面積。'
chillzone_msg = '您可以使用 `areas[4] = "chill zone"` 來更新客廳名稱。'
Ex().check_correct(
  check_object('areas').has_equal_value(incorrect_msg = '您對 `areas` 的更改未產生正確的列表。您確定使用了正確的子集操作嗎？如有疑問，您可以使用提示！'),
  multi(
    has_equal_value(expr_code='areas[-1]', override=10.50, incorrect_msg = bathroom_msg),
    has_equal_value(expr_code='areas[4]', override='chill zone', incorrect_msg = chillzone_msg),
  )
)
success_msg('太棒了！如代碼範例所示，您還可以對列表進行切片，並用另一個列表替換它，以在單個命令中更新多個元素。')
```

---

## 擴展串列

```yaml
type: NormalExercise
key: ff0fe8d967
lang: python
xp: 100
skills:
  - 2
```

既然可以修改串列中的元素，想必你也會想要在串列中新增元素，對吧？這時可以使用 `+` 運算子：

```
x = ["a", "b", "c", "d"]
y = x + ["e", "f"]
```

你中了樂透，太棒了！你決定蓋一間泳池小屋和一座車庫。你能將這些資訊新增到 `areas` 串列中嗎？

`@instructions`
- 使用 `+` 運算子，將串列 `["poolhouse", 24.5]` 串接到 `areas` 串列末尾，並將產生的新串列儲存為 `areas_1`。
- 繼續擴展 `areas_1`，新增關於車庫的資料，包括字串 `"garage"` 和浮點數 `15.45`。將擴展的新串列命名為 `areas_2`。

`@hint`
- 參考題目中的程式碼範例。這裡的 `x` 對應 `areas`，而 `["e", "f"]` 對應 `["poolhouse", 24.5]`。
- 要向 `areas_1` 新增更多元素，請使用 `areas_1 + ["element", 123]`。

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
msg = "請勿移除或編輯預定義的 `areas` 列表。"
Ex().check_object("areas", missing_msg = msg).has_equal_value(incorrect_msg = msg)
Ex().check_object("areas_1").has_equal_value(incorrect_msg = "使用 `areas + [\"poolhouse\", 24.5]` 來創建 `areas_1`。注意拼寫錯誤！")
Ex().check_object("areas_2").has_equal_value(incorrect_msg = "使用 `areas_1 + [\"garage\", 15.45]` 來創建 `areas_2`。注意拼寫錯誤！")
success_msg("太棒了！列表正在很好地成形！")
```

---

## 刪除串列元素

```yaml
type: NormalExercise
key: 85f792356e
xp: 100
```

最後，你還可以從串列中刪除元素。使用 `del` 陳述式即可完成：

```
x = ["a", "b", "c", "d"]
del x[1]
```

注意：一旦從串列中刪除某個元素，該元素後所有元素的索引都會改變！

可惜的是，你中樂透的獎金並沒有想像中那麼多，看來蓋泳池小屋的計畫要落空了。你需要把它從串列中刪除。因此，你決定從 `areas` 串列中刪除對應的字串和浮點數。

`@instructions`
- 從你的 `areas` 串列中刪除 `"poolhouse"` 對應的字串和浮點數。
- 輸出更新後的 `areas` 串列。

`@hint`
- 你需要呼叫 `del` 兩次來刪除兩個元素。不過要注意：索引在刪除元素後會發生變化！

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

Ex().has_printout(0, not_printed_msg="您是否在移除 poolhouse 字串和浮點數後印出 `areas`？")
success_msg("正確！稍後您將學習更簡單的方法來從 Python 列表中移除特定元素。")
```

---

## 串列的運作原理

```yaml
type: NormalExercise
key: af72db9915
lang: python
xp: 100
skills:
  - 2
```

本練習為你提供了一些範例程式碼：一個名為 `areas` 的串列，以及一個名為 `areas_copy` 的副本。

目前的程式碼修改了 `areas_copy` 串列中的第一個元素，並輸出了 `areas` 串列。如果你按下「執行程式碼」按鈕，就會發現雖然你修改的是 `areas_copy`，但在 `areas` 串列中也生效了。這是因為 `areas` 和 `areas_copy` 指向的是同一個串列。

如果你希望在修改 `areas_copy` 時不影響 `areas`，就必須使用 `list()` 或 `[:]`，建立 `areas` 串列的獨立副本。

`@instructions`
- 修改用於建立變數 `areas_copy` 的第二條指令，使 `areas_copy` 成為 `areas` 的獨立副本。完成修改後，對 `areas_copy` 所做的更改就不會影響 `areas` 了。你可以送出答案來進行驗證。

`@hint`
- 修改一下 `areas_copy = areas` 這行程式碼。不要直接指派 `areas`，可以改為指派 `list(areas)` 或 `areas[:]`。

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
  check_object("areas_copy").has_equal_value(incorrect_msg = "看來 `areas_copy` 沒有正確更新。"),
  check_function("list", missing_msg = "請確保使用 `list(areas)` 來創建 `areas_copy`。")
)

mmsg = "不要移除預定義的 `areas` 列表。"
imsg = "請確保僅編輯副本，而不是原始的 `areas` 列表。如果不確定如何創建副本，請再看看練習描述。"
Ex().check_correct(
  check_object("areas", missing_msg = mmsg).has_equal_value(incorrect_msg = imsg),
  check_function("list", missing_msg = "請確保使用 `list(areas)` 來創建 `areas_copy`。")
)

success_msg("很好！顯式和基於引用的副本之間的差異很微妙，但可能非常重要。請記住列表在計算機記憶體中的存儲方式。")
```

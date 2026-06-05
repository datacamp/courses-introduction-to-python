---
title_meta: 第 2 章
title: Python リスト
description: リストにデータを格納し、取り出し、操作する方法を学びましょう。大量のデータを効率よく扱うための第一歩です。
attachments:
  slides_link: 'https://projector-video-pdf-converter.datacamp.com/735/chapter2.pdf'
lessons:
  - nb_of_exercises: 4
    title: Python リスト
  - nb_of_exercises: 4
    title: リストのサブセット化
  - nb_of_exercises: 5
    title: リストの操作
---

## Python リスト

```yaml
type: VideoExercise
key: a5886d213f
xp: 50
```

`@projector_key`
a0530c4542f10988847b2dbb91f717c3

---

## リストを作成する

```yaml
type: NormalExercise
key: e6c527bf41
lang: python
xp: 100
skills:
  - 2
```

リストは複合データ型です。次のように、複数の値をまとめることができます。

```
a = "is"
b = "nice"
my_list = ["my", "list", a, b]
```

家族の身長を測定したあと、住んでいる家についての情報も集めることにしました。この演習では、家の各部分の面積が別々の変数に保存されています。

`@instructions`
- 廊下（`hall`）、キッチン（`kit`）、リビングルーム（`liv`）、寝室（`bed`）、バスルーム（`bath`）の面積をこの順番で含むリスト `areas` を作成してください。定義済みの変数を使ってください。
- `print()` 関数で `areas` を出力してください。

`@hint`
- 作成済みの変数を使って、リストを作成できます：`areas = [hall, kit, ...]`。
- 丸カッコ `()` ではなく、角カッコ `[]` を使いましょう。
- リストに変数を入れる場合、クォート（文字列を囲む ' や "）は必要ありません。
- 解答を送信する際は、`print(areas)` と入力してリストを出力してください。

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
predef_msg = "定義済みの変数を削除したり編集したりしないでください！"
areas_msg = "`areas` を、すべてのエリア変数を正しい順序で含むリストとして定義してください: `[hall, kit, liv, bed, bath]`。タイプミスに注意してください。リストには他のものを含めないでください！"

Ex().check_correct(
    has_printout(0, not_printed_msg = "__JINJA__:`{{sol_call}}` を使用してスクリプトの最後に `areas` リストを出力しましたか？"),
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

success_msg("素晴らしい！ここではリストの方がずっと良いですね。")
```

---

## 異なる型のリストを作成

```yaml
type: NormalExercise
key: 1702a8bcdc
lang: python
xp: 100
skills:
  - 2
```

あまり一般的ではありませんが、リストには文字列、float型の値、ブール値など、複数のPythonの型を混在させることもできます。

これからリストに部屋の名前を追加して、部屋の名前と広さを一緒に簡単に確認できるようにします。

作業を始めやすいように、コードの一部はすでに用意されています。ここで注意してください。 `"bathroom"` は文字列である一方、`bath` は先ほど指定したfloat型の値 `9.50` を表す変数です。

`@instructions`
- `areas` リストを作成するコードを完成させてください。リストでは、各部屋の名前を文字列として先に入れ、その後に面積を入れるようにします。つまり、適切な位置に文字列 `"hallway"`、`"kitchen"`、`"bedroom"` という文字列を追加します。
- `areas` をもう一度出力してみましょう。今回は出力内容がよりわかりやすくなりましたか？

`@hint`
- リスト `areas` の最初の4つの要素は `["hallway", hall, "kitchen", kit, ...` としてコードされています。
- 文字列はここではダブルクォート `""` で囲みます。

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
predef_msg = "定義済みの変数を削除または編集しないでください！"
areas_msg = "`areas` に正しい値を割り当てていません。指示をもう一度確認してください。各エリアを含む変数の前に部屋の名前を必ず置いてください。順序が重要です！タイプミスに注意してください。"

Ex().check_correct(
  check_object("areas").has_equal_value(incorrect_msg = areas_msg),
  multi([ check_object(obj, missing_msg = predef_msg).has_equal_value(incorrect_msg = predef_msg) for obj in objs])
)

Ex().has_printout(0, not_printed_msg = "__JINJA__:`{{sol_call}}` を使用してスクリプトの最後に `areas` リストを出力しましたか？")

success_msg("素晴らしいです！このリストには文字列と浮動小数点数の両方が含まれていますが、Pythonにとっては問題ありません！")
```

---

##  リストのリスト

```yaml
type: NormalExercise
key: 9158c577b0
lang: python
xp: 100
skills:
  - 2
```

データサイエンティストは、大量のデータを扱う場面がよくあります。そのため、関連するデータをまとめてグループ化すると便利です。

家の部屋の名前と面積を表す文字列やfloatを1つのリストに入れる代わりに、複数のリストを要素として持つリストを作成できます。

覚えておきましょう：`"hallway"` は文字列ですが、`hall` は先ほど指定した float 型の値`11.25`を表す変数です。

`@instructions`
- リストのリストを完成させ、bedroom と bathroom のデータも含めてください。必ずこの順番で入力してください。
- `house` を出力してください。このほうが、データの構造としてわかりやすくなりますか？

`@hint`
- 角カッコの中に `["bathroom", bath]` と `["bedroom", bed]` を追加して、`house` _サにブリスト_として加えます。
- 各サブリストの後にカンマ `,` を忘れずに入れてください。
- 変数 `x` を出力するには、新しい行に `print(x)` と入力します。

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
predef_msg = "定義済みの変数を削除したり編集したりしないでください！"
house_msg = "正しい値を`house`に割り当てていません。指示をもう一度見直してください。リストのリストを拡張して、各部屋名と部屋面積のペアのリストを組み込むようにしてください。順序とタイプミスに注意してください！"

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

Ex().has_printout(0, not_printed_msg = "__JINJA__:`{{sol_call}}`を使用して`house`の内容を印刷しましたか？")

success_msg("素晴らしいです！リストのサブセットについて学ぶ準備をしてください！")
```

---

## リストの要素を抽出する

```yaml
type: VideoExercise
key: c076b5a69c
xp: 50
```

`@projector_key`
fc15ba5cb9485456df8589130b519ea3

---

## 取り出して攻略

```yaml
type: NormalExercise
key: c3ce582e32
lang: python
xp: 100
skills:
  - 2
```

Pythonのリストから要素を取り出すのはとても簡単です。以下のサンプルコードを見てみましょう。リスト `x` を作成し、そこから "b" を取り出しています。これは2番目の要素なので、インデックスは 1 になることを覚えておきましょう。負のインデックスも使えます。

```
x = ["a", "b", "c", "d"]
x[1]
x[-3] # same result!
```

先ほどの `areas` リストを覚えていますか？文字列と float型の値の両方が含まれているリストです。その定義はすでにスクリプトにあります。正しいコードを追加して、Pythonでリストの要素を取り出す操作を試してみましょう。

`@instructions`
- `areas` リストから2番目の要素を出力してください。この要素の値は `11.25` です。
- `areas` の最後の要素である `9.50` を取り出して出力してください。ここでは負のインデックスを使うとよいでしょう。
- リビングルームの面積を表す数値 `20.0` 取り出して、出力してください。

`@hint`
- リスト `x[1]` の2番目の要素を取り出すには、`x` を使います。
- リスト `x` の最後の要素を取り出すには、`x[-1]`  を使います。
- リストから要素を取り出す処理は、必ず`print()` 呼び出しの中に入れてください。
- リビングルームの面積を表す数値はリスト内の6番目の要素なので、ここでは、`[5]` が必要です。 `area[4]` を使うと、文字列が表示されてしまいます。。

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
msg = "定義済みの `areas` リストを削除または編集しないでください。"
Ex().check_object("areas", missing_msg = msg).has_equal_value(incorrect_msg = msg)
Ex().has_printout(0, not_printed_msg = "コードをもう一度見直して、`areas` の2番目の要素を出力してください。それはインデックス `1` にあります。")
Ex().has_printout(1, not_printed_msg = "コードをもう一度見直して、`areas` の最後の要素を出力してください。それはインデックス `-1` にあります。")
Ex().has_printout(2, not_printed_msg = "コードをもう一度見直して、リビングルームの面積を出力してください。それはインデックス `5` にあります。")
success_msg("よくできました！")
```

---

## スライスを使いこなす

```yaml
type: NormalExercise
key: 7f08642d18
lang: python
xp: 100
skills:
  - 2
```

リストから1つの値を取り出すのは、方法の一部にすぎません。リストを_スライス_することもできます。することもできます。これは、リストから複数の要素を取り出すという意味です。次の構文を使います。

```
my_list[start:end]
```

`start` インデックスは含まれますが、`end` インデックスは _含まれません_。ただし、これらのインデックスを指定しないこともできます。 `start` インデックスを指定しない場合、Pythonはリストの先頭からスライスを開始すると判断します。

`@instructions`
- スライスを使って、`areas` の最初の6個の要素を含むリスト `downstairs` を作成してください。
- `areas` の最後の `4` 個の要素として、`upstairs` を作成してください。今回は、`end` インデックスを省略してスライスを簡略化します。
- `print()` を使って、`downstairs` と `upstairs` の両方を出力してください。

`@hint`
-  リストの最初の6個の要素を取り出すには、角括弧 `[0:6]` を使います。
- リスト `l` の最初の5個の要素以外をすべて取り出すには、`l[5:]` を使います。
- `print()` を2回使って、`downstairs`  と `upstairs` を出力してください。

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
msg = "定義済みの `areas` リストを削除または編集しないでください。"
Ex().check_object("areas", missing_msg = msg).has_equal_value(incorrect_msg = msg)

patt = "`%s` が正しくありません。`areas[%s]` とスライスを使用して、必要な要素を選択するか、同等のものを使用してください。"
Ex().check_object("downstairs").has_equal_value(incorrect_msg = patt % ('downstairs', '0:6'))
Ex().check_object("upstairs").has_equal_value(incorrect_msg = patt % ("upstairs",":6"))

Ex().has_printout(0, not_printed_msg="計算後に `downstairs` を出力しましたか？")
Ex().has_printout(1, not_printed_msg="計算後に `upstairs` を出力しましたか？")

success_msg("素晴らしいです！")
```

---

## リストのリストの要素を取り出す

```yaml
type: NormalExercise
key: dbbbd306cf
xp: 100
```

Python のリストは、他のリストを要素として含むことができます。

リストのリストから一部を取り出すには、これまでと同じ方法で角括弧を使います。`house`の場合、次のようになります。```
house[2][0]
``` 



`@instructions`
- `house` リストからfloat型の値 `9.5` を取り出します。

`@hint`
- 順を追って考えてみましょう。まず、リストの最後の要素 `["bathroom", 9.50]` を取り出します。最後の要素のインデックスは `-1` でしたね。
- 次に、`["bathroom", 9.50]` の2番目の要素を取り出します。インデックスは `1` です。

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

success_msg("正解です！リストパズルの最後のピースは操作です。")
```

---

## リストの操作

```yaml
type: VideoExercise
key: d7fe818b3a
xp: 50
```

`@projector_key`
355ed52d2fb0d67508c6a311b7cbc6d3

---

## リストの要素を置き換える

```yaml
type: NormalExercise
key: 4e1bba1b55
lang: python
xp: 100
skills:
  - 2
```

リストの要素を置き換えるには、リストから対象の要素やスライスを指定し、そこに新しい値を代入します。1つの要素を指定することも、リストのスライス全体を一度に変更することもできます。

この演習と以降の演習では、家のさまざまな部屋の名前と面積が含まれている `areas`リストを引き続き扱います。

`@instructions`
- 負のインデックスを使って、バスルームの面積を `9.50` 平方メートルから `10.50` 平方メートルに更新します。
- `areas` リストをもっと今風にしましょう。`"living room"` を `"chill zone"`（チル部屋） に変更します。今回は負のインデックスを使わないでください。

`@hint`
- バスルームの面積を更新するには、バスルームの面積に対応する要素を特定しましょう（リストの最後の要素です）。
- 次に、その要素に新しいバスルームの面積を代入して、値を置き換えます。
- インデックス 4 にある `"living room"` という名前も、同じように更新してください。

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
bathroom_msg = 'バスルームの面積を更新するには、`areas[-1] = 10.50` を使用できます。'
chillzone_msg = 'リビングルームの名前を更新するには、`areas[4] = "chill zone"` を使用できます。'
Ex().check_correct(
  check_object('areas').has_equal_value(incorrect_msg = 'あなたの `areas` への変更は正しいリストになりませんでした。正しいサブセット操作を使用したか確認しましたか？迷ったときは、ヒントを使用できます！'),
  multi(
    has_equal_value(expr_code='areas[-1]', override=10.50, incorrect_msg = bathroom_msg),
    has_equal_value(expr_code='areas[4]', override='chill zone', incorrect_msg = chillzone_msg),
  )
)
success_msg('素晴らしいです！コードサンプルが示したように、リストをスライスして別のリストで置き換えることで、単一のコマンドで複数の要素を更新することもできます。')
```

---

## リストを拡張する

```yaml
type: NormalExercise
key: ff0fe8d967
lang: python
xp: 100
skills:
  - 2
```

リスト内の要素を変更できるなら、要素を追加できるようにもなりたいですよね。`+` プラス演算子を使うことができます。

```
x = ["a", "b", "c", "d"]
y = x + ["e", "f"]
```

宝くじに当たりました。すごいですね！プールハウスとガレージを建てることにしました。この情報を `areas` リストに追加してみましょう。

`@instructions`
- `+` 演算子を使って、リスト `["poolhouse", 24.5]` を `areas` リストの末尾に追加しましょう。結果のリストを `areas_1` として保存してください。
- ガレージのデータを追加して `areas_1` をさらに拡張してください。文字列 `"garage"` とfloat型の値 `15.45` を追加します。結果のリストに `areas_2` という名前を付けてください。

`@hint`
- 問題文のコード例を参考にしましょう。ここでは `x` が `areas`、`["e", "f"]` が `["poolhouse", 24.5]` にあたります。
- `areas_1` にさらに要素を追加するには、`areas_1 + ["element", 123]` を使います。

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
msg = "定義済みの `areas` リストを削除または編集しないでください。"
Ex().check_object("areas", missing_msg = msg).has_equal_value(incorrect_msg = msg)
Ex().check_object("areas_1").has_equal_value(incorrect_msg = "`areas + [\"poolhouse\", 24.5]` を使用して `areas_1` を作成してください。タイプミスに注意してください！")
Ex().check_object("areas_2").has_equal_value(incorrect_msg = "`areas_1 + [\"garage\", 15.45]` を使用して `areas_2` を作成してください。タイプミスに注意してください！")
success_msg("素晴らしいです！リストがうまく形になっています！")
```

---

## リスト要素の削除

```yaml
type: NormalExercise
key: 85f792356e
xp: 100
```

最後に、リストから要素を削除することもできます。削除には `del` 文を使います。

```
x = ["a", "b", "c", "d"]
del x[1]
```

ここで注意してください。リストから要素を削除すると、それ以降の要素のインデックスはすべて変わります。

残念ながら、宝くじで当たった金額はそれほど大きくなく、プールハウスの建設は難しそうです。リストからプールハウスの要素を削除する必要があります。`areas` リストから、対応する文字列とfloat型の値を削除することにします。

`@instructions`
- `areas`リストから、`"poolhouse"`に対応する文字列と float型の値を削除してください。
- 更新後の `areas` リストを出力してください。

`@hint`
- 2つの要素を削除するには、`del` を2回使います。ただし、1つ目の要素を削除すると、残りの要素のインデックスが変わる点に注意してください。

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

Ex().has_printout(0, not_printed_msg="`areas`をプールハウスの文字列と浮動小数点数を削除した後に出力しましたか？")
success_msg("正解です！Pythonのリストから特定の要素を削除するより簡単な方法については、後ほど学びます。")
```

---

## リストの内部の仕組み

```yaml
type: NormalExercise
key: af72db9915
lang: python
xp: 100
skills:
  - 2
```

この演習では、`areas` という名前のリストと、それをコピーしたリストである `areas_copy` があらかじめ用意されています。

現在、`areas_copy` リストの最初の要素が変更され、`areas` リストが出力されるようになっています。「コードを実行する」 ボタンを押すと、`areas_copy` を変更したにもかかわらず、その変更が `areas` リストにも反映されていることがわかります。これは、`areas` と `areas_copy` が同じリストを参照しているためです。

`areas_copy` での変更が `areas` に反映されないようにするには、`list()` または `[:]` を使って、`areas` リストを明示的にコピーする必要があります。

`@instructions`
- 変数 `areas_copy` を作成している2行目を変更して、`areas_copy` が `areas` の明示的なコピーになるようにしてください。編集後、`areas_copy` に加えた変更が `areas` に影響しないはずです。**解答を送信**して確認しましょう。

`@hint`
- `areas_copy = areas` の呼び出しを変更してください。`areas` を代入する代わりに、`list(areas)` または `areas[:]` を代入できます。

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
  check_object("areas_copy").has_equal_value(incorrect_msg = "「areas_copy」が正しく更新されていないようです。"),
  check_function("list", missing_msg = "「list(areas)」を使用して「areas_copy」を作成することを確認してください。")
)

mmsg = "事前定義された「areas」リストを削除しないでください。"
imsg = "コピーのみを編集し、元の「areas」リストを編集しないようにしてください。コピーの作成方法が不明な場合は、演習の説明をもう一度確認してください。"
Ex().check_correct(
  check_object("areas", missing_msg = mmsg).has_equal_value(incorrect_msg = imsg),
  check_function("list", missing_msg = "「list(areas)」を使用して「areas_copy」を作成することを確認してください。")
)

success_msg("素晴らしいです！明示的なコピーと参照ベースのコピーの違いは微妙ですが、非常に重要な場合があります。リストがコンピュータのメモリにどのように保存されるかを心に留めておいてください。")
```

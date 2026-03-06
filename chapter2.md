---
title_meta: 第2章
title: Pythonのリスト
description: 大量のデータを効率的に扱う第一歩として、リストでデータを保存・アクセス・操作する方法を学びます。
attachments:
  slides_link: 'https://projector-video-pdf-converter.datacamp.com/735/chapter2.pdf'
lessons:
  - nb_of_exercises: 4
    title: Pythonのリスト
  - nb_of_exercises: 4
    title: リストの抽出
  - nb_of_exercises: 5
    title: リストの操作
---

## Pythonのリスト

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

リストは**複合データ型**で、次のように値をまとめて扱うことができます。

```
a = "is"
b = "nice"
my_list = ["my", "list", a, b]
```

家族の身長を測ったあと、今度は住んでいる家についての情報を集めることにしました。家の各部屋の面積は、この演習内で別々の変数に保存されています。

`@instructions`
- 玄関ホール（`hall`）、キッチン（`kit`）、リビング（`liv`）、寝室（`bed`）、バスルーム（`bath`）の面積を、この順番で含むリスト `areas` を、あらかじめ用意された変数を使って作成してください。
- `print()` 関数で `areas` を出力してください。

`@hint`
- すでに作成されている変数を使ってリストを作成できます: `areas = [hall, kit, ...]`。
- かっこは丸かっこ `()` ではなく、角かっこ `[]` を使ってください。
- リストに変数を入れるときは、引用符で囲む必要はありません。
- 提出時にリストを表示するには、`print(areas)` と入力します。

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

## 異なる型を含むリストを作成する

```yaml
type: NormalExercise
key: 1702a8bcdc
lang: python
xp: 100
skills:
  - 2
```

一般的ではありませんが、リストには文字列、浮動小数点数、真偽値など、異なるPythonの型を混在させて格納できます。

ここでは部屋の名前をリストに追加して、部屋名と広さを並べて見られるようにします。

一部のコードは用意されています。ここに注意してください。`"bathroom"` は文字列ですが、`bath` は先ほど指定した浮動小数点数 `9.50` を表す変数です。

`@instructions`
- `areas` リストを作成するコードを完成させてください。各部屋の名前（文字列）に続けてその広さが入るようにリストを構築します。言い換えると、適切な位置に文字列 `"hallway"`、`"kitchen"`、`"bedroom"` を追加してください。
- `areas` をもう一度printしてみましょう。今回はより情報が分かりやすく表示されますか？

`@hint`
- リスト `areas` の最初の4要素は `["hallway", hall, "kitchen", kit, ...` のように書かれています。
- 文字列は必ず `""` の引用符で囲む必要があります。

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

## リストのリスト

```yaml
type: NormalExercise
key: 9158c577b0
lang: python
xp: 100
skills:
  - 2
```

データサイエンティストとしては、多くのデータを扱うことがよくあり、その一部をまとめてグループ化すると便利です。

部屋の名前と面積を表す文字列と浮動小数点数を1つのリストに入れる代わりに、リストのリストを作成できます。

おさらいです：`"hallway"` は文字列で、`hall` は先ほど指定した浮動小数点数 `11.25` を表す変数です。

`@instructions`
- リストのリストを完成させ、bedroom と bathroom のデータも含めてください。必ずこの順序で入力しましょう！
- `house` を出力してみましょう。このデータ構造のほうが分かりやすくなっていますか？

`@hint`
- 角かっこ内に `["bedroom", bed]` と `["bathroom", bath]` を追加して、`house` リストにサブリストを加えます。
- 各サブリストの後にはコンマ `,` を忘れずに入れてください。
- 変数 `x` を出力するには、新しい行に `print(x)` と書きます。

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

## リストの抽出

```yaml
type: VideoExercise
key: c076b5a69c
xp: 50
```

`@projector_key`
fc15ba5cb9485456df8589130b519ea3

---

## Subset and conquer

```yaml
type: NormalExercise
key: c3ce582e32
lang: python
xp: 100
skills:
  - 2
```

Python のリストの部分抽出はとても簡単です。次のコード例では、リスト `x` を作成し、そこから "b" を選びます。これは2番目の要素なので、インデックスは 1 です。負のインデックスも使えます。

```
x = ["a", "b", "c", "d"]
x[1]
x[-3] # 同じ結果！
```

以前に出てきた、文字列と浮動小数点数が混在する `areas` リストを覚えていますか？定義はすでにスクリプトにあります。正しいコードを追加して、Python の部分抽出をしてみましょう。

`@instructions`
- `areas` リストの2番目の要素（値は `11.25`）を出力してください。
- `areas` の最後の要素（`9.50`）を抽出して出力してください。ここでは負のインデックスを使うのが適しています！
- リビングの面積を表す数値（`20.0`）を選んで、出力してください。

`@hint`
- リスト `x` の2番目の要素を選ぶには `x[1]` を使います。
- リスト `x` の最後の要素を選ぶには `x[-1]` を使います。
- 取り出した結果は `print()` で表示するようにしてください。
- リビングの面積を表す数値はリストの6番目の要素なので、ここでは `[5]` が必要です。`area[4]` だと文字列が表示されてしまいます！

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

## スライスで取り出そう

```yaml
type: NormalExercise
key: 7f08642d18
lang: python
xp: 100
skills:
  - 2
```

リストから単一の値を取り出すだけがすべてではありません。リストをスライスして、複数の要素をまとめて取り出すこともできます。構文は次のとおりです。

```
my_list[start:end]
```

`start` のインデックスは含まれますが、`end` のインデックスは含まれません。また、これらのインデックスを省略することもできます。`start` を省略すると、リストの先頭からスライスを始めるとPythonが解釈します。

`@instructions`
- スライスを使って、`areas` の最初の6要素を含むリスト `downstairs` を作成します。
- `areas` の最後の `4` 要素から `upstairs` を作成します。今回は `end` インデックスを省略してスライスを簡潔に書きましょう。
- `print()` を使って `downstairs` と `upstairs` の両方を出力します。

`@hint`
- リストの最初の6要素を取得するには、角かっこ `[0:6]` を使います。
- リスト `l` の先頭5要素以外すべてを取得するには、`l[5:]` を使います。
- `print()` を2回追加して、`downstairs` と `upstairs` を出力します。

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

## リストのリストの抽出

```yaml
type: NormalExercise
key: dbbbd306cf
xp: 100
```

Python のリストには、他のリストを含めることもできます。

リストのリストを抽出するには、これまでと同じく角かっこを使います。リスト `house` の場合、次のようになります。

```
house[2][0]
```

`@instructions`
- `house` リストから浮動小数 `9.5` を取り出してください。

`@hint`
- 段階的に進めていきましょう。まずはリストの最後の要素 `["bathroom", 9.50]` を取り出します。最後の要素のインデックスは `-1` です。
- 次に、`["bathroom", 9.50]` の2番目の要素を取得します。これはインデックス `1` にあります。

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

## リスト要素の置き換え

```yaml
type: NormalExercise
key: 4e1bba1b55
lang: python
xp: 100
skills:
  - 2
```

リストの要素を置き換えるには、リストを部分的に抽出して、その部分に新しい値を代入します。単一の要素を選ぶことも、リストのスライス全体を一度に変更することもできます。

この演習および次の演習では、家の各部屋の名前と面積が入った `areas` リストを引き続き使います。

`@instructions`
- バスルームの面積を、負のインデックスを使って `9.50` 平方メートルではなく `10.50` に更新してください。
- `areas` リストを今風にしましょう！ `"living room"` を `"chill zone"` に変更します。今回は負のインデックスは使わないでください。

`@hint`
- バスルームの面積を更新するには、まずバスルームの面積の要素を特定します（リストの最後の要素です！）。
- 次に、この部分集合に新しいバスルームの面積を代入して値を置き換えます。
- 同様に、インデックス 4 にある `"living room"` の名前も更新しましょう。

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

リストの要素を変更できるなら、要素を追加もしたいですよね。`+` 演算子が使えます。

```
x = ["a", "b", "c", "d"]
y = x + ["e", "f"]
```

宝くじに当たりました。やりましたね！プールハウスとガレージを建てることにしました。`areas` リストにこの情報を追加できますか？

`@instructions`
- `+` 演算子を使って、リスト `["poolhouse", 24.5]` を `areas` の末尾に連結し、結果を `areas_1` として保存します。
- さらにガレージのデータを追加して `areas_1` を拡張します。文字列 `"garage"` と浮動小数点数 `15.45` を加え、結果のリストを `areas_2` と名付けます。

`@hint`
- 課題のコード例にならいましょう。ここでの `x` は `areas`、`["e", "f"]` は `["poolhouse", 24.5]` にあたります。
- `areas_1` にさらに要素を追加するには、`areas_1 + ["element", 123]` のようにします。

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

最後に、リストから要素を削除することもできます。これは `del` 文で行います。

```
x = ["a", "b", "c", "d"]
del x[1]
```

ここは重要です。リストから要素を1つ削除すると、その要素より後ろにある要素のインデックスがすべて変わります！

残念ながら、宝くじの当選額はそれほど大きくなく、どうやら poolhouse の建設は見送りになりそうです。リストから削除しましょう。`areas` リストから、該当する文字列と浮動小数点数を削除してください。

`@instructions`
- `areas` リストから、`"poolhouse"` に対応する文字列と浮動小数点数を削除してください。
- 更新後の `areas` リストを出力してください。

`@hint`
- 2つの要素を削除するには `del` を2回使う必要があります。ただし、インデックスが変わる点に注意してください！

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

## リストの内部動作

```yaml
type: NormalExercise
key: af72db9915
lang: python
xp: 100
skills:
  - 2
```

この演習では、`areas` という名前のリストと、そのコピーである `areas_copy` が用意されています。

現在は、`areas_copy` リストの最初の要素を変更し、その後に `areas` リストを出力しています。**コードを実行する** ボタンを押すと、`areas_copy` を変更したにもかかわらず、その変更が `areas` リストにも反映されることがわかります。これは、`areas` と `areas_copy` が同じリストを指しているためです。

`areas_copy` の変更が `areas` にも影響するのを防ぐには、`list()` や `[:]` を使って、`areas` リストをより明示的にコピーする必要があります。

`@instructions`
- 変数 `areas_copy` を作成している2行目のコマンドを変更し、`areas_copy` が `areas` の明示的なコピーになるようにしてください。編集後は、`areas_copy` に加えた変更が `areas` に影響しないはずです。確認のために **回答を送信** してください。

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

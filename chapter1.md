---
title_meta: 第1章
title: Pythonの基本
description: >-
  Pythonの基本概念を紹介します。対話的にPythonを使う方法と、スクリプトとして使う方法を学びます。最初の変数を作成し、Pythonの基本的なデータ型に慣れましょう。
attachments:
  slides_link: 'https://projector-video-pdf-converter.datacamp.com/735/chapter1.pdf'
free_preview: true
lessons:
  - nb_of_exercises: 3
    title: Hello Python!
  - nb_of_exercises: 5
    title: 変数と型
---

## Hello Python!

```yaml
type: VideoExercise
key: f644a48d5d
xp: 50
```

`@projector_key`
d8fcd4c930027fa4e1c3870c7e7e0ff1

---

## はじめてのPythonコード

```yaml
type: NormalExercise
key: bdc52f0e19
lang: python
xp: 100
skills:
  - 2
```

いよいよ、はじめてのPythonコードを実行します！

エディタのコードに移動し、「コードを実行する」ボタンを押して出力を確認しましょう。

`@instructions`
- 「コードを実行する」ボタンを押して、`print(5 / 8)` の出力を見てみましょう。

`@hint`
- まず「コードを実行する」でコードを走らせて、出力を確認してから回答を送信すると落ち着いて試せます。

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
Ex().has_printout(0, not_printed_msg = "__JINJA__:`{{sol_call}}`を使用して`5 / 8`を出力しましたか？")
success_msg("素晴らしいです！次に進みましょう！")
```

---

## 電卓としての Python

```yaml
type: NormalExercise
key: 0f7c039428
lang: python
xp: 100
skills:
  - 2
```

Python は簡単な計算に最適です。足し算、引き算、掛け算、割り算ができます。

スクリプト内のコードにいくつかの例があります。

次はあなたの番です。実際にコードを書いて練習してみましょう。

`@instructions`
- `# Subtraction` の下で、`print()` を使って `5` から `5` を引いた結果を表示します。
- `# Multiplication` の下で、`3` に `5` を掛けた結果を表示します。

`@hint`
- 出力を表示するには `print()` を使います。
- 引き算は `-`、掛け算は `*` で行えます。

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
Ex().has_printout(0, not_printed_msg = "和の結果を出力するために `print(4 + 5)` を使用しましたか？")

Ex().has_printout(1, not_printed_msg = "減算の結果を出力するために `print(5 - 5)` を使用しましたか？")

Ex().has_printout(2, not_printed_msg = "乗算の結果を出力するために `print(3 * 5)` を使用しましたか？")

Ex().has_printout(3, not_printed_msg = "除算の結果を出力するために `print(10 / 2)` を使用しましたか？")

success_msg("その通りです！Pythonは計算を手助けしてくれます。これは、データスキルを向上させるにつれて分析に役立つ特性です。")
```

---

## 変数と型

```yaml
type: VideoExercise
key: c2e396792e
xp: 50
```

`@projector_key`
433dcfcfedaee070cbf440491c402e3b

---

## 変数の代入

```yaml
type: NormalExercise
key: 4bf65ad83e
lang: python
xp: 100
skills:
  - 2
```

Python では、変数を使って値に名前を付けて参照できます。値が `5` の変数 `x` を作成するには、次の例のように `=` を使います。

```
x = 5
```

これで実際の値 `5` の代わりに、変数名 `x` を使えるようになります。

なお、Python の `=` は等価をテストするのではなく、_代入_ を意味します。演習では、`____` をあなたのコードに置き換えて試してみてください。

`@instructions`
- 値が `100` の変数 `savings` を作成します。
- スクリプトで `print(savings)` と入力して、この変数を確認します。

`@hint`
- 変数 `savings` を作成するには、`savings = 100` と入力します。
- 変数 `savings` を作成したら、`print(savings)` と入力して確認できます。
- 最終的なコードには `____` を含めないでください。

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
Ex().check_object("savings").has_equal_value(incorrect_msg="変数 `savings` に `100` を代入してください。")
Ex().has_printout(0, not_printed_msg = "作成した変数 `savings` を `print(savings)` で出力してください。")
success_msg("素晴らしいです！次に、この変数を使っていくつかの計算をしてみましょう！")
```

---

## 変数で計算する

```yaml
type: NormalExercise
key: ff06cedeb4
lang: python
xp: 100
skills:
  - 2
```

貯金用の変数を作成できました。さっそく貯金を始めましょう！

実際の数値で計算する代わりに、変数を使うことができます。

毎月 $10 貯金するとして、4 か月後にはいくら貯まっているでしょうか。

`@instructions`
- 変数 `monthly_savings` に `10` を、`num_months` に `4` を代入します。
- `monthly_savings` と `num_months` を掛け算して、結果を `new_savings` に代入します。
- `new_savings` の値を出力します。

`@hint`
- 変数でも数値と同じように計算できます。つまり、`10 * 4` の数値部分を変数に置き換えましょう。
- `print()` を使って、`new_savings` の金額を表示します。
- 変数名のつづりを正確に書くように注意してください。

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
Ex().check_object("monthly_savings").has_equal_value(incorrect_msg = "「monthly_savings」に`10`を`monthly_savings = 10`を使って保存しましたか？")
Ex().check_object("num_months").has_equal_value(incorrect_msg = "「num_months」に`4`を`num_months = 4`を使って保存しましたか？")
Ex().check_object("new_savings").has_equal_value(incorrect_msg = "正しい変数と記号を使って掛け算をしましたか？`monthly_savings * num_months`が期待されますが、他のものが得られました。")
# Ex().check_object("total_savings").has_equal_value(incorrect_msg = "正しい変数と記号を使って足し算をしましたか？`savings + new_savings`が期待されますが、他のものが得られました。")

Ex().has_printout(0, not_printed_msg="スクリプトの最後に「new_savings」を出力することを忘れないでください。")

success_msg("新しい貯金が$40あります！")
```

---

## ほかの変数型

```yaml
type: NormalExercise
key: 006b48561f
lang: python
xp: 100
skills:
  - 2
```

前の演習では、Pythonの整数型を扱いました。

- `int`（整数）：小数部分のない数。値が `100` の `savings` は整数の例です。

数値型以外にも、よく使うデータ型が3つあります。

- `float`（浮動小数点数）：整数部分と小数部分を持ち、ピリオドで区切られる数。`1.1` は float の例です。
- `str`（文字列）：テキストを表す型。文字列はシングルクォートまたはダブルクォートで作成できます。
- `bool`（ブール値）：論理値を表す型。`True` か `False` のどちらかのみです（大文字小文字は重要です！）。

`@instructions`
- 値が `0.5` の新しい float、`half` を作成します。
- 値が `"Hello! How are you?"` の新しい文字列、`intro` を作成します。
- 値が `True` の新しいブール値、`is_good` を作成します。

`@hint`
- Pythonで変数を作るには、`=` を使います。文字列は必ずシングルクォートまたはダブルクォートで囲んでください。
- Pythonにあるブール値は2つだけです: `True` と `False`。`TRUE`、`true`、`FALSE`、`false` などは受け付けられません。

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
Ex().check_object("half").has_equal_value(incorrect_msg = "浮動小数点 `0.5` を `half` に保存しましたか？")

Ex().check_object("intro").has_equal_value(incorrect_msg = "うーん、`intro` 変数に何か間違いがあります。スペルを再確認し、引用符を使用したことを確認してください。")

Ex().check_object("is_good").has_equal_value(incorrect_msg = "ブール値を大文字にしましたか？ここでは引用符を使用する必要はありません。")

success_msg("素晴らしいです！")
```

---

## ほかの型での演算

```yaml
type: BulletExercise
key: 4d0d83cc02
xp: 100
```

Python では、変数にはさまざまな型があります。変数の型は `type()` で確認できます。たとえば、`a` の型を確認するには `type(a)` を実行します。

型が違うと、Python での振る舞いも変わります。たとえば、2つの文字列を足す場合は、2つの整数や2つのブール値を足す場合とは異なる結果になります。

それでは実際に試してみましょう。

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
- `savings` と `new_savings` を足して、`total_savings` に代入します。
- `type()` を使って、`total_savings` の型を表示します。

`@hint`
- `savings + new_savings` を新しい変数 `total_savings` に代入します。
- 変数 `x` の型を表示するには、`print(type(x))` を使います。

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
msg = "既定の変数を変更または削除する必要はありません。"

Ex().multi(
    check_object('savings', missing_msg=msg).has_equal_value(incorrect_msg=msg),
    check_object('new_savings', missing_msg=msg).has_equal_value(incorrect_msg=msg)
)

Ex().multi(
    check_object("total_savings").has_equal_value(incorrect_msg="`savings` と `new_savings` を加算して `total_savings` 変数を作成してください。"),
    has_printout(1, not_printed_msg = "__JINJA__:`{{sol_call}}` を使用して `total_savings` の型を出力してください。")
)
```

***

```yaml
type: NormalExercise
key: f54fbf9bd9
xp: 50
```

`@instructions`
- `intro` と `intro` の和を計算し、結果を `doubleintro` に代入します。
- `doubleintro` を出力します。予想どおりの結果になりましたか？

`@hint`
- `intro + intro` を新しい変数 `doubleintro` に代入します。
- 変数 `x` を表示するには、スクリプトで `print(x)` と書きます。

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
msg = "定義済みの変数を変更または削除する必要はありません。"

Ex().check_object('intro', missing_msg=msg).has_equal_value(incorrect_msg=msg)

Ex().multi(
    check_object("doubleintro").has_equal_value(incorrect_msg  = "`intro + intro` の結果を `doubleintro` に格納しましたか？"),
    has_printout(0, not_printed_msg = "`doubleintro` を出力するのを忘れないでください。")
)

success_msg("素晴らしいです。`intro + intro` が `\"Hello! How are you?\"` と `\"Hello! How are you?\"` を結合することに注意してください。")
```

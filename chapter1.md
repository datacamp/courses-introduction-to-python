---
title_meta: 第 1 章
title: Python の基礎
description: >-
  Python の基本概念を紹介します。コードを1行ずつ実行しながら Python
  を使う方法と、スクリプトを使う方法を学びます。初めての変数を作成し、Python の基本的なデータ型に慣れましょう。
attachments:
  slides_link: 'https://projector-video-pdf-converter.datacamp.com/735/chapter1.pdf'
free_preview: true
lessons:
  - nb_of_exercises: 3
    title: こんにちは、Python！
  - nb_of_exercises: 5
    title: 変数と型
---

## こんにちは、Python！

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

はじめてのPythonコードを実行してみましょう！コードエディタに移動し、「コードを実行する」を押して出力を確認してください。

`@instructions`
- 「コードを実行する」を押して、`print(5 / 8)` の出力を確認しましょう。

`@hint`
- 解答を送信する前に、まずコードを実行して、出力を確認する時間を取りましょう。

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

Pythonは基本的な計算を行うのに適しています。足し算、引き算、掛け算、割り算ができます。

スクリプト内のコードには、いくつかの例が示されています。

では、実際にコードを書いて練習してみましょう。

`@instructions`
- `5` から `5` を引いた結果を、`# Subtraction` の下に `print()` を使って表示してください。
- `3` に `5` を掛けた結果を、`# Multiplication` の下に表示してください。

`@hint`
- 出力を表示するには `print()` を使います。
- 引き算には `-`、掛け算には `*` を使います。

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

## 変数への代入

```yaml
type: NormalExercise
key: 4bf65ad83e
lang: python
xp: 100
skills:
  - 2
```

Pythonでは、変数を使うと値に名前を付けて、あとから使うことができます。たとえば、値が `5` の変数 `x` を作成するには、次の例のように `=` を使います。

```
x = 5
```

これで、`5` の代わりに、`x` を使えるようになります。

Pythonの `=` は代入を意味し、等しいかどうかを調べるものではありません。演習では、`____` を自分のコードに置き換えて試してみてください。

`@instructions`
- 値が `100` の変数 `savings` を作成してください。
- スクリプトに `print(savings)` と入力して、この変数を確認してください。

`@hint`
`savings` という変数を作成するには、`savings = 100` と入力します。
変数 `savings` を作成したら、`print(savings)`  と入力できます。
最終的なコードに `____` が含まれていないようにしてください。

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

## 変数を使った計算

```yaml
type: NormalExercise
key: ff06cedeb4
lang: python
xp: 100
skills:
  - 2
```

貯金額を表す変数を作成したので、さっそく貯金を始めましょう！数値を直接使う代わりに、変数を使って計算できます。

毎月 $10 貯金した場合、4か月後にはいくら貯まっているでしょうか？

`@instructions`
- `monthly_savings` という変数を作成し、`10` を代入します。また、`num_months` という変数を作成し、`4` を代入します。
- `monthly_savings` に `num_months` を掛け、その結果を `new_savings` に代入します。
- `new_savings` の値を出力します。

`@hint`
- 変数を使った計算は、数値を使った計算と同じように行えます。`10 * 4` の計算式の数値を変数に置き換えればよいということです。
- `print()` を使って `new_savings` の値を確認できます。
- 変数名の綴りを間違えないように注意してください。

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

## その他の変数の型

```yaml
type: NormalExercise
key: 006b48561f
lang: python
xp: 100
skills:
  - 2
```

前の演習では、整数を表すPythonのデータ型を扱いました。

- `int`（整数型）：小数部分を持たない数値です。値が `100` の `savings` は integer の例です。

数値データ型の次に、非常によく使われるデータ型がほかに3つあります。

- `float`（浮動小数点型）：整数部分と小数部分を持ち、それらが小数点で区切られた数値です。`1.1` は float の例です。
- `str`（文字列型）：テキストを表す型です。文字列を作るには、シングルクォートまたはダブルクォートを使います。これを string と言います。
- `bool`（真偽値型）：論理値を表す型です。値は `True` または `False` のみです。大文字と小文字の違いが重要です。これを boolean といいます。

`@instructions`
- 新しいfloat型の変数 `half` を作成し、値 `0.5` を代入します。
- 新しいstr型の変数 `intro` を作成し、値 `"Hello! How are you?"` を代入します。
- 新しいbool型の変数 `is_good` を作成し、値 `True` を代入します。

`@hint`
- Python で変数を作成するには、`=` を使います。文字列は必ずシングルクォートまたはダブルクォートで囲んでください。
- Python に存在する boolean 値（真偽値型）は `True` と `False` の2つだけです。`TRUE`、`true`、`FALSE`、`false` など、他の形式は使用できません。

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

## 他の型との演算

```yaml
type: BulletExercise
key: 4d0d83cc02
xp: 100
```

Python では、変数にはさまざまな型があります。変数の型は `type()` を使って確認できます。たとえば、`a` の型を確認するには `type(a)` を実行します。

Pythonでは、型が異なると動作も異なります。たとえば、2つの文字列を足すと、2つの整数や2つのbool値をす場合とは異なる動作になります。

実際に試してみましょう。

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
- `savings` と `new_savings` を足し合わせ、`total_savings` に代入します。
- `type()` を使って、`total_savings` の結果の型を出力します。

`@hint`
- `savings + new_savings` を新しい変数 `total_savings` に代入します。
- 変数 `x` の型を出力するには、`print(type(x))` を使います。

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
- `intro` と `intro` の合計を計算し、その結果を `doubleintro` に代入します。
- `doubleintro` を出力します。これは予想していましたか？

`@hint`
- `intro + intro` を新しい変数 `doubleintro` に代入します。
- 変数 `x` を出力するには、スクリプトに `print(x)` と入力します。

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

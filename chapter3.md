---
title_meta: 第3章
title: 関数とパッケージ
description: >-
  優れたPython開発者が書いたコードを、関数・メソッド・パッケージで効率よく活用する方法を学びます。目的は、難しい問題を解くために必要なコード量を減らすことです。
attachments:
  slides_link: 'https://projector-video-pdf-converter.datacamp.com/735/chapter3.pdf'
lessons:
  - nb_of_exercises: 4
    title: 関数
  - nb_of_exercises: 4
    title: メソッド
  - nb_of_exercises: 4
    title: パッケージ
---

## 関数

```yaml
type: VideoExercise
key: 5c5f365930
xp: 50
```

`@projector_key`
1204d914b0e53100529827e07441ee6c

---

## おなじみの関数

```yaml
type: NormalExercise
key: c422ee929b
lang: python
xp: 100
skills:
  - 2
```

Python には、データサイエンティストの作業を楽にする組み込み関数が最初からたくさん用意されています。すでにご存じの関数としては `print()` と `type()` があります。ほかにも、データ型を切り替える `str()`、`int()`、`bool()`、`float()` といった関数があります。詳しくは[こちら](https://docs.python.org/3/library/functions.html)をご覧ください。これらも組み込み関数です。

関数の呼び出しは簡単です。`3.0` の型を取得し、その出力を新しい変数 `result` に保存するには、次のように書きます。

```
result = type(3.0)
```

`@instructions`
- `print()` と `type()` を組み合わせて、`var1` の型を表示してください。
- `len()` を使って、リスト `var1` の[長さ](https://docs.python.org/3/library/functions.html#len)を取得します。`print()` で包んで、そのまま表示してください。
- `int()` を使って、`var2` を[整数](https://docs.python.org/3/library/functions.html#int)に変換します。出力を `out2` として保存してください。

`@hint`
- `type()` 関数は次のように呼び出します: `type(var1)`。
- これまで通りに `print()` を呼び出します。表示したい変数を丸括弧の中に入れるだけです。
- `int(x)` は `x` を整数に変換します。

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
msg = "定義済みの変数を変更または削除する必要はありません。"
Ex().check_object("var1", missing_msg=msg).has_equal_value(incorrect_msg=msg)
Ex().check_object("var2", missing_msg=msg).has_equal_value(incorrect_msg=msg)

patt = "__JINJA__:`{{sol_call}}`を使用して`var1`の%sを出力することを確認してください。"
Ex().has_printout(0, not_printed_msg = patt % '型')
Ex().has_printout(1, not_printed_msg = patt % '長さ')

int_miss_msg = "`int()`を使用して`var2`を整数にしましたか？"
int_incorr_msg = "`var2`を`int()`に渡しましたか？"
Ex().check_correct(
  check_object("out2").has_equal_value(incorrect_msg="`int()`を正しく呼び出しました。次に、この呼び出しの結果を`out2`に割り当ててください。"),
  check_function("int", missing_msg=int_miss_msg).has_equal_value(incorrect_msg=int_incorr_msg)
)
success_msg("素晴らしい仕事です！`len()`関数は非常に便利です。文字列にも使用して文字数を数えることができます！")
```

---

## Help!

```yaml
type: MultipleChoiceExercise
key: 679b852978
lang: python
xp: 50
skills:
  - 2
```

Pythonの関数名は分かっていても、使い方を確認したいときがありますよね。そんなときは、別の関数で関数の情報を参照します。それが `help()` です。IPython では、関数名の前に `?` を付ける方法も使えます。

たとえば `max()` のヘルプを表示するには、次のどちらかを実行します。

```
help(max)
?max
```

IPython シェルで `pow()` の[ドキュメント](https://docs.python.org/3/library/functions.html#pow)を開いてみましょう。`?pow` または `help(pow)` と入力し、**Enter** を押してください。

次の記述のうち、正しいものはどれですか？

`@possible_answers`
- `pow()` は `base`、`exp`、`mod` の3つの引数を取ります。`mod` を省略するとエラーになります。
- `pow()` は必須の3引数 `base`、`exp`、`None` を取ります。
- `pow()` は `base` と `exp` が必須で、`mod` は省略可能です。
- `pow()` は `exp` と `mod` の2引数を取ります。`exp` がないとエラーになります。

`@hint`
- 省略可能な引数は、`=` でデフォルト値が設定されています。指定しない場合は、そのデフォルト値が使われます。

`@pre_exercise_code`
```{python}

```

`@sct`
```{python}
msg1 = "違います。`mod` にはデフォルト値があり、値を指定しない場合はその値が使用されます。"
msg2 = "不正解です。`mod` 引数のデフォルト値は `None` です。"
msg3 = "完璧です！`help()` を使用することで、関数の動作を理解し、その可能性を最大限に引き出すことができます！"
msg4 = "不正解です。`pow()` は3つの引数を取り、そのうちの1つにはデフォルト値があります。"
Ex().has_chosen(3, [msg1, msg2, msg3, msg4])
```

---

## 複数の引数

```yaml
type: NormalExercise
key: e30486d7c1
lang: python
xp: 100
skills:
  - 2
```

前の演習では、`help()` でドキュメントを表示してオプション引数を確認しました。ここではそれを応用して、`sorted()` 関数の動作を変えてみます。

IPython シェルで `help(sorted)` と入力し、`sorted()` の[ドキュメント](https://docs.python.org/3/library/functions.html#sorted)を確認してください。

`sorted()` は `iterable`、`key`、`reverse` の3つの引数を受け取ります。この演習では、`key` ではなく、`iterable` と `reverse` だけを指定します。

2 つのリストはすでに用意されています。

それらを結合して、降順に並べ替えられますか？

`@instructions`
- `+` を使って、`first` と `second` の中身を結合し、新しいリスト `full` を作成します。
- `full` に対して `sorted()` を呼び出し、`reverse` 引数を `True` に指定します。並べ替えたリストを `full_sorted` として保存します。
- 最後に、`full_sorted` を出力します。

`@hint`
- `first` と `second` を数値のように足し合わせ、結果を `full` に代入します。
- `sorted()` を、2 つの入力 `full` と `reverse=True` で使います。
- 変数を出力するには、`print()` を使います。

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
msg = "既存の変数 `first` と `second` を変更または削除する必要はありません。"
Ex().multi(
  check_object("first", missing_msg=msg).has_equal_value(incorrect_msg=msg),
  check_object("second", missing_msg=msg).has_equal_value(incorrect_msg=msg)
)
Ex().check_correct(
  check_object("full_sorted").has_equal_value(incorrect_msg="`sorted()` を呼び出した結果を `full_sorted` に代入していることを確認してください。"),
  check_function("sorted").multi(
    check_args(0).has_equal_value(),
    check_args('reverse').has_equal_value()
  )
)

success_msg("素晴らしいです！Pythonメソッドに関するビデオに進みましょう。")
```

---

## メソッド

```yaml
type: VideoExercise
key: 2b66cb66b1
xp: 50
```

`@projector_key`
8e387776f3a264a745128b68aa8d8f83

---

## 文字列メソッド

```yaml
type: NormalExercise
key: 4039302ee0
lang: python
xp: 100
skills:
  - 2
```

文字列にはたくさんのメソッドがあります。いくつかを試せるよう、指示に沿って進めてください。もっと詳しく知りたい場合は、IPython シェルで `help(str)` と入力すれば確認できます。

練習用に、文字列 `place` はすでに用意されています。

`@instructions`
- `place` に対して `.upper()` [メソッド](https://docs.python.org/3/library/stdtypes.html#str.upper) を使い、結果を `place_up` に代入します。直前の動画で学んだメソッド呼び出しの構文を使ってください。
- `place` と `place_up` を出力します。両方とも変化しましたか？
- 変数 `place` に含まれる o の数を、`place` に対して `.count()` を呼び出し、メソッドの入力として文字 `'o'` を渡して数え、出力してください。ここで対象なのは変数 `place` であり、単語の `"place"` ではありません！

`@hint`
- `.upper()` メソッドは、追加の入力なしで `place` に対して呼び出せます。
- 変数 `x` を出力するには、`print(x)` と書きます。
- `place.count(____)` の呼び出しは、結果を表示できるように必ず `print()` で包んでください。

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
msg = "定義済みの変数を変更または削除する必要はありません。"
Ex().check_object("place", missing_msg=msg).has_equal_value(incorrect_msg=msg)

patt = "`%s`を出力するのを忘れないでください。"
Ex().has_printout(0, not_printed_msg=patt % "place")
Ex().check_correct(
    has_printout(1, not_printed_msg=patt % "place_up"),
    check_correct(
        check_object("place_up").has_equal_value(incorrect_msg="`place.upper()`の結果を`place_up`に代入してください。"),
        check_function("place.upper", signature=False)
    )
)    

# check count of place
Ex().check_correct(
  has_printout(2, not_printed_msg = "`place`の中の'o'の数を正しく計算しました。次に、`place.count('o')`の呼び出しを`print()`関数でラップして結果を出力してください。"),
  check_function("place.count", signature=False).check_args(0).has_equal_value()
)

success_msg("素晴らしいです！出力から、`upper()`メソッドが呼び出されたオブジェクトを変更しないことに注意してください。次の演習では、リストに対して異なる動作をします！")
```

---

## リストのメソッド

```yaml
type: NormalExercise
key: 0dbe8ed695
lang: python
xp: 100
skills:
  - 2
```

メソッドを持っているのは文字列だけではありません。リスト、float、int、bool などの型にも便利なメソッドがたくさん用意されています。この演習では次のメソッドを試します。

- `.index()`：引数に一致する最初の要素のインデックスを取得します
- `.count()`：ある要素がリスト内に何回出現するかを取得します

家の各部分の面積を表すリスト `areas` を使って進めます。

`@instructions`
- `areas` の中で `20.0` に等しい要素のインデックスを、`.index()` メソッドで取得し、表示してください。
- `.count()` を `areas` に対して呼び出し、`9.50` がリスト内に何回現れるかを調べてください。こちらも数値をそのまま表示します。

`@hint`
- インデックスを表示するには、`areas.index(___)` の呼び出しを `print()` に渡して出力します。
- リスト内で要素 `x` が出現する回数を表示するには、`areas.count(___)` の呼び出しを `print()` に渡して出力します。

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
predef_msg = "定義済みのリスト `areas` を変更または削除する必要はありません。"

Ex().check_object("areas", missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg)

Ex().check_function("print", index=0).check_args(0).check_function('areas.index', signature=False).check_args(0).has_equal_value()

Ex().check_function("print", index=1).check_args(0).check_function('areas.count', signature=False).has_equal_value()

success_msg("素晴らしいです！これらは、呼び出されたリストを変更しなかった `list` メソッドの例です。")
```

---

## リストのメソッド (2)

```yaml
type: NormalExercise
key: 1fbeab82d0
lang: python
xp: 100
skills:
  - 2
```

ほとんどのリストメソッドは、呼び出されたリスト自体を変更します。例としては次のものがあります。

- `.append()` は、呼び出し元のリストに要素を追加します。
- `.remove()` は、入力に一致する最初の要素をリストから[削除](https://docs.python.org/3/library/stdtypes.html#typesseq-mutable)します。
- `.reverse()` は、呼び出し元のリスト内の要素の順序を[反転](https://docs.python.org/3/library/stdtypes.html#typesseq-mutable)します。

ここでは、家の各部分の面積を表すリスト `areas` を使って作業します。

`@instructions`
- `.append()` を2回使って、プールハウスとガレージの面積 `24.5` と `15.45` をこの順番で再度追加します。
- `areas` を出力します。
- `.reverse()` メソッドを使って、`areas` の要素の順序を逆にします。
- もう一度 `areas` を出力します。

`@hint`
- 最初の指示では、`areas.append(___)` を2回使います。
- 変数 `x` を出力するには、単に `print(x)` と書きます。
- `.reverse()` メソッドに追加の入力は不要です。ドット記法と空のかっこだけを使います: `.reverse()`。
- 変数 `x` を出力するには、単に `print(x)` と書きます。

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

success_msg("素晴らしいです！")
```

---

## パッケージ

```yaml
type: VideoExercise
key: ab96a17c5e
xp: 50
```

`@projector_key`
cedcfb34350be8545599768f96695cdd

---

## パッケージをインポートする

```yaml
type: NormalExercise
key: 7432a6376f
lang: python
xp: 100
skills:
  - 2
```

円の円周と面積を計算したいとします。式は次のとおりです。

$$C = 2 \pi r$$
$$A = \pi r^2 $$

`pi` の数値を直接入力するのではなく、数値が入っている `math` パッケージを使えます。

参考までに、`**` は累乗を表す演算子です。たとえば `3**4` は `3` の `4` 乗で、結果は `81` になります。

`@instructions`
- `math` パッケージをインポートしてください。
- `math.pi` を使って円の円周を計算し、`C` に代入してください。
- `math.pi` を使って円の面積を計算し、`A` に代入してください。

`@hint`
- `import math` と書き、`pi` は `math.pi` として参照できます。
- 課題文の式を使って円周 `C` を求めます。`*` を使いましょう。
- 課題文の式を使って面積 `A` を求めます。`*` と `**` を使いましょう。

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
patt = "あなたの`%s`の計算は少し正しくありません。`math.pi`を使用することを確認してください。"
Ex().multi(
  has_import('math', same_as=False),
  check_object('C').has_equal_value(incorrect_msg=patt%'C'),
  check_object('A').has_equal_value(incorrect_msg=patt%'A')
)

Ex().multi(
  has_printout(0, not_printed_msg = "__JINJA__:円周を出力するために`{{sol_call}}`をそのままにしておいてください。"),
  has_printout(1, not_printed_msg = "__JINJA__:面積を出力するために`{{sol_call}}`をそのままにしておいてください。")
)

success_msg("素晴らしいです！パッケージからの関数を扱う方法を知っていれば、多くのPythonプログラマーの力があなたの手の届くところにあります！")
```

---

## 選択的インポート

```yaml
type: NormalExercise
key: fe65eff50a
lang: python
xp: 100
skills:
  - 2
```

`import math` のような一般的なインポートでは、`math` パッケージの機能が**すべて**使えるようになります。ただし、パッケージの一部だけを使うと決めた場合は、次のようにより選択的にインポートできます。

```
from math import pi
```

同じことを、今度は `pi` だけを使って試してみましょう。

`@instructions`
- `math` パッケージから選択的インポートを行い、`pi` だけをインポートしてください。
- `pi` を使って円周を計算し、`C` に保存します。
- `pi` を使って面積を計算し、`A` に保存します。

`@hint`
- 選択的インポートには `from math import pi` を使います。
- これで、`pi` をそのまま使えるようになります！

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
patt = "あなたの`%s`の計算は完全には正しくありません。`pi`のみを使用するようにしてください。"

Ex().has_import("math.pi", not_imported_msg = "`math`パッケージから`pi`をインポートすることを確認してください。`from ___ import ___`の表記を使用する必要があります。",)

Ex().multi(
  check_object('C').has_equal_value(incorrect_msg=patt%'C'),
  check_object('A').has_equal_value(incorrect_msg=patt%'A')
)

Ex().multi(
  has_printout(0, not_printed_msg = "__JINJA__:`{{sol_call}}`をそのままにして、円周を出力してください。"),
  has_printout(1, not_printed_msg = "__JINJA__:`{{sol_call}}`をそのままにして、面積を出力してください。")
)

success_msg("素晴らしいです！次の演習に進みましょう。")
```

---

## インポートのいろいろな方法

```yaml
type: MultipleChoiceExercise
key: f1b2675a2a
lang: python
xp: 50
skills:
  - 2
```

Python では、パッケージやモジュールをインポートする方法がいくつかあります。どのようにインポートするかによって、使う Python コードも変わります。

たとえば、`scipy` パッケージの `linalg` サブパッケージにある [関数](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.inv.html) `inv()` を使いたいとします。この関数を次のように使えるようにしたいとします。

```
my_inv([[1,2], [3,4]])
```

上のコードをエラーなく実行するには、どの `import` 文が必要でしょうか。

`@possible_answers`
- `import scipy`
- `import scipy.linalg`
- `from scipy.linalg import my_inv`
- `from scipy.linalg import inv as my_inv`

`@hint`
- IPython シェルでそれぞれの import 文を試して、`my_inv([[1, 2], [3, 4]])` の行がエラーなく実行できるものを確認してみてください。入力したコードは **enter** を押すと実行されます。

`@pre_exercise_code`
```{python}

```

`@sct`
```{python}
msg1 = msg2 = msg3 = "不正解です。もう一度試してください。IPythonシェルで異なるインポート文を試し、どのインポート文が`my_inv([[1, 2], [3, 4]])`をエラーなく実行できるか確認してください。"
msg4 = "正解です！`as`という単語を使うことで、インポートする関数にローカル名を付けることができます。`inv()`は`my_inv()`として利用可能になりました。"
Ex().has_chosen(4, [msg1, msg2, msg3, msg4])
```

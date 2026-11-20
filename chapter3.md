---
title_meta: 第 3 章
title: 関数とパッケージ
description: >-
  関数、メソッド、パッケージを使って、優れた Python
  開発者たちが書いたコードを効率的に活用する方法を学びます。難しい問題を解くときに、自分で書くコードをできるだけ少なくすることを目指します。
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

## よく使う関数

```yaml
type: NormalExercise
key: c422ee929b
lang: python
xp: 100
skills:
  - 2
```

Python には標準で、データサイエンティストとしての作業を楽にしてくれる組み込み関数がたくさん用意されています。すでに `print()` と `type()` の2つはご存知ですね。データ型を変換する `str()`、`int()`、`bool()`、`float()` のような関数もあります。詳しくは[こちら](https://docs.python.org/3/library/functions.html)で確認できます。これらも組み込み関数です。

関数を呼び出すのは簡単です。 `3.0` の型を取得し、出力を新しい変数 `result` に保存するには、次のようにします。

```
result = type(3.0)
```

`@instructions`
- `print()` と `type()` を組み合わせて使い、`var1` の型を出力します。
- `len()` を使って、リスト`var1`の[ 長さ](https://docs.python.org/3/library/functions.html#len)を取得します。`print()` で囲んで、そのまま出力します。
- `int()` を使って、`var2` を[整数](https://docs.python.org/3/library/functions.html#int)に変換します。出力を `out2` に格納します。

`@hint`
- `type()` 関数はこのように呼び出します：`type(var1)`
- これまで何度も使ってきたように、`print()` を呼び出します。出力したい変数を括弧の中に入れるだけです。
- `int(x)` は、`x` を整数に変換します。

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

## ヘルプ！

```yaml
type: MultipleChoiceExercise
key: 679b852978
lang: python
xp: 50
skills:
  - 2
```

Python 関数の名前はすでに知っていても、その使い方を確認する必要があるかもしれません。皮肉なことに、関数についての情報は、別の関数である `help()` を使って確認します。特に IPython では、関数名の前に `?` を付けることもできます。

たとえば、`max()` 関数のヘルプを確認するには、次のいずれかを呼び出します。

```
help(max)
?max
```

IPython Shell を使って `pow()` の[ ドキュメント ] (https://docs.python.org/3/library/functions.html#pow)を開いてください。`?pow` または `help(pow)` と入力し、**Enter** キーを押します。

次の文のうち、正しいものはどれですか？

`@possible_answers`
- `pow()` は3つの引数 `base`、`exp`、`mod` を取ります。`mod` がない場合、この関数はエラーを返します。
- `pow()` は3つの必須引数 `base`、`exp`、`None` を取ります。
- `pow()` には `base` と `exp` 引数が必要で、`mod` は省略可能です。
- `pow()` は2つの引数 `exp` と `mod` を取ります。`exp` がない場合、エラーになります。

`@hint`
- 省略可能な引数には、`=` を使ってデフォルト値が設定されており、その引数が指定されていない場合、関数はその値を使います。

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

前の演習では、`help()` でドキュメントを確認して、省略可能な引数を見つけました。今度はこれを応用し、`sorted()` 関数の動作を変更します。

IPython Shell で `help(sorted)` と入力して `sorted()` の [ ドキュメント ] (https://docs.python.org/3/library/functions.html#sorted)を確認してみましょう。

`sorted()` は `iterable`、`key`、`reverse` という3つの引数を取ることがわかります。この演習では、`iterable` と `reverse` だけを指定し、`key` は指定しません。

2つのリストが用意されています。

これらを結合して、降順に並べ替えることはできますか？

`@instructions`
- `+` を使って `first` と `second` の中身を新しいリスト `full` に結合します。
- `sorted()` を `full` に対して呼び出し、`reverse` 引数に `True` を指定します。並べ替えたリストを `full_sorted` として保存します。
- 最後に `full_sorted` を出力します。

`@hint`
- `first` と `second` を2つの数値のように足し合わせ、`full` に代入します。
- `sorted()` に2つの入力`full` と `reverse=True`を指定して使います。
- 変数を出力するには `print()` を使います。

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

## 文字列のメソッド

```yaml
type: NormalExercise
key: 4039302ee0
lang: python
xp: 100
skills:
  - 2
```

文字列にはさまざまなメソッドがあります。いくつか確認するために、指示にしっかり従ってください。さらに詳しく知りたい場合は、IPython Shell でいつでも `help(str)` と入力できます。

文字列 `place` は操作を試せるようにすでに用意されています。

`@instructions`
- 前の動画で学んだメソッド呼び出しの構文を使って   `place` に `.upper()` [ メソッド ]  (https://docs.python.org/3/library/stdtypes.html#str.upper) を使い、結果を `place_up` に格納します。

- `place` と `place_up` を出力します。両方とも変わりましたか？
- 変数 `place` に含まれる o の数を出力します。`place` に `.count()` を使い、メソッドへの入力として文字 `'o'` を渡します。ここで指しているのは変数 `place` であって、単語 `"place"` ではありません。

`@hint`
- 追加の入力なしで、`place` に `.upper()` メソッドを使うことができます。  
- 変数 `x` を出力するには、`print(x)` と入力します。
- `place.count(____)` の呼び出しを `print()` 関数で囲み、出力されるようにしてください。

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

メソッドを持つ Python の型は文字列だけではありません。リスト、浮動小数点数型、整数型、ブール型にも、便利なメソッドがたくさん用意されています。この演習では、次のメソッドを確認しましょう。

- `.index()` ：入力と一致するリスト内の最初の要素のインデックスを取得します。
- `.count()` ：リスト内で要素が現れる回数を取得します。

家のさまざまな部分の面積が入ったリスト `areas` を使いましょう。

`@instructions`
- `.index()` メソッドを使って、`areas` の中で `20.0` に等しい要素のインデックスを取得し、出力してください。
- `areas` に対して `.count()` を呼び出し、`9.50` がリスト内に何回現れるかを調べてください。今回も、その数をそのまま出力してください。

`@hint`
- インデックスを出力するには、`areas.index(___)` を `print()` で囲みます。
- 要素 `x` がリスト内で出現する回数を出力するには、`areas.count(___)` を `print()` で囲みます。

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

## リストのメソッド（2）

```yaml
type: NormalExercise
key: 1fbeab82d0
lang: python
xp: 100
skills:
  - 2
```

リストのメソッドのほとんどは、呼び出されたリスト自体を変更します。主なメソッドを見てみましょう。

- `.append()`：呼び出されたリストに要素を追加します。
- `.remove()`：リスト内で入力に一致する[最初の要素を削除](https://docs.python.org/3/library/stdtypes.html#typesseq-mutable)します。
- `.reverse()`：呼び出されたリストの要素の[順番を逆にします](https://docs.python.org/3/library/stdtypes.html#typesseq-mutable)。

ここでは、家のさまざまな部屋の面積が入ったリスト `areas` を使います。

`@instructions`
- `.append()` を2回使って、プールハウスとガレージの面積（`24.5` と `15.45`）をこの順番で追加してください。
- `areas` を出力してください。
- `.reverse()` メソッドを使って、`areas` の要素の順番を逆にしてください。
- もう一度 `areas` を出力してください。

`@hint`
- 1つ目の指示では、`areas.append(___)` の呼び出しを2回使います。
- 変数 `x` を出力するには、`print(x)` と入力するだけです。
- `.reverse()` メソッドに追加の入力は必要ありません。ドット記法と空の括弧を使って、`.reverse()` と入力します。
- 変数 `x` を出力するには、`print(x)` と入力するだけです。

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

## パッケージのインポート

```yaml
type: NormalExercise
key: 7432a6376f
lang: python
xp: 100
skills:
  - 2
```

円周と円の面積を計算したいとします。これらの公式は次のようになります。

$$C = 2 \pi r$$
$$A = \pi r^2 $$

`pi`の数値を入力する代わりに、その値を含む `math` パッケージを使うことができます。

参考までに、`**` は累乗を表す記号です。たとえば、`3**4`は`3`の`4`乗で、結果は`81`になります。

`@instructions`
- `math` パッケージをインポートしてください。
- `math.pi` を使って円の円周を計算し、その結果を `C` に格納してください。
- `math.pi` を使って円の面積を計算し、その結果を `A` に格納してください。

`@hint`
- `import math` を使うだけで、`math.pi` で `pi` を参照できます。
- 指示にある公式を使って `C` を求めてください。`*`を使います
- 指示にある公式を使って `A` を求めてください。 `*` と `**` を使います。

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

## 特定の関数をインポートする

```yaml
type: NormalExercise
key: fe65eff50a
lang: python
xp: 100
skills:
  - 2
```

`import math` のような一般的なインポートでは、`math` パッケージの**すべて**の機能が使えるようになります。ただし、パッケージの特定の機能だけを使いたい場合は、インポートをより絞り込むこともできます。

```
from math import pi
```

もう一度同じことを試しますが、今回は `pi` だけを使います。

`@instructions`
- `math` パッケージから `pi` 関数だけを選択的にインポートしてください。
- `pi` を使って円周を計算し、`C` に格納してください。
- `pi` を使って円の面積を計算し、`A` に格納してください。

`@hint`
- 特定の値だけをインポートするには、`from math import pi` を使います。
- これで `pi` を単独で使えるようになります。

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

## インポートのさまざまな方法

```yaml
type: MultipleChoiceExercise
key: f1b2675a2a
lang: python
xp: 50
skills:
  - 2
```

Python にパッケージやモジュールをインポートする方法はいくつかあります。どのインポート呼び出しを使うかによって、必要な Python コードも変わります。

`scipy`パッケージの`linalg`サブパッケージにある[ 関数 ] (https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.inv.html) `inv()`を使いたいとしましょう。また、この関数を次のように使えるようにしたいとしましょう。

```
my_inv([[1,2], [3,4]])
```

上記のコードをエラーなく実行するには、どの `import` 文が必要でしょうか？

`@possible_answers`
- `import scipy`
- `import scipy.linalg`
- `from scipy.linalg import my_inv`
- `from scipy.linalg import inv as my_inv`

`@hint`
- IPython Shell でさまざまな import 文を試し、`my_inv([[1, 2], [3, 4]])` がエラーなく実行できるものを確認しましょう。**enter** キーを押してコードを実行します。

`@pre_exercise_code`
```{python}

```

`@sct`
```{python}
msg1 = msg2 = msg3 = "不正解です。もう一度試してください。IPythonシェルで異なるインポート文を試し、どのインポート文が`my_inv([[1, 2], [3, 4]])`をエラーなく実行できるか確認してください。"
msg4 = "正解です！`as`という単語を使うことで、インポートする関数にローカル名を付けることができます。`inv()`は`my_inv()`として利用可能になりました。"
Ex().has_chosen(4, [msg1, msg2, msg3, msg4])
```

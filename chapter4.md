---
title_meta: 第 4 章
title: NumPy
description: >-
  NumPyは、データサイエンスを効率的に実践するための基本的なPythonパッケージです。NumPy配列の強力な機能を使う方法を学び、データの特徴を探っていきましょう。
attachments:
  slides_link: 'https://projector-video-pdf-converter.datacamp.com/735/chapter4.pdf'
lessons:
  - nb_of_exercises: 5
    title: NumPy
  - nb_of_exercises: 5
    title: 2次元NumPy配列
  - nb_of_exercises: 3
    title: NumPy：基本的な統計
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

## はじめての NumPy 配列

```yaml
type: NormalExercise
key: 84cab9d170
lang: python
xp: 100
skills:
  - 2
```

いよいよ野球の世界に飛び込みます。その過程で、データサイエンスに使える強力なパッケージである `numpy` の基礎にも慣れていきます。

Python スクリプトには、何人かの野球選手の身長をセンチメートル単位で表すリスト `baseball` がすでに定義されています。このリストから `numpy` 配列を作成するコードを追加できますか？

`@instructions`
- `numpy` パッケージを `np` としてインポートし、`numpy` を `np` で参照できるようにしてください。
- `np.array()` を使って、`baseball` から `numpy` 配列を作成します。この配列に `np_baseball` という名前を付けてください。
- 正しくできたことを確認するために、`np_baseball` の型を出力してください。

`@hint`
- `import numpy as np` を使えば十分です。これで、`numpy` 関数を使いたいときは、常に `np.fun_name()` という形式で呼び出す必要があります。
- `np.array()` には入力として `baseball` を渡します。この関数呼び出しの結果を `np_baseball` に代入してください。
- 変数 `x` の型を出力するには、`print(type(x))` と入力するだけです。

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
predef_msg = "定義済みの変数を変更または削除する必要はありません。"
Ex().has_import("numpy")
Ex().check_correct(
  check_object("np_baseball"),
  multi(
    check_object("baseball", missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
    check_function("numpy.array").check_args(0).has_equal_ast()
  )
)

Ex().has_printout(0)
success_msg("素晴らしい仕事です！")
```

---

## 野球選手の身長

```yaml
type: NormalExercise
key: e7e25a89ea
lang: python
xp: 100
skills:
  - 2
```

あなたは大の野球ファンです。MLB（メジャーリーグベースボール）に電話して、主力選手の身長に関する追加の統計データを尋ねることにしました。1000人を超える選手のデータを提供してもらい、そのデータは通常のPythonリスト `height_in` として保存されています。身長はインチで表されています。このデータから `numpy` 配列を作成し、単位をメートルに変換できますか？`height_in` はすでに使用可能で、`numpy` パッケージも読み込まれているので、すぐに始められます（出典：stat.ucla.edu）。

`@instructions`
-  `height_in` から `numpy` 配列を作成し、`np_height_in` という名前を付けます。
- `np_height_in` を出力します。
- すべての身長の測定値をインチからメートルに変換するために `np_height_in` に `0.0254` を掛けます。新しい値を新しい配列 `np_height_m` に代入してください。
- `np_height_m` を出力し、結果が正しいか確認しましょう。

`@hint`
- `np.array()` を使い、`height` を渡し、結果を `np_height_in` に保存します。
- 変数 `x` を出力するには、Pythonスクリプトに `print(x)` と入力します。
- `np_height_in` が1つの数値であるかのように計算してください。`np_height_in * conversion_factor` が答えの一部です。
- 変数 `x` を出力するには、Pythonスクリプトに `print(x)` と入力します。

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
  check_object("np_height_m").has_equal_value(incorrect_msg = "`np_height_m` を計算するには、`np_height_in * 0.0254` を使用してください。")
)

success_msg("素晴らしいです！一瞬で、`numpy` は 1000 を超える身長測定値に対して乗算を行います。")
```

---

## NumPy の注意点

```yaml
type: MultipleChoiceExercise
key: 3662ff6637
lang: python
xp: 50
skills:
  - 2
```

`numpy` はベクトル演算を行うのにとても便利です。ただし、その機能を通常の Python リストと比較すると、いくつか異なる点があります。

まず、`numpy` 配列には異なる型の要素を混在させることができません。ブール値と整数のように型を混在させると、`numpy` はそれらを自動的に共通の型に変換します。`True` や `False` などのブール値は、数値と組み合わせると `1` と `0` として扱われるため、配列は最終的に整数の配列になります。

次に、`+`、`-`、`*`、`/` などの一般的な算術演算子は、通常の Python リストと `numpy` 配列では意味が異なります。

次の出力になるコードを選択してください。

```
np.array([True, 1, 2]) + np.array([3, 4, False])
```

`numpy` パッケージはすでに `np` としてインポートされています。それぞれの選択肢を IPython Shell で実行して、出力を確認できます。

`@possible_answers`
- `np.array([True, 1, 2, 3, 4, False])`
- `np.array([4, 3, 0]) + np.array([0, 2, 2])`
- `np.array([1, 1, 2]) + np.array([3, 4, -1])`
- `np.array([0, 1, 2, 3, 4, 5])`

`@hint`
- それぞれのコード片をコピーして IPython Shell に貼り付けてください。**enter** キーを押してコードを実行し、どの出力が`np.array([True, 1, 2]) + np.array([3, 4, False])`によって生成されたものと一致するかを確認してください。

`@pre_exercise_code`
```{python}
import numpy as np
```

`@sct`
```{python}
msg1 = msg3 = msg4 = "不正解です。異なるコードチャンクを試して、どれがターゲットコードチャンクに一致するか確認してください。"
msg2 = "素晴らしいです！`True` は 1 に変換され、`False` は 0 に変換されます。"
Ex().has_chosen(2, [msg1, msg2, msg3, msg4])
```

---

## NumPy 配列のサブセット

```yaml
type: NormalExercise
key: fcb2a9007b
lang: python
xp: 100
skills:
  - 2
```

NumPy配列のサブセット化とは、リストや配列に角括弧記法を使って、一部の要素を抽出することです。この操作は、リストでも配列でもまったく同じように行えます。

この演習では、`height_in` と `weight_lb` という2つのリストがすでに読み込まれています。これらには、MLB選手の身長と体重が通常の Python リストとして含まれています。また、`numpy` 配列として、`np_weight_lb` と `np_height_in` も用意されています。

`@instructions`
- `np_weight_lb` のインデックス 50 の要素を出力してください
- `np_height_in` から、インデックス 100 から 110 までの要素を含むサブ配列を出力してください。

`@hint`
- サブセット化の操作は、必ず `print()` で囲んでください。
- インデックス 100 から 110 までを含む要素を取り出すには、`[100:111]` を使います。

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
msg = "定義済みの変数を変更したり削除したりする必要はありません。"
Ex().multi(
    check_object("np_height_in", missing_msg=msg).has_equal_value(incorrect_msg=msg),
    check_object("np_weight_lb", missing_msg=msg).has_equal_value(incorrect_msg=msg)
)

Ex().has_printout(0)
Ex().has_printout(1)

success_msg("素晴らしいです！新しいことを学ぶ時が来ました: 2D NumPy 配列！")
```

---

## 2次元 NumPy 配列

```yaml
type: VideoExercise
key: 1241efac7a
xp: 50
```

`@projector_key`
ae3238dcc7feb9adecfee0c395fc8dc8

---

## 初めての2次元 NumPy 配列

```yaml
type: NormalExercise
key: 5cb045bb13
lang: python
xp: 100
skills:
  - 2
```

実際の MLB データを扱う前に、小さなリストのリストから2次元 `numpy` 配列を作成してみましょう。

この演習では、`baseball` はリストのリストです。外側のリストには4つの要素が含まれています。各要素は、4人の野球選手の身長と体重をこの順番で含むリストです。`baseball` はすでにスクリプト内にコードとして用意されています。

`@instructions`
- `np.array()` を使って、`baseball`から2次元 `numpy` 配列を作成してＪください。`np_baseball` という名前を付けてください。
- `np_baseball` の型を出力してください。
- `np_baseball` の `shape` 属性を出力してください。`np_baseball.shape` を使います。

`@hint`
- `baseball` はすでにスクリプト内にコードとして用意されています。これに対して `np.array()` を呼び出し、作成された2次元 `numpy` 配列を `np_baseball` に格納してください。
- 2つ目の指示では、`print()` と `type()` を組み合わせて使います。
- `np_baseball.shape` を使うと `np_baseball` の各次元のサイズを確認できます。必ず `print()` で囲んでください。

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
msg = "定義済みの変数を変更または削除する必要はありません。"
Ex().check_object("baseball", missing_msg=msg).has_equal_value(incorrect_msg=msg)
Ex().has_import("numpy", same_as=False)

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

success_msg("素晴らしいです！これで実際のMLBデータを2D `numpy` 配列に変換する準備が整いました！")
```

---

## 2次元形式の野球データ

```yaml
type: NormalExercise
key: 5df25d0b7b
lang: python
xp: 100
skills:
  - 2
```

すべての情報を 2D `numpy` 配列に組み替えた方が扱いやすくなります。

Pythonのリストのリストがあります。このリストのリストでは、各サブリストが1人の野球選手の身長と体重を表しています。このリストの名前は `baseball` で、すでに読み込まれています（ただし、表示はされていません）。

データを2次元配列として格納し、`numpy` の追加機能を使えるようにしましょう。

`@instructions`
- `np.array()` を使って `baseball` から2次元 `numpy` 配列を作成し、`np_baseball` という名前を付けてください。
- `np_baseball` の `shape` 属性を出力してください。

`@hint`
-  `baseball` はすでに Python 環境で使用できます。`numpy` に `np.array()` を渡し、作成された二次元  配列を `np_baseball` に格納してください。
- `np_baseball.shape` を使うと、`np_baseball` の各次元のサイズを確認できます。 必ず `print()` で囲んでください。

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

success_msg("素晴らしいです！多次元 `numpy` 配列の素晴らしい機能を披露する時が来ました！")
```

---

## 2次元NumPy配列のサブセット化

```yaml
type: NormalExercise
key: aeca4977f0
lang: python
xp: 100
skills:
  - 2
```

2次元 `numpy` 配列が規則的な構造になっている場合、つまり各行と各列の値の数が決まっている場合は、複雑なサブセット化も非常に簡単になります。下のコードを見てみましょう。ここでは、リストのリストから要素 `"a"` と `"c"` を取り出しています。

```
# numpy
import numpy as np
np_x = np.array(x)
np_x[:, 0]
```

カンマの前のインデックスは行を指し、カンマの後のインデックスは列を指します。`:` はスライスを表します。この例では、すべての行を含めるようPythonに指示しています。

`@instructions`
- `np_baseball` の50行目を出力してください。
-  `np_baseball` の2列目全体を含む新しい変数 `np_weight_lb` を制作してください。
- `np_baseball` から124人目の野球選手の身長（1列目）を選択し、出力してください。

`@hint`
- 最初の指示では、行インデックス 49 が必要です。具体的には `[49, :]` を使います。
- 2列目全体を選択するには、`[:, 1]` が必要です。
- 最後の指示では `[123, 0]` を使います。忘れずに全体を `print()` で囲ってください。

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
msg = "定義済みの変数を変更または削除する必要はありません。"
Ex().multi(
    has_import("numpy", same_as = False),
    check_object("np_baseball", missing_msg=msg).has_equal_value(incorrect_msg = msg)
)

Ex().has_printout(0)

Ex().check_object('np_weight_lb').has_equal_value(incorrect_msg = "np_weight_lb を定義するには `np_baseball[:,1]` を使用できます。これにより、最初の列全体が選択されます。")

Ex().has_printout(1)

success_msg("順調に進んでいます！")
```

---

## 2次元配列の算術演算

```yaml
type: NormalExercise
key: 1c2378b677
lang: python
xp: 100
skills:
  - 2
```

2次元 `numpy` 配列では、`numpy` 配列と同様に、要素ごとの計算を行うことができます。

`np_baseball` はすでにコードとして用意されています。これは、身長（インチ）、体重（ポンド）、年齢（年）を表す3つの列を持つ2次元 `numpy` 配列です。`baseball` は通常のリストのリストとして使用でき、`updated` は2次元 numpy 配列として使用できます。

`@instructions`
- すべての野球選手について、身長、体重、年齢の変化量のデータが手に入りました。このデータは2次元 `numpy` 配列 `updated` として用意されています。`np_baseball` と `updated` を足し合わせ、結果を出力してください。
- 身長と体重の単位を、それぞれメートルとキログラムに変換したいとします。最初のステップとして、`0.0254`、`0.453592`、`1` の3つの値を含む `numpy` 配列を作成してください。この配列に `conversion` という名前を付けてください。
- `np_baseball` に `conversion` を掛け合わせ、結果を出力してください。

`@hint`
- `np_baseball + updated` を使うと、2つの `numpy` 配列を要素ごとに足し合わせることができます。
- `numpy` を使って `np.array()` 配列を作成してください。入力は、3つの要素を持つ通常の Python リストです。
- `np_baseball * conversion` はそのまま使えますので確認しましょう。必ず `print()` 呼び出しで囲んでください。

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

msg = "事前定義された変数を変更または削除する必要はありません。"
Ex().check_object("np_baseball", missing_msg=msg).has_equal_value(incorrect_msg=msg)

Ex().has_printout(0)

Ex().check_correct(
    has_printout(1),
    check_correct(
        check_object('conversion').has_equal_value(),
        check_function('numpy.array', index=1).check_args(0).has_equal_value()
    )    
)

success_msg("素晴らしい仕事です！ごく少ないコードで、`numpy` データ構造内のすべての値を非常に特定の方法で変更できることに注目してください。これは、データサイエンティストとしての将来に非常に役立ちます！")
```

---

## NumPy: 基本統計

```yaml
type: VideoExercise
key: 287995e488
xp: 50
```

`@projector_key`
34495ba457d74296794d2a122c9b6e19

---

## 平均値と中央値

```yaml
type: NormalExercise
key: 509c588eb6
lang: python
xp: 100
skills:
  - 2
```

`numpy` 関数を使って、データの特徴をよりよく把握する方法がわかりました。

野球データは、3つの列（身長、体重、年齢）と1015行を持つ2次元 `numpy` 配列として用意されています。この `numpy` 配列の名前は `np_baseball` です。ただし、データを再構成したあと、一部の身長の値が異常に高いことに気づきます。指示に従って、いわゆる外れ値を扱う場合に、どの要約統計量が最も適しているかを確認しましょう。`np_baseball` は利用できます。

`@instructions`
- `np_baseball` の1列目と同じ値を持つ `numpy` 配列 `np_height_in` を作成してください。
- `np_height_in` の平均値を出力してください。
- `np_height_in` の中央値を出力してください。

`@hint`
- 2次元 `numpy` 配列から要素を取り出します。`[:,0]` が解答の一部になります。。
- `numpy` が `np` としてインポートされる場合、`np.mean()` を使ってNumPy配列の平均値を求めることができます。忘れずに `print()` 呼び出しで囲んでください。
- 最後の指示では、`np.median()` を使います。

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

Ex().check_object("np_height_in").has_equal_value(incorrect_msg = "最初の列を選択するには、`np_baseball[:,0]` を使用できます。"),

Ex().check_correct(
    has_printout(0),
    check_function('numpy.mean').has_equal_value()
)

Ex().check_correct(
    has_printout(1),
    check_function('numpy.median').has_equal_value()
)

success_msg("平均身長が1586インチとは、ちょっとおかしいと思いませんか？しかし、中央値は外れ値の影響を受けていないようです：74インチは理にかなっています。データセット全体の分布を把握するために、中央値と平均値の両方を確認することは常に良い考えです。")
```

---

## 野球データを探索する

```yaml
type: NormalExercise
key: '4409948807'
lang: python
xp: 100
skills:
  - 2
```

平均値と中央値の差が大きいため、MLBに問い合わせることにしました。MLBはエラーを見つけ、修正済みのデータを送り返してくれます。このデータも再び、3つの列を持つ2次元NumPy配列 `np_baseball` として用意されています。

エディタ内のPythonスクリプトには、さまざまな要約統計量を使って有用なメッセージを出力するコードがすでに含まれており、`numpy` はすでに `np` として読み込まれています。最後まで仕上げてみましょう。`np_baseball` は使用できます。

`@instructions`
- 平均身長を出力するコードはすでに含まれています。身長の中央値を求めるコードを完成させてください。
- `np_baseball` の1列目に `np.std()` を使って、標準偏差 `stddev` を計算してください。
- 背の高い選手ほど体重も重い傾向があるでしょうか？`np.corrcoef()` を使って、`np_baseball` の1列目と2列目の相関を `corr` に格納してください。

`@hint`
- 中央値の計算には `np.median()` を使います。先に正しい列を選択してください。
- `np.std()` で標準偏差を計算するときも、同じ列を選択してください。
- 1列目と2列目を選択するには、`np_baseball[:, 0]` と `np_baseball[:, 1]` を使います。これらが `np.corrcoef()` への入力になります。

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
msg = "定義済みの `avg` 変数を変更または削除しないでください。"
Ex().check_object("avg", missing_msg=msg).has_equal_value(incorrect_msg=msg)

missing = "`np.median()` を使用して中央値を計算しましたか？"
incorrect = "`med` を計算するには、`np_baseball` の最初の列を `numpy.median()` に渡します。`np.mean()` の例がその方法を示しています。"
Ex().check_correct(
  check_object("med").has_equal_value(),
  check_function("numpy.median", index=0, missing_msg=missing).check_args(0).has_equal_value(incorrect_msg=incorrect)
)

missing = "`np.std()` を使用して標準偏差を計算しましたか？"
incorrect = "`stddev` を計算するには、`np_baseball` の最初の列を `numpy.std()` に渡します。`np.mean()` の例がその方法を示しています。"
Ex().check_correct(
  check_object("stddev").has_equal_value(),
  check_function("numpy.std", index=0, missing_msg=missing).check_args(0).has_equal_value(incorrect_msg=incorrect)
)

missing = "`np.corrcoef()` を使用して相関を計算しましたか？"
incorrect1 = "`corr` を計算するには、`np.corrcoef()` の最初の引数は `np_baseball` の最初の列であるべきです。以前と同様に行います。"
incorrect2 = "`corr` を計算するには、`np.corrcoef()` の2番目の引数は `np_baseball` の2番目の列であるべきです。今回は `[:,0]` の代わりに `[:,1]` を使用します。"
Ex().check_correct(
  check_object("corr").has_equal_value(),
  check_function("numpy.corrcoef", index=0, missing_msg=missing).multi(
    check_args(0, missing_msg=incorrect1).has_equal_value(incorrect_msg=incorrect1),
    check_args(1, missing_msg=incorrect2).has_equal_value(incorrect_msg=incorrect2)
  )
)

success_msg("素晴らしい仕事です！しっかりとした基礎を築きました - これからは新しいデータサイエンスのスキルを使って、さらに多くの課題を解決し、影響を与える時です。")
```

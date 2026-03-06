---
title_meta: 第4章
title: NumPy
description: NumPyはデータサイエンスを効率的に実践するための基礎的なPythonパッケージです。NumPy配列の強力なツールを使いこなし、データ探索を始めましょう。
attachments:
  slides_link: 'https://projector-video-pdf-converter.datacamp.com/735/chapter4.pdf'
lessons:
  - nb_of_exercises: 5
    title: NumPy
  - nb_of_exercises: 5
    title: 2次元NumPy配列
  - nb_of_exercises: 3
    title: NumPy：基本統計
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

ここから野球のデータに取り組んでいきます。その中で、データサイエンスで強力なパッケージである `numpy` の基本に慣れていきましょう。

Python スクリプトには、いくつかの野球選手の身長（センチメートル）が入ったリスト `baseball` がすでに定義されています。これを元に `numpy` 配列を作成するコードを追加できますか？

`@instructions`
- `numpy` パッケージを `np` という別名でインポートし、`numpy` を `np` として参照できるようにします。
- `np.array()` を使って、`baseball` から `numpy` 配列を作成します。配列名は `np_baseball` としてください。
- `np_baseball` の型を表示して、正しく作成できたか確認します。

`@hint`
- `import numpy as np` と書けばOKです。これで、`numpy` の関数を使うときは常に `np.fun_name()` と呼び出します。
- `np.array()` の入力には `baseball` を渡します。関数呼び出しの結果を `np_baseball` に代入してください。
- 変数 `x` の型を表示するには、`print(type(x))` と入力します。

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

あなたは大の野球ファンです。MLB（Major League Baseball）に電話して、主力選手の身長に関する統計をもう少し教えてもらうことにしました。千人以上の選手データが渡され、通常の Python リスト `height_in` に保存されています。身長の単位はインチです。これを `numpy` 配列にし、単位をメートルに変換できますか？

`height_in` はすでに利用可能で、`numpy` パッケージも読み込まれているので、すぐに始められます（出典: stat.ucla.edu）。

`@instructions`
- `height_in` から `numpy` 配列を作成し、新しい配列を `np_height_in` と名付けます。
- `np_height_in` を表示します。
- すべての身長をインチからメートルに変換するため、`np_height_in` に `0.0254` を掛けます。新しい値は新しい配列 `np_height_m` に保存します。
- `np_height_m` を表示し、出力が妥当か確認します。

`@hint`
- `np.array()` に `height` を渡して使います。結果は `np_height_in` に保存してください。
- 変数 `x` を表示するには、Python スクリプトで `print(x)` と入力します。
- `np_height_in` は単一の数のように計算できます。回答の一部は `np_height_in * conversion_factor` です。
- 変数 `x` を表示するには、Python スクリプトで `print(x)` と入力します。

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

## NumPy の副作用

```yaml
type: MultipleChoiceExercise
key: 3662ff6637
lang: python
xp: 50
skills:
  - 2
```

`numpy` はベクトル演算に最適です。ただし、通常の Python のリストと比べると、いくつか異なる点があります。

まず、`numpy` の配列は異なる型の要素を含めることができません。ブール値と整数のように型を混在させると、`numpy` は自動的に共通の型に変換します。`True` や `False` は数値と組み合わせるとそれぞれ `1` と `0` として扱われるため、結果の配列は整数になります。

次に、`+`、`-`、`*`、`/` といった典型的な算術演算子は、通常の Python リストと `numpy` 配列とで意味が異なります。

次の出力になるコードを選んでください。

```
np.array([True, 1, 2]) + np.array([3, 4, False])
```

`numpy` パッケージはすでに `np` としてインポートされています。各選択肢を IPython シェルで実行し、出力を確認してもかまいません。

`@possible_answers`
- `np.array([True, 1, 2, 3, 4, False])`
- `np.array([4, 3, 0]) + np.array([0, 2, 2])`
- `np.array([1, 1, 2]) + np.array([3, 4, -1])`
- `np.array([0, 1, 2, 3, 4, 5])`

`@hint`
- それぞれのコード片をIPythonシェルにコピー＆ペーストし、**enter** を押してコードを実行してください。`np.array([True, 1, 2]) + np.array([3, 4, False])` が生成する出力と一致するものを確認しましょう。

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

## NumPy配列の部分抽出

```yaml
type: NormalExercise
key: fcb2a9007b
lang: python
xp: 100
skills:
  - 2
```

部分抽出（リストや配列に対して角かっこ表記を使う操作）は、リストでも配列でもまったく同じように動作します。

この演習では、すでに2つのリスト `height_in` と `weight_lb` がバックグラウンドで読み込まれています。これらはMLB選手の身長と体重を通常のリストとして保持しています。さらに、2つの `numpy` 配列である `np_weight_lb` と `np_height_in` も用意されています。

`@instructions`
- インデックス50の要素を表示するように、`np_weight_lb` を部分抽出して `print()` で出力してください。
- `np_height_in` から、インデックス100からインデックス110を**含めて**持つサブ配列を `print()` で出力してください。

`@hint`
- 部分抽出の操作には、必ず `print()` を付けて表示するようにしてください。
- インデックス100から、インデックス110を**含めて**取り出すには、`[100:111]` を使います。

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

## 2次元NumPy配列

```yaml
type: VideoExercise
key: 1241efac7a
xp: 50
```

`@projector_key`
ae3238dcc7feb9adecfee0c395fc8dc8

---

## はじめての2次元NumPy配列

```yaml
type: NormalExercise
key: 5cb045bb13
lang: python
xp: 100
skills:
  - 2
```

実際のMLBデータに取り組む前に、小さな入れ子リストから2次元の `numpy` 配列を作ってみましょう。

この演習では、`baseball` はリストのリストです。外側のリストには4つの要素があり、それぞれの要素は4人の野球選手について、身長と体重をこの順番で格納したリストになっています。`baseball` はスクリプト内にすでに用意されています。

`@instructions`
- `np.array()` を使って、`baseball` から2次元の `numpy` 配列を作成し、`np_baseball` という名前を付けてください。
- `np_baseball` の型を出力してください。
- `np_baseball` の `shape` 属性を出力してください。`np_baseball.shape` を使います。

`@hint`
- スクリプトにはすでに `baseball` が用意されています。これに対して `np.array()` を呼び出し、得られた2次元の `numpy` 配列を `np_baseball` に代入してください。
- 2つ目の指示では、`type()` と組み合わせて `print()` を使いましょう。
- `np_baseball.shape` で `np_baseball` の次元が得られます。これを `print()` で出力するのを忘れないでください。

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

## 2 次元形式の野球データ

```yaml
type: NormalExercise
key: 5df25d0b7b
lang: python
xp: 100
skills:
  - 2
```

この情報はすべて、2 次元の `numpy` 配列に再構成したほうが理にかなっていると気づきます。

Python の「リストのリスト」が用意されています。各サブリストは、1 人の野球選手の身長と体重を表しています。このリストの名前は `baseball` で、すでに読み込まれています（表示はされません）。

`numpy` の追加機能を活用できるよう、データを 2 次元配列として保存してください。

`@instructions`
- `np.array()` を使って、`baseball` から 2 次元の `numpy` 配列を作成し、`np_baseball` という名前で保存してください。
- `np_baseball` の `shape` 属性を出力してください。

`@hint`
- `baseball` はすでに Python 環境に読み込まれています。これに対して `np.array()` を呼び出し、その結果得られる 2 次元の `numpy` 配列を `np_baseball` に保存してください。
- `np_baseball.shape` で `np_baseball` の次元を取得できます。必ず `print()` で包んで表示してください。

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

## 2 次元 NumPy 配列の部分抽出

```yaml
type: NormalExercise
key: aeca4977f0
lang: python
xp: 100
skills:
  - 2
```

2 次元の `numpy` 配列が規則的な構造（各行・各列の要素数が固定）を持っていれば、複雑に見える部分抽出もとても簡単になります。以下のコードでは、リストのリストから要素 `"a"` と `"c"` を取り出す例を見てみましょう。

```
# numpy
import numpy as np
np_x = np.array(x)
np_x[:, 0]
```

カンマの前のインデックスは行、カンマの後のインデックスは列を指します。`:` はスライスを表し、この例では「すべての行を含める」という意味になります。

`@instructions`
- `np_baseball` の 50 行目を出力します。
- `np_baseball` の 2 列目全体を含む新しい変数 `np_weight_lb` を作成します。
- `np_baseball` の 124 人目の野球選手の身長（1 列目）を選択し、出力します。

`@hint`
- 最初の指示では、行インデックス 49 が必要です！具体的には `[49, :]` を使います。
- 2 列目全体を選ぶには、`[:, 1]` を使います。
- 最後の指示では `[123, 0]` を使います。全体を `print()` で囲むのを忘れないでください。

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

## 2D の演算

```yaml
type: NormalExercise
key: 1c2378b677
lang: python
xp: 100
skills:
  - 2
```

2D の `numpy` 配列は、`numpy` 配列と同様に要素ごとの計算を実行できます。

`np_baseball` はすでに用意されています。再び 2D の `numpy` 配列で、3 列はそれぞれ身長（インチ）、体重（ポンド）、年齢（年）を表します。`baseball` は通常のリストのリストとして、`updated` は 2D の numpy 配列として利用できます。

`@instructions`
- 野球選手全員の身長・体重・年齢の変化を入手できました。これは 2D の `numpy` 配列 `updated` として利用できます。`np_baseball` と `updated` を加算し、結果を出力してください。
- 身長と体重の単位をメートル法（それぞれメートルとキログラム）に変換したいとします。最初のステップとして、3 つの値 `0.0254`、`0.453592`、`1` をもつ `numpy` 配列を作成し、`conversion` という名前を付けてください。
- `np_baseball` に `conversion` を掛け算し、結果を出力してください。

`@hint`
- `np_baseball + updated` は、2 つの `numpy` 配列の要素ごとの加算を行います。
- `np.array()` で `numpy` 配列を作成します。入力は 3 要素の通常の Python リストです。
- 追加の作業は不要で、`np_baseball * conversion` はそのまま動作します。ぜひ試してみてください！`print()` で結果を表示しましょう。

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

## NumPy：基本統計

```yaml
type: VideoExercise
key: 287995e488
xp: 50
```

`@projector_key`
34495ba457d74296794d2a122c9b6e19

---

## 平均と中央値

```yaml
type: NormalExercise
key: 509c588eb6
lang: python
xp: 100
skills:
  - 2
```

`numpy` の関数を使って、データの傾向をつかむ方法を学びました。

ベースボールのデータは、3列（身長、体重、年齢）・1015行の2次元 `numpy` 配列として用意されています。配列名は `np_baseball` です。データを再構成したところ、一部の身長の値が異常に高いことに気づきました。次の指示に従って作業し、いわゆる外れ値（_outliers_）があるときにどの要約統計量が適しているかを確かめてみましょう。`np_baseball` は利用可能です。

`@instructions`
- `np_baseball` の最初の列と等しい `numpy` 配列 `np_height_in` を作成します。
- `np_height_in` の平均を出力します。
- `np_height_in` の中央値を出力します。

`@hint`
- 2次元の `numpy` の抽出を使います。`[:,0]` が解法の一部です。
- `numpy` を `np` としてインポートしている場合、`np.mean()` でNumPy配列の平均を求められます。`print()` を呼ぶのを忘れないでください。
- 最後の指示には `np.median()` を使います。

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

## 野球データを探究する

```yaml
type: NormalExercise
key: '4409948807'
lang: python
xp: 100
skills:
  - 2
```

平均と中央値の差が大きすぎるので、MLB に問い合わせることにしました。MLB はエラーを見つけ、修正済みデータを送り返してくれました。今回も 3 列の 2D NumPy 配列 `np_baseball` として利用できます。

エディタ内の Python スクリプトには、各種の要約統計量とともに説明的なメッセージを印字するコードがすでに含まれており、`numpy` も `np` として読み込まれています。仕上げてもらえますか？`np_baseball` は利用可能です。

`@instructions`
- 平均身長を表示するコードはすでに含まれています。中央値のコードを完成させてください。
- `np_baseball` の最初の列に対して `np.std()` を使い、`stddev` を計算します。
- 体が大きい選手は重い傾向があるでしょうか？`np.corrcoef()` を使い、`np_baseball` の最初と2番目の列の相関を `corr` に保存してください。

`@hint`
- 中央値の計算には `np.median()` を使います。まずは正しい列を選択してください。
- `np.std()` で標準偏差を計算するときも、同じ列を抽出します。
- 最初と2番目の列を選ぶには `np_baseball[:, 0]` と `np_baseball[:, 1]` を使います。これらを `np.corrcoef()` に渡します。

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

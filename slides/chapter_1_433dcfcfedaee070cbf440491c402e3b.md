---
title: Insert title here
key: 433dcfcfedaee070cbf440491c402e3b
video_link:
  mp3: >-
    https://videos.datacamp.com/mp3/translations/course_735/ja-JP/145746f7-8b35-43ee-9e86-8cc4c3e9219f-8df1e215ea440ece7610bcf013d7bac0.mp3
---

## 変数と型

```yaml
type: TitleSlide
key: dc8b62f1c8
```

`@lower_third`
name: Hugo Bowne-Anderson
title: Data Scientist at DataCamp

`@script`
よくできました。おかえりなさい！Pythonを電卓として使えることは、もうよくわかりましたね。ただし、より複雑な計算を行うには、コードを書きながら値を保存しておく必要があります。

---

## 変数

```yaml
type: FullSlide
key: 36ec318b41
```

`@part1`
- 大文字と小文字を区別する、特定の名前

- 変数名を使って値を呼び出す{{1}}

- 1.79 m - 68.7 kg{{2}}

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
そのためには、大文字と小文字が区別される特定の名前を付けて、変数を定義します。このような変数を作成すると、後で変数名を入力するだけで、その値を呼び出すことができます。

身長と体重をメートル法の単位で測定したとします。身長は1.79メートル、体重は68.7キログラムです。これらの値を、'height' と 'weight' という名前の2つの変数に、イコール記号で代入できます。

ここで変数名 'height' を入力すると、Pythonはその変数名を探し、値を取得して表示します。

---

## BMIを計算する

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
次に、BMI（Body Mass Index、体格指数）を計算しましょう。BMIは、体重をキログラム、身長をメートルで表して、次のように計算します。実際の値を使って計算することもできますが、ここで示すように、変数 'height' と 'weight' を使っても同じように計算できます。変数名を入力するたびに、Pythonにその変数を実際の値に置き換えて処理するよう指示していることになります。'weight' は 68.7、'height' は 1.79 に対応しています。

最後に、このバージョンでは、Pythonに計算結果を新しい変数bmiに格納させています。bmiには、先ほど計算した値と同じ値が入っています。

Python では、変数は頻繁に使われます。 変数を使うと、コードの再現性を高めることができます。

---

## 再現性

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
height、weight、bmi の各変数を作成するコードが、このようにスクリプトに含まれているとします。 別の体重で bmi を再計算したい場合は、
---

## 再現性

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
weight 変数の値を変更して、スクリプトを再実行するだけです。 それに応じて bmi も変わります。これは、weight 変数の値も変わったためです。

ここまでは、身長や体重などの数値だけを扱ってきました。

---

## Pythonの型

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
Pythonでは、これらの数値にはすべて特定の型があります。type()関数を使うと、値の型を確認できます。bmiの値の型を確認するには、type()と書き、かっこの中にbmiを入れます。これがfloatであることがわかります。floatは、Pythonで実数を表すための型で、整数部分と小数部分の両方を持つことができる数値を表します。Pythonには整数型もあります。この例のように、整数型はintで表されます。

ただし、データサイエンスに取り組むには、intやfloatだけでは不十分です。

---

## Pythonの型（2）

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
Python には他にもたくさんのデータ型があります。 最も一般的なものは、文字列（string）とブール値（bool）です。

文字列は、Python でテキストを表すための型です。 これらの例のように、文字列はダブルクォーテーションとシングルクォーテーションのどちらでも作成できます。 ここで最後の変数の型を出力すると、s-t-r と表示されます。これは string の略です。

ブール値は、TrueまたはFalseのいずれかになる型です。日常の言葉で言えば、「はい」と「いいえ」のようなものです。ブール値は、たとえばデータをフィルタリングする際など、今後とても役立ちます。

Python のデータ型には、少し特別な特徴があります。

---

## Pythonの型（3）

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

- 異なる型 = 異なる動作！{{3}}

`@script`
2つの整数を足すこちらのコードと、2つの文字列を足すこちらのコードを見てみましょう。

整数の場合は値が合計され、文字列の場合は文字列が連結されました。 プラス演算子は、データ型によって異なる動作をします。 これは一般的な原則です。コードの動作は、扱っている型によって異なります。

この後の演習では、初めて変数を作成し、Python のデータ型をいくつか試してみます。 次の動画では、リストについて詳しく説明します。

---

## 練習しましょう！
```yaml
type: FinalSlide
key: b7fc40db4d
```

`@script`
それでは、さっそくコードを書いてみましょう。次の章では、さらに魅力的なグラフをPythonで作成していきます。

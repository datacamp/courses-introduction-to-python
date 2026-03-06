---
title: Insert title here
key: 433dcfcfedaee070cbf440491c402e3b
video_link:
  mp3: >-
    https://videos.datacamp.com/mp3/translations/course_735/ja-JP/16bc89b7-1696-4e70-8fbd-03a9381f9c6b.mp3
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
お疲れさまです。おかえりなさい！Python がとても優秀な電卓だということは、もうおわかりですね。さらに複雑な計算をしたいときは、コードを書きながら値を「保存」しておくと便利です。

---

## 変数

```yaml
type: FullSlide
key: 36ec318b41
```

`@part1`
- 固有で大文字小文字を区別する名前

- 変数名で値を参照{{1}}

- 1.79 m・68.7 kg{{2}}

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
そのためには、大小文字を区別する特定の名前で変数を定義します。こうして変数を作成（宣言）すると、あとでその変数名を入力するだけで、保存した値を呼び出せます。

たとえば、メートル法で身長と体重を測ったとします。身長は 1.79 メートル、体重は 68.7 キログラムです。これらの値を、height と weight という 2 つの変数に、イコール記号を使って代入できます。

ここで変数名の height を入力すると、

Python はその変数名を探し、値を取り出して表示します。

---

## BMI を計算

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
では、体格指数、つまり BMI を計算してみましょう。BMI は、体重をキログラム、身長をメートルとして次のように計算します。実際の数値で計算してもいいですし、このように height と weight の変数を使ってもかまいません。変数名を入力するたびに、Python はその部分を変数の実際の値に置き換えます。weight は 68.7、height は 1.79 に対応します。

最後に、この例では結果を新しい変数 bmi に保存しています。bmi には、先ほど計算したのと同じ値が入っています。

Python では、変数は常に使われます。コードを再現可能にするうえでとても役立ちます。

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
height、weight、bmi の変数を作るコードが、このようにスクリプトに入っているとします。別の体重で bmi を再計算したくなったら、

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
weight 変数の宣言だけを変更して、スクリプトを再実行すれば大丈夫です。変数 weight の値が変わるので、bmi もそれに応じて更新されます。

ここまでは、身長や体重のような数値だけを扱ってきました。

---

## Python の型

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
Python では、これらの数にはそれぞれ特定の型があります。値の型は type 関数で確認できます。bmi の型を知りたいときは、type の括弧の中に bmi と書くだけです。表示されるのは float で、これは実数、つまり整数部分と小数部分の両方を持てる数を表す Python の型です。整数用の型は int で、この例のように使います。

ただ、データサイエンスを行うには、int や float だけでは足りません。

---

## Python の型 (2)

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
Python には、ほかにもたくさんのデータ型があります。よく使うのは、文字列とブール値です。

文字列は、テキストを表すための Python の型です。ダブルクォートでもシングルクォートでも文字列を作れます。最後の変数の型を表示すると、str、つまり string の略であることがわかります。

ブール値は、True か False のどちらかになる型です。日常の「はい／いいえ」に相当すると考えるとよいでしょう。ブール値は、たとえばデータのフィルタリングなどで非常に役立ちます。

Python のデータ型には、もうひとつ特徴があります。

---

## Python の型 (3)

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

- 型が違うと挙動も違う！{{3}}

`@script`
このコード行では 2 つの整数を足し、こちらのコード行では 2 つの文字列を結合しています。

整数の場合は値が加算され、文字列の場合は文字列同士がつながりました。プラス演算子は、データ型によって振る舞いが異なります。これは一般的な原則で、コードの動作は扱っている型に依存します。

続く演習では、最初の変数を作成し、Python のいくつかのデータ型を試していきます。次の動画ではリストについて詳しくご説明しますので、そこでお会いしましょう。

---

## Passons à la pratique !

```yaml
type: FinalSlide
key: b7fc40db4d
```

`@script`
それでは、実際にコードを書いていきましょう。次の章では、さらに見栄えのよい Python のチャートを作っていきます。お楽しみに。

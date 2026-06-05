---
title: Insert title here
key: d8fcd4c930027fa4e1c3870c7e7e0ff1
video_link:
  mp3: >-
    https://videos.datacamp.com/mp3/translations/course_735/ja-JP/5f99991c-4851-41dd-aa35-71af183827a4-a84d3714a54d856aac2ac3186a7b9820.mp3
---

## こんにちは、Python！
```yaml
type: TitleSlide
key: f743ca8c41
```

`@lower_third`
name: Hugo Bowne-Anderson
title: Data Scientist at DataCamp

`@script`
こんにちは。ヒューゴです。この「Python入門」コースをご案内します。

私はDataCampでデータサイエンティスト兼講師をしています。

---

## 学習の進め方

```yaml
type: FullSlide
key: 30ee08a725
disable_transition: true
```

`@part1`
![DataCampインターフェース](https://assets.datacamp.com/img/translations/ja-JP/q1/production/repositories/288/datasets/729574d2168960686381caefe79baf5978e27d0d/liveexercise.gif)

`@script`
このコースでは、このような動画レッスンやインタラクティブな演習を通じて、データサイエンスのためのPythonを学びます。Pythonの実行環境が用意されているので、そこで試行錯誤しながら、指示に沿った正しいコードを書くことができます。実践を通じて学びながら、すぐに個別のフィードバックを受け取れる仕組みになっています。

---

## Python

```yaml
type: FullSlide
key: 3f23b93572
```

`@part1`
![guido-hba.png](https://assets.datacamp.com/img/translations/ja-JP/production/repositories/288/datasets/fb3e4b8dc114529dafffb37d33f2b2244210d40f/guido-hba.png = 38){{1}}

- 汎用言語：何でも作れる{{2}}

- オープンソース！無料！{{3}}

- Pythonパッケージは、データサイエンスにも使える{{4}}

	- さまざまな用途や分野で活用されている {{5}}

`@script`
Pythonはグイド・ヴァンロッサムによって生み出されました。 こちらは、私とグイドの写真です。 趣味として始まったPythonは、やがて汎用プログラミング言語になりました。現在では、Pythonを使って実にさまざまなソフトウェアを作ることができます。 では、なぜここまで広まったのでしょうか？まず第一に、Pythonはオープンソースです。 無料で利用できます。 次に、Pythonではパッケージをとても簡単に作成できます。パッケージとは、特定の問題を解決するために他の人と共有できるコードのことです。 時が経つにつれて、データサイエンス向けに作られたパッケージがますます増えてきました。 たとえば、会社の売上を見やすく可視化したいとしましょう。そのためのパッケージがあります。センサーの測定値を分析するために、データベースに接続したい場合はどうでしょうか？そのためのパッケージもあります。
Pythonは、ほとんど何でもできることから、よく「プログラミング言語の万能ナイフ」と呼ばれます。
このコースでは、データサイエンスのコーディングスキルを少しずつ身につけていきます。Pythonという言語がどれほど強力なのか、このコースで一緒に見ていきましょう。

---

## IPython Shell

```yaml
type: FullSlide
key: 43a91a7217
```

`@part1`
**Pythonコマンドを実行する**

![ipython_shell.png](https://assets.datacamp.com/img/translations/ja-JP/q1/production/repositories/288/datasets/a9e8440bb8fbd49e4a73e4c36ef1cd677c0dd55f/pyexercise.png = 95)

`@script`
Pythonに興味が湧いてきたところで、さっそく試してみましょう。

---

## IPython Shell

```yaml
type: FullSlide
key: 9c51ee700d
disable_transition: true
```

`@part1`
**Pythonコマンドを実行する**

![ipython_shell_highlighted.png](https://assets.datacamp.com/img/translations/ja-JP/production/repositories/288/datasets/dd43cc0183b15b43a072eb0fbab4caa72dee9250/pyexercise_shell.jpg = 95)

`@script`
まずは、Pythonシェルから始めます。Pythonシェルでは、Pythonコードを入力して、すぐに結果を確認できます。DataCampの演習では、このようにPythonシェルが組み込まれています。まずはシンプルに、Pythonを電卓として使ってみましょう。

---

## IPython Shell

```yaml
type: FullSlide
key: 524e4c20a7
disable_transition: true
```

`@part1`
 

![DataCampのIPythonシェルでの計算](https://assets.datacamp.com/img/translations/ja-JP/q1/production/repositories/288/datasets/cee32b788a62e4b9a1234ccde56ac9ebb49cfa72/shelladdition.gif = 95)

`@script`
4 + 5と入力して、Enterキーを押してみましょう。Pythonは入力された内容を解釈し、計算結果の9を表示します。ここで使っているPythonシェルは、実は標準のPythonシェルではありません。ここではIPythonを使っています。IPythonはInteractive Pythonの略で、通常のPythonを拡張したようなものです。これは後ほど役に立ちます。

IPythonはフェルナンド・ペレスによって作成され、現在はJupyterプロジェクトの一部になっています。 Pythonを対話的に操作するだけでなく、
---

## Pythonスクリプト

```yaml
type: FullSlide
key: 78ef256bc0
```

`@part1`
- テキストファイル - `.py`{{1}}

- Pythonコマンドを並べたもの{{2}}

- IPython Shellに1行ずつ入力するのと似ています{{3}}

![Python script in DataCamp](https://assets.datacamp.com/img/translations/ja-JP/q1/production/repositories/288/datasets/59f196e96536543a4fb8801228019fc4106f3791/pyexercise_script.jpg = 78{{3}})

`@script`
Pythonスクリプトを実行することもできます。Pythonスクリプトとは、拡張子が.pyの単なるテキストファイルです。基本的にはPythonコマンドを並べたもので、シェルに自分で1行ずつコマンドを入力する場合と同じように実行されます。

---

## Pythonスクリプト

```yaml
type: FullSlide
key: 717d124175
disable_transition: true
```

`@part1`
![GIF: スクリプトに 4 + 5 と入力し、Submit Answerをクリックする。 出力は表示されません。](https://assets.datacamp.com/img/translations/ja-JP/production/repositories/288/datasets/2f96e979012e15329cc158d1e0f496aac3539f45/scriptnoprint.gif = 95)

`@script`
先ほどのコマンドを、今度はスクリプトに入れてみましょう。スクリプトはDataCampの画面のこちらにあります。次は、「解答を提出」をクリックしてスクリプトを実行します。このスクリプトをDataCamp上で実行しても、出力ペインには何も表示されません。これは、スクリプトの実行時に出力を表示したい場合、スクリプト内で明示的にprint()を使う必要があるためです。

---

## Pythonスクリプト

```yaml
type: FullSlide
key: c7a9d02fb6
disable_transition: true
code_zoom: 90
```

`@part1`
![python_script_print.gif](https://assets.datacamp.com/img/translations/ja-JP/q1/production/repositories/288/datasets/8b13d046bb54dcb11aa49f0da7363781129d1561/scriptwithprint.gif = 95)

- スクリプトから出力を表示するには`print()`を使います用します

`@script`
先ほどの計算をprint()の中に入れて、スクリプトをもう一度実行してみましょう。今度は、先ほどと同じ出力が表示されました。いいですね！コードを毎回手動で入力し直すのではなく、Pythonスクリプトにまとめておくと、構成を整理しやすくなります。変更したい場合も、すべてを何度も入力し直す必要はありません。スクリプト内で変更を加えて、全体を再実行するだけです。

---

## DataCampインターフェース

```yaml
type: FullSlide
key: 693ba1cd14
```

`@part1`
![DataCampインターフェースのスクリーンショット](https://assets.datacamp.com/img/translations/ja-JP/q1/production/repositories/288/datasets/a9e8440bb8fbd49e4a73e4c36ef1cd677c0dd55f/pyexercise.png)

`@script`
Pythonを操作する方法がいくつかわかったところで、演習に進みましょう。コードを試すときはIPythonシェルを使い、実際の解答を書くときはPythonスクリプトエディタを使いましょう。「解答を提出」をクリックすると、スクリプトが実行され、正しく書けているかチェックされます。

---

## 練習しましょう！
```yaml
type: FinalSlide
key: 7445cd202e
```

`@script`
さっそくコードを書いてみましょう。楽しむことも忘れずに！

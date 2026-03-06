---
title: Insert title here
key: d8fcd4c930027fa4e1c3870c7e7e0ff1
video_link:
  mp3: >-
    https://videos.datacamp.com/mp3/translations/course_735/ja-JP/b304ad18-1073-4c50-b93b-a015c968a8e1.mp3
---

## Python へようこそ！

```yaml
type: TitleSlide
key: f743ca8c41
```

`@lower_third`
name: Hugo Bowne-Anderson
title: Data Scientist at DataCamp

`@script`
こんにちは。ヒューゴと申します。「Python入門（データサイエンス向け）」のホストを務めます。

私はDataCampでデータサイエンティスト兼教育担当をしています。

---

## 学び方

```yaml
type: FullSlide
key: 30ee08a725
disable_transition: true
```

`@part1`
![DataCamp のインターフェース](https://assets.datacamp.com/img/translations/ja-JP/production/repositories/288/datasets/729574d2168960686381caefe79baf5978e27d0d/liveexercise.gif)

`@script`
このコースでは、今ご覧いただいているような動画レッスンと、インタラクティブな演習を通して、データサイエンスのためのPythonを学びます。ご自身専用のPythonセッションが用意され、試行錯誤しながら指示を解くための正しいコードを書いていきます。実際に手を動かしながら学び、作業内容に合わせた即時のフィードバックが得られます。

---

## Python

```yaml
type: FullSlide
key: 3f23b93572
```

`@part1`
![guido-hba.png](https://assets.datacamp.com/img/translations/ja-JP/production/repositories/288/datasets/fb3e4b8dc114529dafffb37d33f2b2244210d40f/guido-hba.png = 38){{1}}

- 汎用: 何でも作れる{{2}}

- オープンソース。無料{{3}}

- データサイエンス向けを含む Python パッケージ{{4}}

	- 多様な用途と分野{{5}}

`@script`
Pythonはグイド・ヴァンロッサムによって考案されました。ここに、私とグイドの写真があります。趣味のプロジェクトとして始まったものが、すぐに汎用のプログラミング言語へと発展し、今ではほとんどあらゆるソフトウェアをPythonで作れるようになりました。なぜそうなったのでしょうか。まず、Pythonはオープンソースで、自由に使えます。次に、特定の問題を解くためのコードを他の人と共有できる「パッケージ」をPythonでは作りやすい点があります。時間の経過とともに、データサイエンスに特化したパッケージがどんどん開発されてきました。たとえば、会社の売上を見栄えよく可視化したいなら、そのためのパッケージがあります。センサーの計測値を分析するためにデータベースへ接続したい場合も、やはりそのためのパッケージがあります。
Pythonは、ほとんど何でもできることから「プログラミング言語のスイスアーミーナイフ」と呼ばれることも多いです。
このコースでは、少しずつ着実にコーディングスキルを積み上げていきます。言語の強力さを実感できるので、ぜひ最後まで続けてみてください。

---

## IPython Shell

```yaml
type: FullSlide
key: 43a91a7217
```

`@part1`
**Python コマンドを実行**

![ipython_shell.png](https://assets.datacamp.com/img/translations/ja-JP/production/repositories/288/datasets/a9e8440bb8fbd49e4a73e4c36ef1cd677c0dd55f/pyexercise.png = 95)

`@script`
Pythonに向けて気持ちの準備ができたところで、さっそく試してみましょう。まずは

---

## IPython Shell

```yaml
type: FullSlide
key: 9c51ee700d
disable_transition: true
```

`@part1`
**Python コマンドを実行**

![ipython_shell_highlighted.png](https://assets.datacamp.com/img/translations/ja-JP/production/repositories/288/datasets/dd43cc0183b15b43a072eb0fbab4caa72dee9250/pyexercise_shell.jpg = 95)

`@script`
Pythonシェルです。ここではPythonコードを入力すると、すぐに結果が表示されます。DataCampの演習画面では、このシェルがここに組み込まれています。まずは手始めに、Pythonを電卓として使ってみましょう。

---

## IPython Shell

```yaml
type: FullSlide
key: 524e4c20a7
disable_transition: true
```

`@part1`
&nbsp;

![DataCamp の IPython Shell での計算](https://assets.datacamp.com/img/translations/ja-JP/production/repositories/288/datasets/cee32b788a62e4b9a1234ccde56ac9ebb49cfa72/shelladdition.gif = 95)

`@script`
4 + 5 と入力して、Enterを押してみます。Pythonが入力を解釈し、計算結果の 9 を表示します。ここで使っているPythonシェルは元々のものではなく、IPythonと呼ばれるものです。Interactive Pythonの略で、標準のPythonを強化したもので、後ほど役に立ちます。

IPythonはフェルナンド・ペレスによって作られ、より広いJupyterエコシステムの一部です。対話的にPythonを扱うだけでなく、いわゆる

---

## Python スクリプト

```yaml
type: FullSlide
key: 78ef256bc0
```

`@part1`
- テキストファイル - `.py`{{1}}

- Python コマンドの一覧{{2}}

- IPython Shell での入力に近い{{3}}

![DataCamp の Python スクリプト](https://assets.datacamp.com/img/translations/ja-JP/production/repositories/288/datasets/59f196e96536543a4fb8801228019fc4106f3791/pyexercise_script.jpg = 78){{3}}

`@script`
Pythonスクリプトを実行することもできます。Pythonスクリプトは拡張子が .py の単なるテキストファイルです。シェルで自分が1行ずつ入力していくのとほぼ同じように、Pythonのコマンドが順に実行されます。

---

## Python スクリプト

```yaml
type: FullSlide
key: 717d124175
disable_transition: true
```

`@part1`
![GIF: スクリプトで 4 + 5 を入力して Submit Answer を押すが、出力は表示されない。](https://assets.datacamp.com/img/translations/ja-JP/production/repositories/288/datasets/2f96e979012e15329cc158d1e0f496aac3539f45/scriptnoprint.gif = 95)

`@script`
それでは先ほどのコマンドを、今度はスクリプトに入れてみましょう。DataCampの画面のこちらにあります。次のステップは、"Submit Answer" をクリックしてスクリプトを実行することです。DataCampの画面でこのスクリプトを実行しても、出力ペインには何も表示されません。スクリプトで実行時に出力を表示したい場合は、printを明示的に使う必要があるためです。

---

## Python スクリプト

```yaml
type: FullSlide
key: c7a9d02fb6
disable_transition: true
code_zoom: 90
```

`@part1`
![python_script_print.gif](https://assets.datacamp.com/img/translations/ja-JP/production/repositories/288/datasets/8b13d046bb54dcb11aa49f0da7363781129d1561/scriptwithprint.gif = 95)

- `print()` を使うとスクリプトから出力できます

`@script`
先ほどの計算をprintで包んで、スクリプトを再実行してみましょう。今度は先ほどと同じ出力が表示されました。良いですね。コードを毎回対話的に打ち直すのではなく、Pythonスクリプトにまとめておくと、構造を保てますし、変更したいときも同じ部分を繰り返し入力せずに済みます。スクリプト内を修正して、全体をもう一度実行するだけです。

---

## DataCamp のインターフェース

```yaml
type: FullSlide
key: 693ba1cd14
```

`@part1`
![DataCamp インターフェースのスクリーンショット](https://assets.datacamp.com/img/translations/ja-JP/production/repositories/288/datasets/a9e8440bb8fbd49e4a73e4c36ef1cd677c0dd55f/pyexercise.png)

`@script`
Pythonの使い方を大まかにつかめたところで、演習に進みましょう。試行にはIPythonシェルを使い、実際の解答コードはPythonスクリプトエディタに書いてください。"Submit Answer" をクリックすると、スクリプトが実行され、正しさがチェックされます。

---

## ¡Vamos a practicar!

```yaml
type: FinalSlide
key: 7445cd202e
```

`@script`
それでは、コーディングを始めましょう。楽しむこともお忘れなく！

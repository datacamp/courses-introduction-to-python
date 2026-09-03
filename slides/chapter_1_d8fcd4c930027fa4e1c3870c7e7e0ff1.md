---
title: Insert title here
key: d8fcd4c930027fa4e1c3870c7e7e0ff1
video_link:
  mp3: >-
    https://videos.datacamp.com/mp3/translations/course_735/zh-TW/1a64a914-099f-46a0-959a-cfb0b9e15d58-c984f10a2e5238f0d9d224b11b3184ce.mp3
---

## 你好，Python！
```yaml
type: TitleSlide
key: f743ca8c41
```

`@lower_third`
name: Hugo Bowne-Anderson
title: Data Scientist at DataCamp

`@script`
大家好！我是 Hugo，也是「資料科學 Python 入門」這門課程的主講人。

我是 DataCamp 的一名資料科學家和講師。

---

## 學習方式

```yaml
type: FullSlide
key: 30ee08a725
disable_transition: true
```

`@part1`
![DataCamp 介面](https://assets.datacamp.com/img/translations/zh-TW/production/repositories/288/datasets/729574d2168960686381caefe79baf5978e27d0d/liveexercise.jpg)

`@script`
在這門課程中，你將透過類似這樣的影片講解和互動練習來學習有關資料科學的 Python 知識。課程中提供了獨立的 Python 程式設計環境，你可以自由嘗試並撰寫出符合指令要求的正確程式碼。透過這種邊做邊學的方式，你還能即時獲得個性化反饋指導。

---

## Python

```yaml
type: FullSlide
key: 3f23b93572
```

`@part1`
![guido-hba.png](https://assets.datacamp.com/img/translations/zh-TW/production/repositories/288/datasets/fb3e4b8dc114529dafffb37d33f2b2244210d40f/guido-hba.jpg = 38){{1}}

- 通用程式設計：構建任何內容{{2}}

- 開源！免費！{{3}}

- Python 套件，也適用於資料科學{{4}}

	- 許多應用和領域{{5}}

`@script`
Python 最初由 Guido van Rossum 構想並創立。這張照片就是我和 Guido 的合影。它起初只是一個業餘專案，但很快便發展成為了一種通用程式設計語言：如今，你幾乎可以用 Python 來開發任何軟體。這是怎麼做到的呢？首先，Python 是開源且完全免費的。其次，在 Python 中開發「套件」非常簡單。你可以把這些程式碼分享給他人，用來解決特定的問題。久而久之，越來越多專門針對資料科學的擴充套件應運而生。假設你想為公司的銷售資料製作炫酷的可視化圖表，一般都有現成的套件可用；如果你想連接資料庫來分析感測器測量資料？同樣有對應的套件。
人們經常把 Python 比作程式設計界的「瑞士軍刀」，因為你幾乎能用它做任何事。
在這門課程中，我們將帶你一步步掌握資料科學程式設計技能，務必堅持學習，感受這門語言的強大魅力。

---

## IPython Shell

```yaml
type: FullSlide
key: 43a91a7217
```

`@part1`
**執行 Python 命令**

![ipython_shell.png](https://assets.datacamp.com/img/translations/zh-TW/production/repositories/288/datasets/a9e8440bb8fbd49e4a73e4c36ef1cd677c0dd55f/pyexercise.jpg = 95)

`@script`
現在，既然你對 Python 充滿興趣，那就讓我們開始動手嘗試吧！我先從 Python Shell 講起，

---

## IPython Shell

```yaml
type: FullSlide
key: 9c51ee700d
disable_transition: true
```

`@part1`
**執行 Python 命令**

![ipython_shell_highlighted.png](https://assets.datacamp.com/img/translations/zh-TW/production/repositories/288/datasets/dd43cc0183b15b43a072eb0fbab4caa72dee9250/pyexercise_shell.jpg = 95)

`@script`
在這裡輸入 Python 程式碼能即時看到執行結果。在 DataCamp 的練習介面中，Shell 就嵌入在這裡。我們先從簡單的開始，把 Python 當作計算器來使用。

---

## IPython Shell

```yaml
type: FullSlide
key: 524e4c20a7
disable_transition: true
```

`@part1`
 

![在 DataCamp 的 IPython Shell 中執行計算](https://assets.datacamp.com/img/translations/zh-TW/production/repositories/288/datasets/cee32b788a62e4b9a1234ccde56ac9ebb49cfa72/shelladdition.jpg = 95)

`@script`
輸入 4 加 5，然後按下 Enter 鍵，Python 就會解析你輸入的內容，並印出計算結果 9。這裡用到的 Python Shell 其實不是原生版本，而是 IPython，也就是 Interactive Python 的縮寫。它是常規 Python 的「加強版」，在後面會大有用處。

IPython 由 Fernando Pérez 開發，隸屬於更龐大的 Jupyter 生態系統。除了進行互動式操作外，你還可以用 Python 來執行所謂的

---

## Python 腳本

```yaml
type: FullSlide
key: 78ef256bc0
```

`@part1`
- 文字檔 - `.py`{{1}}

- Python 指令清單{{2}}

- 類似於在 IPython Shell 中輸入{{3}}

![DataCamp 平台上的 Python 腳本](https://assets.datacamp.com/img/translations/zh-TW/production/repositories/288/datasets/59f196e96536543a4fb8801228019fc4106f3791/pyexercise_script.jpg = 78){{3}}

`@script`
這些 Python 腳本在本質上就是副檔名為 .py 的文字檔。它記錄了一連串按順序執行的 Python 指令，就像你自己手動在 Shell 視窗裡逐行輸入並執行一樣。

---

## Python 腳本

```yaml
type: FullSlide
key: 717d124175
disable_transition: true
```

`@part1`
![GIF：在腳本中輸入 4 + 5 並按下送出答案。 未顯示輸出。](https://assets.datacamp.com/img/translations/zh-TW/production/repositories/288/datasets/2f96e979012e15329cc158d1e0f496aac3539f45/scriptnoprint.jpg = 95)

`@script`
現在，我們把剛才的指令新增到腳本裡，腳本就在 DataCamp 介面上的這個位置。下一步是按下「送出答案」來執行腳本。不過，如果在 DataCamp 介面裡執行這個腳本，輸出視窗中不會有任何內容。這是因為要想在腳本執行時顯示輸出結果，還必須在程式碼中明確使用 print() 函式。

---

## Python 腳本

```yaml
type: FullSlide
key: c7a9d02fb6
disable_transition: true
code_zoom: 90
```

`@part1`
![python_script_print.gif](https://assets.datacamp.com/img/translations/zh-TW/production/repositories/288/datasets/8b13d046bb54dcb11aa49f0da7363781129d1561/scriptwithprint.jpg = 95)

- 使用 `print()` 從腳本生成輸出

`@script`
我們把剛才的計算放入 print() 函式中，再重新執行一次腳本。這次，輸出的結果和之前一模一樣，太棒了！我們可以把程式碼儲存到 Python 腳本中，而不是每次都在命令列裡手動重複輸入，這不僅能讓程式碼結構更清晰，還能省去修改程式碼時重複輸入的麻煩。你只需在腳本裡完成修改，重新整體執行一遍就行。

---

## DataCamp 介面

```yaml
type: FullSlide
key: 693ba1cd14
```

`@part1`
![DataCamp 介面截圖](https://assets.datacamp.com/img/translations/zh-TW/production/repositories/288/datasets/a9e8440bb8fbd49e4a73e4c36ef1cd677c0dd55f/pyexercise.jpg)

`@script`
現在你已經熟悉了 Python 的不同使用方式，不妨去練習一下。你可以用 IPython Shell 來進行測試和摸索，並在 Python 腳本編輯器中撰寫最終的解答程式碼。按下「送出答案」後，系統就會執行你的腳本並自動校驗結果。

---

## 一起來練習吧！
```yaml
type: FinalSlide
key: 7445cd202e
```

`@script`
開始編寫程式碼吧，好好享受學習的樂趣！

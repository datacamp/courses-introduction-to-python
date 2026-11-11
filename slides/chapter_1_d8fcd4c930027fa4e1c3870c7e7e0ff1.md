---
title: Insert title here
key: d8fcd4c930027fa4e1c3870c7e7e0ff1
video_link:
  mp3: >-
    https://videos.datacamp.com/mp3/translations/course_735/zh-TW/62b80730-bf48-4a1b-83e8-c4292aa0ba94-a69fb3e074d87246fbfd2d7496c9fd50.mp3
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
你好！我是 Hugo，也是「資料科學 Python 入門」這門課程的主講人。

我是 DataCamp 的資料科學家和講師。

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
在這門課程中，你將透過像這樣的影片講解和互動練習，學習資料科學所需的 Python 技能。課程中提供了獨立的 Python 程式設計環境，你可以自由嘗試撰寫程式碼，寫出符合題目要求的正確寫法。你可以邊做邊學，並立即獲得針對作答結果提供的個人化回饋。

---

## Python

```yaml
type: FullSlide
key: 3f23b93572
```

`@part1`
![guido-hba.png](https://assets.datacamp.com/img/translations/zh-TW/production/repositories/288/datasets/fb3e4b8dc114529dafffb37d33f2b2244210d40f/guido-hba.jpg = 38){{1}}

- 用途廣泛：幾乎什麼都能打造{{2}}

- 開放原始碼！免費！{{3}}

- Python 套件，也適用於資料科學{{4}}

	- 應用廣泛，涵蓋多個領域{{5}}

`@script`
Python 最初由 Guido Van Rossum 發想並創立。這張照片就是我和 Guido 的合影。它起初只是一個業餘專案，但很快便發展成為了一種通用程式設計語言：如今，你可以用 Python 來開發幾乎任何軟體。這是怎麼做到的呢？首先，Python 是開放原始碼且完全免費。其次，在 Python 中開發「套件」非常簡單。你可以透過套件將程式碼分享給他人，用來解決特定的問題。久而久之，越來越多專為資料科學開發的套件陸續問世。假設你想為公司的銷售資料製作酷炫的視覺化圖表，就有現成的套件可用；如果你想連接資料庫來分析感測器測量資料？同樣有對應的套件。
Python 常被稱為程式設計界的瑞士刀，因為你能用它做幾乎任何事。
在這門課程中，我們會帶你一步步掌握資料科學程式設計技能，務必持續學習，感受這門語言的強大魅力。

---

## IPython Shell

```yaml
type: FullSlide
key: 43a91a7217
```

`@part1`
**執行 Python 指令**

![ipython_shell.png](https://assets.datacamp.com/img/translations/zh-TW/q1/production/repositories/288/datasets/a9e8440bb8fbd49e4a73e4c36ef1cd677c0dd55f/pyexercise.jpg = 95)

`@script`
既然你已經對 Python 充滿興趣，就讓我們開始動手實作吧！先從 Python Shell 開始，

---

## IPython Shell

```yaml
type: FullSlide
key: 9c51ee700d
disable_transition: true
```

`@part1`
**執行 Python 指令**

![ipython_shell_highlighted.png](https://assets.datacamp.com/img/translations/zh-TW/q1/production/repositories/288/datasets/dd43cc0183b15b43a072eb0fbab4caa72dee9250/pyexercise_shell.jpg = 95)

`@script`
在這裡輸入 Python 程式碼，能即時看到執行結果。在 DataCamp 的練習介面中，就嵌入了 Shell。我們先從簡單的開始，將 Python 當作計算機來使用。

---

## IPython Shell

```yaml
type: FullSlide
key: 524e4c20a7
disable_transition: true
```

`@part1`
 

![在 DataCamp 的 IPython Shell 中執行計算](https://assets.datacamp.com/img/translations/zh-TW/q1/production/repositories/288/datasets/cee32b788a62e4b9a1234ccde56ac9ebb49cfa72/shelladdition.jpg = 95)

`@script`
輸入 4 + 5，然後按下 Enter 鍵，Python 會解析你輸入的內容，並輸出計算結果 9。這裡使用的 Python Shell 其實不是原生版本，而是 IPython，也就是 Interactive Python 的縮寫。它是一般 Python 的加強版，在之後的課程中會派上用場。

IPython 由 Fernando Pérez 開發，隸屬於更龐大的 Jupyter 生態系統。除了能進行互動式操作外，你還可以讓 Python 執行 Python 腳本。

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
這些 Python 腳本其實就是副檔名為 .py 的文字檔，裡面記錄了一連串 Python 指令，執行腳本時，Python 會依序執行這些指令，就像你親自在 Shell 中逐行輸入指令一樣。

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
現在將剛才的指令新增到腳本裡，腳本就在 DataCamp 介面上的這個位置。下一步是按下「送出答案」來執行腳本。不過，如果在 DataCamp 介面裡執行這個腳本，輸出視窗中不會有任何內容。這是因為要想在腳本執行時顯示輸出結果，還必須在程式碼中明確使用 print() 函式。

---

## Python 腳本

```yaml
type: FullSlide
key: c7a9d02fb6
disable_transition: true
code_zoom: 90
```

`@part1`
![python_script_print.gif](https://assets.datacamp.com/img/translations/zh-TW/q1/production/repositories/288/datasets/8b13d046bb54dcb11aa49f0da7363781129d1561/scriptwithprint.jpg = 95)

- 使用 `print()` 輸出腳本的執行結果

`@script`
將剛才的計算放入 print() 函式中，再重新執行腳本。這次輸出的結果和之前一模一樣，太棒了！我們可以將程式碼寫在 Python 腳本中，而不是每次都手動重新輸入，不僅能讓程式碼結構更清晰，還能避免修改時一再重複輸入所有內容。你只需在腳本裡修改，再重新執行整個腳本就行了。

---

## DataCamp 介面

```yaml
type: FullSlide
key: 693ba1cd14
```

`@part1`
![DataCamp 介面截圖](https://assets.datacamp.com/img/translations/zh-TW/q1/production/repositories/288/datasets/a9e8440bb8fbd49e4a73e4c36ef1cd677c0dd55f/pyexercise.jpg)

`@script`
現在你已經大致瞭解使用 Python 的不同方式，不妨去練習一下。你可以先在 IPython Shell 自由嘗試，再使用 Python 腳本編輯器撰寫解題程式碼。按下「送出答案」後，系統就會執行你的腳本，並檢查答案是否正確。

---

## 練習看看！
```yaml
type: FinalSlide
key: 7445cd202e
```

`@script`
開始寫程式吧！盡情享受學習的樂趣！

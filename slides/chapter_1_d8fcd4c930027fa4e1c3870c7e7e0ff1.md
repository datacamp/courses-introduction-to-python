---
title: Insert title here
key: d8fcd4c930027fa4e1c3870c7e7e0ff1
video_link:
  mp3: >-
    https://videos.datacamp.com/mp3/translations/course_735/de-DE/bb9fe3cf-7b32-4d05-aaa2-ac6631daedb8.mp3
---

## Hallo Python!

```yaml
type: TitleSlide
key: f743ca8c41
```

`@lower_third`
name: Hugo Bowne-Anderson
title: Data Scientist at DataCamp

`@script`
Hey, ich bin Hugo und werde euch durch den Kurs Einführung in Python begleiten.

Ich bin Datenwissenschaftler – oder Data Scientist – und Dozent bei DataCamp.


---

## Wie du lernen wirst

```yaml
type: FullSlide
key: 30ee08a725
disable_transition: true
```

`@part1`
![DataCamp-Schnittstelle](https://assets.datacamp.com/img/translations/de-DE/production/repositories/288/datasets/729574d2168960686381caefe79baf5978e27d0d/liveexercise.gif)

`@script`
In diesem Kurs lernst du die Grundlagen von Python mit Video-Lektionen wie dieser und interaktiven Übungen. Du bekommst deine eigene Python Session, in der du experimentieren und versuchen kannst, den richtigen Code zur Lösung der Aufgaben zu finden. Du lernst durch praktische Übungen und bekommst sofort individuelles Feedback zu deiner Arbeit.


---

## Python

```yaml
type: FullSlide
key: 3f23b93572
```

`@part1`
![guido-hba.png](https://assets.datacamp.com/img/translations/de-DE/production/repositories/288/datasets/fb3e4b8dc114529dafffb37d33f2b2244210d40f/guido-hba.png = 38){{1}}

- Für allgemeine Zwecke: baue alles mögliche damit!{{2}}

- Open Source! Kostenlos!{{3}}

- Python-Pakete, auch für Data Science{{4}}

	- Viele Anwendungen und Bereiche{{5}}

`@script`
Python wurde von Guido Van Rossum erdacht. Guido ist der nette Mann hier auf der linken Seite – daneben bin ich. Was als Hobbyprojekt anfing, wurde schnell zu einer Allzweck-Programmiersprache: Heute kannst du Python für so ziemlich jedes Softwareprojekt nutzen. Aber wie ist es dazu gekommen? Zunächst einmal ist Python „Open Source“ und die Nutzung ist kostenlos. Zweitens ist es sehr einfach, Pakete in Python zu erstellen, also Code, den man mit anderen teilen kann, um bestimmte Probleme zu lösen. Im Laufe der Zeit sind immer mehr dieser speziell für die Datenwissenschaft entwickelten Pakete entstanden. Angenommen, du möchtest ein paar coole Visualisierungen von Firmenumsätzen erstellen. Dafür gibt es dann ein Paket. Oder wie wäre es, eine Verbindung zu einer Datenbank herzustellen, um Sensormessungen zu analysieren? Auch dafür gibt es ein Paket.
Oft wird Python als das Schweizer Taschenmesser unter den Programmiersprachen bezeichnet, weil man damit fast alles machen kann.
In diesem Kurs werden wir deine Programmierkenntnisse im Bereich Datenwissenschaft Schritt für Schritt aufbauen. Bleib also dabei, um zu sehen, wie leistungsstark diese Sprache sein kann.


---

## IPython Shell

```yaml
type: FullSlide
key: 43a91a7217
```

`@part1`
**Python-Befehle ausführen**

![ipython_shell.png](https://assets.datacamp.com/img/translations/de-DE/production/repositories/288/datasets/a9e8440bb8fbd49e4a73e4c36ef1cd677c0dd55f/pyexercise.png = 95)

`@script`
Jetzt, wo du Python kennengelernt hast, lass uns loslegen und experimentieren. Wir starten mit der


---

## IPython Shell

```yaml
type: FullSlide
key: 9c51ee700d
disable_transition: true
```

`@part1`
**Python-Befehle ausführen**

![ipython_shell_highlighted.png](https://assets.datacamp.com/img/translations/de-DE/production/repositories/288/datasets/dd43cc0183b15b43a072eb0fbab4caa72dee9250/pyexercise_shell.jpg = 95)

`@script`
Python „shell“, einem Ort, an dem du Code eingeben und sofort die Ergebnisse sehen kannst. In der Übungsumgebung von DataCamp ist diese Shell eingebettet. Fangen wir ganz einfach an und nutzen Python als Taschenrechner.


---

## IPython Shell

```yaml
type: FullSlide
key: 524e4c20a7
disable_transition: true
```

`@part1`
&nbsp;

![Berechnungen in der IPython-Shell von DataCamp](https://assets.datacamp.com/img/translations/de-DE/production/repositories/288/datasets/cee32b788a62e4b9a1234ccde56ac9ebb49cfa72/shelladdition.gif = 95)

`@script`
Ich tippe vier plus fünf ein und drücke die Eingabetaste. Python versteht die Eingabe und zeigt das Ergebnis der Berechnung an: Neun ist das korrekte Ergebnis. Die Shell, die wir hier benutzen, ist eigentlich nicht die Originalversion; wir benutzen iPython, kurz für „Interactive Python“, eine Art aufgepeppte Version von Python, die später noch nützlich sein wird.

Sie wurde von Fernando Pérez entwickelt und ist Teil des größeren Jupyter-Ökosystems. Neben der interaktiven Arbeit mit Python kannst du Python auch sogenannte


---

## Python-Skript

```yaml
type: FullSlide
key: 78ef256bc0
```

`@part1`
- Textdateien – `.py`{{1}}

- Eine Liste mit Python-Befehlen{{2}}

- Ähnlich wie Befehlseingabe in IPython-Shell{{3}}

![Python-Skript in DataCamp](https://assets.datacamp.com/img/translations/de-DE/production/repositories/288/datasets/59f196e96536543a4fb8801228019fc4106f3791/pyexercise_script.jpg = 78){{3}}

`@script`
Python Skripte ausführen. Diese Python Skripte sind einfach Textdateien mit der Endung „Punkt P-Ypsilon“. Es handelt sich im Grunde um eine Liste von Python Befehlen, die ausgeführt werden. Fast so, als würdest du die Befehle selbst Zeile für Zeile in die Shell eingeben.


---

## Python-Skript

```yaml
type: FullSlide
key: 717d124175
disable_transition: true
```

`@part1`
![GIF: 4 + 5 in das Skript eingeben und auf „Antwort senden“ klicken. Es wird nichts angezeigt.](https://assets.datacamp.com/img/translations/de-DE/production/repositories/288/datasets/2f96e979012e15329cc158d1e0f496aac3539f45/scriptnoprint.gif = 95)

`@script`
Lass uns den Befehl von vorhin jetzt in ein Skript packen, welches sich in der DataCamp-Oberfläche befindet. Jetzt musst du das Skript ausführen, indem du auf „Antworten“ klickst. Wenn du dieses Skript in der DataCamp-Oberfläche ausführst, wird im Ausgabefenster nichts angezeigt. Das liegt daran, dass explizit die Funktion „print“ in Skripten verwenden musst, wenn du während der Ausführung eine Ausgabe generieren möchtest.


---

## Python-Skript

```yaml
type: FullSlide
key: c7a9d02fb6
disable_transition: true
code_zoom: 90
```

`@part1`
![python_script_print.gif](https://assets.datacamp.com/img/translations/de-DE/production/repositories/288/datasets/8b13d046bb54dcb11aa49f0da7363781129d1561/scriptwithprint.gif = 95)

- Verwende `print()`, um die Ausgabe aus dem Skript zu generieren.

`@script`
Packen wir unsere vorherige Berechnung in einen „print“-Befehl und führen das Skript erneut aus. Diesmal wird die gleiche Ausgabe wie zuvor generiert! Das Schreiben von Code in Python Skripten, anstatt dem manuellen Tippen jedes Schritts in der Shell, hilft dir dabei eine Struktur beizubehalten und nicht alles immer wieder neu tippen zu müssen, wenn du etwas ändern möchtest. Du nimmst einfach die Änderung im Skript vor und führst das Ganze erneut aus.


---

## DataCamp-Schnittstelle

```yaml
type: FullSlide
key: 693ba1cd14
```

`@part1`
![Screenshot der DataCamp-Oberfläche](https://assets.datacamp.com/img/translations/de-DE/production/repositories/288/datasets/a9e8440bb8fbd49e4a73e4c36ef1cd677c0dd55f/pyexercise.png)

`@script`
Jetzt, wo du einen Eindruck von den verschiedenen Möglichkeiten der Arbeit mit Python bekommen hast, schau doch mal bei den Übungen vorbei. Experimentiere mit der iPython Shell und schreibe die richtige Antwort mit dem Python Skript-Editor. Wenn du auf „Antworten“ klickst, wird dein Skript ausgeführt und auf Fehler überprüft.


---

## Lass uns üben!

```yaml
type: FinalSlide
key: 7445cd202e
```

`@script`
Leg los mit dem Programmieren hab Spaß dabei!

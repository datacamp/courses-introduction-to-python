---
title: Insert title here
key: 433dcfcfedaee070cbf440491c402e3b
video_link:
  mp3: >-
    https://videos.datacamp.com/mp3/translations/course_735/de-DE/9ec17427-ed61-48b8-97cb-299c6ecf0e2c.mp3
---

## Variablen und Typen

```yaml
type: TitleSlide
key: dc8b62f1c8
```

`@lower_third`
name: Hugo Bowne-Anderson
title: Data Scientist at DataCamp

`@script`
Gut gemacht und willkommen zurück! Es ist offensichtlich, dass Python ein toller Taschenrechner ist. Wenn du aber komplexere Berechnungen durchführen möchtest, solltest du Werte während des Programmierens „speichern“ können.


---

## Variable

```yaml
type: FullSlide
key: 36ec318b41
```

`@part1`
- Spezifischer Name unter Beachtung der Groß-/Kleinschreibung

- Wert prüfen mittels Aufruf des Variablennamen{{1}}

- 1,79 m – 68,7 kg{{2}}

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
Du kannst das machen, indem du eine Variable mit einem bestimmten Namen definierst, bei welchem die Groß- und Kleinschreibung beachtet werden muss. Sobald du solch eine Variable erstellt oder deklariert hast, kannst du ihren Wert später aufrufen, indem du den Variablennamen eingibst.

Angenommen, du misst deine Größe und dein Gewicht in metrischen Einheiten: Du bist ein-Meter-neunundsiebzig groß und wiegst achtundsechzig-Komma-sieben Kilogramm. Du kannst diese Werte zwei Variablen namens „height“ und „weight“ mit einem Gleichheitszeichen zuweisen:

Wenn du jetzt den Namen der Variablen, „height“, eingibst,

sucht Python nach dem Variablennamen, ruft seinen Wert ab und gibt ihn aus.


---

## BMI berechnen

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

$$ \text{BMI} = \frac{\text{Gewicht}}{\text{Körpergröße}^2} $${{1}}

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
Berechnen wir jetzt den Body-Mass-Index, kurz BMI, mit dem Gewicht in Kilogramm und der Größe in Metern. Du kannst das mit den tatsächlichen Werten machen. Genauso gut kannst du die Variablen „height“ und „weight“ verwenden, wie in diesem Beispiel. Jedes Mal, wenn du den Namen der Variablen eingibst, sagst du Python, dass es diesen durch den aktuellen Wert der Variablen ersetzen soll. „weight“ entspricht achtundsechzig-Komma-sieben und „height“ entspricht ein-Meter-neunundsiebzig.

Zum Schluss speichert Python das Ergebnis in einer neuen Variablen namens „BMI“. „BMI“ hat jetzt denselben Wert wie deine vorherige Berechnung.

In Python werden Variablen ständig verwendet. Sie helfen dabei, deinen Code reproduzierbar zu machen.


---

## Reproduzierbarkeit

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
Angenommen, der Code zum Erstellen der Variablen „height“, „weight“ und „BMI“ ist in einem Skript wie diesem enthalten. Wenn du jetzt den BMI für ein anderes Gewicht neu berechnen willst,


---

## Reproduzierbarkeit

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
kannst du einfach die Deklaration der Variablen „weight“ ändern und das Skript erneut ausführen. Der BMI ändert sich entsprechend, weil sich auch der Wert der Variablen „weight“ geändert hat.

Bisher haben wir nur mit Zahlenwerten wie Größe und Gewicht gearbeitet.


---

## Python-Typen

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
In Python haben alle diese Zahlen einen bestimmten Typ. Du kannst den Typ eines Wertes mit der Funktion „type“ überprüfen. Um den Typ deines BMI-Wertes zu sehen, schreibe einfach „type“ und dann „BMI“ in runden Klammern. Du siehst, dass es sich um einen „float“ Datentyp handelt, also um eine Art, wie Python reelle Zahlen darstellt. Das sind Zahlen, die sowohl einen ganzzahligen als auch einen Bruchteil haben können. Python hat auch einen Typ für ganze Zahlen: „int“, „integer“, wie in diesem Beispiel.

Für Data Science brauchst du allerdings mehr als nur „ints“ und „floats“.


---

## Python-Typen (2)

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
Python hat noch jede Menge andere Datentypen. Die am häufigsten genutzten sind „strings“ und „booleans“.

In Python wird ein „string“ dazu genutzt, Text darzustellen. Wir können sowohl einfache als auch doppelte Anführungszeichen verwenden, um einen String zu erstellen, wie wir an diesen Beispielen sehen können. Wenn wir den Typ der letzten Variable ausgeben, sehen wir, dass es „s-t-r“ ist, die kurze Schreibweise für „string“.

Der Boolesche Wert ist ein Typ, der entweder „true“ oder „false“ sein kann. Wir können uns das im Alltag als „Ja“ und „Nein“ vorstellen. Boolesche Werte werden für dich noch sehr nützlich sein, zum Beispiel um deine Daten zu filtern.

Python Datentypen haben etwas Besonderes an sich.


---

## Python-Typen (3)

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

- Unterschiedlicher Typ = unterschiedliches Verhalten!{{3}}

`@script`
Schau dir mal diese Codezeile an, die zwei ganze Zahlen addiert, und dann diese Codezeile, die zwei Zeichenfolgen addiert.

Bei den ganzen Zahlen wurden die Werte einfach addiert, bei den Zeichenfolgen wurden die Zeichenfolgen aneinandergehängt. Der Plus-Operator hat sich bei verschiedenen Datentypen unterschiedlich verhalten. Das ist ein allgemeiner Grundsatz: „Wie“ sich der Code verhält, hängt von den Datentypen ab, mit denen du arbeitest.

In den folgenden Übungen wirst du deine ersten Variablen erstellen und mit einigen Datentypen von Python experimentieren. Wir sehen uns im nächsten Video, wo ich dir alles über Listen erkläre.


---

## Lass uns üben!

```yaml
type: FinalSlide
key: b7fc40db4d
```

`@script`
Lass uns mit dem Programmieren anfangen! Ich freue mich schon darauf, dich im nächsten Kapitel wiederzusehen, wo du noch beeindruckendere Python Diagramme erstellen wirst.

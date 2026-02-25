---
title: Insert title here
key: ae3238dcc7feb9adecfee0c395fc8dc8
video_link:
  mp3: >-
    https://videos.datacamp.com/mp3/translations/course_735/de-DE/bdbbd965-5d02-4c77-909c-455d6fc442dc.mp3
---

## Zweidimensionale NumPy-Arrays

```yaml
type: TitleSlide
key: 0cc8abf493
```

`@lower_third`
name: Hugo Bowne-Anderson
title: Data Scientist at DataCamp

`@script`
Gut gemacht, du bist echt der Hammer! Lass uns jetzt die NumPy-Arrays aus dem letzten Video nachbauen.


---

## Arten von NumPy-Arrays

```yaml
type: FullSlide
key: 1b9db47fd2
code_zoom: 100
```

`@part1`
```py
import numpy as np
np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
np_weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])
```

```py
type(np_height)
```

```out
numpy.ndarray
```

```py
type(np_weight)
```

```out
numpy.ndarray
```

`@script`
Wenn du nach dem Typ dieser Arrays fragst, sagt dir Python, dass es sich um „NumPy Punkt n-d array“ handelt. „NumPy Punkt“ sagt dir, dass es sich um einen Typ handelt, der im NumPy-Paket definiert wurde. „n-d-array“ steht für ein n-dimensionales Array. Die Arrays „n-p Unterstrich height“ und „n-p Unterstrich weight“ sind eindimensionale Arrays. Es ist aber auch absolut möglich, zweidimensionale, dreidimensionale oder sogar siebendimensionale Arrays zu erstellen! Bleiben wir in diesem Video aber bei zweidimensionalen.


---

## Zweidimensionale NumPy-Arrays

```yaml
type: FullSlide
key: ebb550dcba
code_zoom: 71
```

`@part1`
```py
np_2d = np.array([[1.73, 1.68, 1.71, 1.89, 1.79],
                  [65.4, 59.2, 63.6, 88.4, 68.7]])
```{{1}}
```py
np_2d
```{{2}}

```out
array([[ 1.73,  1.68,  1.71,  1.89,  1.79],
       [65.4 , 59.2 , 63.6 , 88.4 , 68.7 ]])
```{{2}}

```py
np_2d.shape
```{{3}}

```out
(2, 5) # 2 rows, 5 columns
```{{3}}

```py
np.array([[1.73, 1.68, 1.71, 1.89, 1.79],
          [65.4, 59.2, 63.6, 88.4, "68.7"]])
```{{4}}

```out
array([['1.73', '1.68', '1.71', '1.89', '1.79'],
       ['65.4', '59.2', '63.6', '88.4', '68.7']], dtype='<U32')
```{{4}}

`@script`
Du kannst ein zweidimensionales-NumPy-Array aus einer regulären Python Liste von Listen erstellen. Versuchen wir nun, ein NumPy-Array für alle Größen- und Gewichtsdaten deiner Familie zu erstellen, so wie hier.

Wenn du jetzt den Inhalt der Liste „n-p Unterstrich_zwei-D“ ausgeben lässt, siehst du, dass es sich um eine rechteckige Datenstruktur handelt: Jede Unterliste in der Liste passt zu einer Zeile im zweidimensionalen Numpy-Array. Aus „n-p Unterstrich zwei-D Punkt shape“ kannst du erkennen, dass wir tatsächlich zwei Zeilen und fünf Spalten haben. „shape“ ist ein sogenanntes Attribut des „n-p-Zwei-D-Arrays“, das dir mehr Infos darüber gibt, wie die Datenstruktur aussieht.

Beachte, dass die Syntax für den Zugriff auf ein Attribut ein bisschen wie der Aufruf einer Methode aussieht. Sie sind jedoch nicht gleich! Denk daran, dass Methoden runde Klammern haben. Wie du hier sehen kannst, haben Attribute diese Klammern nicht.

Auch für „zweidimensionale-Arrays“ gilt die NumPy-Regel: Ein Array kann nur Daten eines einzigen Typs enthalten. Wenn du einen „float“-Wert in einen „string“ umwandelst, werden alle Array-Elemente in „strings“ umgewandelt, sodass am Ende ein homogenes Array entsteht.


---

## Teilmengenbildung

```yaml
type: FullSlide
key: e71d2fc8b8
code_zoom: 80
```

`@part1`
```out
           0       1       2       3       4
           
array([[  1.73,   1.68,   1.71,   1.89,   1.79],     0
       [  65.4,   59.2,   63.6,   88.4,   68.7]])    1
```

```py
np_2d[0]
```

```out
array([1.73, 1.68, 1.71, 1.89, 1.79])
```

`@script`
Du kannst dir das „zweidimensionale-NumPy-Array“ wie eine verbesserte „Liste von Listen“ vorstellen: Du kannst Berechnungen auf den Arrays durchführen. Außerdem kannst du erweiterte Methoden zum Erstellen von Teilmengen anwenden.

Angenommen, du möchtest die erste Zeile und dann das dritte Element in dieser Zeile extrahieren. Um die Zeile auszuwählen, brauchst du den Index Null in eckigen Klammern. Denke immer an die Null-Indizierung.

Um dann das dritte Element zu wählen, kannst du denselben Aufruf mit einem weiteren Klammerpaar erweitern, diesmal mit dem Index „Zwei“.


---

## Teilmengenbildung

```yaml
type: FullSlide
key: 57a1fb1581
disable_transition: true
code_zoom: 80
```

`@part1`
```out
           0       1       2       3       4
           
array([[  1.73,   1.68,   1.71,   1.89,   1.79],     0
       [  65.4,   59.2,   63.6,   88.4,   68.7]])    1
```

```py
np_2d[0][2]
```

```out
1.71
```

```py
np_2d[0, 2]
```{{1}}

```out
1.71
```{{1}}

`@script`
So wie hier. Im Grunde wählst du die Zeile aus und wählst dann in dieser Zeile erneut aus.

Es gibt noch eine andere Möglichkeit, Teilmengen zu bilden, indem man eckige Klammern und ein Komma benutzt. Dieser Aufruf gibt genau den selben Wert wie vorher zurück. Der Wert vor dem Komma gibt die Zeile an, während der Wert nach dem Komma die Spalte angibt. Die Schnittpunkte der angegebenen Zeilen und Spalten werden zurückgegeben. Wenn du dich erst mal daran gewöhnt hast, ist diese Syntax intuitiver und bietet dir mehr Möglichkeiten.


---

## Teilmengenbildung

```yaml
type: FullSlide
key: feb75c975c
disable_transition: true
code_zoom: 80
```

`@part1`
```out
           0       1       2       3       4
           
array([[  1.73,   1.68,   1.71,   1.89,   1.79],     0
       [  65.4,   59.2,   63.6,   88.4,   68.7]])    1
```

```py
np_2d[:, 1:3]
```{{1}}

```out
array([[ 1.68,  1.71],
       [59.2 , 63.6 ]])
```{{1}}

```py
np_2d[1, :]
```{{2}}

```out
array([65.4, 59.2, 63.6, 88.4, 68.7])
```{{2}}

`@script`
Angenommen, du willst die Größe und das Gewicht des zweiten und dritten Familienmitglieds auswählen. Du willst beide Zeilen, also setzt du vor dem Komma einen Doppelpunkt. Du willst nur die zweite und dritte Spalte, also gibst du nach dem Komma die Indizes eins bis drei ein. Denk daran, dass der dritte Index hier nicht inkludiert ist. Die Schnittmenge ergibt ein „zweidimensionales-Array“ mit zwei Zeilen und zwei Spalten:

Genauso kannst du das Gewicht aller Familienmitglieder auswählen: Du willst nur die zweite Zeile, also schreibst du eine eins vor das Komma. Du willst alle Spalten, also setzt du nach dem Komma einen Doppelpunkt. Die Schnittmenge gibt uns die ganze zweite Reihe.

Letztlich kannst du mit „Zweidimensionalen NumPy-Arrays“ genauso elementweise Berechnungen durchführen, wie du es mit eindimensionalen NumPy-Arrays gemacht hast. Das ist echt nützlich.


---

## Lass uns üben!

```yaml
type: FinalSlide
key: 6047b27c09
```

`@script`
Du kannst damit in den Übungen herumspielen und auch zweidimensionale-NumPy-Arrays erstellen und Teilmengen daraus bilden! Spannend

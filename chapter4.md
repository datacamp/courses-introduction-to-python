---
title_meta: "Kapitel\_4"
title: NumPy
description: >-
  NumPy ist ein grundlegendes Python-Paket für Data Science. In diesem Kapitel
  lernst du den Umgang mit den leistungsstarken Tools im NumPy-Array und
  beginnst mit der Datenexploration.
attachments:
  slides_link: 'https://projector-video-pdf-converter.datacamp.com/735/chapter4.pdf'
lessons:
  - nb_of_exercises: 5
    title: NumPy
  - nb_of_exercises: 5
    title: 2D-NumPy-Arrays
  - nb_of_exercises: 3
    title: 'NumPy: Grundlegende Statistiken'
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

## Dein erstes NumPy-Array

```yaml
type: NormalExercise
key: 84cab9d170
lang: python
xp: 100
skills:
  - 2
```

Jetzt widmen wir uns einem spannenden Sport: Baseball! Dabei lernst du die Grundlagen von `numpy` kennen, einem leistungsstarken Paket für Data Science.

Im Python-Skript wurde bereits die Liste `baseball` definiert, in der die Körpergrößen einiger Baseballspieler in Zentimetern enthalten sind. Kannst du den fehlenden Code hinzufügen, um daraus ein `numpy`-Array zu erstellen?

`@instructions`
- Importiere das Paket `numpy` als `np`, sodass du mit `np` auf `numpy` verweisen kannst.
- Verwende `np.array()`, um das `numpy` Array aus `baseball` zu erstellen. Nenne das Array `np_baseball`.
- Gib den Typ von `np_baseball` aus, um zu überprüfen, ob du alles richtig gemacht hast.

`@hint`
- Mit `import numpy as np` klappt es. Jetzt musst du `np.fun_name()` verwenden, wenn du eine Funktion aus `numpy` nutzen willst.
- `np.array()` sollte `baseball` als Eingabe entgegennehmen. Weise das Ergebnis des Funktionsaufrufs `np_baseball` zu.
- Um den Typ einer Variablen `x` auszugeben, schreibe einfach `print(type(x))`.

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
predef_msg = "Du musst die vordefinierten Variablen nicht ändern oder entfernen."
Ex().has_import("numpy")
Ex().check_correct(
  check_object("np_baseball"),
  multi(
    check_object("baseball", missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
    check_function("numpy.array").check_args(0).has_equal_ast()
  )
)

Ex().has_printout(0)
success_msg("Tolle Arbeit!")
```

---

## Körpergrößen der Baseballspieler

```yaml
type: NormalExercise
key: e7e25a89ea
lang: python
xp: 100
skills:
  - 2
```

Du bist ein wahrer Baseballfan. Du beschließt, bei der MLB (Major League Baseball) anzurufen und nach weiteren Statistiken zur Größe der wichtigsten Spieler zu fragen. Man sendet dir Daten zu über tausend Spielern, die als normale Python-Liste gespeichert sind: `height_in`. Die Körpergröße ist jeweils in Zoll angegeben. Kannst du ein `numpy`-Array daraus machen und die Maße in Meter umrechnen?

`height_in` ist bereits erstellt und das Paket `numpy` ist geladen, sodass du sofort loslegen kannst. (Datenquelle: stat.ucla.edu)

`@instructions`
- Erstelle ein `numpy`-Array aus `height_in`. Nenne dieses neue Array `np_height_in`.
- Gib `np_height_in` aus.
- Multipliziere `np_height_in` mit `0.0254`, um alle Größenangaben von Zoll in Meter umzurechnen. Speichere die neuen Werte in ein neues Array namens `np_height_m`.
- Gib `np_height_m` aus und prüfe, ob die Ausgabe Sinn ergibt.

`@hint`
- Verwende `np.array()` und übergebe `height`. Speichere das Ergebnis in `np_height_in`.
- Um eine Variable `x` auszugeben, schreibe `print(x)` im Python-Skript.
- Führe die Berechnungen so durch, als ob `np_height_in` eine einzelne Zahl wäre: `np_height_in * conversion_factor` ist Teil der Antwort.
- Um eine Variable `x` auszugeben, schreibe `print(x)` im Python-Skript.

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
  check_object("np_height_m").has_equal_value(incorrect_msg = "Verwende `np_height_in * 0.0254`, um `np_height_m` zu berechnen.")
)

success_msg("Super! Im Handumdrehen führt `numpy` Multiplikationen an mehr als 1000 Höhenmessungen durch.")
```

---

## NumPy-Nebenwirkungen

```yaml
type: MultipleChoiceExercise
key: 3662ff6637
lang: python
xp: 50
skills:
  - 2
```

`numpy` eignet sich hervorragend für die Vektorrechnung. Wenn du die Funktionalität mit normalen Python-Listen vergleichst, gibt es aber ein paar Unterschiede.

Erstens können `numpy` Arrays keine Elemente mit unterschiedlichen Typen haben. Wenn du verschiedene Typen wie Boolesche Werte und Ganzzahlen mischst, werden sie automatisch mit `numpy` in einen gemeinsamen Typ umgewandelt. Boolesche Werte wie`True`  und`False` werden in Kombination mit Zahlen wie`1` und `0` behandelt, sodass das Array am Ende aus ganzen Zahlen besteht.

Zweitens haben die typischen arithmetischen Operatoren wie `+`, `-`, `*` und `/` eine unterschiedliche Bedeutung bei regulären Python-Listen und `numpy`-Arrays.

Wähle den Code aus, der die folgende Ausgabe erzeugt:

```
np.array([True, 1, 2]) + np.array([3, 4, False])
```

Das Paket `numpy` ist bereits als `np` importiert. Du kannst jede Option in der IPython-Shell ausführen, um die Ausgabe zu sehen.

`@possible_answers`
- `np.array([True, 1, 2, 3, 4, False])`
- `np.array([4, 3, 0]) + np.array([0, 2, 2])`
- `np.array([1, 1, 2]) + np.array([3, 4, -1])`
- `np.array([0, 1, 2, 3, 4, 5])`

`@hint`
- Kopiere die verschiedenen Code-Teile und füge sie in die IPython-Shell ein. Drücke die **Eingabetaste**, um den Code auszuführen und zu sehen, welche Ausgabe mit der von `np.array([True, 1, 2]) + np.array([3, 4, False])` übereinstimmt.

`@pre_exercise_code`
```{python}
import numpy as np
```

`@sct`
```{python}
msg1 = msg3 = msg4 = "Falsch. Probiere die verschiedenen Codeblöcke aus und sieh, welcher mit dem Zielcodeblock übereinstimmt."
msg2 = "Tolle Arbeit! `True` wird in 1 umgewandelt, `False` wird in 0 umgewandelt."
Ex().has_chosen(2, [msg1, msg2, msg3, msg4])
```

---

## Elemente von NumPy-Arrays abrufen

```yaml
type: NormalExercise
key: fcb2a9007b
lang: python
xp: 100
skills:
  - 2
```

Der Zugriff auf Elemente (unter Nutzung der Notation mit eckigen Klammern bei Listen oder Arrays) funktioniert bei Listen und Arrays gleichermaßen.

Für diese Übung wurden bereits die zwei Listen `height_in` und `weight_lb` im Hintergrund für dich geladen. In diesen sind die Größe und das Gewicht der MLB-Spieler hinterlegt. Außerdem sind die zwei `numpy`-Arrays `np_weight_lb` und `np_height_in` für dich vorbereitet.

`@instructions`
- Greife auf das Element mit dem Indexwert 50 in `np_weight_lb` zu und gib es aus.
- Gib ein Teilarray von `np_height_in` aus, das alle Elemente ab Index 100 bis **einschließlich** Index 110 enthält.

`@hint`
- Denk daran, deine Abfragen bestimmter Elemente in eine `print()`-Funktion zu packen.
- Verwende `[100:111]`, um alle Elemente ab Index 100 bis einschließlich Index 110 zu erhalten.

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
msg = "Du musst die vordefinierten Variablen nicht ändern oder entfernen."
Ex().multi(
    check_object("np_height_in", missing_msg=msg).has_equal_value(incorrect_msg=msg),
    check_object("np_weight_lb", missing_msg=msg).has_equal_value(incorrect_msg=msg)
)

Ex().has_printout(0)
Ex().has_printout(1)

success_msg("Schön! Zeit, etwas Neues zu lernen: 2D-NumPy-Arrays!")
```

---

## 2D-NumPy-Arrays

```yaml
type: VideoExercise
key: 1241efac7a
xp: 50
```

`@projector_key`
ae3238dcc7feb9adecfee0c395fc8dc8

---

## Dein erstes 2D-NumPy-Array

```yaml
type: NormalExercise
key: 5cb045bb13
lang: python
xp: 100
skills:
  - 2
```

Bevor wir uns mit den echten MLB-Daten beschäftigen, lass uns versuchen, aus einer kleinen Liste von Listen eine 2D `numpy`-Array zu erstellen.

In dieser Übung ist `baseball` eine Liste, deren Elemente auch Listen sind. Die Hauptliste enthält vier Elemente. Jedes dieser Elemente ist wiederum eine Liste und enthält jeweils die Körpergröße und das Gewicht (in genau dieser Reihenfolge) von vier Baseballspielern. `baseball` ist bereits für dich im Skript kodiert.

`@instructions`
- Verwende `np.array()`, um ein 2D `numpy`-Array aus `baseball` zu erstellen. Nenne es `np_baseball`.
- Gib den Typ von `np_baseball` aus.
- Gib das `shape`-Attribut von `np_baseball` aus. Verwende `np_baseball.shape`.

`@hint`
- `baseball` ist bereits im Skript für dich kodiert. Rufe `np.array()` damit auf und speichere das resultierende 2D `numpy`-Array in `np_baseball`.
- Kombiniere `print()` mit `type()` für die zweite Aufgabe.
- `np_baseball.shape` liefert dir die Dimensionen von `np_baseball`. Denk daran, alles in einen `print()`-Aufruf zu packen!

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
msg = "Du musst die vordefinierten Variablen nicht ändern oder entfernen."
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

success_msg("Super! Du bist jetzt bereit, die tatsächlichen MLB-Daten in ein 2D-`numpy`-Array zu konvertieren!")
```

---

## Baseballdaten im 2D-Format

```yaml
type: NormalExercise
key: 5df25d0b7b
lang: python
xp: 100
skills:
  - 2
```

Du erkennst, dass es sinnvoller ist, all diese Daten in einem 2D-`numpy`-Array zu organisieren.

Du hast eine Python-Liste, deren Elemente ebenfalls Listen sind. In dieser Liste aus Listen enthält jede Unterliste die Körpergröße und das Gewicht eines einzelnen Baseballspielers. Der Name dieser Liste ist `baseball` und sie wurde bereits für dich geladen (obwohl du sie nicht sehen kannst).

Speichere die Daten als 2D-Array, um die zusätzlichen Funktionen von `numpy` nutzen zu können.

`@instructions`
- Verwende `np.array()`, um ein 2D `numpy`-Array aus `baseball` zu erstellen. Nenne es `np_baseball`.
- Gib das `shape`-Attribut von `np_baseball` aus.

`@hint`
- `baseball` ist bereits in der Python-Umgebung verfügbar. Rufe `np.array()` damit auf und speichere das resultierende 2D `numpy`-Array in `np_baseball`.
- `np_baseball.shape` liefert die Dimensionen von `np_baseball`. Vergiss nicht den `print()`-Aufruf!

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

success_msg("Super! Zeit, einige coole Funktionen von mehrdimensionalen `numpy`-Arrays zu zeigen!")
```

---

## Elemente von 2D-NumPy-Arrays abrufen

```yaml
type: NormalExercise
key: aeca4977f0
lang: python
xp: 100
skills:
  - 2
```

Wenn dein 2D-`numpy`-Array eine regelmäßige Struktur hat (das heißt, jede Zeile und Spalte hat eine feste Anzahl von Werten), wird der bisher komplizierte Zugriff auf einzelne Elemente ganz einfach. Sieh dir folgenden Code an, in dem die Elemente `"a"` und `"c"` aus einer Liste, die wiederum aus Listen besteht, extrahiert werden.

```
# numpy
import numpy as np
np_x = np.array(x)
np_x[:, 0]
```

Indexwerte vor dem Komma beziehen sich auf die Zeilen, während Indexwerte nach dem Komma auf die Spalten verweisen. Der `:` dient dem Slicing; in diesem Beispiel weist er Python an, alle Zeilen einzuschließen.

`@instructions`
- Gib die 50. Zeile von `np_baseball` aus.
- Erstelle eine neue Variable namens `np_weight_lb`, welche die gesamte zweite Spalte von `np_baseball` enthält.
- Rufe die Körpergröße (erste Spalte) des 124. Baseballspielers in `np_baseball` ab und gib sie aus.

`@hint`
- Du brauchst den Zeilenindex 49 für die erste Aufgabe. Um genau zu sein, solltest du `[49, :]` verwenden.
- Um die gesamte zweite Spalte auszuwählen, brauchst du `[:, 1]`.
- Nutze `[123, 0]` für die letzte Aufgabe. Vergiss nicht, das Ganze in eine `print()`-Anweisung zu packen.

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
msg = "Du musst die vordefinierten Variablen nicht ändern oder entfernen."
Ex().multi(
    has_import("numpy", same_as = False),
    check_object("np_baseball", missing_msg=msg).has_equal_value(incorrect_msg = msg)
)

Ex().has_printout(0)

Ex().check_object('np_weight_lb').has_equal_value(incorrect_msg = "Du kannst `np_baseball[:,1]` verwenden, um `np_weight_lb` zu definieren. Dies wird die gesamte erste Spalte auswählen.")

Ex().has_printout(1)

success_msg("Das läuft gut!")
```

---

## 2D-Arithmetik

```yaml
type: NormalExercise
key: 1c2378b677
lang: python
xp: 100
skills:
  - 2
```

2D-`numpy`-Arrays können elementweise Berechnungen durchführen, wie auch `numpy`-Arrays.

`np_baseball` ist bereits codiert. Es ist wieder ein 2D-`numpy`-Array mit drei Spalten für die Körpergröße (in Zoll), das Gewicht (in Pfund) und das Alter (in Jahren). `baseball` ist eine reguläre Liste aus Listen. Und `updated` ist ein 2D-NumPy-Array.

`@instructions`
- Du bist an die Daten zu Änderungen bei Körpergröße, Gewicht und Alter aller Baseballspieler gelangt. Diese Daten liegen als 2D-`numpy`-Array namens `updated` vor. Füge `np_baseball` und `updated` zusammen und gib das Ergebnis aus.
- Du möchtest die Maßeinheiten für Körpergröße und Gewicht in metrische Einheiten (Meter bzw. Kilogramm) umrechnen. Im ersten Schritt erstellst du ein `numpy`-Array mit drei Werten: `0.0254`, `0.453592` und `1`. Nenne das Array `conversion`.
- Multipliziere `np_baseball` mit `conversion` und gib das Ergebnis aus.

`@hint`
- `np_baseball + updated` führt eine elementweise Addition der beiden `numpy`-Arrays durch.
- Erstelle ein `numpy`-Array mit `np.array()`. Die Eingabe ist eine reguläre Python-Liste mit drei Elementen.
- `np_baseball * conversion` funktioniert ohne zusätzlichen Aufwand. Probiere es aus! Und denke an den `print()`-Aufruf!

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

msg = "Du musst die vordefinierten Variablen nicht ändern oder entfernen."
Ex().check_object("np_baseball", missing_msg=msg).has_equal_value(incorrect_msg=msg)

Ex().has_printout(0)

Ex().check_correct(
    has_printout(1),
    check_correct(
        check_object('conversion').has_equal_value(),
        check_function('numpy.array', index=1).check_args(0).has_equal_value()
    )    
)

success_msg("Großartige Arbeit! Beachte, wie du mit sehr wenig Code alle Werte in deiner `numpy`-Datenstruktur auf eine sehr spezifische Weise ändern kannst. Das wird in deiner Zukunft als Datenwissenschaftler sehr nützlich sein!")
```

---

## NumPy: Grundlegende Statistiken

```yaml
type: VideoExercise
key: 287995e488
xp: 50
```

`@projector_key`
34495ba457d74296794d2a122c9b6e19

---

## Durchschnitt versus Median

```yaml
type: NormalExercise
key: 509c588eb6
lang: python
xp: 100
skills:
  - 2
```

Du weißt jetzt, wie du die Funktionen von `numpy` nutzen kannst, um deine Daten besser zu verstehen. 

Die Baseballdaten sind als 2D-`numpy`-Array mit 3 Spalten (Körpergröße, Gewicht, Alter) und 1015 Zeilen verfügbar. Der Name dieses `numpy`-Arrays ist `np_baseball`. Nachdem du die Daten umstrukturiert hast, stellst du jedoch fest, dass einige Größenangaben ungewöhnlich groß sind. Befolge die Anweisungen und finde heraus, welche zusammenfassende Kennzahl am besten geeignet ist, wenn du es mit sogenannten _Ausreißern_ zu tun hast. `np_baseball` ist bereits vorhanden.

`@instructions`
- Erstelle das `numpy`-Array `np_height_in`, das der ersten Spalte von `np_baseball` entspricht.
- Gib den Mittelwert von `np_height_in` aus.
- Gib den Median von `np_height_in` aus.

`@hint`
- Greife auf die Elemente des 2D-`numpy`-Arrays zu: `[:,0]` ist Teil der Lösung.
- Wenn `numpy` als `np` importiert wird, kannst du mit `np.mean()` den Mittelwert eines NumPy-Arrays berechnen. Vergiss nicht einen `print()`-Aufruf zu integrieren!
- Nutze `np.median()` für die letzte Aufgabe.

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

Ex().check_object("np_height_in").has_equal_value(incorrect_msg = "Du kannst `np_baseball[:,0]` verwenden, um die erste Spalte von `np_baseball` auszuwählen"),

Ex().check_correct(
    has_printout(0),
    check_function('numpy.mean').has_equal_value()
)

Ex().check_correct(
    has_printout(1),
    check_function('numpy.median').has_equal_value()
)

success_msg("Eine durchschnittliche Größe von 1586 Zoll, das klingt nicht richtig, oder? Allerdings scheint der Median nicht von den Ausreißern beeinflusst zu sein: 74 Zoll machen perfekt Sinn. Es ist immer eine gute Idee, sowohl den Median als auch den Mittelwert zu überprüfen, um eine Vorstellung von der gesamten Verteilung des gesamten Datensatzes zu bekommen.")
```

---

## Analyse der Baseballdaten

```yaml
type: NormalExercise
key: '4409948807'
lang: python
xp: 100
skills:
  - 2
```

Da der Mittelwert und der Median so weit auseinander liegen, beschließt du, dich bei der MLB zu beschweren. Man findet den Fehler und sendet dir die korrigierten Daten zu. Sie liegen wieder als 2D-NumPy-Array namens `np_baseball` mit drei Spalten vor.

Das Python-Skript im Editor enthält schon Code, um die informativen zusammenfassenden Kennzahlen auszugeben. `numpy` ist bereits als `np` geladen. Kannst du die Aufgabe vollenden? `np_baseball` ist verfügbar.

`@instructions`
- Der Code zum Ausgeben der durchschnittlichen Körpergröße ist bereits vorhanden. Vervollständige den Code für den Medianwert der Körpergröße.
- Verwende `np.std()` für die erste Spalte von `np_baseball`, um `stddev` zu berechnen. 
- Sind die großen Spieler tendenziell schwerer? Verwende `np.corrcoef()`, um die Korrelation zwischen der ersten und zweiten Spalte von `np_baseball` in `corr` zu speichern.

`@hint`
- Verwende `np.median()`, um den Median zu berechnen. Achte darauf, zuerst die richtige Spalte auszuwählen!
- Wähle für die Berechnung der Standardabweichung mit `np.std()` Daten aus derselben Spalte aus.
- Verwende `np_baseball[:, 0]` und `np_baseball[:, 1]`, um die erste und zweite Spalte auszuwählen, die als Eingaben für `np.corrcoef()` dienen.

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
msg = "Du solltest die vordefinierte Variable `avg` nicht ändern oder entfernen."
Ex().check_object("avg", missing_msg=msg).has_equal_value(incorrect_msg=msg)

missing = "Hast du `np.median()` verwendet, um den Median zu berechnen?"
incorrect = "Um `med` zu berechnen, übergib die erste Spalte von `np_baseball` an `numpy.median()`. Das Beispiel von `np.mean()` zeigt, wie es gemacht wird."
Ex().check_correct(
  check_object("med").has_equal_value(),
  check_function("numpy.median", index=0, missing_msg=missing).check_args(0).has_equal_value(incorrect_msg=incorrect)
)

missing = "Hast du `np.std()` verwendet, um die Standardabweichung zu berechnen?"
incorrect = "Um `stddev` zu berechnen, übergib die erste Spalte von `np_baseball` an `numpy.std()`. Das Beispiel von `np.mean()` zeigt, wie es gemacht wird."
Ex().check_correct(
  check_object("stddev").has_equal_value(),
  check_function("numpy.std", index=0, missing_msg=missing).check_args(0).has_equal_value(incorrect_msg=incorrect)
)

missing = "Hast du `np.corrcoef()` verwendet, um die Korrelation zu berechnen?"
incorrect1 = "Um `corr` zu berechnen, sollte das erste Argument von `np.corrcoef()` die erste Spalte von `np_baseball` sein, ähnlich wie zuvor."
incorrect2 = "Um `corr` zu berechnen, sollte das zweite Argument von `np.corrcoef()` die zweite Spalte von `np_baseball` sein. Anstelle von `[:,0]`, verwende diesmal `[:,1]`."
Ex().check_correct(
  check_object("corr").has_equal_value(),
  check_function("numpy.corrcoef", index=0, missing_msg=missing).multi(
    check_args(0, missing_msg=incorrect1).has_equal_value(incorrect_msg=incorrect1),
    check_args(1, missing_msg=incorrect2).has_equal_value(incorrect_msg=incorrect2)
  )
)

success_msg("Großartige Arbeit! Du hast eine solide Grundlage geschaffen - jetzt ist es an der Zeit, all deine neuen Data-Science-Fähigkeiten zu nutzen, um weitere Herausforderungen zu meistern und einen Unterschied zu machen.")
```

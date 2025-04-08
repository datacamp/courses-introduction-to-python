---
title_meta: "Kapitel\_3"
title: Funktionen und Pakete
description: >-
  Nun lernst du, wie du dir mithilfe von Funktionen, Methoden und Paketen Code
  zunutze machen kannst, der bereits von brillanten Python-Profis geschrieben
  wurde. Ziel ist es, die Menge an nötigem Code zu reduzieren, die du zum Lösen
  anspruchsvoller Probleme brauchst.
attachments:
  slides_link: 'https://projector-video-pdf-converter.datacamp.com/735/chapter3.pdf'
lessons:
  - nb_of_exercises: 4
    title: Funktionen
  - nb_of_exercises: 4
    title: Methoden
  - nb_of_exercises: 4
    title: Pakete
---

## Funktionen

```yaml
type: VideoExercise
key: 5c5f365930
xp: 50
```

`@projector_key`
1204d914b0e53100529827e07441ee6c

---

## Bekannte Funktionen

```yaml
type: NormalExercise
key: c422ee929b
lang: python
xp: 100
skills:
  - 2
```

Python bietet von Haus aus mehrere vordefinierte Funktionen, die dir das Leben als Data Scientist erleichtern. Zwei dieser Funktionen kennst du bereits: `print()` und `type()`. Es gibt auch Funktionen wie `str()`, `int()`, `bool()` und `float()`, um zwischen Datentypen zu wechseln. Du kannst dich [hier](https://docs.python.org/3/library/functions.html) über sie informieren [.](https://docs.python.org/3/library/functions.html) Auch das sind vordefinierte Funktionen.

Der Aufruf einer Funktion ist ganz einfach. Um den Typ von `3.0` zu ermitteln und die Ausgabe als neue Variable `result` zu speichern, kannst du folgenden Code verwenden:

```
result = type(3.0)
```

`@instructions`
- Verwende `print()` in Kombination mit `type()`, um den Typ von `var1` auszudrucken.
- Benutze `len()`, um die [Länge der Liste](https://docs.python.org/3/library/functions.html#len) `var1` zu erhalten. Verpacke ihn in einen `print()` Aufruf, um ihn direkt auszudrucken.
- Verwende `int()`, um `var2` in eine [ganze Zahl](https://docs.python.org/3/library/functions.html#int) umzuwandeln. Speichere das Ergebnis als `out2`.

`@hint`
- Rufe die Funktion `type()` wie folgt auf: `type(var1)`.
- Ruf `print()` an, wie du es schon so oft getan hast. Setze die Variable, die du ausgeben willst, einfach in Klammern.
- `int(x)` wandelt `x` in eine Ganzzahl um.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create variables var1 and var2
var1 = [1, 2, 3, 4]
var2 = True

# Print out type of var1
____

# Print out length of var1
____

# Convert var2 to an integer: out2
out2 = ____
```

`@solution`
```{python}
# Create variables var1 and var2
var1 = [1, 2, 3, 4]
var2 = True

# Print out type of var1
print(type(var1))

# Print out length of var1
print(len(var1))

# Convert var2 to an integer: out2
out2 = int(var2)
```

`@sct`
```{python}
msg = "Sie müssen die vordefinierten Variablen nicht ändern oder entfernen."
Ex().check_object("var1", missing_msg=msg).has_equal_value(incorrect_msg=msg)
Ex().check_object("var2", missing_msg=msg).has_equal_value(incorrect_msg=msg)

patt = "__JINJA__:Stellen Sie sicher, dass Sie den %s von `var1` mit `{{sol_call}}` ausgeben."
Ex().has_printout(0, not_printed_msg = patt % 'Typ')
Ex().has_printout(1, not_printed_msg = patt % 'Länge')

int_miss_msg = "Haben Sie `int()` verwendet, um eine Ganzzahl von `var2` zu erstellen?"
int_incorr_msg = "Haben Sie `var2` an `int()` übergeben?"
Ex().check_correct(
  check_object("out2").has_equal_value(incorrect_msg="Sie haben `int()` korrekt aufgerufen; stellen Sie nun sicher, dass Sie das Ergebnis dieses Aufrufs `out2` zuweisen."),
  check_function("int", missing_msg=int_miss_msg).has_equal_value(incorrect_msg=int_incorr_msg)
)
success_msg("Großartige Arbeit! Die `len()`-Funktion ist äußerst nützlich; sie funktioniert auch bei Zeichenfolgen, um die Anzahl der Zeichen zu zählen!")

```

---

## Hilfe!

```yaml
type: MultipleChoiceExercise
key: 679b852978
lang: python
xp: 50
skills:
  - 2
```

Vielleicht kennst du schon den Namen einer Python-Funktion, weißt aber noch nicht genau, wie du sie benutzen kannst? Dann musst du ironischerweise eine andere Funktion aufrufen, nämlich `help()`, um weitere Informationen zu deiner gewünschten Funktion zu erhalten. Speziell in IPython kannst du auch `?` vor dem Funktionsnamen verwenden.

Um zum Beispiel Hilfe zur Funktion `max()` zu erhalten, kannst du einen dieser Aufrufe verwenden:

```
help(max)
?max
```

Verwende die IPython Shell, um die [Dokumentation](https://docs.python.org/3/library/functions.html#pow) auf `pow()` zu öffnen. Gib dazu `?pow` oder `help(pow)` ein und drücke die **Eingabetaste**.

Welche der folgenden Aussagen ist richtig?

`@possible_answers`
- `pow()` nimmt drei Argumente: `base`, `exp` und `mod`. Fehlt `mod`, gibt die Funktion einen Fehler aus.
- `pow()` benötigt drei obligatorische Argumente: `base`, `exp` und `None`.
- `pow()` benötigt die Argumente `base` und `exp`; `mod` ist optional.
- `pow()` benötigt zwei Argumente: `exp` und `mod`. Fehlt `exp`, wird ein Fehler ausgegeben.

`@hint`
- Optionalen Argumenten wird ein Standardwert zugewiesen (`=`), den die Funktion verwendet, wenn das Argument nicht angegeben wird.

`@pre_exercise_code`
```{python}

```

`@sct`
```{python}
msg1 = "Nicht ganz. `mod` hat einen Standardwert, der verwendet wird, wenn Sie keinen Wert angeben."
msg2 = "Falsch. `None` ist der Standardwert für das Argument `mod`."
msg3 = "Perfekt! Die Verwendung von `help()` kann Ihnen helfen zu verstehen, wie Funktionen funktionieren, und ihr volles Potenzial freisetzen!"
msg4 = "Falsch. `pow()` nimmt drei Argumente, von denen eines einen Standardwert hat."
Ex().has_chosen(3, [msg1, msg2, msg3, msg4])
```

---

## Mehrere Argumente

```yaml
type: NormalExercise
key: e30486d7c1
lang: python
xp: 100
skills:
  - 2
```

In der vorigen Übung hast du mit der Funktion `help()` die Dokumentation aufgerufen und herausgefunden, welche Argumente einer Funktion optional sind. Nun machst du dir dies zunutze, um das Verhalten der Funktion `sorted()` zu beeinflussen.

Sieh dir die [Dokumentation](https://docs.python.org/3/library/functions.html#sorted) von `sorted()` an, indem du `help(sorted)` in der IPython Shell eingibst.

Du wirst sehen, dass `sorted()` drei Argumente entgegennehmen kann: `iterable`, `key` und `reverse`. In dieser Übung musst du nur `iterable` und `reverse` angeben, nicht `key`.

Es wurden bereits zwei Listen erstellt.

Kannst du sie zusammenfügen und in absteigender Reihenfolge sortieren?

`@instructions`
- Verwende `+`, um die Inhalte von `first` und `second` in einer neuen Liste namens `full` zusammenzufügen.
- Rufe `sorted()` mit der Liste `full` auf und gib für das Argument `reverse` den Wert `True` an. Speichere die sortierte Liste als `full_sorted`.
- Gib abschließend `full_sorted` aus.

`@hint`
- Addiere `first` und `second`, als ob es zwei Zahlen wären, und weise das Ergebnis `full` zu.
- Verwende `sorted()` mit zwei Eingaben: `full` und `reverse=True`.
- Um eine Variable auszugeben, verwende `print()`.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create lists first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# Paste together first and second: full
full = ____ + ____

# Sort full in descending order: full_sorted
full_sorted = ____

# Print out full_sorted
____
```

`@solution`
```{python}
# Create lists first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# Paste together first and second: full
full = first + second

# Sort full in descending order: full_sorted
full_sorted = sorted(full, reverse=True)

# Print out full_sorted
print(full_sorted)
```

`@sct`
```{python}
msg = "Sie müssen die bereits vorhandenen Variablen `first` und `second` nicht ändern oder entfernen."
Ex().multi(
  check_object("first", missing_msg=msg).has_equal_value(incorrect_msg=msg),
  check_object("second", missing_msg=msg).has_equal_value(incorrect_msg=msg)
)
Ex().check_correct(
  check_object("full_sorted").has_equal_value(incorrect_msg="Stellen Sie sicher, dass Sie das Ergebnis des Aufrufs von `sorted()` `full_sorted` zuweisen."),
  check_function("sorted").multi(
    check_args(0).has_equal_value(),
    check_args('reverse').has_equal_value()
  )
)

success_msg("Cool! Schauen Sie sich das Video zu Python-Methoden an.")
```

---

## Methoden

```yaml
type: VideoExercise
key: 2b66cb66b1
xp: 50
```

`@projector_key`
8e387776f3a264a745128b68aa8d8f83

---

## Methoden für Zeichenketten

```yaml
type: NormalExercise
key: 4039302ee0
lang: python
xp: 100
skills:
  - 2
```

Für Zeichenketten gibt es eine Reihe von Methoden. Folge den Anweisungen genau, um einige von ihnen kennenzulernen. Wenn du sie genauer kennenlernen möchtest, kannst du in der IPython Shell `help(str)` eingeben.

Die Zeichenkette `place` wurde bereits erstellt, sodass du mit ihr experimentieren kannst.

`@instructions`
- Verwende die [Methode](https://docs.python.org/3/library/stdtypes.html#str.upper) `.upper()` auf `place` und speichere das Ergebnis in `place_up`. Verwende die Syntax für den Aufruf von Methoden, die im vorigen Video vorgestellt wurde.
- Gib `place` und `place_up` aus. Haben sich beide Objekte verändert?
- Gib die Anzahl der o's auf der Variablen `place` aus, indem du `.count()` auf `place` aufrufst und den Buchstaben `'o'` als Eingabe an die Methode übergibst. Es geht hier um die Variable `place`, nicht um das Wort `"place"`!

`@hint`
- Du kannst die Methode `.upper()` auf `place` ohne weitere Eingaben aufrufen.
- Um eine Variable `x` auszugeben, kannst du `print(x)` schreiben.
- Achte darauf, dass du den Aufruf von `place.count(____)` in eine `print()` Funktion verpackst, damit du ihn ausdrucken kannst.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# string to experiment with: place
place = "poolhouse"

# Use upper() on place
place_up = 

# Print out place and place_up



# Print out the number of o's in place

```

`@solution`
```{python}
# string to experiment with: place
place = "poolhouse"

# Use upper() on place
place_up = place.upper()

# Print out place and place_up
print(place)
print(place_up)

# Print out the number of o's in place
print(place.count('o'))
```

`@sct`
```{python}
msg = "Sie müssen die vordefinierten Variablen nicht ändern oder entfernen."
Ex().check_object("place", missing_msg=msg).has_equal_value(incorrect_msg=msg)

patt = "Vergessen Sie nicht, `%s` auszugeben."
Ex().has_printout(0, not_printed_msg=patt % "place")
Ex().check_correct(
    has_printout(1, not_printed_msg=patt % "place_up"),
    check_correct(
        check_object("place_up").has_equal_value(incorrect_msg="Weisen Sie das Ergebnis Ihres `place.upper()`-Aufrufs `place_up` zu."),
        check_function("place.upper", signature=False)
    )
)    

# check count of place
Ex().check_correct(
  has_printout(2, not_printed_msg = "Sie haben die Anzahl der o's in `place` korrekt berechnet; stellen Sie nun sicher, dass Sie den `place.count('o')`-Aufruf in eine `print()`-Funktion einbetten, um das Ergebnis auszugeben."),
  check_function("place.count", signature=False).check_args(0).has_equal_value()
)

success_msg("Schön! Beachten Sie bei den Ausgaben, dass die `upper()`-Methode das Objekt, auf dem sie aufgerufen wird, nicht ändert. Dies wird bei Listen in der nächsten Übung anders sein!")

```

---

## Methoden für Listen

```yaml
type: NormalExercise
key: 0dbe8ed695
lang: python
xp: 100
skills:
  - 2
```

Zeichenketten sind nicht die einzigen Python-Typen, für die es spezifische Methoden gibt. Listen, Gleitkommazahlen, Ganzzahlen und boolesche Werte sind ebenfalls Typen, die über zahlreiche nützliche Methoden verfügen. In dieser Übung experimentierst du mit:

- `.index()`, um den Index des ersten Elements einer Liste zu erhalten, das mit der Eingabe übereinstimmt und
- `.count()`, um die Anzahl der Vorkommen eines Elements in einer Liste zu ermitteln.

Du nutzt wieder die Liste `areas` mit den Flächen verschiedener Räumlichkeiten eines Hauses.

`@instructions`
- Verwende die Methode `.index()`, um den Index des Elements in `areas` zu ermitteln, das gleich `20.0` ist. Gib den Index aus.
- Rufe `.count()` auf `areas` auf, um herauszufinden, wie oft `9.50` in der Liste erscheint. Dann gib das Ergebnis aus.

`@hint`
- Um den Index auszudrucken, verpackst du den Aufruf von `areas.index(___)` in eine `print()` Funktion.
- Um auszudrucken, wie oft ein Element `x` in der Liste vorkommt, verpacke den Aufruf von `areas.count(___)` in eine `print()` Funktion.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Print out the index of the element 20.0


# Print out how often 9.50 appears in areas

```

`@solution`
```{python}
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Print out the index of the element 20.0
print(areas.index(20.0))

# Print out how often 9.50 appears in areas
print(areas.count(9.50))
```

`@sct`
```{python}
predef_msg = "Sie müssen die vordefinierte Liste `areas` nicht ändern oder entfernen."

Ex().check_object("areas", missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg)

Ex().check_function("print", index=0).check_args(0).check_function('areas.index', signature=False).check_args(0).has_equal_value()

Ex().check_function("print", index=1).check_args(0).check_function('areas.count', signature=False).has_equal_value()

success_msg("Schön! Dies waren Beispiele für `list`-Methoden, die die Liste, auf die sie angewendet wurden, nicht verändert haben.")
```

---

## Methoden für Listen (2)

```yaml
type: NormalExercise
key: 1fbeab82d0
lang: python
xp: 100
skills:
  - 2
```

Die meisten Listenmethoden ändern die Liste, mit der sie aufgerufen werden. Beispiele sind:

- `.append()`die ein Element zu der Liste hinzufügt, auf der sie aufgerufen wird,
- `.remove()`die das erste Element einer Liste [entfernt](https://docs.python.org/3/library/stdtypes.html#typesseq-mutable), das mit der Eingabe übereinstimmt, und
- `.reverse()`die die Reihenfolge der Elemente in der Liste [umkehrt](https://docs.python.org/3/library/stdtypes.html#typesseq-mutable), auf der sie aufgerufen wird.

Auch hier nutzt du wieder die Liste `areas` mit den Flächen verschiedener Räumlichkeiten eines Hauses.

`@instructions`
- Verwende `.append()` zweimal, um die Größe des Poolhauses und der Garage zu addieren: `24.5` bzw. `15.45`. Achte auf die korrekte Reihenfolge!
- Gib `areas` aus.
- Verwende die Methode `.reverse()`, um die Reihenfolge der Elemente in `areas` umzukehren.
- Gib `areas` erneut aus.

`@hint`
- Für die erste Aufgabe musst du `areas.append(___)` zweimal aufrufen.
- Um eine Variable `x` auszugeben, schreibe `print(x)`.
- Die Methode `.reverse()` erfordert keine zusätzlichen Eingaben; verwende einfach die Punktschreibweise und leere Klammern: `.reverse()`.
- Um eine Variable `x` auszugeben, schreibe `print(x)`.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Use append twice to add poolhouse and garage size



# Print out areas


# Reverse the orders of the elements in areas


# Print out areas

```

`@solution`
```{python}
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Use append twice to add poolhouse and garage size
areas.append(24.5)
areas.append(15.45)

# Print out areas
print(areas)

# Reverse the orders of the elements in areas
areas.reverse()

# Print out areas
print(areas)
```

`@sct`
```{python}
Ex().multi(
  check_function("areas.append", index=0, signature=False).check_args(0).has_equal_value(),
  check_function("areas.append", index=1, signature=False).check_args(0).has_equal_value(),
  check_function("print", index=0).check_args(0).has_equal_ast(),
  check_function("areas.reverse", index=0, signature=False),
  check_function("print", index=1).check_args(0).has_equal_ast()
)

success_msg("Großartig!")

```

---

## Pakete

```yaml
type: VideoExercise
key: ab96a17c5e
xp: 50
```

`@projector_key`
cedcfb34350be8545599768f96695cdd

---

## Paket importieren

```yaml
type: NormalExercise
key: 7432a6376f
lang: python
xp: 100
skills:
  - 2
```

Nehmen wir an, du möchtest den Umfang und die Fläche eines Kreises berechnen. Folgende Formeln benötigst du:

$$C = 2 \pi r$$
$$A = \pi r^2 $$

Anstatt den Wert für `pi` einzugeben, kannst du das Paket `math` verwenden, das diesen Wert enthält.

Hinweis: `**` ist das Symbol für die Potenzierung. Ein Beispiel: `3**4` entspricht `3` hoch `4` und ergibt `81`.

`@instructions`
- Importiere das Paket `math`.
- Benutze `math.pi`, um den Umfang des Kreises zu berechnen, und speichere ihn in `C`.
- Benutze `math.pi`, um den Flächeninhalt des Kreises zu berechnen, und speichere ihn in `A`.

`@hint`
- Du kannst einfach `import math` verwenden und dann mit `math.pi` auf `pi` verweisen.
- Verwende die Formel aus dem Aufgabentext, um `C` zu berechnen. Nutze `*`.
- Verwende die Formel aus dem Aufgabentext, um `A` zu berechnen. Nutze `*` und `**`.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Import the math package
import ____

# Calculate C
C = 2 * 0.43 * ____

# Calculate A
A = ____ * 0.43 ** 2

print("Circumference: " + str(C))
print("Area: " + str(A))
```

`@solution`
```{python}
# Import the math package
import math

# Calculate C
C = 2 * 0.43 * math.pi

# Calculate A
A = math.pi * 0.43 ** 2

print("Circumference: " + str(C))
print("Area: " + str(A))
```

`@sct`
```{python}
patt = "Ihre Berechnung von `%s` ist nicht ganz korrekt. Stellen Sie sicher, dass Sie `math.pi` verwenden."
Ex().multi(
  has_import('math', same_as=False),
  check_object('C').has_equal_value(incorrect_msg=patt%'C'),
  check_object('A').has_equal_value(incorrect_msg=patt%'A')
)

Ex().multi(
  has_printout(0, not_printed_msg = "__JINJA__:Lassen Sie `{{sol_call}}` drin, um den Umfang auszugeben."),
  has_printout(1, not_printed_msg = "__JINJA__:Lassen Sie `{{sol_call}}` drin, um die Fläche auszugeben.")
)

success_msg("Schön! Wenn Sie wissen, wie man mit Funktionen aus Paketen umgeht, liegt die Macht vieler Python-Programmierer in Ihren Händen!")

```

---

## Selektiver Import

```yaml
type: NormalExercise
key: fe65eff50a
lang: python
xp: 100
skills:
  - 2
```

Normalerweise wird durch einen Import wie `import math` der **komplette** Funktionsumfang des Pakets `math` bereitgestellt. Wenn du jedoch nur einen bestimmten Teil eines Pakets verwenden möchtest, kannst du den Import selektiver gestalten:

```
from math import pi
```

Versuche es jetzt selbst und importiere diesmal nur `pi`.

`@instructions`
- Führe einen selektiven Import aus dem Paket `math` durch, bei dem du nur die Funktion `pi` importierst.
- Benutze `math.pi`, um den Umfang des Kreises zu berechnen, und speichere ihn in `C`.
- Benutze `math.pi`, um den Flächeninhalt des Kreises zu berechnen, und speichere ihn in `A`.

`@hint`
- Nutze `from math import pi` für den selektiven Import.
- Jetzt kannst du `pi` auch eigenständig verwenden.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Import pi function of math package
from math import ____

# Calculate C
C = 2 * 0.43 * ____

# Calculate A
A = ____ * 0.43 ** 2

print("Circumference: " + str(C))
print("Area: " + str(A))
```

`@solution`
```{python}
# Import pi function of math package
from math import pi

# Calculate C
C = 2 * 0.43 * pi

# Calculate A
A = pi * 0.43 ** 2

print("Circumference: " + str(C))
print("Area: " + str(A))
```

`@sct`
```{python}
patt = "Ihre Berechnung von `%s` ist nicht ganz korrekt. Stellen Sie sicher, dass Sie nur `pi` verwenden."

Ex().has_import("math.pi", not_imported_msg = "Stellen Sie sicher, dass Sie `pi` aus dem `math`-Paket importieren. Sie sollten die Notation `from ___ import ___` verwenden.",)

Ex().multi(
  check_object('C').has_equal_value(incorrect_msg=patt%'C'),
  check_object('A').has_equal_value(incorrect_msg=patt%'A')
)

Ex().multi(
  has_printout(0, not_printed_msg = "__JINJA__:Behalten Sie `{{sol_call}}` bei, um den Umfang auszugeben."),
  has_printout(1, not_printed_msg = "__JINJA__:Behalten Sie `{{sol_call}}` bei, um die Fläche auszugeben.")
)

success_msg("Schön! Gehen Sie zur nächsten Übung.")

```

---

## Unterschiedliche Arten des Imports

```yaml
type: MultipleChoiceExercise
key: f1b2675a2a
lang: python
xp: 50
skills:
  - 2
```

Es gibt verschiedene Möglichkeiten, Pakete und Module in Python zu importieren. Je nach Importbefehl musst du unterschiedlichen Python-Code verwenden.

Angenommen, du möchtest die [Funktion](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.inv.html) `inv()` verwenden, die sich im Unterpaket `linalg` des Pakets `scipy` befindet. Du möchtest diese Funktion wie folgt nutzen können:

```
my_inv([[1,2], [3,4]])
```

Welchen `import`-Befehl brauchst du, damit obiger Code ohne Fehler ausgeführt wird?

`@possible_answers`
- `import scipy`
- `import scipy.linalg`
- `from scipy.linalg import my_inv`
- `from scipy.linalg import inv as my_inv`

`@hint`
- Probiere die verschiedenen Import-Anweisungen in der IPython-Shell aus und sieh nach, welche dazu führt, dass die Zeile `my_inv([[1, 2], [3, 4]])` ohne Fehler läuft. Drücke die **Eingabetaste**, um den eingegebenen Code auszuführen.

`@pre_exercise_code`
```{python}

```

`@sct`
```{python}
msg1 = msg2 = msg3 = "Falsch, versuche es erneut. Probiere die verschiedenen Importanweisungen in der IPython-Shell aus und sieh, welche dazu führt, dass die Zeile `my_inv([[1, 2], [3, 4]])` ohne Fehler ausgeführt wird."
msg4 = "Korrekt! Das Wort `as` ermöglicht es Ihnen, einen lokalen Namen für die Funktion zu erstellen, die Sie importieren: `inv()` ist jetzt als `my_inv()` verfügbar."
Ex().has_chosen(4, [msg1, msg2, msg3, msg4])
```

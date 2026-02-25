---
title_meta: "Kapitel\_1"
title: Grundlagen von Python
description: >-
  Eine Einführung in die grundlegenden Konzepte von Python. Du lernst interaktiv
  und mithilfe eines Skripts, wie du Python nutzen kannst. Du erstellst deine
  ersten Variablen und machst dich mit den grundlegenden Datentypen von Python
  vertraut.
attachments:
  slides_link: 'https://projector-video-pdf-converter.datacamp.com/735/chapter1.pdf'
free_preview: true
lessons:
  - nb_of_exercises: 3
    title: Hallo Python!
  - nb_of_exercises: 5
    title: Variablen und Typen
---

## Hallo Python!

```yaml
type: VideoExercise
key: f644a48d5d
xp: 50
```

`@projector_key`
d8fcd4c930027fa4e1c3870c7e7e0ff1

---

## Dein erster Python-Code

```yaml
type: NormalExercise
key: bdc52f0e19
lang: python
xp: 100
skills:
  - 2
```

Es ist an der Zeit, deinen ersten Python-Code auszuführen!

Wechsle zum Codefenster und klicke auf die Schaltfläche „Code ausführen“, um die Ausgabe zu sehen.

`@instructions`
- Klicke auf die Schaltfläche „Code ausführen“, um zu sehen, was durch den Code `print(5 / 8)` ausgegeben wird.

`@hint`
- Führe den Code zuerst aus, bevor du deine Antwort abschickst, damit du dich mit der Ausgabe vertraut machen kannst.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Hit run code to see the output!
print(5 / 8)
```

`@solution`
```{python}
# Hit run code to see the output!
print(5 / 8)
```

`@sct`
```{python}
Ex().has_printout(0, not_printed_msg = "__JINJA__:Hast du `{{sol_call}}` verwendet, um `5 / 8` auszugeben?")
success_msg("Super! Weiter zum nächsten!")
```

---

## Python als Taschenrechner

```yaml
type: NormalExercise
key: 0f7c039428
lang: python
xp: 100
skills:
  - 2
```

Python ist perfekt dafür geeignet, um grundlegende Berechnungen durchzuführen. Möglich sind Addition, Subtraktion, Multiplikation und Division.

Der Code im Skript enthält einige Beispiele.

Nun bist du dran. Vervollständige den Code in der Übung.

`@instructions`
- Lasse das Ergebnis der Subtraktion – `5`minus`5` – im Abschnitt `# Subtraction` mit `print()` ausgeben.
- Lasse das Ergebnis der Multiplikation – `3`multipliziert mit`5` – im Abschnitt `# Multiplication` ausgeben.

`@hint`
- Du musst `print()` verwenden, um eine Ausgabe zu erzeugen.
- Du kannst mithilfe von `-` subtrahieren und mit `*` multiplizieren.

`@pre_exercise_code`
```{python}
 
```

`@sample_code`
```{python}
# Addition and division
print(4 + 5)
print(10 / 2)

# Subtraction
print()

# Multiplication

```

`@solution`
```{python}
# Addition and division
print(4 + 5)
print(10 / 2)

# Subtraction
print(5 - 5)

# Multiplication
print(3 * 5)
```

`@sct`
```{python}
Ex().has_printout(0, not_printed_msg = "Hast du `print(4 + 5)` verwendet, um das Ergebnis deiner Summe auszugeben?")

Ex().has_printout(1, not_printed_msg = "Hast du `print(5 - 5)` verwendet, um das Ergebnis deiner Subtraktion auszugeben?")

Ex().has_printout(2, not_printed_msg = "Hast du `print(3 * 5)` verwendet, um das Ergebnis deiner Multiplikation auszugeben?")

Ex().has_printout(3, not_printed_msg = "Hast du `print(10 / 2)` verwendet, um das Ergebnis deiner Division auszugeben?")

success_msg("Das ist korrekt! Python kann dir helfen, die Mathematik zu erledigen, eine Eigenschaft, die nützlich sein wird, wenn wir unsere Datenfähigkeiten erweitern.")
```

---

## Variablen und Typen

```yaml
type: VideoExercise
key: c2e396792e
xp: 50
```

`@projector_key`
433dcfcfedaee070cbf440491c402e3b

---

## Variablenzuweisung

```yaml
type: NormalExercise
key: 4bf65ad83e
lang: python
xp: 100
skills:
  - 2
```

Variablen ermöglichen es dir in Python, mittels Namen auf bestimmte Werte zu verweisen. Um eine Variable `x` mit dem Wert `5` zu deklarieren, wird `=` wie in diesem Beispiel genutzt:

```
x = 5
```

Du kannst nun den Namen dieser Variablen – `x` – anstelle des tatsächlichen Wertes (`5`) verwenden.

Denk daran, dass in Python mit `=` keine Gleichheitsprüfung durchgeführt wird, sondern eine _Zuweisung_ erfolgt! Teste es in dieser Übung nun selbst, indem du `____` durch deinen Code ersetzt.

`@instructions`
- Deklariere die Variable `savings` („Ersparnisse“) und weise ihr den Wert `100` zu.
- Prüfe den Wert dieser Variable mittels `print(savings)` im Skript.

`@hint`
- Gib `savings = 100` ein, um die Variable `savings` zu deklarieren.
- Nachdem du die Variable `savings` deklariert hast, kannst du `print(savings)` eingeben.
- Dein fertiger Code sollte den Platzhalter `____` nicht mehr enthalten.

`@pre_exercise_code`
```{python}
 
```

`@sample_code`
```{python}
# Create a variable savings
____

# Print out savings
____
```

`@solution`
```{python}
# Create a variable savings
savings = 100

# Print out savings
print(savings)
```

`@sct`
```{python}
Ex().check_object("savings").has_equal_value(incorrect_msg="Weise der Variablen `savings` den Wert `100` zu.")
Ex().has_printout(0, not_printed_msg = "Gib `savings`, die von dir erstellte Variable, mit `print(savings)` aus.")
success_msg("Super! Lass uns jetzt versuchen, einige Berechnungen mit dieser Variablen durchzuführen!")
```

---

## Berechnungen mit Variablen

```yaml
type: NormalExercise
key: ff06cedeb4
lang: python
xp: 100
skills:
  - 2
```

Da du jetzt eine Variable für deine „savings“ erstellt hast, wird es Zeit, mit dem Sparen anzufangen!

Anstatt mit tatsächlichen Werten zu rechnen, kannst du die Variablen verwenden.

Wie viel Geld hättest du in vier Monaten gespart, wenn du jeden Monat $10 zurückgelegt hättest?

`@instructions`
- Deklariere die Variable `monthly_savings` mit dem Wert `10` und die Variable `num_months` mit dem Wert `4`.
- Multipliziere `monthly_savings` mit `num_months` und weise das Ergebnis der Variablen `new_savings` zu.
- Gib den Wert von `new_savings` aus.

`@hint`
- Du kannst mit Variablen genauso rechnen wie mit Zahlen. Ersetze also bei `10 * 4` einfach die Zahlen durch die Variablen!
- Nutze `print()`, um den Wert von `new_savings` auszugeben.
- Achte darauf, dass du die Variablennamen richtig schreibst!

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create the variables monthly_savings and num_months



# Multiply monthly_savings and num_months
new_savings = ____

# Print new_savings

```

`@solution`
```{python}
# Create the variables monthly_savings and num_months
monthly_savings = 10
num_months = 4

# Multiply monthly_savings and num_months
new_savings = monthly_savings * num_months

# Print new_savings
print(new_savings)
```

`@sct`
```{python}
Ex().check_object("monthly_savings").has_equal_value(incorrect_msg = "Hast du `10` in `monthly_savings` mit `monthly_savings = 10` gespeichert?")
Ex().check_object("num_months").has_equal_value(incorrect_msg = "Hast du `4` in `num_months` mit `num_months = 4` gespeichert?")
Ex().check_object("new_savings").has_equal_value(incorrect_msg = "Hast du die richtigen Variablen und Symbole zum Multiplizieren verwendet? Erwartet wurde `monthly_savings * num_months`, aber es wurde etwas anderes erhalten.")
# Ex().check_object("total_savings").has_equal_value(incorrect_msg = "Hast du die richtigen Variablen und Symbole zum Addieren verwendet? Erwartet wurde `savings + new_savings`, aber es wurde etwas anderes erhalten.")

Ex().has_printout(0, not_printed_msg="Denk daran, `new_savings` am Ende deines Skripts auszugeben.")

success_msg("Du hast $40 an neuen Ersparnissen!")
```

---

## Andere Variablentypen

```yaml
type: NormalExercise
key: 006b48561f
lang: python
xp: 100
skills:
  - 2
```

In der vorigen Übung hast du den Python-Datentyp für Integer (Ganzzahlen) genutzt:

- `int` steht für „integer“: eine Ganzzahl ohne Bruchteil. Die Variable `savings` mit dem Wert `100` ist ein Beispiel für eine Ganzzahl.

Neben den numerischen Datentypen gibt es drei weitere häufig genutzte Datentypen:

- `float` steht für „floating point“: eine Gleitkommazahl, die einen ganzzahligen Teil und einen Bruchteil hat, der in Python durch einen Punkt abgetrennt wird. `1.1` ist ein Beispiel für eine Gleitkommazahl.
- `str` steht für „string“: eine Zeichenkette zur Darstellung von Text. Du kannst einfache oder doppelte Anführungszeichen verwenden, um einen String zu erstellen.
- `bool` steht für „boolean“: ein Datentyp zur Darstellung logischer Werte. Zulässig sind nur die Werte `True` und `False`. Die Großschreibung ist wichtig!

`@instructions`
- Deklariere eine neue Gleitkommazahl `half` mit dem Wert `0.5`.
- Deklariere eine neue Zeichenkette `intro` mit dem Wert `"Hello! How are you?"`.
- Deklariere einen neuen booleschen Wert `is_good` mit dem Wert `True`.

`@hint`
- Um eine Variable in Python zu deklarieren und ihr einen Wert zuzuweisen, wird `=` genutzt. Achte darauf, dass du deine Zeichenkette in einfache oder doppelte Anführungszeichen einschließt.
- In Python gibt es nur zwei boolesche Werte: `True` und `False`. `TRUE`, `true`, `FALSE`, `false` und andere Schreibweisen werden nicht akzeptiert.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create a variable half


# Create a variable intro


# Create a variable is_good

```

`@solution`
```{python}
# Create a variable half
half = 0.5

# Create a variable intro
intro = "Hello! How are you?"

# Create a variable is_good
is_good = True
```

`@sct`
```{python}
Ex().check_object("half").has_equal_value(incorrect_msg = "Hast du die Fließkommazahl `0.5` in `half` gespeichert?")

Ex().check_object("intro").has_equal_value(incorrect_msg = "Hmm, etwas stimmt mit deiner `intro`-Variable nicht. Überprüfe die Rechtschreibung und stelle sicher, dass du Anführungszeichen verwendet hast.")

Ex().check_object("is_good").has_equal_value(incorrect_msg = "Hast du den booleschen Wert großgeschrieben? Denke daran, dass du hier keine Anführungszeichen verwenden musst.")

success_msg("Schön!")
```

---

## Operationen mit anderen Typen

```yaml
type: BulletExercise
key: 4d0d83cc02
xp: 100
```

In Python gibt es verschiedene Variablentypen. Nutze `type()`, um den Typ einer Variablen zu ermitteln. Den Typ von `a` erfährst du zum Beispiel mit: `type(a)`.

Die verschiedenen Datentypen verhalten sich in Python unterschiedlich. Beispielsweise läuft die Addition von zwei Zeichenketten anders ab als die Addition von zwei Ganzzahlen oder zwei booleschen Werten.

Teste es jetzt selbst!

`@pre_exercise_code`
```{python}

```

***

```yaml
type: NormalExercise
key: f4e91c4ae9
xp: 50
```

`@instructions`
- Addiere `savings` und `new_savings` und weise das Ergebnis der Variablen `total_savings` zu.
- Verwende `type()`, um den Datentyp von `total_savings` auszugeben.

`@hint`
- Weise `savings + new_savings` einer neuen Variablen namens `total_savings` zu.
- Um den Typ einer Variablen `x` auszugeben, benutze `print(type(x))`.

`@sample_code`
```{python}
savings = 100
new_savings = 40

# Calculate total_savings using savings and new_savings
____
print(total_savings)

# Print the type of total_savings
print(____)
```

`@solution`
```{python}
savings = 100
new_savings = 40

# Calculate total_savings using savings and new_savings
total_savings = savings + new_savings
print(total_savings)

# Print the type of total_savings
print(type(total_savings))
```

`@sct`
```{python}
# predefined
msg = "You don't have to change or remove the predefined variables."

Ex().multi(
    check_object('savings', missing_msg=msg).has_equal_value(incorrect_msg=msg),
    check_object('new_savings', missing_msg=msg).has_equal_value(incorrect_msg=msg)
)

Ex().multi(
    check_object("total_savings").has_equal_value(incorrect_msg="Addiere `savings` und `new_savings`, um die Variable `total_savings` zu erstellen."),
    has_printout(1, not_printed_msg = "__JINJA__:Verwende `{{sol_call}}`, um den Typ von `total_savings` auszugeben.")
)
```

***

```yaml
type: NormalExercise
key: f54fbf9bd9
xp: 50
```

`@instructions`
- Berechne die Summe von `intro` und `intro` und weise das Ergebnis der Variablen `doubleintro` zu.
- Gib `doubleintro` aus. Hast du dieses Ergebnis erwartet?

`@hint`
- Weise `intro + intro` einer neuen Variablen namens `doubleintro` zu.
- Um eine Variable `x` auszugeben, schreibe `print(x)` im Skript.

`@sample_code`
```{python}
intro = "Hello! How are you?"

# Assign sum of intro and intro to doubleintro
____

# Print out doubleintro
print(____)
```

`@solution`
```{python}
intro = "Hello! How are you?"

# Assign sum of intro and intro to doubleintro
doubleintro = intro + intro

# Print out doubleintro
print(doubleintro)
```

`@sct`
```{python}
# predefined
msg = "Du musst die vordefinierten Variablen nicht ändern oder entfernen."

Ex().check_object('intro', missing_msg=msg).has_equal_value(incorrect_msg=msg)

Ex().multi(
    check_object("doubleintro").has_equal_value(incorrect_msg  = "Hast du das Ergebnis von `intro + intro` in `doubleintro` gespeichert?"),
    has_printout(0, not_printed_msg = "Vergiss nicht, `doubleintro` auszugeben.")
)

success_msg("Gut gemacht. Beachte, wie `intro + intro` dazu führt, dass `\"Hello! How are you?\"` und `\"Hello! How are you?\"` zusammengefügt werden.")
```

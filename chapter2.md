---
title_meta: "Kapitel\_2"
title: Listen in Python
description: "Du lernst, wie du Daten in Listen speicherst, auf sie zugreifst und sie bearbeitest\_– dies ist der erste Schritt, um mit großen Datenmengen effizient arbeiten zu können."
attachments:
  slides_link: 'https://projector-video-pdf-converter.datacamp.com/735/chapter2.pdf'
lessons:
  - nb_of_exercises: 4
    title: Listen in Python
  - nb_of_exercises: 4
    title: Listenelemente abrufen
  - nb_of_exercises: 5
    title: Listen manipulieren
---

## Listen in Python

```yaml
type: VideoExercise
key: a5886d213f
xp: 50
```

`@projector_key`
a0530c4542f10988847b2dbb91f717c3

---

## Eine Liste erstellen

```yaml
type: NormalExercise
key: e6c527bf41
lang: python
xp: 100
skills:
  - 2
```

Eine Liste ist ein **zusammengesetzter Datentyp**. Du kannst Werte gruppieren, etwa so:

```
a = "is"
b = "nice"
my_list = ["my", "list", a, b]
```

Nachdem du die Körpergrößen deiner Familienmitglieder erfasst hast, möchtest du nun einige Informationen zu dem Haus sammeln, in dem du wohnst. Die Flächen der verschiedenen Räumlichkeiten des Hauses werden in der Übung in separaten Variablen gespeichert.

`@instructions`
- Erstelle eine Liste namens `areas`, in der die Flächen von Flur (`hall`), Küche (`kit`), Wohnzimmer (`liv`), Schlafzimmer (`bed`) und Badezimmer (`bath`) in genau dieser Reihenfolge enthalten sind. Verwende die vordefinierten Variablen.
- Gib `areas` mit der Funktion `print()` aus.

`@hint`
- Du kannst die bereits deklarierten Variablen verwenden, um die Liste zu erstellen: `areas = [hall, kit, ...]`.
- Achte darauf, dass du eckige Klammern, also `[]`, und keine runden Klammern, `()`, verwendest.
- Um Variablen in einer Liste zu speichern, brauchst du keine Anführungszeichen zu verwenden.
- Schreibe `print(areas)`, damit die Liste beim Ausführen deines Codes ausgegeben wird.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Create list areas


# Print areas

```

`@solution`
```{python}
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Create list areas
areas = [hall, kit, liv, bed, bath]

# Print areas
print(areas)
```

`@sct`
```{python}
predef_msg = "Entferne oder bearbeite die vordefinierten Variablen nicht!"
areas_msg = "Definiere `areas` als die Liste, die alle Bereichsvariablen in der richtigen Reihenfolge enthält: `[hall, kit, liv, bed, bath]`. Achte auf Tippfehler. Die Liste sollte nichts anderes enthalten!"

Ex().check_correct(
    has_printout(0, not_printed_msg = "__JINJA__:Hast du `{{sol_call}}` verwendet, um die `areas`-Liste am Ende deines Skripts auszugeben?"),
    check_correct(
        check_object("areas").has_equal_value(incorrect_msg = areas_msg),
        multi(
            check_object('hall', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
            check_object('kit', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
            check_object('liv', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
            check_object('bed', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
            check_object('bath', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg)
        )
    )
)

success_msg("Super! Eine Liste ist hier viel besser, oder?")
```

---

## Listen mit verschiedenen Typen erstellen

```yaml
type: NormalExercise
key: 1702a8bcdc
lang: python
xp: 100
skills:
  - 2
```

Obwohl es unüblich ist, kann eine Liste gleichzeitig verschiedene Python-Datentypen wie Zeichenketten, Gleitkommazahlen und boolesche Werte enthalten.

Als Nächstes fügst du deiner Liste die Namen der Räumlichkeiten hinzu, damit du jeweils den Raumnamen und die zugehörige Größe leicht erkennen kannst.

Ein Teil des Codes wurde schon vorbereitet, damit du direkt loslegen kannst. Aber Achtung! `"bathroom"` ist eine Zeichenkette, während `bath` eine Variable ist und die Gleitkommazahl `9.50` repräsentiert, die du zuvor angegeben hast.

`@instructions`
- Ergänze den fehlenden Code, der die Liste `areas` erstellt. Strukturiere die Liste so, dass sie zuerst den Namen jedes Raums als Zeichenkette und dann die zugehörige Fläche enthält. Mit anderen Worten: Füge die Zeichenketten `"hallway"`, `"kitchen"` und `"bedroom"` an den richtigen Stellen ein.
- Gib `areas` erneut aus. Findest du die Ausgabe jetzt informativer?

`@hint`
- Die ersten vier Elemente der Liste `areas` sind `["hallway", hall, "kitchen", kit, ...`.
- Eine Zeichenkette muss in Anführungszeichen (`""`) gesetzt werden.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Adapt list areas
areas = [____, hall, ____, kit, "living room", liv, ____, bed, "bathroom", bath]

# Print areas
____
```

`@solution`
```{python}
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Adapt list areas
areas = ["hallway", hall, "kitchen", kit, "living room", liv, "bedroom", bed, "bathroom", bath]

# Print areas
print(areas)
```

`@sct`
```{python}
objs = ["hall", "kit", "liv", "bed", "bath"]
predef_msg = "Entferne oder bearbeite nicht die vordefinierten Variablen!"
areas_msg = "Du hast `areas` nicht den richtigen Wert zugewiesen. Schau dir die Anweisungen noch einmal an. Achte darauf, den Raumnamen jedes Mal vor die Variable mit der Fläche zu setzen. Die Reihenfolge ist hier wichtig! Pass auf Tippfehler auf."

Ex().check_correct(
  check_object("areas").has_equal_value(incorrect_msg = areas_msg),
  multi([ check_object(obj, missing_msg = predef_msg).has_equal_value(incorrect_msg = predef_msg) for obj in objs])
)

Ex().has_printout(0, not_printed_msg = "__JINJA__:Hast du `{{sol_call}}` verwendet, um die `areas`-Liste am Ende deines Skripts auszugeben?")

success_msg("Super! Diese Liste enthält sowohl Strings als auch Floats, aber das ist kein Problem für Python!")
```

---

## Liste aus Listen

```yaml
type: NormalExercise
key: 9158c577b0
lang: python
xp: 100
skills:
  - 2
```

Als Data Scientist wirst du es oft mit riesigen Datenmengen zu tun haben. Daher kann es sinnvoll sein, einige Daten zu gruppieren.

Anstatt eine Liste mit einem Mix aus Zeichenketten und Gleitkommazahlen für die Namen und Flächen der Räumlichkeiten im Haus zu erstellen, kannst du auch eine Liste erstellen, die weitere Listen enthält.

Zur Erinnerung: `"hallway"` ist eine Zeichenkette, während `hall` eine Variable ist und die Gleitkommazahl `11.25` repräsentiert, die du zuvor angegeben hast.

`@instructions`
- Vervollständige die Liste aus Listen mit den fehlenden Angaben für das Schlafzimmer und das Badezimmer. Achte auf die richtige Reihenfolge!
- Gib `house` aus. Erscheint dir diese Art der Datenstrukturierung sinnvoller?

`@hint`
- Füge der Liste `house` _Unterlisten_ hinzu, indem du `["bedroom", bed]` und `["bathroom", bath]` in eckigen Klammern ergänzt.
- Denk daran, nach jeder Unterliste ein Komma (`,`) zu setzen!
- Um eine Variable `x` auszugeben, schreibe `print(x)` auf eine neue Zeile.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# House information as list of lists
house = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv],
        ____,
        ____]

# Print out house
____
```

`@solution`
```{python}
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# House information as list of lists
house = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv],
         ["bedroom", bed],
         ["bathroom", bath]]

# Print out house
print(house)
```

`@sct`
```{python}
predef_msg = "Entferne oder bearbeite nicht die vordefinierten Variablen!"
house_msg = "Du hast `house` nicht den richtigen Wert zugewiesen. Schau dir die Anweisungen noch einmal an. Erweitere die Liste von Listen, sodass sie eine Liste für jedes Paar von Raumname und Raumfläche enthält. Achte auf die Reihenfolge und Tippfehler!"

Ex().check_correct(
    check_object("house").has_equal_value(incorrect_msg = house_msg),
    multi(
        check_object('hall', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
        check_object('kit', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
        check_object('liv', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
        check_object('bed', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
        check_object('bath', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg)
    )
)

Ex().has_printout(0, not_printed_msg = "__JINJA__:Hast du `{{sol_call}}` verwendet, um den Inhalt von `house` auszugeben?")

success_msg("Super! Mach dich bereit, mehr über das Unterteilen von Listen zu lernen!")
```

---

## Listenelemente abrufen

```yaml
type: VideoExercise
key: c076b5a69c
xp: 50
```

`@projector_key`
fc15ba5cb9485456df8589130b519ea3

---

## Teile und herrsche

```yaml
type: NormalExercise
key: c3ce582e32
lang: python
xp: 100
skills:
  - 2
```

Das Abrufen von Elementen aus Python-Listen ist ein Kinderspiel. Im folgenden Codebeispiel wird die Liste `x` erstellt und dann das Element „b“ abgerufen. Denk daran, dass der Index 1 auf das zweite Element der Liste verweist! Du kannst auch einen negativen Index verwenden.

```
x = ["a", "b", "c", "d"]
x[1]
x[-3] # same result!
```

Erinnerst du dich an die Liste `areas` von vorhin, die sowohl Zeichenketten als auch Gleitkommazahlen enthielt? Sie ist bereits im Skript deklariert. Kannst du den richtigen Code hinzufügen, um auf die gewünschten Elemente der Python-Liste zuzugreifen?

`@instructions`
- Gib das zweite Element der Liste `areas` aus. (Es hat den Wert `11.25`.)
- Greife auf das letzte Element von `areas` zu und gib es aus. (Es hat den Wert `9.50`.) Die Verwendung eines negativen Index ist hier sinnvoll.
- Wähle die Zahl aus, die der Fläche des Wohnzimmers entspricht (`20.0`) und gib sie aus.

`@hint`
- Verwende `x[1]`, um das zweite Element einer Liste `x` auszuwählen.
- Verwende `x[-1]`, um das letzte Element einer Liste `x` auszuwählen.
- Denk daran, deine Elementabfrage in einen `print()`-Aufruf zu packen.
- Die Zahl, die für die Fläche des Wohnzimmers steht, ist das sechste Element der Liste. Du brauchst also den Index `[5]`. `area[4]` würde die Zeichenkette anzeigen.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Print out second element from areas
print(areas[____])

# Print out last element from areas
print(areas[____])

# Print out the area of the living room
print(areas[____])
```

`@solution`
```{python}
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Print out second element from areas
print(areas[1])

# Print out last element from areas
print(areas[-1])

# Print out the area of the living room
print(areas[5])
```

`@sct`
```{python}
msg = "Entferne oder bearbeite nicht die vordefinierte Liste `areas`."
Ex().check_object("areas", missing_msg = msg).has_equal_value(incorrect_msg = msg)
Ex().has_printout(0, not_printed_msg = "Schau dir deinen Code noch einmal an, um das zweite Element in `areas` auszugeben, das sich an Index `1` befindet.")
Ex().has_printout(1, not_printed_msg = "Schau dir deinen Code noch einmal an, um das letzte Element in `areas` auszugeben, das sich an Index `-1` befindet.")
Ex().has_printout(2, not_printed_msg = "Schau dir deinen Code noch einmal an, um die Fläche des Wohnzimmers auszugeben. Sie befindet sich an Index `5`.")
success_msg("Gut gemacht!")
```

---

## Teillisten erstellen

```yaml
type: NormalExercise
key: 7f08642d18
lang: python
xp: 100
skills:
  - 2
```

Du kannst natürlich nicht nur einzelne Werte aus deiner Liste abrufen, sondern auch _Teillisten_ (Slices) erstellen, die aus mehreren Elementen deiner Liste bestehen. Verwende dazu folgende Syntax:

```
my_list[start:end]
```

Das Element, das dem `start`-Index entspricht, wird einbezogen, das Element an der Stelle des `end`-Index hingegen _nicht_. Diese Indexangaben können auch weggelassen werden. Wenn du den `start`-Index nicht angibst, geht Python davon aus, dass die Teilliste am Anfang der Liste beginnen soll.

`@instructions`
- Erstelle mittels Slicing eine Liste namens `downstairs` mit den ersten 6 Elementen von `areas`.
- Erstelle die Teilliste `upstairs` mit den letzten `4` Elementen von `areas`. Vereinfache diesmal den Code, indem du den `end`-Index weglässt.
- Gib sowohl `downstairs` als auch `upstairs` mit `print()` aus.

`@hint`
- Verwende eckige Klammern, also `[0:6]`, um die ersten sechs Elemente einer Liste zu erhalten.
- Um alle Elemente einer Liste `l` bis auf die ersten fünf Elemente zu erhalten, würdest du `l[5:]` verwenden.
- Füge zwei `print()`-Aufrufe hinzu, um `downstairs` und `upstairs` auszugeben.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Use slicing to create downstairs
downstairs = areas[____]

# Use slicing to create upstairs
upstairs = areas[____]

# Print out downstairs and upstairs
____
____
```

`@solution`
```{python}
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Use slicing to create downstairs
downstairs = areas[0:6]

# Use slicing to create upstairs
upstairs = areas[6:]

# Print out downstairs and upstairs
print(downstairs)
print(upstairs)
```

`@sct`
```{python}
msg = "Entferne oder bearbeite nicht die vordefinierte `areas`-Liste."
Ex().check_object("areas", missing_msg = msg).has_equal_value(incorrect_msg = msg)

patt = "`%s` ist falsch. Verwende `areas[%s]` und Slicing, um die gewünschten Elemente auszuwählen, oder etwas Gleichwertiges."
Ex().check_object("downstairs").has_equal_value(incorrect_msg = patt % ('downstairs', '0:6'))
Ex().check_object("upstairs").has_equal_value(incorrect_msg = patt % ("upstairs",":6"))

Ex().has_printout(0, not_printed_msg="Hast du `downstairs` ausgegeben, nachdem du es berechnet hast?")
Ex().has_printout(1, not_printed_msg="Hast du `upstairs` ausgegeben, nachdem du es berechnet hast?")

success_msg("Super!")
```

---

## Elemente von Listen innerhalb einer Liste abrufen

```yaml
type: NormalExercise
key: dbbbd306cf
xp: 100
```

Eine Python-Liste kann auch weitere Listen enthalten.

Um auf Elemente von Listen innerhalb einer Liste zuzugreifen, kannst du dieselbe Methode wie zuvor verwenden: eckige Klammern. Für die Liste `house` würde das wie folgt aussehen:

```
house[2][0]
```

`@instructions`
- Greife in der Liste `house` auf die Gleitkommazahl `9.5` zu.

`@hint`
- Löse diese Aufgabe Schritt für Schritt! Zuerst benötigst du das letzte Element der Liste `["bathroom", 9.50]`. Zur Erinnerung: Der Index des letzten Elements ist `-1`.
- Dann möchtest du auf das zweite Element von `["bathroom", 9.50]` zugreifen; es hat den Index `1`.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
house = [["hallway", 11.25],
         ["kitchen", 18.0],
         ["living room", 20.0],
         ["bedroom", 10.75],
         ["bathroom", 9.50]]

# Subset the house list
house___
```

`@solution`
```{python}
house = [["hallway", 11.25],
         ["kitchen", 18.0],
         ["living room", 20.0],
         ["bedroom", 10.75],
         ["bathroom", 9.50]]

# Subset the house list
house[-1][1]
```

`@sct`
```{python}
Ex().check_or(
  has_code("house[-1][1]", pattern=False),
  has_code("house[4][1]", pattern=False)
)

success_msg("Correctomundo! Das letzte Stück des Listenpuzzles ist die Manipulation.")
```

---

## Listen manipulieren

```yaml
type: VideoExercise
key: d7fe818b3a
xp: 50
```

`@projector_key`
355ed52d2fb0d67508c6a311b7cbc6d3

---

## Listenelemente ersetzen

```yaml
type: NormalExercise
key: 4e1bba1b55
lang: python
xp: 100
skills:
  - 2
```

Um Listenelemente zu ersetzen, greifst du auf die gewünschten Elemente zu und weist ihnen dann die neuen Werte zu. Du kannst einzelne Elemente auswählen oder ganze Listenabschnitte auf einmal ändern.

In dieser und den folgenden Übungen arbeitest du weiter mit der Liste `areas`, in der die Namen und Flächen der Räumlichkeiten eines Hauses enthalten sind.

`@instructions`
- Aktualisiere die Fläche des Badezimmers mit `10.50` Quadratmetern anstelle von `9.50`. Nutze dabei den negativen Index.
- Die Liste `areas` sollte cooler klingen! Ändere darum `"living room"` in `"chill zone"`. Verwende diesmal nicht den negativen Index.

`@hint`
- Um die Fläche des Badezimmers zu aktualisieren, greife auf das entsprechende Element in der Liste zu. (Tipp: Es ist das letzte!)
- Ersetze dann den Wert durch die neue Flächenangabe, indem du sie diesem Element zuweist.
- Führe dieselben Schritte aus, um den Namen `"living room"` zu aktualisieren, der den Index 4 hat.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Correct the bathroom area


# Change "living room" to "chill zone"

```

`@solution`
```{python}
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Correct the bathroom area
areas[-1] = 10.50

# Change "living room" to "chill zone"
areas[4] = "chill zone"
```

`@sct`
```{python}
bathroom_msg = 'Du kannst `areas[-1] = 10.50` verwenden, um die Badezimmerfläche zu aktualisieren.'
chillzone_msg = 'Du kannst `areas[4] = "chill zone"` verwenden, um den Namen des Wohnzimmers zu aktualisieren.'
Ex().check_correct(
  check_object('areas').has_equal_value(incorrect_msg = 'Deine Änderungen an `areas` haben nicht zur korrekten Liste geführt. Bist du sicher, dass du die richtigen Teilmengenoperationen verwendet hast? Wenn du unsicher bist, kannst du einen Hinweis verwenden!'),
  multi(
    has_equal_value(expr_code='areas[-1]', override=10.50, incorrect_msg = bathroom_msg),
    has_equal_value(expr_code='areas[4]', override='chill zone', incorrect_msg = chillzone_msg),
  )
)
success_msg('Super! Wie das Codebeispiel gezeigt hat, kannst du auch eine Liste schneiden und sie durch eine andere Liste ersetzen, um mehrere Elemente in einem einzigen Befehl zu aktualisieren.')
```

---

## Listen erweitern

```yaml
type: NormalExercise
key: ff0fe8d967
lang: python
xp: 100
skills:
  - 2
```

Wenn sich Elemente einer Liste ändern lassen, dann können doch sicher auch neue Elemente hinzugefügt werden, oder? Dazu kannst du den `+`-Operator verwenden:

```
x = ["a", "b", "c", "d"]
y = x + ["e", "f"]
```

Stell dir vor, du hast gerade im Lotto gewonnen. Wie toll! Darum möchtest du jetzt einen überdachten Pool und eine Garage bauen. Kannst du die entsprechenden Daten der Liste `areas` hinzufügen?

`@instructions`
- Verwende den Operator `+`, um die Listenelemente `["poolhouse", 24.5]` am Ende der Liste `areas` einzufügen. Speichere die resultierende Liste als `areas_1`.
- Erweitere die Liste `areas_1` nun mit den Daten zu deiner Garage. Füge die Zeichenkette `"garage"` und die Gleitkommazahl `15.45` hinzu. Nenne die resultierende Liste `areas_2`.

`@hint`
- Orientiere dich bei dieser Übung am Codebeispiel. `x` entspricht hier `areas` und `["e", "f"]` entspricht `["poolhouse", 24.5]`.
- Um weitere Elemente zu `areas_1` hinzuzufügen, benutze `areas_1 + ["element", 123]`.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create the areas list and make some changes
areas = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0,
         "bedroom", 10.75, "bathroom", 10.50]

# Add poolhouse data to areas, new list is areas_1
areas_1 = ____

# Add garage data to areas_1, new list is areas_2
areas_2 = ____
```

`@solution`
```{python}
# Create the areas list (updated version)
areas = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0,
         "bedroom", 10.75, "bathroom", 10.50]

# Add poolhouse data to areas, new list is areas_1
areas_1 = areas + ["poolhouse", 24.5]

# Add garage data to areas_1, new list is areas_2
areas_2 = areas_1 + ["garage", 15.45]
```

`@sct`
```{python}
msg = "Entferne oder bearbeite nicht die vordefinierte Liste `areas`."
Ex().check_object("areas", missing_msg = msg).has_equal_value(incorrect_msg = msg)
Ex().check_object("areas_1").has_equal_value(incorrect_msg = "Verwende `areas + [\"poolhouse\", 24.5]`, um `areas_1` zu erstellen. Achte auf Tippfehler!")
Ex().check_object("areas_2").has_equal_value(incorrect_msg = "Verwende `areas_1 + [\"garage\", 15.45]`, um `areas_2` zu erstellen. Achte auf Tippfehler!")
success_msg("Cool! Die Liste nimmt schön Form an!")
```

---

## Listenelemente löschen

```yaml
type: NormalExercise
key: 85f792356e
xp: 100
```

Zu guter Letzt kannst du auch Elemente aus deiner Liste entfernen. Nutze dazu die Anweisung `del`:

```
x = ["a", "b", "c", "d"]
del x[1]
```

Achtung: Sobald du ein Element aus einer Liste entfernst, ändern sich die Indexwerte aller nachfolgenden Elemente in der Liste!

Wie sich herausstellt, ist dein Lottogewinn nicht so hoch wie erwartet. Nun sieht es so aus, als könntest du den überdachten Pool doch nicht bauen. Diese Daten gehören also nicht mehr in die Liste. Mit anderen Worten: Du musst die entsprechende Zeichenkette und zugehörige Gleitkommazahl aus der Liste `areas` entfernen.

`@instructions`
- Lösche die Zeichenkette und zugehörige Gleitkommazahl für `"poolhouse"` aus deiner `areas`-Liste.
- Gib die aktualisierte Liste `areas` aus.

`@hint`
- Um zwei Elemente zu löschen, musst du `del` zweimal verwenden. Achte aber auf die korrekten Indexwerte!

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
areas = ["hallway", 11.25, "kitchen", 18.0,
        "chill zone", 20.0, "bedroom", 10.75,
         "bathroom", 10.50, "poolhouse", 24.5,
         "garage", 15.45]

# Delete the poolhouse items from the list


# Print the updated list

```

`@solution`
```{python}
areas = ["hallway", 11.25, "kitchen", 18.0,
        "chill zone", 20.0, "bedroom", 10.75,
         "bathroom", 10.50, "poolhouse", 24.5,
         "garage", 15.45]

# Delete the poolhouse items from the list
del areas[10]
del areas[10]

# Print the updated list
print(areas)
```

`@sct`
```{python}
Ex().check_or(
  multi(
    has_code("del areas[10]", pattern=False),
    has_code("del areas[10]", pattern=False)
  ),
  has_code("del areas[-4:-2]", pattern=False),
  has_code("del(areas[-4:-2])", pattern=False),
  multi(
    has_code("del(areas[10])", pattern=False),
    has_code("del(areas[10])", pattern=False)
  ),
  has_code("del areas[10:12]", pattern=False),
  has_code("del(areas[10:12])", pattern=False),
  multi(
    has_code("del areas[-4]", pattern=False),
    has_code("del areas[-3]", pattern=False)
  ),
  multi(
    has_code("del(areas[-4])", pattern=False),
    has_code("del(areas[-3])", pattern=False)
  )
)

Ex().has_printout(0, not_printed_msg="Hast du `areas` ausgegeben, nachdem du den Poolhouse-String und die Float entfernt hast?")
success_msg("Korrekt! Du wirst später einfachere Wege kennenlernen, um spezifische Elemente aus Python-Listen zu entfernen.")
```

---

## Funktionsweise von Listen

```yaml
type: NormalExercise
key: af72db9915
lang: python
xp: 100
skills:
  - 2
```

Für diese Übung haben wir schon Code für dich vorbereitet: eine Liste namens `areas` und eine Kopie der Liste namens `areas_copy`.

In dieser Codeversion wird das erste Element der Liste `areas_copy` geändert und dann die Liste `areas` ausgegeben. Durch Klick auf die Schaltfläche „Code ausführen“ siehst du, dass diese Änderung auch in der Liste `areas` auftaucht, obwohl du `areas_copy` geändert hast. Das liegt daran, dass `areas` und `areas_copy` auf dieselbe Liste verweisen.

Wenn du verhindern willst, dass Änderungen an `areas_copy` auch für `areas` übernommen werden, musst du eine echte Kopie der Liste `areas` mittels `list()` oder `[:]` erstellen.

`@instructions`
- Ändere den zweiten Befehl, der die Variable `areas_copy` deklariert, sodass `areas_copy` eine explizite Kopie von `areas` ist. Nach dieser Codeanpassung sollten sich Änderungen an `areas_copy` nicht mehr auf `areas` auswirken. Schicke deine Antwort ab, um dies zu überprüfen.

`@hint`
- Ändere die Zuweisung `areas_copy = areas`. Anstelle von `areas` kannst du auch `list(areas)` oder `areas[:]` zuweisen.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Change this command
areas_copy = areas

# Change areas_copy
areas_copy[0] = 5.0

# Print areas
print(areas)
```

`@solution`
```{python}
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Change this command
areas_copy = list(areas)

# Change areas_copy
areas_copy[0] = 5.0

# Print areas
print(areas)
```

`@sct`
```{python}
Ex().check_correct(
  check_object("areas_copy").has_equal_value(incorrect_msg = "Es scheint, dass `areas_copy` nicht korrekt aktualisiert wurde."),
  check_function("list", missing_msg = "Stelle sicher, dass du `list(areas)` verwendest, um eine `areas_copy` zu erstellen.")
)

mmsg = "Entferne nicht die vordefinierte Liste `areas`."
imsg = "Achte darauf, NUR die Kopie zu bearbeiten, nicht die ursprüngliche Liste `areas`. Schau dir die Übungsbeschreibung noch einmal an, wenn du dir nicht sicher bist, wie du eine Kopie erstellst."
Ex().check_correct(
  check_object("areas", missing_msg = mmsg).has_equal_value(incorrect_msg = imsg),
  check_function("list", missing_msg = "Stelle sicher, dass du `list(areas)` verwendest, um eine `areas_copy` zu erstellen.")
)

success_msg("Super! Der Unterschied zwischen expliziten und referenzbasierten Kopien ist subtil, kann aber wirklich wichtig sein. Versuche dir zu merken, wie eine Liste im Speicher des Computers gespeichert wird.")
```

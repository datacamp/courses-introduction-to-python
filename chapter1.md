---
title_meta: Hoofdstuk 1
title: Python-basics
description: >-
  Een introductie tot de basisconcepten van Python. Leer hoe je Python
  interactief gebruikt en met een script. Maak je eerste variabelen en maak
  kennis met de basistypen van Python.
attachments:
  slides_link: 'https://projector-video-pdf-converter.datacamp.com/735/chapter1.pdf'
free_preview: true
lessons:
  - nb_of_exercises: 3
    title: Hallo Python!
  - nb_of_exercises: 5
    title: Variabelen en types
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

## Je eerste Python-code

```yaml
type: NormalExercise
key: bdc52f0e19
lang: python
xp: 100
skills:
  - 2
```

Tijd om je eerste Python-code uit te voeren!

Ga naar de code en klik op de knop **Code uitvoeren** om de resultaten te zien.

`@instructions`
- Klik op de knop **Code uitvoeren** om de output van `print(5 / 8)` te zien.

`@hint`
- Voer eerst de code uit voordat je je antwoord verzendt, zodat je de resultaten kunt verkennen.

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
Ex().has_printout(0, not_printed_msg = "__JINJA__:Heb je `{{sol_call}}` gebruikt om `5 / 8` af te drukken?")
success_msg("Geweldig! Op naar de volgende!")
```

---

## Python als rekenmachine

```yaml
type: NormalExercise
key: 0f7c039428
lang: python
xp: 100
skills:
  - 2
```

Python is ideaal voor basisbewerkingen. Je kunt er mee optellen, aftrekken, vermenigvuldigen en delen.

De code in het script laat een paar voorbeelden zien.

Nu ben jij aan de beurt om te oefenen door zelf wat code te schrijven.

`@instructions`
- Print het resultaat van `5` min `5` onder `# Subtraction` met `print()`.
- Print het resultaat van `3` maal `5` onder `# Multiplication`.

`@hint`
- Je hebt `print()` nodig om een resultaat te tonen.
- Je kunt aftrekken met `-` en vermenigvuldigen met `*`.

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
Ex().has_printout(0, not_printed_msg = "Heb je `print(4 + 5)` gebruikt om het resultaat van je optelling af te drukken?")

Ex().has_printout(1, not_printed_msg = "Heb je `print(5 - 5)` gebruikt om het resultaat van je aftrekking af te drukken?")

Ex().has_printout(2, not_printed_msg = "Heb je `print(3 * 5)` gebruikt om het resultaat van je vermenigvuldiging af te drukken?")

Ex().has_printout(3, not_printed_msg = "Heb je `print(10 / 2)` gebruikt om het resultaat van je deling af te drukken?")

success_msg("Dat is correct! Python kan je helpen met rekenen, een eigenschap die nuttig zal zijn voor analyse terwijl we onze data-vaardigheden ontwikkelen.")
```

---

## Variabelen en types

```yaml
type: VideoExercise
key: c2e396792e
xp: 50
```

`@projector_key`
433dcfcfedaee070cbf440491c402e3b

---

## Variabele toewijzen

```yaml
type: NormalExercise
key: 4bf65ad83e
lang: python
xp: 100
skills:
  - 2
```

In Python kun je met een variabele naar een waarde verwijzen met een naam. Om een variabele `x` met de waarde `5` te maken, gebruik je `=`, zoals in dit voorbeeld:

```
x = 5
```

Je kunt nu de naam van deze variabele, `x`, gebruiken in plaats van de daadwerkelijke waarde, `5`.

Onthoud: `=` in Python betekent toewijzing; het test geen gelijkheid! Probeer het in de oefening door `____` te vervangen door je code.

`@instructions`
- Maak een variabele `savings` met de waarde `100`.
- Bekijk deze variabele door `print(savings)` in het script te typen.

`@hint`
- Typ `savings = 100` om de variabele `savings` te maken.
- Nadat je de variabele `savings` hebt gemaakt, kun je `print(savings)` typen.
- Je uiteindelijke code mag geen `____` bevatten.

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
Ex().check_object("savings").has_equal_value(incorrect_msg="Ken `100` toe aan de variabele `savings`.")
Ex().has_printout(0, not_printed_msg = "Print `savings`, de variabele die je hebt aangemaakt, met `print(savings)`.")
success_msg("Goed gedaan! Laten we nu wat berekeningen met deze variabele proberen te maken!")
```

---

## Rekenen met variabelen

```yaml
type: NormalExercise
key: ff06cedeb4
lang: python
xp: 100
skills:
  - 2
```

Je hebt nu een spaar-variabele gemaakt, dus laten we beginnen met sparen!

In plaats van met de daadwerkelijke waarden te rekenen, kun je variabelen gebruiken.

Hoeveel geld heb je over vier maanden gespaard als je elke maand $10 spaart?

`@instructions`
- Maak een variabele `monthly_savings` met de waarde `10` en `num_months` met de waarde `4`.
- Vermenigvuldig `monthly_savings` met `num_months` en sla dit op in `new_savings`.
- Print de waarde van `new_savings`.

`@hint`
- Je kunt met variabelen rekenen net zoals met getallen, dus in plaats van `10 * 4` vervang je de getallen door de variabelen!
- Gebruik `print()` om het bedrag in `new_savings` te zien.
- Let op dat je de variabelen correct spelt!

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
Ex().check_object("monthly_savings").has_equal_value(incorrect_msg = "Heb je `10` opgeslagen in `monthly_savings` met `monthly_savings = 10`?")
Ex().check_object("num_months").has_equal_value(incorrect_msg = "Heb je `4` opgeslagen in `num_months` met `num_months = 4`?")
Ex().check_object("new_savings").has_equal_value(incorrect_msg = "Heb je de juiste variabelen en symbolen gebruikt om te vermenigvuldigen? Verwacht `monthly_savings * num_months` maar kreeg iets anders.")
# Ex().check_object("total_savings").has_equal_value(incorrect_msg = "Heb je de juiste variabelen en symbolen gebruikt om op te tellen? Verwacht `savings + new_savings` maar kreeg iets anders.")

Ex().has_printout(0, not_printed_msg="Vergeet niet om `new_savings` aan het einde van je script af te drukken.")

success_msg("Je hebt $40 aan nieuwe besparingen!")
```

---

## Andere variabeletype

```yaml
type: NormalExercise
key: 006b48561f
lang: python
xp: 100
skills:
  - 2
```

In de vorige oefening werkte je met het Python-gegevenstype voor een geheel getal (integer):

- `int`, of integer: een getal zonder fractiegedeelte. `savings`, met de waarde `100`, is een voorbeeld van een integer.

Naast numerieke gegevenstypen zijn er drie andere veelvoorkomende typen:

- `float`, of floating point: een getal met zowel een geheel als een fractiegedeelte, gescheiden door een punt. `1.1` is een voorbeeld van een float.
- `str`, of string: een type om tekst voor te stellen. Je kunt enkele of dubbele aanhalingstekens gebruiken om een string te maken.
- `bool`, of boolean: een type om logische waarden voor te stellen. Het kan alleen `True` of `False` zijn (de hoofdletters zijn belangrijk!).

`@instructions`
- Maak een nieuwe float, `half`, met de waarde `0.5`.
- Maak een nieuwe string, `intro`, met de waarde `"Hello! How are you?"`.
- Maak een nieuwe boolean, `is_good`, met de waarde `True`.

`@hint`
- Om een variabele in Python te maken, gebruik je `=`. Zet je string tussen enkele of dubbele aanhalingstekens.
- In Python bestaan er maar twee booleaanse waarden: `True` en `False`. `TRUE`, `true`, `FALSE`, `false` en andere varianten worden niet geaccepteerd.

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
Ex().check_object("half").has_equal_value(incorrect_msg = "Heb je de float, `0.5` opgeslagen in `half`?")

Ex().check_object("intro").has_equal_value(incorrect_msg = "Hmm, er is iets mis met je `intro` variabele. Controleer de spelling en zorg ervoor dat je aanhalingstekens hebt gebruikt.")

Ex().check_object("is_good").has_equal_value(incorrect_msg = "Heb je de booleaanse waarde met een hoofdletter geschreven? Vergeet niet dat je hier geen aanhalingstekens hoeft te gebruiken.")

success_msg("Mooi!")
```

---

## Bewerkingen met andere types

```yaml
type: BulletExercise
key: 4d0d83cc02
xp: 100
```

Variabelen hebben in Python verschillende types. Je kunt het type van een variabele zien met `type()`. Om bijvoorbeeld het type van `a` te zien, voer je uit: `type(a)`.

Verschillende types gedragen zich anders in Python. Als je twee strings bij elkaar optelt, krijg je ander gedrag dan wanneer je twee gehele getallen of twee booleans optelt.

Tijd voor jou om dit uit te proberen.

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
- Tel `savings` en `new_savings` op en ken dit toe aan `total_savings`.
- Gebruik `type()` om het resulterende type van `total_savings` te printen.

`@hint`
- Ken `savings + new_savings` toe aan een nieuwe variabele, `total_savings`.
- Om het type van een variabele `x` te printen, gebruik je `print(type(x))`.

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
msg = "Je hoeft de vooraf gedefinieerde variabelen niet te wijzigen of te verwijderen."

Ex().multi(
    check_object('savings', missing_msg=msg).has_equal_value(incorrect_msg=msg),
    check_object('new_savings', missing_msg=msg).has_equal_value(incorrect_msg=msg)
)

Ex().multi(
    check_object("total_savings").has_equal_value(incorrect_msg="Voeg `savings` en `new_savings` toe om de variabele `total_savings` te maken."),
    has_printout(1, not_printed_msg = "__JINJA__:Gebruik `{{sol_call}}` om het type van `total_savings` af te drukken.")
)
```

***

```yaml
type: NormalExercise
key: f54fbf9bd9
xp: 50
```

`@instructions`
- Bereken de som van `intro` en `intro` en ken het resultaat toe aan `doubleintro`.
- Print `doubleintro`. Had je dit verwacht?

`@hint`
- Ken `intro + intro` toe aan een nieuwe variabele, `doubleintro`.
- Om een variabele `x` te printen, zet je `print(x)` in het script.

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
msg = "Je hoeft de vooraf gedefinieerde variabelen niet te wijzigen of te verwijderen."

Ex().check_object('intro', missing_msg=msg).has_equal_value(incorrect_msg=msg)

Ex().multi(
    check_object("doubleintro").has_equal_value(incorrect_msg  = "Heb je het resultaat van `intro + intro` opgeslagen in `doubleintro`?"),
    has_printout(0, not_printed_msg = "Vergeet niet om `doubleintro` af te drukken.")
)

success_msg("Mooi. Merk op hoe `intro + intro` ervoor zorgt dat `\"Hello! How are you?\"` en `\"Hello! How are you?\"` aan elkaar worden geplakt.")
```

---
title_meta: Hoofdstuk 3
title: Functies en pakketten
description: >-
  Je leert hoe je functies, methoden en pakketten gebruikt om slim te profiteren
  van code die briljante Python-ontwikkelaars al hebben geschreven. Het doel is
  om de hoeveelheid code te verkleinen die je nodig hebt om uitdagende problemen
  op te lossen!
attachments:
  slides_link: 'https://projector-video-pdf-converter.datacamp.com/735/chapter3.pdf'
lessons:
  - nb_of_exercises: 4
    title: Functies
  - nb_of_exercises: 4
    title: Methoden
  - nb_of_exercises: 4
    title: Packages
---

## Functies

```yaml
type: VideoExercise
key: 5c5f365930
xp: 50
```

`@projector_key`
1204d914b0e53100529827e07441ee6c

---

## Bekende functies

```yaml
type: NormalExercise
key: c422ee929b
lang: python
xp: 100
skills:
  - 2
```

Python heeft standaard een heleboel ingebouwde functies die je leven als data scientist makkelijker maken. Je kent er al twee: `print()` en `type()`. Er zijn ook functies zoals `str()`, `int()`, `bool()` en `float()` om tussen datatypes te wisselen. Je leest er [hier](https://docs.python.org/3/library/functions.html) meer over. Dit zijn ook ingebouwde functies.

Een functie aanroepen is eenvoudig. Om het type van `3.0` op te vragen en de uitvoer op te slaan in een nieuwe variabele, `result`, kun je het volgende doen:

```
result = type(3.0)
```

`@instructions`
- Gebruik `print()` in combinatie met `type()` om het type van `var1` te printen.
- Gebruik `len()` om de [lengte van de lijst](https://docs.python.org/3/library/functions.html#len) `var1` op te vragen. Verwerk dit in een `print()`-aanroep om het direct te printen.
- Gebruik `int()` om `var2` om te zetten naar een [integer](https://docs.python.org/3/library/functions.html#int). Sla de uitvoer op als `out2`.

`@hint`
- Roep de functie `type()` aan, zoals: `type(var1)`.
- Gebruik `print()` zoals je al zo vaak hebt gedaan. Zet gewoon de variabele die je wilt printen tussen haakjes.
- Met `int(x)` zet je `x` om naar een integer.

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
msg = "Je hoeft de vooraf gedefinieerde variabelen niet te wijzigen of te verwijderen."
Ex().check_object("var1", missing_msg=msg).has_equal_value(incorrect_msg=msg)
Ex().check_object("var2", missing_msg=msg).has_equal_value(incorrect_msg=msg)

patt = "__JINJA__:Zorg ervoor dat je het %s van `var1` afdrukt met `{{sol_call}}`."
Ex().has_printout(0, not_printed_msg = patt % 'type')
Ex().has_printout(1, not_printed_msg = patt % 'length')

int_miss_msg = "Heb je `int()` gebruikt om een geheel getal van `var2` te maken?"
int_incorr_msg = "Heb je `var2` doorgegeven aan `int()`?"
Ex().check_correct(
  check_object("out2").has_equal_value(incorrect_msg="Je hebt `int()` correct aangeroepen; zorg er nu voor dat je het resultaat van deze aanroep toewijst aan `out2`."),
  check_function("int", missing_msg=int_miss_msg).has_equal_value(incorrect_msg=int_incorr_msg)
)
success_msg("Goed gedaan! De `len()` functie is enorm handig; het werkt ook op strings om het aantal tekens te tellen!")
```

---

## Help!

```yaml
type: MultipleChoiceExercise
key: 679b852978
lang: python
xp: 50
skills:
  - 2
```

Misschien ken je de naam van een Python-functie al, maar moet je nog uitzoeken hoe je die gebruikt. Ironisch genoeg vraag je informatie over een functie op met een andere functie: `help()`. Specifiek in IPython kun je ook `?` voor de functienaam gebruiken.

Om bijvoorbeeld hulp te krijgen over de functie `max()`, kun je een van deze aanroepen gebruiken:

```
help(max)
?max
```

Gebruik de IPython-shell om de [documentatie](https://docs.python.org/3/library/functions.html#pow) van `pow()` te openen. Doe dit door `?pow` of `help(pow)` te typen en op **Enter** te drukken.

Welke van de volgende uitspraken is waar?

`@possible_answers`
- `pow()` neemt drie argumenten: `base`, `exp` en `mod`. Zonder `mod` geeft de functie een fout.
- `pow()` neemt drie verplichte argumenten: `base`, `exp` en `None`.
- `pow()` vereist de argumenten `base` en `exp`; `mod` is optioneel.
- `pow()` neemt twee argumenten: `exp` en `mod`. Ontbreekt `exp`, dan resulteert dat in een fout.

`@hint`
- Optionele argumenten krijgen met `=` een standaardwaarde, die de functie gebruikt als dat argument niet is opgegeven.

`@pre_exercise_code`
```{python}

```

`@sct`
```{python}
msg1 = "Niet helemaal. `mod` heeft een standaardwaarde die wordt gebruikt als je geen waarde opgeeft."
msg2 = "Onjuist. `None` is de standaardwaarde voor het `mod` argument."
msg3 = "Perfect! `help()` gebruiken kan je helpen te begrijpen hoe functies werken, waardoor je hun volledige potentieel kunt benutten!"
msg4 = "Onjuist. `pow()` neemt drie argumenten, waarvan er één een standaardwaarde heeft."
Ex().has_chosen(3, [msg1, msg2, msg3, msg4])
```

---

## Meerdere argumenten

```yaml
type: NormalExercise
key: e30486d7c1
lang: python
xp: 100
skills:
  - 2
```

In de vorige oefening heb je optionele argumenten herkend door de documentatie te bekijken met `help()`. Nu ga je dit toepassen om het gedrag van de functie `sorted()` aan te passen.

Bekijk de [documentatie](https://docs.python.org/3/library/functions.html#sorted) van `sorted()` door `help(sorted)` te typen in de IPython-shell.

Je ziet dat `sorted()` drie argumenten accepteert: `iterable`, `key` en `reverse`. In deze oefening hoef je alleen `iterable` en `reverse` op te geven, niet `key`.

Er zijn twee lijsten voor je aangemaakt.

Kun je ze aan elkaar plakken en in aflopende volgorde sorteren?

`@instructions`
- Gebruik `+` om de inhoud van `first` en `second` samen te voegen in een nieuwe lijst: `full`.
- Roep `sorted()` aan op `full` en geef het argument `reverse` de waarde `True`. Sla de gesorteerde lijst op als `full_sorted`.
- Rond af door `full_sorted` af te drukken.

`@hint`
- Tel `first` en `second` bij elkaar op alsof het twee getallen zijn en ken het resultaat toe aan `full`.
- Gebruik `sorted()` met twee inputs: `full` en `reverse=True`.
- Om een variabele af te drukken, gebruik je `print()`.

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
msg = "Je hoeft de al bestaande variabelen `first` en `second` niet te veranderen of te verwijderen."
Ex().multi(
  check_object("first", missing_msg=msg).has_equal_value(incorrect_msg=msg),
  check_object("second", missing_msg=msg).has_equal_value(incorrect_msg=msg)
)
Ex().check_correct(
  check_object("full_sorted").has_equal_value(incorrect_msg="Zorg ervoor dat je het resultaat van het aanroepen van `sorted()` toewijst aan `full_sorted`."),
  check_function("sorted").multi(
    check_args(0).has_equal_value(),
    check_args('reverse').has_equal_value()
  )
)

success_msg("Cool! Ga verder naar de video over Python-methoden.")
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

## String-methoden

```yaml
type: NormalExercise
key: 4039302ee0
lang: python
xp: 100
skills:
  - 2
```

Strings hebben allerlei handige methoden. Volg de instructies goed om er een paar te ontdekken. Wil je ze uitgebreider verkennen, typ dan `help(str)` in de IPython Shell.

Er is alvast een string `place` voor je aangemaakt om mee te experimenteren.

`@instructions`
- Gebruik de [methode](https://docs.python.org/3/library/stdtypes.html#str.upper) `.upper()` op `place` en sla het resultaat op in `place_up`. Gebruik de syntaxis voor het aanroepen van methoden die je in de vorige video hebt geleerd.
- Print `place` en `place_up`. Zijn ze allebei veranderd?
- Print het aantal o’s in de variabele `place` door `.count()` aan te roepen op `place` en de letter `'o'` mee te geven als invoer voor de methode. We bedoelen de variabele `place`, niet het woord `"place"`!

`@hint`
- Je kunt de methode `.upper()` aanroepen op `place` zonder extra invoer.
- Om een variabele `x` te printen, kun je `print(x)` schrijven.
- Zorg dat je je aanroep `place.count(____)` inpakt in een `print()`-functie zodat je het resultaat uitprint.

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
msg = "Je hoeft de vooraf gedefinieerde variabelen niet te wijzigen of te verwijderen."
Ex().check_object("place", missing_msg=msg).has_equal_value(incorrect_msg=msg)

patt = "Vergeet niet om `%s` af te drukken."
Ex().has_printout(0, not_printed_msg=patt % "place")
Ex().check_correct(
    has_printout(1, not_printed_msg=patt % "place_up"),
    check_correct(
        check_object("place_up").has_equal_value(incorrect_msg="Ken het resultaat van je `place.upper()`-aanroep toe aan `place_up`."),
        check_function("place.upper", signature=False)
    )
)    

# check count of place
Ex().check_correct(
  has_printout(2, not_printed_msg = "Je hebt het aantal o's in `place` goed berekend; zorg er nu voor dat je de aanroep `place.count('o')` in een `print()`-functie wikkelt om het resultaat af te drukken."),
  check_function("place.count", signature=False).check_args(0).has_equal_value()
)

success_msg("Mooi! Let op uit de afdrukken dat de `upper()`-methode het object waarop het wordt aangeroepen niet verandert. Dit zal anders zijn voor lijsten in de volgende oefening!")
```

---

## Lijstmethoden

```yaml
type: NormalExercise
key: 0dbe8ed695
lang: python
xp: 100
skills:
  - 2
```

Strings zijn niet de enige Python-typen die methoden hebben. Ook lijsten, floats, integers en booleans worden geleverd met allerlei handige methoden. In deze oefening ga je experimenteren met:

- `.index()`, om de index op te halen van het eerste element in een lijst dat overeenkomt met de invoer, en
- `.count()`, om te tellen hoe vaak een element in een lijst voorkomt.

Je werkt met de lijst met de oppervlakten van verschillende delen van een huis: `areas`.

`@instructions`
- Gebruik de methode `.index()` om de index op te halen van het element in `areas` dat gelijk is aan `20.0`. Print deze index.
- Roep `.count()` aan op `areas` om te achterhalen hoe vaak `9.50` in de lijst voorkomt. Print ook dit getal.

`@hint`
- Om de index af te drukken, zet je de aanroep `areas.index(___)` in een `print()`-functie.
- Om af te drukken hoe vaak een element `x` in de lijst voorkomt, zet je de aanroep `areas.count(___)` in een `print()`-functie.

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
predef_msg = "Je hoeft de vooraf gedefinieerde lijst `areas` niet te wijzigen of te verwijderen."

Ex().check_object("areas", missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg)

Ex().check_function("print", index=0).check_args(0).check_function('areas.index', signature=False).check_args(0).has_equal_value()


Ex().check_function("print", index=1).check_args(0).check_function('areas.count', signature=False).has_equal_value()

success_msg("Mooi! Dit waren voorbeelden van `list`-methoden die de lijst waarop ze werden aangeroepen niet veranderden.")
```

---

## Lijstmethoden (2)

```yaml
type: NormalExercise
key: 1fbeab82d0
lang: python
xp: 100
skills:
  - 2
```

De meeste lijstmethoden passen de lijst aan waarop ze worden aangeroepen. Voorbeelden zijn:

- `.append()`, die een element toevoegt aan de lijst waarop hij wordt aangeroepen,
- `.remove()`, die het eerste element van een lijst [verwijdert](https://docs.python.org/3/library/stdtypes.html#typesseq-mutable) dat overeenkomt met de invoer, en
- `.reverse()`, die de volgorde van de elementen in de lijst waarop hij wordt aangeroepen [omdraait](https://docs.python.org/3/library/stdtypes.html#typesseq-mutable).

Je werkt met de lijst met de oppervlakte van verschillende delen van het huis: `areas`.

`@instructions`
- Gebruik `.append()` twee keer om de grootte van het poolhouse en de garage opnieuw toe te voegen: `24.5` en `15.45`, respectievelijk. Zorg dat je ze in deze volgorde toevoegt.
- Print `areas` af
- Gebruik de methode `.reverse()` om de volgorde van de elementen in `areas` om te draaien.
- Print `areas` nog een keer af.

`@hint`
- Gebruik voor de eerste instructie twee keer de aanroep `areas.append(___)`.
- Om een variabele `x` af te drukken, schrijf je gewoon `print(x)`.
- De methode `.reverse()` heeft geen extra invoer nodig; gebruik gewoon de puntnotatie en lege haakjes: `.reverse()`.
- Om een variabele `x` af te drukken, schrijf je gewoon `print(x)`.

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

success_msg("Geweldig!")
```

---

## Packages

```yaml
type: VideoExercise
key: ab96a17c5e
xp: 50
```

`@projector_key`
cedcfb34350be8545599768f96695cdd

---

## Package importeren

```yaml
type: NormalExercise
key: 7432a6376f
lang: python
xp: 100
skills:
  - 2
```

Stel dat je de omtrek en oppervlakte van een cirkel wilt berekenen. De formules zien er zo uit:

$$C = 2 \pi r$$
$$A = \pi r^2 $$

In plaats van het getal voor `pi` zelf te typen, kun je het pakket `math` gebruiken waarin dit getal staat.

Ter herinnering: `**` is het symbool voor machtsverheffing. Bijvoorbeeld, `3**4` is `3` tot de macht `4` en geeft `81`.

`@instructions`
- Importeer het pakket `math`.
- Gebruik `math.pi` om de omtrek van de cirkel te berekenen en sla deze op in `C`.
- Gebruik `math.pi` om de oppervlakte van de cirkel te berekenen en sla deze op in `A`.

`@hint`
- Je kunt gewoon `import math` gebruiken en vervolgens naar `pi` verwijzen met `math.pi`.
- Gebruik de formule in de opdrachttekst om `C` te berekenen. Gebruik `*`.
- Gebruik de formule in de opdrachttekst om `A` te berekenen. Gebruik `*` en `**`.

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
patt = "Je berekening van `%s` is niet helemaal correct. Zorg ervoor dat je `math.pi` gebruikt."
Ex().multi(
  has_import('math', same_as=False),
  check_object('C').has_equal_value(incorrect_msg=patt%'C'),
  check_object('A').has_equal_value(incorrect_msg=patt%'A')
)

Ex().multi(
  has_printout(0, not_printed_msg = "__JINJA__:Houd `{{sol_call}}` erin om de omtrek af te drukken."),
  has_printout(1, not_printed_msg = "__JINJA__:Houd `{{sol_call}}` erin om de oppervlakte af te drukken.")
)

success_msg("Mooi! Als je weet hoe je met functies uit pakketten om moet gaan, ligt de kracht van veel Python-programmeurs binnen handbereik!")
```

---

## Selectief importeren

```yaml
type: NormalExercise
key: fe65eff50a
lang: python
xp: 100
skills:
  - 2
```

Algemene imports, zoals `import math`, maken **alle** functionaliteit uit het `math`-pakket voor je beschikbaar. Maar als je slechts een specifiek onderdeel van een pakket nodig hebt, kun je je import selectiever maken:

```
from math import pi
```

Probeer hetzelfde opnieuw, maar gebruik deze keer alleen `pi`.

`@instructions`
- Voer een selectieve import uit uit het `math`-pakket waarbij je alleen `pi` importeert.
- Gebruik `pi` om de omtrek van de cirkel te berekenen en sla die op in `C`.
- Gebruik `pi` om de oppervlakte van de cirkel te berekenen en sla die op in `A`.

`@hint`
- Gebruik `from math import pi` om selectief te importeren.
- Nu kun je `pi` los gebruiken!

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
patt = "Je berekening van `%s` is niet helemaal correct. Zorg ervoor dat je alleen `pi` gebruikt."

Ex().has_import("math.pi", not_imported_msg = "Zorg ervoor dat je `pi` uit het `math`-pakket importeert. Je moet de notatie `from ___ import ___` gebruiken.",)

Ex().multi(
  check_object('C').has_equal_value(incorrect_msg=patt%'C'),
  check_object('A').has_equal_value(incorrect_msg=patt%'A')
)

Ex().multi(
  has_printout(0, not_printed_msg = "__JINJA__:Houd `{{sol_call}}` erin om de omtrek af te drukken."),
  has_printout(1, not_printed_msg = "__JINJA__:Houd `{{sol_call}}` erin om de oppervlakte af te drukken.")
)

success_msg("Mooi! Ga verder naar de volgende oefening.")
```

---

## Verschillende manieren van importeren

```yaml
type: MultipleChoiceExercise
key: f1b2675a2a
lang: python
xp: 50
skills:
  - 2
```

Er zijn meerdere manieren om pakketten en modules in Python te importeren. Afhankelijk van de import-aanroep moet je andere Python-code gebruiken.

Stel dat je de [functie](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.inv.html) `inv()` wilt gebruiken, die in de subpackage `linalg` van het pakket `scipy` zit. Je wilt deze functie als volgt kunnen gebruiken:

```
my_inv([[1,2], [3,4]])
```

Welke `import`-instructie heb je nodig om de bovenstaande code zonder fout uit te voeren?

`@possible_answers`
- `import scipy`
- `import scipy.linalg`
- `from scipy.linalg import my_inv`
- `from scipy.linalg import inv as my_inv`

`@hint`
- Probeer de verschillende import-instructies in de IPython-shell en kijk welke ervoor zorgt dat de regel `my_inv([[1, 2], [3, 4]])` zonder fouten draait. Druk op **enter** om de code uit te voeren die je hebt getypt.

`@pre_exercise_code`
```{python}

```

`@sct`
```{python}
msg1 = msg2 = msg3 = "Onjuist, probeer het opnieuw. Probeer de verschillende importinstructies in de IPython-shell en kijk welke ervoor zorgt dat de regel `my_inv([[1, 2], [3, 4]])` zonder fouten wordt uitgevoerd."
msg4 = "Correct! Het woord `as` stelt je in staat om een lokale naam te maken voor de functie die je importeert: `inv()` is nu beschikbaar als `my_inv()`."
Ex().has_chosen(4, [msg1, msg2, msg3, msg4])
```

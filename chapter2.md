---
title_meta: Hoofdstuk 2
title: Python-lijsten
description: >-
  Leer gegevens in lijsten op te slaan, te openen en te bewerken: de eerste stap
  naar efficiënt werken met grote hoeveelheden data.
attachments:
  slides_link: 'https://projector-video-pdf-converter.datacamp.com/735/chapter2.pdf'
lessons:
  - nb_of_exercises: 4
    title: Python-lijsten
  - nb_of_exercises: 4
    title: Lijsten subsetten
  - nb_of_exercises: 5
    title: Lijsten manipuleren
---

## Python-lijsten

```yaml
type: VideoExercise
key: a5886d213f
xp: 50
```

`@projector_key`
a0530c4542f10988847b2dbb91f717c3

---

## Maak een lijst

```yaml
type: NormalExercise
key: e6c527bf41
lang: python
xp: 100
skills:
  - 2
```

Een lijst is een **samengesteld gegevenstype**; je kunt waarden groeperen, zoals hieronder:

```
a = "is"
b = "nice"
my_list = ["my", "list", a, b]
```

Na het meten van de lengte van je familie besluit je wat informatie te verzamelen over het huis waarin je woont. De oppervlaktes van de verschillende delen van je huis zijn in de oefening opgeslagen in aparte variabelen.

`@instructions`
- Maak een lijst, `areas`, die de oppervlakte bevat van de hal (`hall`), keuken (`kit`), woonkamer (`liv`), slaapkamer (`bed`) en badkamer (`bath`), in deze volgorde. Gebruik de vooraf gedefinieerde variabelen.
- Print `areas` met de functie `print()`.

`@hint`
- Je kunt de al aangemaakte variabelen gebruiken om de lijst op te bouwen: `areas = [hall, kit, ...]`.
- Zorg dat je vierkante haken `[]` gebruikt en geen ronde haken `()`.
- Je hoeft geen aanhalingstekens te gebruiken wanneer je variabelen in een lijst opslaat.
- Typ `print(areas)` om de lijst af te drukken wanneer je je antwoord indient.

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
predef_msg = "Verwijder of bewerk de vooraf gedefinieerde variabelen niet!"
areas_msg = "Definieer `areas` als de lijst die alle gebiedsvariabelen bevat, in de juiste volgorde: `[hall, kit, liv, bed, bath]`. Let op typefouten. De lijst mag niets anders bevatten!"

Ex().check_correct(
    has_printout(0, not_printed_msg = "__JINJA__:Heb je `{{sol_call}}` gebruikt om de `areas` lijst aan het einde van je script af te drukken?"),
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

success_msg("Mooi! Een lijst is hier veel beter, nietwaar?")
```

---

## Lijsten maken met verschillende typen

```yaml
type: NormalExercise
key: 1702a8bcdc
lang: python
xp: 100
skills:
  - 2
```

Hoewel het niet heel gebruikelijk is, kan een lijst ook een mix van Python-typen bevatten, zoals strings, floats en booleans.

Je gaat nu de kamernamen aan je lijst toevoegen, zodat je eenvoudig zowel de kamernaam als de oppervlakte bij elkaar ziet.

Een deel van de code is al voor je ingevuld zodat je kunt beginnen. Let op! `"bathroom"` is een string, terwijl `bath` een variabele is die staat voor de float `9.50` die je eerder hebt gedefinieerd.

`@instructions`
- Maak de code af die de lijst `areas` maakt. Bouw de lijst zo op dat eerst de naam van elke kamer als string komt en daarna de oppervlakte. Voeg met andere woorden de strings `"hallway"`, `"kitchen"` en `"bedroom"` op de juiste plekken toe.
- Print `areas` opnieuw; is de output nu informatiever?

`@hint`
- De eerste vier elementen van de lijst `areas` zijn gecodeerd als `["hallway", hall, "kitchen", kit, ...`.
- Een string moet tussen aanhalingstekens `""` staan.

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
predef_msg = "Verwijder of bewerk de vooraf gedefinieerde variabelen niet!"
areas_msg = "Je hebt niet de juiste waarde aan `areas` toegekend. Bekijk de instructies nog eens. Zorg ervoor dat je de naam van de kamer telkens voor de variabele met de oppervlakte plaatst. De volgorde is hier belangrijk! Let op typefouten."

Ex().check_correct(
  check_object("areas").has_equal_value(incorrect_msg = areas_msg),
  multi([ check_object(obj, missing_msg = predef_msg).has_equal_value(incorrect_msg = predef_msg) for obj in objs])
)

Ex().has_printout(0, not_printed_msg = "__JINJA__:Heb je `{{sol_call}}` gebruikt om de `areas` lijst aan het einde van je script af te drukken?")

success_msg("Mooi! Deze lijst bevat zowel strings als floats, maar dat is geen probleem voor Python!")
```

---

## Lijst van lijsten

```yaml
type: NormalExercise
key: 9158c577b0
lang: python
xp: 100
skills:
  - 2
```

Als data scientist werk je vaak met veel data en is het logisch om sommige gegevens te groeperen.

In plaats van één lijst te maken met strings en floats die de namen en oppervlaktes van de kamers in je huis voorstellen, kun je een lijst van lijsten maken.

Onthoud: `"hallway"` is een string, terwijl `hall` een variabele is die de float `11.25` voorstelt die je eerder hebt opgegeven.

`@instructions`
- Maak de lijst van lijsten af zodat deze ook de gegevens van de slaapkamer en badkamer bevat. Zorg dat je ze in de juiste volgorde invoert!
- Print `house`; is deze manier om je data te structureren logischer?

`@hint`
- Voeg _sublijsten_ toe aan de lijst `house` door `["bedroom", bed]` en `["bathroom", bath]` binnen de vierkante haken te zetten.
- Vergeet niet om na elke sublijst een komma `,` te plaatsen.
- Om een variabele `x` te printen, schrijf je `print(x)` op een nieuwe regel.

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
predef_msg = "Verwijder of bewerk de vooraf gedefinieerde variabelen niet!"
house_msg = "Je hebt niet de juiste waarde aan `house` toegewezen. Bekijk de instructies nog eens. Breid de lijst van lijsten uit zodat deze een lijst bevat voor elk paar van kamernaam en kameroppervlakte. Let op de volgorde en typfouten!"

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

Ex().has_printout(0, not_printed_msg = "__JINJA__:Heb je `{{sol_call}}` gebruikt om de inhoud van `house` af te drukken?")

success_msg("Geweldig! Maak je klaar om te leren over het subsetten van lijsten!")
```

---

## Lijsten subsetten

```yaml
type: VideoExercise
key: c076b5a69c
xp: 50
```

`@projector_key`
fc15ba5cb9485456df8589130b519ea3

---

## Subsetten en overwinnen

```yaml
type: NormalExercise
key: c3ce582e32
lang: python
xp: 100
skills:
  - 2
```

Subsets maken van Python-lijsten is kinderspel. Neem het onderstaande codevoorbeeld, waarin een lijst `x` wordt gemaakt en vervolgens "b" wordt geselecteerd. Onthoud dat dit het tweede element is, dus het heeft index 1. Je kunt ook negatieve indexering gebruiken.

```
x = ["a", "b", "c", "d"]
x[1]
x[-3] # zelfde resultaat!
```

Weet je de `areas`-lijst nog van eerder, met zowel strings als floats? De definitie staat al in het script. Kun je de juiste code toevoegen om wat Python-subsetting te doen?

`@instructions`
- Print het tweede element uit de `areas`-lijst (de waarde is `11.25`).
- Maak een subset en print het laatste element van `areas`, namelijk `9.50`. Een negatieve index is hier handig!
- Selecteer het getal dat de oppervlakte van de woonkamer voorstelt (`20.0`) en print het.

`@hint`
- Gebruik `x[1]` om het tweede element van een lijst `x` te selecteren.
- Gebruik `x[-1]` om het laatste element van een lijst `x` te selecteren.
- Zorg dat je je subsetting-bewerkingen in een `print()`-aanroep zet.
- Het getal dat de oppervlakte van de woonkamer voorstelt is het 6e element in de lijst, dus hier heb je `[5]` nodig. `area[4]` zou de string laten zien!

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
msg = "Verwijder of bewerk de vooraf gedefinieerde `areas`-lijst niet."
Ex().check_object("areas", missing_msg = msg).has_equal_value(incorrect_msg = msg)
Ex().has_printout(0, not_printed_msg = "Kijk nog eens naar je code om het tweede element in `areas` af te drukken, dat zich op index `1` bevindt.")
Ex().has_printout(1, not_printed_msg = "Kijk nog eens naar je code om het laatste element in `areas` af te drukken, dat zich op index `-1` bevindt.")
Ex().has_printout(2, not_printed_msg = "Kijk nog eens naar je code om de oppervlakte van de woonkamer af te drukken. Het bevindt zich op index `5`.")
success_msg("Goed gedaan!")
```

---

## Slicing en dicing

```yaml
type: NormalExercise
key: 7f08642d18
lang: python
xp: 100
skills:
  - 2
```

Enkele waarden selecteren uit een lijst is maar een deel van het verhaal. Je kunt je lijst ook _slicen_: meerdere elementen uit je lijst selecteren. Gebruik de volgende syntax:

```
my_list[start:end]
```

De `start`-index wordt meegenomen, terwijl de `end`-index _niet_ wordt meegenomen. Het is echter ook mogelijk om deze indexen weg te laten. Als je de `start`-index niet opgeeft, begrijpt Python dat je je slice aan het begin van je lijst wilt laten starten.

`@instructions`
- Gebruik slicing om een lijst `downstairs` te maken met de eerste 6 elementen van `areas`.
- Maak `upstairs` als de laatste `4` elementen van `areas`. Vereenvoudig de slice dit keer door de `end`-index weg te laten.
- Print zowel `downstairs` als `upstairs` met `print()`.

`@hint`
- Gebruik de haken `[0:6]` om de eerste zes elementen van een lijst op te halen.
- Om alles te krijgen behalve de eerste 5 elementen van een lijst `l`, gebruik je `l[5:]`.
- Voeg twee `print()`-aanroepen toe om `downstairs` en `upstairs` af te drukken.

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
msg = "Verwijder of bewerk de vooraf gedefinieerde `areas`-lijst niet."
Ex().check_object("areas", missing_msg = msg).has_equal_value(incorrect_msg = msg)

patt = "`%s` is onjuist. Gebruik `areas[%s]` en slicing om de elementen te selecteren die je wilt, of iets gelijkwaardigs."
Ex().check_object("downstairs").has_equal_value(incorrect_msg = patt % ('downstairs', '0:6'))
Ex().check_object("upstairs").has_equal_value(incorrect_msg = patt % ("upstairs",":6"))

Ex().has_printout(0, not_printed_msg="Heb je `downstairs` afgedrukt nadat je het hebt berekend?")
Ex().has_printout(1, not_printed_msg="Heb je `upstairs` afgedrukt nadat je het hebt berekend?")

success_msg("Geweldig!")
```

---

## Subsets maken van lijsten-van-lijsten

```yaml
type: NormalExercise
key: dbbbd306cf
xp: 100
```

Een Python-lijst kan ook andere lijsten bevatten.

Om lijsten-van-lijsten te subsetten, kun je dezelfde techniek gebruiken als eerder: vierkante haken. Voor een lijst `house` ziet dat er zo uit:

```
house[2][0]
```

`@instructions`
- Subset de lijst `house` om de float `9.5` te krijgen.

`@hint`
- Pak dit stap voor stap aan. Eerst wil je het laatste element van de lijst ophalen, `["bathroom", 9.50]`. Onthoud: de index van het laatste element is `-1`.
- Vervolgens wil je het tweede element van `["bathroom", 9.50]` krijgen, dat op index `1` staat.

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

success_msg("Correctomundo! Het laatste stukje van de lijstpuzzel is manipulatie.")
```

---

## Lijsten manipuleren

```yaml
type: VideoExercise
key: d7fe818b3a
xp: 50
```

`@projector_key`
355ed52d2fb0d67508c6a311b7cbc6d3

---

## Lijstelementen vervangen

```yaml
type: NormalExercise
key: 4e1bba1b55
lang: python
xp: 100
skills:
  - 2
```

Om lijstelementen te vervangen, maak je een subset van de lijst en wijs je nieuwe waarden toe aan die subset. Je kunt losse elementen selecteren of in één keer hele slices van de lijst veranderen.

Voor deze en de volgende oefeningen werk je verder met de lijst `areas`, die de namen en oppervlaktes van verschillende kamers in een huis bevat.

`@instructions`
- Werk de oppervlakte van de badkamer bij naar `10.50` vierkante meter in plaats van `9.50` met behulp van negatieve indexering.
- Maak de lijst `areas` wat hipper! Verander `"living room"` in `"chill zone"`. Gebruik deze keer geen negatieve indexering.

`@hint`
- Om de badkameroppervlakte bij te werken, selecteer je de subset van de badkamer (het is het laatste item van de lijst!).
- Vervang daarna de waarde door de nieuwe badkameroppervlakte door deze aan deze subset toe te kennen.
- Doe hetzelfde om de naam van `"living room"` te updaten, die op index 4 staat.

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
bathroom_msg = 'Je kunt `areas[-1] = 10.50` gebruiken om de badkameroppervlakte bij te werken.'
chillzone_msg = 'Je kunt `areas[4] = "chill zone"` gebruiken om de naam van de woonkamer bij te werken.'
Ex().check_correct(
  check_object('areas').has_equal_value(incorrect_msg = 'Je wijzigingen aan `areas` hebben niet geresulteerd in de juiste lijst. Weet je zeker dat je de juiste subset-bewerkingen hebt gebruikt? Als je twijfelt, kun je een hint gebruiken!'),
  multi(
    has_equal_value(expr_code='areas[-1]', override=10.50, incorrect_msg = bathroom_msg),
    has_equal_value(expr_code='areas[4]', override='chill zone', incorrect_msg = chillzone_msg),
  )
)
success_msg('Top! Zoals het codevoorbeeld liet zien, kun je ook een lijst slicen en deze vervangen door een andere lijst om meerdere elementen in één opdracht bij te werken.')
```

---

## Breid een lijst uit

```yaml
type: NormalExercise
key: ff0fe8d967
lang: python
xp: 100
skills:
  - 2
```

Als je elementen in een lijst kunt wijzigen, wil je ze vast ook kunnen toevoegen, toch? Je kunt hiervoor de operator `+` gebruiken:

```
x = ["a", "b", "c", "d"]
y = x + ["e", "f"]
```

Je hebt de loterij gewonnen, super! Je besluit een bijgebouw en een garage te bouwen. Kun je deze informatie toevoegen aan de lijst `areas`?

`@instructions`
- Gebruik de operator `+` om de lijst `["poolhouse", 24.5]` achteraan de lijst `areas` te plakken. Sla de resulterende lijst op als `areas_1`.
- Breid `areas_1` verder uit met gegevens over je garage. Voeg de string `"garage"` en de float `15.45` toe. Noem de resulterende lijst `areas_2`.

`@hint`
- Volg het codevoorbeeld in de opdracht. `x` is hier `areas`, en `["e", "f"]` is `["poolhouse", 24.5]`.
- Om meer elementen toe te voegen aan `areas_1`, gebruik je `areas_1 + ["element", 123]`.

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
msg = "Verwijder of bewerk de vooraf gedefinieerde `areas`-lijst niet."
Ex().check_object("areas", missing_msg = msg).has_equal_value(incorrect_msg = msg)
Ex().check_object("areas_1").has_equal_value(incorrect_msg = "Gebruik `areas + [\"poolhouse\", 24.5]` om `areas_1` te maken. Let op typefouten!")
Ex().check_object("areas_2").has_equal_value(incorrect_msg = "Gebruik `areas_1 + [\"garage\", 15.45]` om `areas_2` te maken. Let op typefouten!")
success_msg("Cool! De lijst begint er goed uit te zien!")
```

---

## Lijstelementen verwijderen

```yaml
type: NormalExercise
key: 85f792356e
xp: 100
```

Tot slot kun je ook elementen uit je lijst verwijderen. Dat kan met het `del`-statement:

```
x = ["a", "b", "c", "d"]
del x[1]
```

Let hier goed op: zodra je een element uit een lijst verwijdert, veranderen de indexen van alle elementen die na het verwijderde element komen!

Helaas blijkt het bedrag dat je met de loterij hebt gewonnen toch niet zo groot te zijn en lijkt het poolhouse er niet in te zitten. Je moet het uit de lijst verwijderen. Je besluit de bijbehorende string en float uit de `areas`-lijst te halen.

`@instructions`
- Verwijder de string en de float voor de `"poolhouse"` uit je `areas`-lijst.
- Print de bijgewerkte `areas`-lijst.

`@hint`
- Je moet `del` twee keer gebruiken om twee elementen te verwijderen. Let wel op: als je iets verwijdert, veranderen de indexen!

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

Ex().has_printout(0, not_printed_msg="Heb je `areas` afgedrukt nadat je de poolhouse string en float hebt verwijderd?")
success_msg("Correct! Je leert later over makkelijkere manieren om specifieke elementen uit Python-lijsten te verwijderen.")
```

---

## Hoe lijsten onder de motorkap werken

```yaml
type: NormalExercise
key: af72db9915
lang: python
xp: 100
skills:
  - 2
```

Er is alvast wat code voor je klaargezet: een lijst met de naam `areas` en een kopie genaamd `areas_copy`.

Op dit moment wordt het eerste element in de lijst `areas_copy` aangepast en wordt de lijst `areas` geprint. Als je op de knop **Code uitvoeren** drukt, zie je dat, hoewel je `areas_copy` hebt aangepast, de wijziging ook zichtbaar is in de lijst `areas`. Dat komt omdat `areas` en `areas_copy` naar dezelfde lijst verwijzen.

Als je wilt voorkomen dat wijzigingen in `areas_copy` ook effect hebben op `areas`, moet je een explicietere kopie van de lijst `areas` maken met `list()` of door `[:]` te gebruiken.

`@instructions`
- Pas het tweede commando aan, dat de variabele `areas_copy` maakt, zodat `areas_copy` een expliciete kopie is van `areas`. Na je wijziging mogen aanpassingen in `areas_copy` geen invloed hebben op `areas`. **Antwoord verzenden** om dit te controleren.

`@hint`
- Pas de aanroep `areas_copy = areas` aan. In plaats van `areas` toe te wijzen, kun je `list(areas)` of `areas[:]` toewijzen.

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
  check_object("areas_copy").has_equal_value(incorrect_msg = "Het lijkt erop dat `areas_copy` niet correct is bijgewerkt."),
  check_function("list", missing_msg = "Zorg ervoor dat je `list(areas)` gebruikt om een `areas_copy` te maken.")
)

mmsg = "Verwijder de vooraf gedefinieerde `areas` lijst niet."
imsg = "Zorg ervoor dat je ALLEEN de kopie bewerkt, niet de originele `areas` lijst. Bekijk de oefenbeschrijving nog eens als je niet zeker weet hoe je een kopie moet maken."
Ex().check_correct(
  check_object("areas", missing_msg = mmsg).has_equal_value(incorrect_msg = imsg),
  check_function("list", missing_msg = "Zorg ervoor dat je `list(areas)` gebruikt om een `areas_copy` te maken.")
)

success_msg("Mooi! Het verschil tussen expliciete en referentie-gebaseerde kopieën is subtiel, maar kan echt belangrijk zijn. Probeer te onthouden hoe een lijst in het geheugen van de computer wordt opgeslagen.")
```

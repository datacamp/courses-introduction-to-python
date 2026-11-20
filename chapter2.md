---
title_meta: Kapitel 2
title: Python-listor
description: >-
  Lär dig lagra, komma åt och bearbeta data i listor – det första steget mot att
  arbeta effektivt med stora datamängder.
attachments:
  slides_link: 'https://projector-video-pdf-converter.datacamp.com/735/chapter2.pdf'
lessons:
  - nb_of_exercises: 4
    title: Python-listor
  - nb_of_exercises: 4
    title: Indexering av listor
  - nb_of_exercises: 5
    title: Manipulera listor
---

## Pythonlistor

```yaml
type: VideoExercise
key: a5886d213f
xp: 50
```

`@projector_key`
a0530c4542f10988847b2dbb91f717c3

---

## Skapa en lista

```yaml
type: NormalExercise
key: e6c527bf41
lang: python
xp: 100
skills:
  - 2
```

En lista är en **sammansatt datatyp** – du kan gruppera värden tillsammans, så här:

```
a = "is"
b = "nice"
my_list = ["my", "list", a, b]
```

Efter att ha mätt upp längden på din familj bestämmer du dig för att samla lite information om huset du bor i. Arean för husets olika delar är lagrade i separata variabler i övningen.

`@instructions`
- Skapa en lista, `areas`, som innehåller arean för hallen (`hall`), köket (`kit`), vardagsrummet (`liv`), sovrummet (`bed`) och badrummet (`bath`), i den ordningen. Använd de fördefinierade variablerna.
- Skriv ut `areas` med funktionen `print()`.

`@hint`
- Du kan använda de variabler som redan har skapats för att bygga listan: `areas = [hall, kit, ...]`.
- Se till att använda hakparenteser `[]` i stället för vanliga parenteser `()`.
- Du behöver inte använda citationstecken när du lagrar variabler i en lista.
- Skriv `print(areas)` för att skriva ut listan när du skickar in svaret.

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
predef_msg = "Ta inte bort eller redigera de fördefinierade variablerna!"
areas_msg = "Definiera `areas` som listan som innehåller alla areavariablerna, i rätt ordning: `[hall, kit, liv, bed, bath]`. Kontrollera stavningen. Listan får inte innehålla något annat!"

Ex().check_correct(
    has_printout(0, not_printed_msg = "__JINJA__:Har du använt `{{sol_call}}` för att skriva ut listan `areas` i slutet av ditt skript?"),
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

success_msg("Bra jobbat! En lista är mycket bättre här, eller hur?")
```

---

## Skapa listor med olika typer

```yaml
type: NormalExercise
key: 1702a8bcdc
lang: python
xp: 100
skills:
  - 2
```

Även om det inte är så vanligt kan en lista innehålla en blandning av Python-typer, till exempel strängar, flyttal och booleaner.

Nu ska du lägga till rumsnamnen i din lista, så att du enkelt kan se både namn och yta tillsammans.

En del av koden är redan skriven åt dig. Lägg märke till följande: `"bathroom"` är en sträng, medan `bath` är en variabel som representerar flyttalet `9.50` som du angav tidigare.

`@instructions`
- Slutför koden som skapar listan `areas`. Bygg listan så att varje rums namn som en sträng kommer först, följt av rummets yta. Med andra ord, lägg till strängarna `"hallway"`, `"kitchen"` och `"bedroom"` på rätt platser.
- Skriv ut `areas` igen – är utskriften mer informativ den här gången?

`@hint`
- De fyra första elementen i listan `areas` är kodade som `["hallway", hall, "kitchen", kit, ...`.
- En sträng måste omges av citationstecken `""`.

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
predef_msg = "Ta inte bort eller redigera de fördefinierade variablerna!"
areas_msg = "Du tilldelade inte rätt värde till `areas`. Ta en ny titt på instruktionerna. Se till att placera rumsnamnet före variabeln som innehåller arean varje gång. Ordningen är viktig här! Se upp för stavfel."

Ex().check_correct(
  check_object("areas").has_equal_value(incorrect_msg = areas_msg),
  multi([ check_object(obj, missing_msg = predef_msg).has_equal_value(incorrect_msg = predef_msg) for obj in objs])
)

Ex().has_printout(0, not_printed_msg = "__JINJA__:Har du använt `{{sol_call}}` för att skriva ut listan `areas` i slutet av ditt skript?")

success_msg("Bra gjort! Den här listan innehåller både strängar och flyttal, men det är inget problem för Python!")
```

---

## Lista av listor

```yaml
type: NormalExercise
key: 9158c577b0
lang: python
xp: 100
skills:
  - 2
```

Som datavetare arbetar du ofta med stora mängder data, och det kan vara praktiskt att gruppera en del av den.

I stället för att skapa en lista med strängar och flyttal som representerar namnen på och ytorna av rummen i ditt hus, kan du skapa en lista av listor.

Kom ihåg: `"hallway"` är en sträng, medan `hall` är en variabel som representerar flyttalet `11.25` som du angav tidigare.

`@instructions`
- Komplettera listan av listor så att den även innehåller data för sovrummet och badrummet. Se till att du lägger in dem i rätt ordning!
- Skriv ut `house` – är det här sättet att strukturera data tydligare?

`@hint`
- Lägg till _underlistor_ i listan `house` genom att lägga till `["bedroom", bed]` och `["bathroom", bath]` inom hakparenteserna.
- Kom ihåg att inkludera ett kommatecken `,` efter varje underlista.
- För att skriva ut en variabel `x` skriver du `print(x)` på en ny rad.

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
predef_msg = "Ta inte bort eller redigera de fördefinierade variablerna!"
house_msg = "Du tilldelade inte rätt värde till `house`. Ta en ny titt på instruktionerna. Utöka listan med listor så att den innehåller en lista för varje par av rumsnamn och rumsyta. Var uppmärksam på ordningen och eventuella stavfel!"

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

Ex().has_printout(0, not_printed_msg = "__JINJA__:Har du använt `{{sol_call}}` för att skriva ut innehållet i `house`?")

success_msg("Utmärkt! Gör dig redo att lära dig om listindexering!")
```

---

## Subsetta listor

```yaml
type: VideoExercise
key: c076b5a69c
xp: 50
```

`@projector_key`
fc15ba5cb9485456df8589130b519ea3

---

## Välj och erövra

```yaml
type: NormalExercise
key: c3ce582e32
lang: python
xp: 100
skills:
  - 2
```

Att ta ut delar av Python-listor är enkelt. Ta kodexemplet nedan, som skapar en lista `x` och sedan väljer ut "b" från den. Kom ihåg att det är det andra elementet och därför har index 1. Du kan även använda negativt index.

```
x = ["a", "b", "c", "d"]
x[1]
x[-3] # samma resultat!
```

Kommer du ihåg listan `areas` från tidigare, som innehåller både strängar och flyttal? Definitionen finns redan i skriptet. Kan du lägga till rätt kod för att göra några dellistningsoperationer?

`@instructions`
- Skriv ut det andra elementet i listan `areas` (det har värdet `11.25`).
- Ta ut och skriv ut det sista elementet i `areas`, som är `9.50`. Här passar ett negativt index utmärkt!
- Välj talet som representerar vardagsrummets area (`20.0`) och skriv ut det.

`@hint`
- Använd `x[1]` för att välja det andra elementet i en lista `x`.
- Använd `x[-1]` för att välja det sista elementet i en lista `x`.
- Se till att omge dina dellistningsoperationer med ett `print()`-anrop.
- Talet som representerar vardagsrummets area är det 6:e elementet i listan, så du behöver `[5]` här. `area[4]` skulle visa strängen!

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
msg = "Ta inte bort eller redigera den fördefinierade listan `areas`."
Ex().check_object("areas", missing_msg = msg).has_equal_value(incorrect_msg = msg)
Ex().has_printout(0, not_printed_msg = "Ta en ny titt på din kod för att skriva ut det andra elementet i `areas`, som finns vid index `1`.")
Ex().has_printout(1, not_printed_msg = "Ta en ny titt på din kod för att skriva ut det sista elementet i `areas`, som finns vid index `-1`.")
Ex().has_printout(2, not_printed_msg = "Ta en ny titt på din kod för att skriva ut vardagsrummets area. Den finns vid index `5`.")
success_msg("Bra jobbat!")
```

---

## Skiva och dela

```yaml
type: NormalExercise
key: 7f08642d18
lang: python
xp: 100
skills:
  - 2
```

Att välja enskilda värden från en lista är bara en del av historien. Det går också att _skiva_ din lista, det vill säga välja ut flera element på en gång. Använd följande syntax:

```
my_list[start:end]
```

Indexet `start` inkluderas, medan indexet `end` _inte_ inkluderas. Det är också möjligt att utelämna dessa index. Om du inte anger `start`-indexet förstår Python att du vill börja från listans början.

`@instructions`
- Använd skivning för att skapa en lista, `downstairs`, som innehåller de första 6 elementen i `areas`.
- Skapa `upstairs` som de sista `4` elementen i `areas`. Förenkla skivningen den här gången genom att utelämna `end`-indexet.
- Skriv ut både `downstairs` och `upstairs` med `print()`.

`@hint`
- Använd hakparenteserna `[0:6]` för att hämta de första sex elementen i en lista.
- För att hämta allt utom de första 5 elementen i en lista `l` använder du `l[5:]`.
- Lägg till två `print()`-anrop för att skriva ut `downstairs` och `upstairs`.

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
msg = "Ta inte bort eller redigera den fördefinierade listan `areas`."
Ex().check_object("areas", missing_msg = msg).has_equal_value(incorrect_msg = msg)

patt = "`%s` är felaktig. Använd `areas[%s]` och slicing för att välja de element du vill ha, eller något likvärdigt."
Ex().check_object("downstairs").has_equal_value(incorrect_msg = patt % ('downstairs', '0:6'))
Ex().check_object("upstairs").has_equal_value(incorrect_msg = patt % ("upstairs",":6"))

Ex().has_printout(0, not_printed_msg="Har du skrivit ut `downstairs` efter att ha beräknat det?")
Ex().has_printout(1, not_printed_msg="Har du skrivit ut `upstairs` efter att ha beräknat det?")

success_msg("Bra gjort!")
```

---

## Subsetting av listor i listor

```yaml
type: NormalExercise
key: dbbbd306cf
xp: 100
```

En lista i Python kan också innehålla andra listor.

För att subset:a listor i listor använder du samma teknik som tidigare: hakparenteser. För en lista som heter `house` ser det ut så här:

```
house[2][0]
```

`@instructions`
- Subset:a listan `house` för att hämta flyttalet `9.5`.

`@hint`
- Dela upp det i steg. Börja med att hämta det sista elementet i listan, `["bathroom", 9.50]`. Kom ihåg att det sista elementets index är `-1`.
- Hämta sedan det andra elementet i `["bathroom", 9.50]`, som har index `1`.

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

success_msg("Korrekt! Den sista biten av listpusslet är manipulation.")
```

---

## Manipulera listor

```yaml
type: VideoExercise
key: d7fe818b3a
xp: 50
```

`@projector_key`
355ed52d2fb0d67508c6a311b7cbc6d3

---

## Ersätt listelement

```yaml
type: NormalExercise
key: 4e1bba1b55
lang: python
xp: 100
skills:
  - 2
```

För att ersätta element i en lista väljer du ut en delmängd av listan och tilldelar den nya värden. Du kan välja enskilda element eller ändra hela listsnitt på en gång.

I den här och kommande övningar fortsätter du arbeta med listan `areas`, som innehåller namn och ytor för olika rum i ett hus.

`@instructions`
- Uppdatera badrummets yta till `10.50` kvadratmeter i stället för `9.50` med hjälp av negativt index.
- Gör listan `areas` lite mer trendig! Ändra `"living room"` till `"chill zone"`. Använd inte negativt index den här gången.

`@hint`
- För att uppdatera badrummets yta, identifiera delmängden för badrummet (det är det sista elementet i listan!).
- Ersätt sedan värdet med den nya ytan genom att tilldela det till den här delmängden.
- Gör samma sak för att uppdatera namnet `"living room"`, som finns på index 4.

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
bathroom_msg = 'Du kan använda `areas[-1] = 10.50` för att uppdatera badrumsarean.'
chillzone_msg = 'Du kan använda `areas[4] = "chill zone"` för att uppdatera vardagsrumsnamnet.'
Ex().check_correct(
  check_object('areas').has_equal_value(incorrect_msg = 'Dina ändringar av `areas` resulterade inte i den korrekta listan. Är du säker på att du använde rätt delmängdsoperationer? Om du är osäker kan du använda en ledtråd!'),
  multi(
    has_equal_value(expr_code='areas[-1]', override=10.50, incorrect_msg = bathroom_msg),
    has_equal_value(expr_code='areas[4]', override='chill zone', incorrect_msg = chillzone_msg),
  )
)
success_msg('Utmärkt! Som kodexemplet visade kan du även dela upp en lista och ersätta den med en annan lista för att uppdatera flera element i ett enda kommando.')
```

---

## Utöka en lista

```yaml
type: NormalExercise
key: ff0fe8d967
lang: python
xp: 100
skills:
  - 2
```

Om du kan ändra element i en lista vill du säkert också kunna lägga till nya element, eller hur? Det gör du med operatorn `+`:

```
x = ["a", "b", "c", "d"]
y = x + ["e", "f"]
```

Du har precis vunnit på lotteriet – grattis! Du bestämmer dig för att bygga ett poolhus och ett garage. Kan du lägga till den informationen i listan `areas`?

`@instructions`
- Använd operatorn `+` för att lägga till listan `["poolhouse", 24.5]` i slutet av listan `areas`. Lagra den nya listan som `areas_1`.
- Utöka `areas_1` ytterligare genom att lägga till data om ditt garage. Lägg till strängen `"garage"` och flyttalet `15.45`. Döp den nya listan till `areas_2`.

`@hint`
- Följ kodexemplet i uppgiften. `x` är `areas` här, och `["e", "f"]` är `["poolhouse", 24.5]`.
- För att lägga till fler element i `areas_1`, använd `areas_1 + ["element", 123]`.

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
msg = "Ta inte bort eller redigera den fördefinierade listan `areas`."
Ex().check_object("areas", missing_msg = msg).has_equal_value(incorrect_msg = msg)
Ex().check_object("areas_1").has_equal_value(incorrect_msg = "Använd `areas + [\"poolhouse\", 24.5]` för att skapa `areas_1`. Kontrollera att det inte finns några stavfel!")
Ex().check_object("areas_2").has_equal_value(incorrect_msg = "Använd `areas_1 + [\"garage\", 15.45]` för att skapa `areas_2`. Kontrollera att det inte finns några stavfel!")
success_msg("Bra! Listan tar fin form!")
```

---

## Ta bort listelement

```yaml
type: NormalExercise
key: 85f792356e
xp: 100
```

Slutligen kan du även ta bort element från din lista. Det gör du med `del`-satsen:

```
x = ["a", "b", "c", "d"]
del x[1]
```

Observera: så fort du tar bort ett element från en lista förändras indexen för alla efterföljande element!

Tyvärr visade sig lotterinsten vara mindre än väntat, och det verkar som att poolhuset inte blir av. Du behöver ta bort det från listan. Du bestämmer dig för att ta bort motsvarande sträng och flyttal från listan `areas`.

`@instructions`
- Ta bort strängen och flyttalet för `"poolhouse"` från din lista `areas`.
- Skriv ut den uppdaterade listan `areas`.

`@hint`
- Du behöver använda `del` två gånger för att ta bort två element. Var uppmärksam på att indexen förändras!

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

Ex().has_printout(0, not_printed_msg="Har du skrivit ut `areas` efter att ha tagit bort poolhouse-strängen och flyttalet?")
success_msg("Rätt! Du kommer att lära dig om enklare sätt att ta bort specifika element från Python-listor senare.")
```

---

## Listors inre funktionssätt

```yaml
type: NormalExercise
key: af72db9915
lang: python
xp: 100
skills:
  - 2
```

I den här övningen finns det redan kod på plats: en lista med namnet `areas` och en kopia som heter `areas_copy`.

För närvarande ändras det första elementet i listan `areas_copy`, varefter `areas` skrivs ut. Om du klickar på **Kör koden** ser du att ändringen i `areas_copy` även påverkar `areas`. Det beror på att `areas` och `areas_copy` pekar på samma lista.

För att förhindra att ändringar i `areas_copy` också påverkar `areas` behöver du skapa en explicit kopia av `areas` med `list()` eller med `[:]`.

`@instructions`
- Ändra det andra kommandot, som skapar variabeln `areas_copy`, så att `areas_copy` blir en explicit kopia av `areas`. Efter din ändring ska ändringar i `areas_copy` inte påverka `areas`. Skicka in svaret för att kontrollera att det fungerar.

`@hint`
- Ändra anropet `areas_copy = areas`. Istället för att tilldela `areas` direkt kan du använda `list(areas)` eller `areas[:]`.

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
  check_object("areas_copy").has_equal_value(incorrect_msg = "Det verkar som att `areas_copy` inte har uppdaterats korrekt."),
  check_function("list", missing_msg = "Se till att använda `list(areas)` för att skapa en `areas_copy`.")
)

mmsg = "Ta inte bort den fördefinierade listan `areas`."
imsg = "Se till att endast redigera kopian, inte den ursprungliga listan `areas`. Ta en ny titt på övningsbeskrivningen om du är osäker på hur du skapar en kopia."
Ex().check_correct(
  check_object("areas", missing_msg = mmsg).has_equal_value(incorrect_msg = imsg),
  check_function("list", missing_msg = "Se till att använda `list(areas)` för att skapa en `areas_copy`.")
)

success_msg("Bra! Skillnaden mellan explicita kopior och referensbaserade kopior är subtil, men kan vara mycket viktig. Försök att komma ihåg hur en lista lagras i datorns minne.")
```

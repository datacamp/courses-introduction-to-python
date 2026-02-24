---
title: Insert title here
key: 433dcfcfedaee070cbf440491c402e3b
video_link:
  mp3: >-
    https://videos.datacamp.com/mp3/translations/course_735/nl-NL/280f6c04-c6cf-4ce8-a789-7b7f9a9b5877.mp3
---

## Variabelen en typen

```yaml
type: TitleSlide
key: dc8b62f1c8
```

`@lower_third`
name: Hugo Bowne-Anderson
title: Data Scientist at DataCamp

`@script`
Goed gedaan en welkom terug! Het is duidelijk dat Python een geweldige rekenmachine is. Als je echter complexere berekeningen wilt doen, wil je waarden kunnen "opslaan" terwijl je aan het coderen bent.
---

## Variabele

```yaml
type: FullSlide
key: 36ec318b41
```

`@part1`
- Specifieke, hoofdlettergevoelige naam

- Roep de waarde op via de naam van de variabele.{{1}}

- 1,79 m - 68,7 kg{{2}}

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
Dat doe je door een variabele te definiëren, met een specifieke, hoofdlettergevoelige naam. Zodra je zo’n variabele hebt aangemaakt (of gedeclareerd), kun je later de waarde ervan oproepen door de variabelenaam te typen.

Stel dat je je lengte en gewicht meet, in metrische eenheden: je bent één-komma-negen-en-zeventig meter lang en weegt achtenzestig-komma-zeven kilogram. Je kunt deze waarden toekennen aan twee variabelen, height en weight, met een gelijkteken:

Als je nu de naam van de variabele, height, typt,

zoekt Python naar de variabelenaam, haalt de waarde op en print die.
---

## Bereken BMI

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

$$ \text{BMI} = \frac{\text{gewicht}}{\text{lengte}^2} $${{1}}

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
Laten we nu de Body Mass Index, of BMI, berekenen, die als volgt wordt berekend, met gewicht in kilogram en lengte in meter. Je kunt dit doen met de daadwerkelijke waarden, maar je kunt net zo goed de variabelen height en weight gebruiken, zoals hier. Steeds als je de naam van de variabele typt, vraag je Python om die te vervangen door de daadwerkelijke waarde van de variabele. weight komt overeen met achtenzestig-komma-zeven, en height met één-komma-negen-en-zeventig.

Tot slot laat deze versie Python het resultaat opslaan in een nieuwe variabele, bmi. Bmi bevat nu dezelfde waarde als die je eerder hebt berekend.

In Python worden variabelen voortdurend gebruikt. Ze helpen om je code reproduceerbaar te maken.
---

## Reproduceerbaarheid

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
Stel dat de code om de variabelen height, weight en bmi te maken in een script staat, zoals dit. Als je nu de bmi voor een ander gewicht wilt herberekenen,
---

## Reproduceerbaarheid

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
kun je simpelweg de declaratie van de variabele weight aanpassen en het script opnieuw uitvoeren. De bmi verandert mee, omdat de waarde van de variabele weight ook is gewijzigd.

Tot nu toe hebben we alleen met numerieke waarden gewerkt, zoals lengte en gewicht.
---

## Python-typen

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
In Python hebben deze getallen allemaal een specifiek type. Je kunt het type van een waarde bekijken met de functie type. Om het type van onze bmi-waarde te zien, schrijf je gewoon type en dan bmi tussen haakjes. Je ziet dat het een float is, Pythons manier om een reëel getal weer te geven, dus een getal met zowel een geheel als een kommagedeelte. Python heeft ook een type voor gehele getallen: int, zoals in dit voorbeeld.

Voor data science heb je echter meer nodig dan ints en floats.
---

## Python-typen (2)

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
Python heeft nog tal van andere datatypen. De meest voorkomende zijn strings en booleans.

Een string is Pythons manier om tekst weer te geven. Je kunt zowel dubbele als enkele aanhalingstekens gebruiken om een string te maken, zoals je in deze voorbeelden ziet. Als je het type van de laatste variabele hier print, zie je dat het str is, kort voor string.

De boolean is een type dat ofwel True of False kan zijn. Je kunt het zien als ‘Ja’ en ‘Nee’ in alledaagse taal. Booleans zijn later erg handig, bijvoorbeeld om filterbewerkingen op je data uit te voeren.

Er is iets bijzonders aan Python-datatypen.
---

## Python-typen (3)

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

- Ander type = ander gedrag!{{3}}

`@script`
Kijk eens naar deze coderegel, die twee integers optelt, en dan naar deze regel, die twee strings optelt.

Bij de integers werden de waarden opgeteld, terwijl bij de strings de tekst aan elkaar werd geplakt. De plus-operator gedroeg zich anders voor verschillende datatypen. Dit is een algemeen principe: hoe de code zich gedraagt, hangt af van de typen waarmee je werkt.

In de oefeningen hierna maak je je eerste variabelen en experimenteer je met een paar van Pythons datatypen. Ik zie je in de volgende video, waarin ik alles uitleg over lijsten.
---

## Laten we oefenen!

```yaml
type: FinalSlide
key: b7fc40db4d
```

`@script`
Ik kan niet wachten je te zien in het volgende hoofdstuk, waar je nog gavere Python-grafieken gaat bouwen.

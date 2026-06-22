---
title: Insert title here
key: 433dcfcfedaee070cbf440491c402e3b
video_link:
  mp3: >-
    https://videos.datacamp.com/mp3/translations/course_735/sv-SE/f0aab16d-db98-42e7-9c4d-3cc18c98c861-f192459054e72a9305fcddec779cf9e8.mp3
---

## Variabler och typer

```yaml
type: TitleSlide
key: dc8b62f1c8
```

`@lower_third`
name: Hugo Bowne-Anderson
title: Data Scientist at DataCamp

`@script`
Bra jobbat och välkommen tillbaka! Python är verkligen ett utmärkt verktyg för beräkningar. Men om du vill göra mer komplexa uträkningar behöver du kunna "spara" värden medan du kodar.

---

## Variabel

```yaml
type: FullSlide
key: 36ec318b41
```

`@part1`
- Specifikt, skiftlägeskänsligt namn

- Hämta värdet via variabelnamnet{{1}}

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
Det gör du genom att definiera en variabel med ett specifikt, skiftlägeskänsligt namn. När du väl har skapat, eller deklarerat, en variabel kan du hämta dess värde igen genom att skriva variabelns namn.

Säg att du mäter din längd och vikt i metriska enheter. Du är 1,79 meter lång och väger 68,7 kilo. Du kan tilldela dessa värden till två variabler som heter height och weight, med ett likhetstecken.

Om du nu skriver variabelnamnet height

letar Python upp variabeln, hämtar dess värde och skriver ut det.

---

## Beräkna BMI

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

$$ \text{BMI} = \frac{\text{weight}}{\text{height}^2} $${{1}}

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
Nu beräknar vi kroppsmasseindex, eller BMI, som räknas ut med vikten i kilo och längden i meter. Du kan använda de faktiska värdena direkt, men du kan lika gärna använda variablerna height och weight, som här. Varje gång du skriver ett variabelnamn ber du Python att ersätta det med variabelns faktiska värde. weight motsvarar 68,7 och height motsvarar 1,79.

I den sista versionen låter vi Python spara resultatet i en ny variabel som heter bmi. Den variabeln innehåller nu samma värde som du beräknade tidigare.

Variabler används hela tiden i Python. De hjälper dig att göra din kod återanvändbar.

---

## Reproducerbarhet

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
Tänk dig att koden som skapar variablerna height, weight och bmi finns i ett skript, som det här. Om du nu vill beräkna om BMI för en annan vikt

---

## Reproducerbarhet

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
kan du helt enkelt ändra deklarationen av variabeln weight och köra skriptet igen. BMI uppdateras automatiskt, eftersom värdet på variabeln weight har ändrats.

Hittills har vi bara arbetat med numeriska värden, som längd och vikt.

---

## Python-typer

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
I Python har alla tal en specifik typ. Du kan kontrollera typen på ett värde med funktionen type. För att se typen på vårt bmi-värde skriver du helt enkelt type och sedan bmi inom parentes. Du ser att det är en float, vilket är Pythons sätt att representera reella tal, alltså tal som kan ha både en heltalsdel och en decimaldel. Python har också en typ för heltal, int, som i det här exemplet.

För att arbeta med data räcker det dock inte med enbart int och float.

---

## Python-typer (2)

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
Python har många fler datatyper. De vanligaste är strängar och booleaner.

En sträng är Pythons sätt att representera text. Du kan använda både enkla och dubbla citattecken för att skapa en sträng, som du ser i de här exemplen. Om du skriver ut typen för den sista variabeln ser du att det är str, kort för string.

En booleansk typ kan antingen vara True eller False, ungefär som "ja" och "nej" i vardagsspråk. Booleaner kommer att vara mycket användbara framöver, till exempel när du vill filtrera data.

Det finns något intressant att notera om Pythons datatyper.

---

## Python-typer (3)

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

- Olika typ = olika beteende!{{3}}

`@script`
Titta på den här kodraden som adderar två heltal, och sedan den här raden som adderar två strängar.

För heltalen summeras värdena, medan strängarna fogas ihop till en. Plusoperatorn beter sig alltså olika beroende på datatyp. Det är en grundläggande princip: hur koden fungerar beror på vilka typer du arbetar med.

I övningarna som följer skapar du dina första variabler och provar på några av Pythons datatyper. Vi ses i nästa video där vi går igenom listor.

---

## Nu kör vi en övning!

```yaml
type: FinalSlide
key: b7fc40db4d
```

`@script`
Nu är det dags att koda, och jag ser fram emot att ses i nästa kapitel där du skapar ännu mer imponerande diagram i Python.

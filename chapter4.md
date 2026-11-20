---
title_meta: Hoofdstuk 4
title: NumPy
description: >-
  NumPy is een fundamenteel Python-pakket om efficiënt aan data science te doen.
  Leer werken met krachtige tools in de NumPy-array en ga aan de slag met
  data-exploratie.
attachments:
  slides_link: 'https://projector-video-pdf-converter.datacamp.com/735/chapter4.pdf'
lessons:
  - nb_of_exercises: 5
    title: NumPy
  - nb_of_exercises: 5
    title: 2D NumPy-arrays
  - nb_of_exercises: 3
    title: 'NumPy: basisstatistiek'
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

## Je eerste NumPy-array

```yaml
type: NormalExercise
key: 84cab9d170
lang: python
xp: 100
skills:
  - 2
```

Je gaat nu de honkbalwereld induiken. Onderweg raak je vertrouwd met de basis van `numpy`, een krachtig pakket voor data science.

In het Python-script is al een lijst `baseball` gedefinieerd, met de lengte van een aantal honkbalspelers in centimeters. Kun je code toevoegen om hier een `numpy`-array van te maken?

`@instructions`
- Importeer het pakket `numpy` als `np`, zodat je `numpy` kunt aanroepen met `np`.
- Gebruik `np.array()` om van `baseball` een `numpy`-array te maken. Noem deze array `np_baseball`.
- Print het type van `np_baseball` om te checken of het klopt.

`@hint`
- Met `import numpy as np` zit je goed. Vanaf nu gebruik je `np.fun_name()` wanneer je een `numpy`-functie wilt gebruiken.
- `np.array()` moet `baseball` als input krijgen. Ken het resultaat van de functie-aanroep toe aan `np_baseball`.
- Om het type van een variabele `x` te printen, typ je gewoon `print(type(x))`.

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
predef_msg = "Je hoeft de vooraf gedefinieerde variabelen niet te wijzigen of te verwijderen."
Ex().has_import("numpy")
Ex().check_correct(
  check_object("np_baseball"),
  multi(
    check_object("baseball", missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
    check_function("numpy.array").check_args(0).has_equal_ast()
  )
)

Ex().has_printout(0)
success_msg("Goed gedaan!")
```

---

## Lengte van honkbalspelers

```yaml
type: NormalExercise
key: e7e25a89ea
lang: python
xp: 100
skills:
  - 2
```

Je bent een enorme honkbalfan. Je besluit de MLB (Major League Baseball) te bellen voor extra statistieken over de lengte van de belangrijkste spelers. Ze sturen gegevens door van meer dan duizend spelers, opgeslagen als een gewone Python-lijst: `height_in`. De lengte is uitgedrukt in inches. Kun je er een `numpy`-array van maken en de eenheden omrekenen naar meters?

`height_in` is al beschikbaar en het pakket `numpy` is geladen, dus je kunt meteen aan de slag (bron: stat.ucla.edu).

`@instructions`
- Maak een `numpy`-array van `height_in`. Noem deze nieuwe array `np_height_in`.
- Print `np_height_in`.
- Vermenigvuldig `np_height_in` met `0.0254` om alle lengtemetingen van inches naar meters om te rekenen. Sla de nieuwe waarden op in een nieuwe array, `np_height_m`.
- Print `np_height_m` en check of de output logisch is.

`@hint`
- Gebruik `np.array()` en geef `height` door. Sla het resultaat op in `np_height_in`.
- Om een variabele `x` af te drukken, typ je `print(x)` in het Python-script.
- Voer berekeningen uit alsof `np_height_in` één getal is: `np_height_in * conversion_factor` maakt deel uit van het antwoord.
- Om een variabele `x` af te drukken, typ je `print(x)` in het Python-script.

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
  check_object("np_height_m").has_equal_value(incorrect_msg = "Gebruik `np_height_in * 0.0254` om `np_height_m` te berekenen.")
)

success_msg("Mooi! In een oogwenk voert `numpy` vermenigvuldigingen uit op meer dan 1000 lengtemetingen.")
```

---

## NumPy-bijwerkingen

```yaml
type: MultipleChoiceExercise
key: 3662ff6637
lang: python
xp: 50
skills:
  - 2
```

`numpy` is geweldig voor vectorrekenen. Vergeleken met gewone Python-lijsten zijn er echter een paar verschillen.

Ten eerste kunnen `numpy`-arrays geen elementen met verschillende types bevatten. Als je types mengt, zoals booleans en integers, zet `numpy` ze automatisch om naar één gemeenschappelijk type. Booleans zoals `True` en `False` worden behandeld als `1` en `0` wanneer ze met getallen worden gecombineerd, waardoor de array uit integers bestaat.

Ten tweede hebben de gebruikelijke rekenoperatoren, zoals `+`, `-`, `*` en `/`, een andere betekenis voor gewone Python-lijsten dan voor `numpy`-arrays.

Selecteer de code die het volgende resultaat oplevert:

```
np.array([True, 1, 2]) + np.array([3, 4, False])
```

Het pakket `numpy` is al geïmporteerd als `np`. Je kunt elke optie in de IPython-shell uitvoeren om de output te bekijken.

`@possible_answers`
- `np.array([True, 1, 2, 3, 4, False])`
- `np.array([4, 3, 0]) + np.array([0, 2, 2])`
- `np.array([1, 1, 2]) + np.array([3, 4, -1])`
- `np.array([0, 1, 2, 3, 4, 5])`

`@hint`
- Kopieer de verschillende codeblokken en plak ze in de IPython-shell. Druk op **enter** om de code uit te voeren en kijk welke output overeenkomt met die van `np.array([True, 1, 2]) + np.array([3, 4, False])`.

`@pre_exercise_code`
```{python}
import numpy as np
```

`@sct`
```{python}
msg1 = msg3 = msg4 = "Onjuist. Probeer de verschillende codeblokken uit en kijk welke overeenkomt met het doeldcodeblok."
msg2 = "Goed gedaan! `True` wordt omgezet naar 1, `False` wordt omgezet naar 0."
Ex().has_chosen(2, [msg1, msg2, msg3, msg4])
```

---

## Subsets maken van NumPy-arrays

```yaml
type: NormalExercise
key: fcb2a9007b
lang: python
xp: 100
skills:
  - 2
```

Subsetting (met vierkante haken op lijsten of arrays) werkt exact hetzelfde voor zowel lijsten als arrays.

In deze oefening zijn er al twee lijsten, `height_in` en `weight_lb`, op de achtergrond voor je geladen. Die bevatten de lengte en het gewicht van de MLB-spelers als gewone lijsten. Er zijn ook twee `numpy`-arrays, `np_weight_lb` en `np_height_in`, voor je voorbereid.

`@instructions`
- Maak een subset van `np_weight_lb` door het element op index 50 te printen.
- Print een subarray van `np_height_in` met de elementen van index 100 tot **en met** index 110.

`@hint`
- Zorg dat je je subset-operaties in een `print()`-aanroep zet.
- Gebruik `[100:111]` om de elementen van index 100 tot en met index 110 op te halen.

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
msg = "Je hoeft de vooraf gedefinieerde variabelen niet te wijzigen of te verwijderen."
Ex().multi(
    check_object("np_height_in", missing_msg=msg).has_equal_value(incorrect_msg=msg),
    check_object("np_weight_lb", missing_msg=msg).has_equal_value(incorrect_msg=msg)
)

Ex().has_printout(0)
Ex().has_printout(1)

success_msg("Mooi! Tijd om iets nieuws te leren: 2D NumPy-arrays!")
```

---

## 2D NumPy-arrays

```yaml
type: VideoExercise
key: 1241efac7a
xp: 50
```

`@projector_key`
ae3238dcc7feb9adecfee0c395fc8dc8

---

## Je eerste 2D-NumPy-array

```yaml
type: NormalExercise
key: 5cb045bb13
lang: python
xp: 100
skills:
  - 2
```

Voordat we met de echte MLB-gegevens aan de slag gaan, maken we eerst een 2D-`numpy`-array van een kleine lijst van lijsten.

In deze oefening is `baseball` een lijst van lijsten. De hoofdlijst bevat 4 elementen. Elk van deze elementen is een lijst met de lengte en het gewicht van 4 honkbalspelers, in deze volgorde. `baseball` is al voor je in het script gezet.

`@instructions`
- Gebruik `np.array()` om een 2D-`numpy`-array te maken van `baseball`. Noem deze `np_baseball`.
- Print het type van `np_baseball`.
- Print het `shape`-attribuut van `np_baseball`. Gebruik `np_baseball.shape`.

`@hint`
- `baseball` is al voor je gedefinieerd in het script. Roep `np.array()` erop aan en sla de resulterende 2D-`numpy`-array op in `np_baseball`.
- Gebruik `print()` in combinatie met `type()` voor de tweede instructie.
- `np_baseball.shape` geeft je de afmetingen van `np_baseball`. Zorg dat je er een `print()`-aanroep omheen zet.

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
msg = "Je hoeft de vooraf gedefinieerde variabelen niet te wijzigen of te verwijderen."
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

success_msg("Geweldig! Je bent nu klaar om de daadwerkelijke MLB-gegevens om te zetten naar een 2D `numpy`-array!")
```

---

## Baseballdata in 2D-vorm

```yaml
type: NormalExercise
key: 5df25d0b7b
lang: python
xp: 100
skills:
  - 2
```

Je ziet in dat het logischer is om al deze informatie te herstructureren in een 2D-`numpy`-array.

Je hebt een Python-lijst van lijsten. In deze lijst van lijsten stelt elke sublijst de lengte en het gewicht van één honkbalspeler voor. De naam van deze lijst is `baseball` en hij is al voor je geladen (ook al kun je hem niet zien).

Sla de gegevens op als een 2D-array om de extra functionaliteit van `numpy` te gebruiken.

`@instructions`
- Gebruik `np.array()` om van `baseball` een 2D-`numpy`-array te maken. Noem deze `np_baseball`.
- Print het attribuut `shape` van `np_baseball`.

`@hint`
- `baseball` is al beschikbaar in de Python-omgeving. Roep `np.array()` erop aan en sla de resulterende 2D-`numpy`-array op in `np_baseball`.
- `np_baseball.shape` geeft de afmetingen van `np_baseball`. Zorg dat je er een `print()`-aanroep omheen zet.

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

success_msg("Geweldig! Tijd om wat gave functies van multi-dimensionale `numpy` arrays te laten zien!")
```

---

## Subsetten van 2D-NumPy-arrays

```yaml
type: NormalExercise
key: aeca4977f0
lang: python
xp: 100
skills:
  - 2
```

Als je 2D-`numpy`-array een vaste structuur heeft, dus elke rij en kolom heeft een vast aantal waarden, worden ingewikkelde manieren van subsetten heel eenvoudig. Kijk naar de code hieronder waar de elementen `"a"` en `"c"` worden opgehaald uit een lijst-van-lijsten.

```
# numpy
import numpy as np
np_x = np.array(x)
np_x[:, 0]
```

De indexen vóór de komma verwijzen naar de rijen, en die na de komma naar de kolommen. De `:` gebruik je om te slicen; in dit voorbeeld zeg je tegen Python dat alle rijen moeten worden meegenomen.

`@instructions`
- Print de 50e rij van `np_baseball`.
- Maak een nieuwe variabele, `np_weight_lb`, met de volledige tweede kolom van `np_baseball`.
- Selecteer de lengte (eerste kolom) van de 124e honkballer in `np_baseball` en print die.

`@hint`
- Je hebt rij-index 49 nodig in de eerste instructie! Concreter: gebruik `[49, :]`.
- Om de volledige tweede kolom te selecteren, gebruik je `[:, 1]`.
- Gebruik voor de laatste instructie `[123, 0]`; vergeet niet alles in een `print()`-statement te zetten.

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
msg = "Je hoeft de vooraf gedefinieerde variabelen niet te wijzigen of te verwijderen."
Ex().multi(
    has_import("numpy", same_as = False),
    check_object("np_baseball", missing_msg=msg).has_equal_value(incorrect_msg = msg)
)

Ex().has_printout(0)

Ex().check_object('np_weight_lb').has_equal_value(incorrect_msg = "Je kunt `np_baseball[:,1]` gebruiken om `np_weight_lb` te definiëren. Dit selecteert de hele eerste kolom.")

Ex().has_printout(1)

success_msg("Dit gaat goed!")
```

---

## Rekenen met 2D-arrays

```yaml
type: NormalExercise
key: 1c2378b677
lang: python
xp: 100
skills:
  - 2
```

2D-`numpy`-arrays kunnen, net als `numpy`-arrays, berekeningen element voor element uitvoeren.

`np_baseball` is al voor je gedefinieerd; het is opnieuw een 2D-`numpy`-array met 3 kolommen voor lengte (in inches), gewicht (in ponden) en leeftijd (in jaren). `baseball` is beschikbaar als een gewone lijst-van-lijsten en `updated` is beschikbaar als 2D-`numpy`-array.

`@instructions`
- Je hebt de wijzigingen in lengte, gewicht en leeftijd van alle honkbalspelers te pakken. Deze staan in een 2D-`numpy`-array, `updated`. Tel `np_baseball` en `updated` bij elkaar op en print het resultaat.
- Je wilt de eenheden van lengte en gewicht omzetten naar metrisch (respectievelijk meters en kilogrammen). Maak als eerste stap een `numpy`-array met drie waarden: `0.0254`, `0.453592` en `1`. Noem deze array `conversion`.
- Vermenigvuldig `np_baseball` met `conversion` en print het resultaat.

`@hint`
- `np_baseball + updated` zal een elementgewijze optelling van de twee `numpy`-arrays doen.
- Maak een `numpy`-array met `np.array()`; de invoer is een gewone Python-lijst met drie elementen.
- `np_baseball * conversion` werkt zonder extra stappen. Probeer het uit! Zorg dat je het in een `print()`-aanroep zet.

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

msg = "Je hoeft de vooraf gedefinieerde variabelen niet te wijzigen of te verwijderen."
Ex().check_object("np_baseball", missing_msg=msg).has_equal_value(incorrect_msg=msg)

Ex().has_printout(0)

Ex().check_correct(
    has_printout(1),
    check_correct(
        check_object('conversion').has_equal_value(),
        check_function('numpy.array', index=1).check_args(0).has_equal_value()
    )    
)

success_msg("Goed gedaan! Merk op hoe je met heel weinig code alle waarden in je `numpy` datastructuur op een heel specifieke manier kunt veranderen. Dit zal erg nuttig zijn in je toekomst als datawetenschapper!")
```

---

## NumPy: basisstatistieken

```yaml
type: VideoExercise
key: 287995e488
xp: 50
```

`@projector_key`
34495ba457d74296794d2a122c9b6e19

---

## Gemiddelde versus mediaan

```yaml
type: NormalExercise
key: 509c588eb6
lang: python
xp: 100
skills:
  - 2
```

Je weet nu hoe je `numpy`-functies gebruikt om meer gevoel te krijgen voor je data.

De honkbaldata is beschikbaar als een 2D-`numpy`-array met 3 kolommen (lengte, gewicht, leeftijd) en 1015 rijen. Deze `numpy`-array heet `np_baseball`. Na het herstructureren van de data merk je echter dat sommige lengtewaarden abnormaal hoog zijn. Volg de instructies en ontdek welke samenvattende statistiek het best geschikt is als je te maken hebt met zogeheten outliers. `np_baseball` is beschikbaar.

`@instructions`
- Maak `numpy`-array `np_height_in` die gelijk is aan de eerste kolom van `np_baseball`.
- Print het gemiddelde van `np_height_in`.
- Print de mediaan van `np_height_in`.

`@hint`
- Gebruik 2D-`numpy`-subsetting: `[:,0]` is een deel van de oplossing.
- Als `numpy` is geïmporteerd als `np`, kun je `np.mean()` gebruiken om het gemiddelde van een NumPy-array te berekenen. Vergeet niet om een `print()`-aanroep toe te voegen.
- Gebruik voor de laatste instructie `np.median()`.

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

Ex().check_object("np_height_in").has_equal_value(incorrect_msg = "Je kunt `np_baseball[:,0]` gebruiken om de eerste kolom van `np_baseball` te selecteren"),

Ex().check_correct(
    has_printout(0),
    check_function('numpy.mean').has_equal_value()
)

Ex().check_correct(
    has_printout(1),
    check_function('numpy.median').has_equal_value()
)

success_msg("Een gemiddelde lengte van 1586 inches, dat klinkt niet goed, toch? Maar de mediaan lijkt niet beïnvloed door de uitschieters: 74 inches klinkt perfect logisch. Het is altijd een goed idee om zowel de mediaan als het gemiddelde te controleren, om een idee te krijgen van de algehele verdeling van de hele dataset.")
```

---

## Verken de baseball-data

```yaml
type: NormalExercise
key: '4409948807'
lang: python
xp: 100
skills:
  - 2
```

Omdat het gemiddelde en de mediaan zo ver uit elkaar liggen, besluit je bij de MLB te klagen. Zij vinden de fout en sturen de gecorrigeerde data naar je terug. Deze is opnieuw beschikbaar als een 2D NumPy-array `np_baseball` met drie kolommen.

Het Python-script in de editor bevat al code om informatieve berichten met de verschillende samenvattende statistieken af te drukken en `numpy` is al geladen als `np`. Kun jij het afmaken? `np_baseball` is beschikbaar.

`@instructions`
- De code om de gemiddelde lengte af te drukken staat er al in. Maak de code voor de mediane lengte af.
- Gebruik `np.std()` op de eerste kolom van `np_baseball` om `stddev` te berekenen. 
- Zijn grote spelers meestal zwaarder? Gebruik `np.corrcoef()` om de correlatie tussen de eerste en tweede kolom van `np_baseball` op te slaan in `corr`.

`@hint`
- Gebruik `np.median()` om de mediaan te berekenen. Zorg dat je eerst de juiste kolom selecteert!
- Neem dezelfde kolom als subset wanneer je de standaarddeviatie berekent met `np.std()`.
- Gebruik `np_baseball[:, 0]` en `np_baseball[:, 1]` om de eerste en tweede kolom te selecteren; dit zijn de inputs voor `np.corrcoef()`.

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
msg = "Je zou de vooraf gedefinieerde `avg`-variabele niet moeten wijzigen of verwijderen."
Ex().check_object("avg", missing_msg=msg).has_equal_value(incorrect_msg=msg)

missing = "Heb je `np.median()` gebruikt om de mediaan te berekenen?"
incorrect = "Om `med` te berekenen, geef je de eerste kolom van `np_baseball` door aan `numpy.median()`. Het voorbeeld van `np.mean()` laat zien hoe het moet."
Ex().check_correct(
  check_object("med").has_equal_value(),
  check_function("numpy.median", index=0, missing_msg=missing).check_args(0).has_equal_value(incorrect_msg=incorrect)
)

missing = "Heb je `np.std()` gebruikt om de standaarddeviatie te berekenen?"
incorrect = "Om `stddev` te berekenen, geef je de eerste kolom van `np_baseball` door aan `numpy.std()`. Het voorbeeld van `np.mean()` laat zien hoe het moet."
Ex().check_correct(
  check_object("stddev").has_equal_value(),
  check_function("numpy.std", index=0, missing_msg=missing).check_args(0).has_equal_value(incorrect_msg=incorrect)
)

missing = "Heb je `np.corrcoef()` gebruikt om de correlatie te berekenen?"
incorrect1 = "Om `corr` te berekenen, moet het eerste argument van `np.corrcoef()` de eerste kolom van `np_baseball` zijn, net zoals je eerder deed."
incorrect2 = "Om `corr` te berekenen, moet het tweede argument van `np.corrcoef()` de tweede kolom van `np_baseball` zijn. In plaats van `[:,0]`, gebruik je deze keer `[:,1]`."
Ex().check_correct(
  check_object("corr").has_equal_value(),
  check_function("numpy.corrcoef", index=0, missing_msg=missing).multi(
    check_args(0, missing_msg=incorrect1).has_equal_value(incorrect_msg=incorrect1),
    check_args(1, missing_msg=incorrect2).has_equal_value(incorrect_msg=incorrect2)
  )
)

success_msg("Goed gedaan! Je hebt een solide basis gelegd - nu is het tijd om al je nieuwe data science vaardigheden te gebruiken om meer uitdagingen op te lossen en impact te maken.")
```

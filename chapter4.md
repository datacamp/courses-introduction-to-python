---
title_meta: Kapitel 4
title: NumPy
description: >-
  NumPy är ett grundläggande Python-paket för effektiv datavetenskap. Lär dig
  arbeta med kraftfulla verktyg i NumPy-arrayen och kom igång med
  datautforskning.
attachments:
  slides_link: 'https://projector-video-pdf-converter.datacamp.com/735/chapter4.pdf'
lessons:
  - nb_of_exercises: 5
    title: NumPy
  - nb_of_exercises: 5
    title: Tvådimensionella NumPy-arrayer
  - nb_of_exercises: 3
    title: 'NumPy: grundläggande statistik'
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

## Ditt första NumPy-array

```yaml
type: NormalExercise
key: 84cab9d170
lang: python
xp: 100
skills:
  - 2
```

Nu är det dags att dyka in i basebollens värld. På vägen lär du dig grunderna i `numpy` – ett kraftfullt paket för dataanalys.

En lista, `baseball`, är redan definierad i Python-skriptet och representerar längden på några basebollspelare i centimeter. Kan du lägga till kod som skapar ett `numpy`-array från listan?

`@instructions`
- Importera paketet `numpy` som `np`, så att du kan referera till `numpy` med `np`.
- Använd `np.array()` för att skapa ett `numpy`-array från `baseball`. Ge arrayen namnet `np_baseball`.
- Skriv ut typen av `np_baseball` för att kontrollera att du gjort rätt.

`@hint`
- `import numpy as np` löser det. Därefter använder du `np.fun_name()` varje gång du vill anropa en `numpy`-funktion.
- `np.array()` ska ta `baseball` som indata. Tilldela resultatet till `np_baseball`.
- För att skriva ut typen av en variabel `x` skriver du helt enkelt `print(type(x))`.

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
predef_msg = "Du behöver inte ändra eller ta bort de fördefinierade variablerna."
Ex().has_import("numpy")
Ex().check_correct(
  check_object("np_baseball"),
  multi(
    check_object("baseball", missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
    check_function("numpy.array").check_args(0).has_equal_ast()
  )
)

Ex().has_printout(0)
success_msg("Bra jobbat!")
```

---

## Basebollspelarnas längd

```yaml
type: NormalExercise
key: e7e25a89ea
lang: python
xp: 100
skills:
  - 2
```

Du är ett stort basebollproffs. Du bestämmer dig för att kontakta MLB (Major League Baseball) och fråga efter lite mer statistik om spelarnas längd. De skickar över data om mer än tusen spelare, lagrade som en vanlig Python-lista: `height_in`. Längden anges i tum. Kan du skapa en `numpy`-array av den och konvertera enheterna till meter?

`height_in` finns redan tillgänglig och paketet `numpy` är inläst, så du kan börja direkt (Källa: stat.ucla.edu).

`@instructions`
- Skapa en `numpy`-array från `height_in`. Namnge den nya arrayen `np_height_in`.
- Skriv ut `np_height_in`.
- Multiplicera `np_height_in` med `0.0254` för att konvertera alla längdmått från tum till meter. Spara de nya värdena i en ny array, `np_height_m`.
- Skriv ut `np_height_m` och kontrollera att resultatet ser rimligt ut.

`@hint`
- Använd `np.array()` och skicka in `height`. Spara resultatet i `np_height_in`.
- För att skriva ut en variabel `x` använder du `print(x)` i Python-skriptet.
- Utför beräkningar som om `np_height_in` vore ett enskilt tal: `np_height_in * conversion_factor` är en del av svaret.
- För att skriva ut en variabel `x` använder du `print(x)` i Python-skriptet.

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
  check_object("np_height_m").has_equal_value(incorrect_msg = "Använd `np_height_in * 0.0254` för att beräkna `np_height_m`.")
)

success_msg("Bra! På ett ögonblick utför `numpy` multiplikationer på mer än 1000 höjdmätningar.")
```

---

## NumPy – oväntade beteenden

```yaml
type: MultipleChoiceExercise
key: 3662ff6637
lang: python
xp: 50
skills:
  - 2
```

`numpy` är utmärkt för vektoraritmetik. Om du jämför det med vanliga Python-listor finns det dock vissa skillnader.

För det första kan `numpy`-arrayer inte innehålla element av olika typer. Om du blandar typer, till exempel booleaner och heltal, konverterar `numpy` dem automatiskt till en gemensam typ. Booleaner som `True` och `False` behandlas som `1` respektive `0` när de kombineras med tal, vilket innebär att arrayen omvandlas till heltal.

För det andra har de vanliga aritmetiska operatorerna `+`, `-`, `*` och `/` olika betydelse för vanliga Python-listor och `numpy`-arrayer.

Välj den kod som ger följande utdata:

```
np.array([True, 1, 2]) + np.array([3, 4, False])
```

Paketet `numpy` är redan importerat som `np`. Du kan köra varje alternativ i IPython Shell för att se utdata.

`@possible_answers`
- `np.array([True, 1, 2, 3, 4, False])`
- `np.array([4, 3, 0]) + np.array([0, 2, 2])`
- `np.array([1, 1, 2]) + np.array([3, 4, -1])`
- `np.array([0, 1, 2, 3, 4, 5])`

`@hint`
- Kopiera de olika kodstyckena och klistra in dem i IPython Shell. Tryck på **enter** för att köra koden och se vilket utdata som matchar det som genereras av `np.array([True, 1, 2]) + np.array([3, 4, False])`.

`@pre_exercise_code`
```{python}
import numpy as np
```

`@sct`
```{python}
msg1 = msg3 = msg4 = "Fel. Prova de olika kodstyckena och se vilket som matchar målkodstyckena."
msg2 = "Bra jobbat! `True` konverteras till 1, `False` konverteras till 0."
Ex().has_chosen(2, [msg1, msg2, msg3, msg4])
```

---

## Subsetting av NumPy-arrayer

```yaml
type: NormalExercise
key: fcb2a9007b
lang: python
xp: 100
skills:
  - 2
```

Subsetting (med hakparentesnotation på listor eller arrayer) fungerar på exakt samma sätt för både listor och arrayer.

Den här övningen har redan två listor, `height_in` och `weight_lb`, inlästa i bakgrunden. De innehåller längd och vikt för MLB-spelare som vanliga listor. Det finns även två `numpy`-arraylistor, `np_weight_lb` och `np_height_in`, förberedda åt dig.

`@instructions`
- Gör ett subset av `np_weight_lb` genom att skriva ut elementet vid index 50.
- Skriv ut en delarray av `np_height_in` som innehåller elementen från index 100 upp till **och inklusive** index 110.

`@hint`
- Se till att du omsluter dina subsettingoperationer med ett `print()`-anrop.
- Använd `[100:111]` för att hämta elementen från index 100 upp till och inklusive index 110.

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
msg = "Du behöver inte ändra eller ta bort de fördefinierade variablerna."
Ex().multi(
    check_object("np_height_in", missing_msg=msg).has_equal_value(incorrect_msg = msg),
    check_object("np_weight_lb", missing_msg=msg).has_equal_value(incorrect_msg = msg)
)

Ex().has_printout(0)
Ex().has_printout(1)

success_msg("Bra! Dags att lära sig något nytt: 2D NumPy-arrayer!")
```

---

## 2D NumPy-arrayer

```yaml
type: VideoExercise
key: 1241efac7a
xp: 50
```

`@projector_key`
ae3238dcc7feb9adecfee0c395fc8dc8

---

## Ditt första 2D NumPy-array

```yaml
type: NormalExercise
key: 5cb045bb13
lang: python
xp: 100
skills:
  - 2
```

Innan vi arbetar med den faktiska MLB-datan ska vi skapa ett 2D-`numpy`-array från en liten lista av listor.

I den här övningen är `baseball` en lista av listor. Huvudlistan innehåller 4 element. Varje element är i sin tur en lista med längd och vikt för 4 basebollspelare, i den ordningen. `baseball` är redan definierad i skriptet.

`@instructions`
- Använd `np.array()` för att skapa ett 2D-`numpy`-array från `baseball`. Döp det till `np_baseball`.
- Skriv ut typen av `np_baseball`.
- Skriv ut attributet `shape` för `np_baseball`. Använd `np_baseball.shape`.

`@hint`
- `baseball` är redan definierad i skriptet. Anropa `np.array()` på den och lagra det resulterande 2D-`numpy`-arrayet i `np_baseball`.
- Använd `print()` i kombination med `type()` för den andra instruktionen.
- `np_baseball.shape` ger dig dimensionerna för `np_baseball`. Se till att omsluta anropet med `print()`.

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
msg = "Du behöver inte ändra eller ta bort de fördefinierade variablerna."
Ex().check_object("baseball", missing_msg=msg).has_equal_value(incorrect_msg = msg)
Ex().has_import("numpy", same_as = False)

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

success_msg("Bra gjort! Nu är du redo att konvertera den faktiska MLB-datan till en tvådimensionell `numpy`-array!")
```

---

## Basebolldata i 2D-form

```yaml
type: NormalExercise
key: 5df25d0b7b
lang: python
xp: 100
skills:
  - 2
```

Du inser att det är mer logiskt att strukturera om all den här informationen i ett 2D-`numpy`-array.

Du har en Python-lista av listor. I den här listan representerar varje underlista längden och vikten för en enskild basebollspelare. Listan heter `baseball` och har redan laddats in åt dig (även om du inte kan se den).

Lagra datan som ett 2D-array för att få tillgång till `numpy`s utökade funktionalitet.

`@instructions`
- Använd `np.array()` för att skapa ett 2D-`numpy`-array från `baseball`. Döp det till `np_baseball`.
- Skriv ut attributet `shape` för `np_baseball`.

`@hint`
- `baseball` finns redan tillgänglig i Python-miljön. Anropa `np.array()` på den och lagra det resulterande 2D-`numpy`-arrayet i `np_baseball`.
- `np_baseball.shape` ger dimensionerna för `np_baseball`. Se till att omge anropet med `print()`.

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

success_msg("Snyggt! Dags att visa upp några fantastiska funktioner hos flerdimensionella `numpy`-arrayer!")
```

---

## Subsetting av 2D NumPy-arrayer

```yaml
type: NormalExercise
key: aeca4977f0
lang: python
xp: 100
skills:
  - 2
```

Om din 2D-array i `numpy` har en regelbunden struktur – det vill säga att varje rad och kolumn har ett fast antal värden – blir avancerade sätt att ta ut delmängder mycket enkla. Titta på koden nedan där elementen `"a"` och `"c"` hämtas ut från en lista av listor.

```
# numpy
import numpy as np
np_x = np.array(x)
np_x[:, 0]
```

Indexen före kommatecknet avser raderna, medan de efter kommatecknet avser kolumnerna. Tecknet `:` används för slicing; i det här exemplet anger det att Python ska inkludera alla rader.

`@instructions`
- Skriv ut den 50:e raden i `np_baseball`.
- Skapa en ny variabel, `np_weight_lb`, som innehåller hela den andra kolumnen i `np_baseball`.
- Välj ut längden (första kolumnen) för den 124:e basebollspelaren i `np_baseball` och skriv ut den.

`@hint`
- Du behöver radindex 49 i den första instruktionen! Mer specifikt vill du använda `[49, :]`.
- För att markera hela den andra kolumnen behöver du `[:, 1]`.
- I den sista instruktionen använder du `[123, 0]`; glöm inte att omsluta allt i ett `print()`-anrop.

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
msg = "Du behöver inte ändra eller ta bort de fördefinierade variablerna."
Ex().multi(
    has_import("numpy", same_as = False),
    check_object("np_baseball", missing_msg=msg).has_equal_value(incorrect_msg = msg)
)

Ex().has_printout(0)

Ex().check_object('np_weight_lb').has_equal_value(incorrect_msg = "Du kan använda `np_baseball[:,1]` för att definiera `np_weight_lb`. Detta väljer hela den första kolumnen.")

Ex().has_printout(1)

success_msg("Det går bra!")
```

---

## 2D-aritmetik

```yaml
type: NormalExercise
key: 1c2378b677
lang: python
xp: 100
skills:
  - 2
```

2D `numpy`-arrayer kan utföra beräkningar element för element, precis som vanliga `numpy`-arrayer.

`np_baseball` är redan definierad – det är återigen en 2D `numpy`-array med 3 kolumner som representerar längd (i tum), vikt (i pund) och ålder (i år). `baseball` finns tillgänglig som en vanlig lista av listor och `updated` finns tillgänglig som en 2D numpy-array.

`@instructions`
- Du har lyckats få tag på förändringarna i längd, vikt och ålder för alla basebollspelare. Det finns tillgängligt som en 2D `numpy`-array, `updated`. Addera `np_baseball` och `updated` och skriv ut resultatet.
- Du vill konvertera enheterna för längd och vikt till metriska enheter (meter respektive kilogram). Som ett första steg skapar du en `numpy`-array med tre värden: `0.0254`, `0.453592` och `1`. Namnge denna array `conversion`.
- Multiplicera `np_baseball` med `conversion` och skriv ut resultatet.

`@hint`
- `np_baseball + updated` utför en elementvis summering av de två `numpy`-arrayerna.
- Skapa en `numpy`-array med `np.array()`; indata är en vanlig Python-lista med tre element.
- `np_baseball * conversion` fungerar direkt, utan extra steg. Prova det! Kom ihåg att omsluta det med ett `print()`-anrop.

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

msg = "Du behöver inte ändra eller ta bort de fördefinierade variablerna."
Ex().check_object("np_baseball", missing_msg=msg).has_equal_value(incorrect_msg = msg)

Ex().has_printout(0)

Ex().check_correct(
    has_printout(1),
    check_correct(
        check_object('conversion').has_equal_value(),
        check_function('numpy.array', index = 1).check_args(0).has_equal_value()
    )    
)

success_msg("Bra jobbat! Lägg märke till hur du med mycket lite kod kan ändra alla värden i din `numpy`-datastruktur på ett mycket specifikt sätt. Detta kommer att vara mycket användbart i din framtid som datavetare!")
```

---

## NumPy: Grundläggande statistik

```yaml
type: VideoExercise
key: 287995e488
xp: 50
```

`@projector_key`
34495ba457d74296794d2a122c9b6e19

---

## Medelvärde jämfört med median

```yaml
type: NormalExercise
key: 509c588eb6
lang: python
xp: 100
skills:
  - 2
```

Nu vet du hur du använder `numpy`-funktioner för att få en bättre förståelse för dina data.

Basebolldata finns tillgänglig som en 2D `numpy`-array med 3 kolumner (längd, vikt, ålder) och 1 015 rader. Namnet på denna `numpy`-array är `np_baseball`. När du strukturerar om data märker du dock att vissa längdvärden är ovanligt höga. Följ instruktionerna och undersök vilket sammanfattningsmått som passar bäst när du arbetar med så kallade _extremvärden_. `np_baseball` finns tillgänglig.

`@instructions`
- Skapa `numpy`-arrayen `np_height_in` som är lika med den första kolumnen i `np_baseball`.
- Skriv ut medelvärdet av `np_height_in`.
- Skriv ut medianen av `np_height_in`.

`@hint`
- Använd 2D-subsetting med `numpy`: `[:,0]` är en del av lösningen.
- Om `numpy` är importerat som `np` kan du använda `np.mean()` för att beräkna medelvärdet av en NumPy-array. Glöm inte att lägga till ett `print()`-anrop.
- För den sista instruktionen, använd `np.median()`.

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

Ex().check_object("np_height_in").has_equal_value(incorrect_msg = "Du kan använda `np_baseball[:,0]` för att välja den första kolumnen från `np_baseball`"),

Ex().check_correct(
    has_printout(0),
    check_function('numpy.mean').has_equal_value()
)

Ex().check_correct(
    has_printout(1),
    check_function('numpy.median').has_equal_value()
)

success_msg("Ett genomsnittligt längd på 1586 tum låter inte rätt, eller hur? Medianen verkar dock inte påverkas av extremvärdena: 74 tum är fullt rimligt. Det är alltid en bra idé att kontrollera både medianen och medelvärdet för att få en uppfattning om den övergripande fördelningen av hela datamängden.")
```

---

## Utforska basebolldata

```yaml
type: NormalExercise
key: '4409948807'
lang: python
xp: 100
skills:
  - 2
```

Eftersom medelvärdet och medianen skiljer sig så mycket åt bestämmer du dig för att klaga hos MLB. De hittar felet och skickar korrigerad data till dig. Den är åter tillgänglig som ett 2D NumPy-array `np_baseball`, med tre kolumner.

Python-skriptet i editorn innehåller redan kod för att skriva ut informativa meddelanden med de olika sammanfattande statistikvärdena, och `numpy` är redan inläst som `np`. Kan du slutföra uppgiften? `np_baseball` är tillgänglig.

`@instructions`
- Koden för att skriva ut medelhöjden finns redan. Komplettera koden för medianhöjden.
- Använd `np.std()` på den första kolumnen i `np_baseball` för att beräkna `stddev`.
- Tenderar stora spelare att också vara tyngre? Använd `np.corrcoef()` för att lagra korrelationen mellan den första och andra kolumnen i `np_baseball` i `corr`.

`@hint`
- Använd `np.median()` för att beräkna medianen. Se till att du väljer rätt kolumn först!
- Välj samma kolumn när du beräknar standardavvikelsen med `np.std()`.
- Använd `np_baseball[:, 0]` och `np_baseball[:, 1]` för att välja den första och andra kolumnen – dessa är indata till `np.corrcoef()`.

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
msg = "Du bör inte ändra eller ta bort den fördefinierade variabeln `avg`."
Ex().check_object("avg", missing_msg=msg).has_equal_value(incorrect_msg=msg)

missing = "Har du använt `np.median()` för att beräkna medianen?"
incorrect = "För att beräkna `med`, skicka den första kolumnen av `np_baseball` till `numpy.median()`. Exemplet med `np.mean()` visar hur det går till."
Ex().check_correct(
  check_object("med").has_equal_value(),
  check_function("numpy.median", index=0, missing_msg=missing).check_args(0).has_equal_value(incorrect_msg=incorrect)
)

missing = "Har du använt `np.std()` för att beräkna standardavvikelsen?"
incorrect = "För att beräkna `stddev`, skicka den första kolumnen av `np_baseball` till `numpy.std()`. Exemplet med `np.mean()` visar hur det går till."
Ex().check_correct(
  check_object("stddev").has_equal_value(),
  check_function("numpy.std", index=0, missing_msg=missing).check_args(0).has_equal_value(incorrect_msg=incorrect)
)

missing = "Har du använt `np.corrcoef()` för att beräkna korrelationen?"
incorrect1 = "För att beräkna `corr` ska det första argumentet till `np.corrcoef()` vara den första kolumnen av `np_baseball`, på liknande sätt som tidigare."
incorrect2 = "För att beräkna `corr` ska det andra argumentet till `np.corrcoef()` vara den andra kolumnen av `np_baseball`. Använd `[:,1]` i stället för `[:,0]` den här gången."
Ex().check_correct(
  check_object("corr").has_equal_value(),
  check_function("numpy.corrcoef", index=0, missing_msg=missing).multi(
    check_args(0, missing_msg=incorrect1).has_equal_value(incorrect_msg=incorrect1),
    check_args(1, missing_msg=incorrect2).has_equal_value(incorrect_msg=incorrect2)
  )
)

success_msg("Utmärkt arbete! Du har byggt en solid grund – nu är det dags att använda alla dina nya datavetenskapliga färdigheter för att lösa fler utmaningar och göra skillnad.")
```

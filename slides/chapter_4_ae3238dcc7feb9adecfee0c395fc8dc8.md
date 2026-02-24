---
title: Insert title here
key: ae3238dcc7feb9adecfee0c395fc8dc8
video_link:
  mp3: >-
    https://videos.datacamp.com/mp3/translations/course_735/nl-NL/30044d1f-2732-487f-be3e-2a4e8bc68982.mp3
---

## 2D NumPy-arrays

```yaml
type: TitleSlide
key: 0cc8abf493
```

`@lower_third`
name: Hugo Bowne-Anderson
title: Data Scientist at DataCamp

`@script`
Goed gedaan! Laten we nu de numpy-arrays uit de vorige video opnieuw maken.
---

## Type van NumPy-arrays

```yaml
type: FullSlide
key: 1b9db47fd2
code_zoom: 100
```

`@part1`
```py
import numpy as np
np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
np_weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])
```

```py
type(np_height)
```

```out
numpy.ndarray
```

```py
type(np_weight)
```

```out
numpy.ndarray
```

`@script`
Als je naar het type van deze arrays vraagt, vertelt Python je dat het numpy punt nd-array is. numpy punt geeft aan dat het een type is dat gedefinieerd is in het numpy-pakket. nd-array staat voor n-dimensionale array. De arrays np_height en np_weight zijn eendimensionale arrays, maar je kunt prima tweedimensionale, driedimensionale, zelfs zevendimensionale arrays maken! In deze video houden we het echter bij twee.
---

## 2D NumPy-arrays

```yaml
type: FullSlide
key: ebb550dcba
code_zoom: 71
```

`@part1`
```py
np_2d = np.array([[1.73, 1.68, 1.71, 1.89, 1.79],
                  [65.4, 59.2, 63.6, 88.4, 68.7]])
```{{1}}
```py
np_2d
```{{2}}

```out
array([[ 1.73,  1.68,  1.71,  1.89,  1.79],
       [65.4 , 59.2 , 63.6 , 88.4 , 68.7 ]])
```{{2}}

```py
np_2d.shape
```{{3}}

```out
(2, 5) # 2 rows, 5 columns
```{{3}}

```py
np.array([[1.73, 1.68, 1.71, 1.89, 1.79],
          [65.4, 59.2, 63.6, 88.4, "68.7"]])
```{{4}}

```out
array([['1.73', '1.68', '1.71', '1.89', '1.79'],
       ['65.4', '59.2', '63.6', '88.4', '68.7']], dtype='<U32')
```{{4}}

`@script`
Je kunt een tweedimensionale numpy-array maken van een gewone Python-lijst van lijsten. Laten we proberen één numpy-array te maken voor alle lengte- en gewichtgegevens van je gezin.

Als je np-2d nu afdrukt, zie je dat het een rechthoekige datastructuur is: elke sublijst in de lijst komt overeen met een rij in de tweedimensionale numpy-array. Aan np-2d punt shape zie je dat we inderdaad twee rijen en vijf kolommen hebben. shape is een attribuut van de np-2d-array, dat je meer informatie kan geven over hoe de datastructuur eruitziet.

Let op dat de syntaxis voor het benaderen van een attribuut een beetje lijkt op het aanroepen van een methode, maar ze zijn niet hetzelfde! Onthoud dat methoden ronde haakjes erachter hebben, en, zoals je hier ziet, attributen niet.

Ook voor tweedimensionale arrays geldt de NumPy-regel: een array kan slechts één type bevatten. Als je één float verandert in een string, worden alle array-elementen naar strings omgezet, zodat je een homogene array overhoudt.
---

## Subsets maken

```yaml
type: FullSlide
key: e71d2fc8b8
code_zoom: 80
```

`@part1`
```out
           0       1       2       3       4
           
array([[  1.73,   1.68,   1.71,   1.89,   1.79],     0
       [  65.4,   59.2,   63.6,   88.4,   68.7]])    1
```

```py
np_2d[0]
```

```out
array([1.73, 1.68, 1.71, 1.89, 1.79])
```

`@script`
Je kunt de tweedimensionale numpy-array zien als een verbeterde lijst-van-lijsten: je kunt berekeningen op de arrays uitvoeren, zoals ik eerder liet zien, en je kunt geavanceerdere manieren van subsetting gebruiken.

Stel dat je de eerste rij wilt, en vervolgens het derde element in die rij. Om de rij te selecteren, heb je de index nul tussen vierkante haken nodig. Vergeet de nul-indexering niet.

Om daarna het derde element te kiezen, kun je dezelfde aanroep uitbreiden met nog een paar haken, dit keer met index twee,
---

## Subsets maken

```yaml
type: FullSlide
key: 57a1fb1581
disable_transition: true
code_zoom: 80
```

`@part1`
```out
           0       1       2       3       4
           
array([[  1.73,   1.68,   1.71,   1.89,   1.79],     0
       [  65.4,   59.2,   63.6,   88.4,   68.7]])    1
```

```py
np_2d[0][2]
```

```out
1.71
```

```py
np_2d[0, 2]
```{{1}}

```out
1.71
```{{1}}

`@script`
zo. In feite selecteer je eerst de rij, en doe je vervolgens vanuit die rij nog een selectie.

Er is ook een alternatieve manier van subsetting, met één paar vierkante haken en een komma. Deze aanroep geeft exact dezelfde waarde als daarnet. De waarde vóór de komma specificeert de rij, de waarde na de komma specificeert de kolom. De doorsnede van de opgegeven rijen en kolommen wordt teruggegeven. Als je eraan gewend bent, is deze syntaxis intuïtiever en biedt hij meer mogelijkheden.
---

## Subsets maken

```yaml
type: FullSlide
key: feb75c975c
disable_transition: true
code_zoom: 80
```

`@part1`
```out
           0       1       2       3       4
           
array([[  1.73,   1.68,   1.71,   1.89,   1.79],     0
       [  65.4,   59.2,   63.6,   88.4,   68.7]])    1
```

```py
np_2d[:, 1:3]
```{{1}}

```out
array([[ 1.68,  1.71],
       [59.2 , 63.6 ]])
```{{1}}

```py
np_2d[1, :]
```{{2}}

```out
array([65.4, 59.2, 63.6, 88.4, 68.7])
```{{2}}

`@script`
Stel dat je de lengte en het gewicht van het tweede en derde gezinslid wilt selecteren. Je wilt beide rijen, dus zet je een dubbele punt vóór de komma. Je wilt alleen de tweede en derde kolom, dus zet je de indices één tot drie na de komma. Denk eraan dat de derde index hier niet wordt meegenomen. De doorsnede levert een tweedimensionale array op met twee rijen en twee kolommen:

Op dezelfde manier kun je het gewicht van alle gezinsleden selecteren: je wilt alleen de tweede rij, dus zet je één vóór de komma. Je wilt alle kolommen, dus gebruik je een dubbele punt na de komma. De doorsnede geeft ons de volledige tweede rij.

Tot slot kun je met tweedimensionale numpy-arrays elementgewijze berekeningen doen, net zoals je dat deed met eendimensionale numpy-arrays. Dat is iets
---

## Laten we oefenen!

```yaml
type: FinalSlide
key: 6047b27c09
```

`@script`
waarmee je in de oefeningen kunt experimenteren, samen met het maken en subsetten van tweedimensionale numpy-arrays!

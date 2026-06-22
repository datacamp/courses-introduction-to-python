---
title: Insert title here
key: ae3238dcc7feb9adecfee0c395fc8dc8
video_link:
  mp3: >-
    https://videos.datacamp.com/mp3/translations/course_735/sv-SE/1438ff3c-a630-4b79-a0ac-b1b5a08be091-d77cffcc592b25aff4bf12a35f7b5add.mp3
---

## 2D NumPy-arrayer

```yaml
type: TitleSlide
key: 0cc8abf493
```

`@lower_third`
name: Hugo Bowne-Anderson
title: Data Scientist at DataCamp

`@script`
Bra jobbat! Nu ska vi återskapa numpy-arrayerna från föregående video.

---

## Typ av NumPy-arrayer

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
Om du frågar efter typen för dessa arrayer, svarar Python att de är numpy.ndarray. numpy punkt berättar att det är en typ som definierats i paketet numpy. ndarray står för n-dimensionell array. Arrayerna np_height och np_weight är endimensionella, men det går utmärkt att skapa 2-dimensionella, tredimensionella, ja till och med sjudimensionella arrayer! I den här videon håller vi oss till 2 dimensioner.

---

## 2D NumPy-arrayer

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
Du kan skapa en tvådimensionell numpy-array från en vanlig Python-lista av listor. Vi skapar en numpy-array med all längd- och viktdata för din familj, så här.

Om du skriver ut np_2d ser du att det är en rektangulär datastruktur. Varje underlista i listan motsvarar en rad i den tvådimensionella numpy-arrayen. Via np_2d.shape kan du se att vi har 2 rader och 5 kolumner. shape är ett så kallat attribut på np_2d-arrayen, som ger dig mer information om hur datastrukturen ser ut.

Notera att syntaxen för att komma åt ett attribut liknar ett metodanrop, men de är inte samma sak. Kom ihåg att metoder har runda parenteser efter sig, och som du ser här har attribut det inte.

NumPy-regeln gäller även för tvådimensionella arrayer: en array kan bara innehålla en enda typ. Om du ändrar ett flyttal till en sträng, omvandlas alla element i arrayen till strängar, så att arrayen förblir homogen.

---

## Subsetting

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
Du kan se den tvådimensionella numpy-arrayen som en förbättrad lista av listor. Du kan utföra beräkningar på arrayerna, som jag visade tidigare, och du kan använda mer avancerade sätt att välja ut data.

Säg att du vill ha den första raden och sedan det tredje elementet i den raden. För att välja raden anger du index 0 inom hakparenteser. Glöm inte nollindexeringen.

För att sedan välja det tredje elementet utökar du anropet med ytterligare ett par hakparenteser, den här gången med index 2.

---

## Subsetting

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
Så här. Du väljer alltså först raden och gör sedan ett nytt urval inom den raden.

Det finns också ett alternativt sätt att välja ut data, med enkla hakparenteser och ett kommatecken. Det här anropet returnerar exakt samma värde som tidigare. Värdet före kommat anger raden, och värdet efter kommat anger kolumnen. Det som returneras är skärningspunkten mellan de rader och kolumner du angett. När du väl vant dig är den här syntaxen mer intuitiv och öppnar upp fler möjligheter.

---

## Subsetting

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
Säg att du vill välja längd och vikt för den andra och tredje familjemedlemmen. Du vill ha båda raderna, så du anger ett kolon före kommat. Du vill bara ha den andra och tredje kolumnen, så du anger index 1 till 3 efter kommat. Kom ihåg att det tredje indexet inte inkluderas. Skärningspunkten ger oss en tvådimensionell array med 2 rader och 2 kolumner.

På samma sätt kan du välja vikten för alla familjemedlemmar så här. Du vill bara ha den andra raden, så du anger 1 före kommat. Du vill ha alla kolumner, så du använder ett kolon efter kommat. Skärningspunkten ger oss hela den andra raden.

Tvådimensionella numpy-arrayer gör det också möjligt att utföra elementvisa beräkningar, precis som med endimensionella numpy-arrayer. Det är något

---

## Nu kör vi en övning!

```yaml
type: FinalSlide
key: 6047b27c09
```

`@script`
du kan prova i övningarna, tillsammans med att skapa och välja ut data ur tvådimensionella numpy-arrayer!

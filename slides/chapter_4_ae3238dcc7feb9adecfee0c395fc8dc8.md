---
title: Insert title here
key: ae3238dcc7feb9adecfee0c395fc8dc8
video_link:
  mp3: >-
    https://videos.datacamp.com/mp3/translations/course_735/pl-PL/01fe1c51-e7a7-48ae-9c28-3301e47fb40f-5f0c92679548e02822af3749ab71882a.mp3
---

## Tablice 2D NumPy

```yaml
type: TitleSlide
key: 0cc8abf493
```

`@lower_third`
name: Hugo Bowne-Anderson
title: Data Scientist at DataCamp

`@script`
Świetna robota! Odtwórzmy teraz tablice numpy z poprzedniego filmu.

---

## Typ tablic NumPy

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
Jeśli sprawdzisz typ tych tablic, Python powie ci, że to numpy.ndarray. Człon numpy z kropką oznacza, że typ ten został zdefiniowany w pakiecie numpy. Skrót ndarray pochodzi od angielskiego „n-dimensional array", czyli tablica n-wymiarowa. Tablice np_height i np_weight są jednowymiarowe, ale równie dobrze możesz tworzyć tablice dwu-, trzy-, a nawet siedmiowymiarowe! W tym filmie zostaniemy jednak przy dwóch wymiarach.

---

## Tablice 2D NumPy

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
Tablicę numpy 2D możesz utworzyć ze zwykłej listy list w Pythonie. Spróbujmy stworzyć jedną tablicę numpy zawierającą dane o wzroście i wadze całej twojej rodziny, w taki sposób.

Jeśli teraz wyświetlisz np_2d, zobaczysz, że to prostokątna struktura danych. Każda podlista odpowiada jednemu wierszowi w dwuwymiarowej tablicy numpy. Z wartości np_2d.shape wynika, że mamy dokładnie 2 wiersze i 5 kolumn. shape to tak zwany atrybut tablicy np_2d, który pozwala dowiedzieć się więcej o strukturze danych.

Zwróć uwagę, że składnia dostępu do atrybutu wygląda trochę jak wywołanie metody, ale to nie to samo! Pamiętaj, że metody mają po sobie okrągłe nawiasy, a atrybuty, jak widzisz, nie mają.

Dla tablic 2D obowiązuje ta sama reguła numpy: tablica może zawierać tylko jeden typ danych. Jeśli zmienisz jeden element zmiennoprzecinkowy na łańcuch znaków, wszystkie elementy tablicy zostaną przekształcone na łańcuchy, żeby zachować jednorodność tablicy.

---

## Indeksowanie

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
Tablicę numpy 2D możesz traktować jak ulepszoną listę list. Możesz wykonywać na niej obliczenia, tak jak pokazywałem wcześniej, a poza tym masz do dyspozycji bardziej zaawansowane sposoby indeksowania.

Powiedzmy, że chcesz pobrać pierwszy wiersz, a z niego trzeci element. Żeby wybrać wiersz, podaj indeks 0 w nawiasach kwadratowych. Pamiętaj o indeksowaniu od zera.

Następnie, żeby wybrać trzeci element, rozszerz to samo wywołanie o kolejną parę nawiasów kwadratowych, tym razem z indeksem 2.

---

## Indeksowanie

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
W ten sposób. W praktyce wybierasz najpierw wiersz, a potem wykonujesz kolejne indeksowanie wewnątrz niego.

Istnieje też alternatywny sposób indeksowania z użyciem pojedynczych nawiasów kwadratowych i przecinka. To wywołanie zwraca dokładnie tę samą wartość co poprzednie. Wartość przed przecinkiem wskazuje wiersz, a wartość po przecinku wskazuje kolumnę. W wyniku otrzymujesz element leżący na ich przecięciu. Gdy się do tego przyzwyczaisz, ta składnia okaże się bardziej intuicyjna i da ci więcej możliwości.

---

## Indeksowanie

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
Powiedzmy, że chcesz wybrać wzrost i wagę drugiego oraz trzeciego członka rodziny. Potrzebujesz obu wierszy, więc przed przecinkiem wstawiasz dwukropek. Chcesz tylko drugą i trzecią kolumnę, więc po przecinku podajesz indeksy od 1 do 3. Pamiętaj, że element o indeksie 3 nie jest uwzględniany. W wyniku otrzymujesz tablicę 2D z 2 wierszami i 2 kolumnami.

Podobnie możesz wybrać wagę wszystkich członków rodziny w taki sposób. Potrzebujesz tylko drugiego wiersza, więc przed przecinkiem wstawiasz 1. Chcesz wszystkie kolumny, więc po przecinku dajesz dwukropek. W wyniku otrzymujesz cały drugi wiersz.

Na koniec warto dodać, że tablice numpy 2D umożliwiają obliczenia wykonywane element po elemencie, dokładnie tak samo jak tablice jednowymiarowe. To coś,

---

## Czas na ćwiczenia!

```yaml
type: FinalSlide
key: 6047b27c09
```

`@script`
z czym możesz poeksperymentować w ćwiczeniach, razem z tworzeniem i indeksowaniem tablic numpy 2D. Do dzieła!

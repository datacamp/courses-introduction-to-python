---
title: Insert title here
key: 433dcfcfedaee070cbf440491c402e3b
video_link:
  mp3: >-
    https://videos.datacamp.com/mp3/translations/course_735/pl-PL/bc2c176e-2d0c-49bd-932c-016d80c93a45-a6fcdf2375003ba92664d12edb90385c.mp3
---

## Zmienne i typy

```yaml
type: TitleSlide
key: dc8b62f1c8
```

`@lower_third`
name: Hugo Bowne-Anderson
title: Data Scientist at DataCamp

`@script`
Świetna robota i witaj z powrotem! Python to naprawdę doskonałe narzędzie do obliczeń. Jeśli jednak chcesz wykonywać bardziej złożone obliczenia, przyda ci się możliwość „zapisywania" wartości podczas pisania kodu.

---

## Zmienna

```yaml
type: FullSlide
key: 36ec318b41
```

`@part1`
- Specyficzna, uwzględniająca wielkość liter nazwa

- Dostęp do wartości przez nazwę zmiennej{{1}}

- 1,79 m – 68,7 kg{{2}}

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
Możesz to zrobić, definiując zmienną o konkretnej, uwzględniającej wielkość liter nazwie. Gdy już ją utworzysz, możesz później odwołać się do jej wartości, wpisując tę nazwę.

Wyobraź sobie, że mierzysz swój wzrost i wagę w jednostkach metrycznych. Masz 1,79 metra wzrostu i ważysz 68,7 kilograma. Możesz przypisać te wartości do dwóch zmiennych, o nazwach height i weight, używając znaku równości.

Jeśli teraz wpiszesz nazwę zmiennej height,

Python wyszuka tę zmienną, pobierze jej wartość i wyświetli ją na ekranie.

---

## Obliczanie BMI

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
Teraz obliczmy wskaźnik masy ciała, czyli BMI, który wyznacza się na podstawie wagi w kilogramach i wzrostu w metrach. Możesz użyć do tego konkretnych liczb, ale równie dobrze możesz sięgnąć po zmienne height i weight, tak jak tutaj. Za każdym razem, gdy wpisujesz nazwę zmiennej, prosisz Pythona, żeby zastąpił ją jej rzeczywistą wartością. Zmienna weight odpowiada wartości 68,7, a height wartości 1,79.

Na koniec ta wersja kodu każe Pythonowi zapisać wynik w nowej zmiennej bmi. Zmienna bmi zawiera teraz tę samą wartość, którą wcześniej obliczyłeś.

W Pythonie zmienne są używane nieustannie. Pomagają sprawić, żeby kod był łatwy do ponownego uruchomienia i odtworzenia.

---

## Odtwarzalność

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
Załóżmy, że kod tworzący zmienne height, weight i bmi znajduje się w skrypcie, tak jak tutaj. Jeśli teraz chcesz ponownie obliczyć BMI dla innej wagi,

---

## Odtwarzalność

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
wystarczy zmienić deklarację zmiennej weight i uruchomić skrypt jeszcze raz. Wartość bmi zmieni się odpowiednio, ponieważ zmieniła się wartość zmiennej weight.

Do tej pory pracowaliśmy wyłącznie z wartościami liczbowymi, takimi jak wzrost i waga.

---

## Typy w Pythonie

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
W Pythonie każda liczba ma określony typ. Możesz sprawdzić typ wartości za pomocą funkcji type. Żeby zobaczyć typ zmiennej bmi, wystarczy napisać type, a w nawiasach podać bmi. Widać, że to float, czyli sposób, w jaki Python reprezentuje liczbę rzeczywistą, a więc taką, która może mieć zarówno część całkowitą, jak i ułamkową. Python ma też typ dla liczb całkowitych, czyli int, tak jak w tym przykładzie.

Do pracy z danymi potrzebujesz jednak czegoś więcej niż tylko typów int i float.

---

## Typy w Pythonie (2)

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
Python oferuje wiele innych typów danych. Najczęściej używane to ciągi znaków i wartości logiczne.

Ciąg znaków, czyli string, to sposób Pythona na reprezentowanie tekstu. Możesz używać zarówno cudzysłowów podwójnych, jak i apostrofów, żeby tworzyć string, jak widać w tych przykładach. Jeśli sprawdzisz typ ostatniej zmiennej, zobaczysz, że to str, skrót od słowa string.

Typ Boolean może przyjmować wartość True albo False, czyli prawda albo fałsz. Możesz myśleć o nim jak o odpowiedzi „tak" lub „nie" w codziennym języku. Wartości logiczne będą bardzo przydatne w przyszłości, na przykład do filtrowania danych.

Jest jeszcze jedna ciekawa właściwość typów danych w Pythonie.

---

## Typy w Pythonie (3)

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

- Różny typ = różne zachowanie!{{3}}

`@script`
Przyjrzyj się tej linii kodu, która sumuje dwie liczby całkowite, a następnie tej, która sumuje dwa ciągi znaków.

Dla liczb całkowitych wartości zostały dodane do siebie, natomiast dla ciągów znaków zostały one ze sobą połączone. Operator plus zachował się inaczej dla różnych typów danych. To ogólna zasada: działanie kodu zależy od typów, z którymi pracujesz.

W kolejnych ćwiczeniach stworzysz swoje pierwsze zmienne i poeksperymentujesz z typami danych w Pythonie. Do zobaczenia w następnym filmie, gdzie opowiem ci wszystko o listach.

---

## Czas na ćwiczenia!

```yaml
type: FinalSlide
key: b7fc40db4d
```

`@script`
Czas na kodowanie! Nie mogę się doczekać, żeby zobaczyć cię w następnym rozdziale, gdzie stworzysz jeszcze bardziej zaawansowane wykresy w Pythonie.

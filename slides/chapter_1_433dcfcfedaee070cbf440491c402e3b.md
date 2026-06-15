---
title: Insert title here
key: 433dcfcfedaee070cbf440491c402e3b
video_link:
  mp3: >-
    https://videos.datacamp.com/mp3/translations/course_735/ro-RO/271ccdbe-23fd-411d-a941-70e81bf8022b-1112e002ecf06d1fdc767d07b998b341.mp3
---

## Variabile și tipuri

```yaml
type: TitleSlide
key: dc8b62f1c8
```

`@lower_third`
name: Hugo Bowne-Anderson
title: Data Scientist at DataCamp

`@script`
Felicitări și bine ai revenit! E clar că Python este un calculator excelent. Dacă vrei să faci calcule mai complexe, însă, vei vrea să „salvezi" valorile pe parcurs.

---

## Variabilă

```yaml
type: FullSlide
key: 36ec318b41
```

`@part1`
- Nume specific, sensibil la majuscule

- Accesați valoarea prin numele variabilei{{1}}

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
Poți face asta definind o variabilă, cu un nume specific, care ține cont de majuscule și minuscule. Odată ce creezi sau declari o variabilă, îi poți accesa valoarea mai târziu, scriind numele ei.

Să presupunem că îți măsori înălțimea și greutatea în unități metrice: ai 1,79 metri înălțime și cântărești 68,7 kilograme. Poți atribui aceste valori la două variabile, numite height și weight, folosind semnul egal.

Dacă acum scrii numele variabilei, height,

Python caută variabila, îi recuperează valoarea și o afișează.

---

## Calculați IMC

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
Hai să calculăm acum Indicele de Masă Corporală, sau BMI, calculat după formula următoare, cu greutatea în kilograme și înălțimea în metri. Poți face asta cu valorile directe, dar poți la fel de bine să folosești variabilele height și weight, ca în exemplul de aici. De fiecare dată când scrii numele unei variabile, îi ceri lui Python să o înlocuiască cu valoarea ei reală. weight corespunde valorii 68,7, iar height valorii 1,79.

În final, această versiune îi spune lui Python să stocheze rezultatul într-o nouă variabilă, bmi. Variabila bmi conține acum aceeași valoare pe care ai calculat-o mai devreme.

În Python, variabilele sunt folosite tot timpul. Ele te ajută să îți faci codul reutilizabil.

---

## Reproductibilitate

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
Să presupunem că instrucțiunile pentru crearea variabilelor height, weight și bmi se află într-un script, ca acesta. Dacă vrei acum să recalculezi bmi pentru o altă greutate,

---

## Reproductibilitate

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
poți pur și simplu să modifici declarația variabilei weight și să rulezi din nou scriptul. Valoarea bmi se actualizează corespunzător, pentru că și valoarea variabilei weight s-a schimbat.

Până acum am lucrat doar cu valori numerice, precum înălțimea și greutatea.

---

## Tipuri Python

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
În Python, aceste numere au fiecare un tip specific. Poți verifica tipul unei valori cu funcția type. Ca să vezi tipul variabilei bmi, scrie pur și simplu type, apoi bmi între paranteze. Vei vedea că este un float, adică modul în care Python reprezintă un număr real, un număr care poate avea atât parte întreagă, cât și parte zecimală. Python are și un tip pentru numere întregi: int, ca în exemplul de aici.

Pentru a lucra cu date, vei avea nevoie de mai mult decât int și float, însă.

---

## Tipuri Python (2)

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
Python oferă o mulțime de alte tipuri de date. Cele mai comune sunt șirurile de caractere și valorile booleene.

Un șir de caractere, sau string, este modul în care Python reprezintă text. Poți folosi atât ghilimele duble, cât și ghilimele simple pentru a construi un string, după cum poți vedea în aceste exemple. Dacă afișezi tipul ultimei variabile, vei vedea că este str, prescurtare de la string.

Tipul boolean poate fi fie True, fie False. Îl poți gândi ca pe un „Da" sau „Nu" din limbajul de zi cu zi. Valorile booleene vor fi foarte utile mai târziu, de exemplu pentru a filtra datele.

Există ceva special în legătură cu tipurile de date din Python.

---

## Tipuri Python (3)

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

- Tipuri diferite = comportament diferit!{{3}}

`@script`
Uită-te la această linie de cod, care adună două numere întregi, și apoi la această linie, care adună două șiruri de caractere.

În cazul numerelor întregi, valorile au fost sumate, iar în cazul șirurilor de caractere, acestea au fost concatenate. Operatorul plus s-a comportat diferit în funcție de tipul de date. Acesta este un principiu general: modul în care se comportă codul depinde de tipurile cu care lucrezi.

În exercițiile care urmează, vei crea primele tale variabile și vei experimenta cu câteva tipuri de date din Python. Ne vedem în videoclipul următor, unde vei afla totul despre liste.

---

## Să exersăm!

```yaml
type: FinalSlide
key: b7fc40db4d
```

`@script`
Hai să trecem la cod și abia aștept să te văd în capitolul următor, unde vei crea grafice Python și mai interesante.

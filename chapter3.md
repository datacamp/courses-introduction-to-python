---
title_meta: Capitolul 3
title: Funcții și pachete
description: >-
  Vei învăța cum să folosești funcții, metode și pachete pentru a valorifica
  eficient codul scris de dezvoltatori Python talentați. Scopul este să reduci
  cantitatea de cod necesară pentru a rezolva probleme complexe!
attachments:
  slides_link: 'https://projector-video-pdf-converter.datacamp.com/735/chapter3.pdf'
lessons:
  - nb_of_exercises: 4
    title: Funcții
  - nb_of_exercises: 4
    title: Metode
  - nb_of_exercises: 4
    title: Pachete
---

## Funcții

```yaml
type: VideoExercise
key: 5c5f365930
xp: 50
```

`@projector_key`
1204d914b0e53100529827e07441ee6c

---

## Funcții familiare

```yaml
type: NormalExercise
key: c422ee929b
lang: python
xp: 100
skills:
  - 2
```

Python vine cu o serie de funcții integrate care îți fac viața de om de știință al datelor mai ușoară. Deja cunoști două dintre ele: `print()` și `type()`. Există și funcții precum `str()`, `int()`, `bool()` și `float()` pentru a converti între tipuri de date. Le poți descoperi [aici.](https://docs.python.org/3/library/functions.html) Și acestea sunt funcții integrate.

Apelarea unei funcții este simplă. Pentru a obține tipul valorii `3.0` și a stoca rezultatul într-o variabilă nouă, `result`, poți folosi:

```
result = type(3.0)
```

`@instructions`
- Folosește `print()` împreună cu `type()` pentru a afișa tipul variabilei `var1`.
- Folosește `len()` pentru a obține [lungimea listei](https://docs.python.org/3/library/functions.html#len) `var1`. Include-o într-un apel `print()` pentru a o afișa direct.
- Folosește `int()` pentru a converti `var2` la un număr [întreg](https://docs.python.org/3/library/functions.html#int). Stochează rezultatul în `out2`.

`@hint`
- Apelează funcția `type()` astfel: `type(var1)`.
- Apelează `print()` așa cum ai făcut de multe ori până acum. Pune pur și simplu variabila pe care vrei să o afișezi între paranteze.
- `int(x)` va converti `x` la un număr întreg.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create variables var1 and var2
var1 = [1, 2, 3, 4]
var2 = True

# Print out type of var1
____

# Print out length of var1
____

# Convert var2 to an integer: out2
out2 = ____
```

`@solution`
```{python}
# Create variables var1 and var2
var1 = [1, 2, 3, 4]
var2 = True

# Print out type of var1
print(type(var1))

# Print out length of var1
print(len(var1))

# Convert var2 to an integer: out2
out2 = int(var2)
```

`@sct`
```{python}
msg = "Nu trebuie să modificați sau să eliminați variabilele predefinite."
Ex().check_object("var1", missing_msg=msg).has_equal_value(incorrect_msg=msg)
Ex().check_object("var2", missing_msg=msg).has_equal_value(incorrect_msg=msg)

patt = "__JINJA__:Asigurați-vă că afișați %s al `var1` cu `{{sol_call}}`."
Ex().has_printout(0, not_printed_msg = patt % 'tipul')
Ex().has_printout(1, not_printed_msg = patt % 'lungimea')

int_miss_msg = "Ați folosit `int()` pentru a converti `var2` într-un număr întreg?"
int_incorr_msg = "Ați transmis `var2` către `int()`?"
Ex().check_correct(
  check_object("out2").has_equal_value(incorrect_msg="Ați apelat `int()` corect; acum asigurați-vă că atribuiți rezultatul acestui apel variabilei `out2`."),
  check_function("int", missing_msg=int_miss_msg).has_equal_value(incorrect_msg=int_incorr_msg)
)
success_msg("Excelent! Funcția `len()` este extrem de utilă; funcționează și pe șiruri de caractere pentru a număra numărul de caractere!")
```

---

## Ajutor!

```yaml
type: MultipleChoiceExercise
key: 679b852978
lang: python
xp: 50
skills:
  - 2
```

Poate că știi deja numele unei funcții Python, dar tot trebuie să îți dai seama cum s-o folosești. Ironic, pentru a obține informații despre o funcție, apelezi o altă funcție: `help()`. În IPython, poți folosi și `?` înainte de numele funcției.

De exemplu, pentru a obține ajutor despre funcția `max()`, poți folosi unul dintre aceste apeluri:

```
help(max)
?max
```

Folosește IPython Shell pentru a deschide [documentația](https://docs.python.org/3/library/functions.html#pow) funcției `pow()`. Fă asta tastând `?pow` sau `help(pow)` și apăsând **Enter**.

Care dintre următoarele afirmații este adevărată?

`@possible_answers`
- `pow()` primește trei argumente: `base`, `exp` și `mod`. Fără `mod`, funcția va returna o eroare.
- `pow()` primește trei argumente obligatorii: `base`, `exp` și `None`.
- `pow()` necesită argumentele `base` și `exp`; `mod` este opțional.
- `pow()` primește două argumente: `exp` și `mod`. Lipsa lui `exp` generează o eroare.

`@hint`
- Argumentele opționale sunt setate cu `=` la o valoare implicită, pe care funcția o va folosi dacă acel argument nu este specificat.

`@pre_exercise_code`
```{python}

```

`@sct`
```{python}
msg1 = "Nu chiar. `mod` are o valoare implicită care va fi utilizată dacă nu specificați o valoare."
msg2 = "Incorect. `None` este valoarea implicită pentru argumentul `mod`."
msg3 = "Perfect! Utilizarea `help()` vă poate ajuta să înțelegeți cum funcționează funcțiile, eliberându-le întregul potențial!"
msg4 = "Incorect. `pow()` acceptă trei argumente, dintre care unul are o valoare implicită."
Ex().has_chosen(3, [msg1, msg2, msg3, msg4])
```

---

## Argumente multiple

```yaml
type: NormalExercise
key: e30486d7c1
lang: python
xp: 100
skills:
  - 2
```

În exercițiul anterior, ai identificat argumentele opționale citind documentația cu `help()`. Acum vei aplica același procedeu pentru a modifica comportamentul funcției `sorted()`.

Aruncă o privire la [documentația](https://docs.python.org/3/library/functions.html#sorted) funcției `sorted()` tastând `help(sorted)` în Shell-ul IPython.

Vei vedea că `sorted()` acceptă trei argumente: `iterable`, `key` și `reverse`. În acest exercițiu, va trebui să specifici doar `iterable` și `reverse`, nu și `key`.

Au fost create două liste pentru tine.

Poți să le combini și să le sortezi în ordine descrescătoare?

`@instructions`
- Folosește `+` pentru a îmbina conținutul listelor `first` și `second` într-o nouă listă: `full`.
- Apelează `sorted()` pe `full` și specifică argumentul `reverse` cu valoarea `True`. Salvează lista sortată ca `full_sorted`.
- Încheie prin afișarea variabilei `full_sorted`.

`@hint`
- Adună `first` și `second` ca și cum ar fi două numere și atribuie rezultatul variabilei `full`.
- Folosește `sorted()` cu două argumente: `full` și `reverse=True`.
- Pentru a afișa o variabilă, folosește `print()`.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create lists first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# Paste together first and second: full
full = ____ + ____

# Sort full in descending order: full_sorted
full_sorted = ____

# Print out full_sorted
____
```

`@solution`
```{python}
# Create lists first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# Paste together first and second: full
full = first + second

# Sort full in descending order: full_sorted
full_sorted = sorted(full, reverse=True)

# Print out full_sorted
print(full_sorted)
```

`@sct`
```{python}
msg = "Nu trebuie să modificați sau să eliminați variabilele deja existente `first` și `second`."
Ex().multi(
  check_object("first", missing_msg=msg).has_equal_value(incorrect_msg=msg),
  check_object("second", missing_msg=msg).has_equal_value(incorrect_msg=msg)
)
Ex().check_correct(
  check_object("full_sorted").has_equal_value(incorrect_msg="Asigurați-vă că atribuiți rezultatul apelării `sorted()` variabilei `full_sorted`."),
  check_function("sorted").multi(
    check_args(0).has_equal_value(),
    check_args('reverse').has_equal_value()
  )
)

success_msg("Excelent! Continuați cu videoclipul despre metodele Python.")
```

---

## Metode

```yaml
type: VideoExercise
key: 2b66cb66b1
xp: 50
```

`@projector_key`
8e387776f3a264a745128b68aa8d8f83

---

## Metode pentru șiruri de caractere

```yaml
type: NormalExercise
key: 4039302ee0
lang: python
xp: 100
skills:
  - 2
```

Șirurile de caractere vin cu o mulțime de metode. Urmează instrucțiunile cu atenție pentru a descoperi câteva dintre ele. Dacă vrei să le explorezi mai în detaliu, poți oricând să scrii `help(str)` în Shell-ul IPython.

O variabilă `place` de tip șir de caractere a fost deja creată pentru a experimenta cu ea.

`@instructions`
- Aplică metoda `.upper()` pe `place` și stochează rezultatul în `place_up`. Folosește sintaxa pentru apelarea metodelor pe care ai învățat-o în videoclipul anterior.
- Afișează `place` și `place_up`. S-au modificat ambele?
- Afișează numărul de litere „o" din variabila `place` apelând `.count()` pe `place` și transmițând litera `'o'` ca argument metodei. Ne referim la variabila `place`, nu la cuvântul `"place"`!

`@hint`
- Poți apela metoda `.upper()` pe `place` fără niciun argument suplimentar.
- Pentru a afișa o variabilă `x`, scrie `print(x)`.
- Asigură-te că încadrezi apelul `place.count(____)` într-o funcție `print()` pentru a-l afișa.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# string to experiment with: place
place = "poolhouse"

# Use upper() on place
place_up = 

# Print out place and place_up



# Print out the number of o's in place

```

`@solution`
```{python}
# string to experiment with: place
place = "poolhouse"

# Use upper() on place
place_up = place.upper()

# Print out place and place_up
print(place)
print(place_up)

# Print out the number of o's in place
print(place.count('o'))
```

`@sct`
```{python}
msg = "Nu trebuie să modificați sau să eliminați variabilele predefinite."
Ex().check_object("place", missing_msg=msg).has_equal_value(incorrect_msg=msg)

patt = "Nu uitați să afișați `%s`."
Ex().has_printout(0, not_printed_msg=patt % "place")
Ex().check_correct(
    has_printout(1, not_printed_msg=patt % "place_up"),
    check_correct(
        check_object("place_up").has_equal_value(incorrect_msg="Atribuiți rezultatul apelului `place.upper()` variabilei `place_up`."),
        check_function("place.upper", signature=False)
    )
)    

# check count of place
Ex().check_correct(
  has_printout(2, not_printed_msg = "Ați calculat corect numărul de litere 'o' din `place`; acum asigurați-vă că încadrați apelul `place.count('o')` într-o funcție `print()` pentru a afișa rezultatul."),
  check_function("place.count", signature=False).check_args(0).has_equal_value()
)

success_msg("Bine! Observați din rezultatele afișate că metoda `upper()` nu modifică obiectul asupra căruia este apelată. Acest lucru va fi diferit pentru liste în exercițiul următor!")
```

---

## Metode pentru liste

```yaml
type: NormalExercise
key: 0dbe8ed695
lang: python
xp: 100
skills:
  - 2
```

Șirurile de caractere nu sunt singurul tip de date din Python care au metode asociate. Listele, numerele cu virgulă mobilă, numerele întregi și valorile booleene sunt și ele tipuri care vin cu o serie de metode utile. În acest exercițiu, vei experimenta cu:

- `.index()`, pentru a obține indexul primului element dintr-o listă care corespunde valorii introduse, și
- `.count()`, pentru a afla de câte ori apare un element într-o listă.

Vei lucra cu lista care conține suprafețele diferitelor încăperi ale unei case: `areas`.

`@instructions`
- Folosește metoda `.index()` pentru a obține indexul elementului din `areas` care este egal cu `20.0`. Afișează acest index.
- Apelează `.count()` pe `areas` pentru a afla de câte ori apare `9.50` în listă. Afișează și acest număr.

`@hint`
- Pentru a afișa indexul, învelește apelul `areas.index(___)` într-o funcție `print()`.
- Pentru a afișa de câte ori apare un element `x` în listă, învelește apelul `areas.count(___)` într-o funcție `print()`.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Print out the index of the element 20.0


# Print out how often 9.50 appears in areas

```

`@solution`
```{python}
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Print out the index of the element 20.0
print(areas.index(20.0))

# Print out how often 9.50 appears in areas
print(areas.count(9.50))
```

`@sct`
```{python}
predef_msg = "Nu trebuie să modificați sau să eliminați lista predefinită `areas`."

Ex().check_object("areas", missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg)

Ex().check_function("print", index=0).check_args(0).check_function('areas.index', signature=False).check_args(0).has_equal_value()


Ex().check_function("print", index=1).check_args(0).check_function('areas.count', signature=False).has_equal_value()

success_msg("Bine! Acestea au fost exemple de metode ale listei `list` care nu au modificat lista pe care au fost apelate.")
```

---

## Metode pentru liste (2)

```yaml
type: NormalExercise
key: 1fbeab82d0
lang: python
xp: 100
skills:
  - 2
```

Majoritatea metodelor pentru liste modifică lista asupra căreia sunt aplicate. Câteva exemple:

- `.append()`, care adaugă un element la lista pe care este apelată,
- `.remove()`, care [elimină](https://docs.python.org/3/library/stdtypes.html#typesseq-mutable) primul element din listă care corespunde argumentului dat, și
- `.reverse()`, care [inversează](https://docs.python.org/3/library/stdtypes.html#typesseq-mutable) ordinea elementelor din lista pe care este apelată.

Vei lucra cu lista care conține suprafețele diferitelor încăperi din casă: `areas`.

`@instructions`
- Folosește `.append()` de două ori pentru a adăuga din nou suprafața poolhouse-ului și a garajului: `24.5`, respectiv `15.45`. Asigură-te că le adaugi în această ordine.
- Afișează `areas`.
- Folosește metoda `.reverse()` pentru a inversa ordinea elementelor din `areas`.
- Afișează din nou `areas`.

`@hint`
- Pentru prima instrucțiune, folosește apelul `areas.append(___)` de două ori.
- Pentru a afișa o variabilă `x`, scrie pur și simplu `print(x)`.
- Metoda `.reverse()` nu necesită argumente suplimentare; folosește doar notația cu punct și paranteze goale: `.reverse()`.
- Pentru a afișa o variabilă `x`, scrie pur și simplu `print(x)`.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Use append twice to add poolhouse and garage size



# Print out areas


# Reverse the orders of the elements in areas


# Print out areas

```

`@solution`
```{python}
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Use append twice to add poolhouse and garage size
areas.append(24.5)
areas.append(15.45)

# Print out areas
print(areas)

# Reverse the orders of the elements in areas
areas.reverse()

# Print out areas
print(areas)
```

`@sct`
```{python}
Ex().multi(
  check_function("areas.append", index=0, signature=False).check_args(0).has_equal_value(),
  check_function("areas.append", index=1, signature=False).check_args(0).has_equal_value(),
  check_function("print", index=0).check_args(0).has_equal_ast(),
  check_function("areas.reverse", index=0, signature=False),
  check_function("print", index=1).check_args(0).has_equal_ast()
)

success_msg("Excelent!")
```

---

## Pachete

```yaml
type: VideoExercise
key: ab96a17c5e
xp: 50
```

`@projector_key`
cedcfb34350be8545599768f96695cdd

---

## Importă pachetul

```yaml
type: NormalExercise
key: 7432a6376f
lang: python
xp: 100
skills:
  - 2
```

Să zicem că vrei să calculezi circumferința și aria unui cerc. Iată cum arată formulele:

$$C = 2 \pi r$$
$$A = \pi r^2 $$

În loc să tastezi valoarea numerică a lui `pi`, poți folosi pachetul `math`, care conține această valoare.

Pentru referință, `**` este simbolul pentru exponențiere. De exemplu, `3**4` înseamnă `3` la puterea `4` și returnează `81`.

`@instructions`
- Importă pachetul `math`.
- Folosește `math.pi` pentru a calcula circumferința cercului și stocheaz-o în `C`.
- Folosește `math.pi` pentru a calcula aria cercului și stocheaz-o în `A`.

`@hint`
- Poți folosi pur și simplu `import math`, apoi să te referi la `pi` cu `math.pi`.
- Folosește ecuația din textul exercițiului pentru a calcula `C`. Utilizează `*`.
- Folosește ecuația din textul exercițiului pentru a calcula `A`. Utilizează `*` și `**`.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Import the math package
import ____

# Calculate C
C = 2 * 0.43 * ____

# Calculate A
A = ____ * 0.43 ** 2

print("Circumference: " + str(C))
print("Area: " + str(A))
```

`@solution`
```{python}
# Import the math package
import math

# Calculate C
C = 2 * 0.43 * math.pi

# Calculate A
A = math.pi * 0.43 ** 2

print("Circumference: " + str(C))
print("Area: " + str(A))
```

`@sct`
```{python}
patt = "Calculul dvs. pentru `%s` nu este corect. Asigurați-vă că folosiți `math.pi`."
Ex().multi(
  has_import('math', same_as=False),
  check_object('C').has_equal_value(incorrect_msg=patt%'C'),
  check_object('A').has_equal_value(incorrect_msg=patt%'A')
)

Ex().multi(
  has_printout(0, not_printed_msg = "__JINJA__:Păstrați `{{sol_call}}` acolo pentru a afișa circumferința."),
  has_printout(1, not_printed_msg = "__JINJA__:Păstrați `{{sol_call}}` acolo pentru a afișa aria.")
)

success_msg("Excelent! Dacă știți cum să utilizați funcțiile din pachete, puterea multor programatori Python este la îndemâna dvs.!")
```

---

## Import selectiv

```yaml
type: NormalExercise
key: fe65eff50a
lang: python
xp: 100
skills:
  - 2
```

Importurile generale, precum `import math`, îți pun la dispoziție **toată** funcționalitatea din pachetul `math`. Totuși, dacă ai nevoie doar de o parte dintr-un pachet, poți face importul mai selectiv:

```
from math import pi
```

Încearcă același lucru, dar de data aceasta importă doar `pi`.

`@instructions`
- Efectuează un import selectiv din pachetul `math`, importând doar funcția `pi`.
- Folosește `pi` pentru a calcula circumferința cercului și stochează rezultatul în `C`.
- Folosește `pi` pentru a calcula aria cercului și stochează rezultatul în `A`.

`@hint`
- Folosește `from math import pi` pentru a face importul selectiv.
- Acum poți folosi `pi` de sine stătător!

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Import pi function of math package
from math import ____

# Calculate C
C = 2 * 0.43 * ____

# Calculate A
A = ____ * 0.43 ** 2

print("Circumference: " + str(C))
print("Area: " + str(A))
```

`@solution`
```{python}
# Import pi function of math package
from math import pi

# Calculate C
C = 2 * 0.43 * pi

# Calculate A
A = pi * 0.43 ** 2

print("Circumference: " + str(C))
print("Area: " + str(A))
```

`@sct`
```{python}
patt = "Calculul dvs. pentru `%s` nu este tocmai corect. Asigurați-vă că folosiți doar `pi`."

Ex().has_import("math.pi", not_imported_msg = "Asigurați-vă că importați `pi` din pachetul `math`. Ar trebui să folosiți notația `from ___ import ___`.",)

Ex().multi(
  check_object('C').has_equal_value(incorrect_msg=patt%'C'),
  check_object('A').has_equal_value(incorrect_msg=patt%'A')
)

Ex().multi(
  has_printout(0, not_printed_msg = "__JINJA__:Păstrați `{{sol_call}}` acolo pentru a afișa circumferința."),
  has_printout(1, not_printed_msg = "__JINJA__:Păstrați `{{sol_call}}` acolo pentru a afișa aria.")
)

success_msg("Excelent! Continuați cu următorul exercițiu.")
```

---

## Moduri diferite de a importa

```yaml
type: MultipleChoiceExercise
key: f1b2675a2a
lang: python
xp: 50
skills:
  - 2
```

Există mai multe moduri de a importa pachete și module în Python. În funcție de instrucțiunea de import folosită, va trebui să utilizezi cod Python diferit.

Să presupunem că vrei să folosești [funcția](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.inv.html) `inv()`, care se află în subpachetul `linalg` al pachetului `scipy`. Vrei să poți apela această funcție astfel:

```
my_inv([[1,2], [3,4]])
```

Ce instrucțiune `import` vei folosi pentru a rula codul de mai sus fără erori?

`@possible_answers`
- `import scipy`
- `import scipy.linalg`
- `from scipy.linalg import my_inv`
- `from scipy.linalg import inv as my_inv`

`@hint`
- Încearcă diferitele instrucțiuni de import în shell-ul IPython și vezi care dintre ele permite rularea liniei `my_inv([[1, 2], [3, 4]])` fără erori. Apasă **enter** pentru a rula codul introdus.

`@pre_exercise_code`
```{python}

```

`@sct`
```{python}
msg1 = msg2 = msg3 = "Incorect, mai încercați. Încercați diferitele instrucțiuni de import în shell-ul IPython și vedeți care dintre ele face ca linia `my_inv([[1, 2], [3, 4]])` să ruleze fără erori."
msg4 = "Corect! Cuvântul `as` vă permite să creați un nume local pentru funcția pe care o importați: `inv()` este acum disponibilă ca `my_inv()`."
Ex().has_chosen(4, [msg1, msg2, msg3, msg4])
```

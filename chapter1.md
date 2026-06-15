---
title_meta: Capitolul 1
title: Noțiuni de bază în Python
description: >-
  O introducere în conceptele de bază ale Python. Învață să folosești Python în
  mod interactiv și prin scripturi. Creează primele tale variabile și
  familiarizează-te cu tipurile de date fundamentale din Python.
attachments:
  slides_link: 'https://projector-video-pdf-converter.datacamp.com/735/chapter1.pdf'
free_preview: true
lessons:
  - nb_of_exercises: 3
    title: 'Salut, Python!'
  - nb_of_exercises: 5
    title: Variabile și tipuri
---

## Salut, Python!

```yaml
type: VideoExercise
key: f644a48d5d
xp: 50
```

`@projector_key`
d8fcd4c930027fa4e1c3870c7e7e0ff1

---

## Primul tău cod Python

```yaml
type: NormalExercise
key: bdc52f0e19
lang: python
xp: 100
skills:
  - 2
```

E momentul să rulezi primul tău cod Python!

Mergi la cod și apasă butonul de rulare pentru a vedea rezultatul.

`@instructions`
- Apasă butonul de rulare pentru a vedea rezultatul lui `print(5 / 8)`.

`@hint`
- Rulează codul înainte de a trimite răspunsul, ca să ai timp să explorezi rezultatele.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Hit run code to see the output!
print(5 / 8)
```

`@solution`
```{python}
# Hit run code to see the output!
print(5 / 8)
```

`@sct`
```{python}
Ex().has_printout(0, not_printed_msg = "__JINJA__:Ați folosit `{{sol_call}}` pentru a afișa `5 / 8`?")
success_msg("Excelent! Să trecem la următorul!")
```

---

## Python ca un calculator

```yaml
type: NormalExercise
key: 0f7c039428
lang: python
xp: 100
skills:
  - 2
```

Python este perfect pentru calcule de bază. Poate efectua adunări, scăderi, înmulțiri și împărțiri.

Codul din script oferă câteva exemple.

Acum e rândul tău să exersezi scriind propriul cod.

`@instructions`
- Afișează rezultatul scăderii lui `5` din `5` sub `# Subtraction` folosind `print()`.
- Afișează rezultatul înmulțirii lui `3` cu `5` sub `# Multiplication`.

`@hint`
- Va trebui să folosești `print()` pentru a genera un rezultat.
- Poți scădea cu `-` și înmulți cu `*`.

`@pre_exercise_code`
```{python}
 
```

`@sample_code`
```{python}
# Addition and division
print(4 + 5)
print(10 / 2)

# Subtraction
print()

# Multiplication

```

`@solution`
```{python}
# Addition and division
print(4 + 5)
print(10 / 2)

# Subtraction
print(5 - 5)

# Multiplication
print(3 * 5)
```

`@sct`
```{python}
Ex().has_printout(0, not_printed_msg = "Ați folosit `print(4 + 5)` pentru a afișa rezultatul sumei?")

Ex().has_printout(1, not_printed_msg = "Ați folosit `print(5 - 5)` pentru a afișa rezultatul scăderii?")

Ex().has_printout(2, not_printed_msg = "Ați folosit `print(3 * 5)` pentru a afișa rezultatul înmulțirii?")

Ex().has_printout(3, not_printed_msg = "Ați folosit `print(10 / 2)` pentru a afișa rezultatul împărțirii?")

success_msg("Corect! Python vă poate ajuta să efectuați calcule matematice, o caracteristică ce va fi utilă pentru analiză pe măsură ce ne dezvoltăm competențele în lucrul cu datele.")
```

---

## Variabile și tipuri de date

```yaml
type: VideoExercise
key: c2e396792e
xp: 50
```

`@projector_key`
433dcfcfedaee070cbf440491c402e3b

---

## Atribuirea variabilelor

```yaml
type: NormalExercise
key: 4bf65ad83e
lang: python
xp: 100
skills:
  - 2
```

În Python, o variabilă îți permite să faci referire la o valoare printr-un nume. Pentru a crea o variabilă `x` cu valoarea `5`, folosești `=`, ca în exemplul de mai jos:

```
x = 5
```

Acum poți folosi numele variabilei, `x`, în loc de valoarea propriu-zisă, `5`.

Reține că `=` în Python înseamnă _atribuire_, nu testarea egalității! Încearcă în exercițiu, înlocuind `____` cu propriul tău cod.

`@instructions`
- Creează o variabilă `savings` cu valoarea `100`.
- Verifică această variabilă scriind `print(savings)` în script.

`@hint`
- Scrie `savings = 100` pentru a crea variabila `savings`.
- După ce ai creat variabila `savings`, poți scrie `print(savings)`.
- Codul final nu trebuie să conțină niciun `____`.

`@pre_exercise_code`
```{python}
 
```

`@sample_code`
```{python}
# Create a variable savings
____

# Print out savings
____
```

`@solution`
```{python}
# Create a variable savings
savings = 100

# Print out savings
print(savings)
```

`@sct`
```{python}
Ex().check_object("savings").has_equal_value(incorrect_msg="Atribuiți `100` variabilei `savings`.")
Ex().has_printout(0, not_printed_msg = "Afișați `savings`, variabila pe care ați creat-o, folosind `print(savings)`.")
success_msg("Excelent! Acum să încercăm să facem câteva calcule cu această variabilă!")
```

---

## Calcule cu variabile

```yaml
type: NormalExercise
key: ff06cedeb4
lang: python
xp: 100
skills:
  - 2
```

Ai creat deja o variabilă pentru economii, așa că hai să începem să economisim!

În loc să lucrezi cu valorile efective, poți folosi variabile.

Cât ai economisi în patru luni, dacă pui deoparte 10 dolari în fiecare lună?

`@instructions`
- Creează o variabilă `monthly_savings` cu valoarea `10` și o variabilă `num_months` cu valoarea `4`.
- Înmulțește `monthly_savings` cu `num_months` și atribuie rezultatul variabilei `new_savings`.
- Afișează valoarea variabilei `new_savings`.

`@hint`
- Poți face calcule cu variabile exact ca și cu numere, deci în loc de `10 * 4`, înlocuiește numerele cu variabilele!
- Folosește `print()` pentru a vedea valoarea din `new_savings`.
- Ai grijă să scrii corect numele variabilelor!

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create the variables monthly_savings and num_months



# Multiply monthly_savings and num_months
new_savings = ____

# Print new_savings

```

`@solution`
```{python}
# Create the variables monthly_savings and num_months
monthly_savings = 10
num_months = 4

# Multiply monthly_savings and num_months
new_savings = monthly_savings * num_months

# Print new_savings
print(new_savings)
```

`@sct`
```{python}
Ex().check_object("monthly_savings").has_equal_value(incorrect_msg = "Ați salvat `10` în `monthly_savings` folosind `monthly_savings = 10`?")
Ex().check_object("num_months").has_equal_value(incorrect_msg = "Ați salvat `4` în `num_months` folosind `num_months = 4`?")
Ex().check_object("new_savings").has_equal_value(incorrect_msg = "Ați folosit variabilele și simbolurile corecte pentru înmulțire? Era așteptat `monthly_savings * num_months`, dar s-a obținut altceva.")
# Ex().check_object("total_savings").has_equal_value(incorrect_msg = "Did you use the correct variables and symbols to add? Expected `savings + new_savings` but got something else.")

Ex().has_printout(0, not_printed_msg="Nu uitați să afișați `new_savings` la sfârșitul scriptului dumneavoastră.")

success_msg("Aveți 40 de dolari în economii noi!")
```

---

## Alte tipuri de variabile

```yaml
type: NormalExercise
key: 006b48561f
lang: python
xp: 100
skills:
  - 2
```

În exercițiul anterior, ai lucrat cu tipul de date întreg din Python:

- `int`, sau integer: un număr fără parte fracționară. `savings`, cu valoarea `100`, este un exemplu de integer.

Pe lângă tipurile de date numerice, mai există trei tipuri de date foarte frecvent întâlnite:

- `float`, sau număr cu virgulă mobilă: un număr care are atât o parte întreagă, cât și una fracționară, separate printr-un punct. `1.1` este un exemplu de float.
- `str`, sau string: un tip folosit pentru a reprezenta text. Poți folosi ghilimele simple sau duble pentru a construi un string.
- `bool`, sau boolean: un tip folosit pentru a reprezenta valori logice. Poate fi doar `True` sau `False` (majusculele contează!).

`@instructions`
- Creează un nou float, `half`, cu valoarea `0.5`.
- Creează un nou string, `intro`, cu valoarea `"Hello! How are you?"`.
- Creează un nou boolean, `is_good`, cu valoarea `True`.

`@hint`
- Pentru a crea o variabilă în Python, folosește `=`. Asigură-te că șirul de caractere este între ghilimele simple sau duble.
- În Python există doar două valori booleene: `True` și `False`. `TRUE`, `true`, `FALSE`, `false` și alte variante nu sunt acceptate.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create a variable half


# Create a variable intro


# Create a variable is_good

```

`@solution`
```{python}
# Create a variable half
half = 0.5

# Create a variable intro
intro = "Hello! How are you?"

# Create a variable is_good
is_good = True
```

`@sct`
```{python}
Ex().check_object("half").has_equal_value(incorrect_msg = "Ați salvat numărul zecimal `0.5` în variabila `half`?")

Ex().check_object("intro").has_equal_value(incorrect_msg = "Hmm, ceva este incorect în variabila dvs. `intro`. Verificați din nou ortografia și asigurați-vă că ați folosit ghilimele.")

Ex().check_object("is_good").has_equal_value(incorrect_msg = "Ați scris cu majusculă valoarea booleană? Rețineți că nu este nevoie să folosiți ghilimele aici.")

success_msg("Bravo!")
```

---

## Operații cu alte tipuri

```yaml
type: BulletExercise
key: 4d0d83cc02
xp: 100
```

Variabilele pot fi de tipuri diferite în Python. Poți vedea tipul unei variabile folosind `type()`. De exemplu, pentru a vedea tipul variabilei `a`, execută: `type(a)`.

Tipuri diferite se comportă diferit în Python. Când aduni două șiruri de caractere, de exemplu, vei obține un rezultat diferit față de adunarea a două numere întregi sau a două valori booleene.

Acum e rândul tău să testezi asta.

`@pre_exercise_code`
```{python}

```

***

```yaml
type: NormalExercise
key: f4e91c4ae9
xp: 50
```

`@instructions`
- Adună `savings` și `new_savings` și atribuie rezultatul variabilei `total_savings`.
- Folosește `type()` pentru a afișa tipul rezultat al variabilei `total_savings`.

`@hint`
- Atribuie `savings + new_savings` unei noi variabile, `total_savings`.
- Pentru a afișa tipul unei variabile `x`, folosește `print(type(x))`.

`@sample_code`
```{python}
savings = 100
new_savings = 40

# Calculate total_savings using savings and new_savings
____
print(total_savings)

# Print the type of total_savings
print(____)
```

`@solution`
```{python}
savings = 100
new_savings = 40

# Calculate total_savings using savings and new_savings
total_savings = savings + new_savings
print(total_savings)

# Print the type of total_savings
print(type(total_savings))
```

`@sct`
```{python}
# predefined
msg = "Nu trebuie să modificați sau să eliminați variabilele predefinite."

Ex().multi(
    check_object('savings', missing_msg=msg).has_equal_value(incorrect_msg=msg),
    check_object('new_savings', missing_msg=msg).has_equal_value(incorrect_msg=msg)
)

Ex().multi(
    check_object("total_savings").has_equal_value(incorrect_msg="Adăugați `savings` și `new_savings` pentru a crea variabila `total_savings`."),
    has_printout(1, not_printed_msg = "__JINJA__:Utilizați `{{sol_call}}` pentru a afișa tipul variabilei `total_savings`.")
)
```

***

```yaml
type: NormalExercise
key: f54fbf9bd9
xp: 50
```

`@instructions`
- Calculează suma dintre `intro` și `intro` și atribuie rezultatul variabilei `doubleintro`.
- Afișează `doubleintro`. Te-ai așteptat la acest rezultat?

`@hint`
- Atribuie `intro + intro` unei noi variabile, `doubleintro`.
- Pentru a afișa o variabilă `x`, scrie `print(x)` în script.

`@sample_code`
```{python}
intro = "Hello! How are you?"

# Assign sum of intro and intro to doubleintro
____

# Print out doubleintro
print(____)
```

`@solution`
```{python}
intro = "Hello! How are you?"

# Assign sum of intro and intro to doubleintro
doubleintro = intro + intro

# Print out doubleintro
print(doubleintro)
```

`@sct`
```{python}
# predefined
msg = "Nu trebuie să modificați sau să eliminați variabilele predefinite."

Ex().check_object('intro', missing_msg=msg).has_equal_value(incorrect_msg=msg)

Ex().multi(
    check_object("doubleintro").has_equal_value(incorrect_msg  = "Ați stocat rezultatul `intro + intro` în `doubleintro`?"),
    has_printout(0, not_printed_msg = "Nu uitați să afișați `doubleintro`.")
)

success_msg("Bine. Observați cum `intro + intro` determină lipirea `\"Hello! How are you?\"` și `\"Hello! How are you?\"`.")
```

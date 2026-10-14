---
title_meta: Rozdział 3
title: Funkcje i pakiety
description: >-
  Dowiesz się, jak korzystać z funkcji, metod i pakietów, aby efektywnie używać
  kodu napisanego przez doświadczonych programistów Pythona. Celem jest
  ograniczenie ilości kodu potrzebnego do rozwiązywania złożonych problemów!
attachments:
  slides_link: 'https://projector-video-pdf-converter.datacamp.com/735/chapter3.pdf'
lessons:
  - nb_of_exercises: 4
    title: Funkcje
  - nb_of_exercises: 4
    title: Metody
  - nb_of_exercises: 4
    title: Pakiety
---

## Funkcje

```yaml
type: VideoExercise
key: 5c5f365930
xp: 50
```

`@projector_key`
1204d914b0e53100529827e07441ee6c

---

## Znajome funkcje

```yaml
type: NormalExercise
key: c422ee929b
lang: python
xp: 100
skills:
  - 2
```

Python oferuje gotowy zestaw wbudowanych funkcji, które ułatwiają pracę analityka danych. Znasz już dwie z nich: `print()` i `type()`. Istnieją też funkcje takie jak `str()`, `int()`, `bool()` czy `float()`, które służą do konwersji między typami danych. Możesz dowiedzieć się o nich więcej [tutaj.](https://docs.python.org/3/library/functions.html) To również funkcje wbudowane.

Wywoływanie funkcji jest proste. Aby sprawdzić typ wartości `3.0` i zapisać wynik w nowej zmiennej `result`, możesz użyć następującego kodu:

```
result = type(3.0)
```

`@instructions`
- Użyj `print()` w połączeniu z `type()`, aby wyświetlić typ zmiennej `var1`.
- Użyj `len()`, aby pobrać [długość listy](https://docs.python.org/3/library/functions.html#len) `var1`. Owiń wywołanie w `print()`, żeby od razu wyświetlić wynik.
- Użyj `int()`, aby przekonwertować `var2` na [liczbę całkowitą](https://docs.python.org/3/library/functions.html#int). Zapisz wynik w zmiennej `out2`.

`@hint`
- Wywołaj funkcję `type()` w ten sposób: `type(var1)`.
- Wywołaj `print()` tak jak robiłeś to już wiele razy. Wystarczy podać w nawiasach zmienną, którą chcesz wyświetlić.
- `int(x)` przekonwertuje `x` na liczbę całkowitą.

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
msg = "Nie musisz zmieniać ani usuwać predefiniowanych zmiennych."
Ex().check_object("var1", missing_msg=msg).has_equal_value(incorrect_msg=msg)
Ex().check_object("var2", missing_msg=msg).has_equal_value(incorrect_msg=msg)

patt = "__JINJA__:Upewnij się, że wypisujesz %s `var1` za pomocą `{{sol_call}}`."
Ex().has_printout(0, not_printed_msg = patt % 'typ')
Ex().has_printout(1, not_printed_msg = patt % 'długość')

int_miss_msg = "Czy użyto `int()`, aby przekonwertować `var2` na liczbę całkowitą?"
int_incorr_msg = "Czy przekazano `var2` do `int()`?"
Ex().check_correct(
  check_object("out2").has_equal_value(incorrect_msg="Wywołano `int()` poprawnie; teraz upewnij się, że wynik tego wywołania jest przypisany do `out2`."),
  check_function("int", missing_msg=int_miss_msg).has_equal_value(incorrect_msg=int_incorr_msg)
)
success_msg("Świetna robota! Funkcja `len()` jest niezwykle przydatna; działa również na ciągach znaków, zliczając liczbę znaków!")
```

---

## Pomoc!

```yaml
type: MultipleChoiceExercise
key: 679b852978
lang: python
xp: 50
skills:
  - 2
```

Może znasz już nazwę jakiejś funkcji Pythona, ale wciąż musisz się dowiedzieć, jak jej używać. Paradoksalnie – aby uzyskać informacje o funkcji, trzeba skorzystać z innej funkcji: `help()`. W IPythonie możesz też wpisać `?` przed nazwą funkcji.

Aby na przykład sprawdzić dokumentację funkcji `max()`, użyj jednego z poniższych wywołań:

```
help(max)
?max
```

Skorzystaj z powłoki IPython, aby otworzyć [dokumentację](https://docs.python.org/3/library/functions.html#pow) funkcji `pow()`. Wpisz `?pow` lub `help(pow)` i naciśnij **Enter**.

Które z poniższych stwierdzeń jest prawdziwe?

`@possible_answers`
- `pow()` przyjmuje trzy argumenty: `base`, `exp` i `mod`. Bez argumentu `mod` funkcja zwróci błąd.
- `pow()` przyjmuje trzy wymagane argumenty: `base`, `exp` i `None`.
- `pow()` wymaga argumentów `base` i `exp`; argument `mod` jest opcjonalny.
- `pow()` przyjmuje dwa argumenty: `exp` i `mod`. Brak argumentu `exp` powoduje błąd.

`@hint`
- Argumenty opcjonalne mają przypisaną domyślną wartość przez `=` – funkcja użyje jej, jeśli nie podasz tego argumentu.

`@pre_exercise_code`
```{python}

```

`@sct`
```{python}
msg1 = "Nie do końca. `mod` ma wartość domyślną, która zostanie użyta, jeśli nie określi się żadnej wartości."
msg2 = "Nieprawidłowo. `None` jest wartością domyślną dla argumentu `mod`."
msg3 = "Doskonale! Używanie `help()` może pomóc w zrozumieniu działania funkcji, wykorzystując ich pełny potencjał!"
msg4 = "Nieprawidłowo. `pow()` przyjmuje trzy argumenty, z których jeden ma wartość domyślną."
Ex().has_chosen(3, [msg1, msg2, msg3, msg4])
```

---

## Wiele argumentów

```yaml
type: NormalExercise
key: e30486d7c1
lang: python
xp: 100
skills:
  - 2
```

W poprzednim ćwiczeniu identyfikowałeś(-aś) opcjonalne argumenty, przeglądając dokumentację za pomocą `help()`. Teraz wykorzystasz tę wiedzę, aby zmienić zachowanie funkcji `sorted()`.

Zapoznaj się z [dokumentacją](https://docs.python.org/3/library/functions.html#sorted) funkcji `sorted()`, wpisując `help(sorted)` w konsoli IPython.

Zobaczysz, że `sorted()` przyjmuje trzy argumenty: `iterable`, `key` i `reverse`. W tym ćwiczeniu musisz podać tylko `iterable` i `reverse` – pomiń `key`.

Dwie listy zostały już dla ciebie przygotowane.

Czy potrafisz je połączyć i posortować w kolejności malejącej?

`@instructions`
- Użyj `+`, aby połączyć zawartość `first` i `second` w nową listę: `full`.
- Wywołaj `sorted()` na `full` i ustaw argument `reverse` na `True`. Zapisz posortowaną listę jako `full_sorted`.
- Na koniec wyświetl `full_sorted`.

`@hint`
- Połącz `first` i `second` jak dwie liczby i przypisz wynik do `full`.
- Użyj `sorted()` z dwoma argumentami: `full` i `reverse=True`.
- Aby wyświetlić zmienną, użyj `print()`.

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
msg = "Nie musisz zmieniać ani usuwać już istniejących zmiennych `first` i `second`."
Ex().multi(
  check_object("first", missing_msg=msg).has_equal_value(incorrect_msg=msg),
  check_object("second", missing_msg=msg).has_equal_value(incorrect_msg=msg)
)
Ex().check_correct(
  check_object("full_sorted").has_equal_value(incorrect_msg="Upewnij się, że przypisujesz wynik wywołania `sorted()` do `full_sorted`."),
  check_function("sorted").multi(
    check_args(0).has_equal_value(),
    check_args('reverse').has_equal_value()
  )
)

success_msg("Świetnie! Przejdź do filmu o metodach w Pythonie.")
```

---

## Metody

```yaml
type: VideoExercise
key: 2b66cb66b1
xp: 50
```

`@projector_key`
8e387776f3a264a745128b68aa8d8f83

---

## Metody łańcuchów znaków

```yaml
type: NormalExercise
key: 4039302ee0
lang: python
xp: 100
skills:
  - 2
```

Łańcuchy znaków mają wiele wbudowanych metod. Postępuj zgodnie z instrukcjami, aby poznać kilka z nich. Jeśli chcesz zgłębić ten temat, możesz w każdej chwili wpisać `help(str)` w powłoce IPython.

Zmienna `place` została już dla ciebie utworzona – możesz na niej eksperymentować.

`@instructions`
- Wywołaj [metodę](https://docs.python.org/3/library/stdtypes.html#str.upper) `.upper()` na zmiennej `place` i zapisz wynik w zmiennej `place_up`. Użyj składni wywoływania metod, której nauczyłeś się w poprzednim filmie.
- Wyświetl zmienne `place` i `place_up`. Czy obie uległy zmianie?
- Wyświetl liczbę liter „o" w zmiennej `place`, wywołując metodę `.count()` na `place` i przekazując literę `'o'` jako argument. Chodzi o zmienną `place`, a nie o słowo `"place"`!

`@hint`
- Możesz wywołać metodę `.upper()` na zmiennej `place` bez żadnych dodatkowych argumentów.
- Aby wyświetlić zmienną `x`, napisz `print(x)`.
- Pamiętaj, aby otoczyć wywołanie `place.count(____)` funkcją `print()`, żeby wyświetlić wynik.

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
msg = "Nie musisz zmieniać ani usuwać predefiniowanych zmiennych."
Ex().check_object("place", missing_msg=msg).has_equal_value(incorrect_msg=msg)

patt = "Nie zapomnij wydrukować `%s`."
Ex().has_printout(0, not_printed_msg=patt % "place")
Ex().check_correct(
    has_printout(1, not_printed_msg=patt % "place_up"),
    check_correct(
        check_object("place_up").has_equal_value(incorrect_msg="Przypisz wynik wywołania `place.upper()` do zmiennej `place_up`."),
        check_function("place.upper", signature=False)
    )
)    

# check count of place
Ex().check_correct(
  has_printout(2, not_printed_msg = "Poprawnie obliczono liczbę liter 'o' w zmiennej `place`; teraz upewnij się, że wywołanie `place.count('o')` jest opakowane w funkcję `print()`, aby wydrukować wynik."),
  check_function("place.count", signature=False).check_args(0).has_equal_value()
)

success_msg("Świetnie! Zwróć uwagę na podstawie wydruków, że metoda `upper()` nie zmienia obiektu, na którym jest wywoływana. W przypadku list w następnym ćwiczeniu będzie inaczej!")
```

---

## Metody list

```yaml
type: NormalExercise
key: 0dbe8ed695
lang: python
xp: 100
skills:
  - 2
```

Metody w Pythonie nie są zarezerwowane wyłącznie dla ciągów znaków. Listy, liczby zmiennoprzecinkowe, liczby całkowite i wartości logiczne również mają swoje zestawy przydatnych metod. W tym ćwiczeniu poeksperymentujesz z:

- `.index()` – zwraca indeks pierwszego elementu listy pasującego do podanej wartości,
- `.count()` – zwraca liczbę wystąpień danego elementu na liście.

Będziesz pracować na liście `areas`, która zawiera powierzchnie różnych pomieszczeń w domu.

`@instructions`
- Użyj metody `.index()`, aby znaleźć indeks elementu listy `areas` równego `20.0`. Wyświetl ten indeks.
- Wywołaj metodę `.count()` na liście `areas`, aby sprawdzić, ile razy wartość `9.50` pojawia się na liście. Wyświetl tę liczbę.

`@hint`
- Aby wyświetlić indeks, owiń wywołanie `areas.index(___)` w funkcję `print()`.
- Aby wyświetlić liczbę wystąpień elementu `x` na liście, owiń wywołanie `areas.count(___)` w funkcję `print()`.

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
predef_msg = "Nie musisz zmieniać ani usuwać predefiniowanej listy `areas`."

Ex().check_object("areas", missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg)

Ex().check_function("print", index=0).check_args(0).check_function('areas.index', signature=False).check_args(0).has_equal_value()


Ex().check_function("print", index=1).check_args(0).check_function('areas.count', signature=False).has_equal_value()

success_msg("Świetnie! To były przykłady metod `list`, które nie zmieniają listy, na której zostały wywołane.")
```

---

## Metody listy (2)

```yaml
type: NormalExercise
key: 1fbeab82d0
lang: python
xp: 100
skills:
  - 2
```

Większość metod listy modyfikuje listę, na której są wywoływane. Przykłady:

- `.append()` – dodaje element do listy,
- `.remove()` – [usuwa](https://docs.python.org/3/library/stdtypes.html#typesseq-mutable) pierwsze wystąpienie podanej wartości z listy,
- `.reverse()` – [odwraca](https://docs.python.org/3/library/stdtypes.html#typesseq-mutable) kolejność elementów na liście.

Będziesz pracować na liście `areas`, która zawiera powierzchnie różnych pomieszczeń w domu.

`@instructions`
- Użyj `.append()` dwa razy, aby ponownie dodać powierzchnię basenu i garażu: odpowiednio `24.5` i `15.45`. Pamiętaj, aby dodać je w tej kolejności.
- Wyświetl listę `areas`.
- Użyj metody `.reverse()`, aby odwrócić kolejność elementów na liście `areas`.
- Wyświetl listę `areas` jeszcze raz.

`@hint`
- W pierwszej instrukcji użyj wywołania `areas.append(___)` dwa razy.
- Aby wyświetlić zmienną `x`, po prostu napisz `print(x)`.
- Metoda `.reverse()` nie wymaga żadnych argumentów – użyj jej z notacją kropkową i pustymi nawiasami: `.reverse()`.
- Aby wyświetlić zmienną `x`, po prostu napisz `print(x)`.

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

success_msg("Świetnie!")
```

---

## Pakiety

```yaml
type: VideoExercise
key: ab96a17c5e
xp: 50
```

`@projector_key`
cedcfb34350be8545599768f96695cdd

---

## Importowanie pakietu

```yaml
type: NormalExercise
key: 7432a6376f
lang: python
xp: 100
skills:
  - 2
```

Wyobraź sobie, że chcesz obliczyć obwód i pole koła. Oto odpowiednie wzory:

$$C = 2 \pi r$$
$$A = \pi r^2 $$

Zamiast wpisywać wartość liczbową `pi`, możesz skorzystać z pakietu `math`, który zawiera tę stałą.

Dla przypomnienia: `**` to operator potęgowania. Na przykład `3**4` oznacza `3` do potęgi `4` i daje wynik `81`.

`@instructions`
- Zaimportuj pakiet `math`.
- Użyj `math.pi`, aby obliczyć obwód koła, i zapisz wynik w zmiennej `C`.
- Użyj `math.pi`, aby obliczyć pole koła, i zapisz wynik w zmiennej `A`.

`@hint`
- Możesz po prostu użyć `import math`, a następnie odwołać się do `pi` za pomocą `math.pi`.
- Użyj wzoru z treści zadania, aby obliczyć `C`. Skorzystaj z operatora `*`.
- Użyj wzoru z treści zadania, aby obliczyć `A`. Skorzystaj z operatorów `*` i `**`.

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
patt = "Twoje obliczenie `%s` nie jest do końca poprawne. Upewnij się, że używasz `math.pi`."
Ex().multi(
  has_import('math', same_as=False),
  check_object('C').has_equal_value(incorrect_msg=patt%'C'),
  check_object('A').has_equal_value(incorrect_msg=patt%'A')
)

Ex().multi(
  has_printout(0, not_printed_msg = "__JINJA__:Zachowaj `{{sol_call}}` w kodzie, aby wyświetlić obwód."),
  has_printout(1, not_printed_msg = "__JINJA__:Zachowaj `{{sol_call}}` w kodzie, aby wyświetlić pole.")
)

success_msg("Świetnie! Jeśli wiesz, jak korzystać z funkcji z pakietów, możliwości wielu programistów Pythona są na wyciągnięcie ręki!")
```

---

## Selektywny import

```yaml
type: NormalExercise
key: fe65eff50a
lang: python
xp: 100
skills:
  - 2
```

Ogólny import, taki jak `import math`, udostępnia **wszystkie** funkcje pakietu `math`. Jeśli jednak chcesz skorzystać tylko z wybranego elementu pakietu, możesz zawęzić import:

```
from math import pi
```

Wypróbuj to samo podejście, ale tym razem zaimportuj wyłącznie `pi`.

`@instructions`
- Wykonaj selektywny import z pakietu `math`, importując tylko funkcję `pi`.
- Użyj `pi`, aby obliczyć obwód koła i zapisz wynik w zmiennej `C`.
- Użyj `pi`, aby obliczyć pole koła i zapisz wynik w zmiennej `A`.

`@hint`
- Użyj `from math import pi`, aby wykonać selektywny import.
- Teraz możesz używać `pi` samodzielnie!

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
patt = "Twoje obliczenie `%s` nie jest do końca poprawne. Upewnij się, że używasz tylko `pi`."

Ex().has_import("math.pi", not_imported_msg = "Pamiętaj, aby zaimportować `pi` z pakietu `math`. Należy użyć notacji `from ___ import ___`.",)

Ex().multi(
  check_object('C').has_equal_value(incorrect_msg=patt%'C'),
  check_object('A').has_equal_value(incorrect_msg=patt%'A')
)

Ex().multi(
  has_printout(0, not_printed_msg = "__JINJA__:Proszę zachować `{{sol_call}}`, aby wyświetlić obwód."),
  has_printout(1, not_printed_msg = "__JINJA__:Proszę zachować `{{sol_call}}`, aby wyświetlić pole.")
)

success_msg("Świetnie! Przejdź do następnego ćwiczenia.")
```

---

## Różne sposoby importowania

```yaml
type: MultipleChoiceExercise
key: f1b2675a2a
lang: python
xp: 50
skills:
  - 2
```

Istnieje kilka sposobów importowania pakietów i modułów w Pythonie. W zależności od użytej instrukcji importu, trzeba będzie zastosować inny kod.

Przypuśćmy, że chcesz użyć [funkcji](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.inv.html) `inv()`, która znajduje się w subpakiecie `linalg` pakietu `scipy`. Chcesz móc wywołać tę funkcję w następujący sposób:

```
my_inv([[1,2], [3,4]])
```

Która instrukcja `import` pozwoli uruchomić powyższy kod bez błędu?

`@possible_answers`
- `import scipy`
- `import scipy.linalg`
- `from scipy.linalg import my_inv`
- `from scipy.linalg import inv as my_inv`

`@hint`
- Wypróbuj różne instrukcje importu w powłoce IPython i sprawdź, która z nich pozwala uruchomić linię `my_inv([[1, 2], [3, 4]])` bez błędów. Naciśnij **Enter**, aby uruchomić wpisany kod.

`@pre_exercise_code`
```{python}

```

`@sct`
```{python}
msg1 = msg2 = msg3 = "Niepoprawnie, spróbuj ponownie. Wypróbuj różne instrukcje importu w powłoce IPython i sprawdź, która z nich powoduje, że linia `my_inv([[1, 2], [3, 4]])` działa bez błędów."
msg4 = "Poprawnie! Słowo `as` pozwala utworzyć lokalną nazwę dla importowanej funkcji: `inv()` jest teraz dostępna jako `my_inv()`."
Ex().has_chosen(4, [msg1, msg2, msg3, msg4])
```

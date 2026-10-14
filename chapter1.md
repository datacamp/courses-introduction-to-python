---
title_meta: Rozdział 1
title: Podstawy Pythona
description: >-
  Wprowadzenie do podstawowych pojęć Pythona. Dowiesz się, jak używać Pythona
  interaktywnie i za pomocą skryptów. Stworzysz swoje pierwsze zmienne i poznasz
  podstawowe typy danych.
attachments:
  slides_link: 'https://projector-video-pdf-converter.datacamp.com/735/chapter1.pdf'
free_preview: true
lessons:
  - nb_of_exercises: 3
    title: 'Witaj, Python!'
  - nb_of_exercises: 5
    title: Zmienne i typy danych
---

## Witaj w Pythonie!

```yaml
type: VideoExercise
key: f644a48d5d
xp: 50
```

`@projector_key`
d8fcd4c930027fa4e1c3870c7e7e0ff1

---

## Twój pierwszy kod w Pythonie

```yaml
type: NormalExercise
key: bdc52f0e19
lang: python
xp: 100
skills:
  - 2
```

Czas uruchomić swój pierwszy kod w Pythonie!

Przejdź do edytora kodu i kliknij przycisk **Uruchom kod**, aby zobaczyć wynik.

`@instructions`
- Kliknij przycisk **Uruchom kod**, aby zobaczyć wynik działania `print(5 / 8)`.

`@hint`
- Uruchom kod przed przesłaniem odpowiedzi, żeby mieć czas na zapoznanie się z wynikiem.

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
Ex().has_printout(0, not_printed_msg = "__JINJA__:Czy użył(a) Pan(i) `{{sol_call}}` aby wydrukować `5 / 8`?")
success_msg("Świetnie! Przechodzimy do następnego!")
```

---

## Python jako kalkulator

```yaml
type: NormalExercise
key: 0f7c039428
lang: python
xp: 100
skills:
  - 2
```

Python świetnie nadaje się do podstawowych obliczeń. Obsługuje dodawanie, odejmowanie, mnożenie i dzielenie.

Kod w skrypcie zawiera kilka przykładów.

Teraz twoja kolej – napisz własny kod i poćwicz.

`@instructions`
- Wyświetl wynik odejmowania `5` od `5` pod komentarzem `# Subtraction`, używając funkcji `print()`.
- Wyświetl wynik mnożenia `3` przez `5` pod komentarzem `# Multiplication`.

`@hint`
- Użyj funkcji `print()`, aby wyświetlić wynik.
- Do odejmowania służy operator `-`, a do mnożenia – `*`.

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
Ex().has_printout(0, not_printed_msg = "Czy użył(a) Pan(i) `print(4 + 5)`, aby wydrukować wynik sumy?")

Ex().has_printout(1, not_printed_msg = "Czy użył(a) Pan(i) `print(5 - 5)`, aby wydrukować wynik odejmowania?")

Ex().has_printout(2, not_printed_msg = "Czy użył(a) Pan(i) `print(3 * 5)`, aby wydrukować wynik mnożenia?")

Ex().has_printout(3, not_printed_msg = "Czy użył(a) Pan(i) `print(10 / 2)`, aby wydrukować wynik dzielenia?")

success_msg("Zgadza się! Python może pomóc Panu(i) w obliczeniach, co będzie przydatną cechą podczas analizy danych w miarę rozwijania umiejętności.")
```

---

## Zmienne i typy

```yaml
type: VideoExercise
key: c2e396792e
xp: 50
```

`@projector_key`
433dcfcfedaee070cbf440491c402e3b

---

## Przypisywanie wartości do zmiennej

```yaml
type: NormalExercise
key: 4bf65ad83e
lang: python
xp: 100
skills:
  - 2
```

W Pythonie zmienna pozwala odwoływać się do wartości za pomocą nazwy. Aby utworzyć zmienną `x` o wartości `5`, użyj operatora `=`, tak jak w tym przykładzie:

```
x = 5
```

Od tej chwili możesz używać nazwy zmiennej `x` zamiast samej wartości `5`.

Pamiętaj: `=` w Pythonie oznacza _przypisanie_ – nie sprawdza równości! Wypróbuj to w ćwiczeniu, zastępując `____` swoim kodem.

`@instructions`
- Utwórz zmienną `savings` o wartości `100`.
- Sprawdź tę zmienną, wpisując `print(savings)` w skrypcie.

`@hint`
- Wpisz `savings = 100`, aby utworzyć zmienną `savings`.
- Po utworzeniu zmiennej `savings` możesz wpisać `print(savings)`.
- Twój końcowy kod nie powinien zawierać żadnego `____`.

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
Ex().check_object("savings").has_equal_value(incorrect_msg="Przypisz `100` do zmiennej `savings`.")
Ex().has_printout(0, not_printed_msg = "Wyświetl `savings`, utworzoną zmienną, za pomocą `print(savings)`.")
success_msg("Świetnie! Spróbujmy teraz wykonać kilka obliczeń z tą zmienną!")
```

---

## Obliczenia na zmiennych

```yaml
type: NormalExercise
key: ff06cedeb4
lang: python
xp: 100
skills:
  - 2
```

Masz już zmienną przechowującą oszczędności – czas zacząć odkładać!

Zamiast operować na konkretnych wartościach, możesz używać zmiennych.

Ile pieniędzy zaoszczędzisz przez cztery miesiące, odkładając 10 dolarów miesięcznie?

`@instructions`
- Utwórz zmienną `monthly_savings` o wartości `10` oraz zmienną `num_months` o wartości `4`.
- Pomnóż `monthly_savings` przez `num_months` i przypisz wynik do zmiennej `new_savings`.
- Wyświetl wartość zmiennej `new_savings`.

`@hint`
- Działania na zmiennych wykonuje się tak samo jak na liczbach – zamiast `10 * 4` użyj odpowiednich zmiennych!
- Użyj `print()`, aby wyświetlić wartość `new_savings`.
- Uważaj na poprawną pisownię nazw zmiennych!

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
Ex().check_object("monthly_savings").has_equal_value(incorrect_msg = "Czy zapisano `10` do `monthly_savings` używając `monthly_savings = 10`?")
Ex().check_object("num_months").has_equal_value(incorrect_msg = "Czy zapisano `4` do `num_months` używając `num_months = 4`?")
Ex().check_object("new_savings").has_equal_value(incorrect_msg = "Czy użyto poprawnych zmiennych i symboli do mnożenia? Oczekiwano `monthly_savings * num_months`, ale otrzymano coś innego.")
# Ex().check_object("total_savings").has_equal_value(incorrect_msg = "Czy użyto poprawnych zmiennych i symboli do dodawania? Oczekiwano `savings + new_savings`, ale otrzymano coś innego.")

Ex().has_printout(0, not_printed_msg="Proszę pamiętać o wyświetleniu `new_savings` na końcu skryptu.")

success_msg("Mają Państwo $40 w nowych oszczędnościach!")
```

---

## Inne typy zmiennych

```yaml
type: NormalExercise
key: 006b48561f
lang: python
xp: 100
skills:
  - 2
```

W poprzednim ćwiczeniu pracowałeś z całkowitym typem danych w Pythonie:

- `int`, czyli liczba całkowita: liczba bez części ułamkowej. `savings` o wartości `100` to przykład liczby całkowitej.

Oprócz typów liczbowych istnieją trzy inne, bardzo popularne typy danych:

- `float`, czyli liczba zmiennoprzecinkowa: liczba posiadająca część całkowitą i ułamkową, oddzielone kropką. `1.1` to przykład liczby typu `float`.
- `str`, czyli łańcuch znaków: typ służący do reprezentowania tekstu. Możesz budować łańcuchy znaków, używając pojedynczych lub podwójnych cudzysłowów.
- `bool`, czyli wartość logiczna: typ służący do reprezentowania wartości logicznych. Może przyjmować tylko wartość `True` lub `False` (wielkość liter ma znaczenie!).

`@instructions`
- Utwórz nową liczbę zmiennoprzecinkową `half` o wartości `0.5`.
- Utwórz nowy łańcuch znaków `intro` o wartości `"Hello! How are you?"`.
- Utwórz nową wartość logiczną `is_good` o wartości `True`.

`@hint`
- Aby utworzyć zmienną w Pythonie, użyj operatora `=`. Pamiętaj, żeby ująć tekst w pojedyncze lub podwójne cudzysłowy.
- W Pythonie istnieją tylko dwie wartości logiczne: `True` i `False`. Wersje `TRUE`, `true`, `FALSE`, `false` i inne nie będą akceptowane.

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
Ex().check_object("half").has_equal_value(incorrect_msg = "Czy zapisałeś/zapisałaś liczbę zmiennoprzecinkową `0.5` do zmiennej `half`?")

Ex().check_object("intro").has_equal_value(incorrect_msg = "Hmm, coś jest niepoprawne w zmiennej `intro`. Sprawdź dokładnie pisownię i upewnij się, że użyto cudzysłowów.")

Ex().check_object("is_good").has_equal_value(incorrect_msg = "Czy użyłeś/użyłaś wielkiej litery w wartości logicznej? Pamiętaj, że nie trzeba tu używać cudzysłowów.")

success_msg("Świetnie!")
```

---

## Operacje na różnych typach danych

```yaml
type: BulletExercise
key: 4d0d83cc02
xp: 100
```

Zmienne w Pythonie mogą mieć różne typy. Aby sprawdzić typ zmiennej, użyj funkcji `type()`. Na przykład, żeby zobaczyć typ zmiennej `a`, wpisz: `type(a)`.

Różne typy zachowują się w Pythonie inaczej. Suma dwóch ciągów tekstowych daje inny wynik niż suma dwóch liczb całkowitych czy dwóch wartości logicznych.

Czas, żebyś sprawdził to samodzielnie.

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
- Dodaj `savings` i `new_savings`, a wynik przypisz do zmiennej `total_savings`.
- Użyj funkcji `type()`, aby wyświetlić typ zmiennej `total_savings`.

`@hint`
- Przypisz `savings + new_savings` do nowej zmiennej `total_savings`.
- Aby wyświetlić typ zmiennej `x`, użyj `print(type(x))`.

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
msg = "Nie musisz zmieniać ani usuwać predefiniowanych zmiennych."

Ex().multi(
    check_object('savings', missing_msg=msg).has_equal_value(incorrect_msg=msg),
    check_object('new_savings', missing_msg=msg).has_equal_value(incorrect_msg=msg)
)

Ex().multi(
    check_object("total_savings").has_equal_value(incorrect_msg="Dodaj `savings` i `new_savings`, aby utworzyć zmienną `total_savings`."),
    has_printout(1, not_printed_msg = "__JINJA__:Użyj `{{sol_call}}`, aby wyświetlić typ `total_savings`.")
)
```

***

```yaml
type: NormalExercise
key: f54fbf9bd9
xp: 50
```

`@instructions`
- Oblicz sumę `intro` i `intro`, a wynik przypisz do zmiennej `doubleintro`.
- Wyświetl wartość zmiennej `doubleintro`. Czy spodziewałeś się takiego rezultatu?

`@hint`
- Przypisz `intro + intro` do nowej zmiennej `doubleintro`.
- Aby wyświetlić zmienną `x`, wpisz `print(x)` w skrypcie.

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
msg = "Nie musisz zmieniać ani usuwać predefiniowanych zmiennych."

Ex().check_object('intro', missing_msg=msg).has_equal_value(incorrect_msg=msg)

Ex().multi(
    check_object("doubleintro").has_equal_value(incorrect_msg  = "Czy zapisałeś/zapisałaś wynik `intro + intro` w `doubleintro`?"),
    has_printout(0, not_printed_msg = "Nie zapomnij wydrukować `doubleintro`.")
)

success_msg("Świetnie. Zauważ, jak `intro + intro` powoduje, że `\"Hello! How are you?\"` i `\"Hello! How are you?\"` są łączone razem.")
```

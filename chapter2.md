---
title_meta: Rozdział 2
title: Listy w Pythonie
description: >-
  Naucz się przechowywać dane w listach, uzyskiwać do nich dostęp i je
  modyfikować – to pierwszy krok do efektywnej pracy z dużymi zbiorami danych.
attachments:
  slides_link: 'https://projector-video-pdf-converter.datacamp.com/735/chapter2.pdf'
lessons:
  - nb_of_exercises: 4
    title: Listy w Pythonie
  - nb_of_exercises: 4
    title: Wybieranie elementów list
  - nb_of_exercises: 5
    title: Modyfikowanie list
---

## Listy w Pythonie

```yaml
type: VideoExercise
key: a5886d213f
xp: 50
```

`@projector_key`
a0530c4542f10988847b2dbb91f717c3

---

## Tworzenie listy

```yaml
type: NormalExercise
key: e6c527bf41
lang: python
xp: 100
skills:
  - 2
```

Lista to **złożony typ danych** – pozwala grupować wartości razem, na przykład:

```
a = "is"
b = "nice"
my_list = ["my", "list", a, b]
```

Po zmierzeniu wzrostu członków swojej rodziny postanawiasz zebrać informacje o domu, w którym mieszkasz. Pola powierzchni poszczególnych części domu są zapisane w osobnych zmiennych w tym ćwiczeniu.

`@instructions`
- Utwórz listę `areas`, która zawiera powierzchnię przedpokoju (`hall`), kuchni (`kit`), salonu (`liv`), sypialni (`bed`) i łazienki (`bath`) – w tej kolejności. Skorzystaj z predefiniowanych zmiennych.
- Wyświetl listę `areas` za pomocą funkcji `print()`.

`@hint`
- Możesz użyć zmiennych, które zostały już utworzone, aby zbudować listę: `areas = [hall, kit, ...]`.
- Pamiętaj, aby używać nawiasów kwadratowych `[]`, a nie okrągłych `()`.
- Nie musisz używać cudzysłowów, gdy przechowujesz zmienne na liście.
- Wpisz `print(areas)`, aby wyświetlić listę podczas przesyłania odpowiedzi.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Create list areas


# Print areas

```

`@solution`
```{python}
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Create list areas
areas = [hall, kit, liv, bed, bath]

# Print areas
print(areas)
```

`@sct`
```{python}
predef_msg = "Nie usuwaj ani nie edytuj predefiniowanych zmiennych!"
areas_msg = "Zdefiniuj `areas` jako listę zawierającą wszystkie zmienne obszarów, w odpowiedniej kolejności: `[hall, kit, liv, bed, bath]`. Uważaj na literówki. Lista nie powinna zawierać niczego innego!"

Ex().check_correct(
    has_printout(0, not_printed_msg = "__JINJA__:Czy użył(a) Pan(i) `{{sol_call}}`, aby wydrukować listę `areas` na końcu skryptu?"),
    check_correct(
        check_object("areas").has_equal_value(incorrect_msg = areas_msg),
        multi(
            check_object('hall', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
            check_object('kit', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
            check_object('liv', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
            check_object('bed', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
            check_object('bath', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg)
        )
    )
)

success_msg("Świetnie! Lista jest tutaj o wiele lepsza, prawda?")
```

---

## Tworzenie list z różnymi typami danych

```yaml
type: NormalExercise
key: 1702a8bcdc
lang: python
xp: 100
skills:
  - 2
```

Choć zdarza się to rzadko, lista może zawierać mieszankę różnych typów danych Pythona – łańcuchy znaków, liczby zmiennoprzecinkowe i wartości logiczne.

Teraz dodasz nazwy pomieszczeń do swojej listy, żeby od razu widzieć zarówno nazwę pomieszczenia, jak i jego powierzchnię.

Część kodu została już przygotowana, żebyś mógł zacząć. Zwróć uwagę: `"bathroom"` to łańcuch znaków, natomiast `bath` to zmienna przechowująca liczbę zmiennoprzecinkową `9.50`, którą podałeś wcześniej.

`@instructions`
- Dokończ kod tworzący listę `areas`. Zbuduj ją tak, żeby najpierw znajdowała się nazwa każdego pomieszczenia jako łańcuch znaków, a zaraz po niej jego powierzchnia. Innymi słowy, dodaj łańcuchy `"hallway"`, `"kitchen"` i `"bedroom"` we właściwych miejscach.
- Wyświetl ponownie listę `areas` – czy tym razem wynik jest bardziej czytelny?

`@hint`
- Pierwsze cztery elementy listy `areas` są zakodowane jako `["hallway", hall, "kitchen", kit, ...`.
- Łańcuch znaków musi być ujęty w cudzysłów `""`.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Adapt list areas
areas = [____, hall, ____, kit, "living room", liv, ____, bed, "bathroom", bath]

# Print areas
____
```

`@solution`
```{python}
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Adapt list areas
areas = ["hallway", hall, "kitchen", kit, "living room", liv, "bedroom", bed, "bathroom", bath]

# Print areas
print(areas)
```

`@sct`
```{python}
objs = ["hall", "kit", "liv", "bed", "bath"]
predef_msg = "Nie usuwaj ani nie edytuj predefiniowanych zmiennych!"
areas_msg = "Nie przypisano poprawnej wartości do `areas`. Proszę spojrzeć ponownie na instrukcje. Należy upewnić się, że nazwa pomieszczenia jest umieszczona przed zmienną zawierającą powierzchnię za każdym razem. Kolejność ma tu znaczenie! Proszę uważać na literówki."

Ex().check_correct(
  check_object("areas").has_equal_value(incorrect_msg = areas_msg),
  multi([ check_object(obj, missing_msg = predef_msg).has_equal_value(incorrect_msg = predef_msg) for obj in objs])
)

Ex().has_printout(0, not_printed_msg = "__JINJA__:Czy użyto `{{sol_call}}`, aby wydrukować listę `areas` na końcu skryptu?")

success_msg("Świetnie! Ta lista zawiera zarówno ciągi znaków, jak i liczby zmiennoprzecinkowe, ale nie stanowi to problemu dla Pythona!")
```

---

## Lista list

```yaml
type: NormalExercise
key: 9158c577b0
lang: python
xp: 100
skills:
  - 2
```

Jako badacz danych często będziesz pracować z dużą ilością danych i grupowanie ich okaże się bardzo przydatne.

Zamiast tworzyć listę zawierającą ciągi znaków i liczby zmiennoprzecinkowe reprezentujące nazwy i powierzchnie pomieszczeń w twoim domu, możesz stworzyć listę list.

Pamiętaj: `"hallway"` to ciąg znaków, natomiast `hall` to zmienna, która przechowuje wartość zmiennoprzecinkową `11.25` określoną wcześniej.

`@instructions`
- Uzupełnij listę list tak, aby zawierała również dane dotyczące sypialni i łazienki. Wprowadź je w odpowiedniej kolejności!
- Wyświetl listę `house` – czy taki sposób organizowania danych wydaje ci się bardziej czytelny?

`@hint`
- Dodaj _podlisty_ do listy `house`, wpisując `["bedroom", bed]` i `["bathroom", bath]` wewnątrz nawiasów kwadratowych.
- Pamiętaj, aby po każdej podliście wstawić przecinek `,`.
- Aby wyświetlić zmienną `x`, napisz `print(x)` w nowej linii.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# House information as list of lists
house = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv],
        ____,
        ____]

# Print out house
____
```

`@solution`
```{python}
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# House information as list of lists
house = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv],
         ["bedroom", bed],
         ["bathroom", bath]]

# Print out house
print(house)
```

`@sct`
```{python}
predef_msg = "Nie usuwaj ani nie edytuj predefiniowanych zmiennych!"
house_msg = "Nie przypisano poprawnej wartości do `house`. Proszę jeszcze raz zapoznać się z instrukcjami. Należy rozszerzyć listę list tak, aby zawierała listę dla każdej pary nazwy pokoju i jego powierzchni. Proszę zwrócić uwagę na kolejność i literówki!"

Ex().check_correct(
    check_object("house").has_equal_value(incorrect_msg = house_msg),
    multi(
        check_object('hall', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
        check_object('kit', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
        check_object('liv', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
        check_object('bed', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
        check_object('bath', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg)
    )
)

Ex().has_printout(0, not_printed_msg = "__JINJA__:Czy użyto `{{sol_call}}`, aby wydrukować zawartość `house`?")

success_msg("Świetnie! Przygotuj się na naukę o wyodrębnianiu elementów z list!")
```

---

## Wycinanie elementów z list

```yaml
type: VideoExercise
key: c076b5a69c
xp: 50
```

`@projector_key`
fc15ba5cb9485456df8589130b519ea3

---

## Indeksowanie list

```yaml
type: NormalExercise
key: c3ce582e32
lang: python
xp: 100
skills:
  - 2
```

Indeksowanie list w Pythonie jest bardzo proste. Spójrz na poniższy przykład: tworzymy listę `x`, a następnie wybieramy z niej element `"b"`. To drugi element, więc ma indeks 1. Możesz też używać indeksów ujemnych.

```
x = ["a", "b", "c", "d"]
x[1]
x[-3] # ten sam wynik!
```

Pamiętasz listę `areas` zawierającą zarówno napisy, jak i liczby zmiennoprzecinkowe? Jej definicja jest już w skrypcie. Dodaj odpowiedni kod, aby pobrać wybrane elementy listy.

`@instructions`
- Wyświetl drugi element listy `areas` (ma wartość `11.25`).
- Pobierz i wyświetl ostatni element listy `areas`, czyli `9.50`. Indeks ujemny będzie tu wygodnym rozwiązaniem!
- Wybierz liczbę reprezentującą powierzchnię salonu (`20.0`) i wyświetl ją.

`@hint`
- Użyj `x[1]`, aby wybrać drugi element listy `x`.
- Użyj `x[-1]`, aby wybrać ostatni element listy `x`.
- Pamiętaj, aby otoczyć operacje indeksowania wywołaniem `print()`.
- Liczba reprezentująca powierzchnię salonu to 6. element listy, więc potrzebujesz tutaj `[5]`. `area[4]` zwróciłoby napis!

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Print out second element from areas
print(areas[____])

# Print out last element from areas
print(areas[____])

# Print out the area of the living room
print(areas[____])
```

`@solution`
```{python}
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Print out second element from areas
print(areas[1])

# Print out last element from areas
print(areas[-1])

# Print out the area of the living room
print(areas[5])
```

`@sct`
```{python}
msg = "Nie usuwaj ani nie edytuj predefiniowanej listy `areas`."
Ex().check_object("areas", missing_msg = msg).has_equal_value(incorrect_msg = msg)
Ex().has_printout(0, not_printed_msg = "Przyjrzyj się ponownie swojemu kodowi, aby wyświetlić drugi element listy `areas`, który znajduje się pod indeksem `1`.")
Ex().has_printout(1, not_printed_msg = "Przyjrzyj się ponownie swojemu kodowi, aby wyświetlić ostatni element listy `areas`, który znajduje się pod indeksem `-1`.")
Ex().has_printout(2, not_printed_msg = "Przyjrzyj się ponownie swojemu kodowi, aby wyświetlić powierzchnię salonu. Znajduje się ona pod indeksem `5`.")
success_msg("Dobra robota!")
```

---

## Wycinanie fragmentów listy

```yaml
type: NormalExercise
key: 7f08642d18
lang: python
xp: 100
skills:
  - 2
```

Pobieranie pojedynczych wartości z listy to tylko część możliwości. Listę można też _wycinać_ (ang. _slicing_), czyli wybierać z niej wiele elementów naraz. Służy do tego następująca składnia:

```
my_list[start:end]
```

Element o indeksie `start` jest uwzględniany, natomiast element o indeksie `end` – już _nie_. Możesz też pominąć te indeksy. Jeśli nie podasz indeksu `start`, Python automatycznie przyjmie, że wycinek ma się zaczynać od początku listy.

`@instructions`
- Użyj wycinania, aby utworzyć listę `downstairs` zawierającą pierwsze 6 elementów listy `areas`.
- Utwórz listę `upstairs` jako ostatnie `4` elementy listy `areas`. Tym razem uprość zapis, pomijając indeks `end`.
- Wyświetl obie listy – `downstairs` i `upstairs` – za pomocą `print()`.

`@hint`
- Użyj nawiasów kwadratowych `[0:6]`, aby pobrać pierwsze sześć elementów listy.
- Aby pobrać wszystko oprócz pierwszych 5 elementów listy `l`, użyj `l[5:]`.
- Dodaj dwa wywołania `print()`, aby wyświetlić `downstairs` i `upstairs`.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Use slicing to create downstairs
downstairs = areas[____]

# Use slicing to create upstairs
upstairs = areas[____]

# Print out downstairs and upstairs
____
____
```

`@solution`
```{python}
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Use slicing to create downstairs
downstairs = areas[0:6]

# Use slicing to create upstairs
upstairs = areas[6:]

# Print out downstairs and upstairs
print(downstairs)
print(upstairs)
```

`@sct`
```{python}
msg = "Nie usuwaj ani nie edytuj predefiniowanej listy `areas`."
Ex().check_object("areas", missing_msg = msg).has_equal_value(incorrect_msg = msg)

patt = "`%s` jest niepoprawne. Użyj `areas[%s]` i wycinania, aby wybrać żądane elementy lub coś równoważnego."
Ex().check_object("downstairs").has_equal_value(incorrect_msg = patt % ('downstairs', '0:6'))
Ex().check_object("upstairs").has_equal_value(incorrect_msg = patt % ("upstairs",":6"))

Ex().has_printout(0, not_printed_msg="Czy wydrukowano `downstairs` po jego obliczeniu?")
Ex().has_printout(1, not_printed_msg="Czy wydrukowano `upstairs` po jego obliczeniu?")

success_msg("Świetnie!")
```

---

## Indeksowanie list zagnieżdżonych

```yaml
type: NormalExercise
key: dbbbd306cf
xp: 100
```

Lista w Pythonie może zawierać inne listy.

Aby odwoływać się do elementów list zagnieżdżonych, stosuj tę samą technikę co wcześniej: nawiasy kwadratowe. Dla listy `house` wygląda to następująco:

```
house[2][0]
```

`@instructions`
- Pobierz z listy `house` wartość zmiennoprzecinkową `9.5`.

`@hint`
- Rozłóż to na etapy. Najpierw odwołaj się do ostatniego elementu listy, czyli `["bathroom", 9.50]`. Pamiętaj, że indeks ostatniego elementu to `-1`.
- Następnie pobierz drugi element z `["bathroom", 9.50]`, który ma indeks `1`.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
house = [["hallway", 11.25],
         ["kitchen", 18.0],
         ["living room", 20.0],
         ["bedroom", 10.75],
         ["bathroom", 9.50]]

# Subset the house list
house___
```

`@solution`
```{python}
house = [["hallway", 11.25],
         ["kitchen", 18.0],
         ["living room", 20.0],
         ["bedroom", 10.75],
         ["bathroom", 9.50]]

# Subset the house list
house[-1][1]
```

`@sct`
```{python}
Ex().check_or(
  has_code("house[-1][1]", pattern=False),
  has_code("house[4][1]", pattern=False)
)

success_msg("Zgadza się! Ostatnim elementem układanki z listami jest manipulacja.")
```

---

## Manipulowanie listami

```yaml
type: VideoExercise
key: d7fe818b3a
xp: 50
```

`@projector_key`
355ed52d2fb0d67508c6a311b7cbc6d3

---

## Zastępowanie elementów listy

```yaml
type: NormalExercise
key: 4e1bba1b55
lang: python
xp: 100
skills:
  - 2
```

Aby zastąpić elementy listy, wybierasz odpowiedni podzbiór i przypisujesz do niego nowe wartości. Możesz wskazać pojedyncze elementy lub zmienić całe wycinki listy naraz.

W tym i kolejnych ćwiczeniach będziesz dalej pracować z listą `areas`, która zawiera nazwy i powierzchnie różnych pomieszczeń w domu.

`@instructions`
- Zaktualizuj powierzchnię łazienki – zmień wartość z `9.50` na `10.50` metra kwadratowego, korzystając z indeksowania ujemnego.
- Nadaj liście `areas` bardziej nowoczesny charakter! Zmień `"living room"` na `"chill zone"`. Tym razem nie używaj indeksowania ujemnego.

`@hint`
- Aby zaktualizować powierzchnię łazienki, wskaż odpowiedni podzbiór listy (to ostatni element listy!).
- Następnie przypisz nową wartość powierzchni do tego podzbioru.
- Zrób to samo, aby zmienić nazwę `"living room"`, która znajduje się pod indeksem 4.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Correct the bathroom area


# Change "living room" to "chill zone"

```

`@solution`
```{python}
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Correct the bathroom area
areas[-1] = 10.50

# Change "living room" to "chill zone"
areas[4] = "chill zone"
```

`@sct`
```{python}
bathroom_msg = 'Możesz użyć `areas[-1] = 10.50`, aby zaktualizować powierzchnię łazienki.'
chillzone_msg = 'Możesz użyć `areas[4] = "chill zone"`, aby zaktualizować nazwę salonu.'
Ex().check_correct(
  check_object('areas').has_equal_value(incorrect_msg = 'Wprowadzone zmiany w `areas` nie dały poprawnej listy. Czy na pewno użyto właściwych operacji na podzbiorach? W razie wątpliwości można skorzystać z podpowiedzi!'),
  multi(
    has_equal_value(expr_code='areas[-1]', override=10.50, incorrect_msg = bathroom_msg),
    has_equal_value(expr_code='areas[4]', override='chill zone', incorrect_msg = chillzone_msg),
  )
)
success_msg('Świetnie! Jak pokazał przykładowy kod, można również wyciąć fragment listy i zastąpić go inną listą, aby zaktualizować wiele elementów jednym poleceniem.')
```

---

## Rozszerzanie listy

```yaml
type: NormalExercise
key: ff0fe8d967
lang: python
xp: 100
skills:
  - 2
```

Skoro można zmieniać elementy listy, to pewnie chcesz też umieć dodawać do niej nowe, prawda? Możesz do tego użyć operatora `+`:

```
x = ["a", "b", "c", "d"]
y = x + ["e", "f"]
```

Wygrałeś na loterii – gratulacje! Postanawiasz dobudować basen i garaż. Dodaj odpowiednie informacje do listy `areas`.

`@instructions`
- Użyj operatora `+`, aby dołączyć listę `["poolhouse", 24.5]` na końcu listy `areas`. Zapisz wynikową listę jako `areas_1`.
- Rozszerz dalej `areas_1`, dodając dane dotyczące garażu. Dodaj ciąg znaków `"garage"` oraz liczbę zmiennoprzecinkową `15.45`. Wynikową listę nazwij `areas_2`.

`@hint`
- Postępuj zgodnie z przykładem kodu w treści zadania. `x` to tutaj `areas`, a `["e", "f"]` to `["poolhouse", 24.5]`.
- Aby dodać więcej elementów do `areas_1`, użyj `areas_1 + ["element", 123]`.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create the areas list and make some changes
areas = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0,
         "bedroom", 10.75, "bathroom", 10.50]

# Add poolhouse data to areas, new list is areas_1
areas_1 = ____

# Add garage data to areas_1, new list is areas_2
areas_2 = ____
```

`@solution`
```{python}
# Create the areas list (updated version)
areas = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0,
         "bedroom", 10.75, "bathroom", 10.50]

# Add poolhouse data to areas, new list is areas_1
areas_1 = areas + ["poolhouse", 24.5]

# Add garage data to areas_1, new list is areas_2
areas_2 = areas_1 + ["garage", 15.45]
```

`@sct`
```{python}
msg = "Nie usuwaj ani nie edytuj predefiniowanej listy `areas`."
Ex().check_object("areas", missing_msg = msg).has_equal_value(incorrect_msg = msg)
Ex().check_object("areas_1").has_equal_value(incorrect_msg = "Użyj `areas + [\"poolhouse\", 24.5]`, aby utworzyć `areas_1`. Uważaj na literówki!")
Ex().check_object("areas_2").has_equal_value(incorrect_msg = "Użyj `areas_1 + [\"garage\", 15.45]`, aby utworzyć `areas_2`. Uważaj na literówki!")
success_msg("Świetnie! Lista nabiera kształtu!")
```

---

## Usuwanie elementów listy

```yaml
type: NormalExercise
key: 85f792356e
xp: 100
```

Na koniec możesz też usuwać elementy z listy. Służy do tego instrukcja `del`:

```
x = ["a", "b", "c", "d"]
del x[1]
```

Zwróć uwagę: gdy tylko usuniesz element z listy, indeksy wszystkich kolejnych elementów ulegają zmianie!

Niestety wygrana na loterii okazała się nie tak duża, jak myślałeś, i wygląda na to, że basen w ogrodzie nie wchodzi w grę. Musisz usunąć go z listy. Zdecydujesz się usunąć odpowiadający mu napis i liczbę zmiennoprzecinkową z listy `areas`.

`@instructions`
- Usuń napis i liczbę zmiennoprzecinkową dla `"poolhouse"` z listy `areas`.
- Wyświetl zaktualizowaną listę `areas`.

`@hint`
- Musisz użyć `del` dwa razy, aby usunąć dwa elementy. Uważaj jednak na zmieniające się indeksy!

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
areas = ["hallway", 11.25, "kitchen", 18.0,
        "chill zone", 20.0, "bedroom", 10.75,
         "bathroom", 10.50, "poolhouse", 24.5,
         "garage", 15.45]

# Delete the poolhouse items from the list


# Print the updated list

```

`@solution`
```{python}
areas = ["hallway", 11.25, "kitchen", 18.0,
        "chill zone", 20.0, "bedroom", 10.75,
         "bathroom", 10.50, "poolhouse", 24.5,
         "garage", 15.45]

# Delete the poolhouse items from the list
del areas[10]
del areas[10]

# Print the updated list
print(areas)
```

`@sct`
```{python}
Ex().check_or(
  multi(
    has_code("del areas[10]", pattern=False),
    has_code("del areas[10]", pattern=False)
  ),
  has_code("del areas[-4:-2]", pattern=False),
  has_code("del(areas[-4:-2])", pattern=False),
  multi(
    has_code("del(areas[10])", pattern=False),
    has_code("del(areas[10])", pattern=False)
  ),
  has_code("del areas[10:12]", pattern=False),
  has_code("del(areas[10:12])", pattern=False),
  multi(
    has_code("del areas[-4]", pattern=False),
    has_code("del areas[-3]", pattern=False)
  ),
  multi(
    has_code("del(areas[-4])", pattern=False),
    has_code("del(areas[-3])", pattern=False)
  )
)

Ex().has_printout(0, not_printed_msg="Czy wyświetlono listę `areas` po usunięciu ciągu znaków i liczby zmiennoprzecinkowej dotyczących basenu?")
success_msg("Poprawnie! Później dowiedzą się Państwo o łatwiejszych sposobach usuwania określonych elementów z list w Pythonie.")
```

---

## Jak działają listy od środka

```yaml
type: NormalExercise
key: af72db9915
lang: python
xp: 100
skills:
  - 2
```

W tym ćwiczeniu masz już przygotowany kod: listę o nazwie `areas` oraz jej kopię o nazwie `areas_copy`.

Aktualnie pierwszy element listy `areas_copy` jest zmieniany, a następnie wypisywana jest lista `areas`. Jeśli klikniesz **Uruchom kod**, zobaczysz, że choć zmieniłeś(-aś) `areas_copy`, zmiana ta jest widoczna również w liście `areas`. Dzieje się tak dlatego, że `areas` i `areas_copy` wskazują na tę samą listę.

Jeśli chcesz, żeby zmiany w `areas_copy` nie wpływały na `areas`, musisz wykonać jawną kopię listy `areas` – za pomocą `list()` lub używając `[:]`.

`@instructions`
- Zmień drugie polecenie, które tworzy zmienną `areas_copy`, tak aby `areas_copy` była jawną kopią listy `areas`. Po tej zmianie modyfikacje wprowadzone w `areas_copy` nie powinny wpływać na `areas`. Prześlij odpowiedź, żeby to sprawdzić.

`@hint`
- Zmień wywołanie `areas_copy = areas`. Zamiast przypisywać `areas`, możesz przypisać `list(areas)` lub `areas[:]`.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Change this command
areas_copy = areas

# Change areas_copy
areas_copy[0] = 5.0

# Print areas
print(areas)
```

`@solution`
```{python}
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Change this command
areas_copy = list(areas)

# Change areas_copy
areas_copy[0] = 5.0

# Print areas
print(areas)
```

`@sct`
```{python}
Ex().check_correct(
  check_object("areas_copy").has_equal_value(incorrect_msg = "Wydaje się, że `areas_copy` nie została poprawnie zaktualizowana."),
  check_function("list", missing_msg = "Proszę użyć `list(areas)`, aby utworzyć `areas_copy`.")
)

mmsg = "Proszę nie usuwać predefiniowanej listy `areas`."
imsg = "Proszę edytować TYLKO kopię, a nie oryginalną listę `areas`. Jeśli nie jest jasne, jak utworzyć kopię, proszę ponownie zapoznać się z opisem ćwiczenia."
Ex().check_correct(
  check_object("areas", missing_msg = mmsg).has_equal_value(incorrect_msg = imsg),
  check_function("list", missing_msg = "Proszę użyć `list(areas)`, aby utworzyć `areas_copy`.")
)

success_msg("Świetnie! Różnica między kopiami jawnymi a kopiami opartymi na referencjach jest subtelna, ale może być naprawdę istotna. Warto pamiętać, w jaki sposób lista jest przechowywana w pamięci komputera.")
```

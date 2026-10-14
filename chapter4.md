---
title_meta: Rozdział 4
title: NumPy
description: >-
  NumPy to podstawowa biblioteka Pythona do efektywnej pracy w obszarze data
  science. Naucz się korzystać z możliwości tablic NumPy i zacznij eksplorować
  dane.
attachments:
  slides_link: 'https://projector-video-pdf-converter.datacamp.com/735/chapter4.pdf'
lessons:
  - nb_of_exercises: 5
    title: NumPy
  - nb_of_exercises: 5
    title: Dwuwymiarowe tablice NumPy
  - nb_of_exercises: 3
    title: 'NumPy: podstawy statystyki'
---

## NumPy

```yaml
type: VideoExercise
key: f4545baa53
xp: 50
```

`@projector_key`
a0487c26210f6b71ea98f917734cea3a

---

## Twoja pierwsza tablica NumPy

```yaml
type: NormalExercise
key: 84cab9d170
lang: python
xp: 100
skills:
  - 2
```

Czas zanurzyć się w świat baseballu. Po drodze poznasz podstawy `numpy` – potężnej biblioteki do analizy danych.

W skrypcie Pythona zdefiniowano już listę `baseball` zawierającą wzrost wybranych graczy baseballowych w centymetrach. Dodaj kod, który utworzy z niej tablicę `numpy`.

`@instructions`
- Zaimportuj pakiet `numpy` jako `np`, aby móc odwoływać się do `numpy` przez `np`.
- Użyj `np.array()`, aby utworzyć tablicę `numpy` z listy `baseball`. Nazwij tę tablicę `np_baseball`.
- Wyświetl typ zmiennej `np_baseball`, żeby sprawdzić, czy wszystko się zgadza.

`@hint`
- `import numpy as np` załatwi sprawę. Od tej pory używaj `np.fun_name()` za każdym razem, gdy chcesz skorzystać z funkcji `numpy`.
- `np.array()` powinno przyjąć jako argument `baseball`. Przypisz wynik wywołania funkcji do `np_baseball`.
- Aby wyświetlić typ zmiennej `x`, wpisz po prostu `print(type(x))`.

`@pre_exercise_code`
```{python}
import numpy as np
```

`@sample_code`
```{python}
# Import the numpy package as np


baseball = [180, 215, 210, 210, 188, 176, 209, 200]

# Create a numpy array from baseball: np_baseball


# Print out type of np_baseball

```

`@solution`
```{python}
# Import the numpy package as np
import numpy as np

baseball = [180, 215, 210, 210, 188, 176, 209, 200]

# Create a NumPy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out type of np_baseball
print(type(np_baseball))
```

`@sct`
```{python}
predef_msg = "Nie należy zmieniać ani usuwać predefiniowanych zmiennych."
Ex().has_import("numpy")
Ex().check_correct(
  check_object("np_baseball"),
  multi(
    check_object("baseball", missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
    check_function("numpy.array").check_args(0).has_equal_ast()
  )
)

Ex().has_printout(0)
success_msg("Świetna robota!")
```

---

## Wzrost baseballistów

```yaml
type: NormalExercise
key: e7e25a89ea
lang: python
xp: 100
skills:
  - 2
```

Jesteś wielkim fanem baseballa. Postanawiasz zadzwonić do MLB (Major League Baseball) i zapytać o dodatkowe statystyki dotyczące wzrostu głównych zawodników. Otrzymujesz dane o ponad tysiącu graczy, zapisane jako zwykła lista Pythona: `height_in`. Wzrost podany jest w calach. Czy potrafisz przekształcić ją w tablicę `numpy` i przeliczyć jednostki na metry?

`height_in` jest już dostępna, a pakiet `numpy` jest wczytany, więc możesz od razu zacząć (źródło: stat.ucla.edu).

`@instructions`
- Utwórz tablicę `numpy` na podstawie `height_in`. Nadaj tej tablicy nazwę `np_height_in`.
- Wyświetl `np_height_in`.
- Pomnóż `np_height_in` przez `0.0254`, aby przeliczyć wszystkie wartości wzrostu z cali na metry. Wynik zapisz w nowej tablicy `np_height_m`.
- Wyświetl `np_height_m` i sprawdź, czy wynik ma sens.

`@hint`
- Użyj `np.array()` i przekaż jej `height`. Wynik zapisz w `np_height_in`.
- Aby wyświetlić zmienną `x`, wpisz `print(x)` w skrypcie Pythona.
- Wykonaj obliczenia tak, jakby `np_height_in` był pojedynczą liczbą: `np_height_in * conversion_factor` jest częścią odpowiedzi.
- Aby wyświetlić zmienną `x`, wpisz `print(x)` w skrypcie Pythona.

`@pre_exercise_code`
```{python}
import pandas as pd
mlb = pd.read_csv("https://assets.datacamp.com/course/intro_to_python/baseball.csv")
height_in = mlb['Height'].tolist()
import numpy as np
```

`@sample_code`
```{python}
# Import numpy
import numpy as np

# Create a numpy array from height_in: np_height_in


# Print out np_height_in


# Convert np_height_in to m: np_height_m


# Print np_height_m

```

`@solution`
```{python}
# Import numpy
import numpy as np

# Create a numpy array from height_in: np_height_in
np_height_in = np.array(height_in)

# Print out np_height_in
print(np_height_in)

# Convert np_height_in to m: np_height_m
np_height_m = np_height_in * 0.0254

# Print np_height_m
print(np_height_m)
```

`@sct`
```{python}
Ex().has_import("numpy", same_as = False)

Ex().check_correct(
  has_printout(0),
  check_correct(
    check_object('np_height_in').has_equal_value(),
    check_function('numpy.array').check_args(0).has_equal_ast()
  )
)

Ex().check_correct(
  has_printout(1),
  check_object("np_height_m").has_equal_value(incorrect_msg = "Użyj `np_height_in * 0.0254`, aby obliczyć `np_height_m`.")
)

success_msg("Świetnie! W mgnieniu oka `numpy` wykonuje mnożenia na ponad 1000 pomiarach wzrostu.")
```

---

## Efekty uboczne NumPy

```yaml
type: MultipleChoiceExercise
key: 3662ff6637
lang: python
xp: 50
skills:
  - 2
```

`numpy` świetnie sprawdza się przy arytmetyce wektorowej. Jeśli jednak porównasz jego działanie ze zwykłymi listami Pythona, zauważysz pewne różnice.

Po pierwsze, tablice `numpy` nie mogą zawierać elementów różnych typów. Gdy pomieszasz typy – na przykład wartości logiczne z liczbami całkowitymi – `numpy` automatycznie przekonwertuje je do wspólnego typu. Wartości logiczne `True` i `False` są traktowane odpowiednio jako `1` i `0`, kiedy zestawia się je z liczbami, więc tablica przyjmuje typ całkowitoliczbowy.

Po drugie, typowe operatory arytmetyczne, takie jak `+`, `-`, `*` i `/`, mają inne znaczenie dla zwykłych list Pythona i tablic `numpy`.

Wybierz kod, który daje następujący wynik:

```
np.array([True, 1, 2]) + np.array([3, 4, False])
```

Pakiet `numpy` jest już zaimportowany jako `np`. Każdą z opcji możesz uruchomić w powłoce IPython, aby sprawdzić wynik.

`@possible_answers`
- `np.array([True, 1, 2, 3, 4, False])`
- `np.array([4, 3, 0]) + np.array([0, 2, 2])`
- `np.array([1, 1, 2]) + np.array([3, 4, -1])`
- `np.array([0, 1, 2, 3, 4, 5])`

`@hint`
- Skopiuj poszczególne fragmenty kodu i wklej je do powłoki IPython. Naciśnij **Enter**, aby uruchomić kod i sprawdzić, który wynik odpowiada temu generowanemu przez `np.array([True, 1, 2]) + np.array([3, 4, False])`.

`@pre_exercise_code`
```{python}
import numpy as np
```

`@sct`
```{python}
msg1 = msg3 = msg4 = "Niepoprawnie. Wypróbuj różne fragmenty kodu i sprawdź, który pasuje do docelowego fragmentu kodu."
msg2 = "Świetna robota! `True` jest konwertowane na 1, `False` jest konwertowane na 0."
Ex().has_chosen(2, [msg1, msg2, msg3, msg4])
```

---

## Indeksowanie tablic NumPy

```yaml
type: NormalExercise
key: fcb2a9007b
lang: python
xp: 100
skills:
  - 2
```

Indeksowanie (czyli korzystanie z nawiasów kwadratowych na listach lub tablicach) działa dokładnie tak samo w przypadku list i tablic.

W tym ćwiczeniu w tle są już wczytane dwie listy: `height_in` i `weight_lb`. Zawierają one wzrost i wagę graczy MLB jako zwykłe listy. Przygotowano dla ciebie również dwie tablice `numpy`: `np_weight_lb` i `np_height_in`.

`@instructions`
- Pobierz element z indeksu 50 z tablicy `np_weight_lb` i wyświetl go za pomocą `print()`.
- Wyświetl podtablicę z `np_height_in`, która zawiera elementy od indeksu 100 do indeksu 110 **włącznie**.

`@hint`
- Pamiętaj, aby otoczyć operacje indeksowania wywołaniem `print()`.
- Użyj `[100:111]`, aby pobrać elementy od indeksu 100 aż do indeksu 110 włącznie.

`@pre_exercise_code`
```{python}
import pandas as pd
mlb = pd.read_csv("https://assets.datacamp.com/course/intro_to_python/baseball.csv")
height_in = mlb['Height'].tolist()
weight_lb = mlb['Weight'].tolist()
```

`@sample_code`
```{python}
import numpy as np

np_weight_lb = np.array(weight_lb)
np_height_in = np.array(height_in)

# Print out the weight at index 50


# Print out sub-array of np_height_in: index 100 up to and including index 110

```

`@solution`
```{python}
import numpy as np

np_weight_lb = np.array(weight_lb)
np_height_in = np.array(height_in)

# Print out the weight at index 50
print(np_weight_lb[50])

# Print out sub-array of np_height_in: index 100 up to and including index 110
print(np_height_in[100:111])
```

`@sct`
```{python}
Ex().has_import("numpy", same_as=False)
msg = "Nie musisz zmieniać ani usuwać predefiniowanych zmiennych."
Ex().multi(
    check_object("np_height_in", missing_msg=msg).has_equal_value(incorrect_msg = msg),
    check_object("np_weight_lb", missing_msg=msg).has_equal_value(incorrect_msg = msg)
)

Ex().has_printout(0)
Ex().has_printout(1)

success_msg("Świetnie! Czas nauczyć się czegoś nowego: dwuwymiarowe tablice NumPy!")
```

---

## Dwuwymiarowe tablice NumPy

```yaml
type: VideoExercise
key: 1241efac7a
xp: 50
```

`@projector_key`
ae3238dcc7feb9adecfee0c395fc8dc8

---

## Twoja pierwsza dwuwymiarowa tablica NumPy

```yaml
type: NormalExercise
key: 5cb045bb13
lang: python
xp: 100
skills:
  - 2
```

Zanim przejdziemy do właściwych danych MLB, spróbuj utworzyć dwuwymiarową tablicę `numpy` na podstawie małej listy list.

W tym ćwiczeniu `baseball` to lista list. Główna lista zawiera 4 elementy. Każdy z nich to lista zawierająca wzrost i wagę jednego z 4 baseballistów – właśnie w tej kolejności. Zmienna `baseball` jest już zdefiniowana w skrypcie.

`@instructions`
- Użyj `np.array()`, aby utworzyć dwuwymiarową tablicę `numpy` na podstawie `baseball`. Nadaj jej nazwę `np_baseball`.
- Wyświetl typ zmiennej `np_baseball`.
- Wyświetl atrybut `shape` tablicy `np_baseball`, korzystając z `np_baseball.shape`.

`@hint`
- `baseball` jest już zdefiniowane w skrypcie. Wywołaj na nim `np.array()` i zapisz wynikową dwuwymiarową tablicę `numpy` w zmiennej `np_baseball`.
- Użyj `print()` razem z `type()` do drugiego polecenia.
- `np_baseball.shape` zwróci wymiary tablicy `np_baseball`. Pamiętaj, żeby opakować to wywołanie w `print()`.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
import numpy as np

baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

# Create a 2D numpy array from baseball: np_baseball


# Print out the type of np_baseball


# Print out the shape of np_baseball

```

`@solution`
```{python}
import numpy as np

baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

# Create a 2D numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out the type of np_baseball
print(type(np_baseball))

# Print out the shape of np_baseball
print(np_baseball.shape)
```

`@sct`
```{python}
msg = "Nie musisz zmieniać ani usuwać predefiniowanych zmiennych."
Ex().check_object("baseball", missing_msg=msg).has_equal_value(incorrect_msg = msg)
Ex().has_import("numpy", same_as = False)

Ex().check_correct(
    multi(
        has_printout(0),
        has_printout(1)
    ),
    check_correct(
        check_object('np_baseball').has_equal_value(),
        check_function('numpy.array').check_args(0).has_equal_ast()
    )
)

success_msg("Świetnie! Teraz możesz przekonwertować rzeczywiste dane MLB do dwuwymiarowej tablicy `numpy`!")
```

---

## Dane baseballowe w formie 2D

```yaml
type: NormalExercise
key: 5df25d0b7b
lang: python
xp: 100
skills:
  - 2
```

Zauważasz, że lepiej byłoby uporządkować wszystkie te informacje w dwuwymiarowej tablicy `numpy`.

Masz listę list w Pythonie. Każda podlista reprezentuje wzrost i wagę jednego gracza baseballowego. Ta lista nazywa się `baseball` i została już dla ciebie wczytana (choć jej nie widzisz).

Zapisz dane jako tablicę 2D, aby skorzystać z dodatkowych możliwości biblioteki `numpy`.

`@instructions`
- Użyj `np.array()`, aby utworzyć dwuwymiarową tablicę `numpy` z listy `baseball`. Nazwij ją `np_baseball`.
- Wyświetl atrybut `shape` tablicy `np_baseball`.

`@hint`
- `baseball` jest już dostępny w środowisku Pythona. Wywołaj na nim `np.array()` i zapisz wynikową tablicę 2D `numpy` w zmiennej `np_baseball`.
- `np_baseball.shape` zwróci wymiary tablicy `np_baseball`. Pamiętaj, aby owinąć to wywołanie funkcją `print()`.

`@pre_exercise_code`
```{python}
import pandas as pd
baseball = pd.read_csv("https://assets.datacamp.com/course/intro_to_python/baseball.csv")[['Height', 'Weight']].to_numpy().tolist()
import numpy as np
```

`@sample_code`
```{python}
import numpy as np

# Create a 2D numpy array from baseball: np_baseball
np_baseball = 

# Print out the shape of np_baseball

```

`@solution`
```{python}
import numpy as np

# Create a 2D numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out the shape of np_baseball
print(np_baseball.shape)
```

`@sct`
```{python}
Ex().has_import("numpy", same_as = False)

Ex().check_correct(
    has_printout(0),
    check_correct(
        check_object('np_baseball').has_equal_value(),
        check_function('numpy.array').check_args(0).has_equal_ast()
    )
)

success_msg("Świetnie! Czas pokazać kilka zabójczych funkcji wielowymiarowych tablic `numpy`!")
```

---

## Wycinanie fragmentów dwuwymiarowych tablic NumPy

```yaml
type: NormalExercise
key: aeca4977f0
lang: python
xp: 100
skills:
  - 2
```

Jeśli twoja dwuwymiarowa tablica `numpy` ma regularną strukturę – tzn. każdy wiersz i kolumna mają stałą liczbę wartości – wycinanie jej fragmentów staje się bardzo proste. Przyjrzyj się poniższemu kodowi, w którym elementy `"a"` i `"c"` są wyodrębniane z listy list.

```
# numpy
import numpy as np
np_x = np.array(x)
np_x[:, 0]
```

Indeksy przed przecinkiem odnoszą się do wierszy, a te po przecinku – do kolumn. Znak `:` służy do wycinania zakresów; w tym przykładzie informuje Pythona, że mają zostać uwzględnione wszystkie wiersze.

`@instructions`
- Wyświetl 50. wiersz tablicy `np_baseball`.
- Utwórz nową zmienną `np_weight_lb`, która będzie zawierać cały drugi kolumnę tablicy `np_baseball`.
- Wybierz wzrost (pierwsza kolumna) 124. gracza baseballowego z tablicy `np_baseball` i wyświetl go.

`@hint`
- W pierwszej instrukcji potrzebujesz indeksu wiersza 49! Dokładniej mówiąc, użyj `[49, :]`.
- Aby wybrać cały drugi kolumnę, użyj `[:, 1]`.
- W ostatniej instrukcji użyj `[123, 0]` i nie zapomnij otoczyć całości wywołaniem `print()`.

`@pre_exercise_code`
```{python}
import pandas as pd
baseball = pd.read_csv("https://assets.datacamp.com/course/intro_to_python/baseball.csv")[['Height', 'Weight']].to_numpy().tolist()
import numpy as np
```

`@sample_code`
```{python}
import numpy as np

np_baseball = np.array(baseball)

# Print out the 50th row of np_baseball


# Select the entire second column of np_baseball: np_weight_lb


# Print out height of 124th player

```

`@solution`
```{python}
import numpy as np

np_baseball = np.array(baseball)

# Print out the 50th row of np_baseball
print(np_baseball[49,:])

# Select the entire second column of np_baseball: np_weight_lb
np_weight_lb = np_baseball[:,1]

# Print out height of 124th player
print(np_baseball[123, 0])
```

`@sct`
```{python}
msg = "Nie musisz zmieniać ani usuwać predefiniowanych zmiennych."
Ex().multi(
    has_import("numpy", same_as = False),
    check_object("np_baseball", missing_msg=msg).has_equal_value(incorrect_msg = msg)
)

Ex().has_printout(0)

Ex().check_object('np_weight_lb').has_equal_value(incorrect_msg = "Możesz użyć `np_baseball[:,1]`, aby zdefiniować `np_weight_lb`. Spowoduje to wybranie całej pierwszej kolumny.")

Ex().has_printout(1)

success_msg("Idzie dobrze!")
```

---

## Arytmetyka 2D

```yaml
type: NormalExercise
key: 1c2378b677
lang: python
xp: 100
skills:
  - 2
```

Dwuwymiarowe tablice `numpy` umożliwiają wykonywanie obliczeń element po elemencie, podobnie jak zwykłe tablice `numpy`.

`np_baseball` jest już zdefiniowany – to dwuwymiarowa tablica `numpy` z 3 kolumnami reprezentującymi wzrost (w calach), wagę (w funtach) i wiek (w latach). `baseball` jest dostępny jako zwykła lista list, a `updated` jako dwuwymiarowa tablica numpy.

`@instructions`
- Udało ci się zdobyć dane o zmianach wzrostu, wagi i wieku wszystkich baseballistów. Są one dostępne jako dwuwymiarowa tablica `numpy` o nazwie `updated`. Dodaj `np_baseball` i `updated`, a następnie wyświetl wynik.
- Chcesz przeliczyć jednostki wzrostu i wagi na metryczne (odpowiednio metry i kilogramy). Jako pierwszy krok utwórz tablicę `numpy` z trzema wartościami: `0.0254`, `0.453592` i `1`. Nazwij tę tablicę `conversion`.
- Pomnóż `np_baseball` przez `conversion` i wyświetl wynik.

`@hint`
- `np_baseball + updated` wykona sumowanie element po elemencie dwóch tablic `numpy`.
- Utwórz tablicę `numpy` za pomocą `np.array()`; na wejściu podaj zwykłą listę Pythona z trzema elementami.
- `np_baseball * conversion` zadziała bez żadnych dodatkowych kroków. Wypróbuj to! Pamiętaj, żeby opakować wynik w wywołanie `print()`.

`@pre_exercise_code`
```{python}
import pandas as pd
import numpy as np
baseball = pd.read_csv("https://assets.datacamp.com/course/intro_to_python/baseball.csv")[['Height', 'Weight', 'Age']].to_numpy().tolist()
n = len(baseball)
updated = np.array(pd.read_csv("https://assets.datacamp.com/course/intro_to_python/update.csv", header = None))
import numpy as np
```

`@sample_code`
```{python}
import numpy as np

np_baseball = np.array(baseball)

# Print out addition of np_baseball and updated


# Create numpy array: conversion


# Print out product of np_baseball and conversion

```

`@solution`
```{python}
import numpy as np

np_baseball = np.array(baseball)

# Print out addition of np_baseball and updated
print(np_baseball + updated)

# Create numpy array: conversion
conversion = np.array([0.0254, 0.453592, 1])

# Print out product of np_baseball and conversion
print(np_baseball * conversion)
```

`@sct`
```{python}
Ex().has_import("numpy")

msg = "Nie musisz zmieniać ani usuwać predefiniowanych zmiennych."
Ex().check_object("np_baseball", missing_msg=msg).has_equal_value(incorrect_msg = msg)

Ex().has_printout(0)

Ex().check_correct(
    has_printout(1),
    check_correct(
        check_object('conversion').has_equal_value(),
        check_function('numpy.array', index = 1).check_args(0).has_equal_value()
    )    
)

success_msg("Świetna robota! Zwróć uwagę, jak przy użyciu bardzo małej ilości kodu możesz zmieniać wszystkie wartości w strukturze danych `numpy` w bardzo precyzyjny sposób. Będzie to bardzo przydatne w Państwa przyszłej karierze jako analityk danych!")
```

---

## NumPy: Podstawy statystyki

```yaml
type: VideoExercise
key: 287995e488
xp: 50
```

`@projector_key`
34495ba457d74296794d2a122c9b6e19

---

## Średnia a mediana

```yaml
type: NormalExercise
key: 509c588eb6
lang: python
xp: 100
skills:
  - 2
```

Wiesz już, jak korzystać z funkcji `numpy`, aby lepiej zrozumieć swoje dane.

Dane baseballowe są dostępne jako dwuwymiarowa tablica `numpy` z 3 kolumnami (wzrost, waga, wiek) i 1015 wierszami. Tablica ta nosi nazwę `np_baseball`. Po przetworzeniu danych zauważasz jednak, że niektóre wartości wzrostu są wyjątkowo wysokie. Wykonaj poniższe instrukcje i sprawdź, która miara statystyczna najlepiej sprawdza się w przypadku tzw. _wartości odstających_. Tablica `np_baseball` jest już dostępna.

`@instructions`
- Utwórz tablicę `numpy` o nazwie `np_height_in`, równą pierwszej kolumnie tablicy `np_baseball`.
- Wyświetl średnią wartość tablicy `np_height_in`.
- Wyświetl medianę tablicy `np_height_in`.

`@hint`
- Użyj indeksowania 2D w `numpy`: `[:,0]` jest częścią rozwiązania.
- Jeśli `numpy` jest zaimportowane jako `np`, możesz użyć `np.mean()`, aby obliczyć średnią tablicy NumPy. Nie zapomnij dodać wywołania `print()`.
- W ostatniej instrukcji użyj `np.median()`.

`@pre_exercise_code`
```{python}
import pandas as pd
np_baseball = pd.read_csv("https://assets.datacamp.com/course/intro_to_python/baseball.csv")[['Height', 'Weight', 'Age']].to_numpy()
np_baseball[slice(0, 1015, 50), 0] = np_baseball[slice(0, 1015, 50), 0]*1000
import numpy as np
```

`@sample_code`
```{python}
import numpy as np

# Create np_height_in from np_baseball


# Print out the mean of np_height_in


# Print out the median of np_height_in

```

`@solution`
```{python}
import numpy as np

# Create np_height_in from np_baseball
np_height_in = np_baseball[:,0]

# Print out the mean of np_height_in
print(np.mean(np_height_in))

# Print out the median of np_height_in
print(np.median(np_height_in))
```

`@sct`
```{python}
Ex().has_import("numpy", same_as = False)

Ex().check_object("np_height_in").has_equal_value(incorrect_msg = "Można użyć `np_baseball[:,0]`, aby wybrać pierwszą kolumnę z `np_baseball`."),

Ex().check_correct(
    has_printout(0),
    check_function('numpy.mean').has_equal_value()
)

Ex().check_correct(
    has_printout(1),
    check_function('numpy.median').has_equal_value()
)

success_msg("Średnia wysokość wynosi 1586 cali – brzmi to nieprawdopodobnie, prawda? Jednak mediana wydaje się być odporna na wartości odstające: 74 cale brzmią całkowicie rozsądnie. Zawsze warto sprawdzić zarówno medianę, jak i średnią, aby uzyskać ogólny obraz rozkładu całego zbioru danych.")
```

---

## Eksploracja danych baseballowych

```yaml
type: NormalExercise
key: '4409948807'
lang: python
xp: 100
skills:
  - 2
```

Ponieważ średnia i mediana tak bardzo się od siebie różnią, postanawiasz złożyć skargę do MLB. Organizacja odnajduje błąd i przesyła ci poprawione dane. Są one ponownie dostępne jako dwuwymiarowa tablica NumPy `np_baseball` z trzema kolumnami.

Skrypt Pythona w edytorze zawiera już kod wyświetlający informacyjne komunikaty z różnymi statystykami podsumowującymi, a biblioteka `numpy` jest załadowana jako `np`. Czy uda ci się ukończyć zadanie? Tablica `np_baseball` jest dostępna.

`@instructions`
- Kod wyświetlający średnią wzrostu jest już gotowy. Uzupełnij kod obliczający medianę wzrostu.
- Użyj `np.std()` na pierwszej kolumnie tablicy `np_baseball`, aby obliczyć `stddev`.
- Czy wyżsi zawodnicy mają tendencję do większej masy ciała? Użyj `np.corrcoef()`, aby zapisać korelację między pierwszą a drugą kolumną tablicy `np_baseball` w zmiennej `corr`.

`@hint`
- Użyj `np.median()`, aby obliczyć medianę. Pamiętaj, żeby najpierw wybrać właściwą kolumnę!
- Przy obliczaniu odchylenia standardowego za pomocą `np.std()` wybierz tę samą kolumnę.
- Użyj `np_baseball[:, 0]` i `np_baseball[:, 1]`, aby wybrać pierwszą i drugą kolumnę – to właśnie te wartości przekazujesz do `np.corrcoef()`.

`@pre_exercise_code`
```{python}
import pandas as pd
np_baseball = pd.read_csv("https://assets.datacamp.com/course/intro_to_python/baseball.csv")[['Height', 'Weight', 'Age']].to_numpy()
import numpy as np
```

`@sample_code`
```{python}
avg = np.mean(np_baseball[:,0])
print("Average: " + str(avg))

# Print median height
med = ____
print("Median: " + str(med))

# Print out the standard deviation on height
stddev = ____
print("Standard Deviation: " + str(stddev))

# Print out correlation between first and second column
corr = ____
print("Correlation: " + str(corr))
```

`@solution`
```{python}
avg = np.mean(np_baseball[:,0])
print("Average: " + str(avg))

# Print median height
med = np.median(np_baseball[:,0])
print("Median: " + str(med))

# Print out the standard deviation on height
stddev = np.std(np_baseball[:,0])
print("Standard Deviation: " + str(stddev))

# Print out correlation between first and second column
corr = np.corrcoef(np_baseball[:,0], np_baseball[:,1])
print("Correlation: " + str(corr))
```

`@sct`
```{python}
msg = "Nie należy zmieniać ani usuwać predefiniowanej zmiennej `avg`."
Ex().check_object("avg", missing_msg=msg).has_equal_value(incorrect_msg=msg)

missing = "Czy użyto funkcji `np.median()` do obliczenia mediany?"
incorrect = "Aby obliczyć `med`, należy przekazać pierwszą kolumnę `np_baseball` do funkcji `numpy.median()`. Przykład użycia `np.mean()` pokazuje, jak to zrobić."
Ex().check_correct(
  check_object("med").has_equal_value(),
  check_function("numpy.median", index=0, missing_msg=missing).check_args(0).has_equal_value(incorrect_msg=incorrect)
)

missing = "Czy użyto funkcji `np.std()` do obliczenia odchylenia standardowego?"
incorrect = "Aby obliczyć `stddev`, należy przekazać pierwszą kolumnę `np_baseball` do funkcji `numpy.std()`. Przykład użycia `np.mean()` pokazuje, jak to zrobić."
Ex().check_correct(
  check_object("stddev").has_equal_value(),
  check_function("numpy.std", index=0, missing_msg=missing).check_args(0).has_equal_value(incorrect_msg=incorrect)
)

missing = "Czy użyto funkcji `np.corrcoef()` do obliczenia korelacji?"
incorrect1 = "Aby obliczyć `corr`, pierwszym argumentem funkcji `np.corrcoef()` powinna być pierwsza kolumna `np_baseball`, podobnie jak zostało to zrobione wcześniej."
incorrect2 = "Aby obliczyć `corr`, drugim argumentem funkcji `np.corrcoef()` powinna być druga kolumna `np_baseball`. Zamiast `[:,0]` należy użyć tym razem `[:,1]`."
Ex().check_correct(
  check_object("corr").has_equal_value(),
  check_function("numpy.corrcoef", index=0, missing_msg=missing).multi(
    check_args(0, missing_msg=incorrect1).has_equal_value(incorrect_msg=incorrect1),
    check_args(1, missing_msg=incorrect2).has_equal_value(incorrect_msg=incorrect2)
  )
)

success_msg("Świetna robota! Zbudowano solidne podstawy — teraz czas wykorzystać wszystkie nowe umiejętności z zakresu nauki o danych, aby rozwiązywać kolejne wyzwania i wywierać realny wpływ.")
```

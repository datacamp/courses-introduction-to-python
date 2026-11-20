---
title_meta: Kapitola 4
title: NumPy
description: >-
  NumPy je základní Python balíček pro efektivní práci v oblasti datové vědy.
  Naučíš se pracovat s výkonnými nástroji pole NumPy a uděláš první kroky v
  průzkumu dat.
attachments:
  slides_link: 'https://projector-video-pdf-converter.datacamp.com/735/chapter4.pdf'
lessons:
  - nb_of_exercises: 5
    title: NumPy
  - nb_of_exercises: 5
    title: 2D pole NumPy
  - nb_of_exercises: 3
    title: 'NumPy: základní statistika'
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

## Tvoje první NumPy pole

```yaml
type: NormalExercise
key: 84cab9d170
lang: python
xp: 100
skills:
  - 2
```

Teď se ponoříš do světa baseballu. Cestou se seznámíš se základy `numpy` – výkonného balíčku pro práci s daty.

V Python skriptu je už připravený seznam `baseball` s výškami několika baseballových hráčů v centimetrech. Zkus přidat kód, který z tohoto seznamu vytvoří pole `numpy`.

`@instructions`
- Importuj balíček `numpy` jako `np`, abys na něj mohl/a odkazovat zkráceně pomocí `np`.
- Pomocí `np.array()` vytvoř z `baseball` pole `numpy`. Toto pole pojmenuj `np_baseball`.
- Vypiš typ proměnné `np_baseball`, abys ověřil/a, že vše proběhlo správně.

`@hint`
- `import numpy as np` to załatví. Pak používej `np.fun_name()` vždy, když chceš volat funkci z `numpy`.
- `np.array()` by mělo dostat na vstupu `baseball`. Výsledek volání funkce přiřaď do `np_baseball`.
- Pro výpis typu proměnné `x` jednoduše napiš `print(type(x))`.

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
predef_msg = "Předdefinované proměnné není třeba měnit ani odstraňovat."
Ex().has_import("numpy")
Ex().check_correct(
  check_object("np_baseball"),
  multi(
    check_object("baseball", missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
    check_function("numpy.array").check_args(0).has_equal_ast()
  )
)

Ex().has_printout(0)
success_msg("Skvělá práce!")
```

---

## Výška hráčů baseballu

```yaml
type: NormalExercise
key: e7e25a89ea
lang: python
xp: 100
skills:
  - 2
```

Jsi velký fanoušek baseballu. Rozhodneš se zavolat do MLB (Major League Baseball) a zjistit další statistiky o výšce hlavních hráčů. Dostanou se k tobě data o více než tisíci hráčích, která jsou uložená jako běžný pythonový seznam: `height_in`. Výška je vyjádřena v palcích. Dokážeš z něj vytvořit pole `numpy` a převést jednotky na metry?

`height_in` je už k dispozici a balíček `numpy` je načten, takže můžeš rovnou začít (zdroj: stat.ucla.edu).

`@instructions`
- Vytvoř pole `numpy` z `height_in` a pojmenuj ho `np_height_in`.
- Vypiš `np_height_in`.
- Vynásob `np_height_in` hodnotou `0.0254`, abys převedl/a všechny výšky z palců na metry. Nové hodnoty ulož do pole `np_height_m`.
- Vypiš `np_height_m` a zkontroluj, jestli výsledek dává smysl.

`@hint`
- Použij `np.array()` a předej mu `height`. Výsledek ulož do `np_height_in`.
- Pro výpis proměnné `x` napiš do skriptu `print(x)`.
- Počítej s `np_height_in` jako s běžným číslem: součást odpovědi je `np_height_in * conversion_factor`.
- Pro výpis proměnné `x` napiš do skriptu `print(x)`.

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
  check_object("np_height_m").has_equal_value(incorrect_msg = "Pro výpočet `np_height_m` použijte `np_height_in * 0.0254`.")
)

success_msg("Výborně! `numpy` provede násobení více než 1000 měření výšky během okamžiku.")
```

---

## Vedlejší efekty NumPy

```yaml
type: MultipleChoiceExercise
key: 3662ff6637
lang: python
xp: 50
skills:
  - 2
```

`numpy` je skvělý nástroj pro vektorové výpočty. Když ale jeho funkce porovnáš s běžnými Python listy, zjistíš, že se v některých věcech liší.

Za prvé, pole `numpy` nemůžou obsahovat prvky různých typů. Pokud typy smícháš – například booleany s celými čísly – `numpy` je automaticky převede na společný typ. Booleany jako `True` a `False` se při kombinaci s čísly chovají jako `1` a `0`, takže výsledné pole bude tvořeno celými čísly.

Za druhé, běžné aritmetické operátory jako `+`, `-`, `*` a `/` mají jiný význam pro standardní Python listy a pro pole `numpy`.

Vyber kód, který produkuje následující výstup:

```
np.array([True, 1, 2]) + np.array([3, 4, False])
```

Balíček `numpy` je už naimportovaný jako `np`. Každou z možností si můžeš vyzkoušet přímo v IPython Shellu.

`@possible_answers`
- `np.array([True, 1, 2, 3, 4, False])`
- `np.array([4, 3, 0]) + np.array([0, 2, 2])`
- `np.array([1, 1, 2]) + np.array([3, 4, -1])`
- `np.array([0, 1, 2, 3, 4, 5])`

`@hint`
- Zkopíruj jednotlivé úryvky kódu a vlož je do IPython Shellu. Stiskni **Enter** a spusť kód – uvidíš, které výsledky odpovídají výstupu výrazu `np.array([True, 1, 2]) + np.array([3, 4, False])`.

`@pre_exercise_code`
```{python}
import numpy as np
```

`@sct`
```{python}
msg1 = msg3 = msg4 = "Nesprávně. Vyzkoušejte různé části kódu a zjistěte, která odpovídá cílovému bloku kódu."
msg2 = "Výborně! `True` se převede na 1, `False` se převede na 0."
Ex().has_chosen(2, [msg1, msg2, msg3, msg4])

```

---

## Subsetting NumPy polí

```yaml
type: NormalExercise
key: fcb2a9007b
lang: python
xp: 100
skills:
  - 2
```

Subsetting (výběr prvků pomocí hranatých závorek u seznamů nebo polí) funguje úplně stejně jak u seznamů, tak u polí.

Toto cvičení má v pozadí připravené dva seznamy, `height_in` a `weight_lb`. Obsahují výšku a váhu hráčů MLB jako běžné seznamy. Jsou tu také dvě `numpy` pole, `np_weight_lb` a `np_height_in`.

`@instructions`
- Vyber prvek z `np_weight_lb` na indexu 50 a vypiš ho.
- Vypiš podpole z `np_height_in`, které obsahuje prvky od indexu 100 až po index 110 **včetně**.

`@hint`
- Nezapomeň obalit operace subsettingu voláním `print()`.
- Použij `[100:111]` pro získání prvků od indexu 100 až po index 110 včetně.

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
msg = "Předdefinované proměnné není třeba měnit ani odstraňovat."
Ex().multi(
    check_object("np_height_in", missing_msg=msg).has_equal_value(incorrect_msg = msg),
    check_object("np_weight_lb", missing_msg=msg).has_equal_value(incorrect_msg = msg)
)

Ex().has_printout(0)
Ex().has_printout(1)

success_msg("Výborně! Je čas naučit se něco nového: 2D NumPy pole!")
```

---

## 2D NumPy Arrays

```yaml
type: VideoExercise
key: 1241efac7a
xp: 50
```

`@projector_key`
ae3238dcc7feb9adecfee0c395fc8dc8

---

## Tvoje první 2D pole NumPy

```yaml
type: NormalExercise
key: 5cb045bb13
lang: python
xp: 100
skills:
  - 2
```

Než se pustíme do skutečných dat MLB, vyzkoušíme si vytvořit 2D pole `numpy` z jednoduchého seznamu seznamů.

V tomto cvičení je `baseball` seznam seznamů. Hlavní seznam obsahuje 4 prvky. Každý z nich je seznam s výškou a váhou jednoho baseballového hráče, právě v tomto pořadí. Proměnná `baseball` je v kódu už připravená.

`@instructions`
- Pomocí `np.array()` vytvoř z `baseball` 2D pole `numpy`. Pojmenuj ho `np_baseball`.
- Vypiš typ proměnné `np_baseball`.
- Vypiš atribut `shape` proměnné `np_baseball` pomocí `np_baseball.shape`.

`@hint`
- `baseball` je už v kódu připraveno. Zavolej na něj `np.array()` a výsledné 2D pole `numpy` ulož do proměnné `np_baseball`.
- Pro druhý pokyn použij `print()` v kombinaci s `type()`.
- `np_baseball.shape` ti vrátí rozměry pole `np_baseball`. Nezapomeň výsledek obalit voláním `print()`.

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
msg = "Předefinované proměnné nemusíte měnit ani odstraňovat."
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

success_msg("Skvělé! Nyní jste připraveni převést skutečná data MLB do 2D pole `numpy`!")
```

---

## Baseballová data ve 2D podobě

```yaml
type: NormalExercise
key: 5df25d0b7b
lang: python
xp: 100
skills:
  - 2
```

Uvědomíš si, že by dávalo větší smysl uspořádat všechny tyto informace do 2D pole `numpy`.

Máš k dispozici Pythonový seznam seznamů. V tomto seznamu každý podseznam představuje výšku a váhu jednoho baseballového hráče. Tento seznam se jmenuje `baseball` a byl za tebe již načten (i když ho nevidíš).

Ulož data jako 2D pole a odemkni tím rozšířené funkce `numpy`.

`@instructions`
- Pomocí `np.array()` vytvoř 2D pole `numpy` z proměnné `baseball`. Pojmenuj ho `np_baseball`.
- Vypiš atribut `shape` pole `np_baseball`.

`@hint`
- `baseball` je už dostupný v prostředí Pythonu. Zavolej na něj `np.array()` a výsledné 2D pole `numpy` ulož do proměnné `np_baseball`.
- `np_baseball.shape` vrátí rozměry pole `np_baseball`. Nezapomeň to celé obalit voláním `print()`.

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

success_msg("Skvělé! Čas předvést některé skvělé funkce vícerozměrných polí `numpy`!")
```

---

## Podsetting 2D NumPy polí

```yaml
type: NormalExercise
key: aeca4977f0
lang: python
xp: 100
skills:
  - 2
```

Pokud má tvoje 2D pole `numpy` pravidelnou strukturu – tedy každý řádek a sloupec má pevně daný počet hodnot – stane se složitější podsetting velmi jednoduchým. Podívej se na kód níže, kde jsou ze seznamu seznamů extrahovány prvky `"a"` a `"c"`.

```
# numpy
import numpy as np
np_x = np.array(x)
np_x[:, 0]
```

Indexy před čárkou odkazují na řádky, indexy za čárkou odkazují na sloupce. Znak `:` slouží k řezání (slicing); v tomto příkladu říká Pythonu, aby zahrnul všechny řádky.

`@instructions`
- Vypiš 50. řádek pole `np_baseball`.
- Vytvoř novou proměnnou `np_weight_lb`, která bude obsahovat celý druhý sloupec pole `np_baseball`.
- Vyber výšku (první sloupec) 124. baseballového hráče v poli `np_baseball` a vypiš ji.

`@hint`
- V prvním úkolu potřebuješ řádkový index 49 – konkrétně použij `[49, :]`.
- Pro výběr celého druhého sloupce použij `[:, 1]`.
- V posledním úkolu použij `[123, 0]` a nezapomeň vše obalit do příkazu `print()`.

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
msg = "Předefinované proměnné není třeba měnit ani odstraňovat."
Ex().multi(
    has_import("numpy", same_as = False),
    check_object("np_baseball", missing_msg=msg).has_equal_value(incorrect_msg = msg)
)

Ex().has_printout(0)

Ex().check_object('np_weight_lb').has_equal_value(incorrect_msg = "Pomocí `np_baseball[:,1]` můžete definovat `np_weight_lb`. Tím vyberete celý první sloupec.")

Ex().has_printout(1)

success_msg("Jde to dobře!")
```

---

## 2D aritmetika

```yaml
type: NormalExercise
key: 1c2378b677
lang: python
xp: 100
skills:
  - 2
```

2D `numpy` pole umí provádět výpočty po prvcích, stejně jako běžná `numpy` pole.

`np_baseball` je pro tebe připraveno – jde opět o 2D `numpy` pole se 3 sloupci, které reprezentují výšku (v palcích), váhu (v librách) a věk (v letech). `baseball` je k dispozici jako běžný seznam seznamů a `updated` jako 2D numpy pole.

`@instructions`
- Podařilo se ti získat údaje o změnách výšky, váhy a věku všech baseballových hráčů. Jsou dostupné jako 2D `numpy` pole `updated`. Sečti `np_baseball` a `updated` a výsledek vypiš.
- Chceš převést jednotky výšky a váhy na metrické (metry a kilogramy). Jako první krok vytvoř `numpy` pole se třemi hodnotami: `0.0254`, `0.453592` a `1`. Pojmenuj toto pole `conversion`.
- Vynásob `np_baseball` polem `conversion` a výsledek vypiš.

`@hint`
- `np_baseball + updated` provede sčítání dvou `numpy` polí po prvcích.
- Vytvoř `numpy` pole pomocí `np.array()`; jako vstup použij běžný pythonový seznam se třemi prvky.
- `np_baseball * conversion` bude fungovat bez dalších úprav. Vyzkoušej to! Nezapomeň výsledek zabalit do volání `print()`.

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

msg = "Nemusíte měnit ani odstraňovat předdefinované proměnné."
Ex().check_object("np_baseball", missing_msg=msg).has_equal_value(incorrect_msg = msg)

Ex().has_printout(0)

Ex().check_correct(
    has_printout(1),
    check_correct(
        check_object('conversion').has_equal_value(),
        check_function('numpy.array', index = 1).check_args(0).has_equal_value()
    )    
)

success_msg("Skvělá práce! Všimněte si, jak pomocí velmi malého množství kódu můžete změnit všechny hodnoty ve své datové struktuře `numpy` velmi specifickým způsobem. To se vám v budoucnu jako datovému vědci velmi hodí!")
```

---

## NumPy: Základní statistika

```yaml
type: VideoExercise
key: 287995e488
xp: 50
```

`@projector_key`
34495ba457d74296794d2a122c9b6e19

---

## Průměr versus medián

```yaml
type: NormalExercise
key: 509c588eb6
lang: python
xp: 100
skills:
  - 2
```

Teď už víš, jak používat funkce `numpy` k lepšímu pochopení svých dat.

Baseballová data jsou dostupná jako 2D `numpy` pole se 3 sloupci (výška, váha, věk) a 1015 řádky. Toto `numpy` pole se jmenuje `np_baseball`. Po restrukturalizaci dat si ale všimneš, že některé hodnoty výšky jsou nezvykle vysoké. Postupuj podle instrukcí a zjisti, která souhrnná statistika je nejvhodnější při práci s takzvanými _odlehlými hodnotami_. Pole `np_baseball` je k dispozici.

`@instructions`
- Vytvoř `numpy` pole `np_height_in` odpovídající prvnímu sloupci pole `np_baseball`.
- Vypiš průměr pole `np_height_in`.
- Vypiš medián pole `np_height_in`.

`@hint`
- Použij 2D `numpy` subsetting: `[:,0]` je součástí řešení.
- Pokud je `numpy` importováno jako `np`, můžeš použít `np.mean()` pro výpočet průměru NumPy pole. Nezapomeň přidat volání `print()`.
- Pro poslední instrukci použij `np.median()`.

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

Ex().check_object("np_height_in").has_equal_value(incorrect_msg = "Můžete použít `np_baseball[:,0]` pro výběr prvního sloupce z `np_baseball`"),

Ex().check_correct(
    has_printout(0),
    check_function('numpy.mean').has_equal_value()
)

Ex().check_correct(
    has_printout(1),
    check_function('numpy.median').has_equal_value()
)

success_msg("Průměrná výška 1586 palců nezní správně, že? Medián však zdá se není ovlivněn odlehlými hodnotami: 74 palců dává dokonalý smysl. Vždy je dobré zkontrolovat jak medián, tak průměr, abyste získali představu o celkovém rozložení celého souboru dat.")
```

---

## Prozkoumej baseballová data

```yaml
type: NormalExercise
key: '4409948807'
lang: python
xp: 100
skills:
  - 2
```

Protože jsou průměr a medián tak vzdálené, rozhodneš se to nahlásit MLB. Chybu najdou a pošlou ti opravená data. Opět jsou k dispozici jako 2D NumPy pole `np_baseball` se třemi sloupci.

Skript v editoru už obsahuje kód pro výpis informativních zpráv s různými souhrnými statistikami a `numpy` je načtené jako `np`. Dokážeš úkol dokončit? Pole `np_baseball` je k dispozici.

`@instructions`
- Kód pro výpis průměrné výšky už je připravený. Doplň kód pro výpočet mediánu výšky.
- Pomocí `np.std()` na prvním sloupci pole `np_baseball` vypočítej `stddev`.
- Jsou větší hráči zároveň těžší? Pomocí `np.corrcoef()` ulož korelaci mezi prvním a druhým sloupcem pole `np_baseball` do proměnné `corr`.

`@hint`
- Medián vypočítáš pomocí `np.median()`. Nezapomeň nejdřív vybrat správný sloupec!
- Při výpočtu směrodatné odchylky s `np.std()` použij stejný sloupec.
- Pro výběr prvního a druhého sloupce použij `np_baseball[:, 0]` a `np_baseball[:, 1]` — to jsou vstupy pro `np.corrcoef()`.

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
msg = "Neměli byste měnit ani odstraňovat předdefinovanou proměnnou `avg`."
Ex().check_object("avg", missing_msg=msg).has_equal_value(incorrect_msg=msg)

missing = "Použili jste `np.median()` pro výpočet mediánu?"
incorrect = "Pro výpočet `med` předejte první sloupec `np_baseball` funkci `numpy.median()`. Příklad s `np.mean()` ukazuje, jak to provést."
Ex().check_correct(
  check_object("med").has_equal_value(),
  check_function("numpy.median", index=0, missing_msg=missing).check_args(0).has_equal_value(incorrect_msg=incorrect)
)

missing = "Použili jste `np.std()` pro výpočet směrodatné odchylky?"
incorrect = "Pro výpočet `stddev` předejte první sloupec `np_baseball` funkci `numpy.std()`. Příklad s `np.mean()` ukazuje, jak to provést."
Ex().check_correct(
  check_object("stddev").has_equal_value(),
  check_function("numpy.std", index=0, missing_msg=missing).check_args(0).has_equal_value(incorrect_msg=incorrect)
)

missing = "Použili jste `np.corrcoef()` pro výpočet korelace?"
incorrect1 = "Pro výpočet `corr` by měl být první argument funkce `np.corrcoef()` prvním sloupcem `np_baseball`, podobně jako jste to udělali dříve."
incorrect2 = "Pro výpočet `corr` by měl být druhý argument funkce `np.corrcoef()` druhým sloupcem `np_baseball`. Místo `[:,0]` použijte tentokrát `[:,1]`."
Ex().check_correct(
  check_object("corr").has_equal_value(),
  check_function("numpy.corrcoef", index=0, missing_msg=missing).multi(
    check_args(0, missing_msg=incorrect1).has_equal_value(incorrect_msg=incorrect1),
    check_args(1, missing_msg=incorrect2).has_equal_value(incorrect_msg=incorrect2)
  )
)

success_msg("Výborná práce! Vybudovali jste si pevný základ – nyní je čas využít všechny své nové dovednosti v oblasti datové vědy k řešení dalších výzev a dosažení výsledků.")
```

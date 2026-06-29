---
title_meta: Kapitola 3
title: Funkce a balíčky
description: >-
  Zjistíš, jak využívat funkce, metody a balíčky, abys mohl/a těžit z kódu,
  který napsali skvělí vývojáři Pythonu. Cílem je psát méně kódu a přitom řešit
  i náročné problémy!
attachments:
  slides_link: 'https://projector-video-pdf-converter.datacamp.com/735/chapter3.pdf'
lessons:
  - nb_of_exercises: 4
    title: Funkce
  - nb_of_exercises: 4
    title: Metody
  - nb_of_exercises: 4
    title: Balíčky
---

## Funkce

```yaml
type: VideoExercise
key: 5c5f365930
xp: 50
```

`@projector_key`
1204d914b0e53100529827e07441ee6c

---

## Známé funkce

```yaml
type: NormalExercise
key: c422ee929b
lang: python
xp: 100
skills:
  - 2
```

Python hned po instalaci nabízí řadu vestavěných funkcí, které ti jako datovému analytikovi usnadní práci. Dvě z nich už znáš: `print()` a `type()`. K dispozici jsou také funkce jako `str()`, `int()`, `bool()` nebo `float()` pro převod mezi datovými typy. Víc se o nich dozvíš [zde.](https://docs.python.org/3/library/functions.html) Jsou to také vestavěné funkce.

Volání funkce je jednoduché. Pokud chceš zjistit typ hodnoty `3.0` a výsledek uložit do nové proměnné `result`, použij následující kód:

```
result = type(3.0)
```

`@instructions`
- Pomocí `print()` a `type()` vypiš typ proměnné `var1`.
- Pomocí `len()` zjisti [délku seznamu](https://docs.python.org/3/library/functions.html#len) `var1`. Výsledek obal voláním `print()`, aby se rovnou vypsal.
- Pomocí `int()` převeď `var2` na [celé číslo](https://docs.python.org/3/library/functions.html#int). Výsledek ulož do proměnné `out2`.

`@hint`
- Funkci `type()` zavoláš takto: `type(var1)`.
- Funkci `print()` zavoláš stejně jako předtím – jednoduše vlož proměnnou, kterou chceš vypsat, do závorek.
- `int(x)` převede `x` na celé číslo.

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
msg = "Předefinované proměnné není třeba měnit ani odstraňovat."
Ex().check_object("var1", missing_msg=msg).has_equal_value(incorrect_msg=msg)
Ex().check_object("var2", missing_msg=msg).has_equal_value(incorrect_msg=msg)

patt = "__JINJA__:Ujistěte se, že jste vytiskli %s proměnné `var1` pomocí `{{sol_call}}`."
Ex().has_printout(0, not_printed_msg = patt % 'type')
Ex().has_printout(1, not_printed_msg = patt % 'length')

int_miss_msg = "Použili jste `int()` pro převod `var2` na celé číslo?"
int_incorr_msg = "Předali jste `var2` funkci `int()`?"
Ex().check_correct(
  check_object("out2").has_equal_value(incorrect_msg="Funkci `int()` jste zavolali správně; nyní se ujistěte, že výsledek tohoto volání přiřadíte do `out2`."),
  check_function("int", missing_msg=int_miss_msg).has_equal_value(incorrect_msg=int_incorr_msg)
)
success_msg("Výborně! Funkce `len()` je nesmírně užitečná; funguje také na řetězcích pro počítání počtu znaků!")
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

Možná už název pythonové funkce znáš, ale pořád ti zbývá přijít na to, jak ji použít. Informace o funkci paradoxně získáš pomocí jiné funkce: `help()`. V IPythonu můžeš navíc použít `?` před názvem funkce.

Pro zobrazení nápovědy k funkci `max()` například poslouží jeden z těchto příkazů:

```
help(max)
?max
```

Použij IPython Shell k otevření [dokumentace](https://docs.python.org/3/library/functions.html#pow) k funkci `pow()`. Zadej `?pow` nebo `help(pow)` a stiskni **Enter**.

Které z následujících tvrzení je pravdivé?

`@possible_answers`
- `pow()` přijímá tři argumenty: `base`, `exp` a `mod`. Bez `mod` funkce vrátí chybu.
- `pow()` přijímá tři povinné argumenty: `base`, `exp` a `None`.
- `pow()` vyžaduje argumenty `base` a `exp`; argument `mod` je volitelný.
- `pow()` přijímá dva argumenty: `exp` a `mod`. Chybějící `exp` způsobí chybu.

`@hint`
- Volitelné argumenty mají přiřazenou výchozí hodnotu pomocí `=`, kterou funkce použije, pokud daný argument nezadáš.

`@pre_exercise_code`
```{python}

```

`@sct`
```{python}
msg1 = "Není správně. `mod` má výchozí hodnotu, která bude použita, pokud hodnotu nezadáte."
msg2 = "Nesprávně. `None` je výchozí hodnota pro argument `mod`."
msg3 = "Výborně! Použití `help()` vám může pomoci pochopit, jak funkce fungují, a plně využít jejich potenciál!"
msg4 = "Nesprávně. `pow()` přijímá tři argumenty, z nichž jeden má výchozí hodnotu."
Ex().has_chosen(3, [msg1, msg2, msg3, msg4])
```

---

## Více argumentů

```yaml
type: NormalExercise
key: e30486d7c1
lang: python
xp: 100
skills:
  - 2
```

V předchozím cvičení jsi identifikoval/a volitelné argumenty pomocí dokumentace zobrazené přes `help()`. Teď tohle využiješ ke změně chování funkce `sorted()`.

Prohlédni si [dokumentaci](https://docs.python.org/3/library/functions.html#sorted) funkce `sorted()` tak, že do IPython Shellu zadáš `help(sorted)`.

Uvidíš, že `sorted()` přijímá tři argumenty: `iterable`, `key` a `reverse`. V tomto cvičení budeš muset zadat pouze `iterable` a `reverse`, nikoli `key`.

Dva seznamy už jsou pro tebe připravené.

Dokážeš je spojit dohromady a seřadit sestupně?

`@instructions`
- Pomocí `+` spoj obsah `first` a `second` do nového seznamu: `full`.
- Zavolej `sorted()` na `full` a nastav argument `reverse` na `True`. Seřazený seznam ulož jako `full_sorted`.
- Na závěr vypiš `full_sorted`.

`@hint`
- Sečti `first` a `second` jako dvě čísla a výsledek přiřaď do proměnné `full`.
- Použij `sorted()` se dvěma vstupy: `full` a `reverse=True`.
- Pro výpis proměnné použij `print()`.

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
msg = "Nemusíte měnit ani odstraňovat již existující proměnné `first` a `second`."
Ex().multi(
  check_object("first", missing_msg=msg).has_equal_value(incorrect_msg=msg),
  check_object("second", missing_msg=msg).has_equal_value(incorrect_msg=msg)
)
Ex().check_correct(
  check_object("full_sorted").has_equal_value(incorrect_msg="Ujistěte se, že výsledek volání `sorted()` přiřadíte do proměnné `full_sorted`."),
  check_function("sorted").multi(
    check_args(0).has_equal_value(),
    check_args('reverse').has_equal_value()
  )
)

success_msg("Skvěle! Přejděte na video o metodách v Pythonu.")
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

## Řetězcové metody

```yaml
type: NormalExercise
key: 4039302ee0
lang: python
xp: 100
skills:
  - 2
```

Řetězce mají k dispozici celou řadu metod. Pečlivě se řiď pokyny níže a objevíš některé z nich. Pokud je chceš prozkoumat podrobněji, stačí zadat `help(str)` v IPython Shellu.

Proměnná `place` je pro tebe už připravená – můžeš si na ní vše vyzkoušet.

`@instructions`
- Použij metodu `.upper()` na proměnné `place` a výsledek ulož do `place_up`. Využij syntaxi pro volání metod, kterou jsi viděl/a v předchozím videu.
- Vypiš proměnné `place` i `place_up`. Změnily se obě?
- Vypiš počet výskytů písmene `'o'` v proměnné `place` – zavolej na ní metodu `.count()` a předej jí písmeno `'o'` jako vstup. Pracujeme s proměnnou `place`, ne se slovem `"place"`!

`@hint`
- Metodu `.upper()` můžeš zavolat na proměnné `place` bez jakýchkoli dalších vstupů.
- Pro výpis proměnné `x` napiš `print(x)`.
- Nezapomeň obalit volání `place.count(____)` funkcí `print()`, aby se výsledek vypsal.

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
msg = "Předefinované proměnné není třeba měnit ani odstraňovat."
Ex().check_object("place", missing_msg=msg).has_equal_value(incorrect_msg=msg)

patt = "Nezapomeňte vypsat `%s`."
Ex().has_printout(0, not_printed_msg=patt % "place")
Ex().check_correct(
    has_printout(1, not_printed_msg=patt % "place_up"),
    check_correct(
        check_object("place_up").has_equal_value(incorrect_msg="Přiřaďte výsledek volání `place.upper()` do proměnné `place_up`."),
        check_function("place.upper", signature=False)
    )
)    

# check count of place
Ex().check_correct(
  has_printout(2, not_printed_msg = "Počet výskytů písmene 'o' v proměnné `place` jste vypočítali správně; nezapomeňte volání `place.count('o')` obalit funkcí `print()`, aby byl výsledek vypsán."),
  check_function("place.count", signature=False).check_args(0).has_equal_value()
)

success_msg("Výborně! Všimněte si z výpisů, že metoda `upper()` nemění objekt, na kterém je volána. U seznamů v následujícím cvičení to bude jinak!")
```

---

## Metody seznamů

```yaml
type: NormalExercise
key: 0dbe8ed695
lang: python
xp: 100
skills:
  - 2
```

Metody nejsou výsadou jen řetězců. Mají je i seznamy, čísla s desetinnou čárkou, celá čísla a booleany – každý z těchto typů přichází s užitečnou sadou metod. V tomto cvičení si vyzkoušíš:

- `.index()` – pro získání indexu prvního prvku seznamu, který odpovídá zadané hodnotě, a
- `.count()` – pro zjištění, kolikrát se daný prvek v seznamu vyskytuje.

Budeš pracovat se seznamem `areas`, který obsahuje plochy různých částí domu.

`@instructions`
- Pomocí metody `.index()` zjisti index prvku v `areas`, který se rovná `20.0`. Tento index vypiš.
- Zavolej `.count()` na `areas` a zjisti, kolikrát se v seznamu vyskytuje hodnota `9.50`. Výsledek jednoduše vypiš.

`@hint`
- Pro výpis indexu obal volání `areas.index(___)` funkcí `print()`.
- Pro výpis počtu výskytů prvku `x` v seznamu obal volání `areas.count(___)` funkcí `print()`.

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
predef_msg = "Nemusíte měnit ani odstraňovat předdefinovaný seznam `areas`."

Ex().check_object("areas", missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg)

Ex().check_function("print", index=0).check_args(0).check_function('areas.index', signature=False).check_args(0).has_equal_value()


Ex().check_function("print", index=1).check_args(0).check_function('areas.count', signature=False).has_equal_value()

success_msg("Výborně! Toto byly příklady metod `list`, které nezměnily seznam, na kterém byly volány.")
```

---

## Metody seznamů (2)

```yaml
type: NormalExercise
key: 1fbeab82d0
lang: python
xp: 100
skills:
  - 2
```

Většina metod seznamů upraví seznam, na kterém jsou volány. Příklady:

- `.append()` přidá prvek na konec seznamu,
- `.remove()` [odstraní](https://docs.python.org/3/library/stdtypes.html#typesseq-mutable) první prvek seznamu, který odpovídá zadané hodnotě,
- `.reverse()` [obrátí](https://docs.python.org/3/library/stdtypes.html#typesseq-mutable) pořadí prvků v seznamu.

Budeš pracovat se seznamem `areas`, který obsahuje plochy různých částí domu.

`@instructions`
- Pomocí `.append()` přidej dvakrát velikost bazénového domku a garáže: `24.5` a `15.45`. Přidej je v tomto pořadí.
- Vypiš seznam `areas`.
- Pomocí metody `.reverse()` obrať pořadí prvků v seznamu `areas`.
- Vypiš seznam `areas` ještě jednou.

`@hint`
- Pro první instrukci použij volání `areas.append(___)` dvakrát.
- Pro výpis proměnné `x` jednoduše napiš `print(x)`.
- Metoda `.reverse()` nevyžaduje žádné vstupní hodnoty – stačí použít tečkovou notaci a prázdné závorky: `.reverse()`.
- Pro výpis proměnné `x` jednoduše napiš `print(x)`.

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

success_msg("Výborně!")
```

---

## Balíčky

```yaml
type: VideoExercise
key: ab96a17c5e
xp: 50
```

`@projector_key`
cedcfb34350be8545599768f96695cdd

---

## Import balíčku

```yaml
type: NormalExercise
key: 7432a6376f
lang: python
xp: 100
skills:
  - 2
```

Řekněme, že chceš vypočítat obvod a obsah kruhu. Příslušné vzorce vypadají takto:

$$C = 2 \pi r$$
$$A = \pi r^2 $$

Místo ručního zadávání čísla pro `pi` můžeš využít balíček `math`, který tuto hodnotu obsahuje.

Pro připomenutí: `**` je operátor umocňování. Například `3**4` znamená `3` na `4`. mocninu a výsledek je `81`.

`@instructions`
- Importuj balíček `math`.
- Pomocí `math.pi` vypočítej obvod kruhu a výsledek ulož do proměnné `C`.
- Pomocí `math.pi` vypočítej obsah kruhu a výsledek ulož do proměnné `A`.

`@hint`
- Stačí použít `import math` a pak se na `pi` odkazovat jako `math.pi`.
- Pro výpočet `C` použij vzorec ze zadání a operátor `*`.
- Pro výpočet `A` použij vzorec ze zadání a operátory `*` a `**`.

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
patt = "Váš výpočet `%s` není zcela správný. Ujistěte se, že používáte `math.pi`."
Ex().multi(
  has_import('math', same_as=False),
  check_object('C').has_equal_value(incorrect_msg=patt%'C'),
  check_object('A').has_equal_value(incorrect_msg=patt%'A')
)

Ex().multi(
  has_printout(0, not_printed_msg = "__JINJA__:Ponechte `{{sol_call}}` pro výpis obvodu."),
  has_printout(1, not_printed_msg = "__JINJA__:Ponechte `{{sol_call}}` pro výpis obsahu.")
)

success_msg("Výborně! Pokud víte, jak pracovat s funkcemi z balíčků, máte k dispozici sílu mnoha Python programátorů!")
```

---

## Selektivní import

```yaml
type: NormalExercise
key: fe65eff50a
lang: python
xp: 100
skills:
  - 2
```

Obecné importy, jako `import math`, ti zpřístupní **veškerou** funkcionalitu z balíčku `math`. Pokud ale potřebuješ jen určitou část balíčku, můžeš import zúžit:

```
from math import pi
```

Vyzkoušej to samé, ale tentokrát použij pouze `pi`.

`@instructions`
- Proveď selektivní import z balíčku `math` tak, aby ses importoval/a pouze funkci `pi`.
- Pomocí `pi` vypočítej obvod kružnice a výsledek ulož do `C`.
- Pomocí `pi` vypočítej obsah kruhu a výsledek ulož do `A`.

`@hint`
- Použij `from math import pi` pro selektivní import.
- Teď můžeš používat `pi` samostatně!

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
patt = "Váš výpočet `%s` není zcela správný. Ujistěte se, že používáte pouze `pi`."

Ex().has_import("math.pi", not_imported_msg = "Nezapomeňte importovat `pi` z balíčku `math`. Měli byste použít notaci `from ___ import ___`.",)

Ex().multi(
  check_object('C').has_equal_value(incorrect_msg=patt%'C'),
  check_object('A').has_equal_value(incorrect_msg=patt%'A')
)

Ex().multi(
  has_printout(0, not_printed_msg = "__JINJA__:Ponechte `{{sol_call}}` pro výpis obvodu."),
  has_printout(1, not_printed_msg = "__JINJA__:Ponechte `{{sol_call}}` pro výpis obsahu.")
)

success_msg("Výborně! Přejděte k dalšímu cvičení.")
```

---

## Různé způsoby importu

```yaml
type: MultipleChoiceExercise
key: f1b2675a2a
lang: python
xp: 50
skills:
  - 2
```

Do Pythonu lze balíčky a moduly importovat několika způsoby. Podle toho, jaký příkaz pro import použiješ, se bude lišit i způsob, jakým pak funkci voláš.

Představme si, že chceš použít [funkci](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.inv.html) `inv()` z podbalíčku `linalg` balíčku `scipy`. Chceš ji volat takto:

```
my_inv([[1,2], [3,4]])
```

Který příkaz `import` ti umožní spustit tento kód bez chyby?

`@possible_answers`
- `import scipy`
- `import scipy.linalg`
- `from scipy.linalg import my_inv`
- `from scipy.linalg import inv as my_inv`

`@hint`
- Vyzkoušej různé způsoby importu v IPython shellu a zjisti, který z nich umožní spustit řádek `my_inv([[1, 2], [3, 4]])` bez chyby. Stiskni **enter** pro spuštění zadaného kódu.

`@pre_exercise_code`
```{python}

```

`@sct`
```{python}
msg1 = msg2 = msg3 = "Nesprávně, zkuste to znovu. Vyzkoušejte různé příkazy importu v prostředí IPython a zjistěte, který z nich umožní spustit řádek `my_inv([[1, 2], [3, 4]])` bez chyb."
msg4 = "Správně! Klíčové slovo `as` umožňuje vytvořit lokální název pro importovanou funkci: `inv()` je nyní dostupná jako `my_inv()`."
Ex().has_chosen(4, [msg1, msg2, msg3, msg4])

```

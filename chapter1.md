---
title_meta: Kapitola 1
title: Základy Pythonu
description: >-
  Úvod do základních konceptů Pythonu. Naučíš se pracovat s Pythonem
  interaktivně i pomocí skriptů, vytvoříš své první proměnné a seznámíš se se
  základními datovými typy.
attachments:
  slides_link: 'https://projector-video-pdf-converter.datacamp.com/735/chapter1.pdf'
free_preview: true
lessons:
  - nb_of_exercises: 3
    title: 'Ahoj, Pythone!'
  - nb_of_exercises: 5
    title: Proměnné a typy
---

## Ahoj, Pythone!

```yaml
type: VideoExercise
key: f644a48d5d
xp: 50
```

`@projector_key`
d8fcd4c930027fa4e1c3870c7e7e0ff1

---

## Tvůj první kód v Pythonu

```yaml
type: NormalExercise
key: bdc52f0e19
lang: python
xp: 100
skills:
  - 2
```

Je čas spustit svůj první kód v Pythonu!

Přejdi do editoru a klikni na tlačítko pro spuštění kódu, abys viděl/a výstup.

`@instructions`
- Klikni na tlačítko pro spuštění kódu a podívej se na výstup `print(5 / 8)`.

`@hint`
- Nejdřív spusť kód a teprve pak odešli odpověď – budeš mít čas prozkoumat výstup.

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
Ex().has_printout(0, not_printed_msg = "__JINJA__:Použili jste `{{sol_call}}` pro výpis `5 / 8`?")
success_msg("Skvělé! Pojďme na další!")
```

---

## Python jako kalkulačka

```yaml
type: NormalExercise
key: 0f7c039428
lang: python
xp: 100
skills:
  - 2
```

Python se skvěle hodí na základní výpočty. Zvládne sčítání, odčítání, násobení i dělení.

Ukázky najdeš přímo ve skriptu.

Teď je řada na tobě – zkus si napsat vlastní kód.

`@instructions`
- Pod `# Subtraction` vypiš pomocí `print()` výsledek odečtení `5` od `5`.
- Pod `# Multiplication` vypiš výsledek násobení `3` číslem `5`.

`@hint`
- Pro zobrazení výstupu použij `print()`.
- Odečítání se zapisuje pomocí `-` a násobení pomocí `*`.

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
Ex().has_printout(0, not_printed_msg = "Použili jste `print(4 + 5)` pro výpis výsledku součtu?")

Ex().has_printout(1, not_printed_msg = "Použili jste `print(5 - 5)` pro výpis výsledku odčítání?")

Ex().has_printout(2, not_printed_msg = "Použili jste `print(3 * 5)` pro výpis výsledku násobení?")

Ex().has_printout(3, not_printed_msg = "Použili jste `print(10 / 2)` pro výpis výsledku dělení?")

success_msg("Správně! Python vám může pomoci s výpočty, což je vlastnost, která bude užitečná pro analýzu dat, jak budeme rozvíjet naše dovednosti.")
```

---

## Proměnné a datové typy

```yaml
type: VideoExercise
key: c2e396792e
xp: 50
```

`@projector_key`
433dcfcfedaee070cbf440491c402e3b

---

## Přiřazení proměnné

```yaml
type: NormalExercise
key: 4bf65ad83e
lang: python
xp: 100
skills:
  - 2
```

V Pythonu ti proměnná umožňuje odkazovat se na hodnotu pomocí názvu. Proměnnou `x` s hodnotou `5` vytvoříš pomocí `=`, jak ukazuje tento příklad:

```
x = 5
```

Místo skutečné hodnoty `5` teď můžeš používat název proměnné `x`.

Pamatuj, že `=` v Pythonu znamená _přiřazení_ – netestuje rovnost! Vyzkoušej si to v cvičení nahrazením `____` svým kódem.

`@instructions`
- Vytvoř proměnnou `savings` s hodnotou `100`.
- Zobraz její hodnotu zadáním `print(savings)` do skriptu.

`@hint`
- Zadej `savings = 100` pro vytvoření proměnné `savings`.
- Po vytvoření proměnné `savings` můžeš zadat `print(savings)`.
- Výsledný kód by neměl obsahovat žádné `____`.

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
Ex().check_object("savings").has_equal_value(incorrect_msg="Přiřaďte `100` proměnné `savings`.")
Ex().has_printout(0, not_printed_msg = "Vypište `savings`, proměnnou, kterou jste vytvořili, pomocí `print(savings)`.")
success_msg("Skvělé! Zkusme nyní provést některé výpočty s touto proměnnou!")
```

---

## Výpočty s proměnnými

```yaml
type: NormalExercise
key: ff06cedeb4
lang: python
xp: 100
skills:
  - 2
```

Teď, když máš vytvořenou proměnnou pro úspory, se pustíme do spoření!

Místo konkrétních čísel můžeš ve výpočtech používat proměnné.

Kolik peněz budeš mít naspořeno za čtyři měsíce, pokud budeš každý měsíc odkládat 10 $?

`@instructions`
- Vytvoř proměnnou `monthly_savings` s hodnotou `10` a proměnnou `num_months` s hodnotou `4`.
- Vynásob `monthly_savings` hodnotou `num_months` a výsledek ulož do `new_savings`.
- Vypiš hodnotu proměnné `new_savings`.

`@hint`
- S proměnnými můžeš počítat úplně stejně jako s čísly – takže místo `10 * 4` jednoduše dosaď příslušné proměnné!
- Pomocí `print()` zobraz hodnotu uloženou v `new_savings`.
- Dávej pozor na správný pravopis názvů proměnných!

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
Ex().check_object("monthly_savings").has_equal_value(incorrect_msg = "Uložili jste hodnotu `10` do proměnné `monthly_savings` pomocí `monthly_savings = 10`?")
Ex().check_object("num_months").has_equal_value(incorrect_msg = "Uložili jste hodnotu `4` do proměnné `num_months` pomocí `num_months = 4`?")
Ex().check_object("new_savings").has_equal_value(incorrect_msg = "Použili jste správné proměnné a symboly pro násobení? Očekáváno `monthly_savings * num_months`, ale byl zadán jiný výraz.")
# Ex().check_object("total_savings").has_equal_value(incorrect_msg = "Použili jste správné proměnné a symboly pro sčítání? Očekáváno `savings + new_savings`, ale byl zadán jiný výraz.")

Ex().has_printout(0, not_printed_msg="Nezapomeňte na konci skriptu vypsat hodnotu `new_savings`.")

success_msg("Máte 40 $ v nových úsporách!")
```

---

## Další typy proměnných

```yaml
type: NormalExercise
key: 006b48561f
lang: python
xp: 100
skills:
  - 2
```

V předchozím cvičení jsi pracoval/a s datovým typem integer:

- `int`, neboli celé číslo: číslo bez desetinné části. Příkladem je proměnná `savings` s hodnotou `100`.

Kromě číselných datových typů existují tři další velmi běžné typy:

- `float`, neboli číslo s plovoucí desetinnou čárkou: číslo, které má celou i desetinnou část oddělené tečkou. Příkladem je `1.1`.
- `str`, neboli řetězec: typ pro reprezentaci textu. Řetězec můžeš uzavřít do jednoduchých nebo dvojitých uvozovek.
- `bool`, neboli boolean: typ pro reprezentaci logických hodnot. Může nabývat pouze hodnot `True` nebo `False` (velikost písmen je důležitá!).

`@instructions`
- Vytvoř novou proměnnou typu float, `half`, s hodnotou `0.5`.
- Vytvoř novou proměnnou typu string, `intro`, s hodnotou `"Hello! How are you?"`.
- Vytvoř novou proměnnou typu boolean, `is_good`, s hodnotou `True`.

`@hint`
- Proměnnou v Pythonu vytvoříš pomocí `=`. Řetězec nezapomeň uzavřít do jednoduchých nebo dvojitých uvozovek.
- V Pythonu existují pouze dvě hodnoty typu boolean: `True` a `False`. Varianty jako `TRUE`, `true`, `FALSE`, `false` a jiné nejsou platné.

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
Ex().check_object("half").has_equal_value(incorrect_msg = "Uložili jste číslo s plovoucí desetinnou čárkou `0.5` do proměnné `half`?")

Ex().check_object("intro").has_equal_value(incorrect_msg = "Hmm, něco je ve vaší proměnné `intro` nesprávně. Zkontrolujte prosím pravopis a ujistěte se, že jste použili uvozovky.")

Ex().check_object("is_good").has_equal_value(incorrect_msg = "Použili jste velké písmeno u logické hodnoty? Nezapomeňte, že zde není třeba používat uvozovky.")

success_msg("Výborně!")
```

---

## Operace s různými typy

```yaml
type: BulletExercise
key: 4d0d83cc02
xp: 100
```

V Pythonu existují proměnné různých typů. Typ proměnné zjistíš pomocí funkce `type()`. Například pro zjištění typu proměnné `a` spusť: `type(a)`.

Různé typy se v Pythonu chovají různě. Když sečteš dva řetězce, dostaneš jiný výsledek, než když sečteš dvě celá čísla nebo dvě booleovské hodnoty.

Čas si to vyzkoušet na vlastní kůži.

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
- Sečti `savings` a `new_savings` a výsledek přiřaď do `total_savings`.
- Pomocí `type()` vypiš výsledný typ proměnné `total_savings`.

`@hint`
- Přiřaď `savings + new_savings` do nové proměnné `total_savings`.
- Pro výpis typu proměnné `x` použij `print(type(x))`.

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
msg = "Předefinované proměnné není třeba měnit ani odstraňovat."

Ex().multi(
    check_object('savings', missing_msg=msg).has_equal_value(incorrect_msg=msg),
    check_object('new_savings', missing_msg=msg).has_equal_value(incorrect_msg=msg)
)

Ex().multi(
    check_object("total_savings").has_equal_value(incorrect_msg="Přičtěte `savings` a `new_savings` pro vytvoření proměnné `total_savings`."),
    has_printout(1, not_printed_msg = "__JINJA__:Použijte `{{sol_call}}` pro výpis typu `total_savings`.")
)
```

***

```yaml
type: NormalExercise
key: f54fbf9bd9
xp: 50
```

`@instructions`
- Vypočítej součet `intro` a `intro` a výsledek přiřaď do `doubleintro`.
- Vypiš `doubleintro`. Čekal/a jsi takový výsledek?

`@hint`
- Přiřaď `intro + intro` do nové proměnné `doubleintro`.
- Pro výpis proměnné `x` napiš do skriptu `print(x)`.

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
msg = "Předdefinované proměnné nemusíte měnit ani odstraňovat."

Ex().check_object('intro', missing_msg=msg).has_equal_value(incorrect_msg=msg)

Ex().multi(
    check_object("doubleintro").has_equal_value(incorrect_msg  = "Uložili jste výsledek `intro + intro` do proměnné `doubleintro`?"),
    has_printout(0, not_printed_msg = "Nezapomeňte vypsat `doubleintro`.")
)

success_msg("Výborně. Všimněte si, jak `intro + intro` způsobí, že se `\"Hello! How are you?\"` a `\"Hello! How are you?\"` spojí dohromady.")
```

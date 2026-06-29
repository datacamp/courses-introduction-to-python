---
title: Insert title here
key: 433dcfcfedaee070cbf440491c402e3b
video_link:
  mp3: >-
    https://videos.datacamp.com/mp3/translations/course_735/cs-CZ/08a54120-151a-435e-891c-dc3cb4953a3e-c886d53f2d9f733d02ebdb264ade8c9e.mp3
---

## Proměnné a typy

```yaml
type: TitleSlide
key: dc8b62f1c8
```

`@lower_third`
name: Hugo Bowne-Anderson
title: Data Scientist at DataCamp

`@script`
Výborně a vítej zpět! Je jasné, že Python je skvělá kalkulačka. Pokud ale chceš provádět složitější výpočty, budeš chtít hodnoty během psaní kódu „ukládat".

---

## Proměnná

```yaml
type: FullSlide
key: 36ec318b41
```

`@part1`
- Konkrétní název rozlišující velikost písmen

- Hodnotu získáme přes název proměnné{{1}}

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
Lze to udělat tak, že definuješ proměnnou s konkrétním názvem, přičemž záleží na velikosti písmen. Jakmile takovou proměnnou vytvoříš, můžeš její hodnotu kdykoli vyvolat zadáním jejího názvu.

Představ si, že měříš svou výšku a váhu v metrické soustavě: měříš 1,79 metru a vážíš 68,7 kilogramu. Tyto hodnoty přiřadíš dvěma proměnným — height a weight — pomocí znaku rovná se.

Pokud teď zadáš název proměnné height,

Python ji vyhledá, získá její hodnotu a vypíše ji.

---

## Výpočet BMI

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
Teď si vypočítáme index tělesné hmotnosti, nebo také B-M-I, který se počítá podle tohoto vzorce — váha je v kilogramech a výška v metrech. Výpočet lze provést přímo s číselnými hodnotami, ale stejně dobře poslouží proměnné height a weight, jak vidíš tady. Pokaždé, když zadáš název proměnné, říkáš Pythonu, aby ji nahradil její skutečnou hodnotou. weight odpovídá 68,7 a height 1,79.

V poslední verzi Python výsledek uloží do nové proměnné bmi. bmi teď obsahuje stejnou hodnotu, jakou jsi vypočítal dříve.

V Pythonu se proměnné používají neustále — pomáhají psát znovu použitelný kód.

---

## Reprodukovatelnost

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
Představ si, že kód pro vytvoření proměnných height, weight a bmi je uložený ve skriptu, jako je tento. Pokud teď chceš přepočítat bmi pro jinou váhu,

---

## Reprodukovatelnost

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
stačí jednoduše změnit deklaraci proměnné weight a skript znovu spustit. bmi se odpovídajícím způsobem změní, protože se změnila i hodnota proměnné weight.

Doposud jsme pracovali pouze s číselnými hodnotami, jako jsou výška a váha.

---

## Typy v Pythonu

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
V Pythonu mají všechna čísla konkrétní typ. Typ hodnoty zjistíš pomocí funkce type. Chceš-li zjistit typ naší hodnoty bmi, jednoduše napíšeš type a do závorek vložíš bmi. Uvidíš, že je to float — tak Python označuje reálné číslo, tedy číslo, které může mít celou i desetinnou část. Python má také typ pro celá čísla: int, jak ukazuje tento příklad.

Pro datovou vědu ale ints a floaty nestačí.

---

## Typy v Pythonu (2)

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
Python nabízí celou řadu dalších datových typů. Nejběžnější jsou string a boolean.

String je způsob, jakým Python pracuje s textem. K jeho vytvoření lze použít dvojité i jednoduché uvozovky, jak vidíš na těchto příkladech. Pokud vypíšeš typ poslední proměnné, uvidíš str — zkratka pro string.

Boolean je typ, který může nabývat hodnoty True nebo False — v běžném jazyce si ho představ jako „Ano" a „Ne". Booleany se ti budou velmi hodit, například při filtrování dat.

Datové typy v Pythonu mají ještě jednu zajímavou vlastnost.

---

## Typy v Pythonu (3)

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

- Různý typ = různé chování!{{3}}

`@script`
Podívej se na tento řádek kódu, který sečte dvě celá čísla, a pak na tento, který spojí dva stringy.

U celých čísel se hodnoty sečetly, zatímco u stringů se řetězce spojily za sebou. Operátor plus se choval jinak podle toho, s jakým datovým typem pracoval. To je obecný princip: chování kódu závisí na typech, se kterými pracuješ.

V následujících cvičeních si vytvoříš první proměnné a vyzkoušíš různé datové typy Pythonu. Ve videu tě pak provedu světem seznamů.

---

## Pojďme cvičit!

```yaml
type: FinalSlide
key: b7fc40db4d
```

`@script`
Pusť se do kódování a těším se na tebe v další kapitole, kde vytvoříš ještě působivější grafy v Pythonu.

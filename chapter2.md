---
title_meta: Kapitola 2
title: Seznamy v Pythonu
description: >-
  Naučíš se ukládat, přistupovat k datům a pracovat s nimi v seznamech – to je
  první krok k efektivní práci s velkými objemy dat.
attachments:
  slides_link: 'https://projector-video-pdf-converter.datacamp.com/735/chapter2.pdf'
lessons:
  - nb_of_exercises: 4
    title: Seznamy v Pythonu
  - nb_of_exercises: 4
    title: Výběr prvků ze seznamu
  - nb_of_exercises: 5
    title: Úpravy seznamů
---

## Seznamy v Pythonu

```yaml
type: VideoExercise
key: a5886d213f
xp: 50
```

`@projector_key`
a0530c4542f10988847b2dbb91f717c3

---

## Vytvoř seznam

```yaml
type: NormalExercise
key: e6c527bf41
lang: python
xp: 100
skills:
  - 2
```

Seznam je **složený datový typ** – umožňuje ti seskupit více hodnot dohromady, třeba takto:

```
a = "is"
b = "nice"
my_list = ["my", "list", a, b]
```

Po změření výšky členů své rodiny se rozhodneš shromáždit také informace o domě, ve kterém bydlíš. Rozlohy jednotlivých místností jsou uloženy v samostatných proměnných připravených v tomto cvičení.

`@instructions`
- Vytvoř seznam `areas`, který bude obsahovat rozlohu chodby (`hall`), kuchyně (`kit`), obývacího pokoje (`liv`), ložnice (`bed`) a koupelny (`bath`) – přesně v tomto pořadí. Použij připravené proměnné.
- Vypiš `areas` pomocí funkce `print()`.

`@hint`
- K sestavení seznamu můžeš použít proměnné, které už jsou vytvořené: `areas = [hall, kit, ...]`.
- Nezapomeň použít hranaté závorky `[]`, ne kulaté `()`.
- Při ukládání proměnných do seznamu nepotřebuješ uvozovky.
- Pro výpis seznamu napiš `print(areas)`.

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
predef_msg = "Neodstraňujte ani neupravujte předdefinované proměnné!"
areas_msg = "Definujte `areas` jako seznam obsahující všechny proměnné ploch ve správném pořadí: `[hall, kit, liv, bed, bath]`. Dávejte pozor na překlepy. Seznam by neměl obsahovat nic jiného!"

Ex().check_correct(
    has_printout(0, not_printed_msg = "__JINJA__:Použili jste `{{sol_call}}` pro výpis seznamu `areas` na konci skriptu?"),
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

success_msg("Výborně! Seznam je zde mnohem lepší volbou, že ano?")
```

---

## Vytváření seznamů s různými typy

```yaml
type: NormalExercise
key: 1702a8bcdc
lang: python
xp: 100
skills:
  - 2
```

Ačkoliv to není úplně běžné, seznam může obsahovat kombinaci různých typů Pythonu – například řetězce, desetinná čísla a booleany.

Teď do svého seznamu přidáš názvy místností, takže uvidíš název i rozlohu každé místnosti pohromadě.

Část kódu už je připravená, aby ti usnadnila začátek. Dej pozor! `"bathroom"` je řetězec, zatímco `bath` je proměnná reprezentující desetinné číslo `9.50`, které jsi zadal/a dříve.

`@instructions`
- Dokonči kód, který vytváří seznam `areas`. Sestav ho tak, aby nejprve obsahoval název každé místnosti jako řetězec a za ním její rozlohu. Jinými slovy, přidej řetězce `"hallway"`, `"kitchen"` a `"bedroom"` na příslušná místa.
- Vypiš `areas` znovu – je výstup tentokrát přehlednější?

`@hint`
- První čtyři prvky seznamu `areas` jsou zapsány jako `["hallway", hall, "kitchen", kit, ...`.
- Řetězec musí být uzavřen v uvozovkách `""`.

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
predef_msg = "Neodstraňujte ani neupravujte předdefinované proměnné!"
areas_msg = "Nepřiřadili jste správnou hodnotu k `areas`. Podívejte se znovu na instrukce. Ujistěte se, že pokaždé uvádíte název místnosti před proměnnou obsahující plochu. Pořadí je zde důležité! Dávejte pozor na překlepy."

Ex().check_correct(
  check_object("areas").has_equal_value(incorrect_msg = areas_msg),
  multi([ check_object(obj, missing_msg = predef_msg).has_equal_value(incorrect_msg = predef_msg) for obj in objs])
)

Ex().has_printout(0, not_printed_msg = "__JINJA__:Použili jste `{{sol_call}}` k vytištění seznamu `areas` na konci skriptu?")

success_msg("Výborně! Tento seznam obsahuje jak řetězce, tak čísla s plovoucí desetinnou čárkou, ale to pro Python není problém!")
```

---

## Seznam seznamů

```yaml
type: NormalExercise
key: 9158c577b0
lang: python
xp: 100
skills:
  - 2
```

Jako datový analytik budeš pracovat s velkým množstvím dat, a proto se hodí umět je vhodně seskupovat.

Místo jednoho seznamu obsahujícího řetězce a desetinná čísla, která představují názvy a rozlohy místností ve tvém domě, můžeš vytvořit seznam seznamů.

Pamatuj: `"hallway"` je řetězec, zatímco `hall` je proměnná, která reprezentuje desetinné číslo `11.25` zadané dříve.

`@instructions`
- Doplň seznam seznamů tak, aby obsahoval i data o ložnici a koupelně. Dbej na správné pořadí!
- Vypiš `house` – dává ti tento způsob strukturování dat větší smysl?

`@hint`
- Přidej _podseznam_ do seznamu `house` tak, že dovnitř hranatých závorek vložíš `["bedroom", bed]` a `["bathroom", bath]`.
- Nezapomeň za každý podseznam přidat čárku `,`.
- Proměnnou `x` vypíšeš tak, že na nový řádek napíšeš `print(x)`.

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
predef_msg = "Neodstraňujte ani neupravujte předdefinované proměnné!"
house_msg = "Proměnné `house` jste nepřiřadili správnou hodnotu. Podívejte se znovu na instrukce. Rozšiřte seznam seznamů tak, aby obsahoval seznam pro každý pár názvu místnosti a její plochy. Dbejte na pořadí a překlepy!"

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

Ex().has_printout(0, not_printed_msg = "__JINJA__:Použili jste `{{sol_call}}` pro výpis obsahu proměnné `house`?")

success_msg("Výborně! Připravte se na výuku výběru prvků ze seznamu!")
```

---

## Výběr prvků ze seznamu

```yaml
type: VideoExercise
key: c076b5a69c
xp: 50
```

`@projector_key`
fc15ba5cb9485456df8589130b519ea3

---

## Výběr prvků ze seznamu

```yaml
type: NormalExercise
key: c3ce582e32
lang: python
xp: 100
skills:
  - 2
```

Výběr prvků z Pythonových seznamů je hračka. Podívej se na ukázku níže – vytvoří seznam `x` a pak z něj vybere "b". Pamatuj, že jde o druhý prvek, tedy má index 1. Lze použít i záporné indexování.

```
x = ["a", "b", "c", "d"]
x[1]
x[-3] # stejný výsledek!
```

Pamatuješ na seznam `areas` z dřívějška, který obsahoval jak řetězce, tak čísla s desetinnou čárkou? Jeho definice je už ve skriptu. Přidej správný kód a vyzkoušej výběr prvků v Pythonu.

`@instructions`
- Vypiš druhý prvek ze seznamu `areas` (má hodnotu `11.25`).
- Vyber a vypiš poslední prvek seznamu `areas`, tedy `9.50`. Tady se záporný index přímo nabízí!
- Vyber číslo reprezentující plochu obývacího pokoje (`20.0`) a vypiš ho.

`@hint`
- Pomocí `x[1]` vyber druhý prvek seznamu `x`.
- Pomocí `x[-1]` vyber poslední prvek seznamu `x`.
- Nezapomeň obalit každou operaci výběru voláním `print()`.
- Číslo reprezentující plochu obývacího pokoje je 6. prvek v seznamu, takže budeš potřebovat `[5]`. `area[4]` by vrátilo řetězec!

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
msg = "Neodstraňujte ani neupravujte předdefinovaný seznam `areas`."
Ex().check_object("areas", missing_msg = msg).has_equal_value(incorrect_msg = msg)
Ex().has_printout(0, not_printed_msg = "Podívejte se znovu na svůj kód a vypište druhý prvek v `areas`, který je na indexu `1`.")
Ex().has_printout(1, not_printed_msg = "Podívejte se znovu na svůj kód a vypište poslední prvek v `areas`, který je na indexu `-1`.")
Ex().has_printout(2, not_printed_msg = "Podívejte se znovu na svůj kód a vypište plochu obývacího pokoje. Nachází se na indexu `5`.")
success_msg("Výborně!")
```

---

## Slicing a práce se seznamy

```yaml
type: NormalExercise
key: 7f08642d18
lang: python
xp: 100
skills:
  - 2
```

Výběr jednotlivých hodnot ze seznamu je jen část příběhu. Seznamy také umožňují _slicing_ – tedy výběr více prvků najednou. Použij následující syntaxi:

```
my_list[start:end]
```

Index `start` je do výběru zahrnut, zatímco index `end` zahrnut _není_. Tyto indexy ale nemusíš vždy uvádět. Pokud vynecháš index `start`, Python automaticky začne od začátku seznamu.

`@instructions`
- Pomocí slicingu vytvoř seznam `downstairs` obsahující prvních 6 prvků seznamu `areas`.
- Vytvoř seznam `upstairs` jako poslední `4` prvky seznamu `areas`. Tentokrát slicing zjednodušíš vynecháním indexu `end`.
- Oba seznamy `downstairs` a `upstairs` vypiš pomocí `print()`.

`@hint`
- Pomocí `[0:6]` získáš prvních šest prvků seznamu.
- Pokud chceš ze seznamu `l` vybrat vše kromě prvních 5 prvků, použij `l[5:]`.
- Přidej dvě volání `print()` pro výpis `downstairs` a `upstairs`.

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
msg = "Neodstraňujte ani neupravujte předdefinovaný seznam `areas`."
Ex().check_object("areas", missing_msg = msg).has_equal_value(incorrect_msg = msg)

patt = "`%s` je nesprávné. Použijte `areas[%s]` a slicing pro výběr požadovaných prvků nebo ekvivalentní postup."
Ex().check_object("downstairs").has_equal_value(incorrect_msg = patt % ('downstairs', '0:6'))
Ex().check_object("upstairs").has_equal_value(incorrect_msg = patt % ("upstairs",":6"))

Ex().has_printout(0, not_printed_msg="Vypsal/a jste `downstairs` po jeho výpočtu?")
Ex().has_printout(1, not_printed_msg="Vypsal/a jste `upstairs` po jeho výpočtu?")

success_msg("Výborně!")
```

---

## Výběr prvků ze seznamů seznamů

```yaml
type: NormalExercise
key: dbbbd306cf
xp: 100
```

Pythonový seznam může obsahovat i další seznamy.

Pro výběr prvků ze seznamů seznamů použiješ stejnou techniku jako předtím: hranaté závorky. Pro seznam `house` by to vypadalo třeba takto:

```
house[2][0]
```

`@instructions`
- Vyber ze seznamu `house` hodnotu `9.5` typu float.

`@hint`
- Postupuj krok za krokem. Nejdřív potřebuješ dostat se k poslednímu prvku seznamu, `["bathroom", 9.50]`. Vzpomeň si, že index posledního prvku je `-1`.
- Pak potřebuješ získat druhý prvek seznamu `["bathroom", 9.50]`, který je na indexu `1`.

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

success_msg("Správně! Poslední část skládanky se seznamy je manipulace.")
```

---

## Práce se seznamy

```yaml
type: VideoExercise
key: d7fe818b3a
xp: 50
```

`@projector_key`
355ed52d2fb0d67508c6a311b7cbc6d3

---

## Nahrazení prvků seznamu

```yaml
type: NormalExercise
key: 4e1bba1b55
lang: python
xp: 100
skills:
  - 2
```

Prvky seznamu nahradíš tak, že vybereš část seznamu a přiřadíš jí nové hodnoty. Můžeš vybrat jednotlivé prvky nebo změnit celé řezy seznamu najednou.

V tomto i v následujících cvičeních budeš pracovat se seznamem `areas`, který obsahuje názvy a plochy jednotlivých místností v domě.

`@instructions`
- Aktualizuj plochu koupelny na `10.50` čtverečních metrů místo `9.50` – použij přitom negativní indexování.
- Udělej seznam `areas` modernější! Změň `"living room"` na `"chill zone"`. Tentokrát ale negativní indexování nepoužívej.

`@hint`
- Abys aktualizoval/a plochu koupelny, identifikuj příslušný prvek v seznamu (je to poslední položka!).
- Pak nahraď hodnotu novou plochou koupelny tím, že ji přiřadíš k tomuto podseznamu.
- Stejným způsobem aktualizuj název `"living room"`, který je na indexu 4.

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
bathroom_msg = 'Pomocí `areas[-1] = 10.50` můžete aktualizovat plochu koupelny.'
chillzone_msg = 'Pomocí `areas[4] = "chill zone"` můžete aktualizovat název obývacího pokoje.'
Ex().check_correct(
  check_object('areas').has_equal_value(incorrect_msg = 'Vaše změny v `areas` nevedly ke správnému seznamu. Jste si jisti, že jste použili správné operace s podmnožinami? V případě pochybností můžete použít nápovědu!'),
  multi(
    has_equal_value(expr_code='areas[-1]', override=10.50, incorrect_msg = bathroom_msg),
    has_equal_value(expr_code='areas[4]', override='chill zone', incorrect_msg = chillzone_msg),
  )
)
success_msg('Výborně! Jak ukázal příklad kódu, můžete také rozdělit seznam a nahradit ho jiným seznamem, abyste aktualizovali více prvků jediným příkazem.')
```

---

## Rozšíření seznamu

```yaml
type: NormalExercise
key: ff0fe8d967
lang: python
xp: 100
skills:
  - 2
```

Když už umíš měnit prvky seznamu, jistě se hodí i umět do něj prvky přidávat. K tomu slouží operátor `+`:

```
x = ["a", "b", "c", "d"]
y = x + ["e", "f"]
```

Vyhrál/a jsi loterii – nádhera! Rozhodneš se postavit bazénový domek a garáž. Dokážeš přidat tyto informace do seznamu `areas`?

`@instructions`
- Pomocí operátoru `+` přidej seznam `["poolhouse", 24.5]` na konec seznamu `areas`. Výsledný seznam ulož jako `areas_1`.
- Dále rozšiř `areas_1` o data týkající se garáže. Přidej řetězec `"garage"` a desetinné číslo `15.45`. Výsledný seznam pojmenuj `areas_2`.

`@hint`
- Postupuj podle ukázky kódu v zadání. `x` odpovídá `areas` a `["e", "f"]` odpovídá `["poolhouse", 24.5]`.
- Pro přidání dalších prvků do `areas_1` použij `areas_1 + ["element", 123]`.

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
msg = "Neodstraňujte ani neupravujte předdefinovaný seznam `areas`."
Ex().check_object("areas", missing_msg = msg).has_equal_value(incorrect_msg = msg)
Ex().check_object("areas_1").has_equal_value(incorrect_msg = "Použijte `areas + [\"poolhouse\", 24.5]` k vytvoření `areas_1`. Dávejte pozor na překlepy!")
Ex().check_object("areas_2").has_equal_value(incorrect_msg = "Použijte `areas_1 + [\"garage\", 15.45]` k vytvoření `areas_2`. Dávejte pozor na překlepy!")
success_msg("Skvělé! Seznam se pěkně formuje!")
```

---

## Mazání prvků ze seznamu

```yaml
type: NormalExercise
key: 85f792356e
xp: 100
```

A nakonec – ze seznamu lze také odstraňovat prvky. Slouží k tomu příkaz `del`:

```
x = ["a", "b", "c", "d"]
del x[1]
```

Dej si pozor: jakmile ze seznamu odstraníš prvek, indexy všech následujících prvků se změní!

Bohužel, výhra v loterii nebyla tak velká, jak ses naděje/a, a pool house z plánů vypadl. Budeš ho muset ze seznamu odebrat – konkrétně odpovídající řetězec a desetinné číslo ze seznamu `areas`.

`@instructions`
- Odstraň ze seznamu `areas` řetězec a desetinné číslo patřící k `"poolhouse"`.
- Vypiš aktualizovaný seznam `areas`.

`@hint`
- Budeš muset použít `del` dvakrát, abys smazal/a dva prvky. Dávej ale pozor na změnu indexů!

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

Ex().has_printout(0, not_printed_msg="Vypsal/a jste `areas` po odstranění řetězce a čísla s plovoucí desetinnou čárkou pro bazén?")
success_msg("Správně! Později se dozvíte o jednodušších způsobech, jak odstraňovat konkrétní prvky z Pythonových seznamů.")
```

---

## Jak seznamy fungují uvnitř

```yaml
type: NormalExercise
key: af72db9915
lang: python
xp: 100
skills:
  - 2
```

V tomto cvičení máš připravený kód: seznam s názvem `areas` a jeho kopii pojmenovanou `areas_copy`.

V současné chvíli se změní první prvek seznamu `areas_copy` a poté se vypíše seznam `areas`. Pokud spustíš kód, uvidíš, že přestože jsi změnil/a `areas_copy`, změna se projeví i v seznamu `areas`. Je to proto, že `areas` i `areas_copy` ukazují na stejný seznam.

Pokud chceš zabránit tomu, aby se změny v `areas_copy` projevovaly i v `areas`, musíš vytvořit explicitní kopii seznamu `areas` pomocí `list()` nebo zápisu `[:]`.

`@instructions`
- Uprav druhý příkaz, který vytváří proměnnou `areas_copy`, tak aby byla `areas_copy` explicitní kopií `areas`. Po úpravě by změny provedené v `areas_copy` neměly ovlivnit `areas`. Odešli odpověď a ověř výsledek.

`@hint`
- Uprav volání `areas_copy = areas`. Místo přiřazení `areas` můžeš přiřadit `list(areas)` nebo `areas[:]`.

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
  check_object("areas_copy").has_equal_value(incorrect_msg = "Zdá se, že `areas_copy` nebyla správně aktualizována."),
  check_function("list", missing_msg = "Ujistěte se, že používáte `list(areas)` k vytvoření `areas_copy`.")
)

mmsg = "Neodstraňujte předdefinovaný seznam `areas`."
imsg = "Upravujte pouze kopii, nikoli původní seznam `areas`. Pokud si nejste jisti, jak vytvořit kopii, přečtěte si znovu popis cvičení."
Ex().check_correct(
  check_object("areas", missing_msg = mmsg).has_equal_value(incorrect_msg = imsg),
  check_function("list", missing_msg = "Ujistěte se, že používáte `list(areas)` k vytvoření `areas_copy`.")
)

success_msg("Výborně! Rozdíl mezi explicitními kopiemi a kopiemi založenými na referencích je nenápadný, ale může být velmi důležitý. Snažte se mít na paměti, jak je seznam uložen v paměti počítače.")
```

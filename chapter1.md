---
title_meta: Kapitel 1
title: Grunderna i Python
description: >-
  En introduktion till Pythons grundläggande koncept. Lär dig använda Python
  interaktivt och via skript. Skapa dina första variabler och bekanta dig med
  Pythons grundläggande datatyper.
attachments:
  slides_link: 'https://projector-video-pdf-converter.datacamp.com/735/chapter1.pdf'
free_preview: true
lessons:
  - nb_of_exercises: 3
    title: Hej Python!
  - nb_of_exercises: 5
    title: Variabler och typer
---

## Hej Python!

```yaml
type: VideoExercise
key: f644a48d5d
xp: 50
```

`@projector_key`
d8fcd4c930027fa4e1c3870c7e7e0ff1

---

## Din första Python-kod

```yaml
type: NormalExercise
key: bdc52f0e19
lang: python
xp: 100
skills:
  - 2
```

Nu är det dags att köra din första Python-kod!

Gå till koden och klicka på knappen Kör koden för att se utdatan.

`@instructions`
- Klicka på knappen Kör koden för att se utdatan av `print(5 / 8)`.

`@hint`
- Kör koden innan du skickar in ditt svar, så att du hinner utforska utdatan.

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
Ex().has_printout(0, not_printed_msg = "__JINJA__:Har du använt `{{sol_call}}` för att skriva ut `5 / 8`?")
success_msg("Bra! Vidare till nästa!")
```

---

## Python som miniräknare

```yaml
type: NormalExercise
key: 0f7c039428
lang: python
xp: 100
skills:
  - 2
```

Python lämpar sig utmärkt för grundläggande beräkningar – addition, subtraktion, multiplikation och division.

Koden i skriptet visar några exempel.

Nu är det din tur att öva genom att skriva lite kod själv.

`@instructions`
- Skriv ut resultatet av att subtrahera `5` från `5` under `# Subtraction` med hjälp av `print()`.
- Skriv ut resultatet av att multiplicera `3` med `5` under `# Multiplication`.

`@hint`
- Du behöver använda `print()` för att generera utdata.
- Du kan subtrahera med `-` och multiplicera med `*`.

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
Ex().has_printout(0, not_printed_msg = "Har du använt `print(4 + 5)` för att skriva ut resultatet av din addition?")

Ex().has_printout(1, not_printed_msg = "Har du använt `print(5 - 5)` för att skriva ut resultatet av din subtraktion?")

Ex().has_printout(2, not_printed_msg = "Har du använt `print(3 * 5)` för att skriva ut resultatet av din multiplikation?")

Ex().has_printout(3, not_printed_msg = "Har du använt `print(10 / 2)` för att skriva ut resultatet av din division?")

success_msg("Det är rätt! Python kan hjälpa dig med matematiken, en egenskap som kommer att vara användbar för analys när vi utvecklar våra datakunskaper.")
```

---

## Variabler och typer

```yaml
type: VideoExercise
key: c2e396792e
xp: 50
```

`@projector_key`
433dcfcfedaee070cbf440491c402e3b

---

## Tilldela variabler

```yaml
type: NormalExercise
key: 4bf65ad83e
lang: python
xp: 100
skills:
  - 2
```

I Python kan du använda en variabel för att referera till ett värde med ett namn. För att skapa en variabel `x` med värdet `5` använder du `=`, som i det här exemplet:

```
x = 5
```

Nu kan du använda variabelnamnet `x` i stället för det faktiska värdet `5`.

Kom ihåg att `=` i Python betyder _tilldelning_ – det testar inte likhet! Prova det i övningen genom att ersätta `____` med din kod.

`@instructions`
- Skapa en variabel `savings` med värdet `100`.
- Kontrollera variabeln genom att skriva `print(savings)` i skriptet.

`@hint`
- Skriv `savings = 100` för att skapa variabeln `savings`.
- När du har skapat variabeln `savings` kan du skriva `print(savings)`.
- Din färdiga kod ska inte innehålla några `____`.

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
Ex().check_object("savings").has_equal_value(incorrect_msg="Tilldela `100` till variabeln `savings`.")
Ex().has_printout(0, not_printed_msg = "Skriv ut `savings`, variabeln du skapade, med `print(savings)`.")
success_msg("Bra! Låt oss nu försöka göra några beräkningar med den här variabeln!")
```

---

## Beräkningar med variabler

```yaml
type: NormalExercise
key: ff06cedeb4
lang: python
xp: 100
skills:
  - 2
```

Nu har du skapat en variabel för ditt sparande – då är det dags att börja räkna!

Istället för att använda faktiska värden direkt i beräkningarna kan du använda variabler.

Hur mycket pengar skulle du ha sparat om fyra månader, om du sparar 10 dollar i månaden?

`@instructions`
- Skapa en variabel `monthly_savings` med värdet `10` och en variabel `num_months` med värdet `4`.
- Multiplicera `monthly_savings` med `num_months` och tilldela resultatet till `new_savings`.
- Skriv ut värdet av `new_savings`.

`@hint`
- Du kan räkna med variabler på samma sätt som med tal – ersätt alltså `10 * 4` med variablerna!
- Använd `print()` för att se värdet i `new_savings`.
- Kontrollera att du stavat variabelnamnen rätt!

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
Ex().check_object("monthly_savings").has_equal_value(incorrect_msg = "Sparade du `10` till `monthly_savings` med hjälp av `monthly_savings = 10`?")
Ex().check_object("num_months").has_equal_value(incorrect_msg = "Sparade du `4` till `num_months` med hjälp av `num_months = 4`?")
Ex().check_object("new_savings").has_equal_value(incorrect_msg = "Använde du rätt variabler och symboler för att multiplicera? Förväntade `monthly_savings * num_months` men fick något annat.")
# Ex().check_object("total_savings").has_equal_value(incorrect_msg = "Använde du rätt variabler och symboler för att addera? Förväntade `savings + new_savings` men fick något annat.")

Ex().has_printout(0, not_printed_msg="Kom ihåg att skriva ut `new_savings` i slutet av ditt skript.")

success_msg("Du har 40 dollar i nya besparingar!")
```

---

## Andra variabeltyper

```yaml
type: NormalExercise
key: 006b48561f
lang: python
xp: 100
skills:
  - 2
```

I den föregående övningen arbetade du med datatypen heltal i Python:

- `int`, eller heltal: ett tal utan decimaldel. `savings`, med värdet `100`, är ett exempel på ett heltal.

Förutom numeriska datatyper finns det tre andra vanliga datatyper:

- `float`, eller flyttal: ett tal som har både en heltalsdel och en decimaldel, åtskilda av en punkt. `1.1` är ett exempel på ett flyttal.
- `str`, eller sträng: en typ för att representera text. Du kan använda enkla eller dubbla citattecken för att skapa en sträng.
- `bool`, eller boolean: en typ för att representera logiska värden. Det kan bara vara `True` eller `False` (versalerna är viktiga!).

`@instructions`
- Skapa ett nytt flyttal, `half`, med värdet `0.5`.
- Skapa en ny sträng, `intro`, med värdet `"Hello! How are you?"`.
- Skapa ett nytt booleskt värde, `is_good`, med värdet `True`.

`@hint`
- För att skapa en variabel i Python använder du `=`. Kom ihåg att omge strängen med enkla eller dubbla citattecken.
- Det finns bara två booleska värden i Python: `True` och `False`. `TRUE`, `true`, `FALSE`, `false` och andra varianter godkänns inte.

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
Ex().check_object("half").has_equal_value(incorrect_msg = "Sparade du flyttalet `0.5` till `half`?")

Ex().check_object("intro").has_equal_value(incorrect_msg = "Hmm, något är felaktigt i din `intro`-variabel. Kontrollera stavningen och se till att du har använt citattecken.")

Ex().check_object("is_good").has_equal_value(incorrect_msg = "Skrev du det booleska värdet med stor bokstav? Kom ihåg att du inte behöver använda citattecken här.")

success_msg("Bra gjort!")
```

---

## Operationer med olika typer

```yaml
type: BulletExercise
key: 4d0d83cc02
xp: 100
```

Variabler kan ha olika typer i Python. Du kan se typen för en variabel med hjälp av `type()`. För att till exempel se typen för `a` kör du: `type(a)`.

Olika typer beter sig olika i Python. När du summerar två strängar får du ett annat resultat än när du summerar två heltal eller två booleska värden.

Dags att testa detta själv.

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
- Addera `savings` och `new_savings` och tilldela resultatet till `total_savings`.
- Använd `type()` för att skriva ut typen för `total_savings`.

`@hint`
- Tilldela `savings + new_savings` till en ny variabel, `total_savings`.
- För att skriva ut typen för en variabel `x` använder du `print(type(x))`.

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
msg = "Du behöver inte ändra eller ta bort de fördefinierade variablerna."

Ex().multi(
    check_object('savings', missing_msg=msg).has_equal_value(incorrect_msg=msg),
    check_object('new_savings', missing_msg=msg).has_equal_value(incorrect_msg=msg)
)

Ex().multi(
    check_object("total_savings").has_equal_value(incorrect_msg="Lägg till `savings` och `new_savings` för att skapa variabeln `total_savings`."),
    has_printout(1, not_printed_msg = "__JINJA__:Använd `{{sol_call}}` för att skriva ut typen av `total_savings`.")
)
```

***

```yaml
type: NormalExercise
key: f54fbf9bd9
xp: 50
```

`@instructions`
- Beräkna summan av `intro` och `intro` och tilldela resultatet till `doubleintro`.
- Skriv ut `doubleintro`. Fick du det resultat du förväntade dig?

`@hint`
- Tilldela `intro + intro` till en ny variabel, `doubleintro`.
- För att skriva ut en variabel `x` skriver du `print(x)` i skriptet.

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
msg = "Du behöver inte ändra eller ta bort de fördefinierade variablerna."

Ex().check_object('intro', missing_msg=msg).has_equal_value(incorrect_msg=msg)

Ex().multi(
    check_object("doubleintro").has_equal_value(incorrect_msg  = "Har du lagrat resultatet av `intro + intro` i `doubleintro`?"),
    has_printout(0, not_printed_msg = "Glöm inte att skriva ut `doubleintro`.")
)

success_msg("Bra. Lägg märke till hur `intro + intro` gör att `\"Hello! How are you?\"` och `\"Hello! How are you?\"` klistras ihop.")
```

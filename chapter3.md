---
title_meta: Kapitel 3
title: Funktioner och paket
description: >-
  Du lär dig använda funktioner, metoder och paket för att på ett effektivt sätt
  dra nytta av kod som skickliga Python-utvecklare redan har skrivit. Målet är
  att minska mängden kod du behöver skriva för att lösa komplexa problem!
attachments:
  slides_link: 'https://projector-video-pdf-converter.datacamp.com/735/chapter3.pdf'
lessons:
  - nb_of_exercises: 4
    title: Funktioner
  - nb_of_exercises: 4
    title: Metoder
  - nb_of_exercises: 4
    title: Paket
---

## Funktioner

```yaml
type: VideoExercise
key: 5c5f365930
xp: 50
```

`@projector_key`
1204d914b0e53100529827e07441ee6c

---

## Bekanta funktioner

```yaml
type: NormalExercise
key: c422ee929b
lang: python
xp: 100
skills:
  - 2
```

Python levereras med ett antal inbyggda funktioner som gör livet enklare för dig som datavetare. Du känner redan till två sådana funktioner: `print()` och `type()`. Det finns också funktioner som `str()`, `int()`, `bool()` och `float()` för att växla mellan datatyper. Du kan läsa mer om dem [här.](https://docs.python.org/3/library/functions.html) Även dessa är inbyggda funktioner.

Att anropa en funktion är enkelt. För att ta reda på typen av `3.0` och spara resultatet i en ny variabel, `result`, kan du skriva följande:

```
result = type(3.0)
```

`@instructions`
- Använd `print()` i kombination med `type()` för att skriva ut typen av `var1`.
- Använd `len()` för att hämta [längden på listan](https://docs.python.org/3/library/functions.html#len) `var1`. Omslut anropet med `print()` för att skriva ut resultatet direkt.
- Använd `int()` för att konvertera `var2` till ett [heltal](https://docs.python.org/3/library/functions.html#int). Spara resultatet i variabeln `out2`.

`@hint`
- Anropa funktionen `type()` så här: `type(var1)`.
- Anropa `print()` på samma sätt som du gjort många gånger tidigare. Ange helt enkelt den variabel du vill skriva ut inom parenteserna.
- `int(x)` konverterar `x` till ett heltal.

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
msg = "Du behöver inte ändra eller ta bort de fördefinierade variablerna."
Ex().check_object("var1", missing_msg=msg).has_equal_value(incorrect_msg=msg)
Ex().check_object("var2", missing_msg=msg).has_equal_value(incorrect_msg=msg)

patt = "__JINJA__:Se till att skriva ut %s av `var1` med `{{sol_call}}`."
Ex().has_printout(0, not_printed_msg = patt % 'typen')
Ex().has_printout(1, not_printed_msg = patt % 'längden')

int_miss_msg = "Har du använt `int()` för att skapa ett heltal av `var2`?"
int_incorr_msg = "Har du skickat `var2` till `int()`?"
Ex().check_correct(
  check_object("out2").has_equal_value(incorrect_msg="Du anropade `int()` korrekt; se nu till att tilldela resultatet av detta anrop till `out2`."),
  check_function("int", missing_msg=int_miss_msg).has_equal_value(incorrect_msg=int_incorr_msg)
)
success_msg("Bra jobbat! Funktionen `len()` är extremt användbar; den fungerar även på strängar för att räkna antalet tecken!")
```

---

## Hjälp!

```yaml
type: MultipleChoiceExercise
key: 679b852978
lang: python
xp: 50
skills:
  - 2
```

Kanske vet du redan namnet på en Python-funktion, men behöver ta reda på hur du använder den. Något ironiskt nog behöver du då använda en annan funktion för att få information: `help()`. I IPython kan du även skriva `?` före funktionsnamnet.

För att till exempel få hjälp med funktionen `max()` kan du använda något av dessa anrop:

```
help(max)
?max
```

Använd IPython Shell för att öppna [dokumentationen](https://docs.python.org/3/library/functions.html#pow) för `pow()`. Skriv `?pow` eller `help(pow)` och tryck på **Enter**.

Vilket av följande påståenden stämmer?

`@possible_answers`
- `pow()` tar tre argument: `base`, `exp` och `mod`. Utan `mod` returnerar funktionen ett fel.
- `pow()` tar tre obligatoriska argument: `base`, `exp` och `None`.
- `pow()` kräver argumenten `base` och `exp`; `mod` är valfritt.
- `pow()` tar två argument: `exp` och `mod`. Om `exp` saknas uppstår ett fel.

`@hint`
- Valfria argument tilldelas ett standardvärde med `=`, som funktionen använder om argumentet inte anges.

`@pre_exercise_code`
```{python}

```

`@sct`
```{python}
msg1 = "Inte riktigt. `mod` har ett standardvärde som används om du inte anger ett värde."
msg2 = "Felaktigt. `None` är standardvärdet för argumentet `mod`."
msg3 = "Perfekt! Att använda `help()` kan hjälpa dig att förstå hur funktioner fungerar och frigöra deras fulla potential!"
msg4 = "Felaktigt. `pow()` tar tre argument, varav ett har ett standardvärde."
Ex().has_chosen(3, [msg1, msg2, msg3, msg4])
```

---

## Flera argument

```yaml
type: NormalExercise
key: e30486d7c1
lang: python
xp: 100
skills:
  - 2
```

I föregående övning identifierade du valfria argument genom att läsa dokumentationen med `help()`. Nu ska du använda samma metod för att ändra beteendet hos funktionen `sorted()`.

Ta en titt på [dokumentationen](https://docs.python.org/3/library/functions.html#sorted) för `sorted()` genom att skriva `help(sorted)` i IPython Shell.

Du ser att `sorted()` tar tre argument: `iterable`, `key` och `reverse`. I den här övningen behöver du bara ange `iterable` och `reverse`, inte `key`.

Det finns redan två listor skapade åt dig.

Kan du slå ihop dem och sortera dem i fallande ordning?

`@instructions`
- Använd `+` för att slå ihop innehållet i `first` och `second` till en ny lista: `full`.
- Anropa `sorted()` på `full` och ange argumentet `reverse` till `True`. Spara den sorterade listan som `full_sorted`.
- Avsluta med att skriva ut `full_sorted`.

`@hint`
- Summera `first` och `second` som om de vore två tal och tilldela resultatet till `full`.
- Använd `sorted()` med två argument: `full` och `reverse=True`.
- Använd `print()` för att skriva ut en variabel.

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
msg = "Du behöver inte ändra eller ta bort de redan befintliga variablerna `first` och `second`."
Ex().multi(
  check_object("first", missing_msg=msg).has_equal_value(incorrect_msg=msg),
  check_object("second", missing_msg=msg).has_equal_value(incorrect_msg=msg)
)
Ex().check_correct(
  check_object("full_sorted").has_equal_value(incorrect_msg="Se till att du tilldelar resultatet av anropet till `sorted()` till `full_sorted`."),
  check_function("sorted").multi(
    check_args(0).has_equal_value(),
    check_args('reverse').has_equal_value()
  )
)

success_msg("Bra gjort! Gå vidare till videon om Python-metoder.")
```

---

## Metoder

```yaml
type: VideoExercise
key: 2b66cb66b1
xp: 50
```

`@projector_key`
8e387776f3a264a745128b68aa8d8f83

---

## Strängmetoder

```yaml
type: NormalExercise
key: 4039302ee0
lang: python
xp: 100
skills:
  - 2
```

Strängar har många användbara metoder. Följ instruktionerna noggrant för att bekanta dig med några av dem. Om du vill utforska dem mer i detalj kan du alltid skriva `help(str)` i IPython Shell.

En sträng `place` har redan skapats åt dig att experimentera med.

`@instructions`
- Använd metoden `.upper()` på `place` och lagra resultatet i `place_up`. Använd den syntax för metodanrop som du lärde dig i föregående video.
- Skriv ut `place` och `place_up`. Förändrades båda?
- Skriv ut antalet o:n i variabeln `place` genom att anropa `.count()` på `place` och skicka in bokstaven `'o'` som argument. Det gäller variabeln `place`, inte ordet `"place"`!

`@hint`
- Du kan anropa metoden `.upper()` på `place` utan några extra argument.
- För att skriva ut en variabel `x` kan du använda `print(x)`.
- Se till att omsluta anropet `place.count(____)` i en `print()`-funktion så att resultatet skrivs ut.

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
msg = "Du behöver inte ändra eller ta bort de fördefinierade variablerna."
Ex().check_object("place", missing_msg=msg).has_equal_value(incorrect_msg=msg)

patt = "Glöm inte att skriva ut `%s`."
Ex().has_printout(0, not_printed_msg=patt % "place")
Ex().check_correct(
    has_printout(1, not_printed_msg=patt % "place_up"),
    check_correct(
        check_object("place_up").has_equal_value(incorrect_msg="Tilldela resultatet av ditt `place.upper()`-anrop till `place_up`."),
        check_function("place.upper", signature=False)
    )
)    

# check count of place
Ex().check_correct(
  has_printout(2, not_printed_msg = "Du har beräknat antalet o:n i `place` korrekt; se nu till att omsluta `place.count('o')`-anropet i en `print()`-funktion för att skriva ut resultatet."),
  check_function("place.count", signature=False).check_args(0).has_equal_value()
)

success_msg("Bra gjort! Lägg märke till i utskrifterna att metoden `upper()` inte förändrar det objekt den anropas på. Detta kommer att vara annorlunda för listor i nästa övning!")
```

---

## Listmetoder

```yaml
type: NormalExercise
key: 0dbe8ed695
lang: python
xp: 100
skills:
  - 2
```

Strängar är inte den enda Python-typen som har tillhörande metoder. Listor, flyttal, heltal och booleaner är också typer som kommer med en uppsättning användbara metoder. I den här övningen får du prova på:

- `.index()`, för att hämta indexet för det första elementet i en lista som matchar det angivna värdet, och
- `.count()`, för att räkna hur många gånger ett element förekommer i en lista.

Du kommer att arbeta med listan `areas`, som innehåller arean för olika delar av ett hus.

`@instructions`
- Använd metoden `.index()` för att hämta indexet för det element i `areas` som är lika med `20.0`. Skriv ut detta index.
- Anropa `.count()` på `areas` för att ta reda på hur många gånger `9.50` förekommer i listan. Skriv ut även detta antal.

`@hint`
- För att skriva ut indexet, omslut anropet `areas.index(___)` med funktionen `print()`.
- För att skriva ut antalet gånger elementet `x` förekommer i listan, omslut anropet `areas.count(___)` med funktionen `print()`.

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
predef_msg = "Du behöver inte ändra eller ta bort den fördefinierade listan `areas`."

Ex().check_object("areas", missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg)

Ex().check_function("print", index=0).check_args(0).check_function('areas.index', signature=False).check_args(0).has_equal_value()


Ex().check_function("print", index=1).check_args(0).check_function('areas.count', signature=False).has_equal_value()

success_msg("Bra gjort! Det här var exempel på `list`-metoder som inte ändrade listan de anropades på.")
```

---

## Listmetoder (2)

```yaml
type: NormalExercise
key: 1fbeab82d0
lang: python
xp: 100
skills:
  - 2
```

De flesta listmetoder förändrar listan de anropas på. Exempel på sådana metoder:

- `.append()`, som lägger till ett element i listan,
- `.remove()`, som [tar bort](https://docs.python.org/3/library/stdtypes.html#typesseq-mutable) det första elementet i en lista som matchar det angivna värdet, och
- `.reverse()`, som [vänder](https://docs.python.org/3/library/stdtypes.html#typesseq-mutable) på ordningen av elementen i listan.

Du kommer att arbeta med listan `areas`, som innehåller ytan för olika delar av ett hus.

`@instructions`
- Använd `.append()` två gånger för att lägga till ytan för poolhuset och garaget igen: `24.5` respektive `15.45`. Se till att lägga till dem i den ordningen.
- Skriv ut `areas`.
- Använd metoden `.reverse()` för att vända på ordningen av elementen i `areas`.
- Skriv ut `areas` en gång till.

`@hint`
- För den första instruktionen, använd `areas.append(___)` två gånger.
- För att skriva ut en variabel `x`, skriv helt enkelt `print(x)`.
- Metoden `.reverse()` kräver inga extra argument – använd bara punktnotation och tomma parenteser: `.reverse()`.
- För att skriva ut en variabel `x`, skriv helt enkelt `print(x)`.

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

success_msg("Bra gjort!")
```

---

## Paket

```yaml
type: VideoExercise
key: ab96a17c5e
xp: 50
```

`@projector_key`
cedcfb34350be8545599768f96695cdd

---

## Importera paket

```yaml
type: NormalExercise
key: 7432a6376f
lang: python
xp: 100
skills:
  - 2
```

Säg att du vill beräkna omkretsen och arean av en cirkel. Formlerna ser ut så här:

$$C = 2 \pi r$$
$$A = \pi r^2 $$

Istället för att skriva in talet för `pi` manuellt kan du använda paketet `math`, som redan innehåller det värdet.

För referens: `**` är symbolen för upphöjning till. Till exempel är `3**4` lika med `3` upphöjt till `4`, vilket ger `81`.

`@instructions`
- Importera paketet `math`.
- Använd `math.pi` för att beräkna cirkelns omkrets och lagra resultatet i `C`.
- Använd `math.pi` för att beräkna cirkelns area och lagra resultatet i `A`.

`@hint`
- Du kan enkelt använda `import math` och sedan referera till `pi` med `math.pi`.
- Använd formeln i uppgiftstexten för att beräkna `C`. Använd `*`.
- Använd formeln i uppgiftstexten för att beräkna `A`. Använd `*` och `**`.

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
patt = "Din beräkning av `%s` är inte helt korrekt. Se till att använda `math.pi`."
Ex().multi(
  has_import('math', same_as=False),
  check_object('C').has_equal_value(incorrect_msg=patt%'C'),
  check_object('A').has_equal_value(incorrect_msg=patt%'A')
)

Ex().multi(
  has_printout(0, not_printed_msg = "__JINJA__:Behåll `{{sol_call}}` där för att skriva ut omkretsen."),
  has_printout(1, not_printed_msg = "__JINJA__:Behåll `{{sol_call}}` där för att skriva ut arean.")
)

success_msg("Bra gjort! Om du vet hur man hanterar funktioner från paket, har du tillgång till kraften hos många Python-programmerare!")
```

---

## Selektivt import

```yaml
type: NormalExercise
key: fe65eff50a
lang: python
xp: 100
skills:
  - 2
```

Generella importer, som `import math`, ger dig tillgång till **all** funktionalitet i paketet `math`. Men om du bara behöver en specifik del av ett paket kan du göra importen mer selektiv:

```
from math import pi
```

Pröva samma sak igen, men den här gången importerar du bara `pi`.

`@instructions`
- Gör ett selektivt import från paketet `math` där du bara importerar funktionen `pi`.
- Använd `pi` för att beräkna cirkelns omkrets och lagra resultatet i `C`.
- Använd `pi` för att beräkna cirkelns area och lagra resultatet i `A`.

`@hint`
- Använd `from math import pi` för att göra ett selektivt import.
- Nu kan du använda `pi` direkt!

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
patt = "Din beräkning av `%s` är inte riktigt korrekt. Se till att endast använda `pi`."

Ex().has_import("math.pi", not_imported_msg = "Se till att importera `pi` från paketet `math`. Du bör använda notationen `from ___ import ___`.",)

Ex().multi(
  check_object('C').has_equal_value(incorrect_msg=patt%'C'),
  check_object('A').has_equal_value(incorrect_msg=patt%'A')
)

Ex().multi(
  has_printout(0, not_printed_msg = "__JINJA__:Behåll `{{sol_call}}` där för att skriva ut omkretsen."),
  has_printout(1, not_printed_msg = "__JINJA__:Behåll `{{sol_call}}` där för att skriva ut arean.")
)

success_msg("Bra! Gå vidare till nästa övning.")
```

---

## Olika sätt att importera

```yaml
type: MultipleChoiceExercise
key: f1b2675a2a
lang: python
xp: 50
skills:
  - 2
```

Det finns flera sätt att importera paket och moduler i Python. Beroende på hur du skriver importanropet behöver du använda olika Python-kod.

Anta att du vill använda [funktionen](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.inv.html) `inv()`, som finns i underpaketet `linalg` i paketet `scipy`. Du vill kunna använda funktionen på följande sätt:

```
my_inv([[1,2], [3,4]])
```

Vilken `import`-sats behöver du för att köra koden ovan utan fel?

`@possible_answers`
- `import scipy`
- `import scipy.linalg`
- `from scipy.linalg import my_inv`
- `from scipy.linalg import inv as my_inv`

`@hint`
- Prova de olika importsatserna i IPython-skalet och se vilken som gör att raden `my_inv([[1, 2], [3, 4]])` körs utan fel. Tryck på **enter** för att köra koden du har skrivit.

`@pre_exercise_code`
```{python}

```

`@sct`
```{python}
msg1 = msg2 = msg3 = "Felaktigt, försök igen. Prova de olika importsatserna i IPython-skalet och se vilken som gör att raden `my_inv([[1, 2], [3, 4]])` körs utan fel."
msg4 = "Rätt! Ordet `as` låter dig skapa ett lokalt namn för funktionen du importerar: `inv()` är nu tillgänglig som `my_inv()`."
Ex().has_chosen(4, [msg1, msg2, msg3, msg4])
```

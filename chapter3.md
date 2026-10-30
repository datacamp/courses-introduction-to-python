---
title_meta: Capitolo 3
title: Funzioni e pacchetti
description: >-
  Imparerai a usare funzioni, metodi e pacchetti per sfruttare in modo
  efficiente il codice scritto da sviluppatori Python di grande talento.
  L'obiettivo è ridurre la quantità di codice necessaria per risolvere problemi
  complessi!
attachments:
  slides_link: 'https://projector-video-pdf-converter.datacamp.com/735/chapter3.pdf'
lessons:
  - nb_of_exercises: 4
    title: Funzioni
  - nb_of_exercises: 4
    title: Metodi
  - nb_of_exercises: 4
    title: Pacchetti
---

## Funzioni

```yaml
type: VideoExercise
key: 5c5f365930
xp: 50
```

`@projector_key`
1204d914b0e53100529827e07441ee6c

---

## Funzioni familiari

```yaml
type: NormalExercise
key: c422ee929b
lang: python
xp: 100
skills:
  - 2
```

Python offre molte funzioni integrate per rendere la vita dei data scientist più semplice. Conosci già due di queste funzioni: `print()` e `type()`. Esistono anche funzioni come `str()`, `int()`, `bool()` e `float()` per passare da un tipo di dato a un altro. Puoi scoprirne di più [qui.](https://docs.python.org/3/library/functions.html) Anche queste sono funzioni integrate.

Chiamare una funzione è semplice. Per ottenere il tipo di `3.0` e salvare il risultato in una nuova variabile chiamata `result`, puoi fare così:

```
result = type(3.0)
```

`@instructions`
- Usa `print()` insieme a `type()` per stampare il tipo di `var1`.
- Usa `len()` per ottenere la [lunghezza della lista](https://docs.python.org/3/library/functions.html#len) `var1`. Racchiudila in una chiamata a `print()` per stamparla direttamente.
- Usa `int()` per convertire `var2` in un [numero intero](https://docs.python.org/3/library/functions.html#int). Salva il risultato in `out2`.

`@hint`
- Chiama la funzione `type()` in questo modo: `type(var1)`.
- Chiama `print()`, come hai già fatto tante volte. Basta mettere tra parentesi la variabile che vuoi stampare.
- `int(x)` convertirà `x` in un numero intero.

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
msg = "Non devi cambiare o rimuovere le variabili predefinite."
Ex().check_object("var1", missing_msg=msg).has_equal_value(incorrect_msg=msg)
Ex().check_object("var2", missing_msg=msg).has_equal_value(incorrect_msg=msg)

patt = "__JINJA__:Assicurati di stampare il %s di `var1` con `{{sol_call}}`."
Ex().has_printout(0, not_printed_msg = patt % 'tipo')
Ex().has_printout(1, not_printed_msg = patt % 'lunghezza')

int_miss_msg = "Hai usato `int()` per creare un intero da `var2`?"
int_incorr_msg = "Hai passato `var2` a `int()`?"
Ex().check_correct(
  check_object("out2").has_equal_value(incorrect_msg="Hai chiamato `int()` correttamente; ora assicurati di assegnare il risultato di questa chiamata a `out2`."),
  check_function("int", missing_msg=int_miss_msg).has_equal_value(incorrect_msg=int_incorr_msg)
)
success_msg("Ottimo lavoro! La funzione `len()` è estremamente utile; funziona anche sulle stringhe per contare il numero di caratteri!")
```

---

## Aiuto!

```yaml
type: MultipleChoiceExercise
key: 679b852978
lang: python
xp: 50
skills:
  - 2
```

Forse conosci già il nome di una funzione Python, ma devi ancora capire come usarla. È curioso, ma per ottenere informazioni su una funzione devi usare un’altra funzione: `help()`. In IPython, puoi anche usare `?` prima del nome della funzione.

Per esempio, per ottenere aiuto sulla funzione `max()`, puoi usare una di queste chiamate:

```
help(max)
?max
```

Usa la shell IPython per aprire la [documentazione](https://docs.python.org/3/library/functions.html#pow) su `pow()`. Per farlo, digita `?pow` o `help(pow)` e premi **Invio**.

Quale delle seguenti affermazioni è vera?

`@possible_answers`
- `pow()` accetta tre argomenti: `base`, `exp` e `mod`. Senza `mod`, la funzione restituirà un errore.
- `pow()` richiede tre argomenti: `base`, `exp` e `None`.
- `pow()` richiede gli argomenti `base` e `exp`; `mod` è facoltativo.
- `pow()` accetta due argomenti: `exp` e `mod`. Se manca `exp`, si verifica un errore.

`@hint`
- Gli argomenti opzionali sono quelli a cui viene assegnato `=` un valore predefinito, che la funzione utilizza se l’argomento non viene specificato.

`@pre_exercise_code`
```{python}

```

`@sct`
```{python}
msg1 = "Non proprio. `mod` ha un valore predefinito che verrà utilizzato se non specifichi un valore."
msg2 = "Errato. `None` è il valore predefinito per l'argomento `mod`."
msg3 = "Perfetto! Usare `help()` può aiutarti a capire come funzionano le funzioni, sbloccando tutto il loro potenziale!"
msg4 = "Errato. `pow()` accetta tre argomenti, uno dei quali ha un valore predefinito."
Ex().has_chosen(3, [msg1, msg2, msg3, msg4])
```

---

## Argomenti multipli

```yaml
type: NormalExercise
key: e30486d7c1
lang: python
xp: 100
skills:
  - 2
```

Nell’esercizio precedente hai individuato gli argomenti opzionali consultando la documentazione con `help()`. Ora applicherai questo approccio per modificare il comportamento della funzione `sorted()`.

Dai un'occhiata alla [documentazione](https://docs.python.org/3/library/functions.html#sorted) di `sorted()` digitando `help(sorted)` nella shell IPython.

Vedrai che `sorted()` accetta tre argomenti: `iterable`, `key` e `reverse`. In questo esercizio dovrai specificare solo `iterable` e `reverse`, non `key`.

Sono già state create due liste per te.

Riesci a unirle e ordinarle in ordine decrescente?

`@instructions`
- Usa `+` per unire gli elementi di `first` e `second` in una nuova lista chiamata `full`.
- Chiama `sorted()` su `full` e imposta l’argomento`reverse` su `True`. Salva la lista ordinata in `full_sorted`.
- Infine, stampa `full_sorted`.

`@hint`
- Somma `first` e `second` come se fossero numeri e assegna il risultato a `full`.
- Usa `sorted()` con due input: `full` e `reverse=True`.
- Per stampare una variabile, usa `print()`.

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
msg = "Non devi cambiare o rimuovere le variabili `first` e `second` già esistenti."
Ex().multi(
  check_object("first", missing_msg=msg).has_equal_value(incorrect_msg=msg),
  check_object("second", missing_msg=msg).has_equal_value(incorrect_msg=msg)
)
Ex().check_correct(
  check_object("full_sorted").has_equal_value(incorrect_msg="Assicurati di assegnare il risultato della chiamata a `sorted()` a `full_sorted`."),
  check_function("sorted").multi(
    check_args(0).has_equal_value(),
    check_args('reverse').has_equal_value()
  )
)

success_msg("Forte! Vai al video sui metodi Python.")
```

---

## Metodi

```yaml
type: VideoExercise
key: 2b66cb66b1
xp: 50
```

`@projector_key`
8e387776f3a264a745128b68aa8d8f83

---

## Metodi delle stringhe

```yaml
type: NormalExercise
key: 4039302ee0
lang: python
xp: 100
skills:
  - 2
```

Le stringhe hanno molti metodi utili. Segui attentamente le istruzioni per scoprirne alcuni. Se vuoi esplorarli più nel dettaglio, puoi sempre digitare `help(str)` nella shell IPython.

È già stata creata per te una stringa `place` con cui sperimentare.

`@instructions`
- Usa il [metodo](https://docs.python.org/3/library/stdtypes.html#str.upper) `.upper()` su`place` e salva il risultato in `place_up`. Utilizza la sintassi per la chiamata ai metodi che hai visto nel video precedente.
- Stampa `place` e `place_up`. Sono cambiati entrambi?
- Stampa il numero di “o” presenti nella variabile `place` chiamando `.count()` su `place` e passando la lettera `'o'` come input del metodo. Parliamo della variabile `place`, non della parola `"place"`!

`@hint`
- Puoi chiamare il metodo `.upper()` su `place` senza fornire input aggiuntivi.
- Per stampare una variabile `x`, puoi scrivere `print(x)`.
- Assicurati di racchiudere la chiamata a `place.count(____)` in una funzione `print()` per stamparne il risultato.

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
msg = "Non devi cambiare o rimuovere le variabili predefinite."
Ex().check_object("place", missing_msg=msg).has_equal_value(incorrect_msg=msg)

patt = "Non dimenticare di stampare `%s`."
Ex().has_printout(0, not_printed_msg=patt % "place")
Ex().check_correct(
    has_printout(1, not_printed_msg=patt % "place_up"),
    check_correct(
        check_object("place_up").has_equal_value(incorrect_msg="Assegna il risultato della tua chiamata `place.upper()` a `place_up`."),
        check_function("place.upper", signature=False)
    )
)    

# check count of place
Ex().check_correct(
  has_printout(2, not_printed_msg = "Hai calcolato correttamente il numero di o in `place`; ora assicurati di racchiudere la chiamata `place.count('o')` in una funzione `print()` per stampare il risultato."),
  check_function("place.count", signature=False).check_args(0).has_equal_value()
)

success_msg("Ben fatto! Nota dai risultati stampati che il metodo `upper()` non cambia l'oggetto su cui è chiamato. Questo sarà diverso per le liste nel prossimo esercizio!")
```

---

## Metodi delle liste

```yaml
type: NormalExercise
key: 0dbe8ed695
lang: python
xp: 100
skills:
  - 2
```

Le stringhe non sono gli unici tipi Python a disporre di metodi. Anche liste, float, numeri interi e booleani includono numerosi metodi utili. In questo esercizio userai:

- `.index()`, per ottenere l’indice del primo elemento di una lista che corrisponde all’input, e
- `.count()`, per sapere quante volte un elemento compare in una lista.

Lavorerai sulla lista `areas` con le aree delle diverse parti di una casa.

`@instructions`
- Usa il metodo `.index()` per ottenere l’indice dell’elemento in `areas` uguale a `20.0`. Stampalo.
- Chiama `.count()` su `areas` per scoprire quante volte `9.50` compare nella lista. Anche in questo caso, stampa semplicemente il numero.

`@hint`
- Per stampare l'indice, racchiudi la chiamata a `areas.index(___)` in una funzione `print()`.
- Per stampare il numero di volte in cui un elemento `x` compare nella lista, racchiudi la chiamata `areas.count(___)` in una funzione `print()`.

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
predef_msg = "Non devi cambiare o rimuovere la lista predefinita `areas`."

Ex().check_object("areas", missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg)

Ex().check_function("print", index=0).check_args(0).check_function('areas.index', signature=False).check_args(0).has_equal_value()


Ex().check_function("print", index=1).check_args(0).check_function('areas.count', signature=False).has_equal_value()

success_msg("Ben fatto! Questi erano esempi di metodi `list` che non hanno modificato la lista su cui sono stati chiamati.")
```

---

## Metodi delle liste (2)

```yaml
type: NormalExercise
key: 1fbeab82d0
lang: python
xp: 100
skills:
  - 2
```

La maggior parte dei metodi delle liste modifica la lista stessa. Ecco un paio di esempi:

- `.append()`, che aggiunge un elemento alla lista.
- `.remove()`, che [rimuove](https://docs.python.org/3/library/stdtypes.html#typesseq-mutable) il primo elemento di una lista che corrisponde all'input, e
- `.reverse()`, che [inverte](https://docs.python.org/3/library/stdtypes.html#typesseq-mutable) l'ordine degli elementi nella lista.

Lavorerai sulla lista `areas` con le aree delle diverse parti di una casa.

`@instructions`
- Usa due volte `.append()` per aggiungere di nuovo le dimensioni della casetta in giardino e del garage: `24.5` e `15.45`, rispettivamente. Assicurati di aggiungerli in quest’ordine.
- Stampa `areas`.
- Usa il metodo `.reverse()` per invertire l'ordine degli elementi in `areas`.
- Stampa nuovamente `areas`.

`@hint`
- Per la prima istruzione, usa due volte la chiamata `areas.append(___)`.
- Per stampare una variabile `x`, basta scrivere `print(x)`.
- Il metodo `.reverse()` non richiede input extra: usa la notazione a punto seguita da parentesi vuote, `.reverse()`.
- Per stampare una variabile `x`, basta scrivere `print(x)`.

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

success_msg("Ottimo!")
```

---

## Pacchetti

```yaml
type: VideoExercise
key: ab96a17c5e
xp: 50
```

`@projector_key`
cedcfb34350be8545599768f96695cdd

---

## Importare un pacchetto

```yaml
type: NormalExercise
key: 7432a6376f
lang: python
xp: 100
skills:
  - 2
```

Diciamo che vuoi calcolare la circonferenza e l'area di un cerchio. Ecco le formule:

$$C = 2 \pi r$$
$$A = \pi r^2 $$

Invece di digitare il valore di `pi`, puoi usare il pacchetto `math`, che lo contiene.

Nota: `**` è l’operatore di esponenziazione. Per esempio, `3**4` è `3` elevato a `4` e restituisce `81`.

`@instructions`
- Importa il pacchetto `math`.
- Usa `math.pi` per calcolare la circonferenza del cerchio e salva il risultato in `C`.
- Usa `math.pi` per calcolare l'area del cerchio e salva il risultato in `A`.

`@hint`
- Puoi semplicemente usare `import math` e poi fare riferimento a `pi` tramite `math.pi`.
- Usa l'equazione nel testo dell'esercizio per trovare `C`. Usa `*`.
- Usa l'equazione nel testo dell'esercizio per trovare `A`. Usa `*` e `**`.

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
patt = "Il tuo calcolo di `%s` non è del tutto corretto. Assicurati di usare `math.pi`."
Ex().multi(
  has_import('math', same_as=False),
  check_object('C').has_equal_value(incorrect_msg=patt%'C'),
  check_object('A').has_equal_value(incorrect_msg=patt%'A')
)

Ex().multi(
  has_printout(0, not_printed_msg = "__JINJA__:Mantieni `{{sol_call}}` lì per stampare la circonferenza."),
  has_printout(1, not_printed_msg = "__JINJA__:Mantieni `{{sol_call}}` lì per stampare l'area.")
)

success_msg("Ottimo! Se sai come gestire le funzioni dai pacchetti, il potere di molti programmatori Python è a portata di mano!")
```

---

## Importazione selettiva

```yaml
type: NormalExercise
key: fe65eff50a
lang: python
xp: 100
skills:
  - 2
```

Le importazioni generali, come `import math`, ti danno accesso a **tutte** le funzionalità del pacchetto `math`. Tuttavia, se vuoi usare solo una parte di un pacchetto, puoi sempre rendere l'importazione più selettiva:

```
from math import pi
```

Prova di nuovo la stessa cosa, ma questa volta usa solo `pi`.

`@instructions`
- Fai un'importazione selettiva dal pacchetto `math`, importando solo la funzione `pi`.
- Usa `pi` per calcolare la circonferenza del cerchio e salva il risultato in `C`.
- Usa `pi` per calcolare l'area del cerchio e salva il risultato in `A`.

`@hint`
- Usa `from math import pi` per fare un’importazione selettiva.
- Ora puoi usare direttamente `pi`!

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
patt = "Il tuo calcolo di `%s` non è del tutto corretto. Assicurati di usare solo `pi`."

Ex().has_import("math.pi", not_imported_msg = "Assicurati di importare `pi` dal pacchetto `math`. Dovresti usare la notazione `from ___ import ___`.",)

Ex().multi(
  check_object('C').has_equal_value(incorrect_msg=patt%'C'),
  check_object('A').has_equal_value(incorrect_msg=patt%'A')
)

Ex().multi(
  has_printout(0, not_printed_msg = "__JINJA__:Mantieni `{{sol_call}}` lì per stampare la circonferenza."),
  has_printout(1, not_printed_msg = "__JINJA__:Mantieni `{{sol_call}}` lì per stampare l'area.")
)

success_msg("Ben fatto! Passa all'esercizio successivo.")
```

---

## Diversi modi per importare

```yaml
type: MultipleChoiceExercise
key: f1b2675a2a
lang: python
xp: 50
skills:
  - 2
```

Esistono diversi modi per importare pacchetti e moduli in Python. A seconda della sintassi di importazione, dovrai scrivere il codice in modo diverso.

Supponiamo che tu voglia usare la [funzione](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.inv.html) `inv()`, che si trova nel sottopacchetto `linalg` del pacchetto `scipy`. Vuoi poter usare questa funzione in questo modo:

```
my_inv([[1,2], [3,4]])
```

Quale istruzione `import` devi usare per eseguire il codice qui sopra senza errori?

`@possible_answers`
- `import scipy`
- `import scipy.linalg`
- `from scipy.linalg import my_inv`
- `from scipy.linalg import inv as my_inv`

`@hint`
- Prova le diverse istruzioni di importazione nella shell IPython e verifica quale permette di eseguire la riga `my_inv([[1, 2], [3, 4]])` senza errori. Premi **Invio** per eseguire il codice che hai scritto.

`@pre_exercise_code`
```{python}

```

`@sct`
```{python}
msg1 = msg2 = msg3 = "Incorretto, riprova. Prova i diversi comandi di importazione nella shell IPython e vedi quale fa eseguire la linea `my_inv([[1, 2], [3, 4]])` senza errori."
msg4 = "Corretto! La parola `as` ti permette di creare un nome locale per la funzione che stai importando: `inv()` è ora disponibile come `my_inv()`."
Ex().has_chosen(4, [msg1, msg2, msg3, msg4])
```

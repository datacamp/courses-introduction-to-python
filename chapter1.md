---
title_meta: Capitolo 1
title: Nozioni di base di Python
description: >-
  Un’introduzione ai concetti base di Python. Impara a utilizzarlo in modo
  interattivo e tramite script. Crea le tue prime variabili e familiarizza con i
  tipi di dati base di questo linguaggio.
attachments:
  slides_link: 'https://projector-video-pdf-converter.datacamp.com/735/chapter1.pdf'
free_preview: true
lessons:
  - nb_of_exercises: 3
    title: Ciao Python!
  - nb_of_exercises: 5
    title: Variabili e tipi
---

## Ciao Python!

```yaml
type: VideoExercise
key: f644a48d5d
xp: 50
```

`@projector_key`
d8fcd4c930027fa4e1c3870c7e7e0ff1

---

## Il tuo primo codice Python

```yaml
type: NormalExercise
key: bdc52f0e19
lang: python
xp: 100
skills:
  - 2
```

È ora di eseguire il tuo primo codice Python!

Vai al codice e clicca sul pulsante "Esegui codice" per vedere il risultato.

`@instructions`
- Premi il pulsante "Esegui codice" per vedere il risultato di `print(5 / 8)`.

`@hint`
- Prima di inviare la tua risposta, esegui il codice così avrai tempo di esplorarne l’output.

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
Ex().has_printout(0, not_printed_msg = "__JINJA__:Hai usato `{{sol_call}}` per stampare `5 / 8`?")
success_msg("Ottimo! Passiamo al prossimo!")
```

---

## Python come calcolatrice

```yaml
type: NormalExercise
key: 0f7c039428
lang: python
xp: 100
skills:
  - 2
```

Python è perfetto per fare calcoli di base. Può fare addizioni, sottrazioni, moltiplicazioni e divisioni.

Il codice nello script ti dà qualche esempio.

Ora tocca a te fare pratica scrivendo un po’ di codice.

`@instructions`
- Stampa il risultato della sottrazione di `5` meno `5` in `# Subtraction` usando `print()`.
- Stampa il risultato della moltiplicazione di `3` per `5` in `# Multiplication`.

`@hint`
- Dovrai usare `print()` per generare un output.
- Puoi sottrarre con `-` e moltiplicare con `*`.

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
Ex().has_printout(0, not_printed_msg = "Hai usato `print(4 + 5)` per stampare il risultato della tua somma?")

Ex().has_printout(1, not_printed_msg = "Hai usato `print(5 - 5)` per stampare il risultato della tua sottrazione?")

Ex().has_printout(2, not_printed_msg = "Hai usato `print(3 * 5)` per stampare il risultato della tua moltiplicazione?")

Ex().has_printout(3, not_printed_msg = "Hai usato `print(10 / 2)` per stampare il risultato della tua divisione?")

success_msg("Esatto! Python può aiutarti a fare i calcoli, una caratteristica che sarà utile per l'analisi man mano che svilupperemo le nostre competenze sui dati.")
```

---

## Variabili e tipi

```yaml
type: VideoExercise
key: c2e396792e
xp: 50
```

`@projector_key`
433dcfcfedaee070cbf440491c402e3b

---

## Assegnazione delle variabili

```yaml
type: NormalExercise
key: 4bf65ad83e
lang: python
xp: 100
skills:
  - 2
```

In Python, una variabile ti permette di fare riferimento a un valore con un nome. Per creare una variabile `x` con il valore `5`, usa `=`, come in questo esempio:

```
x = 5
```

Ora puoi usare il nome di questa variabile, `x`, invece del valore vero e proprio, `5`.

Ricorda, in Python `=` indica un’_assegnazione_, non una verifica di uguaglianza! Provalo nell'esercizio sostituendo `____` con il tuo codice.

`@instructions`
- Crea una variabile `savings` con il valore `100`.
- Visualizza questa variabile digitando `print(savings)` nello script.

`@hint`
- Digita `savings = 100` per creare la variabile `savings`.
- Dopo aver creato la variabile `savings`, puoi digitare `print(savings)`.
- Il codice finale non deve contenere alcun `____`.

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
Ex().check_object("savings").has_equal_value(incorrect_msg="Assegna `100` alla variabile `savings`.")
Ex().has_printout(0, not_printed_msg = "Stampa `savings`, la variabile che hai creato, con `print(savings)`.")
success_msg("Ottimo! Proviamo a fare qualche calcolo con questa variabile ora!")
```

---

## Calcoli con variabili

```yaml
type: NormalExercise
key: ff06cedeb4
lang: python
xp: 100
skills:
  - 2
```

Hai appena creato una variabile di risparmio, quindi iniziamo a mettere qualche soldino da parte!

Invece di usare i valori reali, puoi usare delle variabili.

Quanto avresti risparmiato tra quattro mesi se avessi messo da parte $10 ogni mese?

`@instructions`
- Crea una variabile `monthly_savings` uguale a `10` e una variabile `num_months` uguale a `4`.
- Moltiplica `monthly_savings` per `num_months` e assegna il risultato a `new_savings`.
- Stampa il valore di `new_savings`.

`@hint`
- Puoi fare calcoli con le variabili proprio come faresti con i numeri: al posto di scrivere `10 * 4`, usa le variabili!
- Usa `print()` per vedere l'importo in `new_savings`.
- Fai attenzione a scrivere correttamente i nomi delle variabili!

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
Ex().check_object("monthly_savings").has_equal_value(incorrect_msg = "Hai salvato `10` in `monthly_savings` usando `monthly_savings = 10`?")
Ex().check_object("num_months").has_equal_value(incorrect_msg = "Hai salvato `4` in `num_months` usando `num_months = 4`?")
Ex().check_object("new_savings").has_equal_value(incorrect_msg = "Hai usato le variabili e i simboli corretti per moltiplicare? Mi aspettavo `monthly_savings * num_months` ma ho ottenuto qualcos'altro.")
# Ex().check_object("total_savings").has_equal_value(incorrect_msg = "Hai usato le variabili e i simboli corretti per aggiungere? Mi aspettavo `savings + new_savings` ma ho ottenuto qualcos'altro.")

Ex().has_printout(0, not_printed_msg="Ricorda di stampare `new_savings` alla fine del tuo script.")

success_msg("Hai $40 in nuovi risparmi!")
```

---

## Altri tipi di variabili

```yaml
type: NormalExercise
key: 006b48561f
lang: python
xp: 100
skills:
  - 2
```

Nell’esercizio precedente hai lavorato con il tipo di dato intero di Python:

- `int`, o numero intero: un numero senza parte decimale. `savings`, con valore `100`, è un esempio di numero intero.

Oltre ai tipi numerici, ci sono altri tre tipi di dati molto comuni:

- `float`, o floating point: un numero che ha sia una parte intera che una parte decimale, separate da un punto. `1.1`, è un esempio di floating point.
- `str`, o stringa: un tipo che rappresenta il testo. Puoi usare virgolette singole o doppie per creare una stringa.
- `bool`, o booleano: un tipo che rappresenta valori logici. Può essere solo `True` o `False` (la maiuscola conta!).

`@instructions`
- Crea un nuovo float chiamato `half` con valore `0.5`.
- Crea una nuova stringa chiamata `intro` con valore `"Hello! How are you?"`.
- Crea un nuovo valore booleano chiamato`is_good` con valore `True`.

`@hint`
- Per creare una variabile in Python, usa `=`. Assicurati di racchiudere la stringa tra virgolette singole o doppie.
- In Python ci sono solo due valori booleani: `True` e `False`. `TRUE`, `true`, `FALSE`, `false` e altre varianti non sono accettate.

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
Ex().check_object("half").has_equal_value(incorrect_msg = "Hai salvato il float, `0.5` in `half`?")

Ex().check_object("intro").has_equal_value(incorrect_msg = "Hmm, c'è qualcosa di sbagliato nella tua variabile `intro`. Ricontrolla l'ortografia e assicurati di aver usato le virgolette.")

Ex().check_object("is_good").has_equal_value(incorrect_msg = "Hai scritto con la maiuscola il valore booleano? Ricorda che qui non devi usare le virgolette.")

success_msg("Ben fatto!")
```

---

## Operazioni con altri tipi

```yaml
type: BulletExercise
key: 4d0d83cc02
xp: 100
```

In Python esistono diversi tipi di variabili. Puoi vedere il tipo di una variabile usando `type()`. Per esempio, per vedere il tipo di `a`, prova a digitare: `type(a)`.

I diversi tipi si comportano in modo differente in Python. Quando combini due stringhe, per esempio, il comportamento è diverso rispetto a quando sommi due numeri interi o due valori booleani.

È il momento di provarlo.

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
- Somma `savings` e `new_savings`, e assegna il risultato a `total_savings`.
- Usa `type()` per stampare il tipo risultante di `total_savings`.

`@hint`
- Assegna `savings + new_savings` alla nuova variabile `total_savings`.
- Per stampare il tipo di una variabile `x`, usa `print(type(x))`.

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
msg = "Non devi cambiare o rimuovere le variabili predefinite."

Ex().multi(
    check_object('savings', missing_msg=msg).has_equal_value(incorrect_msg=msg),
    check_object('new_savings', missing_msg=msg).has_equal_value(incorrect_msg=msg)
)

Ex().multi(
    check_object("total_savings").has_equal_value(incorrect_msg="Somma `savings` e `new_savings` per creare la variabile `total_savings`."),
    has_printout(1, not_printed_msg = "__JINJA__:Usa `{{sol_call}}` per stampare il tipo di `total_savings`.")
)
```

***

```yaml
type: NormalExercise
key: f54fbf9bd9
xp: 50
```

`@instructions`
- Calcola la somma di `intro` ed `intro`, e assegna il risultato a `doubleintro`.
- Stampa `doubleintro`. Te lo aspettavi?

`@hint`
- Assegna `intro + intro` alla nuova variabile `doubleintro`.
- Per stampare una variabile `x`, digita `print(x)` nello script.

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
msg = "Non devi cambiare o rimuovere le variabili predefinite."

Ex().check_object('intro', missing_msg=msg).has_equal_value(incorrect_msg=msg)

Ex().multi(
    check_object("doubleintro").has_equal_value(incorrect_msg  = "Hai memorizzato il risultato di `intro + intro` in `doubleintro`?"),
    has_printout(0, not_printed_msg = "Non dimenticare di stampare `doubleintro`.")
)

success_msg("Ben fatto. Nota come `intro + intro` fa sì che `\"Hello! How are you?\"` e `\"Hello! How are you?\"` vengano incollati insieme.")
```

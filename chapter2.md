---
title_meta: Capitolo 2
title: Liste in Python
description: >-
  Impara a memorizzare, accedere e manipolare dati nelle liste: il primo passo
  per lavorare in modo efficiente con grandi quantità di dati.
attachments:
  slides_link: 'https://projector-video-pdf-converter.datacamp.com/735/chapter2.pdf'
lessons:
  - nb_of_exercises: 4
    title: Liste in Python
  - nb_of_exercises: 4
    title: Sottoinsiemi di liste
  - nb_of_exercises: 5
    title: Come gestire le liste
---

## Liste in Python

```yaml
type: VideoExercise
key: a5886d213f
xp: 50
```

`@projector_key`
a0530c4542f10988847b2dbb91f717c3

---

## Creare una lista

```yaml
type: NormalExercise
key: e6c527bf41
lang: python
xp: 100
skills:
  - 2
```

Una lista è un **tipo di dato composto**; puoi raggruppare insieme diversi valori, come in questo esempio:

```
a = "is"
b = "nice"
my_list = ["my", "list", a, b]
```

Dopo aver misurato l'altezza dei tuoi familiari, decidi di raccogliere alcune informazioni sulla casa in cui vivi. Le superfici delle diverse parti della casa sono memorizzate in variabili separate nell'esercizio.

`@instructions`
- Crea la lista `areas`, che contenga l’area del corridoio (`hall`), della cucina (`kit`), del soggiorno (`liv`), della camera da letto (`bed`) e del bagno (`bath`), in quest'ordine. Usa le variabili predefinite.
- Stampa `areas` usando la funzione `print()`.

`@hint`
- Puoi usare le variabili già create per costruire la lista: `areas = [hall, kit, ...]`.
- Assicurati di usare le parentesi quadre `[]` invece delle parentesi tonde `()`.
- Non è necessario usare le virgolette quando inserisci variabili all’interno di una lista.
- Digita `print(areas)` per stampare la lista quando invii la risposta.

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
predef_msg = "Non rimuovere o modificare le variabili predefinite!"
areas_msg = "Definisci `areas` come la lista contenente tutte le variabili di area, nell'ordine corretto: `[hall, kit, liv, bed, bath]`. Attento agli errori di battitura. La lista non dovrebbe contenere nient'altro!"

Ex().check_correct(
    has_printout(0, not_printed_msg = "__JINJA__:Hai usato `{{sol_call}}` per stampare la lista `areas` alla fine del tuo script?"),
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

success_msg("Ottimo! Una lista è decisamente meglio qui, vero?")
```

---

## Creare liste con tipi diversi

```yaml
type: NormalExercise
key: 1702a8bcdc
lang: python
xp: 100
skills:
  - 2
```

Anche se non è molto comune, una lista può contenere un mix di tipi Python, come stringhe, float e booleani.

Ora aggiungerai i nomi delle stanze alla lista, così potrai vedere facilmente sia il nome che le dimensioni di ogni stanza.

Ti abbiamo fornito un po’ di codice per aiutarti a iniziare. Attenzione! `"bathroom"` è una stringa, mentre `bath` è una variabile che rappresenta il float `9.50` che hai specificato prima.

`@instructions`
- Completa il codice che crea la lista `areas`. Costruisci la lista in modo che contenga prima il nome di ogni stanza come stringa, seguito dalla sua superficie. In altre parole, aggiungi le stringhe `"hallway"`,`"kitchen"` e `"bedroom"` nelle posizioni corrette.
- Stampa di nuovo `areas`: il risultato è più chiaro questa volta?

`@hint`
- I primi quattro elementi della lista `areas` sono codificati come `["hallway", hall, "kitchen", kit, ...`.
- Le stringhe devono essere racchiuse tra virgolette `""`.

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
predef_msg = "Non rimuovere o modificare le variabili predefinite!"
areas_msg = "Non hai assegnato il valore corretto a `areas`. Dai un'altra occhiata alle istruzioni. Assicurati di mettere il nome della stanza prima della variabile che contiene l'area ogni volta. L'ordine è importante qui! Attento agli errori di battitura."

Ex().check_correct(
  check_object("areas").has_equal_value(incorrect_msg = areas_msg),
  multi([ check_object(obj, missing_msg = predef_msg).has_equal_value(incorrect_msg = predef_msg) for obj in objs])
)

Ex().has_printout(0, not_printed_msg = "__JINJA__:Hai usato `{{sol_call}}` per stampare la lista `areas` alla fine del tuo script?")

success_msg("Ottimo! Questa lista contiene sia stringhe che numeri decimali, ma non è un problema per Python!")
```

---

## Lista di liste

```yaml
type: NormalExercise
key: 9158c577b0
lang: python
xp: 100
skills:
  - 2
```

Come data scientist, ti capiterà spesso di lavorare con molti dati, e può avere senso raggrupparne alcuni.

Invece di creare una lista con stringhe e float, che rappresentano i nomi e le superfici delle stanze di casa tua, puoi creare una lista di liste.

Ricorda: `"hallway"` è una stringa, mentre `hall` è una variabile che rappresenta il float `11.25` che hai specificato prima.

`@instructions`
- Completa la lista di liste in modo che includa anche i dati della camera da letto e del bagno. Assicurati di inserirli nell'ordine giusto!
- Stampa `house`. Questo modo di organizzare i dati ti sembra più chiaro?

`@hint`
- Aggiungi delle _sottoliste_ alla lista `house` mettendo `["bedroom", bed]` e `["bathroom", bath]` tra parentesi quadre.
- Ricordati di separare ogni sottolista con una virgola `,`.
- Per stampare una variabile `x`, scrivi `print(x)` su una nuova riga.

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
predef_msg = "Non rimuovere o modificare le variabili predefinite!"
house_msg = "Non hai assegnato il valore corretto a `house`. Dai un'altra occhiata alle istruzioni. Estendi l'elenco di elenchi in modo che incorpori un elenco per ogni coppia di nome stanza e area stanza. Fai attenzione all'ordine e agli errori di battitura!"

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

Ex().has_printout(0, not_printed_msg = "__JINJA__:Hai usato `{{sol_call}}` per stampare il contenuto di `house`?")

success_msg("Ottimo! Preparati a imparare il sottoinsieme delle liste!")
```

---

## Sottoinsiemi di liste

```yaml
type: VideoExercise
key: c076b5a69c
xp: 50
```

`@projector_key`
fc15ba5cb9485456df8589130b519ea3

---

## Dividi (in sottoinsiemi) e conquista

```yaml
type: NormalExercise
key: c3ce582e32
lang: python
xp: 100
skills:
  - 2
```

Creare sottoinsiemi di liste in Python è un gioco da ragazzi. Ecco un esempio di codice che crea una lista `x`, seleziona al suo interno l’elemento “b”. Ricorda che questo è il secondo elemento, quindi ha indice 1. Puoi anche usare l'indicizzazione negativa.

```
x = ["a", "b", "c", "d"]
x[1]
x[-3] # same result!
```

Ricordi la lista `areas` di prima, che contiene sia stringhe che float? La sua definizione è già nello script. Riesci ad aggiungere il codice giusto per fare un po’ di slicing in Python?

`@instructions`
- Stampa il secondo elemento della lista `areas` (il cui valore è `11.25`).
- Crea un sottoinsieme e stampa l'ultimo elemento di `areas`, che è `9.50`. In questo caso, ha senso usare un indice negativo!
- Seleziona il numero che rappresenta la superficie del soggiorno (`20.0`) e stampalo.

`@hint`
- Usa `x[1]` per selezionare il secondo elemento della lista `x`.
- Usa `x[-1]` per selezionare l'ultimo elemento della lista `x`.
- Assicurati di racchiudere le operazioni di slicing in una chiamata `print()`.
- Il numero che rappresenta la superficie del soggiorno è il 6º elemento della lista, quindi qui ti serve `[5]`. `area[4]` mostrerebbe invece la stringa!

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
msg = "Non rimuovere o modificare la lista `areas` predefinita."
Ex().check_object("areas", missing_msg = msg).has_equal_value(incorrect_msg = msg)
Ex().has_printout(0, not_printed_msg = "Dai un'altra occhiata al tuo codice per stampare il secondo elemento in `areas`, che si trova all'indice `1`.")
Ex().has_printout(1, not_printed_msg = "Dai un'altra occhiata al tuo codice per stampare l'ultimo elemento in `areas`, che si trova all'indice `-1`.")
Ex().has_printout(2, not_printed_msg = "Dai un'altra occhiata al tuo codice per stampare l'area del soggiorno. Si trova all'indice `5`.")
success_msg("Ottimo lavoro!")
```

---

## Slicing and dicing

```yaml
type: NormalExercise
key: 7f08642d18
lang: python
xp: 100
skills:
  - 2
```

Selezionare singoli valori da una lista è solo una parte del lavoro. Puoi anche _fare uno slicing_ della tua lista, cioè selezionare più elementi contemporaneamente. Usa questa sintassi:

```
my_list[start:end]
```

L’indice `start` sarà incluso, mentre quello `end` _non_ sarà incluso. Comunque, puoi anche non specificare questi indici. Se non specifichi l’indice `start`, Python capisce che vuoi iniziare lo slicing dall’inizio della lista.

`@instructions`
- Usa il slicing per creare una lista chiamata `downstairs`, che contenga i primi 6 elementi di `areas`.
- Crea `upstairs`, prendendo gli ultimi `4` elementi di `areas`. Questa volta, semplifica lo slicing omettendo l’indice `end`.
- Stampa sia `downstairs` che `upstairs` usando `print()`.

`@hint`
- Usa le parentesi quadre `[0:6]` per ottenere i primi sei elementi di una lista.
- Per ottenere tutti gli elementi tranne i primi 5, `l`, dovresti usare `l[5:]`.
- Aggiungi due chiamate `print()` per stampare `downstairs` e `upstairs`.

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
msg = "Non rimuovere o modificare la lista `areas` predefinita."
Ex().check_object("areas", missing_msg = msg).has_equal_value(incorrect_msg = msg)

patt = "`%s` è errato. Usa `areas[%s]` e slicing per selezionare gli elementi che vuoi, o qualcosa di equivalente."
Ex().check_object("downstairs").has_equal_value(incorrect_msg = patt % ('downstairs', '0:6'))
Ex().check_object("upstairs").has_equal_value(incorrect_msg = patt % ("upstairs",":6"))

Ex().has_printout(0, not_printed_msg="Hai stampato `downstairs` dopo averlo calcolato?")
Ex().has_printout(1, not_printed_msg="Hai stampato `upstairs` dopo averlo calcolato?")

success_msg("Ottimo!")
```

---

## Sottoinsiemi di liste di liste

```yaml
type: NormalExercise
key: dbbbd306cf
xp: 100
```

Una lista Python può anche contenere altre liste.

Per creare sottoinsiemi di liste di liste (o liste annidate), puoi usare la stessa tecnica di prima: le parentesi quadre. Per una lista `house`, sarebbe qualcosa del genere:

```
house[2][0]
```

`@instructions`
- Seleziona `house` dalla lista per ottenere il float `9.5`.

`@hint`
- Analizziamo passo per passo. Prima devi arrivare all'ultimo elemento della lista `["bathroom", 9.50]`. Ricorda che l'indice dell'ultimo elemento è `-1`.
- Poi vuoi ottenere il secondo elemento di `["bathroom", 9.50]`, che si trova all'indice `1`.

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

success_msg("Corretto! L'ultimo pezzo del puzzle della lista è la manipolazione.")
```

---

## Come gestire le liste

```yaml
type: VideoExercise
key: d7fe818b3a
xp: 50
```

`@projector_key`
355ed52d2fb0d67508c6a311b7cbc6d3

---

## Sostituire elementi da una lista

```yaml
type: NormalExercise
key: 4e1bba1b55
lang: python
xp: 100
skills:
  - 2
```

Per sostituire gli elementi di una lista, devi creare un sottoinsieme e assegnarvi nuovi valori. Puoi modificare singoli elementi oppure cambiare intere sezioni della lista in una volta sola.

In questo e nei prossimi esercizi continuerai a lavorare sulla lista `areas`, che contiene i nomi e le superfici delle diverse stanze di una casa.

`@instructions`
- Aggiorna la superficie del bagno a `10.50` metri quadrati invece di `9.50` usando l'indicizzazione negativa.
- Rendi più trendy la lista `areas`! Cambia `"living room"` in `"chill zone"`. Questa volta non usare l’indicizzazione negativa.

`@hint`
- Per aggiornare la superficie del bagno, individua il sottoinsieme che la contiene (è l’ultimo elemento della lista).
- Poi, sostituisci quel valore con la nuova superficie assegnandolo a quel sottoinsieme.
- Fai lo stesso per aggiornare il nome di `"living room"`, che si trova all'indice 4.

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
bathroom_msg = 'Puoi usare `areas[-1] = 10.50` per aggiornare l\'area del bagno.'
chillzone_msg = 'Puoi usare `areas[4] = "chill zone"` per aggiornare il nome del soggiorno.'
Ex().check_correct(
  check_object('areas').has_equal_value(incorrect_msg = 'Le tue modifiche a `areas` non hanno prodotto la lista corretta. Sei sicuro di aver usato le operazioni di sottoinsieme corrette? In caso di dubbio, puoi usare un suggerimento!'),
  multi(
    has_equal_value(expr_code='areas[-1]', override=10.50, incorrect_msg = bathroom_msg),
    has_equal_value(expr_code='areas[4]', override='chill zone', incorrect_msg = chillzone_msg),
  )
)
success_msg('Fantastico! Come mostrato nell\'esempio di codice, puoi anche affettare una lista e sostituirla con un\'altra lista per aggiornare più elementi in un unico comando.')
```

---

## Ampliare una lista

```yaml
type: NormalExercise
key: ff0fe8d967
lang: python
xp: 100
skills:
  - 2
```

Se puoi modificare gli elementi di una lista, probabilmente vorrai anche aggiungerne di nuovi, giusto? Puoi farlo usando l’operatore `+`:

```
x = ["a", "b", "c", "d"]
y = x + ["e", "f"]
```

Hai appena vinto alla lotteria, fantastico! Hai deciso di costruire una casetta per la piscina e un garage. Riesci ad aggiungere queste informazioni alla lista `areas`?

`@instructions`
- Usa l'operatore `+` per concatenare la lista `["poolhouse", 24.5]` alla fine della lista `areas`. Salva la lista risultante come `areas_1`.
- Amplia ulteriormente `areas_1` aggiungendo i dati del tuo garage. Aggiungi la stringa `"garage"` e il float `15.45`. Assegna alla lista risultante il nome di `areas_2`.

`@hint`
- Segui l’esempio di codice nell’esercizio. Qui `x` è `areas`, `["e", "f"]` è `["poolhouse", 24.5]`.
- Per aggiungere altri elementi a `areas_1`, usa `areas_1 + ["element", 123]`.

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
msg = "Non rimuovere o modificare la lista `areas` predefinita."
Ex().check_object("areas", missing_msg = msg).has_equal_value(incorrect_msg = msg)
Ex().check_object("areas_1").has_equal_value(incorrect_msg = "Usa `areas + [\"poolhouse\", 24.5]` per creare `areas_1`. Attento agli errori di battitura!")
Ex().check_object("areas_2").has_equal_value(incorrect_msg = "Usa `areas_1 + [\"garage\", 15.45]` per creare `areas_2`. Attento agli errori di battitura!")
success_msg("Forte! La lista sta prendendo forma alla grande!")
```

---

## Rimuovere elementi da una lista

```yaml
type: NormalExercise
key: 85f792356e
xp: 100
```

Infine, puoi anche rimuovere elementi dalla tua lista. Per farlo, usa l'istruzione `del`:

```
x = ["a", "b", "c", "d"]
del x[1]
```

Attenzione: appena rimuovi un elemento da una lista, gli indici degli elementi successivi cambiano!

Purtroppo, la somma che hai vinto alla lotteria non è così alta e sembra che la casetta in giardino non si farà più. Dovrai rimuoverla dalla lista. Decidi di rimuovere la stringa e il float corrispondenti dalla lista `areas`.

`@instructions`
- Rimuovi la stringa e il float per `"poolhouse"` dalla tua lista `areas`.
- Stampa la lista aggiornata `areas`.

`@hint`
- Dovrai usare due volte `del` per eliminare due elementi. Fai attenzione al cambiamento degli indici!

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

Ex().has_printout(0, not_printed_msg="Hai stampato `areas` dopo aver rimosso la stringa e il float di poolhouse?")
success_msg("Corretto! Imparerai modi più semplici per rimuovere elementi specifici dalle liste Python più avanti.")
```

---

## Come funzionano le liste

```yaml
type: NormalExercise
key: af72db9915
lang: python
xp: 100
skills:
  - 2
```

In questo esercizio ti è già stato fornito del codice: una lista chiamata `areas` e una copia chiamata `areas_copy`.

Al momento, il primo elemento nella lista `areas_copy` è stato modificato e viene stampata la lista `areas`. Se clicchi sul pulsante "Esegui codice", vedrai che, anche se hai modificato `areas_copy`, la modifica si applica anche alla lista `areas`. Questo perché `areas` e `areas_copy` puntano alla stessa lista.

Se vuoi evitare che le modifiche in `areas_copy` vengano applicate anche in `areas`, devi fare una copia più esplicita della lista `areas` con `list()` o usando `[:]`.

`@instructions`
- Modifica il secondo comando che crea la variabile`areas_copy`, in modo che `areas_copy` sia una copia esplicita di `areas`. Dopo questo cambio, le modifiche apportate a `areas_copy` non dovrebbero influire su `areas`. Invia la risposta per verificare.

`@hint`
- Modifica la chiamata `areas_copy = areas`. Invece di usare `areas`, puoi usare `list(areas)` o `areas[:]`.

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
  check_object("areas_copy").has_equal_value(incorrect_msg = "Sembra che `areas_copy` non sia stato aggiornato correttamente."),
  check_function("list", missing_msg = "Assicurati di usare `list(areas)` per creare un `areas_copy`.")
)

mmsg = "Non rimuovere la lista `areas` predefinita."
imsg = "Assicurati di modificare SOLO la copia, non la lista `areas` originale. Dai un'altra occhiata alla descrizione dell'esercizio se non sei sicuro di come creare una copia."
Ex().check_correct(
  check_object("areas", missing_msg = mmsg).has_equal_value(incorrect_msg = imsg),
  check_function("list", missing_msg = "Assicurati di usare `list(areas)` per creare un `areas_copy`.")
)

success_msg("Ben fatto! La differenza tra copie esplicite e basate su riferimento è sottile, ma può essere davvero importante. Cerca di tenere a mente come una lista è memorizzata nella memoria del computer.")
```

---
title_meta: Capitolo 4
title: NumPy
description: >-
  NumPy è un pacchetto Python fondamentale per fare data science in modo
  efficiente. Impara a usare i potenti strumenti degli array NumPy e inizia a
  esplorare i dati.
attachments:
  slides_link: 'https://projector-video-pdf-converter.datacamp.com/735/chapter4.pdf'
lessons:
  - nb_of_exercises: 5
    title: Numpy
  - nb_of_exercises: 5
    title: Array Numpy 2D
  - nb_of_exercises: 3
    title: 'Numpy: Statistiche di base'
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

## Il tuo primo array NumPy

```yaml
type: NormalExercise
key: 84cab9d170
lang: python
xp: 100
skills:
  - 2
```

Ora ti immergerai nel mondo del baseball. Lungo il percorso, acquisirai familiarità con le nozioni di base di `numpy`, un potente pacchetto per la data science.

Nello script Python è già stata definita una lista chiamata `baseball` che contiene l’altezza in centimetri di alcuni giocatori di baseball. Riesci ad aggiungere del codice per creare un array `numpy` a partire da essa?

`@instructions`
- Importa il pacchetto `numpy` come `np`, così potrai fare riferimento a `numpy` con `np`.
- Usa `np.array()` per creare un array `numpy` da `baseball`. Assegna a questo array il nome di `np_baseball`.
- Stampa il tipo di `np_baseball` per verificare che sia corretto.

`@hint`
- `import numpy as np` farà al caso tuo. Ora, devi usare `np.fun_name()` ogni volta che vuoi utilizzare una funzione `numpy`.
- `np.array()` dovrebbe accettare l'input `baseball`. Assegna il risultato della chiamata a `np_baseball`.
- Per stampare il tipo di una variabile `x`, basta scrivere `print(type(x))`.

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
predef_msg = "Non devi cambiare o rimuovere le variabili predefinite."
Ex().has_import("numpy")
Ex().check_correct(
  check_object("np_baseball"),
  multi(
    check_object("baseball", missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
    check_function("numpy.array").check_args(0).has_equal_ast()
  )
)

Ex().has_printout(0)
success_msg("Ottimo lavoro!")
```

---

## L’altezza dei giocatori di baseball

```yaml
type: NormalExercise
key: e7e25a89ea
lang: python
xp: 100
skills:
  - 2
```

Sei un grande appassionato di baseball. Decidi di contattare la MLB (Major League Baseball) per raccogliere altri dati sull’altezza dei principali giocatori. Ti forniscono i dati su più di mille giocatori, memorizzati come una normale lista Python: `height_in`. L’altezza è espressa in pollici. Riesci a creare un array `numpy` e convertire le unità in metri?

`height_in` è a tua disposizione e il pacchetto `numpy` è già stato caricato, quindi puoi iniziare subito (Fonte: stat.ucla.edu).

`@instructions`
- Crea un array `numpy` da `height_in`. Assegna a questo nuovo array il nome di `np_height_in`.
- Stampa `np_height_in`.
- Moltiplica `np_height_in` per `0.0254`, per convertire tutte le misure di altezza da pollici a metri. Salva i nuovi valori in un nuovo array chiamato `np_height_m`.
- Stampa `np_height_m` e verifica se il risultato ha senso.

`@hint`
- Usa `np.array()` e passagli `height`. Salva il risultato in `np_height_in`.
- Per stampare una variabile `x`, scrivi `print(x)` nello script Python.
- Esegui i calcoli come se `np_height_in` fosse un numero singolo: `np_height_in * conversion_factor` fa parte della risposta.
- Per stampare una variabile `x`, scrivi `print(x)` nello script Python.

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
  check_object("np_height_m").has_equal_value(incorrect_msg = "Usa `np_height_in * 0.0254` per calcolare `np_height_m`.")
)

success_msg("Ottimo! In un batter d'occhio, `numpy` esegue moltiplicazioni su più di 1000 misurazioni di altezza.")
```

---

## Effetti collaterali di NumPy

```yaml
type: MultipleChoiceExercise
key: 3662ff6637
lang: python
xp: 50
skills:
  - 2
```

`numpy` è perfetto per fare aritmetica vettoriale. Se confronti come funziona con le normali liste Python, però, ci sono alcune differenze.

Prima di tutto, gli array`numpy` non possono contenere elementi di tipi diversi. Se metti insieme tipi diversi, per esempio booleani e interi,`numpy` li trasforma automaticamente in un tipo comune. I valori booleani come`True`  e`False`  vengono considerati come `1` e `0` quando sono insieme ai numeri, quindi l'array finisce per essere composto da numeri interi.

In secondo luogo, gli operatori aritmetici tipici, come `+`, `-`, `*` e `/` hanno un significato diverso per le liste Python regolari e gli array `numpy`.

Scegli il codice che ti dà questo risultato:

```
np.array([True, 1, 2]) + np.array([3, 4, False])
```

Il pacchetto `numpy` è già stato importato come `np`. Puoi provare ogni opzione nella shell IPython per vedere il risultato.

`@possible_answers`
- `np.array([True, 1, 2, 3, 4, False])`
- `np.array([4, 3, 0]) + np.array([0, 2, 2])`
- `np.array([1, 1, 2]) + np.array([3, 4, -1])`
- `np.array([0, 1, 2, 3, 4, 5])`

`@hint`
- Copia i vari blocchi di codice e incollali nella shell IPython. Premi **Invio** per eseguire il codice e vedere quale output corrisponde a quello generato da `np.array([True, 1, 2]) + np.array([3, 4, False])`.

`@pre_exercise_code`
```{python}
import numpy as np
```

`@sct`
```{python}
msg1 = msg3 = msg4 = "Non corretto. Prova i diversi blocchi di codice e vedi quale corrisponde al blocco di codice di destinazione."
msg2 = "Ottimo lavoro! `True` è convertito in 1, `False` è convertito in 0."
Ex().has_chosen(2, [msg1, msg2, msg3, msg4])
```

---

## Sottoinsieme di array NumPy

```yaml
type: NormalExercise
key: fcb2a9007b
lang: python
xp: 100
skills:
  - 2
```

Il sottoinsieme (usando le parentesi quadre su liste o array) funziona esattamente allo stesso modo sia con le liste che con gli array.

In questo esercizio sono già state caricate due liste Python regolari, `height_in` e `weight_lb`, contenenti l'altezza e il peso dei giocatori della MLB. Ci sono, inoltre, due liste di array `numpy`, `np_weight_lb` e `np_height_in`, a tua disposizione.

`@instructions`
- Crea un sottoinsieme di `np_weight_lb` stampando l'elemento all'indice 50.
- Stampa un sottoarray di `np_height_in` che contiene gli elementi dall'indice 100 fino all'indice 110 **compreso**.

`@hint`
- Assicurati di racchiudere le operazioni di sottoinsieme in una chiamata a `print()`.
- Usa `[100:111]` per prendere gli elementi dall'indice 100 fino all'indice 110 compreso.

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
msg = "Non devi cambiare o rimuovere le variabili predefinite."
Ex().multi(
    check_object("np_height_in", missing_msg=msg).has_equal_value(incorrect_msg=msg),
    check_object("np_weight_lb", missing_msg=msg).has_equal_value(incorrect_msg=msg)
)

Ex().has_printout(0)
Ex().has_printout(1)

success_msg("Ottimo! È ora di imparare qualcosa di nuovo: array NumPy 2D!")
```

---

## Array NumPy 2D

```yaml
type: VideoExercise
key: 1241efac7a
xp: 50
```

`@projector_key`
ae3238dcc7feb9adecfee0c395fc8dc8

---

## Il tuo primo array NumPy 2D

```yaml
type: NormalExercise
key: 5cb045bb13
lang: python
xp: 100
skills:
  - 2
```

Prima di lavorare sui dati reali della MLB, proviamo a creare un array `numpy` 2D da una piccola lista di liste.

In questo esercizio, `baseball` è una lista di liste. La lista principale ha 4 elementi. Ognuno di questi elementi è una lista che contiene l'altezza e il peso di 4 giocatori di baseball, in quest’ordine. `baseball` è già definito nello script.

`@instructions`
- Usa `np.array()` per creare un array `numpy` 2D da `baseball`. Assegnagli il nome `np_baseball`.
- Stampa il tipo di `np_baseball`.
- Stampa l'attributo `shape` di `np_baseball`. Usa `np_baseball.shape`.

`@hint`
- `baseball` è già definito nello script. Chiama `np.array()` e salva l'array `numpy` 2D risultante in `np_baseball`.
- Usa `print()` insieme a `type()` per la seconda istruzione.
- `np_baseball.shape` ti fornirà le dimensioni di `np_baseball`. Assicurati di racchiudere tutto in una chiamata a `print()`.

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
msg = "Non devi cambiare o rimuovere le variabili predefinite."
Ex().check_object("baseball", missing_msg=msg).has_equal_value(incorrect_msg=msg)
Ex().has_import("numpy", same_as=False)

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

success_msg("Ottimo! Ora sei pronto per convertire i dati effettivi della MLB in un array 2D `numpy`!")
```

---

## Dati sul baseball in formato 2D

```yaml
type: NormalExercise
key: 5df25d0b7b
lang: python
xp: 100
skills:
  - 2
```

Ti rendi conto che ha più senso riorganizzare tutte queste informazioni in un array `numpy` 2D.

Hai a disposizione una lista di liste Python. In questa lista di liste, ogni sottolista rappresenta l’altezza e il peso di un singolo giocatore di baseball. Il nome di questa lista è `baseball` ed è già stata caricata per te (anche se non puoi vederla).

Salva i dati come un array 2D per sbloccare le funzionalità avanzate di `numpy`.

`@instructions`
- Usa `np.array()` per creare un array `numpy` 2D da `baseball`. Assegnagli il nome `np_baseball`.
- Stampa l'attributo `shape` di `np_baseball`.

`@hint`
- `baseball` è già disponibile nell'ambiente Python. Chiama `np.array()` e salva l'array `numpy` 2D risultante in `np_baseball`.
- `np_baseball.shape` ti restituirà le dimensioni di `np_baseball`. Assicurati di racchiudere tutto in una chiamata a `print()`.

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

success_msg("Fantastico! È ora di mostrare alcune caratteristiche straordinarie degli array multi-dimensionali di `numpy`!")
```

---

## Sottoinsieme di array NumPy 2D

```yaml
type: NormalExercise
key: aeca4977f0
lang: python
xp: 100
skills:
  - 2
```

Se il tuo array `numpy` 2D ha una struttura regolare (cioè ogni riga e colonna ha un numero fisso di valori), le operazioni complesse di sottoinsiemi diventano molto più semplici. Dai un'occhiata al codice qui sotto, dove gli elementi `"a"` e `"c"` vengono estratti da una lista di liste.

```
# numpy
import numpy as np
np_x = np.array(x)
np_x[:, 0]
```

Gli indici prima della virgola si riferiscono alle righe, mentre quelli dopo la virgola si riferiscono alle colonne. `:` serve per fare slicing; nell’esempio dice a Python di includere tutte le righe.

`@instructions`
- Stampa la riga numero 50 di `np_baseball`.
- Crea una nuova variabile `np_weight_lb`, contenente l’intera seconda colonna di `np_baseball`.
- Scegli l'altezza (prima colonna) del 124° giocatore di baseball in `np_baseball` e stampala.

`@hint`
- Hai bisogno dell'indice di riga 49 nella prima istruzione! Più precisamente, usa `[49, :]`.
- Per selezionare tutta la seconda colonna, usa `[:, 1]`.
- Per l'ultima istruzione, usa `[123, 0]`; non dimenticare di racchiuderlo in un’istruzione `print()`.

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
msg = "Non devi cambiare o rimuovere le variabili predefinite."
Ex().multi(
    has_import("numpy", same_as = False),
    check_object("np_baseball", missing_msg=msg).has_equal_value(incorrect_msg = msg)
)

Ex().has_printout(0)

Ex().check_object('np_weight_lb').has_equal_value(incorrect_msg = "Puoi usare `np_baseball[:,1]` per definire `np_weight_lb`. Questo selezionerà l'intera prima colonna.")

Ex().has_printout(1)

success_msg("Sta andando bene!")
```

---

## Aritmetica 2D

```yaml
type: NormalExercise
key: 1c2378b677
lang: python
xp: 100
skills:
  - 2
```

Gli array `numpy` 2D possono fare calcoli elemento per elemento, proprio come gli array `numpy`.

`np_baseball` è già stato definito per te; si tratta nuovamente di un array `numpy` 2D con 3 colonne, che rappresentano l'altezza (in pollici), il peso (in libbre) e l'età (in anni). A tua disposizione trovi `baseball` come una lista di liste regolare e `updated` come un array numpy 2D.

`@instructions`
- Sei riuscito a trovare i cambiamenti di altezza, peso ed età di tutti i giocatori di baseball, disponibili come array `numpy` 2D `updated`. Aggiungi `np_baseball` e `updated`, e stampa il risultato.
- Vuoi convertire le unità di misura dell'altezza e del peso in unità metriche (rispettivamente, metri e chilogrammi). Per prima cosa, crea un array `numpy` con tre valori: `0.0254`, `0.453592` e `1`. Assegna a questo array il nome di `conversion`.
- Moltiplica `np_baseball` per `conversion` e stampa il risultato.

`@hint`
- `np_baseball + updated` eseguirà una somma elemento per elemento dei due array `numpy`.
- Crea un array `numpy` con `np.array()`; l'input è una lista Python regolare con tre elementi.
- `np_baseball * conversion` funzionerà senza ulteriori modifiche. Provalo! Assicurati di racchiuderlo in una chiamata a `print()`.

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

msg = "Non devi cambiare o rimuovere le variabili predefinite."
Ex().check_object("np_baseball", missing_msg=msg).has_equal_value(incorrect_msg=msg)

Ex().has_printout(0)

Ex().check_correct(
    has_printout(1),
    check_correct(
        check_object('conversion').has_equal_value(),
        check_function('numpy.array', index=1).check_args(0).has_equal_value()
    )    
)

success_msg("Ottimo lavoro! Nota come con pochissimo codice puoi cambiare tutti i valori nella tua struttura dati `numpy` in un modo molto specifico. Questo sarà molto utile nel tuo futuro come data scientist!")
```

---

## NumPy: Statistiche di base

```yaml
type: VideoExercise
key: 287995e488
xp: 50
```

`@projector_key`
34495ba457d74296794d2a122c9b6e19

---

## Media vs. mediana

```yaml
type: NormalExercise
key: 509c588eb6
lang: python
xp: 100
skills:
  - 2
```

Ora sai come usare le funzioni di `numpy` per capire meglio i tuoi dati. 

I dati sul baseball sono disponibili in un array `numpy` 2D con 3 colonne (altezza, peso, età) e 1015 righe. Il nome di questo array `numpy` è `np_baseball`. Dopo aver sistemato i dati, però, noti che alcuni valori di altezza sono anormalmente alti. Segui le istruzioni e scopri quale statistica riassuntiva è più adatta se hai a che fare con i cosiddetti _outlier_ (valori anomali). `np_baseball` è a tua disposizione.

`@instructions`
- Crea un array `numpy` chiamato `np_height_in` uguale alla prima colonna di `np_baseball`.
- Stampa la media di `np_height_in`.
- Stampa la mediana di `np_height_in`.

`@hint`
- Usa il sottogruppo `numpy` 2D: `[:,0]` è parte della soluzione.
- Se importi `numpy` come `np`, puoi usare `np.mean()` per calcolare la media di un array NumPy. Non dimenticare di inserire una chiamata a `print()`.
- Per l'ultima istruzione, usa `np.median()`.

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

Ex().check_object("np_height_in").has_equal_value(incorrect_msg = "Puoi usare `np_baseball[:,0]` per selezionare la prima colonna da `np_baseball`"),

Ex().check_correct(
    has_printout(0),
    check_function('numpy.mean').has_equal_value()
)

Ex().check_correct(
    has_printout(1),
    check_function('numpy.median').has_equal_value()
)

success_msg("Un'altezza media di 1586 pollici, non suona giusto, vero? Tuttavia, la mediana non sembra essere influenzata dai valori anomali: 74 pollici ha perfettamente senso. È sempre una buona idea controllare sia la mediana che la media, per avere un'idea della distribuzione complessiva dell'intero dataset.")
```

---

## Esplorare i dati sul baseball

```yaml
type: NormalExercise
key: '4409948807'
lang: python
xp: 100
skills:
  - 2
```

Poiché media e mediana sono così distanti, decidi di segnalare l’errore alla MLB. Trovano l’errore e ti inviano i dati corretti. `np_baseball` è di nuovo disponibile come array NumPy 2D, con tre colonne.

Lo script Python nell’editor include già il codice per stampare messaggi informativi con le diverse statistiche riassuntive, e `numpy` è già caricato come `np`. Riesci a completare il lavoro? `np_baseball` è a tua disposizione.

`@instructions`
- Il codice per stampare l'altezza media è già incluso. Completa il codice per calcolare l’altezza mediana.
- Usa `np.std()` sulla prima colonna di `np_baseball` per calcolare `stddev`. 
- I giocatori più grandi tendono a essere più pesanti? Usa `np.corrcoef()` per memorizzare la correlazione tra la prima e la seconda colonna di `np_baseball` in `corr`.

`@hint`
- Usa `np.median()` per calcolare la mediana. Assicurati di selezionare prima la colonna corretta!
- Seleziona la stessa colonna quando calcoli la deviazione standard con `np.std()`.
- Usa `np_baseball[:, 0]` e `np_baseball[:, 1]` per selezionare la prima e la seconda colonna; questi sono gli input per `np.corrcoef()`.

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
msg = "Non dovresti cambiare o rimuovere la variabile `avg` predefinita."
Ex().check_object("avg", missing_msg=msg).has_equal_value(incorrect_msg=msg)

missing = "Hai usato `np.median()` per calcolare la mediana?"
incorrect = "Per calcolare `med`, passa la prima colonna di `np_baseball` a `numpy.median()`. L'esempio di `np.mean()` mostra come si fa."
Ex().check_correct(
  check_object("med").has_equal_value(),
  check_function("numpy.median", index=0, missing_msg=missing).check_args(0).has_equal_value(incorrect_msg=incorrect)
)

missing = "Hai usato `np.std()` per calcolare la deviazione standard?"
incorrect = "Per calcolare `stddev`, passa la prima colonna di `np_baseball` a `numpy.std()`. L'esempio di `np.mean()` mostra come si fa."
Ex().check_correct(
  check_object("stddev").has_equal_value(),
  check_function("numpy.std", index=0, missing_msg=missing).check_args(0).has_equal_value(incorrect_msg=incorrect)
)

missing = "Hai usato `np.corrcoef()` per calcolare la correlazione?"
incorrect1 = "Per calcolare `corr`, il primo argomento di `np.corrcoef()` dovrebbe essere la prima colonna di `np_baseball`, come hai fatto prima."
incorrect2 = "Per calcolare `corr`, il secondo argomento di `np.corrcoef()` dovrebbe essere la seconda colonna di `np_baseball`. Invece di `[:,0]`, usa `[:,1]` questa volta."
Ex().check_correct(
  check_object("corr").has_equal_value(),
  check_function("numpy.corrcoef", index=0, missing_msg=missing).multi(
    check_args(0, missing_msg=incorrect1).has_equal_value(incorrect_msg=incorrect1),
    check_args(1, missing_msg=incorrect2).has_equal_value(incorrect_msg=incorrect2)
  )
)

success_msg("Ottimo lavoro! Hai costruito una solida base - ora è il momento di usare tutte le tue nuove competenze di data science per risolvere più sfide e fare la differenza.")
```

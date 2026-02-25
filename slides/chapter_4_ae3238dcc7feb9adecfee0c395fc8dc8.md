---
title: Insert title here
key: ae3238dcc7feb9adecfee0c395fc8dc8
video_link:
  mp3: >-
    https://videos.datacamp.com/mp3/translations/course_735/it-IT/f75c68c1-df45-4820-9d54-79456fdceeb1.mp3
---

## Array NumPy 2D

```yaml
type: TitleSlide
key: 0cc8abf493
```

`@lower_third`
name: Hugo Bowne-Anderson
title: Data Scientist at DataCamp

`@script`
Grande, sei un mito! Adesso ricreiamo gli array di numpy dal video precedente.

---

## Tipi di array NumPy

```yaml
type: FullSlide
key: 1b9db47fd2
code_zoom: 100
```

`@part1`
```py
import numpy as np
np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
np_weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])
```

```py
type(np_height)
```

```out
numpy.ndarray
```

```py
type(np_weight)
```

```out
numpy.ndarray
```

`@script`
Se chiedi il tipo di questi array, Python ti dice che sono numpy.ndarray. Il punto tra numpy e ndarray ti indica che è un tipo definito nel pacchetto numpy. ndarray sta per array a n dimensioni. Gli array np_height e np_weight sono monodimensionali, ma puoi tranquillamente creare array bidimensionali, tridimensionali, persino a sette dimensioni! In questo video però restiamo su due.

---

## Array NumPy 2D

```yaml
type: FullSlide
key: ebb550dcba
code_zoom: 71
```

`@part1`
```py
np_2d = np.array([[1.73, 1.68, 1.71, 1.89, 1.79],
                  [65.4, 59.2, 63.6, 88.4, 68.7]])
```{{1}}
```py
np_2d
```{{2}}

```out
array([[ 1.73,  1.68,  1.71,  1.89,  1.79],
       [65.4 , 59.2 , 63.6 , 88.4 , 68.7 ]])
```{{2}}

```py
np_2d.shape
```{{3}}

```out
(2, 5) # 2 rows, 5 columns
```{{3}}

```py
np.array([[1.73, 1.68, 1.71, 1.89, 1.79],
          [65.4, 59.2, 63.6, 88.4, "68.7"]])
```{{4}}

```out
array([['1.73', '1.68', '1.71', '1.89', '1.79'],
       ['65.4', '59.2', '63.6', '88.4', '68.7']], dtype='<U32')
```{{4}}

`@script`
Puoi creare un array numpy bidimensionale a partire da una normale lista di liste in Python. Proviamo a crearne uno che contenga tutte le altezze e i pesi della tua famiglia, così.

Se ora stampi np_2d, vedrai che è una struttura rettangolare: ogni sotto-lista della lista corrisponde a una riga nell’array numpy bidimensionale. Da np_2d.shape puoi vedere che abbiamo effettivamente due righe e cinque colonne. shape è un cosiddetto attributo dell’array np_2d che ti dà più informazioni su com’è fatta la struttura dati.

Nota che la sintassi per accedere a un attributo assomiglia a una chiamata di metodo, ma non è la stessa cosa! Ricorda che i metodi hanno le parentesi tonde dopo il nome, mentre, come vedi qui, gli attributi no.

Anche per gli array bidimensionali vale la regola di NumPy: un array può contenere un solo tipo. Se cambi un valore float in una stringa, tutti gli elementi dell’array verranno convertiti in stringhe, per ottenere un array omogeneo.

---

## Sottogruppi

```yaml
type: FullSlide
key: e71d2fc8b8
code_zoom: 80
```

`@part1`
```out
           0       1       2       3       4
           
array([[  1.73,   1.68,   1.71,   1.89,   1.79],     0
       [  65.4,   59.2,   63.6,   88.4,   68.7]])    1
```

```py
np_2d[0]
```

```out
array([1.73, 1.68, 1.71, 1.89, 1.79])
```

`@script`
Puoi pensare all’array numpy bidimensionale come a una lista di liste migliorata: puoi fare calcoli sugli array, come ti ho mostrato prima, e puoi usare modalità più avanzate di selezione.

Supponi di volere la prima riga e poi il terzo elemento di quella riga. Per selezionare la riga, ti serve l’indice zero tra parentesi quadre. Non dimenticare che l’indicizzazione parte da zero.

Per selezionare poi il terzo elemento, puoi estendere la stessa chiamata con un’altra coppia di parentesi, questa volta con l’indice due,

---

## Sottogruppi

```yaml
type: FullSlide
key: 57a1fb1581
disable_transition: true
code_zoom: 80
```

`@part1`
```out
           0       1       2       3       4
           
array([[  1.73,   1.68,   1.71,   1.89,   1.79],     0
       [  65.4,   59.2,   63.6,   88.4,   68.7]])    1
```

```py
np_2d[0][2]
```

```out
1.71
```

```py
np_2d[0, 2]
```{{1}}

```out
1.71
```{{1}}

`@script`
in questo modo. In pratica selezioni la riga e poi, da quella riga, fai un’altra selezione.

C’è anche un modo alternativo di selezionare, usando una sola coppia di parentesi quadre e una virgola. Questa chiamata restituisce esattamente lo stesso valore di prima. Il valore prima della virgola specifica la riga, quello dopo la virgola specifica la colonna. Viene restituita l’intersezione tra le righe e le colonne che hai indicato. Una volta che ci fai l’abitudine, questa sintassi risulta più intuitiva e apre più possibilità.

---

## Sottogruppi

```yaml
type: FullSlide
key: feb75c975c
disable_transition: true
code_zoom: 80
```

`@part1`
```out
           0       1       2       3       4
           
array([[  1.73,   1.68,   1.71,   1.89,   1.79],     0
       [  65.4,   59.2,   63.6,   88.4,   68.7]])    1
```

```py
np_2d[:, 1:3]
```{{1}}

```out
array([[ 1.68,  1.71],
       [59.2 , 63.6 ]])
```{{1}}

```py
np_2d[1, :]
```{{2}}

```out
array([65.4, 59.2, 63.6, 88.4, 68.7])
```{{2}}

`@script`
Supponi di voler selezionare altezza e peso del secondo e del terzo membro della famiglia. Ti servono entrambe le righe, quindi metti i due punti prima della virgola. Vuoi solo la seconda e la terza colonna, quindi metti gli indici da uno a tre dopo la virgola. Ricorda che il terzo indice non è incluso qui. L’intersezione ci dà un array bidimensionale con due righe e due colonne:

Allo stesso modo, puoi selezionare il peso di tutti i membri della famiglia così: ti serve solo la seconda riga, quindi metti uno prima della virgola. Vuoi tutte le colonne, quindi usi i due punti dopo la virgola. L’intersezione restituisce l’intera seconda riga.

Infine, gli array numpy bidimensionali ti permettono di fare calcoli elemento per elemento, proprio come hai fatto con gli array monodimensionali. Questo è qualcosa

---

## Passiamo alla pratica!

```yaml
type: FinalSlide
key: 6047b27c09
```

`@script`
che puoi sperimentare negli esercizi, insieme alla creazione e alla selezione di array numpy bidimensionali! Fantastico

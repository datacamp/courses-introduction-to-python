---
title: Insert title here
key: 433dcfcfedaee070cbf440491c402e3b
video_link:
  mp3: >-
    https://videos.datacamp.com/mp3/translations/course_735/it-IT/d5c57822-aa36-4307-989b-0ec8b90ef06b.mp3
---

## Variabili e tipi

```yaml
type: TitleSlide
key: dc8b62f1c8
```

`@lower_third`
name: Hugo Bowne-Anderson
title: Data Scientist at DataCamp

`@script`
Ottimo lavoro e bentornato! È chiaro che Python è un ottimo calcolatore. Se però vuoi fare calcoli più complessi, ti conviene "salvare" dei valori mentre scrivi il codice.

---

## Variabile

```yaml
type: FullSlide
key: 36ec318b41
```

`@part1`
- Nome specifico, con distinzione tra maiuscole e minuscole

- Richiamare il valore tramite il nome della variabile{{1}}

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
Puoi farlo definendo una variabile, con un nome specifico che distingue tra maiuscole e minuscole. Una volta creata (o dichiarata) questa variabile, potrai richiamarne il valore in seguito semplicemente digitando il nome della variabile.

Supponiamo che tu misuri altezza e peso, in unità metriche: sei alto uno virgola settantanove metri e pesi sessantotto virgola sette chilogrammi. Puoi assegnare questi valori a due variabili, chiamate height e weight, usando il segno di uguale:

Se ora digiti il nome della variabile, height,

Python cerca il nome della variabile, ne recupera il valore e lo stampa.

---

## Calcola il BMI

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

$$ \text{BMI} = \frac{\text{peso}}{\text{altezza}^2} $${{1}}

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
Calcoliamo ora il Body Mass Index, o BMI, che si calcola così, con il peso in chilogrammi e l’altezza in metri. Puoi farlo con i valori effettivi, ma puoi altrettanto bene usare le variabili height e weight, come qui. Ogni volta che digiti il nome di una variabile, stai chiedendo a Python di sostituirlo con il valore reale della variabile. weight corrisponde a sessantotto virgola sette e height a uno virgola settantanove.

Infine, in questa versione Python memorizza il risultato in una nuova variabile, bmi. bmi ora contiene lo stesso valore che hai calcolato prima.

In Python, le variabili si usano continuamente. Ti aiutano a rendere il codice riproducibile.

---

## Riproducibilità

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
Supponi che il codice per creare le variabili height, weight e bmi sia in uno script, come questo. Se ora vuoi ricalcolare il bmi per un altro peso,

---

## Riproducibilità

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
puoi semplicemente cambiare la dichiarazione della variabile weight e rieseguire lo script. Il bmi cambia di conseguenza, perché è cambiato anche il valore della variabile weight.

Finora, abbiamo lavorato solo con valori numerici, come altezza e peso.

---

## Tipi Python

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
In Python, questi numeri hanno tutti un tipo specifico. Puoi verificare il tipo di un valore con la funzione type. Per vedere il tipo del nostro valore bmi, scrivi semplicemente type e poi bmi tra parentesi. Vedrai che è un float, il modo in cui Python rappresenta un numero reale, quindi un numero che può avere sia la parte intera sia la parte decimale. Python ha anche un tipo per i numeri interi: int, come in questo esempio.

Per fare data science, però, ti servirà più di int e float.

---

## Tipi Python (2)

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
Python offre moltissimi altri tipi di dati. I più comuni sono stringhe e booleani.

Una stringa è il modo di Python per rappresentare del testo. Puoi usare sia le virgolette doppie sia le virgolette singole per creare una stringa, come vedi in questi esempi. Se stampi il tipo dell’ultima variabile qui, vedrai che è str, abbreviazione di string.

Il booleano è un tipo che può essere True oppure False. Puoi pensarlo come "Sì" e "No" nel linguaggio di tutti i giorni. I booleani saranno molto utili in futuro, per esempio per filtrare i tuoi dati.

C’è qualcosa di speciale nei tipi di dati di Python.

---

## Tipi Python (3)

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

- Tipo diverso = comportamento diverso!{{3}}

`@script`
Guarda questa riga di codice, che somma due interi, e poi questa riga di codice, che somma due stringhe.

Per gli interi, i valori sono stati sommati, mentre per le stringhe, le stringhe sono state concatenate. L’operatore più si è comportato in modo diverso a seconda dei tipi di dati. Questo è un principio generale: il comportamento del codice dipende dai tipi con cui stai lavorando.

Negli esercizi che seguono, creerai le tue prime variabili ed esplorerai alcuni dei tipi di dati di Python. Ci vediamo nel prossimo video per spiegare tutto sulle liste.

---

## Passiamo alla pratica!

```yaml
type: FinalSlide
key: b7fc40db4d
```

`@script`
Mettiamoci al lavoro con il codice e non vedo l’ora di rivederti nel prossimo capitolo, dove costruirai grafici in Python ancora più belli.

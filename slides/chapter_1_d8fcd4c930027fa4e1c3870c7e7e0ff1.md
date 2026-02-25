---
title: Insert title here
key: d8fcd4c930027fa4e1c3870c7e7e0ff1
video_link:
  mp3: >-
    https://videos.datacamp.com/mp3/translations/course_735/it-IT/db242450-b9ea-4f09-b7a8-327258487fb9.mp3
---

## Ciao Python!

```yaml
type: TitleSlide
key: f743ca8c41
```

`@lower_third`
name: Hugo Bowne-Anderson
title: Data Scientist at DataCamp

`@script`
Ciao, mi chiamo Hugo e sarò la tua guida per Introduzione a Python per la Data Science.

Sono un data scientist e formatore in DataCamp.

---

## Come imparerai

```yaml
type: FullSlide
key: 30ee08a725
disable_transition: true
```

`@part1`
![Interfaccia DataCamp](https://assets.datacamp.com/img/translations/it-IT/production/repositories/288/datasets/729574d2168960686381caefe79baf5978e27d0d/liveexercise.gif)

`@script`
In questo corso imparerai Python per la Data Science attraverso videolezioni, come questa, ed esercizi interattivi. Avrai una tua sessione di Python in cui potrai sperimentare e provare a scrivere il codice giusto per risolvere le consegne. Impari facendo, mentre ricevi un feedback personalizzato e immediato sul tuo lavoro.

---

## Python

```yaml
type: FullSlide
key: 3f23b93572
```

`@part1`
![guido-hba.png](https://assets.datacamp.com/img/translations/it-IT/production/repositories/288/datasets/fb3e4b8dc114529dafffb37d33f2b2244210d40f/guido-hba.png = 38){{1}}

- Scopo generale: costruire qualsiasi cosa{{2}}

- Open source! Gratis!{{3}}

- Pacchetti Python, anche per la scienza dei dati{{4}}

	- Tante applicazioni e campi{{5}}

`@script`
Python è stato ideato da Guido Van Rossum. Qui puoi vedere una mia foto con Guido. Quello che è nato come un progetto hobbistico è presto diventato un linguaggio di programmazione generalista: oggi puoi usare Python per costruire praticamente qualsiasi software. Ma come è successo? Prima di tutto, Python è open source. È gratuito da usare. In secondo luogo, è molto semplice creare pacchetti in Python, cioè codice che puoi condividere con altre persone per risolvere problemi specifici. Col tempo, sono stati sviluppati sempre più pacchetti pensati proprio per la data science. Supponi di voler creare visualizzazioni accattivanti delle vendite della tua azienda. C’è un pacchetto anche per questo. O che ne dici di collegarti a un database per analizzare misurazioni di sensori? Anche per questo c’è un pacchetto.
Spesso ci si riferisce a Python come al coltellino svizzero dei linguaggi di programmazione, perché ci puoi fare quasi tutto.
In questo corso, costruiremo le tue competenze di coding per la data science poco alla volta, quindi resta con noi per scoprire quanto può essere potente questo linguaggio.

---

## Shell IPython

```yaml
type: FullSlide
key: 43a91a7217
```

`@part1`
**Esegui i comandi Python**

![ipython_shell.png](https://assets.datacamp.com/img/translations/it-IT/production/repositories/288/datasets/a9e8440bb8fbd49e4a73e4c36ef1cd677c0dd55f/pyexercise.png = 95)

`@script`
Ora che sei tutto occhi e orecchie per Python, iniziamo a sperimentare. Partirò con la

---

## Shell IPython

```yaml
type: FullSlide
key: 9c51ee700d
disable_transition: true
```

`@part1`
**Esegui i comandi Python**

![ipython_shell_highlighted.png](https://assets.datacamp.com/img/translations/it-IT/production/repositories/288/datasets/dd43cc0183b15b43a072eb0fbab4caa72dee9250/pyexercise_shell.jpg = 95)

`@script`
shell di Python, un posto dove puoi digitare codice Python e vedere subito i risultati. Nell’interfaccia degli esercizi di DataCamp, questa shell è integrata qui. Partiamo con qualcosa di semplice e usiamo Python come calcolatrice.

---

## Shell IPython

```yaml
type: FullSlide
key: 524e4c20a7
disable_transition: true
```

`@part1`
&nbsp;

![Calcoli nella shell IPython di DataCamp](https://assets.datacamp.com/img/translations/it-IT/production/repositories/288/datasets/cee32b788a62e4b9a1234ccde56ac9ebb49cfa72/shelladdition.gif = 95)

`@script`
Scrivo quattro più cinque e premo Invio. Python interpreta quello che hai digitato e stampa il risultato del calcolo, nove. La shell di Python che usiamo qui in realtà non è quella originale; stiamo usando IPython, abbreviazione di Interactive Python, una versione potenziata del Python “classico” che più avanti tornerà molto utile.

IPython è stato creato da Fernando Pérez e fa parte dell’ecosistema più ampio di Jupyter. Oltre a lavorare in modo interattivo con Python, puoi anche far eseguire a Python i cosiddetti

---

## Script Python

```yaml
type: FullSlide
key: 78ef256bc0
```

`@part1`
- File di testo - `.py`{{1}}

- Elenco dei comandi Python{{2}}

- Simile alla digitazione nella shell IPython{{3}}

![Script Python in DataCamp](https://assets.datacamp.com/img/translations/it-IT/production/repositories/288/datasets/59f196e96536543a4fb8801228019fc4106f3791/pyexercise_script.jpg = 78){{3}}

`@script`
script Python. Questi script Python sono semplici file di testo con estensione punto py. In pratica, è un elenco di comandi Python che vengono eseguiti quasi come se stessi digitando tu stesso i comandi nella shell, riga per riga.

---

## Script Python

```yaml
type: FullSlide
key: 717d124175
disable_transition: true
```

`@part1`
![GIF: scrivi 4 + 5 nello script e clicca su "Invia risposta". Non viene mostrato niente.](https://assets.datacamp.com/img/translations/it-IT/production/repositories/288/datasets/2f96e979012e15329cc158d1e0f496aac3539f45/scriptnoprint.gif = 95)

`@script`
Mettiamo ora il comando di prima in uno script, che trovi qui nell’interfaccia di DataCamp. Il passo successivo è eseguire lo script cliccando "Submit Answer". Se esegui questo script nell’interfaccia di DataCamp, non appare nulla nel riquadro di output. Questo perché negli script devi usare esplicitamente print se vuoi generare output durante l’esecuzione.

---

## Script Python

```yaml
type: FullSlide
key: c7a9d02fb6
disable_transition: true
code_zoom: 90
```

`@part1`
![python_script_print.gif](https://assets.datacamp.com/img/translations/it-IT/production/repositories/288/datasets/8b13d046bb54dcb11aa49f0da7363781129d1561/scriptwithprint.gif = 95)

- Usa`print()`  per creare un output dallo script

`@script`
Incartiamo il nostro calcolo precedente in una chiamata a print e rieseguiamo lo script. Questa volta viene generato lo stesso output di prima, ottimo! Mettere il codice in script Python, invece di riscrivere tutto manualmente in modo interattivo, ti aiuta a mantenere struttura ed evitare di ridigitare tutto ogni volta che vuoi fare una modifica; ti basta cambiare lo script e rieseguire l’intero blocco.

---

## Interfaccia DataCamp

```yaml
type: FullSlide
key: 693ba1cd14
```

`@part1`
![Screenshot dell'interfaccia di DataCamp](https://assets.datacamp.com/img/translations/it-IT/production/repositories/288/datasets/a9e8440bb8fbd49e4a73e4c36ef1cd677c0dd55f/pyexercise.png)

`@script`
Ora che hai un’idea dei diversi modi di lavorare con Python, ti suggerisco di passare agli esercizi. Usa la IPython Shell per sperimentare e usa l’editor degli script Python per scrivere la risposta vera e propria. Se fai clic su Submit Answer, il tuo script verrà eseguito e controllato per verificarne la correttezza.

---

## Passiamo alla pratica!

```yaml
type: FinalSlide
key: 7445cd202e
```

`@script`
Mettiti a programmare e non dimenticare di divertirti!

---
title: Insert title here
key: d8fcd4c930027fa4e1c3870c7e7e0ff1
video_link:
  mp3: >-
    https://videos.datacamp.com/mp3/translations/course_735/nl-NL/fe64869f-5d63-410a-be93-a1c38eb522b4.mp3
---

## Hallo Python!

```yaml
type: TitleSlide
key: f743ca8c41
```

`@lower_third`
name: Hugo Bowne-Anderson
title: Data Scientist at DataCamp

`@script`
Hoi, ik ben Hugo en ik ben je host voor Inleiding tot Python voor Data Science.

Ik ben data scientist en docent bij DataCamp.
---

## Hoe je gaat leren

```yaml
type: FullSlide
key: 30ee08a725
disable_transition: true
```

`@part1`
![DataCamp-interface](https://assets.datacamp.com/img/translations/nl-NL/production/repositories/288/datasets/729574d2168960686381caefe79baf5978e27d0d/liveexercise.gif)

`@script`
In deze cursus leer je Python voor Data Science via videolessen, zoals deze, en interactieve oefeningen. Je krijgt je eigen Python-sessie waarin je kunt experimenteren en proberen de juiste code te bedenken om de opdrachten op te lossen. Door te doen, leer je, terwijl je op maat gemaakte en directe feedback op je werk krijgt.
---

## Python

```yaml
type: FullSlide
key: 3f23b93572
```

`@part1`
![guido-hba.png](https://assets.datacamp.com/img/translations/nl-NL/production/repositories/288/datasets/fb3e4b8dc114529dafffb37d33f2b2244210d40f/guido-hba.png = 38){{1}}

- Algemeen doel: bouw wat je maar wilt{{2}}

- Open source! Gratis!{{3}}

- Python-pakketten, ook voor datawetenschap{{4}}

	- Veel toepassingen en gebieden{{5}}

`@script`
Pai-thon is bedacht door Guido van Rossum. Hier zie je een foto van mij met Guido. Wat begon als een hobbyproject, groeide uit tot een algemene programmeertaal: tegenwoordig kun je met Python vrijwel elk stuk software bouwen. Maar hoe is dat zo gekomen? Allereerst is Python open source. Het is gratis te gebruiken. Ten tweede is het heel eenvoudig om pakketten in Python te bouwen: code die je kunt delen met anderen om specifieke problemen op te lossen. In de loop der tijd zijn er steeds meer van zulke pakketten ontwikkeld, speciaal voor data science. Stel dat je fraaie visualisaties van de verkoop van je bedrijf wilt maken. Daar is een pakket voor. Of wat dacht je van verbinden met een database om sensormetingen te analyseren? Ook daar is een pakket voor.
Mensen noemen Python vaak het Zwitsers zakmes onder de programmeertalen, omdat je er bijna alles mee kunt.
In deze cursus bouwen we stap voor stap je data-science-vaardigheden in coderen op, dus blijf vooral kijken om te leren hoe krachtig de taal is.
---

## IPython-shell

```yaml
type: FullSlide
key: 43a91a7217
```

`@part1`
**Python-opdrachten uitvoeren**

![ipython_shell.png](https://assets.datacamp.com/img/translations/nl-NL/production/repositories/288/datasets/a9e8440bb8fbd49e4a73e4c36ef1cd677c0dd55f/pyexercise.png = 95)

`@script`
Nu je helemaal klaar bent voor Python, gaan we experimenteren. Ik begin met de
---

## IPython-shell

```yaml
type: FullSlide
key: 9c51ee700d
disable_transition: true
```

`@part1`
**Python-opdrachten uitvoeren**

![ipython_shell_highlighted.png](https://assets.datacamp.com/img/translations/nl-NL/production/repositories/288/datasets/dd43cc0183b15b43a072eb0fbab4caa72dee9250/pyexercise_shell.jpg = 95)

`@script`
Python-shell, een plek waar je Python-code kunt typen en meteen het resultaat ziet. In de oefenomgeving van DataCamp is deze shell hier ingebouwd. Laten we eenvoudig beginnen en Python gebruiken als rekenmachine.
---

## IPython-shell

```yaml
type: FullSlide
key: 524e4c20a7
disable_transition: true
```

`@part1`
&nbsp;

![Berekeningen in de IPython-shell van DataCamp](https://assets.datacamp.com/img/translations/nl-NL/production/repositories/288/datasets/cee32b788a62e4b9a1234ccde56ac9ebb49cfa72/shelladdition.gif = 95)

`@script`
Ik typ vier plus vijf en druk op Enter. Python interpreteert wat je typt en print het resultaat van je berekening: negen. De Python-shell die we hier gebruiken is eigenlijk niet de originele; we gebruiken IPython, kort voor Interactive Python, een soort opgevoerde versie van gewone Python die later handig zal zijn.

IPython is gemaakt door Fernando Pérez en maakt deel uit van het bredere Jupyter-ecosysteem. Naast interactief werken met Python kun je Python ook zogenaamde
---

## Python-script

```yaml
type: FullSlide
key: 78ef256bc0
```

`@part1`
- Tekstbestanden: `.py`{{1}}

- Lijst met Python-opdrachten{{2}}

- Net als typen in IPython Shell{{3}}

![Python-script in DataCamp](https://assets.datacamp.com/img/translations/nl-NL/production/repositories/288/datasets/59f196e96536543a4fb8801228019fc4106f3791/pyexercise_script.jpg = 78){{3}}

`@script`
python-scripts laten uitvoeren. Die python-scripts zijn simpele tekstbestanden met de extensie punt py. Het is in feite een lijst met Python-opdrachten die worden uitgevoerd, bijna alsof je de commando’s zelf regel voor regel in de shell zou typen.
---

## Python-script

```yaml
type: FullSlide
key: 717d124175
disable_transition: true
```

`@part1`
![GIF: typ 4 + 5 in het script en klik op 'antwoorden'. Er wordt niks weergegeven.](https://assets.datacamp.com/img/translations/nl-NL/production/repositories/288/datasets/2f96e979012e15329cc158d1e0f496aac3539f45/scriptnoprint.gif = 95)

`@script`
Laten we de opdracht van daarnet nu in een script zetten, dat je hier in de interface van DataCamp vindt. De volgende stap is het script uitvoeren door op "Antwoorden" te klikken. Als je dit script in de DataCamp-interface uitvoert, verschijnt er niets in het uitvoervenster. Dat komt omdat je in scripts expliciet print moet gebruiken als je tijdens de uitvoering output wilt genereren.
---

## Python-script

```yaml
type: FullSlide
key: c7a9d02fb6
disable_transition: true
code_zoom: 90
```

`@part1`
![python_script_print.gif](https://assets.datacamp.com/img/translations/nl-NL/production/repositories/288/datasets/8b13d046bb54dcb11aa49f0da7363781129d1561/scriptwithprint.gif = 95)

- Gebruik `print()` om output te genereren vanuit een script

`@script`
Laten we onze vorige berekening in een print-aanroep zetten en het script opnieuw uitvoeren. Deze keer krijg je dezelfde output als daarnet, top! Je code in Python-scripts zetten in plaats van elke stap telkens interactief overtikken, helpt je structuur te houden en voorkomt herhalen als je iets wilt aanpassen; je past het script aan en voert het geheel opnieuw uit.
---

## DataCamp-interface

```yaml
type: FullSlide
key: 693ba1cd14
```

`@part1`
![Screenshot van de DataCamp-interface](https://assets.datacamp.com/img/translations/nl-NL/production/repositories/288/datasets/a9e8440bb8fbd49e4a73e4c36ef1cd677c0dd55f/pyexercise.png)

`@script`
Nu je een idee hebt van verschillende manieren om met Python te werken, stel ik voor dat je naar de oefeningen gaat. Gebruik de IPython-shell om te experimenteren, en gebruik de Python-script-editor om het antwoord te programmeren. Als je op Antwoorden klikt, wordt je script uitgevoerd en gecontroleerd.
---

## Laten we oefenen!

```yaml
type: FinalSlide
key: 7445cd202e
```

`@script`
Veel codeerplezier en vergeet niet te genieten!

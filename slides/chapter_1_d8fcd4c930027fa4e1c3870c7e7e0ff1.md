---
title: Insert title here
key: d8fcd4c930027fa4e1c3870c7e7e0ff1
video_link:
  mp3: >-
    https://videos.datacamp.com/mp3/translations/course_735/sv-SE/0342609f-edd0-4a10-b5e6-5b541b3616b4-2a9ab4c95377dc1094ee47b7724139a0.mp3
---

## Hej Python!

```yaml
type: TitleSlide
key: f743ca8c41
```

`@lower_third`
name: Hugo Bowne-Anderson
title: Data Scientist at DataCamp

`@script`
Hej, mitt namn är Hugo och jag kommer att vara din guide i kursen Introduktion till Python för datavetenskap.

Jag är datavetare och lärare på DataCamp.

---

## Så här lär du dig

```yaml
type: FullSlide
key: 30ee08a725
disable_transition: true
```

`@part1`
![DataCamp-gränssnitt](https://assets.datacamp.com/img/translations/sv-SE/production/repositories/288/datasets/729574d2168960686381caefe79baf5978e27d0d/liveexercise.gif)

`@script`
I den här kursen lär du dig Python för datavetenskap genom videolektioner som den här, och interaktiva övningar. Du får en egen Python-session där du kan experimentera och skriva kod som löser uppgifterna. Du lär dig genom att göra, och får direkt och anpassad återkoppling på ditt arbete.

---

## Python

```yaml
type: FullSlide
key: 3f23b93572
```

`@part1`
![guido-hba.png](https://assets.datacamp.com/img/translations/sv-SE/production/repositories/288/datasets/fb3e4b8dc114529dafffb37d33f2b2244210d40f/guido-hba.png = 38){{1}}

- Allmänt syfte: bygg vad som helst{{2}}

- Öppen källkod! Gratis!{{3}}

- Python-paket, även för datavetenskap{{4}}

	- Många användningsområden och fält{{5}}

`@script`
Python skapades av Guido van Rossum. Här ser du ett foto på mig och Guido. Det som började som ett hobbyprojekt blev snart ett allmänt programmeringsspråk. I dag kan du använda Python för att bygga i princip vilken typ av mjukvara som helst. Hur gick det till? Jo, dels är Python öppen källkod och helt gratis att använda. Dels är det enkelt att bygga paket i Python, det vill säga kod som du kan dela med andra för att lösa specifika problem. Med tiden har allt fler paket anpassade för datavetenskap utvecklats. Vill du skapa avancerade visualiseringar av ditt företags försäljning? Det finns ett paket för det. Eller vill du ansluta till en databas för att analysera sensordata? Det finns också ett paket för det.
Python brukar beskrivas som ett universalverktyg bland programmeringsspråk, eftersom du kan göra nästan vad som helst med det.
I den här kursen bygger vi upp dina kodningsfärdigheter inom datavetenskap steg för steg, så häng med och se hur kraftfullt språket kan vara.

---

## IPython Shell

```yaml
type: FullSlide
key: 43a91a7217
```

`@part1`
**Kör Python-kommandon**

![ipython_shell.png](https://assets.datacamp.com/img/translations/sv-SE/production/repositories/288/datasets/a9e8440bb8fbd49e4a73e4c36ef1cd677c0dd55f/pyexercise.png = 95)

`@script`
Nu när du är redo att utforska Python, låt oss börja experimentera. Vi startar med

---

## IPython Shell

```yaml
type: FullSlide
key: 9c51ee700d
disable_transition: true
```

`@part1`
**Kör Python-kommandon**

![ipython_shell_highlighted.png](https://assets.datacamp.com/img/translations/sv-SE/production/repositories/288/datasets/dd43cc0183b15b43a072eb0fbab4caa72dee9250/pyexercise_shell.jpg = 95)

`@script`
Python-skalet, ett verktyg där du kan skriva Python-kod och direkt se resultatet. I DataCamps övningsgränssnitt finns skalet inbyggt här. Vi börjar enkelt och använder Python som en miniräknare.

---

## IPython Shell

```yaml
type: FullSlide
key: 524e4c20a7
disable_transition: true
```

`@part1`
&nbsp;

![Beräkningar i DataCamps IPython Shell](https://assets.datacamp.com/img/translations/sv-SE/production/repositories/288/datasets/cee32b788a62e4b9a1234ccde56ac9ebb49cfa72/shelladdition.gif = 95)

`@script`
Jag skriver 4 + 5 och trycker på Enter. Python tolkar det du skrivit och visar resultatet av beräkningen, alltså 9. Skalet som används här är egentligen inte det ursprungliga Python-skalet. Vi använder IPython, kort för Interactive Python, som är en mer kraftfull version av det vanliga Python-skalet och som kommer att vara användbart längre fram.

IPython skapades av Fernando Pérez och ingår i det bredare Jupyter-ekosystemet. Förutom att arbeta interaktivt med Python kan du också låta Python köra så kallade

---

## Python-skript

```yaml
type: FullSlide
key: 78ef256bc0
```

`@part1`
- Textfiler – `.py`{{1}}

- Lista med Python-kommandon{{2}}

- Liknar att skriva i IPython Shell{{3}}

![Python-skript i DataCamp](https://assets.datacamp.com/img/translations/sv-SE/production/repositories/288/datasets/59f196e96536543a4fb8801228019fc4106f3791/pyexercise_script.jpg = 78){{3}}

`@script`
Python-skript. Dessa skript är enkla textfiler med filändelsen .py. Det är i grunden en lista med Python-kommandon som körs i ordning, ungefär som om du själv hade skrivit dem i skalet, rad för rad.

---

## Python-skript

```yaml
type: FullSlide
key: 717d124175
disable_transition: true
```

`@part1`
![GIF: skriver 4 + 5 i skriptet och klickar på Skicka in svar. Ingen utdata visas.](https://assets.datacamp.com/img/translations/sv-SE/production/repositories/288/datasets/2f96e979012e15329cc158d1e0f496aac3539f45/scriptnoprint.gif = 95)

`@script`
Vi lägger nu in kommandot från tidigare i ett skript, som du hittar här i DataCamps gränssnitt. Nästa steg är att köra skriptet genom att klicka på "Skicka svar". Om du kör skriptet i DataCamps gränssnitt visas ingenting i utdatafältet. Det beror på att du måste använda print explicit i skript om du vill generera utdata under körningen.

---

## Python-skript

```yaml
type: FullSlide
key: c7a9d02fb6
disable_transition: true
code_zoom: 90
```

`@part1`
![python_script_print.gif](https://assets.datacamp.com/img/translations/sv-SE/production/repositories/288/datasets/8b13d046bb54dcb11aa49f0da7363781129d1561/scriptwithprint.gif = 95)

- Använd `print()` för att generera utdata från skriptet

`@script`
Vi omger den tidigare beräkningen med ett print-anrop och kör skriptet igen. Den här gången genereras samma utdata som tidigare. Att lägga sin kod i Python-skript i stället för att skriva om varje steg interaktivt hjälper dig att hålla ordning och slippa skriva om allt från början när du vill göra en ändring. Du ändrar helt enkelt i skriptet och kör om det.

---

## DataCamp-gränssnitt

```yaml
type: FullSlide
key: 693ba1cd14
```

`@part1`
![Skärmbild av DataCamps gränssnitt](https://assets.datacamp.com/img/translations/sv-SE/production/repositories/288/datasets/a9e8440bb8fbd49e4a73e4c36ef1cd677c0dd55f/pyexercise.png)

`@script`
Nu när du har en bild av olika sätt att arbeta med Python är det dags att gå vidare till övningarna. Använd IPython-skalet för att experimentera, och använd Python-skriptredigeraren för att skriva ditt faktiska svar. När du klickar på "Skicka svar" körs och kontrolleras skriptet.

---

## Nu kör vi en övning!

```yaml
type: FinalSlide
key: 7445cd202e
```

`@script`
Nu är det din tur att koda, och kom ihåg att ha roligt!

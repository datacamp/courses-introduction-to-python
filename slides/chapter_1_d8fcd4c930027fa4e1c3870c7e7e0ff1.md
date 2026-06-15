---
title: Insert title here
key: d8fcd4c930027fa4e1c3870c7e7e0ff1
video_link:
  mp3: >-
    https://videos.datacamp.com/mp3/translations/course_735/ro-RO/e4dda8ca-efb7-480c-9968-65aec15bf6f1-728332c1167761714d709f49b933462d.mp3
---

## Salut, Python!

```yaml
type: TitleSlide
key: f743ca8c41
```

`@lower_third`
name: Hugo Bowne-Anderson
title: Data Scientist at DataCamp

`@script`
Bună, mă numesc Hugo și voi fi ghidul tău în acest curs de Introducere în Python pentru Știința Datelor.

Sunt data scientist și instructor la DataCamp.

---

## Cum veți învăța

```yaml
type: FullSlide
key: 30ee08a725
disable_transition: true
```

`@part1`
![Interfața DataCamp](https://assets.datacamp.com/img/translations/ro-RO/production/repositories/288/datasets/729574d2168960686381caefe79baf5978e27d0d/liveexercise.gif)

`@script`
În acest curs, vei învăța Python pentru Știința Datelor prin lecții video, ca aceasta, și exerciții interactive. Ai propria ta sesiune Python unde poți experimenta și găsi codul potrivit pentru a rezolva cerințele. Înveți făcând, și primești feedback personalizat și imediat pentru tot ce scrii.

---

## Python

```yaml
type: FullSlide
key: 3f23b93572
```

`@part1`
![guido-hba.png](https://assets.datacamp.com/img/translations/ro-RO/production/repositories/288/datasets/fb3e4b8dc114529dafffb37d33f2b2244210d40f/guido-hba.png = 38){{1}}

- Scop general: construiți orice{{2}}

- Open source! Gratuit!{{3}}

- Pachete Python, inclusiv pentru știința datelor{{4}}

	- Multe aplicații și domenii{{5}}

`@script`
Python a fost creat de Guido Van Rossum. Aici poți vedea o fotografie cu mine și Guido. Ce a început ca un proiect de hobby a devenit rapid un limbaj de programare de uz general. Astăzi, poți folosi Python pentru a construi aproape orice tip de software. Cum s-a întâmplat asta? În primul rând, Python este open source, adică este gratuit. În al doilea rând, în Python este foarte ușor să creezi pachete, adică bucăți de cod pe care le poți distribui altor persoane pentru a rezolva probleme specifice. De-a lungul timpului, tot mai multe astfel de pachete dedicate științei datelor au fost dezvoltate. Vrei să creezi vizualizări complexe pentru vânzările companiei tale? Există un pachet pentru asta. Vrei să te conectezi la o bază de date și să analizezi măsurători de senzori? Există și pentru asta un pachet.
Python este cunoscut ca un limbaj extrem de versatil, cu care poți face aproape orice.
În acest curs, îți vom construi abilitățile de programare pentru știința datelor pas cu pas, așa că rămâi alături de noi și vei vedea cât de puternic este acest limbaj.

---

## Shell IPython

```yaml
type: FullSlide
key: 43a91a7217
```

`@part1`
**Executați comenzi Python**

![ipython_shell.png](https://assets.datacamp.com/img/translations/ro-RO/production/repositories/288/datasets/a9e8440bb8fbd49e4a73e4c36ef1cd677c0dd55f/pyexercise.png = 95)

`@script`
Acum că ești pregătit să descoperi Python, hai să începem să experimentăm. Voi porni cu

---

## Shell IPython

```yaml
type: FullSlide
key: 9c51ee700d
disable_transition: true
```

`@part1`
**Executați comenzi Python**

![ipython_shell_highlighted.png](https://assets.datacamp.com/img/translations/ro-RO/production/repositories/288/datasets/dd43cc0183b15b43a072eb0fbab4caa72dee9250/pyexercise_shell.jpg = 95)

`@script`
shell-ul Python, un spațiu unde poți scrie cod Python și vedea imediat rezultatele. În interfața de exerciții a DataCamp, acest shell se află chiar aici. Hai să începem simplu și să folosim Python ca pe un calculator.

---

## Shell IPython

```yaml
type: FullSlide
key: 524e4c20a7
disable_transition: true
```

`@part1`
&nbsp;

![Calcule în Shell-ul IPython al DataCamp](https://assets.datacamp.com/img/translations/ro-RO/production/repositories/288/datasets/cee32b788a62e4b9a1234ccde56ac9ebb49cfa72/shelladdition.gif = 95)

`@script`
Tastez 4 + 5 și apăs Enter. Python interpretează ce ai scris și afișează rezultatul calculului, adică 9. Shell-ul Python folosit aici nu este cel original. Folosim IPython, prescurtare de la Interactive Python, o versiune îmbunătățită a Python-ului clasic, care va fi utilă mai târziu.

IPython a fost creat de Fernando Pérez și face parte din ecosistemul Jupyter. Pe lângă lucrul interactiv cu Python, poți rula și

---

## Script Python

```yaml
type: FullSlide
key: 78ef256bc0
```

`@part1`
- Fișiere text - `.py`{{1}}

- Listă de comenzi Python{{2}}

- Similar cu tastarea în Shell IPython{{3}}

![Script Python în DataCamp](https://assets.datacamp.com/img/translations/ro-RO/production/repositories/288/datasets/59f196e96536543a4fb8801228019fc4106f3791/pyexercise_script.jpg = 78){{3}}

`@script`
scripturi Python. Aceste scripturi sunt pur și simplu fișiere text cu extensia punct py. Practic, conțin o listă de comenzi Python care se execută pe rând, aproape ca și cum le-ai tasta tu însuți în shell, linie cu linie.

---

## Script Python

```yaml
type: FullSlide
key: 717d124175
disable_transition: true
```

`@part1`
![GIF: tastarea 4 + 5 în script și apăsarea butonului de trimitere. Nu este afișat niciun rezultat.](https://assets.datacamp.com/img/translations/ro-RO/production/repositories/288/datasets/2f96e979012e15329cc158d1e0f496aac3539f45/scriptnoprint.gif = 95)

`@script`
Hai să punem comanda anterioară într-un script, pe care îl găsești aici în interfața DataCamp. Urmează să executăm scriptul apăsând „Trimite răspunsul". Dacă rulezi scriptul în interfața DataCamp, nu apare nimic în panoul de rezultate. Asta pentru că în scripturi trebuie să folosești explicit funcția print dacă vrei să generezi rezultate în timpul execuției.

---

## Script Python

```yaml
type: FullSlide
key: c7a9d02fb6
disable_transition: true
code_zoom: 90
```

`@part1`
![python_script_print.gif](https://assets.datacamp.com/img/translations/ro-RO/production/repositories/288/datasets/8b13d046bb54dcb11aa49f0da7363781129d1561/scriptwithprint.gif = 95)

- Folosiți `print()` pentru a genera rezultate din script

`@script`
Hai să înglobăm calculul anterior într-un apel print și să rerulăm scriptul. De data aceasta, se generează același rezultat ca înainte. Să scrii codul în scripturi Python, în loc să retastezi totul interactiv pas cu pas, te ajută să menții o structură clară și să eviți repetițiile inutile. Dacă vrei să faci o modificare, o faci în script și rerulezi totul.

---

## Interfața DataCamp

```yaml
type: FullSlide
key: 693ba1cd14
```

`@part1`
![Captură de ecran a interfeței DataCamp](https://assets.datacamp.com/img/translations/ro-RO/production/repositories/288/datasets/a9e8440bb8fbd49e4a73e4c36ef1cd677c0dd55f/pyexercise.png)

`@script`
Acum că ai o idee despre diferitele moduri de a lucra cu Python, îți sugerez să treci la exerciții. Folosește shell-ul IPython pentru experimente și editorul de scripturi Python pentru a scrie răspunsul final. Când apeși „Trimite răspunsul", scriptul tău va fi executat și verificat.

---

## Să exersăm!

```yaml
type: FinalSlide
key: 7445cd202e
```

`@script`
Apucă-te de cod și nu uita să te bucuri de proces!

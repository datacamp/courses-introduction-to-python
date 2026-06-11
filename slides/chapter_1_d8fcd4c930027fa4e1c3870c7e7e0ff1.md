---
title: Insert title here
key: d8fcd4c930027fa4e1c3870c7e7e0ff1
video_link:
  mp3: >-
    https://videos.datacamp.com/mp3/translations/course_735/pl-PL/8e5a62e8-f97a-4f4e-93fc-cce8270f14a6-d0161b047be5fe8d88f1fe9451be85db.mp3
---

## Witaj, Python!

```yaml
type: TitleSlide
key: f743ca8c41
```

`@lower_third`
name: Hugo Bowne-Anderson
title: Data Scientist at DataCamp

`@script`
Cześć, mam na imię Hugo i będę twoim przewodnikiem po kursie Wprowadzenie do Pythona dla Data Science.

Jestem data scientistem i instruktorem w DataCamp.

---

## Jak będziesz się uczyć

```yaml
type: FullSlide
key: 30ee08a725
disable_transition: true
```

`@part1`
![Interfejs DataCamp](https://assets.datacamp.com/img/translations/pl-PL/production/repositories/288/datasets/729574d2168960686381caefe79baf5978e27d0d/liveexercise.gif)

`@script`
W tym kursie nauczysz się Pythona w zastosowaniu do data science. Czeka cię mix lekcji wideo, takich jak ta, oraz ćwiczeń interaktywnych. Dostaniesz własną sesję Pythona, gdzie możesz eksperymentować i pisać kod, który rozwiązuje kolejne zadania. Uczysz się przez praktykę i od razu dostajesz spersonalizowaną informację zwrotną.

---

## Python

```yaml
type: FullSlide
key: 3f23b93572
```

`@part1`
![guido-hba.png](https://assets.datacamp.com/img/translations/pl-PL/production/repositories/288/datasets/fb3e4b8dc114529dafffb37d33f2b2244210d40f/guido-hba.png = 38){{1}}

- Język ogólnego przeznaczenia: do budowania wszystkiego{{2}}

- Open source! Bezpłatny!{{3}}

- Pakiety Python, również do analizy danych{{4}}

	- Wiele zastosowań i dziedzin{{5}}

`@script`
Pythona stworzył Guido van Rossum. Tutaj możesz zobaczyć moje zdjęcie z Guidem. To, co zaczęło się jako projekt hobbystyczny, szybko stało się językiem programowania ogólnego przeznaczenia. Dziś w Pythonie można napisać praktycznie każde oprogramowanie. Skąd taki sukces? Po pierwsze, Python jest open source, czyli całkowicie darmowy. Po drugie, bardzo łatwo tworzyć w nim pakiety, czyli gotowy kod, którym można dzielić się z innymi, żeby rozwiązywać konkretne problemy. Z czasem powstało coraz więcej pakietów stworzonych specjalnie z myślą o data science. Chcesz zrobić efektowne wizualizacje sprzedaży swojej firmy? Jest pakiet od tego. A może połączyć się z bazą danych i analizować pomiary z czujników? Na to też znajdziesz pakiet.
Często mówi się o Pythonie jako o szwajcarskim scyzoryku wśród języków programowania, bo można w nim zrobić niemal wszystko.
W tym kursie będziemy krok po kroku budować twoje umiejętności programowania w data science, więc zostań z nami i przekonaj się, jak potężnym narzędziem jest ten język.

---

## Powłoka IPython

```yaml
type: FullSlide
key: 43a91a7217
```

`@part1`
**Wykonywanie poleceń Python**

![ipython_shell.png](https://assets.datacamp.com/img/translations/pl-PL/production/repositories/288/datasets/a9e8440bb8fbd49e4a73e4c36ef1cd677c0dd55f/pyexercise.png = 95)

`@script`
Skoro masz już ochotę na Pythona, zacznijmy eksperymenty. Zacznę od

---

## Powłoka IPython

```yaml
type: FullSlide
key: 9c51ee700d
disable_transition: true
```

`@part1`
**Wykonywanie poleceń Python**

![ipython_shell_highlighted.png](https://assets.datacamp.com/img/translations/pl-PL/production/repositories/288/datasets/dd43cc0183b15b43a072eb0fbab4caa72dee9250/pyexercise_shell.jpg = 95)

`@script`
powłoki Pythona, czyli miejsca, gdzie możesz wpisywać kod i od razu widzieć wyniki. W interfejsie ćwiczeń DataCamp ta powłoka jest wbudowana tutaj. Zacznijmy od czegoś prostego i użyjmy Pythona jak kalkulatora.

---

## Powłoka IPython

```yaml
type: FullSlide
key: 524e4c20a7
disable_transition: true
```

`@part1`
&nbsp;

![Obliczenia w powłoce IPython DataCamp](https://assets.datacamp.com/img/translations/pl-PL/production/repositories/288/datasets/cee32b788a62e4b9a1234ccde56ac9ebb49cfa72/shelladdition.gif = 95)

`@script`
Wpiszę 4 + 5 i nacisnę Enter. Python interpretuje to, co wpisałeś, i wyświetla wynik działania, czyli 9. Powłoka Pythona użyta tutaj to w rzeczywistości nie ta oryginalna. Korzystamy z IPython, skrótu od Interactive Python, czyli rozbudowanej wersji standardowego Pythona, która przyda się nam później.

IPython stworzył Fernando Pérez i jest częścią szerszego ekosystemu Jupyter. Oprócz pracy interaktywnej możesz też uruchamiać tak zwane

---

## Skrypt Python

```yaml
type: FullSlide
key: 78ef256bc0
```

`@part1`
- Pliki tekstowe - `.py`{{1}}

- Lista poleceń Python{{2}}

- Podobne do wpisywania w powłoce IPython{{3}}

![Skrypt Python w DataCamp](https://assets.datacamp.com/img/translations/pl-PL/production/repositories/288/datasets/59f196e96536543a4fb8801228019fc4106f3791/pyexercise_script.jpg = 78){{3}}

`@script`
skrypty Pythona. Skrypt Pythona to po prostu plik tekstowy z rozszerzeniem .py. To w zasadzie lista poleceń, które są wykonywane jedno po drugim, tak jakbyś sam wpisywał je w powłoce, linijka po linijce.

---

## Skrypt Python

```yaml
type: FullSlide
key: 717d124175
disable_transition: true
```

`@part1`
![GIF: wpisywanie 4 + 5 w skrypcie i kliknięcie przycisku submit. Brak danych wyjściowych.](https://assets.datacamp.com/img/translations/pl-PL/production/repositories/288/datasets/2f96e979012e15329cc158d1e0f496aac3539f45/scriptnoprint.gif = 95)

`@script`
Umieśćmy teraz poprzednie polecenie w skrypcie. Znajdziesz go tutaj, w interfejsie DataCamp. Kolejny krok to uruchomienie skryptu przez kliknięcie „Prześlij odpowiedź". Jeśli uruchomisz ten skrypt w interfejsie DataCamp, w panelu wyjściowym nie pojawi się nic. Dzieje się tak dlatego, że w skryptach trzeba jawnie użyć funkcji print, jeśli chcesz zobaczyć wynik działania kodu.

---

## Skrypt Python

```yaml
type: FullSlide
key: c7a9d02fb6
disable_transition: true
code_zoom: 90
```

`@part1`
![python_script_print.gif](https://assets.datacamp.com/img/translations/pl-PL/production/repositories/288/datasets/8b13d046bb54dcb11aa49f0da7363781129d1561/scriptwithprint.gif = 95)

- Użyj `print()`, aby wyświetlić dane wyjściowe ze skryptu

`@script`
Opakujmy poprzednie obliczenie w wywołanie funkcji print i uruchommy skrypt ponownie. Tym razem widzimy ten sam wynik co wcześniej. Zapisywanie kodu w skryptach zamiast ręcznego wpisywania każdego kroku pozwala utrzymać porządek i uniknąć wielokrotnego powtarzania tej samej pracy. Jeśli chcesz coś zmienić, po prostu edytujesz skrypt i uruchamiasz go od nowa.

---

## Interfejs DataCamp

```yaml
type: FullSlide
key: 693ba1cd14
```

`@part1`
![Zrzut ekranu interfejsu DataCamp](https://assets.datacamp.com/img/translations/pl-PL/production/repositories/288/datasets/a9e8440bb8fbd49e4a73e4c36ef1cd677c0dd55f/pyexercise.png)

`@script`
Wiesz już, na jakie sposoby można pracować z Pythonem. Przejdźmy teraz do ćwiczeń. Używaj powłoki IPython do eksperymentowania, a edytora skryptów do wpisywania właściwych odpowiedzi. Kliknięcie „Prześlij odpowiedź" uruchomi twój skrypt i sprawdzi, czy jest poprawny.

---

## Czas na ćwiczenia!

```yaml
type: FinalSlide
key: 7445cd202e
```

`@script`
Do dzieła i pamiętaj, żeby się przy tym dobrze bawić!

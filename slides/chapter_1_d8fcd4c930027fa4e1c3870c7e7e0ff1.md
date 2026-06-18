---
title: Insert title here
key: d8fcd4c930027fa4e1c3870c7e7e0ff1
video_link:
  mp3: >-
    https://videos.datacamp.com/mp3/translations/course_735/uk-UA/15e9db05-25f6-4def-9e18-b9923a9384fe-8d8bae3a19923d25276fa609ecaa0777.mp3
---

## Вітаємо в Python!

```yaml
type: TitleSlide
key: f743ca8c41
```

`@lower_third`
name: Hugo Bowne-Anderson
title: Data Scientist at DataCamp

`@script`
Вітаю, мене звати Г'юго, і я буду вашим провідником у курсі «Вступ до Python для науки про дані».

Я дата-сайєнтист і викладач у DataCamp.

---

## Як ви навчатиметесь

```yaml
type: FullSlide
key: 30ee08a725
disable_transition: true
```

`@part1`
![Інтерфейс DataCamp](https://assets.datacamp.com/img/translations/uk-UA/production/repositories/288/datasets/729574d2168960686381caefe79baf5978e27d0d/liveexercise.gif)

`@script`
У цьому курсі ви опануєте Python для науки про дані через відеоуроки, як цей, та інтерактивні вправи. Ви отримаєте власну сесію Python, де зможете експериментувати й підбирати правильний код для розв'язання завдань. Ви навчаєтеся, виконуючи дії, і одразу отримуєте персоналізований зворотний зв'язок щодо своєї роботи.

---

## Python

```yaml
type: FullSlide
key: 3f23b93572
```

`@part1`
![guido-hba.png](https://assets.datacamp.com/img/translations/uk-UA/production/repositories/288/datasets/fb3e4b8dc114529dafffb37d33f2b2244210d40f/guido-hba.png = 38){{1}}

- Загального призначення: можна створити що завгодно{{2}}

- Відкритий код! Безплатно!{{3}}

- Пакети Python, зокрема для data science{{4}}

	- Багато сфер і застосувань{{5}}

`@script`
Python створив Гвідо ван Россум. Ось фото, де я разом із Гвідо. Те, що починалося як хобі, швидко перетворилося на мову програмування загального призначення. Нині Python можна використати, щоб створити майже будь-яке програмне забезпечення. Як це стало можливим? По-перше, Python є відкритим кодом. Ним можна вільно користуватися. По-друге, у Python дуже просто створювати пакети. Це код, яким можна поділитися з іншими, щоб розв'язувати конкретні завдання. З плином часу з'являлося дедалі більше пакетів спеціально для науки про дані. Припустімо, ви хочете зробити наочні візуалізації продажів вашої компанії. Є пакет для цього. Або потрібно під'єднатися до бази даних, щоб проаналізувати показники з датчиків. Також є пакет для цього.
Python часто називають універсальним інструментом серед мов програмування, адже з ним можна зробити майже все.
У цьому курсі ми поступово розвиватимемо ваші навички кодування для науки про дані. Тож залишайтеся з нами, щоб побачити, наскільки потужною може бути ця мова.

---

## IPython Shell

```yaml
type: FullSlide
key: 43a91a7217
```

`@part1`
**Виконуйте команди Python**

![ipython_shell.png](https://assets.datacamp.com/img/translations/uk-UA/production/repositories/288/datasets/a9e8440bb8fbd49e4a73e4c36ef1cd677c0dd55f/pyexercise.png = 95)

`@script`
Тепер, коли ви налаштовані слухати й дивитися про Python, почнімо експерименти. Я почну з

---

## IPython Shell

```yaml
type: FullSlide
key: 9c51ee700d
disable_transition: true
```

`@part1`
**Виконуйте команди Python**

![ipython_shell_highlighted.png](https://assets.datacamp.com/img/translations/uk-UA/production/repositories/288/datasets/dd43cc0183b15b43a072eb0fbab4caa72dee9250/pyexercise_shell.jpg = 95)

`@script`
оболонки Python. Це місце, де ви вводите код Python і миттєво бачите результат. В інтерфейсі вправ DataCamp ця оболонка вбудована ось тут. Почнімо з простого та використаймо Python як калькулятор.

---

## IPython Shell

```yaml
type: FullSlide
key: 524e4c20a7
disable_transition: true
```

`@part1`
&nbsp;

![Обчислення в IPython shell DataCamp](https://assets.datacamp.com/img/translations/uk-UA/production/repositories/288/datasets/cee32b788a62e4b9a1234ccde56ac9ebb49cfa72/shelladdition.gif = 95)

`@script`
Наберу 4 + 5 і натисну Enter. Python інтерпретує введене та виводить результат обчислення, 9. Оболонка Python, яку ми тут використовуємо, насправді не оригінальна. Це IPython, скорочено від Interactive Python, тобто розширена версія звичайного Python, яка знадобиться нам згодом.

IPython створив Фернандо Перес і він є частиною ширшої екосистеми Jupyter. Крім інтерактивної роботи з Python, ви також можете запускати так звані

---

## Скрипт Python

```yaml
type: FullSlide
key: 78ef256bc0
```

`@part1`
- Текстові файли — `.py`{{1}}

- Список команд Python{{2}}

- Подібно до введення в IPython Shell{{3}}

![Скрипт Python у DataCamp](https://assets.datacamp.com/img/translations/uk-UA/production/repositories/288/datasets/59f196e96536543a4fb8801228019fc4106f3791/pyexercise_script.jpg = 78){{3}}

`@script`
скрипти Python. Це звичайні текстові файли з розширенням .py. По суті це список команд Python, які виконуються майже так само, ніби ви вводили їх в оболонці власноруч, рядок за рядком.

---

## Скрипт Python

```yaml
type: FullSlide
key: 717d124175
disable_transition: true
```

`@part1`
![GIF: введення 4 + 5 у скрипті й натискання submit answer. Виводу немає.](https://assets.datacamp.com/img/translations/uk-UA/production/repositories/288/datasets/2f96e979012e15329cc158d1e0f496aac3539f45/scriptnoprint.gif = 95)

`@script`
Тепер помістімо попередню команду в скрипт. Його можна знайти тут, в інтерфейсі DataCamp. Наступний крок – виконати скрипт, натиснувши "Submit Answer". Якщо ви запустите цей скрипт в інтерфейсі DataCamp, у вікні виводу нічого не з'явиться. Це тому, що в скриптах потрібно явно використовувати print, якщо ви хочете побачити результат під час виконання.

---

## Скрипт Python

```yaml
type: FullSlide
key: c7a9d02fb6
disable_transition: true
code_zoom: 90
```

`@part1`
![python_script_print.gif](https://assets.datacamp.com/img/translations/uk-UA/production/repositories/288/datasets/8b13d046bb54dcb11aa49f0da7363781129d1561/scriptwithprint.gif = 95)

- Використовуйте `print()` для виводу зі скрипту

`@script`
Обернімо наше попереднє обчислення у виклик print і перезапустімо скрипт. Цього разу з'являється такий самий результат, чудово. Розміщення коду в скриптах Python, замість постійного ручного введення кожного кроку інтерактивно, допомагає підтримувати структуру та не перевводити все наново, коли потрібно внести зміни. Ви просто змінюєте скрипт і запускаєте все ще раз.

---

## Інтерфейс DataCamp

```yaml
type: FullSlide
key: 693ba1cd14
```

`@part1`
![Знімок екрана інтерфейсу DataCamp](https://assets.datacamp.com/img/translations/uk-UA/production/repositories/288/datasets/a9e8440bb8fbd49e4a73e4c36ef1cd677c0dd55f/pyexercise.png)

`@script`
Тепер, коли ви розумієте різні способи роботи з Python, пропоную перейти до вправ. Використовуйте оболонку IPython для експериментів, а редактор скриптів Python – щоб написати фактичне розв'язання. Коли натиснете Submit Answer, ваш скрипт буде виконано й перевірено на правильність.

---

## Давайте потренуємось!

```yaml
type: FinalSlide
key: 7445cd202e
```

`@script`
Починайте кодувати і не забувайте отримувати задоволення від процесу!

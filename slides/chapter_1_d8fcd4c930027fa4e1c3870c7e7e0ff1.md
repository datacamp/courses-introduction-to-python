---
title: Insert title here
key: d8fcd4c930027fa4e1c3870c7e7e0ff1
video_link:
  mp3: >-
    https://videos.datacamp.com/mp3/translations/course_735/ru-RU/a43091aa-1f65-4c09-811e-547168df7449-f922e4bb2251cc091f36e64077542cae.mp3
---

## Привет, Python!

```yaml
type: TitleSlide
key: f743ca8c41
```

`@lower_third`
name: Hugo Bowne-Anderson
title: Data Scientist at DataCamp

`@script`
Привет, меня зовут Хьюго, и я буду вашим преподавателем в курсе «Введение в Python для науки о данных».

Я специалист по данным и преподаватель в DataCamp.

---

## Как проходит обучение

```yaml
type: FullSlide
key: 30ee08a725
disable_transition: true
```

`@part1`
![Интерфейс DataCamp](https://assets.datacamp.com/img/translations/ru-RU/production/repositories/288/datasets/729574d2168960686381caefe79baf5978e27d0d/liveexercise.gif)

`@script`
В этом курсе вы будете изучать Python для науки о данных через видеоуроки, подобные этому, и интерактивные упражнения. У вас будет собственная сессия Python, где вы сможете экспериментировать и находить верный код для выполнения заданий. Вы учитесь на практике и сразу получаете персональную обратную связь.

---

## Python

```yaml
type: FullSlide
key: 3f23b93572
```

`@part1`
![guido-hba.png](https://assets.datacamp.com/img/translations/ru-RU/production/repositories/288/datasets/fb3e4b8dc114529dafffb37d33f2b2244210d40f/guido-hba.png = 38){{1}}

- Универсальный язык: подходит для любых задач{{2}}

- Open source! Бесплатно!{{3}}

- Пакеты Python, в том числе для анализа данных{{4}}

	- Широкое применение в разных областях{{5}}

`@script`
Python был создан Гвидо ван Россумом. Здесь вы можете увидеть моё фото вместе с Гвидо. То, что начиналось как хобби-проект, вскоре превратилось в универсальный язык программирования. Сегодня с помощью Python можно создать практически любое программное обеспечение. Как же это произошло? Во-первых, Python — это проект с открытым исходным кодом, он бесплатен. Во-вторых, на Python очень легко создавать пакеты — готовый код, которым можно делиться с другими для решения конкретных задач. Со временем всё больше таких пакетов разрабатывается специально для науки о данных. Хотите создать красивые визуализации продаж вашей компании? Для этого есть пакет. Нужно подключиться к базе данных и проанализировать показания датчиков? И для этого тоже есть пакет.
Python часто называют швейцарским армейским ножом среди языков программирования — с его помощью можно решить почти любую задачу.
В этом курсе мы будем шаг за шагом формировать ваши навыки программирования в области науки о данных. Оставайтесь с нами, и вы сами убедитесь, насколько мощным может быть этот язык.

---

## IPython Shell

```yaml
type: FullSlide
key: 43a91a7217
```

`@part1`
**Выполнение команд Python**

![ipython_shell.png](https://assets.datacamp.com/img/translations/ru-RU/production/repositories/288/datasets/a9e8440bb8fbd49e4a73e4c36ef1cd677c0dd55f/pyexercise.png = 95)

`@script`
Теперь, когда вы готовы познакомиться с Python поближе, давайте начнём экспериментировать. Начнём с

---

## IPython Shell

```yaml
type: FullSlide
key: 9c51ee700d
disable_transition: true
```

`@part1`
**Выполнение команд Python**

![ipython_shell_highlighted.png](https://assets.datacamp.com/img/translations/ru-RU/production/repositories/288/datasets/dd43cc0183b15b43a072eb0fbab4caa72dee9250/pyexercise_shell.jpg = 95)

`@script`
оболочки Python — среды, где вы можете вводить код и сразу видеть результат. В интерфейсе упражнений DataCamp эта оболочка встроена прямо здесь. Давайте начнём с простого и используем Python как калькулятор.

---

## IPython Shell

```yaml
type: FullSlide
key: 524e4c20a7
disable_transition: true
```

`@part1`
&nbsp;

![Вычисления в IPython Shell DataCamp](https://assets.datacamp.com/img/translations/ru-RU/production/repositories/288/datasets/cee32b788a62e4b9a1234ccde56ac9ebb49cfa72/shelladdition.gif = 95)

`@script`
Введём 4 + 5 и нажмём Enter. Python обрабатывает введённое выражение и выводит результат вычисления — 9. Оболочка Python, которая используется здесь, — это не стандартная оболочка. Мы работаем с IPython, сокращённо от «Interactive Python» — это расширенная версия обычного Python, которая пригодится нам позже.

IPython был создан Фернандо Пересом и является частью экосистемы Jupyter. Помимо интерактивной работы с Python, вы также можете запускать так называемые

---

## Скрипт Python

```yaml
type: FullSlide
key: 78ef256bc0
```

`@part1`
- Текстовые файлы — `.py`{{1}}

- Набор команд Python{{2}}

- Похоже на ввод команд в IPython Shell{{3}}

![Скрипт Python в DataCamp](https://assets.datacamp.com/img/translations/ru-RU/production/repositories/288/datasets/59f196e96536543a4fb8801228019fc4106f3791/pyexercise_script.jpg = 78){{3}}

`@script`
скрипты Python. Скрипты Python — это обычные текстовые файлы с расширением «.py». По сути, это список команд Python, которые выполняются последовательно, строка за строкой, как если бы вы вводили их в оболочке вручную.

---

## Скрипт Python

```yaml
type: FullSlide
key: 717d124175
disable_transition: true
```

`@part1`
![GIF: ввод 4 + 5 в скрипте и нажатие «Отправить ответ». Вывод не отображается.](https://assets.datacamp.com/img/translations/ru-RU/production/repositories/288/datasets/2f96e979012e15329cc158d1e0f496aac3539f45/scriptnoprint.gif = 95)

`@script`
Давайте теперь поместим предыдущую команду в скрипт — его можно найти здесь, в интерфейсе DataCamp. Следующий шаг — выполнить скрипт, нажав кнопку «Отправить ответ». Если вы запустите этот скрипт в интерфейсе DataCamp, область вывода окажется пустой. Это потому, что в скриптах нужно явно использовать функцию print, если вы хотите получить вывод во время выполнения.

---

## Скрипт Python

```yaml
type: FullSlide
key: c7a9d02fb6
disable_transition: true
code_zoom: 90
```

`@part1`
![python_script_print.gif](https://assets.datacamp.com/img/translations/ru-RU/production/repositories/288/datasets/8b13d046bb54dcb11aa49f0da7363781129d1561/scriptwithprint.gif = 95)

- Используйте `print()`, чтобы получить вывод из скрипта

`@script`
Давайте обернём предыдущее вычисление в вызов print и запустим скрипт заново. На этот раз мы получим тот же вывод, что и раньше. Хранение кода в скриптах Python вместо того, чтобы каждый раз вводить его вручную, помогает поддерживать структуру и избегать повторного набора. Если нужно что-то изменить, просто внесите правку в скрипт и запустите его снова целиком.

---

## Интерфейс DataCamp

```yaml
type: FullSlide
key: 693ba1cd14
```

`@part1`
![Снимок экрана интерфейса DataCamp](https://assets.datacamp.com/img/translations/ru-RU/production/repositories/288/datasets/a9e8440bb8fbd49e4a73e4c36ef1cd677c0dd55f/pyexercise.png)

`@script`
Теперь, когда вы познакомились с разными способами работы с Python, предлагаю перейти к упражнениям. Используйте оболочку IPython для экспериментов, а редактор скриптов Python — для написания окончательного ответа. Если вы нажмёте кнопку «Отправить ответ», ваш скрипт будет выполнен и проверен на правильность.

---

## Давайте потренируемся!

```yaml
type: FinalSlide
key: 7445cd202e
```

`@script`
Приступайте к программированию и не забывайте получать удовольствие от процесса!

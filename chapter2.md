---
title_meta: Розділ 2
title: Списки в Python
description: >-
  Навчіться зберігати, отримувати доступ і змінювати дані в списках — перший
  крок до ефективної роботи з великими обсягами даних.
attachments:
  slides_link: 'https://projector-video-pdf-converter.datacamp.com/735/chapter2.pdf'
lessons:
  - nb_of_exercises: 4
    title: Списки в Python
  - nb_of_exercises: 4
    title: Вибір підсписків
  - nb_of_exercises: 5
    title: Зміна списків
---

## Списки в Python

```yaml
type: VideoExercise
key: a5886d213f
xp: 50
```

`@projector_key`
a0530c4542f10988847b2dbb91f717c3

---

## Створіть список

```yaml
type: NormalExercise
key: e6c527bf41
lang: python
xp: 100
skills:
  - 2
```

Список — це **складений тип даних**; у ньому можна групувати значення, наприклад так:

```
a = "is"
b = "nice"
my_list = ["my", "list", a, b]
```

Після того як ви виміряли зріст членів родини, вирішили зібрати деякі відомості про дім, у якому живете. Площі різних частин вашого житла збережені в окремих змінних у цій вправі.

`@instructions`
- Створіть список `areas`, до якого увійдуть площі коридору (`hall`), кухні (`kit`), вітальні (`liv`), спальні (`bed`) та ванної кімнати (`bath`) — у такому порядку. Використайте заздалегідь оголошені змінні.
- Виведіть `areas` за допомогою функції `print()`.

`@hint`
- Ви можете використати вже створені змінні, щоб зібрати список: `areas = [hall, kit, ...]`.
- Обовʼязково використовуйте квадратні дужки `[]`, а не круглі `()`.
- Не потрібно ставити лапки, коли зберігаєте змінні у списку.
- Введіть `print(areas)`, щоб вивести список під час надсилання відповіді.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Create list areas


# Print areas

```

`@solution`
```{python}
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Create list areas
areas = [hall, kit, liv, bed, bath]

# Print areas
print(areas)
```

`@sct`
```{python}
predef_msg = "Не видаляйте та не редагуйте попередньо визначені змінні!"
areas_msg = "Визначте `areas` як список, що містить усі змінні площі у правильному порядку: `[hall, kit, liv, bed, bath]`. Уникайте друкарських помилок. Список не повинен містити нічого іншого!"

Ex().check_correct(
    has_printout(0, not_printed_msg = "__JINJA__:Чи використали Ви `{{sol_call}}`, щоб вивести список `areas` в кінці Вашого скрипту?"),
    check_correct(
        check_object("areas").has_equal_value(incorrect_msg = areas_msg),
        multi(
            check_object('hall', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
            check_object('kit', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
            check_object('liv', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
            check_object('bed', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
            check_object('bath', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg)
        )
    )
)

success_msg("Чудово! Список тут набагато кращий, чи не так?")
```

---

## Створення списків із різних типів

```yaml
type: NormalExercise
key: 1702a8bcdc
lang: python
xp: 100
skills:
  - 2
```

Хоч це й не дуже поширено, список може містити суміш типів Python, зокрема рядки, числа з плавною комою та булеві значення.

Тепер ви додасте назви кімнат до свого списку, щоб легко бачити і назву кімнати, і її розмір разом.

Частину коду вже надано, щоб ви швидше розпочали. Зверніть увагу: `"bathroom"` — це рядок, а `bath` — це змінна, що представляє число з плавною комою `9.50`, яке ви задали раніше.

`@instructions`
- Допишіть код, який створює список `areas`. Побудуйте його так, щоб спочатку йшла назва кожної кімнати як рядок, а потім її площа. Тобто додайте рядки `"hallway"`, `"kitchen"` і `"bedroom"` у відповідні місця.
- Знову виведіть `areas`; чи став вивід цього разу інформативнішим?

`@hint`
- Перші чотири елементи списку `areas` записані як `["hallway", hall, "kitchen", kit, ...`.
- Рядок має бути в лапках `""`.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Adapt list areas
areas = [____, hall, ____, kit, "living room", liv, ____, bed, "bathroom", bath]

# Print areas
____
```

`@solution`
```{python}
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Adapt list areas
areas = ["hallway", hall, "kitchen", kit, "living room", liv, "bedroom", bed, "bathroom", bath]

# Print areas
print(areas)
```

`@sct`
```{python}
objs = ["hall", "kit", "liv", "bed", "bath"]
predef_msg = "Не видаляйте та не редагуйте попередньо визначені змінні!"
areas_msg = "Ви не призначили правильне значення для `areas`. Перегляньте інструкції ще раз. Переконайтеся, що кожного разу розміщуєте назву кімнати перед змінною, що містить площу. Порядок тут має значення! Уважно перевірте на наявність друкарських помилок."

Ex().check_correct(
  check_object("areas").has_equal_value(incorrect_msg = areas_msg),
  multi([ check_object(obj, missing_msg = predef_msg).has_equal_value(incorrect_msg = predef_msg) for obj in objs])
)

Ex().has_printout(0, not_printed_msg = "__JINJA__:Чи використали Ви `{{sol_call}}` для виведення списку `areas` в кінці Вашого скрипту?")

success_msg("Чудово! Цей список містить як рядки, так і числа з плаваючою комою, але для Python це не проблема!")
```

---

## Список зі списків

```yaml
type: NormalExercise
key: 9158c577b0
lang: python
xp: 100
skills:
  - 2
```

Як дата-сайєнтист(ка), ви часто працюватимете з великими обсягами даних, і логічно буде згрупувати частину з них.

Замість того щоб створювати список зі строк і чисел з плаваючою крапкою, які представляють назви та площі кімнат у вашому будинку, ви можете створити список зі списків.

Пам'ятайте: `"hallway"` — це рядок, а `hall` — змінна, що представляє число з плаваючою крапкою `11.25`, яке ви вказали раніше.

`@instructions`
- Завершіть список зі списків так, щоб він також містив дані про спальню та ванну кімнату. Введіть їх у правильному порядку!
- Виведіть `house`; чи такий спосіб структурування даних здається вам логічнішим?

`@hint`
- Додайте підсписки до списку `house`, вставивши `["bedroom", bed]` і `["bathroom", bath]` у квадратні дужки.
- Не забудьте поставити кому `,` після кожного підсписку.
- Щоб надрукувати змінну `x`, напишіть на новому рядку `print(x)`.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# House information as list of lists
house = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv],
        ____,
        ____]

# Print out house
____
```

`@solution`
```{python}
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# House information as list of lists
house = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv],
         ["bedroom", bed],
         ["bathroom", bath]]

# Print out house
print(house)
```

`@sct`
```{python}
predef_msg = "Не видаляйте та не редагуйте попередньо визначені змінні!"
house_msg = "Ви не призначили правильне значення для `house`. Перегляньте інструкції ще раз. Розширте список списків, щоб він включав список для кожної пари назви кімнати та площі кімнати. Зверніть увагу на порядок і друкарські помилки!"

Ex().check_correct(
    check_object("house").has_equal_value(incorrect_msg = house_msg),
    multi(
        check_object('hall', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
        check_object('kit', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
        check_object('liv', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
        check_object('bed', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
        check_object('bath', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg)
    )
)

Ex().has_printout(0, not_printed_msg = "__JINJA__:Ви використали `{{sol_call}}`, щоб вивести вміст `house`?")

success_msg("Чудово! Готуйтеся дізнатися про підмножини списків!")
```

---

## Вибірка зі списків

```yaml
type: VideoExercise
key: c076b5a69c
xp: 50
```

`@projector_key`
fc15ba5cb9485456df8589130b519ea3

---

## Індексування — і вперед

```yaml
type: NormalExercise
key: c3ce582e32
lang: python
xp: 100
skills:
  - 2
```

Вибирати елементи зі списків Python — дуже просто. Подивіться на приклад нижче: він створює список `x` і потім вибирає з нього «b». Памʼятайте, це другий елемент, отже його індекс — 1. Також можна використовувати відʼємні індекси.

```
x = ["a", "b", "c", "d"]
x[1]
x[-3] # той самий результат!
```

Памʼятаєте список `areas` з попередніх завдань, де є і рядки, і числа з плаваючою крапкою? Його вже оголошено в скрипті. Додайте правильний код, щоб потренуватися у вибірці елементів зі списку в Python.

`@instructions`
- Виведіть другий елемент зі списку `areas` (його значення `11.25`).
- Виберіть і виведіть останній елемент `areas`, тобто `9.50`. Тут зручно використати відʼємний індекс!
- Виберіть число, що відповідає площі вітальні (`20.0`), і виведіть його.

`@hint`
- Використайте `x[1]`, щоб вибрати другий елемент списку `x`.
- Використайте `x[-1]`, щоб вибрати останній елемент списку `x`.
- Обовʼязково обгорніть операції індексування викликом `print()`.
- Число, що відповідає площі вітальні, є шостим елементом списку, тож тут потрібен індекс `[5]`. `area[4]` виведе рядок!

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Print out second element from areas
print(areas[____])

# Print out last element from areas
print(areas[____])

# Print out the area of the living room
print(areas[____])
```

`@solution`
```{python}
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Print out second element from areas
print(areas[1])

# Print out last element from areas
print(areas[-1])

# Print out the area of the living room
print(areas[5])
```

`@sct`
```{python}
msg = "Не видаляйте та не редагуйте попередньо визначений список `areas`."
Ex().check_object("areas", missing_msg = msg).has_equal_value(incorrect_msg = msg)
Ex().has_printout(0, not_printed_msg = "Перегляньте свій код, щоб вивести другий елемент у `areas`, який знаходиться за індексом `1`.")
Ex().has_printout(1, not_printed_msg = "Перегляньте свій код, щоб вивести останній елемент у `areas`, який знаходиться за індексом `-1`.")
Ex().has_printout(2, not_printed_msg = "Перегляньте свій код, щоб вивести площу вітальні. Вона знаходиться за індексом `5`.")
success_msg("Гарна робота!")
```

---

## Нарізання списків (slicing)

```yaml
type: NormalExercise
key: 7f08642d18
lang: python
xp: 100
skills:
  - 2
```

Вибір окремих значень зі списку — це лише частина задачі. Ви також можете _відсікати_ (slice) список, тобто вибирати з нього кілька елементів. Скористайтеся такою синтаксичною конструкцією:

```
my_list[start:end]
```

Індекс `start` включається, тоді як індекс `end` — _ні_. Водночас можна не зазначати ці індекси. Якщо ви не вкажете індекс `start`, Python зрозуміє, що зріз слід починати від початку списку.

`@instructions`
- За допомогою зрізу створіть список `downstairs`, що містить перші 6 елементів `areas`.
- Створіть `upstairs` як останні `4` елементи `areas`. Цього разу спростіть зріз, опустивши індекс `end`.
- Виведіть і `downstairs`, і `upstairs` за допомогою `print()`.

`@hint`
- Використайте дужки `[0:6]`, щоб отримати перші шість елементів списку.
- Щоб отримати все, окрім перших 5 елементів списку `l`, скористайтеся `l[5:]`.
- Додайте два виклики `print()`, щоб вивести `downstairs` і `upstairs`.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Use slicing to create downstairs
downstairs = areas[____]

# Use slicing to create upstairs
upstairs = areas[____]

# Print out downstairs and upstairs
____
____
```

`@solution`
```{python}
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Use slicing to create downstairs
downstairs = areas[0:6]

# Use slicing to create upstairs
upstairs = areas[6:]

# Print out downstairs and upstairs
print(downstairs)
print(upstairs)
```

`@sct`
```{python}
msg = "Не видаляйте та не редагуйте попередньо визначений список `areas`."
Ex().check_object("areas", missing_msg = msg).has_equal_value(incorrect_msg = msg)

patt = "`%s` є неправильним. Використовуйте `areas[%s]` та зрізи для вибору потрібних елементів, або щось еквівалентне."
Ex().check_object("downstairs").has_equal_value(incorrect_msg = patt % ('downstairs', '0:6'))
Ex().check_object("upstairs").has_equal_value(incorrect_msg = patt % ("upstairs",":6"))

Ex().has_printout(0, not_printed_msg="Ви вивели `downstairs` після його обчислення?")
Ex().has_printout(1, not_printed_msg="Ви вивели `upstairs` після його обчислення?")

success_msg("Чудово!")
```

---

## Вибірка зі списків списків

```yaml
type: NormalExercise
key: dbbbd306cf
xp: 100
```

Список Python також може містити інші списки.

Щоб робити вибірку зі списків списків, використовуйте той самий прийом, що й раніше: квадратні дужки. Для списку `house` це виглядатиме так:

```
house[2][0]
```

`@instructions`
- Зробіть вибірку зі списку `house`, щоб отримати число з рухомою крапкою `9.5`.

`@hint`
- Розбийте завдання на кроки. Спочатку потрібно дістатися до останнього елемента списку, `["bathroom", 9.50]`. Згадайте, що індекс останнього елемента — `-1`.
- Далі потрібно взяти другий елемент із `["bathroom", 9.50]`, який має індекс `1`.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
house = [["hallway", 11.25],
         ["kitchen", 18.0],
         ["living room", 20.0],
         ["bedroom", 10.75],
         ["bathroom", 9.50]]

# Subset the house list
house___
```

`@solution`
```{python}
house = [["hallway", 11.25],
         ["kitchen", 18.0],
         ["living room", 20.0],
         ["bedroom", 10.75],
         ["bathroom", 9.50]]

# Subset the house list
house[-1][1]
```

`@sct`
```{python}
Ex().check_or(
  has_code("house[-1][1]", pattern=False),
  has_code("house[4][1]", pattern=False)
)

success_msg("Правильно! Остання частина головоломки зі списками - це маніпуляція.")
```

---

## Робота зі списками

```yaml
type: VideoExercise
key: d7fe818b3a
xp: 50
```

`@projector_key`
355ed52d2fb0d67508c6a311b7cbc6d3

---

## Заміна елементів списку

```yaml
type: NormalExercise
key: 4e1bba1b55
lang: python
xp: 100
skills:
  - 2
```

Щоб замінити елементи списку, виділіть підмножину списку та присвойте нові значення цій підмножині. Ви можете вибирати окремі елементи або змінювати цілі зрізи списку за один раз.

У цій і наступних вправах ви продовжите працювати зі списком `areas`, що містить назви та площі різних кімнат у будинку.

`@instructions`
- Оновіть площу ванної кімнати до `10.50` квадратних метрів замість `9.50`, використавши негативну індексацію.
- Зробіть список `areas` більш трендовим! Змініть `"living room"` на `"chill zone"`. Цього разу не використовуйте негативну індексацію.

`@hint`
- Щоб оновити площу ванної кімнати, визначте підмножину з площею ванної (це останній елемент списку!).
- Потім замініть значення новою площею ванної, присвоївши її цій підмножині.
- Зробіть так само, щоб оновити назву `"living room"`, яка має індекс 4.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Correct the bathroom area


# Change "living room" to "chill zone"

```

`@solution`
```{python}
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Correct the bathroom area
areas[-1] = 10.50

# Change "living room" to "chill zone"
areas[4] = "chill zone"
```

`@sct`
```{python}
bathroom_msg = 'Ви можете використати `areas[-1] = 10.50`, щоб оновити площу ванної кімнати.'
chillzone_msg = 'Ви можете використати `areas[4] = "chill zone"`, щоб оновити назву вітальні.'
Ex().check_correct(
  check_object('areas').has_equal_value(incorrect_msg = 'Ваші зміни до `areas` не призвели до правильного списку. Ви впевнені, що використали правильні операції підмножини? Якщо сумніваєтеся, ви можете скористатися підказкою!'),
  multi(
    has_equal_value(expr_code='areas[-1]', override=10.50, incorrect_msg = bathroom_msg),
    has_equal_value(expr_code='areas[4]', override='chill zone', incorrect_msg = chillzone_msg),
  )
)
success_msg('Чудово! Як показано в прикладі коду, ви також можете зрізати список і замінити його іншим списком, щоб оновити кілька елементів в одній команді.')
```

---

## Розширення списку

```yaml
type: NormalExercise
key: ff0fe8d967
lang: python
xp: 100
skills:
  - 2
```

Якщо ви можете змінювати елементи в списку, то, звісно, хочете вміти й додавати їх, чи не так? Для цього можна використати оператор `+`:

```
x = ["a", "b", "c", "d"]
y = x + ["e", "f"]
```

Ви щойно виграли в лотерею — чудово! Ви вирішили збудувати басейн із будиночком і гараж. Чи можете додати цю інформацію до списку `areas`?

`@instructions`
- Використайте оператор `+`, щоб додати список `["poolhouse", 24.5]` у кінець списку `areas`. Збережіть отриманий список як `areas_1`.
- Далі розширте `areas_1`, додавши дані про ваш гараж. Додайте рядок `"garage"` і число з плаваючою крапкою `15.45`. Назвіть отриманий список `areas_2`.

`@hint`
- Дотримуйтеся прикладу коду в завданні. Тут `x` — це `areas`, а `["e", "f"]` — це `["poolhouse", 24.5]`.
- Щоб додати більше елементів до `areas_1`, використайте `areas_1 + ["element", 123]`.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create the areas list and make some changes
areas = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0,
         "bedroom", 10.75, "bathroom", 10.50]

# Add poolhouse data to areas, new list is areas_1
areas_1 = ____

# Add garage data to areas_1, new list is areas_2
areas_2 = ____
```

`@solution`
```{python}
# Create the areas list (updated version)
areas = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0,
         "bedroom", 10.75, "bathroom", 10.50]

# Add poolhouse data to areas, new list is areas_1
areas_1 = areas + ["poolhouse", 24.5]

# Add garage data to areas_1, new list is areas_2
areas_2 = areas_1 + ["garage", 15.45]
```

`@sct`
```{python}
msg = "Не видаляйте та не редагуйте попередньо визначений список `areas`."
Ex().check_object("areas", missing_msg = msg).has_equal_value(incorrect_msg = msg)
Ex().check_object("areas_1").has_equal_value(incorrect_msg = "Використовуйте `areas + [\"poolhouse\", 24.5]`, щоб створити `areas_1`. Уважно перевірте на наявність помилок!")
Ex().check_object("areas_2").has_equal_value(incorrect_msg = "Використовуйте `areas_1 + [\"garage\", 15.45]`, щоб створити `areas_2`. Уважно перевірте на наявність помилок!")
success_msg("Чудово! Список набуває гарного вигляду!")
```

---

## Видалення елементів списку

```yaml
type: NormalExercise
key: 85f792356e
xp: 100
```

Нарешті, ви також можете видаляти елементи зі свого списку. Це можна зробити за допомогою оператора `del`:

```
x = ["a", "b", "c", "d"]
del x[1]
```

Зверніть увагу: щойно ви видалите елемент зі списку, індекси всіх елементів, що йдуть після нього, зміняться!

На жаль, виграш у лотереї виявився не таким уже й великим, тож басейного будиночка не буде. Вам потрібно прибрати його зі списку. Ви вирішили видалити відповідний рядок і число з рухомою крапкою зі списку `areas`.

`@instructions`
- Видаліть рядок і число з рухомою крапкою для `"poolhouse"` зі свого списку `areas`.
- Надрукуйте оновлений список `areas`.

`@hint`
- Вам знадобиться двічі використати `del`, щоб видалити два елементи. Але будьте уважні: індекси змінюються!

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
areas = ["hallway", 11.25, "kitchen", 18.0,
        "chill zone", 20.0, "bedroom", 10.75,
         "bathroom", 10.50, "poolhouse", 24.5,
         "garage", 15.45]

# Delete the poolhouse items from the list


# Print the updated list

```

`@solution`
```{python}
areas = ["hallway", 11.25, "kitchen", 18.0,
        "chill zone", 20.0, "bedroom", 10.75,
         "bathroom", 10.50, "poolhouse", 24.5,
         "garage", 15.45]

# Delete the poolhouse items from the list
del areas[10]
del areas[10]

# Print the updated list
print(areas)
```

`@sct`
```{python}
Ex().check_or(
  multi(
    has_code("del areas[10]", pattern=False),
    has_code("del areas[10]", pattern=False)
  ),
  has_code("del areas[-4:-2]", pattern=False),
  has_code("del(areas[-4:-2])", pattern=False),
  multi(
    has_code("del(areas[10])", pattern=False),
    has_code("del(areas[10])", pattern=False)
  ),
  has_code("del areas[10:12]", pattern=False),
  has_code("del(areas[10:12])", pattern=False),
  multi(
    has_code("del areas[-4]", pattern=False),
    has_code("del areas[-3]", pattern=False)
  ),
  multi(
    has_code("del(areas[-4])", pattern=False),
    has_code("del(areas[-3])", pattern=False)
  )
)

Ex().has_printout(0, not_printed_msg="Ви вивели `areas` після видалення рядка та числа з poolhouse?")
success_msg("Правильно! Пізніше Ви дізнаєтеся про простіші способи видалення конкретних елементів зі списків Python.")
```

---

## Як працюють списки всередині

```yaml
type: NormalExercise
key: af72db9915
lang: python
xp: 100
skills:
  - 2
```

Для цієї вправи вам уже підготовлено код: список з назвою `areas` і копію під назвою `areas_copy`.

Зараз змінюється перший елемент у списку `areas_copy`, а потім виводиться список `areas`. Якщо натиснете кнопку «Запустити код», побачите, що хоча ви змінили `areas_copy`, зміни також з'являються в списку `areas`. Це тому, що `areas` і `areas_copy` посилаються на той самий список.

Якщо ви хочете, щоб зміни в `areas_copy` не впливали на `areas`, потрібно зробити явну копію списку `areas` за допомогою `list()` або зрізу `[:]`.

`@instructions`
- Змініть другу команду, яка створює змінну `areas_copy`, так, щоб `areas_copy` була явною копією `areas`. Після редагування зміни в `areas_copy` не повинні впливати на `areas`. Надішліть відповідь, щоб перевірити це.

`@hint`
- Змініть виклик `areas_copy = areas`. Замість присвоювання `areas` використайте `list(areas)` або `areas[:]`.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Change this command
areas_copy = areas

# Change areas_copy
areas_copy[0] = 5.0

# Print areas
print(areas)
```

`@solution`
```{python}
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Change this command
areas_copy = list(areas)

# Change areas_copy
areas_copy[0] = 5.0

# Print areas
print(areas)
```

`@sct`
```{python}
Ex().check_correct(
  check_object("areas_copy").has_equal_value(incorrect_msg = "Схоже, що `areas_copy` не було оновлено правильно."),
  check_function("list", missing_msg = "Переконайтеся, що використовуєте `list(areas)`, щоб створити `areas_copy`.")
)

mmsg = "Не видаляйте попередньо визначений список `areas`."
imsg = "Переконайтеся, що редагуєте ТІЛЬКИ копію, а не оригінальний список `areas`. Якщо ви не впевнені, як створити копію, перегляньте опис вправи ще раз."
Ex().check_correct(
  check_object("areas", missing_msg = mmsg).has_equal_value(incorrect_msg = imsg),
  check_function("list", missing_msg = "Переконайтеся, що використовуєте `list(areas)`, щоб створити `areas_copy`.")
)

success_msg("Чудово! Різниця між явними та посилальними копіями є тонкою, але може бути дійсно важливою. Намагайтеся пам'ятати, як список зберігається в пам'яті комп'ютера.")
```

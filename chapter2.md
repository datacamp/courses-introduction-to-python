---
title_meta: Глава 2
title: Списки в Python
description: >-
  Научитесь хранить данные в списках, обращаться к ним и изменять их — это
  первый шаг к эффективной работе с большими объёмами данных.
attachments:
  slides_link: 'https://projector-video-pdf-converter.datacamp.com/735/chapter2.pdf'
lessons:
  - nb_of_exercises: 4
    title: Списки в Python
  - nb_of_exercises: 4
    title: Извлечение элементов из списков
  - nb_of_exercises: 5
    title: Работа со списками
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

## Создание списка

```yaml
type: NormalExercise
key: e6c527bf41
lang: python
xp: 100
skills:
  - 2
```

Список — это **составной тип данных**, который позволяет группировать значения вместе. Например:

```
a = "is"
b = "nice"
my_list = ["my", "list", a, b]
```

После того как вы измерили рост членов своей семьи, вы решили собрать некоторые сведения о доме, в котором живёте. Площади различных частей дома уже сохранены в отдельных переменных в этом упражнении.

`@instructions`
- Создайте список `areas`, который содержит площадь прихожей (`hall`), кухни (`kit`), гостиной (`liv`), спальни (`bed`) и ванной комнаты (`bath`) — именно в таком порядке. Используйте заранее заданные переменные.
- Выведите `areas` с помощью функции `print()`.

`@hint`
- Для создания списка можно использовать уже заданные переменные: `areas = [hall, kit, ...]`.
- Убедитесь, что используете квадратные скобки `[]`, а не круглые `()`.
- Кавычки при добавлении переменных в список не нужны.
- Введите `print(areas)`, чтобы вывести список при отправке ответа.

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
predef_msg = "Не удаляйте и не изменяйте предопределённые переменные!"
areas_msg = "Определите `areas` как список, содержащий все переменные площадей в правильном порядке: `[hall, kit, liv, bed, bath]`. Проверьте наличие опечаток. Список не должен содержать ничего лишнего!"

Ex().check_correct(
    has_printout(0, not_printed_msg = "__JINJA__:Использовали ли вы `{{sol_call}}` для вывода списка `areas` в конце вашего скрипта?"),
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

success_msg("Отлично! Список здесь гораздо удобнее, не правда ли?")
```

---

## Создание списков с элементами разных типов

```yaml
type: NormalExercise
key: 1702a8bcdc
lang: python
xp: 100
skills:
  - 2
```

Хотя это не так распространено, список может содержать элементы разных типов Python: строки, числа с плавающей точкой и логические значения.

Теперь вы добавите названия комнат в свой список, чтобы видеть название и площадь каждой комнаты рядом.

Часть кода уже написана за вас. Обратите внимание: `"bathroom"` — это строка, а `bath` — переменная, которая хранит значение `9.50`, заданное ранее.

`@instructions`
- Завершите код, который создаёт список `areas`. Составьте список так, чтобы сначала шло название комнаты в виде строки, а затем её площадь. Другими словами, добавьте строки `"hallway"`, `"kitchen"` и `"bedroom"` в нужные места.
- Выведите `areas` ещё раз — стал ли результат более наглядным?

`@hint`
- Первые четыре элемента списка `areas` записаны как `["hallway", hall, "kitchen", kit, ...`.
- Строка должна быть заключена в кавычки `""`.

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
predef_msg = "Не удаляйте и не изменяйте предопределённые переменные!"
areas_msg = "Вы не присвоили правильное значение переменной `areas`. Ещё раз ознакомьтесь с инструкциями. Убедитесь, что каждый раз название комнаты указывается перед переменной, содержащей её площадь. Порядок важен! Проверьте наличие опечаток."

Ex().check_correct(
  check_object("areas").has_equal_value(incorrect_msg = areas_msg),
  multi([ check_object(obj, missing_msg = predef_msg).has_equal_value(incorrect_msg = predef_msg) for obj in objs])
)

Ex().has_printout(0, not_printed_msg = "__JINJA__:Использовали ли вы `{{sol_call}}` для вывода списка `areas` в конце вашего скрипта?")

success_msg("Отлично! Этот список содержит как строки, так и числа с плавающей точкой, но для Python это не проблема!")
```

---

## Список списков

```yaml
type: NormalExercise
key: 9158c577b0
lang: python
xp: 100
skills:
  - 2
```

В работе специалиста по данным часто приходится иметь дело с большими объёмами данных, и группировка данных существенно упрощает работу с ними.

Вместо того чтобы создавать один список из строк и чисел с плавающей точкой, представляющих названия и площади комнат в вашем доме, можно создать список списков.

Помните: `"hallway"` — это строка, тогда как `hall` — переменная, которая представляет значение `11.25`, заданное ранее.

`@instructions`
- Дополните список списков так, чтобы он также содержал данные о спальне и ванной комнате. Убедитесь, что вы вводите их в правильном порядке!
- Выведите `house` на экран: стал ли такой способ структурирования данных более удобным?

`@hint`
- Добавьте _подсписки_ в список `house`, вставив `["bedroom", bed]` и `["bathroom", bath]` внутри квадратных скобок.
- Не забудьте добавить запятую `,` после каждого подсписка.
- Чтобы вывести переменную `x`, напишите `print(x)` на новой строке.

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
predef_msg = "Не удаляйте и не изменяйте предопределённые переменные!"
house_msg = "Вы не присвоили переменной `house` правильное значение. Ещё раз ознакомьтесь с инструкциями. Расширьте список списков так, чтобы он включал список для каждой пары: название комнаты и её площадь. Обратите внимание на порядок и опечатки!"

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

Ex().has_printout(0, not_printed_msg = "__JINJA__:Использовали ли вы `{{sol_call}}` для вывода содержимого `house`?")

success_msg("Отлично! Приготовьтесь узнать о выборке элементов из списка!")
```

---

## Извлечение элементов из списков

```yaml
type: VideoExercise
key: c076b5a69c
xp: 50
```

`@projector_key`
fc15ba5cb9485456df8589130b519ea3

---

## Извлекаем элементы

```yaml
type: NormalExercise
key: c3ce582e32
lang: python
xp: 100
skills:
  - 2
```

Извлечение элементов из списков Python — дело простое. Рассмотрите пример ниже: здесь создаётся список `x`, а затем из него выбирается элемент `"b"`. Помните, что это второй элемент, поэтому его индекс равен 1. Также можно использовать отрицательную индексацию.

```
x = ["a", "b", "c", "d"]
x[1]
x[-3] # тот же результат!
```

Вспомните список `areas` из предыдущего упражнения, который содержит и строки, и числа с плавающей точкой. Его определение уже есть в скрипте. Добавьте нужный код для извлечения элементов из этого списка.

`@instructions`
- Выведите на экран второй элемент списка `areas` (его значение — `11.25`).
- Извлеките и выведите последний элемент списка `areas` — `9.50`. Здесь удобно воспользоваться отрицательным индексом!
- Выберите число, представляющее площадь гостиной (`20.0`), и выведите его на экран.

`@hint`
- Используйте `x[1]`, чтобы выбрать второй элемент списка `x`.
- Используйте `x[-1]`, чтобы выбрать последний элемент списка `x`.
- Не забудьте обернуть операции извлечения элементов в вызов `print()`.
- Число, представляющее площадь гостиной, является 6-м элементом списка, поэтому здесь нужно использовать `[5]`. `area[4]` вернёт строку!

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
msg = "Не удаляйте и не изменяйте предопределённый список `areas`."
Ex().check_object("areas", missing_msg = msg).has_equal_value(incorrect_msg = msg)
Ex().has_printout(0, not_printed_msg = "Ещё раз проверьте свой код, чтобы вывести на экран второй элемент в `areas`, который находится по индексу `1`.")
Ex().has_printout(1, not_printed_msg = "Ещё раз проверьте свой код, чтобы вывести на экран последний элемент в `areas`, который находится по индексу `-1`.")
Ex().has_printout(2, not_printed_msg = "Ещё раз проверьте свой код, чтобы вывести на экран площадь гостиной. Она находится по индексу `5`.")
success_msg("Отличная работа!")
```

---

## Срезы списков

```yaml
type: NormalExercise
key: 7f08642d18
lang: python
xp: 100
skills:
  - 2
```

Выбор отдельных значений из списка — это лишь часть возможностей. Список также можно _нарезать_, то есть выбирать из него сразу несколько элементов. Для этого используйте следующий синтаксис:

```
my_list[start:end]
```

Элемент с индексом `start` включается в результат, а элемент с индексом `end` — _нет_. При этом оба индекса можно не указывать. Если не задать индекс `start`, Python начнёт срез с самого начала списка.

`@instructions`
- С помощью среза создайте список `downstairs`, содержащий первые 6 элементов списка `areas`.
- Создайте список `upstairs` из последних `4` элементов списка `areas`. На этот раз упростите срез, опустив конечный индекс.
- Выведите оба списка — `downstairs` и `upstairs` — с помощью функции `print()`.

`@hint`
- Используйте срез `[0:6]`, чтобы получить первые шесть элементов списка.
- Чтобы получить все элементы списка `l`, кроме первых пяти, используйте `l[5:]`.
- Добавьте два вызова `print()`, чтобы вывести `downstairs` и `upstairs`.

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
msg = "Не удаляйте и не редактируйте предопределённый список `areas`."
Ex().check_object("areas", missing_msg = msg).has_equal_value(incorrect_msg = msg)

patt = "`%s` указано неверно. Используйте `areas[%s]` и срезы для выбора нужных элементов или эквивалентный способ."
Ex().check_object("downstairs").has_equal_value(incorrect_msg = patt % ('downstairs', '0:6'))
Ex().check_object("upstairs").has_equal_value(incorrect_msg = patt % ("upstairs",":6"))

Ex().has_printout(0, not_printed_msg="Вы вывели на экран `downstairs` после его вычисления?")
Ex().has_printout(1, not_printed_msg="Вы вывели на экран `upstairs` после его вычисления?")

success_msg("Отлично!")
```

---

## Подмножества списков списков

```yaml
type: NormalExercise
key: dbbbd306cf
xp: 100
```

Список Python может содержать другие списки.

Чтобы извлекать элементы из списков списков, используйте тот же приём, что и раньше: квадратные скобки. Для списка `house` это выглядит примерно так:

```
house[2][0]
```

`@instructions`
- Обратитесь к списку `house` так, чтобы получить число с плавающей точкой `9.5`.

`@hint`
- Решайте задачу пошагово. Сначала нужно добраться до последнего элемента списка — `["bathroom", 9.50]`. Вспомните, что индекс последнего элемента равен `-1`.
- Затем нужно получить второй элемент списка `["bathroom", 9.50]`, который находится по индексу `1`.

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

success_msg("Правильно! Последний элемент головоломки со списками — это манипуляция.")
```

---

## Управление списками

```yaml
type: VideoExercise
key: d7fe818b3a
xp: 50
```

`@projector_key`
355ed52d2fb0d67508c6a311b7cbc6d3

---

## Замена элементов списка

```yaml
type: NormalExercise
key: 4e1bba1b55
lang: python
xp: 100
skills:
  - 2
```

Чтобы заменить элементы списка, нужно выбрать нужный фрагмент и присвоить ему новое значение. Можно изменять как отдельные элементы, так и целые срезы списка.

В этом и последующих упражнениях вы продолжите работу со списком `areas`, который содержит названия и площади различных комнат в доме.

`@instructions`
- Обновите площадь ванной комнаты: замените `9.50` на `10.50` квадратных метра, используя отрицательную индексацию.
- Сделайте список `areas` более современным! Замените `"living room"` на `"chill zone"`. На этот раз не используйте отрицательную индексацию.

`@hint`
- Чтобы обновить площадь ванной комнаты, выберите соответствующий элемент списка (это последний элемент!).
- Затем присвойте этому элементу новое значение площади.
- Аналогичным образом обновите название `"living room"` — оно находится по индексу 4.

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
bathroom_msg = 'Используйте `areas[-1] = 10.50` для обновления площади ванной комнаты.'
chillzone_msg = 'Используйте `areas[4] = "chill zone"` для обновления названия гостиной.'
Ex().check_correct(
  check_object('areas').has_equal_value(incorrect_msg = 'Внесённые вами изменения в `areas` не привели к правильному списку. Вы уверены, что использовали правильные операции подмножества? Если сомневаетесь, воспользуйтесь подсказкой!'),
  multi(
    has_equal_value(expr_code='areas[-1]', override=10.50, incorrect_msg = bathroom_msg),
    has_equal_value(expr_code='areas[4]', override='chill zone', incorrect_msg = chillzone_msg),
  )
)
success_msg('Отлично! Как показано в примере кода, вы также можете выбрать срез списка и заменить его другим списком, чтобы обновить несколько элементов одной командой.')
```

---

## Расширение списка

```yaml
type: NormalExercise
key: ff0fe8d967
lang: python
xp: 100
skills:
  - 2
```

Раз уж вы умеете изменять элементы списка, хочется уметь и добавлять новые, не правда ли? Для этого используйте оператор `+`:

```
x = ["a", "b", "c", "d"]
y = x + ["e", "f"]
```

Вы выиграли в лотерею — поздравляем! Вы решаете построить бассейный домик и гараж. Добавьте эту информацию в список `areas`.

`@instructions`
- Используйте оператор `+`, чтобы добавить список `["poolhouse", 24.5]` в конец списка `areas`. Сохраните результат в переменную `areas_1`.
- Расширьте список `areas_1`, добавив данные о гараже. Добавьте строку `"garage"` и число с плавающей точкой `15.45`. Назовите результирующий список `areas_2`.

`@hint`
- Следуйте образцу кода из задания. Здесь `x` — это `areas`, а `["e", "f"]` — это `["poolhouse", 24.5]`.
- Чтобы добавить элементы в `areas_1`, используйте конструкцию `areas_1 + ["element", 123]`.

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
msg = "Не удаляйте и не изменяйте предопределённый список `areas`."
Ex().check_object("areas", missing_msg = msg).has_equal_value(incorrect_msg = msg)
Ex().check_object("areas_1").has_equal_value(incorrect_msg = "Используйте `areas + [\"poolhouse\", 24.5]` для создания `areas_1`. Проверьте правильность написания!")
Ex().check_object("areas_2").has_equal_value(incorrect_msg = "Используйте `areas_1 + [\"garage\", 15.45]` для создания `areas_2`. Проверьте правильность написания!")
success_msg("Отлично! Список приобретает хорошую форму!")
```

---

## Удаление элементов списка

```yaml
type: NormalExercise
key: 85f792356e
xp: 100
```

Наконец, элементы из списка можно удалять. Для этого используется оператор `del`:

```
x = ["a", "b", "c", "d"]
del x[1]
```

Обратите внимание: как только элемент удалён из списка, индексы всех следующих за ним элементов изменяются!

К сожалению, выигрыш в лотерею оказался не таким большим, и бассейный домик построить не получится. Его нужно убрать из списка. Удалите соответствующую строку и число с плавающей точкой из списка `areas`.

`@instructions`
- Удалите строку и число с плавающей точкой, соответствующие `"poolhouse"`, из списка `areas`.
- Выведите обновлённый список `areas`.

`@hint`
- Вам потребуется использовать `del` дважды, чтобы удалить два элемента. Будьте внимательны: индексы элементов после удаления изменятся!

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

Ex().has_printout(0, not_printed_msg="Вы вывели на экран `areas` после удаления строки и числа с плавающей точкой, относящихся к бассейну?")
success_msg("Верно! Позже вы узнаете о более простых способах удаления определённых элементов из списков Python.")
```

---

## Как устроены списки изнутри

```yaml
type: NormalExercise
key: af72db9915
lang: python
xp: 100
skills:
  - 2
```

В этом упражнении уже есть готовый код: список `areas` и его копия `areas_copy`.

Первый элемент списка `areas_copy` изменяется, после чего выводится список `areas`. Если нажать кнопку **Запустить код**, вы увидите, что изменение `areas_copy` затрагивает и список `areas`. Это происходит потому, что `areas` и `areas_copy` указывают на один и тот же список.

Чтобы изменения в `areas_copy` не влияли на `areas`, нужно создать явную копию списка `areas` — с помощью функции `list()` или среза `[:]`.

`@instructions`
- Измените вторую команду, которая создаёт переменную `areas_copy`, так чтобы `areas_copy` стала явной копией `areas`. После этого изменения в `areas_copy` не должны влиять на `areas`. Нажмите **Отправить ответ**, чтобы проверить результат.

`@hint`
- Измените вызов `areas_copy = areas`. Вместо прямого присваивания `areas` используйте `list(areas)` или `areas[:]`.

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
  check_object("areas_copy").has_equal_value(incorrect_msg = "Похоже, что `areas_copy` не был обновлён корректно."),
  check_function("list", missing_msg = "Убедитесь, что используете `list(areas)` для создания `areas_copy`.")
)

mmsg = "Не удаляйте предопределённый список `areas`."
imsg = "Убедитесь, что вносите изменения ТОЛЬКО в копию, а не в оригинальный список `areas`. Если вы не уверены, как создать копию, ещё раз ознакомьтесь с описанием задания."
Ex().check_correct(
  check_object("areas", missing_msg = mmsg).has_equal_value(incorrect_msg = imsg),
  check_function("list", missing_msg = "Убедитесь, что используете `list(areas)` для создания `areas_copy`.")
)

success_msg("Отлично! Разница между явным копированием и копированием по ссылке незначительна, но может быть очень важна. Постарайтесь помнить о том, как список хранится в памяти компьютера.")
```

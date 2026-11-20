---
title_meta: Глава 1
title: Основы Python
description: >-
  Знакомство с основными концепциями Python. Вы научитесь работать с Python в
  интерактивном режиме и с помощью скриптов, создадите первые переменные и
  освоите базовые типы данных.
attachments:
  slides_link: 'https://projector-video-pdf-converter.datacamp.com/735/chapter1.pdf'
free_preview: true
lessons:
  - nb_of_exercises: 3
    title: 'Привет, Python!'
  - nb_of_exercises: 5
    title: Переменные и типы данных
---

## Привет, Python!

```yaml
type: VideoExercise
key: f644a48d5d
xp: 50
```

`@projector_key`
d8fcd4c930027fa4e1c3870c7e7e0ff1

---

## Ваш первый код на Python

```yaml
type: NormalExercise
key: bdc52f0e19
lang: python
xp: 100
skills:
  - 2
```

Пришло время запустить ваш первый код на Python!

Перейдите к коду и нажмите кнопку запуска, чтобы увидеть вывод.

`@instructions`
- Нажмите кнопку запуска кода, чтобы увидеть результат выполнения `print(5 / 8)`.

`@hint`
- Запустите код, прежде чем отправлять ответ, — так у вас будет время изучить вывод.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Hit run code to see the output!
print(5 / 8)
```

`@solution`
```{python}
# Hit run code to see the output!
print(5 / 8)
```

`@sct`
```{python}
Ex().has_printout(0, not_printed_msg = "__JINJA__:Вы использовали `{{sol_call}}` для вывода `5 / 8`?")
success_msg("Отлично! Переходим к следующему!")
```

---

## Python как калькулятор

```yaml
type: NormalExercise
key: 0f7c039428
lang: python
xp: 100
skills:
  - 2
```

Python отлично справляется с базовыми вычислениями: сложением, вычитанием, умножением и делением.

В скрипте уже есть несколько примеров.

Теперь ваша очередь — попробуйте написать код самостоятельно.

`@instructions`
- Выведите результат вычитания `5` из `5` под комментарием `# Subtraction` с помощью `print()`.
- Выведите результат умножения `3` на `5` под комментарием `# Multiplication`.

`@hint`
- Чтобы вывести результат, используйте функцию `print()`.
- Для вычитания используйте `-`, для умножения — `*`.

`@pre_exercise_code`
```{python}
 
```

`@sample_code`
```{python}
# Addition and division
print(4 + 5)
print(10 / 2)

# Subtraction
print()

# Multiplication

```

`@solution`
```{python}
# Addition and division
print(4 + 5)
print(10 / 2)

# Subtraction
print(5 - 5)

# Multiplication
print(3 * 5)
```

`@sct`
```{python}
Ex().has_printout(0, not_printed_msg = "Вы использовали `print(4 + 5)` для вывода результата сложения?")

Ex().has_printout(1, not_printed_msg = "Вы использовали `print(5 - 5)` для вывода результата вычитания?")

Ex().has_printout(2, not_printed_msg = "Вы использовали `print(3 * 5)` для вывода результата умножения?")

Ex().has_printout(3, not_printed_msg = "Вы использовали `print(10 / 2)` для вывода результата деления?")

success_msg("Верно! Python поможет вам выполнять математические вычисления — это свойство окажется полезным для анализа данных по мере развития ваших навыков.")
```

---

## Переменные и типы данных

```yaml
type: VideoExercise
key: c2e396792e
xp: 50
```

`@projector_key`
433dcfcfedaee070cbf440491c402e3b

---

## Присваивание переменных

```yaml
type: NormalExercise
key: 4bf65ad83e
lang: python
xp: 100
skills:
  - 2
```

В Python переменная позволяет обращаться к значению по имени. Чтобы создать переменную `x` со значением `5`, используйте `=`, как в примере:

```
x = 5
```

Теперь вместо самого значения `5` можно использовать имя переменной — `x`.

Помните: `=` в Python означает _присваивание_, а не проверку равенства! Попробуйте сами — замените `____` на нужный код.

`@instructions`
- Создайте переменную `savings` со значением `100`.
- Выведите значение этой переменной, введя `print(savings)` в скрипте.

`@hint`
- Введите `savings = 100`, чтобы создать переменную `savings`.
- После создания переменной `savings` введите `print(savings)`.
- В финальном коде не должно остаться ни одного `____`.

`@pre_exercise_code`
```{python}
 
```

`@sample_code`
```{python}
# Create a variable savings
____

# Print out savings
____
```

`@solution`
```{python}
# Create a variable savings
savings = 100

# Print out savings
print(savings)
```

`@sct`
```{python}
Ex().check_object("savings").has_equal_value(incorrect_msg="Присвойте переменной `savings` значение `100`.")
Ex().has_printout(0, not_printed_msg = "Выведите на экран `savings`, созданную вами переменную, с помощью `print(savings)`.")
success_msg("Отлично! Теперь попробуем выполнить некоторые вычисления с этой переменной!")
```

---

## Вычисления с переменными

```yaml
type: NormalExercise
key: ff06cedeb4
lang: python
xp: 100
skills:
  - 2
```

Вы уже создали переменную для сбережений — теперь давайте посчитаем!

Вместо того чтобы использовать конкретные числа, можно задействовать переменные.

Сколько денег вы накопите за четыре месяца, если откладывать по 10 долларов в месяц?

`@instructions`
- Создайте переменную `monthly_savings` со значением `10` и переменную `num_months` со значением `4`.
- Умножьте `monthly_savings` на `num_months` и присвойте результат переменной `new_savings`.
- Выведите значение `new_savings` с помощью `print()`.

`@hint`
- С переменными можно выполнять вычисления так же, как и с числами: вместо `10 * 4` используйте переменные!
- Используйте `print()`, чтобы вывести значение `new_savings`.
- Проверьте правильность написания переменных!

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create the variables monthly_savings and num_months



# Multiply monthly_savings and num_months
new_savings = ____

# Print new_savings

```

`@solution`
```{python}
# Create the variables monthly_savings and num_months
monthly_savings = 10
num_months = 4

# Multiply monthly_savings and num_months
new_savings = monthly_savings * num_months

# Print new_savings
print(new_savings)
```

`@sct`
```{python}
Ex().check_object("monthly_savings").has_equal_value(incorrect_msg = "Вы сохранили `10` в `monthly_savings` с помощью `monthly_savings = 10`?")
Ex().check_object("num_months").has_equal_value(incorrect_msg = "Вы сохранили `4` в `num_months` с помощью `num_months = 4`?")
Ex().check_object("new_savings").has_equal_value(incorrect_msg = "Вы использовали правильные переменные и символы для умножения? Ожидалось `monthly_savings * num_months`, но получено что-то другое.")
# Ex().check_object("total_savings").has_equal_value(incorrect_msg = "Вы использовали правильные переменные и символы для сложения? Ожидалось `savings + new_savings`, но получено что-то другое.")

Ex().has_printout(0, not_printed_msg="Не забудьте вывести на экран `new_savings` в конце вашего скрипта.")

success_msg("У вас $40 в новых сбережениях!")
```

---

## Другие типы переменных

```yaml
type: NormalExercise
key: 006b48561f
lang: python
xp: 100
skills:
  - 2
```

В предыдущем упражнении вы работали с целочисленным типом данных Python:

- `int`, или целое число: число без дробной части. Например, `savings` со значением `100` — это целое число.

Помимо числовых типов данных, существуют ещё три широко используемых типа:

- `float`, или число с плавающей точкой: число, у которого есть целая и дробная части, разделённые точкой. Например, `1.1` — это число с плавающей точкой.
- `str`, или строка: тип для представления текста. Строку можно создать с помощью одинарных или двойных кавычек.
- `bool`, или булев тип: тип для представления логических значений. Он может принимать только значения `True` или `False` (регистр важен!).

`@instructions`
- Создайте новую переменную с плавающей точкой `half` со значением `0.5`.
- Создайте новую строку `intro` со значением `"Hello! How are you?"`.
- Создайте новую булеву переменную `is_good` со значением `True`.

`@hint`
- Чтобы создать переменную в Python, используйте `=`. Не забудьте заключить строку в одинарные или двойные кавычки.
- В Python существует только два булевых значения: `True` и `False`. Варианты `TRUE`, `true`, `FALSE`, `false` и другие не будут приняты.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create a variable half


# Create a variable intro


# Create a variable is_good

```

`@solution`
```{python}
# Create a variable half
half = 0.5

# Create a variable intro
intro = "Hello! How are you?"

# Create a variable is_good
is_good = True
```

`@sct`
```{python}
Ex().check_object("half").has_equal_value(incorrect_msg = "Вы сохранили число с плавающей точкой `0.5` в переменную `half`?")

Ex().check_object("intro").has_equal_value(incorrect_msg = "Хм, в вашей переменной `intro` что-то не так. Проверьте правильность написания и убедитесь, что вы использовали кавычки.")

Ex().check_object("is_good").has_equal_value(incorrect_msg = "Вы написали булево значение с заглавной буквы? Помните, что здесь не нужно использовать кавычки.")

success_msg("Отлично!")
```

---

## Операции с разными типами данных

```yaml
type: BulletExercise
key: 4d0d83cc02
xp: 100
```

В Python переменные бывают разных типов. Узнать тип переменной можно с помощью функции `type()`. Например, чтобы узнать тип переменной `a`, выполните: `type(a)`.

Разные типы данных ведут себя по-разному. Например, сложение двух строк даст совсем другой результат, чем сложение двух целых чисел или двух логических значений.

Проверьте это самостоятельно.

`@pre_exercise_code`
```{python}

```

***

```yaml
type: NormalExercise
key: f4e91c4ae9
xp: 50
```

`@instructions`
- Сложите `savings` и `new_savings` и присвойте результат переменной `total_savings`.
- С помощью `type()` выведите тип переменной `total_savings`.

`@hint`
- Сложите `savings` и `new_savings` и присвойте результат новой переменной `total_savings`.
- Чтобы вывести тип переменной `x`, используйте `print(type(x))`.

`@sample_code`
```{python}
savings = 100
new_savings = 40

# Calculate total_savings using savings and new_savings
____
print(total_savings)

# Print the type of total_savings
print(____)
```

`@solution`
```{python}
savings = 100
new_savings = 40

# Calculate total_savings using savings and new_savings
total_savings = savings + new_savings
print(total_savings)

# Print the type of total_savings
print(type(total_savings))
```

`@sct`
```{python}
# predefined
msg = "Вам не нужно изменять или удалять предопределённые переменные."

Ex().multi(
    check_object('savings', missing_msg=msg).has_equal_value(incorrect_msg=msg),
    check_object('new_savings', missing_msg=msg).has_equal_value(incorrect_msg=msg)
)

Ex().multi(
    check_object("total_savings").has_equal_value(incorrect_msg="Сложите `savings` и `new_savings`, чтобы создать переменную `total_savings`."),
    has_printout(1, not_printed_msg = "__JINJA__:Используйте `{{sol_call}}`, чтобы вывести тип `total_savings`.")
)
```

***

```yaml
type: NormalExercise
key: f54fbf9bd9
xp: 50
```

`@instructions`
- Вычислите сумму `intro` и `intro` и присвойте результат переменной `doubleintro`.
- Выведите значение `doubleintro`. Такой ли результат вы ожидали?

`@hint`
- Сложите `intro` и `intro` и присвойте результат новой переменной `doubleintro`.
- Чтобы вывести переменную `x`, напишите в скрипте `print(x)`.

`@sample_code`
```{python}
intro = "Hello! How are you?"

# Assign sum of intro and intro to doubleintro
____

# Print out doubleintro
print(____)
```

`@solution`
```{python}
intro = "Hello! How are you?"

# Assign sum of intro and intro to doubleintro
doubleintro = intro + intro

# Print out doubleintro
print(doubleintro)
```

`@sct`
```{python}
# predefined
msg = "Вам не нужно изменять или удалять предопределённые переменные."

Ex().check_object('intro', missing_msg=msg).has_equal_value(incorrect_msg=msg)

Ex().multi(
    check_object("doubleintro").has_equal_value(incorrect_msg  = "Сохранили ли вы результат `intro + intro` в `doubleintro`?"),
    has_printout(0, not_printed_msg = "Не забудьте вывести на экран `doubleintro`.")
)

success_msg("Отлично. Обратите внимание, как `intro + intro` приводит к склеиванию `\"Hello! How are you?\"` и `\"Hello! How are you?\"`.")
```

---
title_meta: Розділ 1
title: Основи Python
description: >-
  Вступ до базових понять Python. Дізнайтеся, як працювати з Python інтерактивно
  та за допомогою скрипту. Створіть свої перші змінні та ознайомтеся з основними
  типами даних у Python.
attachments:
  slides_link: 'https://projector-video-pdf-converter.datacamp.com/735/chapter1.pdf'
free_preview: true
lessons:
  - nb_of_exercises: 3
    title: 'Привіт, Python!'
  - nb_of_exercises: 5
    title: Змінні та типи
---

## Привіт, Python!

```yaml
type: VideoExercise
key: f644a48d5d
xp: 50
```

`@projector_key`
d8fcd4c930027fa4e1c3870c7e7e0ff1

---

## Ваш перший код на Python

```yaml
type: NormalExercise
key: bdc52f0e19
lang: python
xp: 100
skills:
  - 2
```

Час запустити ваш перший код на Python!

Перейдіть до редактора коду та натисніть кнопку "Запустити код", щоб побачити результат.

`@instructions`
- Натисніть кнопку "Запустити код", щоб побачити результат виконання `print(5 / 8)`.

`@hint`
- Спочатку запустіть код, перш ніж надсилати відповідь, щоб мати час дослідити результати.

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
Ex().has_printout(0, not_printed_msg = "__JINJA__:Чи використали Ви `{{sol_call}}` для виведення `5 / 8`?")
success_msg("Чудово! Переходимо до наступного завдання!")
```

---

## Python як калькулятор

```yaml
type: NormalExercise
key: 0f7c039428
lang: python
xp: 100
skills:
  - 2
```

Python чудово підходить для базових обчислень. Він уміє додавати, віднімати, множити й ділити.

Код у скрипті містить кілька прикладів.

Тепер ваша черга потренуватися та написати власний код.

`@instructions`
- Виведіть результат віднімання `5` від `5` під розділом `# Subtraction`, використовуючи `print()`.
- Виведіть результат множення `3` на `5` під розділом `# Multiplication`.

`@hint`
- Щоб отримати вивід, вам знадобиться використати `print()`.
- Для віднімання використовуйте `-`, а для множення — `*`.

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
Ex().has_printout(0, not_printed_msg = "Ви використали `print(4 + 5)`, щоб вивести результат вашого додавання?")

Ex().has_printout(1, not_printed_msg = "Ви використали `print(5 - 5)`, щоб вивести результат вашого віднімання?")

Ex().has_printout(2, not_printed_msg = "Ви використали `print(3 * 5)`, щоб вивести результат вашого множення?")

Ex().has_printout(3, not_printed_msg = "Ви використали `print(10 / 2)`, щоб вивести результат вашого ділення?")

success_msg("Це правильно! Python може допомогти вам виконувати обчислення, що буде корисно для аналізу, коли ми розвиватимемо наші навички роботи з даними.")
```

---

## Змінні та типи

```yaml
type: VideoExercise
key: c2e396792e
xp: 50
```

`@projector_key`
433dcfcfedaee070cbf440491c402e3b

---

## Присвоювання змінній

```yaml
type: NormalExercise
key: 4bf65ad83e
lang: python
xp: 100
skills:
  - 2
```

У Python змінна дає змогу звертатися до значення за назвою. Щоб створити змінну `x` зі значенням `5`, використайте `=`, як у прикладі:

```
x = 5
```

Тепер ви можете використовувати назву цієї змінної, `x`, замість фактичного значення `5`.

Пам'ятайте: `=` у Python означає _присвоювання_, а не перевірку на рівність! Спробуйте у вправі, замінивши `____` на свій код.

`@instructions`
- Створіть змінну `savings` зі значенням `100`.
- Перевірте цю змінну, ввівши в скрипті `print(savings)`.

`@hint`
- Введіть `savings = 100`, щоб створити змінну `savings`.
- Після створення змінної `savings` введіть `print(savings)`.
- У фінальному коді не має бути жодних `____`.

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
Ex().check_object("savings").has_equal_value(incorrect_msg="Призначте `100` змінній `savings`.")
Ex().has_printout(0, not_printed_msg = "Виведіть на екран `savings`, змінну, яку Ви створили, за допомогою `print(savings)`.")
success_msg("Чудово! Давайте спробуємо виконати деякі обчислення з цією змінною зараз!")
```

---

## Обчислення зі змінними

```yaml
type: NormalExercise
key: ff06cedeb4
lang: python
xp: 100
skills:
  - 2
```

Ви вже створили змінну для заощаджень, тож почнімо відкладати!

Замість обчислень із самими значеннями можна використовувати змінні.

Скільки грошей ви заощадите за чотири місяці, якщо щомісяця відкладатимете по $10?

`@instructions`
- Створіть змінну `monthly_savings`, що дорівнює `10`, і `num_months`, що дорівнює `4`.
- Помножте `monthly_savings` на `num_months` і присвойте результат змінній `new_savings`.
- Виведіть значення `new_savings`.

`@hint`
- Обчислення зі змінними виконуються так само, як і з числами, тож замість `10 * 4` підставте змінні!
- Скористайтеся `print()`, щоб побачити суму в `new_savings`.
- Уважно перевірте написання назв змінних!

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
Ex().check_object("monthly_savings").has_equal_value(incorrect_msg = "Чи зберегли Ви `10` у `monthly_savings`, використовуючи `monthly_savings = 10`?")
Ex().check_object("num_months").has_equal_value(incorrect_msg = "Чи зберегли Ви `4` у `num_months`, використовуючи `num_months = 4`?")
Ex().check_object("new_savings").has_equal_value(incorrect_msg = "Чи використали Ви правильні змінні та символи для множення? Очікувалося `monthly_savings * num_months`, але отримано щось інше.")
# Ex().check_object("total_savings").has_equal_value(incorrect_msg = "Чи використали Ви правильні змінні та символи для додавання? Очікувалося `savings + new_savings`, але отримано щось інше.")

Ex().has_printout(0, not_printed_msg="Не забудьте вивести `new_savings` в кінці Вашого скрипту.")

success_msg("У Вас $40 нових заощаджень!")
```

---

## Інші типи змінних

```yaml
type: NormalExercise
key: 006b48561f
lang: python
xp: 100
skills:
  - 2
```

У попередній вправі ви працювали з цілим числом — типом даних Python:

- `int` (integer): число без дробової частини. `savings` зі значенням `100` — це приклад цілого числа.

Окрім числових типів даних, є ще три дуже поширені типи даних:

- `float` (floating point): число, що має цілу і дробову частини, розділені крапкою. `1.1` — це приклад числа з плаваючою комою.
- `str` (string): тип для представлення тексту. Ви можете використовувати одинарні або подвійні лапки, щоб створити рядок.
- `bool` (boolean): тип для представлення логічних значень. Він може бути лише `True` або `False` (важливо дотримуватися регістру!).

`@instructions`
- Створіть нове число з плаваючою комою `half` зі значенням `0.5`.
- Створіть новий рядок `intro` зі значенням `"Hello! How are you?"`.
- Створіть нове булеве значення `is_good` зі значенням `True`.

`@hint`
- Щоб створити змінну в Python, використовуйте `=`. Не забудьте взяти рядок у одинарні або подвійні лапки.
- У Python є лише два булеві значення: `True` і `False`. `TRUE`, `true`, `FALSE`, `false` та інші варіанти не приймаються.

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
Ex().check_object("half").has_equal_value(incorrect_msg = "Чи зберегли Ви число з плаваючою комою, `0.5` у змінну `half`?")

Ex().check_object("intro").has_equal_value(incorrect_msg = "Хмм, щось не так у Вашій змінній `intro`. Перевірте правопис і переконайтеся, що Ви використали лапки.")

Ex().check_object("is_good").has_equal_value(incorrect_msg = "Чи написали Ви з великої літери значення типу boolean? Пам'ятайте, що тут не потрібно використовувати лапки.")

success_msg("Чудово!")
```

---

## Операції з іншими типами

```yaml
type: BulletExercise
key: 4d0d83cc02
xp: 100
```

У Python змінні можуть бути різних типів. Ви можете побачити тип змінної за допомогою `type()`. Наприклад, щоб дізнатися тип `a`, виконайте: `type(a)`.

Різні типи в Python поводяться по‑різному. Якщо, наприклад, додати два рядки, ви отримаєте інший результат, ніж коли додаєте два цілі числа або два булеві значення.

Час перевірити це на практиці.

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
- Додайте `savings` і `new_savings` та присвойте результат змінній `total_savings`.
- Використайте `type()`, щоб надрукувати тип `total_savings`.

`@hint`
- Присвойте `savings + new_savings` новій змінній `total_savings`.
- Щоб надрукувати тип змінної `x`, використайте `print(type(x))`.

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
msg = "Вам не потрібно змінювати або видаляти попередньо визначені змінні."

Ex().multi(
    check_object('savings', missing_msg=msg).has_equal_value(incorrect_msg=msg),
    check_object('new_savings', missing_msg=msg).has_equal_value(incorrect_msg=msg)
)

Ex().multi(
    check_object("total_savings").has_equal_value(incorrect_msg="Додайте `savings` та `new_savings`, щоб створити змінну `total_savings`."),
    has_printout(1, not_printed_msg = "__JINJA__:Використовуйте `{{sol_call}}`, щоб вивести тип `total_savings`.")
)
```

***

```yaml
type: NormalExercise
key: f54fbf9bd9
xp: 50
```

`@instructions`
- Обчисліть суму `intro` і `intro` та присвойте результат змінній `doubleintro`.
- Виведіть `doubleintro`. Ви цього й очікували?

`@hint`
- Присвойте `intro + intro` новій змінній `doubleintro`.
- Щоб вивести змінну `x`, запишіть у скрипті `print(x)`.

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
msg = "Вам не потрібно змінювати або видаляти попередньо визначені змінні."

Ex().check_object('intro', missing_msg=msg).has_equal_value(incorrect_msg=msg)

Ex().multi(
    check_object("doubleintro").has_equal_value(incorrect_msg  = "Чи зберегли Ви результат `intro + intro` у `doubleintro`?"),
    has_printout(0, not_printed_msg = "Не забудьте вивести `doubleintro`.")
)

success_msg("Чудово. Зверніть увагу, як `intro + intro` призводить до об'єднання `\"Hello! How are you?\"` та `\"Hello! How are you?\"`.")
```

---
title_meta: Розділ 3
title: Функції та пакети
description: >-
  Ви навчитеся використовувати функції, методи та пакети, щоб ефективно
  задіювати код, який уже написали досвідчені розробники Python. Мета — зменшити
  обсяг коду, потрібного для розв'язання складних задач!
attachments:
  slides_link: 'https://projector-video-pdf-converter.datacamp.com/735/chapter3.pdf'
lessons:
  - nb_of_exercises: 4
    title: Функції
  - nb_of_exercises: 4
    title: Методи
  - nb_of_exercises: 4
    title: Пакети
---

## Функції

```yaml
type: VideoExercise
key: 5c5f365930
xp: 50
```

`@projector_key`
1204d914b0e53100529827e07441ee6c

---

## Знайомі функції

```yaml
type: NormalExercise
key: c422ee929b
lang: python
xp: 100
skills:
  - 2
```

Із коробки Python пропонує багато вбудованих функцій, щоб полегшити вам роботу з даними. Ви вже знаєте дві такі функції: `print()` і `type()`. Є також функції `str()`, `int()`, `bool()` та `float()` для перетворення між типами даних. Докладніше про них можна дізнатися [тут.](https://docs.python.org/3/library/functions.html) Це теж вбудовані функції.

Викликати функцію просто. Щоб отримати тип `3.0` і зберегти результат у новій змінній `result`, можна використати таке:

```
result = type(3.0)
```

`@instructions`
- Використайте `print()` разом із `type()`, щоб вивести тип `var1`.
- Застосуйте `len()`, щоб отримати [довжину списку](https://docs.python.org/3/library/functions.html#len) `var1`. Обгорніть це викликом `print()`, щоб одразу його вивести.
- Використайте `int()`, щоб перетворити `var2` на [ціле число](https://docs.python.org/3/library/functions.html#int). Збережіть результат у змінній `out2`.

`@hint`
- Викличте функцію `type()` ось так: `type(var1)`.
- Викличте `print()`, як ви вже робили багато разів. Просто розмістіть змінну, яку хочете вивести, у дужках.
- `int(x)` перетворює `x` на ціле число.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create variables var1 and var2
var1 = [1, 2, 3, 4]
var2 = True

# Print out type of var1
____

# Print out length of var1
____

# Convert var2 to an integer: out2
out2 = ____
```

`@solution`
```{python}
# Create variables var1 and var2
var1 = [1, 2, 3, 4]
var2 = True

# Print out type of var1
print(type(var1))

# Print out length of var1
print(len(var1))

# Convert var2 to an integer: out2
out2 = int(var2)
```

`@sct`
```{python}
msg = "Вам не потрібно змінювати або видаляти попередньо визначені змінні."
Ex().check_object("var1", missing_msg=msg).has_equal_value(incorrect_msg=msg)
Ex().check_object("var2", missing_msg=msg).has_equal_value(incorrect_msg=msg)

patt = "__JINJA__:Переконайтеся, що виводите %s `var1` за допомогою `{{sol_call}}`."
Ex().has_printout(0, not_printed_msg = patt % 'тип')
Ex().has_printout(1, not_printed_msg = patt % 'довжину')

int_miss_msg = "Чи використовували Ви `int()`, щоб перетворити `var2` на ціле число?"
int_incorr_msg = "Чи передали Ви `var2` у `int()`?"
Ex().check_correct(
  check_object("out2").has_equal_value(incorrect_msg="Ви правильно викликали `int()`; тепер переконайтеся, що призначили результат цього виклику `out2`."),
  check_function("int", missing_msg=int_miss_msg).has_equal_value(incorrect_msg=int_incorr_msg)
)
success_msg("Чудова робота! Функція `len()` надзвичайно корисна; вона також працює зі строками, щоб підрахувати кількість символів!")
```

---

## Допоможіть!

```yaml
type: MultipleChoiceExercise
key: 679b852978
lang: python
xp: 50
skills:
  - 2
```

Можливо, ви вже знаєте назву функції Python, але ще треба зʼясувати, як її використовувати. Парадоксально, але інформацію про функцію слід запитувати іншою функцією: `help()`. У IPython також можна ставити `?` перед назвою функції.

Щоб отримати довідку про функцію `max()`, наприклад, ви можете використати один із цих викликів:

```
help(max)
?max
```

Скористайтеся оболонкою IPython, щоб відкрити [документацію](https://docs.python.org/3/library/functions.html#pow) на `pow()`. Зробіть це, ввівши `?pow` або `help(pow)` і натиснувши **Enter**.

Яке з наведених тверджень є правильним?

`@possible_answers`
- `pow()` приймає три аргументи: `base`, `exp` і `mod`. Без `mod` функція поверне помилку.
- `pow()` приймає три обовʼязкові аргументи: `base`, `exp` і `None`.
- `pow()` потребує аргументи `base` та `exp`; `mod` є необовʼязковим.
- `pow()` приймає два аргументи: `exp` і `mod`. Пропуск `exp` призводить до помилки.

`@hint`
- Необовʼязкові аргументи задаються через `=`, мають типовe значення, яке функція використає, якщо цей аргумент не вказано.

`@pre_exercise_code`
```{python}

```

`@sct`
```{python}
msg1 = "Не зовсім так. `mod` має значення за замовчуванням, яке буде використано, якщо ви не вкажете значення."
msg2 = "Неправильно. `None` є значенням за замовчуванням для аргументу `mod`."
msg3 = "Чудово! Використання `help()` може допомогти вам зрозуміти, як працюють функції, розкриваючи їхній повний потенціал!"
msg4 = "Неправильно. `pow()` приймає три аргументи, один з яких має значення за замовчуванням."
Ex().has_chosen(3, [msg1, msg2, msg3, msg4])
```

---

## Кілька аргументів

```yaml
type: NormalExercise
key: e30486d7c1
lang: python
xp: 100
skills:
  - 2
```

У попередній вправі ви визначали необов'язкові аргументи, переглядаючи документацію за допомогою `help()`. Тепер застосуйте це, щоб змінити поведінку функції `sorted()`.

Перегляньте [документацію](https://docs.python.org/3/library/functions.html#sorted) для `sorted()`, ввівши `help(sorted)` в оболонці IPython.

Ви побачите, що `sorted()` приймає три аргументи: `iterable`, `key` і `reverse`. У цій вправі вам потрібно вказати лише `iterable` і `reverse`, без `key`.

Для вас уже створено два списки.

Чи зможете ви об'єднати їх і відсортувати у спадному порядку?

`@instructions`
- Використайте `+`, щоб об'єднати вміст `first` і `second` у новий список: `full`.
- Викличте `sorted()` для `full` і вкажіть аргумент `reverse` як `True`. Збережіть відсортований список у змінній `full_sorted`.
- На завершення виведіть `full_sorted`.

`@hint`
- Додайте `first` і `second`, як два числа, та присвойте результат змінній `full`.
- Використайте `sorted()` з двома аргументами: `full` і `reverse=True`.
- Щоб вивести змінну на екран, скористайтеся `print()'.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create lists first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# Paste together first and second: full
full = ____ + ____

# Sort full in descending order: full_sorted
full_sorted = ____

# Print out full_sorted
____
```

`@solution`
```{python}
# Create lists first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# Paste together first and second: full
full = first + second

# Sort full in descending order: full_sorted
full_sorted = sorted(full, reverse=True)

# Print out full_sorted
print(full_sorted)
```

`@sct`
```{python}
msg = "Вам не потрібно змінювати або видаляти вже існуючі змінні `first` та `second`."
Ex().multi(
  check_object("first", missing_msg=msg).has_equal_value(incorrect_msg=msg),
  check_object("second", missing_msg=msg).has_equal_value(incorrect_msg=msg)
)
Ex().check_correct(
  check_object("full_sorted").has_equal_value(incorrect_msg="Переконайтеся, що ви присвоїли результат виклику `sorted()` змінній `full_sorted`."),
  check_function("sorted").multi(
    check_args(0).has_equal_value(),
    check_args('reverse').has_equal_value()
  )
)

success_msg("Чудово! Перейдіть до відео про методи Python.")
```

---

## Методи

```yaml
type: VideoExercise
key: 2b66cb66b1
xp: 50
```

`@projector_key`
8e387776f3a264a745128b68aa8d8f83

---

## Методи рядків

```yaml
type: NormalExercise
key: 4039302ee0
lang: python
xp: 100
skills:
  - 2
```

У рядків є багато методів. Уважно виконайте інструкції, щоб познайомитися з деякими з них. Якщо хочете розібратися детальніше, у будь-який момент введіть `help(str)` в оболонці IPython.

Рядок `place` уже створено для вас, щоб ви могли експериментувати.

`@instructions`
- Скористайтеся [методом](https://docs.python.org/3/library/stdtypes.html#str.upper) `.upper()` для `place` і збережіть результат у `place_up`. Використайте синтаксис виклику методів, який ви вивчали в попередньому відео.
- Виведіть `place` і `place_up`. Чи обидва змінилися?
- Виведіть кількість літер o у змінній `place`, викликавши `.count()` для `place` і передавши літеру `'o'` як аргумент методу. Йдеться про змінну `place`, а не про слово "place"!

`@hint`
- Ви можете викликати метод `.upper()` для `place` без жодних додаткових аргументів.
- Щоб вивести змінну `x`, напишіть `print(x)`.
- Обов'язково обгорніть виклик `place.count(____)` у функцію `print()`, щоб побачити результат.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# string to experiment with: place
place = "poolhouse"

# Use upper() on place
place_up = 

# Print out place and place_up



# Print out the number of o's in place

```

`@solution`
```{python}
# string to experiment with: place
place = "poolhouse"

# Use upper() on place
place_up = place.upper()

# Print out place and place_up
print(place)
print(place_up)

# Print out the number of o's in place
print(place.count('o'))
```

`@sct`
```{python}
msg = "Вам не потрібно змінювати або видаляти попередньо визначені змінні."
Ex().check_object("place", missing_msg=msg).has_equal_value(incorrect_msg=msg)

patt = "Не забудьте вивести `%s`."
Ex().has_printout(0, not_printed_msg=patt % "place")
Ex().check_correct(
    has_printout(1, not_printed_msg=patt % "place_up"),
    check_correct(
        check_object("place_up").has_equal_value(incorrect_msg="Призначте результат виклику `place.upper()` змінній `place_up`."),
        check_function("place.upper", signature=False)
    )
)    

# check count of place
Ex().check_correct(
  has_printout(2, not_printed_msg = "Ви правильно обчислили кількість 'o' у `place`; тепер переконайтеся, що обгорнули виклик `place.count('o')` у функцію `print()`, щоб вивести результат."),
  check_function("place.count", signature=False).check_args(0).has_equal_value()
)

success_msg("Чудово! Зверніть увагу на виведення, що метод `upper()` не змінює об'єкт, на якому він викликається. Це буде відрізнятися для списків у наступній вправі!")
```

---

## Методи списків

```yaml
type: NormalExercise
key: 0dbe8ed695
lang: python
xp: 100
skills:
  - 2
```

Методи в Python мають не лише рядки. Списки, числа з рухомою комою (float), цілі числа (int) і булеві значення також мають низку корисних методів. У цій вправі ви попрактикуєтеся з:

- `.index()`, щоб отримати індекс першого елемента списку, який збігається з переданим значенням, та
- `.count()`, щоб дізнатися, скільки разів елемент з'являється у списку.

Ви працюватимете зі списком площ різних частин будинку: `areas`.

`@instructions`
- Скористайтеся методом `.index()`, щоб отримати індекс елемента в `areas`, який дорівнює `20.0`. Виведіть цей індекс.
- Викличте `.count()` для `areas`, щоб з'ясувати, скільки разів `9.50` трапляється у списку. Знову просто виведіть це число.

`@hint`
- Щоб вивести індекс, обгорніть виклик `areas.index(___)` у функцію `print()`.
- Щоб вивести кількість появ елемента `x` у списку, обгорніть виклик `areas.count(___)` у функцію `print()`.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Print out the index of the element 20.0


# Print out how often 9.50 appears in areas

```

`@solution`
```{python}
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Print out the index of the element 20.0
print(areas.index(20.0))

# Print out how often 9.50 appears in areas
print(areas.count(9.50))
```

`@sct`
```{python}
predef_msg = "Вам не потрібно змінювати або видаляти попередньо визначений список `areas`."

Ex().check_object("areas", missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg)

Ex().check_function("print", index=0).check_args(0).check_function('areas.index', signature=False).check_args(0).has_equal_value()


Ex().check_function("print", index=1).check_args(0).check_function('areas.count', signature=False).has_equal_value()

success_msg("Чудово! Це були приклади методів `list`, які не змінювали список, до якого вони були застосовані.")
```

---

## Методи списків (2)

```yaml
type: NormalExercise
key: 1fbeab82d0
lang: python
xp: 100
skills:
  - 2
```

Більшість методів списків змінюють список, для якого їх викликають. Приклади:

- `.append()` — додає елемент до списку, для якого його викликали,
- `.remove()` — [видаляє](https://docs.python.org/3/library/stdtypes.html#typesseq-mutable) перший елемент списку, що збігається з переданим аргументом, і
- `.reverse()` — [змінює на зворотний](https://docs.python.org/3/library/stdtypes.html#typesseq-mutable) порядок елементів у списку, для якого його викликали.

Ви працюватимете зі списком `areas`, що містить площі різних частин будинку.

`@instructions`
- Двічі використайте `.append()`, щоб знову додати площі басейну та гаража: відповідно `24.5` і `15.45`. Додайте їх саме в такому порядку.
- Виведіть `areas`.
- Використайте метод `.reverse()`, щоб обернути порядок елементів у `areas`.
- Ще раз виведіть `areas`.

`@hint`
- Для першої інструкції двічі виконайте виклик `areas.append(___)`.
- Щоб вивести змінну `x`, просто напишіть `print(x)`.
- Метод `.reverse()` не потребує додаткових аргументів; використайте крапкову нотацію та порожні дужки: `.reverse()`.
- Щоб вивести змінну `x`, просто напишіть `print(x)`.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Use append twice to add poolhouse and garage size



# Print out areas


# Reverse the orders of the elements in areas


# Print out areas

```

`@solution`
```{python}
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Use append twice to add poolhouse and garage size
areas.append(24.5)
areas.append(15.45)

# Print out areas
print(areas)

# Reverse the orders of the elements in areas
areas.reverse()

# Print out areas
print(areas)
```

`@sct`
```{python}
Ex().multi(
  check_function("areas.append", index=0, signature=False).check_args(0).has_equal_value(),
  check_function("areas.append", index=1, signature=False).check_args(0).has_equal_value(),
  check_function("print", index=0).check_args(0).has_equal_ast(),
  check_function("areas.reverse", index=0, signature=False),
  check_function("print", index=1).check_args(0).has_equal_ast()
)

success_msg("Чудово!")
```

---

## Пакети

```yaml
type: VideoExercise
key: ab96a17c5e
xp: 50
```

`@projector_key`
cedcfb34350be8545599768f96695cdd

---

## Імпорт пакета

```yaml
type: NormalExercise
key: 7432a6376f
lang: python
xp: 100
skills:
  - 2
```

Припустімо, ви хочете обчислити довжину кола та площу круга. Формули такі:

$$C = 2 \pi r$$
$$A = \pi r^2 $$

Замість того щоб набирати число для `pi`, ви можете використати пакет `math`, який містить це значення.

Для довідки: `**` — це оператор піднесення до степеня. Наприклад, `3**4` — це `3` у степені `4` і дасть `81`.

`@instructions`
- Імпортуйте пакет `math`.
- Використайте `math.pi`, щоб обчислити довжину кола та зберегти її в `C`.
- Використайте `math.pi`, щоб обчислити площу круга та зберегти її в `A`.

`@hint`
- Ви можете просто використати `import math`, а тоді звертатися до `pi` як `math.pi`.
- Скористайтеся формулою з тексту завдання, щоб обчислити `C`. Використовуйте `*`.
- Скористайтеся формулою з тексту завдання, щоб обчислити `A`. Використовуйте `*` і `**`.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Import the math package
import ____

# Calculate C
C = 2 * 0.43 * ____

# Calculate A
A = ____ * 0.43 ** 2

print("Circumference: " + str(C))
print("Area: " + str(A))
```

`@solution`
```{python}
# Import the math package
import math

# Calculate C
C = 2 * 0.43 * math.pi

# Calculate A
A = math.pi * 0.43 ** 2

print("Circumference: " + str(C))
print("Area: " + str(A))
```

`@sct`
```{python}
patt = "Ваше обчислення `%s` не зовсім правильне. Переконайтеся, що використовуєте `math.pi`."
Ex().multi(
  has_import('math', same_as=False),
  check_object('C').has_equal_value(incorrect_msg=patt%'C'),
  check_object('A').has_equal_value(incorrect_msg=patt%'A')
)

Ex().multi(
  has_printout(0, not_printed_msg = "__JINJA__:Залиште `{{sol_call}}` там, щоб вивести окружність."),
  has_printout(1, not_printed_msg = "__JINJA__:Залиште `{{sol_call}}` там, щоб вивести площу.")
)

success_msg("Чудово! Якщо Ви знаєте, як працювати з функціями з пакетів, сила багатьох програмістів Python у Вас під рукою!")
```

---

## Вибірковий імпорт

```yaml
type: NormalExercise
key: fe65eff50a
lang: python
xp: 100
skills:
  - 2
```

Загальні імпорти на кшталт `import math` надають вам доступ до **всієї** функціональності пакета `math`. Однак, якщо вам потрібна лише конкретна частина пакета, можна зробити імпорт вибірковим:

```
from math import pi
```

Спробуйте те саме ще раз, але цього разу використовуйте лише `pi`.

`@instructions`
- Виконайте вибірковий імпорт із пакета `math`, імпортувавши лише `pi`.
- Використайте `pi`, щоб обчислити довжину кола та збережіть її в `C`.
- Використайте `pi`, щоб обчислити площу кола та збережіть її в `A`.

`@hint`
- Скористайтеся вибірковим імпортом: `from math import pi`.
- Тепер ви можете використовувати `pi` самостійно!

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Import pi function of math package
from math import ____

# Calculate C
C = 2 * 0.43 * ____

# Calculate A
A = ____ * 0.43 ** 2

print("Circumference: " + str(C))
print("Area: " + str(A))
```

`@solution`
```{python}
# Import pi function of math package
from math import pi

# Calculate C
C = 2 * 0.43 * pi

# Calculate A
A = pi * 0.43 ** 2

print("Circumference: " + str(C))
print("Area: " + str(A))
```

`@sct`
```{python}
patt = "Ваше обчислення `%s` не зовсім правильне. Переконайтеся, що використовуєте лише `pi`."

Ex().has_import("math.pi", not_imported_msg = "Переконайтеся, що імпортуєте `pi` з пакету `math`. Ви повинні використовувати нотацію `from ___ import ___`.",)

Ex().multi(
  check_object('C').has_equal_value(incorrect_msg=patt%'C'),
  check_object('A').has_equal_value(incorrect_msg=patt%'A')
)

Ex().multi(
  has_printout(0, not_printed_msg = "__JINJA__:Залиште `{{sol_call}}` там, щоб вивести окружність."),
  has_printout(1, not_printed_msg = "__JINJA__:Залиште `{{sol_call}}` там, щоб вивести площу.")
)

success_msg("Чудово! Перейдіть до наступної вправи.")
```

---

## Різні способи імпорту

```yaml
type: MultipleChoiceExercise
key: f1b2675a2a
lang: python
xp: 50
skills:
  - 2
```

У Python є кілька способів імпортувати пакети й модулі. Залежно від того, як ви імпортуєте, доведеться писати різний код.

Припустімо, ви хочете використати [функцію](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.inv.html) `inv()`, яка міститься в підпакеті `linalg` пакета `scipy`. Ви хочете мати змогу викликати цю функцію так:

```
my_inv([[1,2], [3,4]])
```

Який саме оператор `import` потрібен, щоб наведений вище код виконувався без помилки?

`@possible_answers`
- `import scipy`
- `import scipy.linalg`
- `from scipy.linalg import my_inv`
- `from scipy.linalg import inv as my_inv`

`@hint`
- Спробуйте різні інструкції імпорту в оболонці IPython і подивіться, яка з них дозволяє рядку `my_inv([[1, 2], [3, 4]])` виконатися без помилок. Натисніть **enter**, щоб запустити введений вами код.

`@pre_exercise_code`
```{python}

```

`@sct`
```{python}
msg1 = msg2 = msg3 = "Неправильно, спробуйте ще раз. Спробуйте різні оператори імпорту в IPython shell і подивіться, який з них дозволяє рядку `my_inv([[1, 2], [3, 4]])` виконатися без помилок."
msg4 = "Правильно! Слово `as` дозволяє створити локальне ім'я для функції, яку ви імпортуєте: `inv()` тепер доступна як `my_inv()`."
Ex().has_chosen(4, [msg1, msg2, msg3, msg4])
```

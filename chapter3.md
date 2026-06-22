---
title_meta: Глава 3
title: Функции и пакеты
description: >-
  Вы узнаете, как использовать функции, методы и пакеты, чтобы эффективно
  применять код, написанный опытными Python-разработчиками. Цель — решать
  сложные задачи с минимальным количеством кода.
attachments:
  slides_link: 'https://projector-video-pdf-converter.datacamp.com/735/chapter3.pdf'
lessons:
  - nb_of_exercises: 4
    title: Функции
  - nb_of_exercises: 4
    title: Методы
  - nb_of_exercises: 4
    title: Пакеты
---

## Функции

```yaml
type: VideoExercise
key: 5c5f365930
xp: 50
```

`@projector_key`
1204d914b0e53100529827e07441ee6c

---

## Знакомые функции

```yaml
type: NormalExercise
key: c422ee929b
lang: python
xp: 100
skills:
  - 2
```

Python сразу «из коробки» предоставляет множество встроенных функций, которые упрощают работу специалиста по данным. Вы уже знакомы с двумя из них: `print()` и `type()`. Есть и другие функции — например, `str()`, `int()`, `bool()` и `float()` — для преобразования типов данных. Узнать о них подробнее можно [здесь.](https://docs.python.org/3/library/functions.html) Это тоже встроенные функции.

Вызвать функцию очень просто. Чтобы узнать тип значения `3.0` и сохранить результат в новую переменную `result`, используйте следующий код:

```
result = type(3.0)
```

`@instructions`
- Используйте `print()` вместе с `type()`, чтобы вывести тип переменной `var1`.
- Используйте `len()`, чтобы получить [длину списка](https://docs.python.org/3/library/functions.html#len) `var1`. Оберните вызов в `print()`, чтобы сразу вывести результат.
- Используйте `int()`, чтобы преобразовать `var2` в [целое число](https://docs.python.org/3/library/functions.html#int). Сохраните результат в переменную `out2`.

`@hint`
- Вызовите функцию `type()` следующим образом: `type(var1)`.
- Вызовите `print()` так же, как вы делали это раньше. Просто передайте переменную, которую хотите вывести, в скобках.
- `int(x)` преобразует `x` в целое число.

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
msg = "Вам не нужно изменять или удалять предопределённые переменные."
Ex().check_object("var1", missing_msg=msg).has_equal_value(incorrect_msg=msg)
Ex().check_object("var2", missing_msg=msg).has_equal_value(incorrect_msg=msg)

patt = "__JINJA__:Убедитесь, что вы выводите %s переменной `var1` с помощью `{{sol_call}}`."
Ex().has_printout(0, not_printed_msg = patt % 'тип')
Ex().has_printout(1, not_printed_msg = patt % 'длину')

int_miss_msg = "Использовали ли вы `int()` для преобразования `var2` в целое число?"
int_incorr_msg = "Передали ли вы `var2` в `int()`?"
Ex().check_correct(
  check_object("out2").has_equal_value(incorrect_msg="Вы правильно вызвали `int()`; теперь убедитесь, что результат этого вызова присвоен переменной `out2`."),
  check_function("int", missing_msg=int_miss_msg).has_equal_value(incorrect_msg=int_incorr_msg)
)
success_msg("Отличная работа! Функция `len()` крайне полезна; она также работает со строками для подсчёта количества символов!")
```

---

## Справка!

```yaml
type: MultipleChoiceExercise
key: 679b852978
lang: python
xp: 50
skills:
  - 2
```

Возможно, вы уже знаете название нужной функции Python, но ещё не разобрались, как её использовать. Как ни странно, информацию о функции можно получить с помощью другой функции — `help()`. В IPython также можно использовать `?` перед именем функции.

Например, чтобы получить справку по функции `max()`, воспользуйтесь одним из следующих вызовов:

```
help(max)
?max
```

Откройте [документацию](https://docs.python.org/3/library/functions.html#pow) по функции `pow()` в оболочке IPython. Для этого введите `?pow` или `help(pow)` и нажмите **Enter**.

Какое из следующих утверждений верно?

`@possible_answers`
- `pow()` принимает три аргумента: `base`, `exp` и `mod`. Без `mod` функция вернёт ошибку.
- `pow()` принимает три обязательных аргумента: `base`, `exp` и `None`.
- `pow()` требует аргументы `base` и `exp`; аргумент `mod` является необязательным.
- `pow()` принимает два аргумента: `exp` и `mod`. Если `exp` не указан, функция вернёт ошибку.

`@hint`
- Необязательные аргументы задаются через `=` и имеют значение по умолчанию, которое функция использует, если аргумент не указан.

`@pre_exercise_code`
```{python}

```

`@sct`
```{python}
msg1 = "Не совсем верно. У `mod` есть значение по умолчанию, которое будет использовано, если вы не укажете значение."
msg2 = "Неверно. `None` является значением по умолчанию для аргумента `mod`."
msg3 = "Отлично! Использование `help()` поможет вам понять, как работают функции, раскрывая их полный потенциал!"
msg4 = "Неверно. `pow()` принимает три аргумента, один из которых имеет значение по умолчанию."
Ex().has_chosen(3, [msg1, msg2, msg3, msg4])
```

---

## Несколько аргументов

```yaml
type: NormalExercise
key: e30486d7c1
lang: python
xp: 100
skills:
  - 2
```

В предыдущем упражнении вы научились находить необязательные аргументы с помощью документации и функции `help()`. Теперь применим эти знания, чтобы изменить поведение функции `sorted()`.

Изучите [документацию](https://docs.python.org/3/library/functions.html#sorted) функции `sorted()`, введя `help(sorted)` в оболочке IPython.

Вы увидите, что `sorted()` принимает три аргумента: `iterable`, `key` и `reverse`. В этом упражнении вам нужно будет указать только `iterable` и `reverse` — аргумент `key` можно пропустить.

Два списка уже созданы для вас.

Попробуйте объединить их и отсортировать в порядке убывания.

`@instructions`
- Используйте `+`, чтобы объединить содержимое `first` и `second` в новый список `full`.
- Вызовите `sorted()` для `full` и задайте аргументу `reverse` значение `True`. Сохраните отсортированный список в переменную `full_sorted`.
- В завершение выведите `full_sorted` на экран.

`@hint`
- Сложите `first` и `second` как два числа и присвойте результат переменной `full`.
- Используйте `sorted()` с двумя аргументами: `full` и `reverse=True`.
- Чтобы вывести переменную, используйте `print()`.

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
msg = "Вам не нужно изменять или удалять уже существующие переменные `first` и `second`."
Ex().multi(
  check_object("first", missing_msg=msg).has_equal_value(incorrect_msg=msg),
  check_object("second", missing_msg=msg).has_equal_value(incorrect_msg=msg)
)
Ex().check_correct(
  check_object("full_sorted").has_equal_value(incorrect_msg="Убедитесь, что вы присваиваете результат вызова `sorted()` переменной `full_sorted`."),
  check_function("sorted").multi(
    check_args(0).has_equal_value(),
    check_args('reverse').has_equal_value()
  )
)

success_msg("Отлично! Переходите к видео о методах Python.")
```

---

## Методы

```yaml
type: VideoExercise
key: 2b66cb66b1
xp: 50
```

`@projector_key`
8e387776f3a264a745128b68aa8d8f83

---

## Методы строк

```yaml
type: NormalExercise
key: 4039302ee0
lang: python
xp: 100
skills:
  - 2
```

У строк есть множество встроенных методов. Следуйте инструкциям, чтобы познакомиться с некоторыми из них. Если хотите изучить их подробнее, введите `help(str)` в оболочке IPython.

Переменная `place` уже создана — используйте её для экспериментов.

`@instructions`
- Примените метод `.upper()` ([документация](https://docs.python.org/3/library/stdtypes.html#str.upper)) к переменной `place` и сохраните результат в `place_up`. Используйте синтаксис вызова методов, который вы изучили в предыдущем видео.
- Выведите на экран `place` и `place_up`. Изменились ли обе переменные?
- Выведите количество букв «o» в переменной `place`: вызовите метод `.count()` на переменной `place` и передайте букву `'o'` в качестве аргумента. Речь идёт о переменной `place`, а не о слове `"place"`!

`@hint`
- Метод `.upper()` можно вызвать на переменной `place` без дополнительных аргументов.
- Чтобы вывести переменную `x`, используйте `print(x)`.
- Не забудьте обернуть вызов `place.count(____)` в функцию `print()`, чтобы результат был выведен на экран.

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
msg = "Вам не нужно изменять или удалять предопределённые переменные."
Ex().check_object("place", missing_msg=msg).has_equal_value(incorrect_msg=msg)

patt = "Не забудьте вывести на экран `%s`."
Ex().has_printout(0, not_printed_msg=patt % "place")
Ex().check_correct(
    has_printout(1, not_printed_msg=patt % "place_up"),
    check_correct(
        check_object("place_up").has_equal_value(incorrect_msg="Присвойте результат вызова `place.upper()` переменной `place_up`."),
        check_function("place.upper", signature=False)
    )
)    

# check count of place
Ex().check_correct(
  has_printout(2, not_printed_msg = "Вы правильно подсчитали количество букв 'o' в `place`; теперь убедитесь, что вызов `place.count('o')` обёрнут в функцию `print()` для вывода результата на экран."),
  check_function("place.count", signature=False).check_args(0).has_equal_value()
)

success_msg("Отлично! Обратите внимание по результатам вывода, что метод `upper()` не изменяет объект, для которого он вызывается. В следующем упражнении для списков всё будет иначе!")
```

---

## Методы списков

```yaml
type: NormalExercise
key: 0dbe8ed695
lang: python
xp: 100
skills:
  - 2
```

Методы есть не только у строк. Списки, числа с плавающей точкой, целые числа и логические значения тоже обладают набором полезных методов. В этом упражнении вы поработаете с:

- `.index()` — для получения индекса первого элемента списка, совпадающего с заданным значением;
- `.count()` — для подсчёта количества вхождений элемента в список.

Вы будете работать со списком `areas`, содержащим площади различных комнат дома.

`@instructions`
- Используйте метод `.index()`, чтобы найти индекс элемента в `areas`, равного `20.0`. Выведите этот индекс на экран.
- Вызовите метод `.count()` для списка `areas`, чтобы узнать, сколько раз значение `9.50` встречается в списке. Выведите это число на экран.

`@hint`
- Чтобы вывести индекс, оберните вызов `areas.index(___)` в функцию `print()`.
- Чтобы вывести количество вхождений элемента `x` в список, оберните вызов `areas.count(___)` в функцию `print()`.

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
predef_msg = "Вам не нужно изменять или удалять предопределённый список `areas`."

Ex().check_object("areas", missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg)

Ex().check_function("print", index=0).check_args(0).check_function('areas.index', signature=False).check_args(0).has_equal_value()


Ex().check_function("print", index=1).check_args(0).check_function('areas.count', signature=False).has_equal_value()

success_msg("Отлично! Это были примеры методов `list`, которые не изменяют список, для которого они были вызваны.")
```

---

## Методы списков (2)

```yaml
type: NormalExercise
key: 1fbeab82d0
lang: python
xp: 100
skills:
  - 2
```

Большинство методов списков изменяют сам список, к которому они применяются. Примеры таких методов:

- `.append()` — добавляет элемент в конец списка,
- `.remove()` — [удаляет](https://docs.python.org/3/library/stdtypes.html#typesseq-mutable) первый элемент списка, совпадающий с указанным значением,
- `.reverse()` — [переворачивает](https://docs.python.org/3/library/stdtypes.html#typesseq-mutable) порядок элементов в списке.

Вы будете работать со списком `areas`, содержащим площади различных помещений дома.

`@instructions`
- Используйте `.append()` дважды, чтобы добавить площадь бассейного домика и гаража: `24.5` и `15.45` соответственно. Добавьте их именно в таком порядке.
- Выведите `areas` на экран.
- Используйте метод `.reverse()`, чтобы изменить порядок элементов в `areas` на обратный.
- Снова выведите `areas` на экран.

`@hint`
- Для первой инструкции используйте вызов `areas.append(___)` дважды.
- Чтобы вывести переменную `x` на экран, напишите `print(x)`.
- Метод `.reverse()` не требует дополнительных аргументов — просто используйте точечную нотацию и пустые скобки: `.reverse()`.
- Чтобы вывести переменную `x` на экран, напишите `print(x)`.

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

success_msg("Отлично!")
```

---

## Пакеты

```yaml
type: VideoExercise
key: ab96a17c5e
xp: 50
```

`@projector_key`
cedcfb34350be8545599768f96695cdd

---

## Импорт пакета

```yaml
type: NormalExercise
key: 7432a6376f
lang: python
xp: 100
skills:
  - 2
```

Предположим, вам нужно вычислить длину окружности и площадь круга. Вот соответствующие формулы:

$$C = 2 \pi r$$
$$A = \pi r^2 $$

Вместо того чтобы вводить числовое значение `pi` вручную, можно воспользоваться пакетом `math`, в котором оно уже определено.

Для справки: `**` — это оператор возведения в степень. Например, `3**4` означает `3` в степени `4` и даёт результат `81`.

`@instructions`
- Импортируйте пакет `math`.
- Используйте `math.pi`, чтобы вычислить длину окружности, и сохраните результат в переменную `C`.
- Используйте `math.pi`, чтобы вычислить площадь круга, и сохраните результат в переменную `A`.

`@hint`
- Можно просто написать `import math`, а затем обращаться к числу пи через `math.pi`.
- Используйте формулу из условия задания, чтобы найти `C`. Применяйте оператор `*`.
- Используйте формулу из условия задания, чтобы найти `A`. Применяйте операторы `*` и `**`.

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
patt = "Ваше вычисление `%s` не совсем верно. Убедитесь, что используете `math.pi`."
Ex().multi(
  has_import('math', same_as=False),
  check_object('C').has_equal_value(incorrect_msg=patt%'C'),
  check_object('A').has_equal_value(incorrect_msg=patt%'A')
)

Ex().multi(
  has_printout(0, not_printed_msg = "__JINJA__:Оставьте `{{sol_call}}` для вывода длины окружности."),
  has_printout(1, not_printed_msg = "__JINJA__:Оставьте `{{sol_call}}` для вывода площади.")
)

success_msg("Отлично! Если вы умеете работать с функциями из пакетов, в ваших руках оказывается мощь многих программистов на Python!")
```

---

## Выборочный импорт

```yaml
type: NormalExercise
key: fe65eff50a
lang: python
xp: 100
skills:
  - 2
```

Общий импорт, например `import math`, открывает доступ ко **всем** возможностям пакета `math`. Однако если вам нужна только определённая часть пакета, импорт можно сделать более избирательным:

```
from math import pi
```

Попробуйте сделать то же самое, но на этот раз импортируйте только `pi`.

`@instructions`
- Выполните выборочный импорт из пакета `math`, импортировав только функцию `pi`.
- Используйте `pi`, чтобы вычислить длину окружности и сохранить результат в `C`.
- Используйте `pi`, чтобы вычислить площадь круга и сохранить результат в `A`.

`@hint`
- Используйте `from math import pi` для выборочного импорта.
- После этого можно использовать `pi` напрямую!

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
patt = "Ваш расчёт `%s` не совсем верен. Убедитесь, что используете только `pi`."

Ex().has_import("math.pi", not_imported_msg = "Обязательно импортируйте `pi` из пакета `math`. Следует использовать нотацию `from ___ import ___`.",)

Ex().multi(
  check_object('C').has_equal_value(incorrect_msg=patt%'C'),
  check_object('A').has_equal_value(incorrect_msg=patt%'A')
)

Ex().multi(
  has_printout(0, not_printed_msg = "__JINJA__:Оставьте `{{sol_call}}` для вывода длины окружности."),
  has_printout(1, not_printed_msg = "__JINJA__:Оставьте `{{sol_call}}` для вывода площади.")
)

success_msg("Отлично! Переходите к следующему упражнению.")
```

---

## Различные способы импорта

```yaml
type: MultipleChoiceExercise
key: f1b2675a2a
lang: python
xp: 50
skills:
  - 2
```

Существует несколько способов импортировать пакеты и модули в Python. В зависимости от способа импорта вам потребуется использовать разный код.

Предположим, вы хотите использовать [функцию](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.inv.html) `inv()`, которая находится в подпакете `linalg` пакета `scipy`. При этом вы хотите вызывать её следующим образом:

```
my_inv([[1,2], [3,4]])
```

Какой оператор `import` нужен, чтобы этот код выполнился без ошибок?

`@possible_answers`
- `import scipy`
- `import scipy.linalg`
- `from scipy.linalg import my_inv`
- `from scipy.linalg import inv as my_inv`

`@hint`
- Попробуйте разные варианты импорта в оболочке IPython и проверьте, при каком из них строка `my_inv([[1, 2], [3, 4]])` выполняется без ошибок. Нажмите **enter**, чтобы запустить введённый код.

`@pre_exercise_code`
```{python}

```

`@sct`
```{python}
msg1 = msg2 = msg3 = "Неверно, попробуйте ещё раз. Попробуйте различные операторы импорта в оболочке IPython и посмотрите, какой из них позволяет выполнить строку `my_inv([[1, 2], [3, 4]])` без ошибок."
msg4 = "Правильно! Слово `as` позволяет создать локальное имя для импортируемой функции: `inv()` теперь доступна как `my_inv()`."
Ex().has_chosen(4, [msg1, msg2, msg3, msg4])
```

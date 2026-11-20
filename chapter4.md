---
title_meta: Розділ 4
title: NumPy
description: >-
  NumPy — базовий пакет Python для ефективної роботи в науці про дані. Навчіться
  працювати з потужними інструментами масиву NumPy та розпочніть дослідження
  даних.
attachments:
  slides_link: 'https://projector-video-pdf-converter.datacamp.com/735/chapter4.pdf'
lessons:
  - nb_of_exercises: 5
    title: NumPy
  - nb_of_exercises: 5
    title: Двовимірні масиви NumPy
  - nb_of_exercises: 3
    title: 'NumPy: базова статистика'
---

## NumPy

```yaml
type: VideoExercise
key: f4545baa53
xp: 50
```

`@projector_key`
a0487c26210f6b71ea98f917734cea3a

---

## Ваш перший масив NumPy

```yaml
type: NormalExercise
key: 84cab9d170
lang: python
xp: 100
skills:
  - 2
```

Зараз ви поринете у світ бейсболу. Паралельно ви опanuєте основи `numpy` — потужної бібліотеки для роботи з даними.

У Python-скрипті вже визначено список `baseball`, що містить зріст деяких бейсболістів у сантиметрах. Додайте код, щоб створити з нього масив `numpy`.

`@instructions`
- Імпортуйте бібліотеку `numpy` як `np`, щоб звертатися до `numpy` через `np`.
- Використайте `np.array()`, щоб створити масив `numpy` з `baseball`. Назвіть цей масив `np_baseball`.
- Виведіть тип `np_baseball`, щоб переконатися, що все зроблено правильно.

`@hint`
- Скористайтеся `import numpy as np`. Тепер щоразу, коли потрібна функція з `numpy`, використовуйте `np.fun_name()`.
- `np.array()` має отримати на вхід `baseball`. Присвойте результат виклику функції до `np_baseball`.
- Щоб вивести тип змінної `x`, просто наберіть `print(type(x))`.

`@pre_exercise_code`
```{python}
import numpy as np
```

`@sample_code`
```{python}
# Import the numpy package as np


baseball = [180, 215, 210, 210, 188, 176, 209, 200]

# Create a numpy array from baseball: np_baseball


# Print out type of np_baseball

```

`@solution`
```{python}
# Import the numpy package as np
import numpy as np

baseball = [180, 215, 210, 210, 188, 176, 209, 200]

# Create a NumPy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out type of np_baseball
print(type(np_baseball))
```

`@sct`
```{python}
predef_msg = "Вам не потрібно змінювати або видаляти попередньо визначені змінні."
Ex().has_import("numpy")
Ex().check_correct(
  check_object("np_baseball"),
  multi(
    check_object("baseball", missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
    check_function("numpy.array").check_args(0).has_equal_ast()
  )
)

Ex().has_printout(0)
success_msg("Чудова робота!")
```

---

## Зріст гравців у бейсбол

```yaml
type: NormalExercise
key: e7e25a89ea
lang: python
xp: 100
skills:
  - 2
```

Ви — затятий фанат бейсболу. Ви вирішуєте зателефонувати до MLB (Major League Baseball) і дізнатися додаткову статистику щодо зросту основних гравців. Вам передають дані більш ніж про тисячу гравців, збережені у звичайному списку Python: `height_in`. Зріст указано в дюймах. Чи зможете ви створити з нього масив `numpy` і перевести одиниці виміру в метри?

`height_in` уже доступний, а пакет `numpy` завантажено, тож можете одразу починати (джерело: stat.ucla.edu).

`@instructions`
- Створіть масив `numpy` з `height_in`. Назвіть цей новий масив `np_height_in`.
- Виведіть `np_height_in`.
- Помножте `np_height_in` на `0.0254`, щоб перевести всі вимірювання зросту з дюймів у метри. Збережіть нові значення в новому масиві `np_height_m`.
- Виведіть `np_height_m` і перевірте, чи результати мають сенс.

`@hint`
- Використайте `np.array()` і передайте туди `height`. Збережіть результат у `np_height_in`.
- Щоб вивести змінну `x`, введіть у скрипті Python `print(x)`.
- Виконуйте обчислення так, ніби `np_height_in` — це одне число: `np_height_in * conversion_factor` є частиною відповіді.
- Щоб вивести змінну `x`, введіть у скрипті Python `print(x)`.

`@pre_exercise_code`
```{python}
import pandas as pd
mlb = pd.read_csv("https://assets.datacamp.com/course/intro_to_python/baseball.csv")
height_in = mlb['Height'].tolist()
import numpy as np
```

`@sample_code`
```{python}
# Import numpy
import numpy as np

# Create a numpy array from height_in: np_height_in


# Print out np_height_in


# Convert np_height_in to m: np_height_m


# Print np_height_m

```

`@solution`
```{python}
# Import numpy
import numpy as np

# Create a numpy array from height_in: np_height_in
np_height_in = np.array(height_in)

# Print out np_height_in
print(np_height_in)

# Convert np_height_in to m: np_height_m
np_height_m = np_height_in * 0.0254

# Print np_height_m
print(np_height_m)
```

`@sct`
```{python}
Ex().has_import("numpy", same_as = False)

Ex().check_correct(
  has_printout(0),
  check_correct(
    check_object('np_height_in').has_equal_value(),
    check_function('numpy.array').check_args(0).has_equal_ast()
  )
)

Ex().check_correct(
  has_printout(1),
  check_object("np_height_m").has_equal_value(incorrect_msg = "Використовуйте `np_height_in * 0.0254` для обчислення `np_height_m`.")
)

success_msg("Чудово! Миттєво `numpy` виконує множення на більш ніж 1000 вимірювань висоти.")
```

---

## Побічні ефекти NumPy

```yaml
type: MultipleChoiceExercise
key: 3662ff6637
lang: python
xp: 50
skills:
  - 2
```

`numpy` чудово підходить для векторної арифметики. Але якщо порівняти його можливості зі звичайними списками Python, деякі речі відрізняються.

По-перше, масиви `numpy` не можуть містити елементи різних типів. Якщо ви змішуєте типи, як-от булеві значення та цілі числа, `numpy` автоматично перетворює їх до спільного типу. Булеві значення `True` і `False` під час поєднання з числами розглядаються як `1` і `0`, тож у підсумку масив стає цілими числами.

По-друге, звичні арифметичні оператори, як-от `+`, `-`, `*` і `/`, мають інше значення для звичайних списків Python і масивів `numpy`.

Виберіть код, який дає такий результат:

```
np.array([True, 1, 2]) + np.array([3, 4, False])
```

Пакет `numpy` уже імпортовано як `np`. Ви можете запустити кожен варіант в IPython Shell, щоб побачити результат.

`@possible_answers`
- `np.array([True, 1, 2, 3, 4, False])`
- `np.array([4, 3, 0]) + np.array([0, 2, 2])`
- `np.array([1, 1, 2]) + np.array([3, 4, -1])`
- `np.array([0, 1, 2, 3, 4, 5])`

`@hint`
- Скопіюйте різні фрагменти коду та вставте їх в IPython Shell. Натисніть **enter**, щоб запустити код і побачити, який результат збігається з тим, що отримано виразом `np.array([True, 1, 2]) + np.array([3, 4, False])`.

`@pre_exercise_code`
```{python}
import numpy as np
```

`@sct`
```{python}
msg1 = msg3 = msg4 = "Неправильно. Спробуйте різні фрагменти коду та подивіться, який з них відповідає цільовому фрагменту коду."
msg2 = "Чудова робота! `True` перетворюється на 1, `False` перетворюється на 0."
Ex().has_chosen(2, [msg1, msg2, msg3, msg4])
```

---

## Вибірка з масивів NumPy

```yaml
type: NormalExercise
key: fcb2a9007b
lang: python
xp: 100
skills:
  - 2
```

Вибірка (використання квадратних дужок для списків або масивів) працює однаково і для списків, і для масивів.

У цій вправі у тлі вже завантажено два списки `height_in` і `weight_lb`. Вони містять зріст і вагу гравців MLB як звичайні списки. Також для вас підготовлено два масиви `numpy`: `np_weight_lb` і `np_height_in`.

`@instructions`
- Зробіть вибірку з `np_weight_lb`, надрукувавши елемент з індексом 50.
- Надрукуйте підмасив `np_height_in`, який містить елементи з індексу 100 до індексу 110 включно.

`@hint`
- Обов'язково обгорніть операції вибірки у виклик `print()`.
- Використайте `[100:111]`, щоб отримати елементи з індексу 100 до індексу 110 включно.

`@pre_exercise_code`
```{python}
import pandas as pd
mlb = pd.read_csv("https://assets.datacamp.com/course/intro_to_python/baseball.csv")
height_in = mlb['Height'].tolist()
weight_lb = mlb['Weight'].tolist()
```

`@sample_code`
```{python}
import numpy as np

np_weight_lb = np.array(weight_lb)
np_height_in = np.array(height_in)

# Print out the weight at index 50


# Print out sub-array of np_height_in: index 100 up to and including index 110

```

`@solution`
```{python}
import numpy as np

np_weight_lb = np.array(weight_lb)
np_height_in = np.array(height_in)

# Print out the weight at index 50
print(np_weight_lb[50])

# Print out sub-array of np_height_in: index 100 up to and including index 110
print(np_height_in[100:111])
```

`@sct`
```{python}
Ex().has_import("numpy", same_as=False)
msg = "Вам не потрібно змінювати або видаляти попередньо визначені змінні."
Ex().multi(
    check_object("np_height_in", missing_msg=msg).has_equal_value(incorrect_msg = msg),
    check_object("np_weight_lb", missing_msg=msg).has_equal_value(incorrect_msg = msg)
)

Ex().has_printout(0)
Ex().has_printout(1)

success_msg("Чудово! Час дізнатися щось нове: двовимірні масиви NumPy!")
```

---

## Двовимірні масиви NumPy

```yaml
type: VideoExercise
key: 1241efac7a
xp: 50
```

`@projector_key`
ae3238dcc7feb9adecfee0c395fc8dc8

---

## Ваш перший 2D-масив NumPy

```yaml
type: NormalExercise
key: 5cb045bb13
lang: python
xp: 100
skills:
  - 2
```

Перш ніж працювати з реальними даними MLB, спробуймо створити 2D масив `numpy` з невеликого списку списків.

У цій вправі `baseball` — це список списків. Головний список містить 4 елементи. Кожен із цих елементів — список, що містить зріст і вагу 4 гравців у бейсбол, саме в такому порядку. Змінна `baseball` уже додана для вас у скрипт.

`@instructions`
- Використайте `np.array()`, щоб створити 2D масив `numpy` з `baseball`. Назвіть його `np_baseball`.
- Виведіть тип `np_baseball`.
- Виведіть атрибут `shape` об'єкта `np_baseball`. Використайте `np_baseball.shape`.

`@hint`
- `baseball` уже заготовлено для вас у скрипті. Викличте `np.array()` для нього та збережіть отриманий 2D масив `numpy` у змінній `np_baseball`.
- Для другої інструкції скористайтеся `print()` разом із `type()`.
- `np_baseball.shape` повертає розміри `np_baseball`. Не забудьте обгорнути це викликом `print()`.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
import numpy as np

baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

# Create a 2D numpy array from baseball: np_baseball


# Print out the type of np_baseball


# Print out the shape of np_baseball

```

`@solution`
```{python}
import numpy as np

baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

# Create a 2D numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out the type of np_baseball
print(type(np_baseball))

# Print out the shape of np_baseball
print(np_baseball.shape)
```

`@sct`
```{python}
msg = "Вам не потрібно змінювати або видаляти попередньо визначені змінні."
Ex().check_object("baseball", missing_msg=msg).has_equal_value(incorrect_msg = msg)
Ex().has_import("numpy", same_as = False)

Ex().check_correct(
    multi(
        has_printout(0),
        has_printout(1)
    ),
    check_correct(
        check_object('np_baseball').has_equal_value(),
        check_function('numpy.array').check_args(0).has_equal_ast()
    )
)

success_msg("Чудово! Тепер Ви готові перетворити фактичні дані MLB у 2D масив `numpy`!")
```

---

## Дані з бейсболу у 2D-формі

```yaml
type: NormalExercise
key: 5df25d0b7b
lang: python
xp: 100
skills:
  - 2
```

Ви розумієте, що логічніше перетворити всю цю інформацію на двовимірний масив `numpy`.

У вас є список списків Python. У цьому списку кожен підсписок містить зріст і вагу одного гравця в бейсбол. Назва цього списку — `baseball`, і його вже завантажено для вас (хоча ви його не бачите).

Збережіть дані як двовимірний масив, щоб отримати додаткові можливості `numpy`.

`@instructions`
- Використайте `np.array()`, щоб створити двовимірний масив `numpy` з `baseball`. Назвіть його `np_baseball`.
- Виведіть атрибут `shape` змінної `np_baseball`.

`@hint`
- `baseball` уже доступний у середовищі Python. Викличте `np.array()` для нього та збережіть отриманий двовимірний масив `numpy` у змінній `np_baseball`.
- `np_baseball.shape` поверне розмірності `np_baseball`. Обовʼязково обгорніть це викликом `print()`.

`@pre_exercise_code`
```{python}
import pandas as pd
baseball = pd.read_csv("https://assets.datacamp.com/course/intro_to_python/baseball.csv")[['Height', 'Weight']].to_numpy().tolist()
import numpy as np
```

`@sample_code`
```{python}
import numpy as np

# Create a 2D numpy array from baseball: np_baseball
np_baseball = 

# Print out the shape of np_baseball

```

`@solution`
```{python}
import numpy as np

# Create a 2D numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out the shape of np_baseball
print(np_baseball.shape)
```

`@sct`
```{python}
Ex().has_import("numpy", same_as = False)

Ex().check_correct(
    has_printout(0),
    check_correct(
        check_object('np_baseball').has_equal_value(),
        check_function('numpy.array').check_args(0).has_equal_ast()
    )
)

success_msg("Чудово! Час продемонструвати деякі вражаючі можливості багатовимірних масивів `numpy`!")
```

---

## Вибір підмножин у 2D-масивах NumPy

```yaml
type: NormalExercise
key: aeca4977f0
lang: python
xp: 100
skills:
  - 2
```

Якщо ваш 2D-масив `numpy` має регулярну структуру, тобто в кожному рядку та стовпці фіксована кількість значень, складні варіанти вибірки підмножин стають дуже простими. Подивіться на код нижче, де елементи `"a"` і `"c"` видобуваються зі списку списків.

```
# numpy
import numpy as np
np_x = np.array(x)
np_x[:, 0]
```

Індекси перед комою стосуються рядків, а після коми — стовпців. Символ `:` означає зріз; у цьому прикладі він вказує Python включити всі рядки.

`@instructions`
- Виведіть 50-й рядок масиву `np_baseball`.
- Створіть нову змінну `np_weight_lb`, що містить увесь другий стовпець `np_baseball`.
- Виберіть зріст (перший стовпець) 124-го бейсболіста в `np_baseball` і виведіть його.

`@hint`
- Вам потрібен рядок з індексом 49 у першій інструкції! Точніше, використайте `[49, :]`.
- Щоб вибрати весь другий стовпець, скористайтеся `[:, 1]`.
- Для останньої інструкції використайте `[123, 0]`; не забудьте обгорнути це у виклик `print()`.

`@pre_exercise_code`
```{python}
import pandas as pd
baseball = pd.read_csv("https://assets.datacamp.com/course/intro_to_python/baseball.csv")[['Height', 'Weight']].to_numpy().tolist()
import numpy as np
```

`@sample_code`
```{python}
import numpy as np

np_baseball = np.array(baseball)

# Print out the 50th row of np_baseball


# Select the entire second column of np_baseball: np_weight_lb


# Print out height of 124th player

```

`@solution`
```{python}
import numpy as np

np_baseball = np.array(baseball)

# Print out the 50th row of np_baseball
print(np_baseball[49,:])

# Select the entire second column of np_baseball: np_weight_lb
np_weight_lb = np_baseball[:,1]

# Print out height of 124th player
print(np_baseball[123, 0])
```

`@sct`
```{python}
msg = "Вам не потрібно змінювати або видаляти попередньо визначені змінні."
Ex().multi(
    has_import("numpy", same_as = False),
    check_object("np_baseball", missing_msg=msg).has_equal_value(incorrect_msg = msg)
)

Ex().has_printout(0)

Ex().check_object('np_weight_lb').has_equal_value(incorrect_msg = "Ви можете використовувати `np_baseball[:,1]` для визначення `np_weight_lb`. Це вибере весь перший стовпець.")

Ex().has_printout(1)

success_msg("Це йде добре!")
```

---

## 2D-арифметика

```yaml
type: NormalExercise
key: 1c2378b677
lang: python
xp: 100
skills:
  - 2
```

Двовимірні масиви `numpy` можуть виконувати обчислення покомпонентно, як і звичайні масиви `numpy`.

`np_baseball` уже підготовлено; це знову 2D-масив `numpy` із 3 стовпцями, що відповідають зросту (у дюймах), вазі (у фунтах) та віку (у роках). `baseball` доступний як звичайний список зі списків, а `updated` — як двовимірний масив numpy.

`@instructions`
- Ви отримали зміни зросту, ваги та віку всіх гравців у бейсбол. Вони доступні як 2D-масив `numpy` — `updated`. Додайте `np_baseball` і `updated` та виведіть результат.
- Ви хочете перевести одиниці зросту й ваги в метричні (метри та кілограми відповідно). Спочатку створіть масив `numpy` із трьома значеннями: `0.0254`, `0.453592` і `1`. Назвіть цей масив `conversion`.
- Помножте `np_baseball` на `conversion` та виведіть результат.

`@hint`
- `np_baseball + updated` виконає покомпонентне додавання двох масивів `numpy`.
- Створіть масив `numpy` за допомогою `np.array()`; вхідні дані — звичайний список Python із трьох елементів.
- `np_baseball * conversion` спрацює без додаткових дій. Спробуйте! Обов'язково обгорніть це у виклик `print()`.

`@pre_exercise_code`
```{python}
import pandas as pd
import numpy as np
baseball = pd.read_csv("https://assets.datacamp.com/course/intro_to_python/baseball.csv")[['Height', 'Weight', 'Age']].to_numpy().tolist()
n = len(baseball)
updated = np.array(pd.read_csv("https://assets.datacamp.com/course/intro_to_python/update.csv", header = None))
import numpy as np
```

`@sample_code`
```{python}
import numpy as np

np_baseball = np.array(baseball)

# Print out addition of np_baseball and updated


# Create numpy array: conversion


# Print out product of np_baseball and conversion

```

`@solution`
```{python}
import numpy as np

np_baseball = np.array(baseball)

# Print out addition of np_baseball and updated
print(np_baseball + updated)

# Create numpy array: conversion
conversion = np.array([0.0254, 0.453592, 1])

# Print out product of np_baseball and conversion
print(np_baseball * conversion)
```

`@sct`
```{python}
Ex().has_import("numpy")

msg = "Вам не потрібно змінювати або видаляти попередньо визначені змінні."
Ex().check_object("np_baseball", missing_msg=msg).has_equal_value(incorrect_msg = msg)

Ex().has_printout(0)

Ex().check_correct(
    has_printout(1),
    check_correct(
        check_object('conversion').has_equal_value(),
        check_function('numpy.array', index = 1).check_args(0).has_equal_value()
    )    
)

success_msg("Чудова робота! Зверніть увагу, як за допомогою дуже невеликої кількості коду ви можете змінити всі значення у вашій структурі даних `numpy` дуже специфічним чином. Це буде дуже корисно у вашому майбутньому як дата-сайентиста!")
```

---

## NumPy: базова статистика

```yaml
type: VideoExercise
key: 287995e488
xp: 50
```

`@projector_key`
34495ba457d74296794d2a122c9b6e19

---

## Середнє проти медіани

```yaml
type: NormalExercise
key: 509c588eb6
lang: python
xp: 100
skills:
  - 2
```

Тепер ви знаєте, як використовувати функції `numpy`, щоб краще відчути свої дані.

Дані з бейсболу доступні як 2D-масив `numpy` із 3 стовпцями (зріст, вага, вік) і 1015 рядками. Назва цього масиву `numpy` — `np_baseball`. Однак після переформатування даних ви помічаєте, що деякі значення зросту аномально великі. Виконайте інструкції та з'ясуйте, яка підсумкова статистика найкраще підходить, якщо ви маєте справу з так званими „викидами". `np_baseball` доступний.

`@instructions`
- Створіть масив `numpy` `np_height_in`, який дорівнює першому стовпцю `np_baseball`.
- Виведіть середнє значення `np_height_in`.
- Виведіть медіану `np_height_in`.

`@hint`
- Використайте індексування 2D-масиву `numpy`: `[:,0]` є частиною розв'язку.
- Якщо `numpy` імпортовано як `np`, ви можете скористатися `np.mean()`, щоб обчислити середнє значення масиву NumPy. Не забудьте додати виклик `print()`.
- Для останньої інструкції скористайтеся `np.median()`.

`@pre_exercise_code`
```{python}
import pandas as pd
np_baseball = pd.read_csv("https://assets.datacamp.com/course/intro_to_python/baseball.csv")[['Height', 'Weight', 'Age']].to_numpy()
np_baseball[slice(0, 1015, 50), 0] = np_baseball[slice(0, 1015, 50), 0]*1000
import numpy as np
```

`@sample_code`
```{python}
import numpy as np

# Create np_height_in from np_baseball


# Print out the mean of np_height_in


# Print out the median of np_height_in

```

`@solution`
```{python}
import numpy as np

# Create np_height_in from np_baseball
np_height_in = np_baseball[:,0]

# Print out the mean of np_height_in
print(np.mean(np_height_in))

# Print out the median of np_height_in
print(np.median(np_height_in))
```

`@sct`
```{python}
Ex().has_import("numpy", same_as = False)

Ex().check_object("np_height_in").has_equal_value(incorrect_msg = "Ви можете використовувати `np_baseball[:,0]`, щоб вибрати перший стовпець з `np_baseball`"),

Ex().check_correct(
    has_printout(0),
    check_function('numpy.mean').has_equal_value()
)

Ex().check_correct(
    has_printout(1),
    check_function('numpy.median').has_equal_value()
)

success_msg("Середня висота 1586 дюймів, це не звучить правильно, чи не так? Однак, медіана, здається, не піддається впливу викидів: 74 дюйми виглядають цілком логічно. Завжди корисно перевіряти як медіану, так і середнє значення, щоб отримати уявлення про загальний розподіл всього набору даних.")
```

---

## Дослідження даних із бейсболу

```yaml
type: NormalExercise
key: '4409948807'
lang: python
xp: 100
skills:
  - 2
```

Оскільки середнє і медіана так сильно відрізняються, ви вирішуєте поскаржитися до MLB. Вони знаходять помилку та надсилають вам виправлені дані. Вони знову доступні як 2D-масив NumPy `np_baseball` із трьома стовпцями.

Скрипт Python в редакторі вже містить код, який виводить інформативні повідомлення з різними описовими статистиками, а `numpy` уже імпортовано як `np`. Чи зможете ви завершити завдання? `np_baseball` доступний.

`@instructions`
- Код для виведення середнього зросту вже додано. Доповніть код для медіанного зросту.
- Використайте `np.std()` для першого стовпця `np_baseball`, щоб обчислити `stddev`.
- Чи мають великі гравці тенденцію бути важчими? Використайте `np.corrcoef()`, щоб зберегти кореляцію між першим і другим стовпцями `np_baseball` у змінній `corr`.

`@hint`
- Використайте `np.median()`, щоб обчислити медіану. Спершу оберіть правильний стовпець!
- Виділіть той самий стовпець, коли рахуєте стандартне відхилення за допомогою `np.std()`.
- Скористайтеся `np_baseball[:, 0]` і `np_baseball[:, 1]`, щоб вибрати перший і другий стовпці; ці значення є вхідними для `np.corrcoef()`.

`@pre_exercise_code`
```{python}
import pandas as pd
np_baseball = pd.read_csv("https://assets.datacamp.com/course/intro_to_python/baseball.csv")[['Height', 'Weight', 'Age']].to_numpy()
import numpy as np
```

`@sample_code`
```{python}
avg = np.mean(np_baseball[:,0])
print("Average: " + str(avg))

# Print median height
med = ____
print("Median: " + str(med))

# Print out the standard deviation on height
stddev = ____
print("Standard Deviation: " + str(stddev))

# Print out correlation between first and second column
corr = ____
print("Correlation: " + str(corr))
```

`@solution`
```{python}
avg = np.mean(np_baseball[:,0])
print("Average: " + str(avg))

# Print median height
med = np.median(np_baseball[:,0])
print("Median: " + str(med))

# Print out the standard deviation on height
stddev = np.std(np_baseball[:,0])
print("Standard Deviation: " + str(stddev))

# Print out correlation between first and second column
corr = np.corrcoef(np_baseball[:,0], np_baseball[:,1])
print("Correlation: " + str(corr))
```

`@sct`
```{python}
msg = "Ви не повинні змінювати або видаляти заздалегідь визначену змінну `avg`."
Ex().check_object("avg", missing_msg=msg).has_equal_value(incorrect_msg=msg)

missing = "Ви використали `np.median()` для обчислення медіани?"
incorrect = "Щоб обчислити `med`, передайте перший стовпець `np_baseball` до `numpy.median()`. Приклад `np.mean()` показує, як це зробити."
Ex().check_correct(
  check_object("med").has_equal_value(),
  check_function("numpy.median", index=0, missing_msg=missing).check_args(0).has_equal_value(incorrect_msg=incorrect)
)

missing = "Ви використали `np.std()` для обчислення стандартного відхилення?"
incorrect = "Щоб обчислити `stddev`, передайте перший стовпець `np_baseball` до `numpy.std()`. Приклад `np.mean()` показує, як це зробити."
Ex().check_correct(
  check_object("stddev").has_equal_value(),
  check_function("numpy.std", index=0, missing_msg=missing).check_args(0).has_equal_value(incorrect_msg=incorrect)
)

missing = "Ви використали `np.corrcoef()` для обчислення кореляції?"
incorrect1 = "Щоб обчислити `corr`, першим аргументом до `np.corrcoef()` повинен бути перший стовпець `np_baseball`, так само, як це було зроблено раніше."
incorrect2 = "Щоб обчислити `corr`, другим аргументом до `np.corrcoef()` повинен бути другий стовпець `np_baseball`. Замість `[:,0]`, цього разу використовуйте `[:,1]`."
Ex().check_correct(
  check_object("corr").has_equal_value(),
  check_function("numpy.corrcoef", index=0, missing_msg=missing).multi(
    check_args(0, missing_msg=incorrect1).has_equal_value(incorrect_msg=incorrect1),
    check_args(1, missing_msg=incorrect2).has_equal_value(incorrect_msg=incorrect2)
  )
)

success_msg("Чудова робота! Ви заклали міцний фундамент - тепер настав час використовувати всі ваші нові навички в галузі науки про дані, щоб вирішувати більше завдань і робити вплив.")
```

---
title_meta: Глава 4
title: NumPy
description: >-
  NumPy — фундаментальный пакет Python для науки о данных. Вы научитесь работать
  с массивами NumPy и сделаете первые шаги в исследовании данных.
attachments:
  slides_link: 'https://projector-video-pdf-converter.datacamp.com/735/chapter4.pdf'
lessons:
  - nb_of_exercises: 5
    title: NumPy
  - nb_of_exercises: 5
    title: Двумерные массивы NumPy
  - nb_of_exercises: 3
    title: 'NumPy: базовая статистика'
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

## Ваш первый массив NumPy

```yaml
type: NormalExercise
key: 84cab9d170
lang: python
xp: 100
skills:
  - 2
```

Сейчас мы погрузимся в мир бейсбола — и заодно познакомимся с основами `numpy`, мощного пакета для анализа данных.

В скрипте уже определён список `baseball`, содержащий рост некоторых бейсбольных игроков в сантиметрах. Добавьте код, который создаст на его основе массив `numpy`.

`@instructions`
- Импортируйте пакет `numpy` под псевдонимом `np`, чтобы обращаться к нему как `np`.
- С помощью `np.array()` создайте массив `numpy` из списка `baseball`. Назовите этот массив `np_baseball`.
- Выведите тип переменной `np_baseball`, чтобы убедиться, что всё сделано правильно.

`@hint`
- `import numpy as np` — это то, что нужно. После этого для вызова любой функции `numpy` используйте синтаксис `np.fun_name()`.
- Передайте `baseball` в качестве аргумента функции `np.array()`. Присвойте результат переменной `np_baseball`.
- Чтобы вывести тип переменной `x`, используйте `print(type(x))`.

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
predef_msg = "Вам не нужно изменять или удалять предопределённые переменные."
Ex().has_import("numpy")
Ex().check_correct(
  check_object("np_baseball"),
  multi(
    check_object("baseball", missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
    check_function("numpy.array").check_args(0).has_equal_ast()
  )
)

Ex().has_printout(0)
success_msg("Отличная работа!")
```

---

## Рост игроков в бейсбол

```yaml
type: NormalExercise
key: e7e25a89ea
lang: python
xp: 100
skills:
  - 2
```

Вы большой поклонник бейсбола. Вы решаете позвонить в MLB (Главную лигу бейсбола) и узнать дополнительную статистику о росте ведущих игроков. Вам передают данные о более чем тысяче игроков — они хранятся в виде обычного списка Python: `height_in`. Рост указан в дюймах. Попробуйте создать массив `numpy` из этих данных и перевести значения в метры.

`height_in` уже доступна, а пакет `numpy` загружен, так что можно приступать прямо сейчас (источник: stat.ucla.edu).

`@instructions`
- Создайте массив `numpy` из `height_in`. Назовите новый массив `np_height_in`.
- Выведите `np_height_in` на экран.
- Умножьте `np_height_in` на `0.0254`, чтобы перевести все значения роста из дюймов в метры. Сохраните новые значения в массив `np_height_m`.
- Выведите `np_height_m` и проверьте, выглядит ли результат корректно.

`@hint`
- Используйте `np.array()`, передав в неё `height`. Сохраните результат в `np_height_in`.
- Чтобы вывести переменную `x`, напишите `print(x)` в скрипте Python.
- Выполняйте вычисления так, как если бы `np_height_in` было обычным числом: `np_height_in * conversion_factor` — часть ответа.
- Чтобы вывести переменную `x`, напишите `print(x)` в скрипте Python.

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
  check_object("np_height_m").has_equal_value(incorrect_msg = "Используйте `np_height_in * 0.0254` для вычисления `np_height_m`.")
)

success_msg("Отлично! В мгновение ока `numpy` выполняет умножение более чем 1000 измерений роста.")
```

---

## Побочные эффекты NumPy

```yaml
type: MultipleChoiceExercise
key: 3662ff6637
lang: python
xp: 50
skills:
  - 2
```

`numpy` отлично подходит для векторных вычислений. Однако если сравнить его с обычными списками Python, можно заметить некоторые отличия.

Во-первых, массивы `numpy` не могут содержать элементы разных типов. Если смешать типы, например булевы значения и целые числа, `numpy` автоматически приведёт их к общему типу. Значения `True` и `False` при сочетании с числами интерпретируются как `1` и `0`, поэтому итоговый массив будет состоять из целых чисел.

Во-вторых, стандартные арифметические операторы `+`, `-`, `*` и `/` работают по-разному для обычных списков Python и массивов `numpy`.

Выберите код, который даёт следующий результат:

```
np.array([True, 1, 2]) + np.array([3, 4, False])
```

Пакет `numpy` уже импортирован как `np`. Запустите каждый вариант в оболочке IPython, чтобы увидеть результат.

`@possible_answers`
- `np.array([True, 1, 2, 3, 4, False])`
- `np.array([4, 3, 0]) + np.array([0, 2, 2])`
- `np.array([1, 1, 2]) + np.array([3, 4, -1])`
- `np.array([0, 1, 2, 3, 4, 5])`

`@hint`
- Скопируйте каждый из вариантов кода и вставьте его в оболочку IPython. Нажмите **Enter**, чтобы запустить код, и проверьте, какой результат совпадает с выводом выражения `np.array([True, 1, 2]) + np.array([3, 4, False])`.

`@pre_exercise_code`
```{python}
import numpy as np
```

`@sct`
```{python}
msg1 = msg3 = msg4 = "Неверно. Попробуйте различные фрагменты кода и посмотрите, какой из них соответствует целевому фрагменту кода."
msg2 = "Отлично! `True` преобразуется в 1, `False` преобразуется в 0."
Ex().has_chosen(2, [msg1, msg2, msg3, msg4])
```

---

## Выборка элементов из массивов NumPy

```yaml
type: NormalExercise
key: fcb2a9007b
lang: python
xp: 100
skills:
  - 2
```

Выборка элементов (с помощью квадратных скобок) работает одинаково как для списков, так и для массивов.

В этом упражнении уже загружены два списка — `height_in` и `weight_lb` — с ростом и весом игроков MLB в виде обычных списков. Также подготовлены два массива `numpy`: `np_weight_lb` и `np_height_in`.

`@instructions`
- Выполните выборку из `np_weight_lb`, выведя элемент с индексом 50.
- Выведите подмассив из `np_height_in`, содержащий элементы с индекса 100 по 110 **включительно**.

`@hint`
- Не забудьте обернуть операции выборки в вызов `print()`.
- Используйте `[100:111]`, чтобы получить элементы с индекса 100 по 110 включительно.

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
msg = "Вам не нужно изменять или удалять предопределённые переменные."
Ex().multi(
    check_object("np_height_in", missing_msg=msg).has_equal_value(incorrect_msg = msg),
    check_object("np_weight_lb", missing_msg=msg).has_equal_value(incorrect_msg = msg)
)

Ex().has_printout(0)
Ex().has_printout(1)

success_msg("Отлично! Пришло время узнать кое-что новое: двумерные массивы NumPy!")
```

---

## Двумерные массивы NumPy

```yaml
type: VideoExercise
key: 1241efac7a
xp: 50
```

`@projector_key`
ae3238dcc7feb9adecfee0c395fc8dc8

---

## Ваш первый двумерный массив NumPy

```yaml
type: NormalExercise
key: 5cb045bb13
lang: python
xp: 100
skills:
  - 2
```

Прежде чем работать с реальными данными MLB, давайте попробуем создать двумерный массив `numpy` из небольшого списка списков.

В этом упражнении `baseball` — это список списков. Главный список содержит 4 элемента. Каждый из них — список с ростом и весом одного из 4 бейсболистов, именно в таком порядке. Переменная `baseball` уже определена в скрипте.

`@instructions`
- С помощью `np.array()` создайте двумерный массив `numpy` из `baseball`. Назовите его `np_baseball`.
- Выведите тип переменной `np_baseball`.
- Выведите атрибут `shape` массива `np_baseball`, используя `np_baseball.shape`.

`@hint`
- Переменная `baseball` уже определена в скрипте. Вызовите `np.array()` на её основе и сохраните полученный двумерный массив `numpy` в переменную `np_baseball`.
- Для второй инструкции используйте `print()` вместе с `type()`.
- `np_baseball.shape` покажет размерность массива `np_baseball`. Не забудьте обернуть этот вызов в `print()`.

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
msg = "Вам не нужно изменять или удалять предопределённые переменные."
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

success_msg("Отлично! Теперь вы готовы преобразовать реальные данные MLB в двумерный массив `numpy`!")
```

---

## Данные о бейсболистах в двумерном формате

```yaml
type: NormalExercise
key: 5df25d0b7b
lang: python
xp: 100
skills:
  - 2
```

Вы понимаете, что удобнее организовать все эти данные в виде двумерного массива `numpy`.

У вас есть список списков Python. В каждом вложенном списке хранятся рост и вес одного бейсболиста. Этот список называется `baseball` и уже загружен для вас (хотя вы его не видите).

Сохраните данные в виде двумерного массива, чтобы воспользоваться расширенными возможностями `numpy`.

`@instructions`
- С помощью `np.array()` создайте двумерный массив `numpy` из `baseball`. Назовите его `np_baseball`.
- Выведите на экран атрибут `shape` массива `np_baseball`.

`@hint`
- Переменная `baseball` уже доступна в среде Python. Вызовите `np.array()` для неё и сохраните полученный двумерный массив `numpy` в переменную `np_baseball`.
- `np_baseball.shape` возвращает размерность массива `np_baseball`. Не забудьте обернуть этот вызов в `print()`.

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

success_msg("Отлично! Пришло время продемонстрировать некоторые выдающиеся возможности многомерных массивов `numpy`!")
```

---

## Извлечение данных из двумерных массивов NumPy

```yaml
type: NormalExercise
key: aeca4977f0
lang: python
xp: 100
skills:
  - 2
```

Если двумерный массив `numpy` имеет регулярную структуру, то есть каждая строка и каждый столбец содержат фиксированное количество элементов, работа с подмножествами становится очень простой. Рассмотрите код ниже, в котором элементы `"a"` и `"c"` извлекаются из списка списков.

```
# numpy
import numpy as np
np_x = np.array(x)
np_x[:, 0]
```

Индексы до запятой относятся к строкам, а после запятой — к столбцам. Символ `:` используется для срезов; в данном примере он указывает Python включить все строки.

`@instructions`
- Выведите на экран 50-ю строку массива `np_baseball`.
- Создайте новую переменную `np_weight_lb`, содержащую весь второй столбец массива `np_baseball`.
- Выберите рост (первый столбец) 124-го бейсболиста из массива `np_baseball` и выведите его на экран.

`@hint`
- В первой инструкции вам нужен индекс строки 49! Точнее, используйте `[49, :]`.
- Чтобы выбрать весь второй столбец, используйте `[:, 1]`.
- В последней инструкции применяйте `[123, 0]`; не забудьте обернуть всё в оператор `print()`.

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
msg = "Вам не нужно изменять или удалять предопределённые переменные."
Ex().multi(
    has_import("numpy", same_as = False),
    check_object("np_baseball", missing_msg=msg).has_equal_value(incorrect_msg = msg)
)

Ex().has_printout(0)

Ex().check_object('np_weight_lb').has_equal_value(incorrect_msg = "Вы можете использовать `np_baseball[:,1]` для определения `np_weight_lb`. Это выберет весь первый столбец.")

Ex().has_printout(1)

success_msg("Всё идёт хорошо!")
```

---

## Арифметика с двумерными массивами

```yaml
type: NormalExercise
key: 1c2378b677
lang: python
xp: 100
skills:
  - 2
```

Двумерные массивы `numpy` поддерживают поэлементные вычисления — так же, как и обычные массивы `numpy`.

`np_baseball` уже задан в коде — это двумерный массив `numpy` с тремя столбцами: рост (в дюймах), вес (в фунтах) и возраст (в годах). `baseball` доступен как обычный список списков, а `updated` — как двумерный массив `numpy`.

`@instructions`
- Вам удалось получить данные об изменениях роста, веса и возраста всех бейсболистов. Они хранятся в двумерном массиве `numpy` с именем `updated`. Сложите `np_baseball` и `updated` и выведите результат на экран.
- Вы хотите перевести единицы измерения роста и веса в метрическую систему (метры и килограммы соответственно). Для начала создайте массив `numpy` из трёх значений: `0.0254`, `0.453592` и `1`. Назовите этот массив `conversion`.
- Умножьте `np_baseball` на `conversion` и выведите результат на экран.

`@hint`
- `np_baseball + updated` выполнит поэлементное сложение двух массивов `numpy`.
- Создайте массив `numpy` с помощью `np.array()`; на входе — обычный список Python из трёх элементов.
- `np_baseball * conversion` сработает без дополнительных действий. Попробуйте! Не забудьте обернуть результат в вызов `print()`.

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

msg = "Вам не нужно изменять или удалять предопределённые переменные."
Ex().check_object("np_baseball", missing_msg=msg).has_equal_value(incorrect_msg = msg)

Ex().has_printout(0)

Ex().check_correct(
    has_printout(1),
    check_correct(
        check_object('conversion').has_equal_value(),
        check_function('numpy.array', index = 1).check_args(0).has_equal_value()
    )    
)

success_msg("Отличная работа! Обратите внимание, как с помощью совсем небольшого количества кода можно изменить все значения в структуре данных `numpy` очень специфическим образом. Это будет очень полезно в вашей будущей карьере специалиста по данным!")
```

---

## NumPy: основы статистики

```yaml
type: VideoExercise
key: 287995e488
xp: 50
```

`@projector_key`
34495ba457d74296794d2a122c9b6e19

---

## Среднее значение и медиана

```yaml
type: NormalExercise
key: 509c588eb6
lang: python
xp: 100
skills:
  - 2
```

Теперь вы умеете применять функции `numpy`, чтобы лучше понять свои данные.

Данные о бейсболистах представлены в виде двумерного массива `numpy` с 3 столбцами (рост, вес, возраст) и 1015 строками. Массив называется `np_baseball`. После преобразования данных вы замечаете, что некоторые значения роста аномально велики. Выполните инструкции и выясните, какая описательная статистика лучше подходит для работы с так называемыми _выбросами_. Массив `np_baseball` уже доступен.

`@instructions`
- Создайте массив `numpy` с именем `np_height_in`, равный первому столбцу массива `np_baseball`.
- Выведите на экран среднее значение `np_height_in`.
- Выведите на экран медиану `np_height_in`.

`@hint`
- Используйте двумерную индексацию `numpy`: `[:,0]` — часть решения.
- Если `numpy` импортирован как `np`, применяйте `np.mean()` для вычисления среднего значения массива NumPy. Не забудьте обернуть результат в вызов `print()`.
- Для последней инструкции используйте `np.median()`.

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

Ex().check_object("np_height_in").has_equal_value(incorrect_msg = "Вы можете использовать `np_baseball[:,0]` для выбора первого столбца из `np_baseball`"),

Ex().check_correct(
    has_printout(0),
    check_function('numpy.mean').has_equal_value()
)

Ex().check_correct(
    has_printout(1),
    check_function('numpy.median').has_equal_value()
)

success_msg("Средний рост 1586 дюймов — звучит неправдоподобно, не так ли? Однако медиана, по всей видимости, не подвержена влиянию выбросов: 74 дюйма выглядит вполне разумно. Всегда полезно проверять как медиану, так и среднее значение, чтобы получить представление об общем распределении всего набора данных.")
```

---

## Исследование данных о бейсболе

```yaml
type: NormalExercise
key: '4409948807'
lang: python
xp: 100
skills:
  - 2
```

Поскольку среднее значение и медиана сильно расходятся, вы решаете пожаловаться в MLB. Там обнаруживают ошибку и присылают вам исправленные данные. Они снова доступны в виде двумерного массива NumPy `np_baseball` с тремя столбцами.

Скрипт Python в редакторе уже содержит код для вывода информационных сообщений с различными сводными статистиками, а библиотека `numpy` уже импортирована как `np`. Доделайте оставшуюся работу! Массив `np_baseball` доступен.

`@instructions`
- Код для вывода среднего значения роста уже включён. Завершите код для вычисления медианного роста.
- Используйте `np.std()` на первом столбце массива `np_baseball`, чтобы вычислить `stddev`.
- Действительно ли крупные игроки tend to весят больше? Используйте `np.corrcoef()`, чтобы сохранить в переменную `corr` коэффициент корреляции между первым и вторым столбцами массива `np_baseball`.

`@hint`
- Используйте `np.median()` для вычисления медианы. Убедитесь, что предварительно выбрали нужный столбец!
- При вычислении стандартного отклонения с помощью `np.std()` выберите тот же столбец.
- Используйте `np_baseball[:, 0]` и `np_baseball[:, 1]` для выбора первого и второго столбцов — они передаются в качестве аргументов в `np.corrcoef()`.

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
msg = "Не изменяйте и не удаляйте предопределённую переменную `avg`."
Ex().check_object("avg", missing_msg=msg).has_equal_value(incorrect_msg=msg)

missing = "Использовали ли вы `np.median()` для вычисления медианы?"
incorrect = "Чтобы вычислить `med`, передайте первый столбец `np_baseball` в `numpy.median()`. Пример с `np.mean()` демонстрирует, как это делается."
Ex().check_correct(
  check_object("med").has_equal_value(),
  check_function("numpy.median", index=0, missing_msg=missing).check_args(0).has_equal_value(incorrect_msg=incorrect)
)

missing = "Использовали ли вы `np.std()` для вычисления стандартного отклонения?"
incorrect = "Чтобы вычислить `stddev`, передайте первый столбец `np_baseball` в `numpy.std()`. Пример с `np.mean()` демонстрирует, как это делается."
Ex().check_correct(
  check_object("stddev").has_equal_value(),
  check_function("numpy.std", index=0, missing_msg=missing).check_args(0).has_equal_value(incorrect_msg=incorrect)
)

missing = "Использовали ли вы `np.corrcoef()` для вычисления корреляции?"
incorrect1 = "Чтобы вычислить `corr`, первым аргументом `np.corrcoef()` должен быть первый столбец `np_baseball`, аналогично тому, как вы делали это ранее."
incorrect2 = "Чтобы вычислить `corr`, вторым аргументом `np.corrcoef()` должен быть второй столбец `np_baseball`. Вместо `[:,0]` используйте на этот раз `[:,1]`."
Ex().check_correct(
  check_object("corr").has_equal_value(),
  check_function("numpy.corrcoef", index=0, missing_msg=missing).multi(
    check_args(0, missing_msg=incorrect1).has_equal_value(incorrect_msg=incorrect1),
    check_args(1, missing_msg=incorrect2).has_equal_value(incorrect_msg=incorrect2)
  )
)

success_msg("Отличная работа! Вы заложили прочную основу — теперь пришло время применить все ваши новые навыки в области науки о данных для решения более сложных задач и достижения значимых результатов.")
```

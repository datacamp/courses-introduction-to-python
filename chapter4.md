---
title_meta: Capítulo 4
title: NumPy
description: >-
  NumPy es un paquete fundamental de Python para trabajar eficientemente en
  ciencia de datos. Aprende a trabajar con potentes herramientas de matrices en
  NumPy para a explorar y manipular datos.
attachments:
  slides_link: 'https://projector-video-pdf-converter.datacamp.com/735/chapter4.pdf'
lessons:
  - nb_of_exercises: 7
    title: Numpy
  - nb_of_exercises: 5
    title: Matrices 2D Numpy
  - nb_of_exercises: 4
    title: 'Numpy:  Estadísticas Básicas'
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

## Tu primer vector NumPy

```yaml
type: NormalExercise
key: 84cab9d170
lang: python
xp: 100
skills:
  - 2
```

En este capítulo, vamos a sumergirnos en el mundo del béisbol. En el camino, nos familiarizaremos con los conceptos básicos de `numpy`, un poderoso paquete para ciencia de datos.

Ya se ha definido una lista `baseball` en el script de Python, que representa la altura de algunos jugadores de béisbol en centímetros. ¿Puedes agregar algún código aquí y allá para crear un vector `numpy` a partir de él?

`@instructions`
- Importa el paquete `numpy` como `np`, para que puedas referirte a `numpy` usando `np`.
- Usa [`np.array()`](http://docs.scipy.org/doc/numpy-1.10.0/glossary.html#term-array) para crear un vector `numpy` de `baseball`. Nombra a este vector `np_baseball`.
- Imprime el tipo de `np_baseball` para comprobar que lo has hecho bien.

`@hint`
- `import numpy as np` es lo que se requiere. Ahora, debes usar `np.fun_name()` siempre que quieras usar una función de `numpy`.
- [`np.array()`](http://docs.scipy.org/doc/numpy-1.10.0/glossary.html#term-array) deberías tomar el argumento `baseball`. Asigna el resultado de la llamada a `np_baseball`.
- Para imprimir el tipo de una variable `x`, simplemente escribe `print(type(x))`.

`@pre_exercise_code`
```{python}
import numpy as np
```

`@sample_code`
```{python}
# Importa el paquete numpy como np


# Crea la lista baseball
baseball = [180, 215, 210, 210, 188, 176, 209, 200]

# Crea un vector numpy con baseball: np_baseball


# Imprime el tipo de np_baseball

```

`@solution`
```{python}
# Importa el paquete numpy como np
import numpy as np

# Crea la lista baseball
baseball = [180, 215, 210, 210, 188, 176, 209, 200]

# Crea un vector NumPy a partir de baseball: np_baseball
np_baseball = np.array(baseball)

# Imprime el tipo de np_baseball
print(type(np_baseball))
```

`@sct`
```{python}
predef_msg = "No tienes que cambiar o eliminar las variables predefinidas."
Ex().has_import("numpy")
Ex().check_correct(
  check_object("np_baseball"),
  multi(
    check_object("baseball", missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
    check_function("numpy.array").check_args(0).has_equal_ast()
  )
)

Ex().has_printout(0)
success_msg("¡Buen trabajo!")
```

---

## Altura de los beisbolistas

```yaml
type: NormalExercise
key: e7e25a89ea
lang: python
xp: 100
skills:
  - 2
```

Eres un gran fanático del béisbol. Decides llamar a la MLB (Major League Baseball) y pedir más estadísticas sobre la altura de los jugadores principales. Te pasan datos sobre más de mil jugadores, que se almacenan como una lista de Python: `height_in`. La altura se expresa en pulgadas. ¿Puedes convertirla en un vector `numpy` y convertir las unidades a metros?

`height_in` ya está disponible y el paquete `numpy` está cargado, por lo que puedes comenzar de inmediato (Fuente: stat.ucla.edu).

`@instructions`
- Crea un vector `numpy` con `height_in`. Nombra este nuevo vector `np_height_in`.
- Imprime `np_height_in`.
- Multiplica `np_height_in` por `0.0254` para convertir todas las medidas de altura de pulgadas a metros. Almacena los nuevos valores en un nuevo vector, `np_height_m`.
- Imprime `np_height_m` y verifica si el resultado tiene sentido.

`@hint`
- Usa [`np.array()`](http://docs.scipy.org/doc/numpy-1.10.0/glossary.html#term-array) y pásale `height`. Almacena el resultado en `np_height_in`.
- Para imprimir una variable `x`, escribe `print(x)` en el script de Python.
- Realiza cálculos como si `np_height_in` fuera un solo número: `np_height_in * conversion_factor` es parte de la respuesta.
- Para imprimir una variable `x`, escribe `print(x)` en el script de Python.

`@pre_exercise_code`
```{python}
import pandas as pd
mlb = pd.read_csv("http://assets.datacamp.com/course/intro_to_python/baseball.csv")
height_in = mlb['Height'].tolist()
import numpy as np
```

`@sample_code`
```{python}
# Importa numpy
import numpy as np

# Crea un vector numpy desde height_in: np_height_in


# Imprime np_height_in


# Convierte np_height_in a m: np_height_m


# Imprime np_height_m

```

`@solution`
```{python}
# Importa numpy
import numpy as np

# Crea un vector numpy desde height_in: np_height_in
np_height_in = np.array(height_in)

# Imprime np_height_in
print(np_height_in)

# Convierte np_height_in a m: np_height_m
np_height_m = np_height_in * 0.0254

# Imprime np_height_m
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
  check_object("np_height_m").has_equal_value(incorrect_msg = "Usa `np_height_in * 0.0254` para calcular `np_height_m`.")
)

success_msg("¡Bien! En un abrir y cerrar de ojos, `numpy` realiza multiplicaciones en más de 1000 medidas de altura.")
```

---

## IMC del beisbolista

```yaml
type: NormalExercise
key: 689fdbc950
lang: python
xp: 100
skills:
  - 2
```

La MLB también te permitirá analizar los datos de peso de los jugadores de béisbol. Una vez más, ambos están disponibles como listas de Python: `height_in` y `weight_lb`. `height_in` está en pulgadas y `weight_lb` está en libras.

Ahora es posible calcular el IMC de cada jugador de béisbol. El código de Python para convertir `height_in` en un vector `numpy` con las unidades correctas ya está disponible en el espacio de trabajo. ¡Sigue las instrucciones paso a paso y termina el juego! `height_in` y `weight_lb` están disponibles como listas.

`@instructions`
- Crea un vector `numpy` a partir de la lista `weight_lb` con las unidades correctas. Multiplica por `0.453592` para pasar de libras a kilogramos. Almacena el vector `numpy` resultante como `np_weight_kg`.
- Usa `np_height_m` y `np_weight_kg` para calcular el IMC de cada jugador. Usa la siguiente ecuación: $$ \mathrm{IMC} = \frac{\mathrm{peso (kg)}}{\mathrm{altura (m)}^2}$$ Guarda el vector `numpy` resultante como `bmi`.
- Imprime `bmi`.

`@hint`
- Usa un enfoque similar al código que calcula `np_height_m`. Esta vez, sin embargo, tienes que trabajar con `weight` y multiplicar por `0.453592`.
- Para calcular el `IMC`, necesitarás los operadores `/` y `**`.
- Para imprimir una variable `x`, escribe `print(x)` en el script.

`@pre_exercise_code`
```{python}
import pandas as pd
mlb = pd.read_csv("http://assets.datacamp.com/course/intro_to_python/baseball.csv")
height_in = mlb['Height'].tolist()
weight_lb = mlb['Weight'].tolist()
import numpy as np
```

`@sample_code`
```{python}
# Importa numpy
import numpy as np

# Crea un vector desde height_in con unidades métricas: np_height_m
np_height_m = np.array(height_in) * 0.0254

# Crea un vector a partir de weight_lb con unidades métricas: np_weight_kg


# Calcular el IMC: bmi


# Imprime bmi

```

`@solution`
```{python}
# Importa numpy
import numpy as np

# Crea un vector desde height_in con unidades métricas: np_height_m
np_height_m = np.array(height_in) * 0.0254

# Crea un vector a partir de weight_lb con unidades métricas: np_weight_kg
np_weight_kg = np.array(weight_lb) * 0.453592

# Calcula el IMC: bmi
bmi = np_weight_kg / np_height_m ** 2

# Imprime bmi
print(bmi)
```

`@sct`
```{python}
Ex().has_import('numpy')

# Chequea np_height_m
msg = "La variable `np_height_m` fue definida para ti. ¡No tienes que cambiarla o eliminarla!"
Ex().check_object("np_height_m", missing_msg=msg).has_equal_value(incorrect_msg = msg)

# Chequea np_weight_kg
Ex().check_correct(
  check_object("np_weight_kg").has_equal_value(),
  multi(
    check_function("numpy.array", index=1).check_args(0).has_equal_ast(),
    has_code('0.453592', not_typed_msg="Asegúrate de multiplicar `np.array(weight_lb)` por `0.453592` para obtener los pesos en kg.")
  )
)

# Chequea bmi
patt = "Necesitas usar `%s` en tu cálculo de `bmi`."
Ex().check_correct(
  has_printout(0),
  check_correct(
    check_object('bmi').has_equal_value(),
    multi(
      has_code('np_weight_kg', not_typed_msg = patt % 'np_weight_kg'),
      has_code('np_height_m', not_typed_msg = patt % 'np_height_m'),
      has_code('**', pattern = False, not_typed_msg = patt % '**')
    )
  )
)

success_msg("¡Genial! ¡Es hora de subir al siguiente nivel!")
```

---

## Beisbolistas peso ligero

```yaml
type: NormalExercise
key: ef6add980e
lang: python
xp: 100
skills:
  - 2
```

Para crear subconjuntos tanto de listas regulares de Python como de matrices y vectores `numpy`, puedes usar corchetes:

```
x = [4 , 9 , 6, 3, 1]
x[1]
import numpy as np
y = np.array(x)
y[1]
```

Para `numpy` específicamente, también puedes usar matrices booleanas `numpy` :

```
high = y > 5
y[high]
```

Ya se incluye el código que calcula el IMC de todos los beisbolistas. ¡Sigue las instrucciones y revela cosas interesantes de los datos! `height_in` y `weight_lb` están disponibles como listas regulares.

`@instructions`
- Crea un vector `numpy` booleano: el elemento del vector debe ser `True` si el IMC del jugador de béisbol correspondiente es inferior a 21. Puedes usar el operador `<` para esto. Nombra el vector `light`.
- Imprime el vector `light`.
- Imprime un vector `numpy` con los IMC de todos los jugadores de béisbol cuyo IMC sea inferior a 21. Usa `light` dentro de los corchetes para hacer una selección del vector `bmi`.

`@hint`
- `bmi> 30` te daría un vector `numpy` booleano en la que los elementos son `True` si el IMC del jugador correspondiente es superior a 30.
- Para imprimir una variable `x`, escribe `print(x)` en el script de Python.
- `bmi[light]` devolverá el vector que necesitas. ¡No olvides envolverlo con una llamada [`print()`](https://docs.python.org/3/library/functions.html#print)!

`@pre_exercise_code`
```{python}
import pandas as pd
mlb = pd.read_csv("http://assets.datacamp.com/course/intro_to_python/baseball.csv")
height_in = mlb['Height'].tolist()
weight_lb = mlb['Weight'].tolist()
import numpy as np
```

`@sample_code`
```{python}
# Importa numpy
import numpy as np

# Calcular el IMC: bmi
np_height_m = np.array(height_in) * 0.0254
np_weight_kg = np.array(weight_lb) * 0.453592
bmi = np_weight_kg / np_height_m ** 2

# Crea el vector light


# Imprime light


# Imprime los IMC de todos los jugadores de béisbol cuyo IMC sea inferior a 21

```

`@solution`
```{python}
# Importa numpy
import numpy as np

# Calcula el IMC: bmi
np_height_m = np.array(height_in) * 0.0254
np_weight_kg = np.array(weight_lb) * 0.453592
bmi = np_weight_kg / np_height_m ** 2

# Crea el vector light
light = bmi < 21

# Imprime light
print(light)

# Imprime los IMC de todos los jugadores de béisbol cuyo IMC sea inferior a 21
print(bmi[light])
```

`@sct`
```{python}
msg = "No es necesario que cambies o elimines las variables predefinidas `np_height_m`, `np_weight_kg`o `bmi`."
Ex().multi(
  check_object("np_height_m", missing_msg=msg).has_equal_value(incorrect_msg = msg),
  check_object("np_weight_kg", missing_msg=msg).has_equal_value(incorrect_msg = msg),
  check_object("bmi", missing_msg=msg).has_equal_value(incorrect_msg = msg)
)

Ex().check_correct(
    multi(
       has_printout(0),
       has_printout(1)
    ),
    check_object("light").has_equal_value(incorrect_msg = "Usa `bmi < 21` para definir `light`")
)

success_msg("Increíble! ¡Parece que solo 11 de los más de 1000 jugadores de béisbol tienen un IMC inferior a 21!")
```

---

## Efectos secundarios de NumPy

```yaml
type: MultipleChoiceExercise
key: 3662ff6637
lang: python
xp: 50
skills:
  - 2
```

Como Hugo explicó previamente, `numpy` es excelente para hacer aritmética vectorial. Sin embargo, si comparas su funcionalidad con las listas regulares de Python, algunas cosas han cambiado.

En primer lugar, las matrices `numpy` no pueden contener elementos con diferentes tipos. Si intentas construir una lista de este tipo, algunos de los tipos de elementos se cambian para tener una lista homogénea. Esto se conoce como _coerción de tipo_.

En segundo lugar, los operadores aritméticos típicos, como `+`, `-`, `*` y `/` tienen un significado diferente para las listas regulares de Python y las matrices y vectores `numpy`.

Echa un vistazo a esta línea de código:

```
np.array([True, 1, 2]) + np.array([3, 4, False])
```

¿Puedes seleccionar el fragmento de código que crea exactamente el mismo objeto en Python? El paquete `numpy` ya está importado como `np`, ¡así que puedes comenzar a experimentar en el IPython Shell de inmediato!

`@possible_answers`
- `np.array([True, 1, 2, 3, 4, False])`
- `np.array([4, 3, 0]) + np.array([0, 2, 2])`
- `np.array([1, 1, 2]) + np.array([3, 4, -1])`
- `np.array([0, 1, 2, 3, 4, 5])`

`@hint`
Copia los diferentes fragmentos de código y pégalos en el IPython Shell. Ve qué resultado coincide con el generado por `np.array([True, 1, 2]) + np.array([3, 4, False])`.

`@pre_exercise_code`
```{python}
import numpy as np
```

`@sct`
```{python}
msg1 = msg3 = msg4 = "Incorrecto. Prueba los diferentes fragmentos de código y ve cuál coincide con el fragmento de código objetivo."
msg2 = "¡Buen trabajo! 'True' se convierte en 1, 'False' se convierte en 0."
Ex().has_chosen(2, [msg1, msg2, msg3, msg4])
```

---

## Subdivisión de vectores NumPy

```yaml
type: NormalExercise
key: fcb2a9007b
lang: python
xp: 100
skills:
  - 2
```

Lo has visto con tus propios ojos: Las listas de Python y las matrices `numpy` a veces se comportan de manera diferente. Por suerte, todavía hay certezas en este mundo. Por ejemplo, la creación de subconjuntos (usando la notación de corchetes en listas o matrices y vectores) funciona exactamente igual. Para ver esto por ti mismo, prueba las siguientes líneas de código en el IPython Shell:

```
x = ["a", "b", "c"]
x[1]

np_x = np.array(x)
np_x[1]
```

El script en el editor ya contiene código que importa `numpy` como `np`y almacena tanto la altura como el peso de los jugadores de la MLB como vectores `numpy`. `height_in` y `weight_lb` están disponibles como listas regulares.

`@instructions`
- Subdivide `np_weight_lb` imprimiendo el elemento en el índice 50.
- Imprime un sub vector de `np_height_in` que contenga los elementos en el índice 100 hasta el índice 110 ** incluidos**.

`@hint`
- Asegúrate de envolver una llamada [`print()`](https://docs.python.org/3/library/functions.html#print) alrededor de las operaciones de creación de subconjuntos.
- Usa `[100:111]` para obtener los elementos desde el índice 100 hasta el índice 110 incluidos.

`@pre_exercise_code`
```{python}
import pandas as pd
mlb = pd.read_csv("http://assets.datacamp.com/course/intro_to_python/baseball.csv")
height_in = mlb['Height'].tolist()
weight_lb = mlb['Weight'].tolist()
```

`@sample_code`
```{python}
# Importa numpy
import numpy as np

# Almacena las listas weight y height como vectores numpy
np_weight_lb = np.array(weight_lb)
np_height_in = np.array(height_in)

# Imprime el índice 50 de np_weight_lb


# Imprime el sub vector de np_height_in: desde el índice 100 hasta el índice 110 incluidos

```

`@solution`
```{python}
# Importa numpy
import numpy as np

# Almacena las listas weight y height como vectores numpy
np_weight_lb = np.array(weight_lb)
np_height_in = np.array(height_in)

# Imprime el índice 50 de np_weight_lb
print(np_weight_lb[50])

# Imprime el sub vector de np_height_in: desde el índice 100 hasta el índice 110 incluidos
print(np_height_in[100:111])
```

`@sct`
```{python}
Ex().has_import("numpy", same_as=False)
msg = "No tienes que cambiar o eliminar las variables predefinidas."
Ex().multi(
    check_object("np_height_in", missing_msg=msg).has_equal_value(incorrect_msg = msg),
    check_object("np_weight_lb", missing_msg=msg).has_equal_value(incorrect_msg = msg)
)

Ex().has_printout(0)
Ex().has_printout(1)

success_msg("¡Bien! Es hora de aprender algo nuevo: ¡matrices 2D en NumPy!")
```

---

## Matrices 2D Numpy

```yaml
type: VideoExercise
key: 1241efac7a
xp: 50
```

`@projector_key`
ae3238dcc7feb9adecfee0c395fc8dc8

---

## Tu primer matriz 2D en NumPy

```yaml
type: NormalExercise
key: 5cb045bb13
lang: python
xp: 100
skills:
  - 2
```

Antes de trabajar con los datos reales de MLB, intentemos crear una matriz `numpy` 2D a partir de una pequeña lista de listas.

En este ejercicio, `baseball` es una lista de listas. La lista principal contiene 4 elementos. Cada uno de estos elementos es una lista que contiene la altura y el peso de 4 jugadores de béisbol, en ese orden. `baseball` ya está codificado para ti en el guión.

`@instructions`
- Usa [`np.array()`](http://docs.scipy.org/doc/numpy-1.10.0/glossary.html#term-array) para crear una matriz `numpy` 2D de `baseball`. Llamala `np_baseball`.
- Imprime el tipo de `np_baseball`.
- Imprime el atributo `shape` de `np_baseball`. Usa `np_baseball.shape`.

`@hint`
- `baseball` ya está codificado para ti en el script. Llama a [`np.array()`](http://docs.scipy.org/doc/numpy-1.10.0/glossary.html#term-array) y almacena la matriz `numpy` 2D resultante en `np_baseball`.
- Usa [`print()`](https://docs.python.org/3/library/functions.html#print) en combinación con [`type()`](https://docs.python.org/3/library/functions.html#type) para la segunda instrucción.
- `np_baseball.shape` te dará las dimensiones del `np_baseball`. Asegúrate de envolver una llamada a [`print()`](https://docs.python.org/3/library/functions.html#print) a su alrededor.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Importa numpy
import numpy as np

# Crea baseball, una lista de listas
baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

# Crea una matriz numpy 2D de baseball: np_baseball


# Imprime el tipo de np_baseball


# Imprime el atributo shape de np_baseball

```

`@solution`
```{python}
# Importa numpy
import numpy as np

# Crea baseball, una lista de listas
baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

# Crea una matriz numpy 2D de baseball: np_baseball
np_baseball = np.array(baseball)

# Imprime el tipo de np_baseball
print(type(np_baseball))

# Imprime el atributo shape de np_baseball
print(np_baseball.shape)
```

`@sct`
```{python}
msg = "No tienes que cambiar o eliminar las variables predefinidas."
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

success_msg("¡Buen trabajo! ¡Ya estás listo para convertir los datos reales de MLB en una matriz `numpy` 2D!")
```

---

## Datos de béisbol en formato 2D

```yaml
type: NormalExercise
key: 5df25d0b7b
lang: python
xp: 100
skills:
  - 2
```

Echa otro vistazo a los datos de MLB y te darás cuenta de que tiene más sentido reestructurar toda esta información en una matriz `numpy` 2D. Esta matriz debe tener 1015 filas, correspondientes a los 1015 jugadores de béisbol sobre los que se tiene información, y 2 columnas (para altura y peso).

La MLB fue, nuevamente, muy útil y te pasó los datos en una estructura diferente, una lista de listas de Python. En esta lista de listas, cada sublista representa la altura y el peso de un solo jugador de béisbol. El nombre de esta lista de listas es `baseball`.

¿Puedes almacenar los datos como una matriz 2D para aprovechar la funcionalidad adicional de `numpy`? `baseball` está disponible como una lista de listas regular.

`@instructions`
- Usa [`np.array()`](http://docs.scipy.org/doc/numpy-1.10.0/glossary.html#term-array) para crear una matriz `numpy` 2D de `baseball`. Llamala `np_baseball`.
- Imprime el atributo `shape` de `np_baseball`.

`@hint`
- `baseball` ya está disponible en el entorno de Python. Llama a [`np.array()`](http://docs.scipy.org/doc/numpy-1.10.0/glossary.html#term-array) y almacena la matriz `numpy` 2D resultante en `np_baseball`.
- `np_baseball.shape` nos dará las dimensiones de `np_baseball`. Asegúrate de envolver una llamada a [`print()`](https://docs.python.org/3/library/functions.html#print) a su alrededor.

`@pre_exercise_code`
```{python}
import pandas as pd
baseball = pd.read_csv("http://assets.datacamp.com/course/intro_to_python/baseball.csv")[['Height', 'Weight']].to_numpy().tolist()
import numpy as np
```

`@sample_code`
```{python}
# Importa el paquete numpy
import numpy as np

# Crea una matriz numpy 2D de baseball: np_baseball


# Imprime el atributo shape de np_baseball

```

`@solution`
```{python}
# Importa el paquete numpy
import numpy as np

# Crea una matriz numpy 2D de baseball: np_baseball
np_baseball = np.array(baseball)

# Imprime el atributo shape de np_baseball
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

success_msg("¡Eso! ¡Es hora de explorar algunas características increíbles de las matrices `numpy` multidimensionales!")
```

---

## Subdivisión de matrices NumPy 2D

```yaml
type: NormalExercise
key: aeca4977f0
lang: python
xp: 100
skills:
  - 2
```

Si tu matriz `numpy` 2D tiene una estructura regular, es decir, cada fila y columna tiene un número fijo de valores, subdividir se vuelve muy fácil. Echa un vistazo al código a continuación donde los elementos `"a"` y `"c"` se extraen de una lista de listas.

```
# lista de listas regular
x = [["a", "b"], ["c", "d"]]
[x[0][0], x[1][0]]

# numpy
import numpy as np
np_x = np.array(x)
np_x[:, 0]
```

Para las listas regulares de Python, esto es un verdadero dolor de cabeza. Sin embargo, para las matrices `numpy` 2D, ¡es bastante intuitivo! Los índices antes de la coma se refieren a las filas, mientras que los que están después de la coma se refieren a las columnas. El `:` es para rebanar; en este ejemplo, le dice a Python que incluya todas las filas.

El código que convierte la lista `baseball` precargada en una matriz `numpy` 2D ya está en el script. La primera columna contiene la altura de los jugadores en pulgadas y la segunda columna contiene el peso de los jugadores en libras. Agrega algunas líneas para hacer las selecciones correctas. ¡Recuerda que en Python, el primer elemento está en el índice 0! `baseball` está disponible como una lista de listas regular.

`@instructions`
- Imprime la fila 50 de `np_baseball`.
- Crea una nueva variable, `np_weight_lb`, que contenga toda la segunda columna de `np_baseball`.
- Selecciona la altura (primera columna) del jugador de béisbol número 124 en `np_baseball` e imprímela.

`@hint`
- ¡Necesita el índice de fila 49 en la primera instrucción! Más específicamente, debes usar `[49,:]`.
- Para seleccionar toda la segunda columna, usa `[:, 1]`.
- Para la última instrucción, usa `[123, 0]`; no olvides envolverlo todo dentro de [`print()`](https://docs.python.org/3/library/functions.html#print).

`@pre_exercise_code`
```{python}
import pandas as pd
baseball = pd.read_csv("http://assets.datacamp.com/course/intro_to_python/baseball.csv")[['Height', 'Weight']].to_numpy().tolist()
import numpy as np
```

`@sample_code`
```{python}
# Importa el paquete numpy
import numpy as np

# Crea np_baseball (2 columnas)
np_baseball = np.array(baseball)

# Imprime la fila 50 de np_baseball


# Selecciona toda la segunda columna de np_baseball: np_weight_lb


# Imprime la altura del jugador 124

```

`@solution`
```{python}
# Importa el paquete numpy
import numpy as np

# Crea np_baseball (2 columnas)
np_baseball = np.array(baseball)

# Imprime la fila 50 de np_baseball
print(np_baseball[49,:])

# Selecciona toda la segunda columna de np_baseball: np_weight_lb
np_weight_lb = np_baseball[:,1]

# Imprime la altura del jugador 124
print(np_baseball[123, 0])
```

`@sct`
```{python}
msg = "No tienes que cambiar o eliminar las variables predefinidas."
Ex().multi(
    has_import("numpy", same_as = False),
    check_object("np_baseball", missing_msg=msg).has_equal_value(incorrect_msg = msg)
)

Ex().has_printout(0)

Ex().check_object('np_weight_lb').has_equal_value(incorrect_msg = "Puedes usar `np_baseball[:,1]` para definir `np_weight_lb`. Esto seleccionará toda la primera columna.")

Ex().has_printout(1)

success_msg("¡Vamos bien!")
```

---

## Aritmética 2D

```yaml
type: NormalExercise
key: 1c2378b677
lang: python
xp: 100
skills:
  - 2
```

¿Recuerdas cómo calculaste el índice de masa corporal para todos los jugadores de béisbol? `numpy` pudo realizar todos los cálculos al nivel elemento (es decir, elemento por elemento). ¡Para matrices `numpy` 2D no es diferente! Puedes combinar matrices con números, con vectores y con otras matrices.

Ejecuta el siguiente código en el shell de IPython y ve si queda claro:

```
import numpy as np
np_mat = np.array([[1, 2],
                   [3, 4],
                   [5, 6]])
np_mat * 2
np_mat + np.array([10, 10])
np_mat + np_mat
```

`np_baseball` está codificado para ti; es nuevamente una matriz `numpy` 2D con 3 columnas que representan la altura (en pulgadas), el peso (en libras) y la edad (en años). `baseball` está disponible como una lista de listas regular y `updated` está disponible como matriz numpy 2D.

`@instructions`
- Conseguiste los cambios de altura, peso y edad de todos los beisbolistas. Está disponible como una matriz `numpy` 2D, `updated`. Suma `np_baseball` y `updated` e imprime el resultado.
- Convierte las unidades de altura y peso a métricas (metros y kilogramos, respectivamente). Como primer paso, crea una matriz `numpy` con tres valores: `0.0254`, `0.453592` y `1`. Usa el nombre `conversion` para esta matriz.
- Multiplica `np_baseball` por `conversion` e imprime el resultado.

`@hint`
- `np_baseball + actualizado` hará una suma de elementos de las dos matrices `numpy`.
- Crea una matriz `numpy` con [`np.array()`](http://docs.scipy.org/doc/numpy-1.10.0/glossary.html#term-array); la entrada es una lista normal de Python con tres elementos.
- `np_baseball * conversion` funcionará.  ¡Pruébalo! Asegúrate de envolverlo en una llamada a [`print()`](https://docs.python.org/3/library/functions.html#print) .

`@pre_exercise_code`
```{python}
import pandas as pd
import numpy as np
baseball = pd.read_csv("http://assets.datacamp.com/course/intro_to_python/baseball.csv")[['Height', 'Weight', 'Age']].to_numpy().tolist()
n = len(baseball)
updated = np.array(pd.read_csv("http://assets.datacamp.com/course/intro_to_python/update.csv", header = None))
import numpy as np
```

`@sample_code`
```{python}
# Importa el paquete numpy
import numpy as np

# Crea np_baseball (3 columnas)
np_baseball = np.array(baseball)

# Imprime la suma de np_baseball y updated


# Crea una matriz numpy: conversion


# Imprime el producto de np_baseball y conversion

```

`@solution`
```{python}
# Importa el paquete numpy
import numpy as np

# Crea np_baseball (3 columnas)
np_baseball = np.array(baseball)

# Imprime la suma de np_baseball y updated
print(np_baseball + updated)

# Crea una matriz numpy: conversion
conversion = np.array([0.0254, 0.453592, 1])

# Imprime el producto de np_baseball y conversion
print(np_baseball * conversion)
```

`@sct`
```{python}
Ex().has_import("numpy")

msg = "No tienes que cambiar o eliminar las variables predefinidas."
Ex().check_object("np_baseball", missing_msg=msg).has_equal_value(incorrect_msg = msg)

Ex().has_printout(0)

Ex().check_correct(
    has_printout(1),
    check_correct(
        check_object('conversion').has_equal_value(),
        check_function('numpy.array', index = 1).check_args(0).has_equal_value()
    )    
)

success_msg("¡Buen trabajo! Observa cómo con muy poco código, puedes cambiar todos los valores en su estructura de datos `numpy` de una manera muy específica. ¡Esto será muy útil en tu futuro como científico de datos!")
```

---

## NumPy:  Estadísticas Básicas

```yaml
type: VideoExercise
key: 287995e488
xp: 50
```

`@projector_key`
34495ba457d74296794d2a122c9b6e19

---

## Promedio versus mediana

```yaml
type: NormalExercise
key: 509c588eb6
lang: python
xp: 100
skills:
  - 2
```

Ahora sabes cómo usar funciones `numpy` para tener una mejor visión de tus datos. Básicamente se trata de importar `numpy` y luego llamar a varias funciones simples en las matrices `numpy`:

```
import numpy as np
x = [1, 4, 8, 10, 12]
np.mean(x)
np.median(x)
```

Los datos de béisbol están disponibles como una matriz `numpy` 2D con 3 columnas (altura, peso, edad) y 1015 filas. El nombre de esta matriz `numpy` es `np_baseball`. Sin embargo, después de reestructurar los datos, observas que algunos valores de altura son anormalmente altos. Sigue las instrucciones y descubre qué estadística de resumen es la más adecuada si se trata de los denominados _valores atípicos_. `np_baseball` está disponible.

`@instructions`
- Crea una matriz `numpy` `np_height_in` que sea igual a la primera columna de `np_baseball`.
- Imprime la media de `np_height_in`.
- Imprime la mediana de `np_height_in`.

`@hint`
- Usar subconjuntos `numpy` 2D: `[:,0]` es parte de la solución.
- Si `numpy` se importa como `np`, puedes usar [`np.mean()`](http://docs.scipy.org/doc/numpy-1.10.0/reference/generated/numpy.mean.html) para obtener la media de una matriz NumPy. No olvides incluir la función [`print()`](https://docs.python.org/3/library/functions.html#print).
- Para la última instrucción, usa [`np.median()`](http://docs.scipy.org/doc/numpy-1.10.0/reference/generated/numpy.median.html).

`@pre_exercise_code`
```{python}
import pandas as pd
np_baseball = pd.read_csv("http://assets.datacamp.com/course/intro_to_python/baseball.csv")[['Height', 'Weight', 'Age']].to_numpy()
np_baseball[slice(0, 1015, 50), 0] = np_baseball[slice(0, 1015, 50), 0]*1000
import numpy as np
```

`@sample_code`
```{python}
# Importa numpy
import numpy as np

# Crea np_height_in usando np_baseball


# Imprime la media de np_height_in


# Imprime la mediana de np_height_in

```

`@solution`
```{python}
# Importa numpy
import numpy as np

# Crea np_height_in usando np_baseball
np_height_in = np_baseball[:,0]

# Imprime la media de np_height_in
print(np.mean(np_height_in))

# Imprime la mediana de np_height_in
print(np.median(np_height_in))
```

`@sct`
```{python}
Ex().has_import("numpy", same_as = False)

Ex().check_object("np_height_in").has_equal_value(incorrect_msg = "Puedes usar `np_baseball[:,0]` para seleccionar la primera columna de `np_baseball`"),

Ex().check_correct(
    has_printout(0),
    check_function('numpy.mean').has_equal_value()
)

Ex().check_correct(
    has_printout(1),
    check_function('numpy.median').has_equal_value()
)

success_msg("Una altura promedio de 1586 pulgadas, eso no suena correcto, ¿verdad? Sin embargo, la mediana no parece afectada por los valores atípicos: 74 pulgadas tiene mucho sentido. Siempre es una buena idea verificar tanto la mediana como la media, para tener una idea de la distribución general del set de datos.")
```

---

## Explora los datos de béisbol

```yaml
type: NormalExercise
key: '4409948807'
lang: python
xp: 100
skills:
  - 2
```

Debido a que la media y la mediana están tan alejadas, decides presentar una queja ante la MLB. Encuentran el error y te envían los datos corregidos. Están nuevamente disponibles como una matriz 2D NumPy `np_baseball`, con tres columnas.

El script de Python en el editor ya incluye código para imprimir mensajes informativos con las diferentes estadísticas de resumen. ¿Puedes terminar el trabajo? `np_baseball` está disponible.

`@instructions`
- El código para imprimir la altura media ya está incluido. Completa el código para la altura mediana. Reemplaza `None` con el código correcto.
- Usa [`np.std()`](http://docs.scipy.org/doc/numpy-1.10.0/reference/generated/numpy.std.html) en la primera columna de `np_baseball` para calcular `stddev`. Reemplaza `None` con el código correcto.
- ¿Los jugadores altos tienden a ser más pesados? Usa [`np.corrcoef()`](http://docs.scipy.org/doc/numpy-1.10.0/reference/generated/numpy.corrcoef.html) para almacenar la correlación entre la primera y la segunda columnas de `np_baseball` en `corr`. Reemplaza `None` con el código correcto.

`@hint`
- Utiliza [`np.median()`](http://docs.scipy.org/doc/numpy-1.10.0/reference/generated/numpy.median.html) para calcular la mediana. ¡Asegúrate de seleccionar la columna correcta!
- Usa de la misma columna al calcular la desviación estándar con [`np.std()`](http://docs.scipy.org/doc/numpy-1.10.0/reference/generated/numpy.std.html).
- Utiliza `np_baseball[:, 0]` y `np_baseball[:, 1]` para seleccionar la primera y la segunda columnas; estas son los argumentos de [`np.corrcoef()`](http://docs.scipy.org/doc/numpy-1.10.0/reference/generated/numpy.corrcoef.html).

`@pre_exercise_code`
```{python}
import pandas as pd
np_baseball = pd.read_csv("http://assets.datacamp.com/course/intro_to_python/baseball.csv")[['Height', 'Weight', 'Age']].to_numpy()
import numpy as np
```

`@sample_code`
```{python}
# Importa numpy
import numpy as np

# Imprime la altura media (primera columna)
avg = np.mean(np_baseball[:,0])
print("Average: " + str(avg))

# Imprime altura mediana. Reemplaza 'None'
med = None
print("Median: " + str(med))

# Imprime la desviación estándar de la altura. Reemplaza 'None'
stddev = None
print("Standard Deviation: " + str(stddev))

# Imprime la correlación entre la primera y la segunda columnas. Reemplaza 'None'
corr = None
print("Correlation: " + str(corr))
```

`@solution`
```{python}
# Import numpy
import numpy as np

# Imprime la altura media (primera columna)
avg = np.mean(np_baseball[:,0])
print("Average: " + str(avg))

# Imprime altura mediana. Reemplaza 'None'
med = np.median(np_baseball[:,0])
print("Median: " + str(med))

# Imprime la desviación estándar de la altura. Reemplaza 'None'
stddev = np.std(np_baseball[:,0])
print("Standard Deviation: " + str(stddev))

# Imprime la correlación entre la primera y la segunda columnas. Reemplaza 'None'
corr = np.corrcoef(np_baseball[:,0], np_baseball[:,1])
print("Correlation: " + str(corr))
```

`@sct`
```{python}
Ex().has_import("numpy")

msg = "No debes cambiar ni eliminar la variable `avg` predefinida."
Ex().check_object("avg", missing_msg=msg).has_equal_value(incorrect_msg=msg)

missing = "¿Has usado `np.median()` para calcular la mediana?"
incorrect = "Para calcular `med`, pasa la primera columna de `np_baseball` a `numpy.median()`. El ejemplo de `np.mean()` muestra cómo se hace."
Ex().check_correct(
  check_object("med").has_equal_value(),
  check_function("numpy.median", index=0,missing_msg=missing).check_args(0).has_equal_value(incorrect_msg=incorrect)
)

missing = "¿Has utilizado `np.std()` para calcular la desviación estándar?"
incorrect = "Para calcular `stddev`, pasa la primera columna de `np_baseball` a `numpy.std()`. El ejemplo de `np.mean()` muestra cómo se hace."
Ex().check_correct(
  check_object("stddev").has_equal_value(),
  check_function("numpy.std", index=0,missing_msg=missing).check_args(0).has_equal_value(incorrect_msg=incorrect)
)

missing = "¿Has utilizado `np.corrcoef()` para calcular la correlación?"
incorrect1 = "Para calcular `corr`, el primer argumento de `np.corrcoef()` debe ser la primera columna de `np_baseball`, similar a como se hizo antes."
incorrect2 = "Para calcular `corr`, el segundo argumento de `np.corrcoef()` debe ser la segunda columna de `np_baseball`. En lugar de `[:,0]`, usa `[:,1]`"
Ex().check_correct(
  check_object("corr").has_equal_value(),
  check_function("numpy.corrcoef", index=0, missing_msg=missing).multi(
    check_args(0, missing_msg=incorrect1).has_equal_value(incorrect_msg=incorrect1),
    check_args(1, missing_msg=incorrect2).has_equal_value(incorrect_msg=incorrect2)
  )
)

success_msg("¡Buen trabajo! ¡Es hora de usar todas tus nuevas habilidades de ciencia de datos en el último ejercicio!")
```

---

## Juntemos todo

```yaml
type: NormalExercise
key: e125cad8a5
lang: python
xp: 100
skills:
  - 2
```

En los últimos ejercicios hemos visto todo lo que hay que saber sobre la altura y el peso de los jugadores de béisbol. Ahora es el momento de sumergirse en otro deporte: el fútbol.

Te has puesto en contacto con la FIFA y te han pasado dos listas. Las listas son las siguientes:
```
positions = ['GK', 'M', 'A', 'D', ...]
heights = [191, 184, 185, 180, ...]
```
Cada elemento de las listas corresponde a un jugador. La primera lista, `positions`, contiene cadenas que representan la posición de cada jugador. Las posiciones son: `'GK'` (portero), `'M'` (medio), `'A'` (delantero) y `'D'` (defensa). La segunda lista, `heights`, contiene números enteros que representan la altura del jugador en cm. El primer jugador de las listas es portero y es bastante alto (191 cm).

Estás bastante seguro de que la altura media de los porteros es más alta que la de otros jugadores en el campo de fútbol. Algunos de tus amigos no te creen, por lo que estás decidido a mostrárselos usando los datos que recibiste de FIFA y tus habilidades de Python recién adquiridas. `heights` y `positions` están disponibles como listas.

`@instructions`
- Convierte `heights` y `positions`, que son listas regulares, en matrices numpy. Llámalas `np_heights` y `np_positions`.
- Extrae todas las alturas de los porteros. Puedes usar un pequeño truco aquí: usa `np_positions == 'GK'` como índice para `np_heights`. Asigna el resultado a `gk_heights`.
- Extrae todas las alturas de todos los demás jugadores. Esta vez usa `np_positions != 'GK'` como índice para `np_heights`. Asigna el resultado a `other_heights`.
- Imprime la altura mediana de los porteros usando [`np.median()`](http://docs.scipy.org/doc/numpy-1.10.0/reference/generated/numpy.median.html). Reemplaza `None` con el código correcto.
- Haz lo mismo con los demás jugadores. Imprime su altura mediana. Reemplaza `None` con el código correcto.

`@hint`
- Usa [`np.array()`](http://docs.scipy.org/doc/numpy-1.10.0/glossary.html#term-array) para convertir las listas en matrices numpy.
- Usa `np_heights[np_positions == 'GK']` para extraer las alturas de todos los porteros. No olvides asignar el resultado a `gk_heights`.
- Usa `np_heights[np_positions != 'GK']` para extraer las alturas de todos los demás jugadores. No olvides asignar el resultado a `other_heights`.
- Imprime la altura mediana de los porteros usando `np.median(gk_heights)`.
- Imprime la altura mediana de los otros jugadores usando `np.median(other_heights)`.

`@pre_exercise_code`
```{python}
import pandas as pd
fifa =  pd.read_csv("http://assets.datacamp.com/course/intro_to_python/fifa.csv", skipinitialspace=True, usecols=['position', 'height'])
positions = list(fifa.position)
heights = list(fifa.height)
```

`@sample_code`
```{python}
# Import numpy
import numpy as np

# Convierte positions y heights en matrices numpy: np_positions, np_heights



# Alturas de los porteros: gk_heights


# Alturas de los otros jugadores: other_heights


# Imprime la altura mediana de los porteros. Reemplaza 'None'
print("Median height of goalkeepers: " + str(None))

# Imprime la altura mediana de los otros jugadores. Reemplaza 'None'
print("Median height of other players: " + str(None))
```

`@solution`
```{python}
# Importa numpy
import numpy as np

# Convierte positions y heights en matrices numpy: np_positions, np_heights
np_positions = np.array(positions)
np_heights = np.array(heights)

# Alturas de los porteros: gk_heights
gk_heights = np_heights[np_positions == 'GK']

# Alturas de los otros jugadores: other_heights
other_heights = np_heights[np_positions != 'GK']

# Imprime la altura mediana de los porteros. Reemplaza 'None'
print("Median height of goalkeepers: " + str(np.median(gk_heights)))

# Imprime la altura mediana de los otros jugadores. Reemplaza 'None'
print("Median height of other players: " + str(np.median(other_heights)))
```

`@sct`
```{python}
Ex().has_import("numpy")

msg_gk_heights = "Puedes usar `[np_positions == 'GK']` como índice de `np_heights` para encontrar las alturas de todos los porteros, `gk_heights`."
msg_other_heights = "Puedes usar `[np_positions != 'GK']` como un índice de `np_heights` para encontrar las alturas de todos los demás jugadores, `other_heights`."

Ex().check_correct(
    multi(
        has_printout(0),
        has_printout(1)
    ),
    multi(
        check_correct(
            multi(
                check_object('gk_heights').has_equal_value(incorrect_msg=msg_gk_heights),
                check_object('other_heights').has_equal_value(incorrect_msg=msg_other_heights)
            ),
            multi(
                check_correct(
                    check_object("np_positions").has_equal_value(incorrect_msg="Asigna la versión de la matriz numpy de `positions` a `np_positions`."),
                    check_function('numpy.array', index=0).check_args(0).has_equal_ast()
                ),
                check_correct(
                    check_object("np_heights").has_equal_value(incorrect_msg="Asigna la versión de matriz numpy de `heights` a `np_heights`."),
                    check_function('numpy.array', index=1).check_args(0).has_equal_ast()
                )
            )
        ),
        check_function('str', index=0),
        check_function('numpy.median', index=0),
        check_function('str', index=1),
        check_function('numpy.median', index=1)
    )
)

success_msg("¡Maravilloso! ¡Tenías razón y los incrédulos estaban equivocados! Este ejercicio marca el final del curso Introducción a Python para ciencia de datos. ¡Nos vemos en otro curso!")
```

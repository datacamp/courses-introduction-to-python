---
title_meta: Capítulo 4
title: NumPy
description: >-
  NumPy es un paquete de Python fundamental para practicar con eficiencia la
  ciencia de datos. Aprende a trabajar con las potentes herramientas de la
  matriz NumPy e iníciate en la exploración de datos.
attachments:
  slides_link: 'https://projector-video-pdf-converter.datacamp.com/735/chapter4.pdf'
lessons:
  - nb_of_exercises: 5
    title: Numpy
  - nb_of_exercises: 5
    title: Matrices de Numpy 2D
  - nb_of_exercises: 3
    title: 'Numpy: estadística básica'
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

## Tu primera matriz de NumPy

```yaml
type: NormalExercise
key: 84cab9d170
lang: python
xp: 100
skills:
  - 2
```

Ahora vas a adentrarte en el mundo del béisbol. Por el camino, te irás familiarizando con los conceptos básicos de `numpy`, un paquete potentísimo para hacer ciencia de datos.

En el script de Python ya tienes definida una lista llamada `baseball` que representa la altura en centímetros de varios jugadores. ¿Podrías añadir el código necesario para crear un array de `numpy` a partir de ella?

`@instructions`
- Importa el paquete `numpy` como `np`, para que puedas referirte a `numpy` con `np`.
- Usa `np.array()` para crear un array de `numpy` a partir de `baseball`. Nombra este array `np_baseball`.
- Muestra por pantalla el tipo de `np_baseball` para comprobar que lo has hecho correctamente.

`@hint`
- Con `import numpy as np` será suficiente. A partir de ahora, tendrás que usar `np.fun_name()` cada vez que quieras utilizar una función de `numpy`.
- La función `np.array()` debe recibir `baseball` como argumento de entrada. Asigna el resultado de esta llamada a la variable `np_baseball`.
- Para mostrar por pantalla el tipo de una variable `x`, simplemente escribe `print(type(x))`.

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
predef_msg = "No tienes que cambiar ni eliminar las variables predefinidas."
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

## Altura de los jugadores de béisbol

```yaml
type: NormalExercise
key: e7e25a89ea
lang: python
xp: 100
skills:
  - 2
```

Eres un gran aficionado al béisbol. Decides llamar a la MLB (Major League Baseball) y pedir más estadísticas sobre la altura de los jugadores principales. Te facilitan datos de más de mil jugadores, que se almacenan como una lista normal de Python: `height_in`. La altura se expresa en pulgadas. ¿Puedes crear un array `numpy` a partir de ella y convertir las unidades a metros?

`height_in` ya está disponible y el paquete `numpy` está cargado, así que puedes empezar de inmediato (Fuente: stat.ucla.edu).

`@instructions`
- Crea un array `numpy` a partir de `height_in`. Nombra este nuevo array `np_height_in`.
- Muestra `np_height_in` por pantalla.
- Multiplica `np_height_in` por `0.0254` para convertir todas las medidas de altura de pulgadas a metros. Guarda los nuevos valores en un nuevo array, `np_height_m`.
- Muestra `np_height_m` por pantalla y comprueba si el resultado tiene sentido.

`@hint`
- Utiliza `np.array()` pasándole `height`. Guarda el resultado en `np_height_in`.
- Para mostrar una variable `x` por pantalla, escribe `print(x)` en el script de Python.
- Realiza los cálculos como si `np_height_in` fuera un único número: parte de la respuesta consiste en hacer `np_height_in * conversion_factor`.
- Para mostrar una variable `x` por pantalla, escribe `print(x)` en el script de Python.

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
  check_object("np_height_m").has_equal_value(incorrect_msg = "Usa `np_height_in * 0.0254` para calcular `np_height_m`.")
)

success_msg("¡Bien hecho! En un abrir y cerrar de ojos, `numpy` realiza multiplicaciones en más de 1000 mediciones de altura.")
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

`numpy` es fantástico para realizar aritmética de vectores. Sin embargo, si comparas su funcionalidad con la de las listas normales de Python, hay algunas diferencias.

En primer lugar, los arrays de `numpy` no pueden contener elementos de diferentes tipos. Si mezclas tipos, como booleanos y enteros, `numpy` los convierte automáticamente a un tipo común. Los booleanos como `True` y `False` se tratan como `1` y `0` cuando se combinan con números, por lo que el array termina siendo de enteros.

En segundo lugar, los operadores aritméticos típicos, como `+`, `-`, `*` y `/` tienen un significado diferente para las listas normales de Python y para los arrays de `numpy`.

Selecciona el código que dé el siguiente resultado:

```
np.array([True, 1, 2]) + np.array([3, 4, False])
```

El paquete `numpy` ya está importado como `np`. Puedes ejecutar cada opción en el shell IPython para ver el resultado.

`@possible_answers`
- `np.array([True, 1, 2, 3, 4, False])`
- `np.array([4, 3, 0]) + np.array([0, 2, 2])`
- `np.array([1, 1, 2]) + np.array([3, 4, -1])`
- `np.array([0, 1, 2, 3, 4, 5])`

`@hint`
- Copia los distintos fragmentos de código y pégalos en el shell de IPython. Pulsa **Intro** para ejecutar el código ver qué resultado coincide con el generado por `np.array([True, 1, 2]) + np.array([3, 4, False])`.

`@pre_exercise_code`
```{python}
import numpy as np
```

`@sct`
```{python}
msg1 = msg3 = msg4 = "Incorrecto. Prueba los diferentes fragmentos de código y mira cuál coincide con el fragmento de código objetivo."
msg2 = "¡Buen trabajo! `True` se convierte en 1, `False` se convierte en 0."
Ex().has_chosen(2, [msg1, msg2, msg3, msg4])
```

---

## Crear subconjuntos de matrices de NumPy

```yaml
type: NormalExercise
key: fcb2a9007b
lang: python
xp: 100
skills:
  - 2
```

La indexación (es decir, el uso de los corchetes en listas o arrays) funciona exactamente de la misma manera tanto en las listas como en los arrays.

Este ejercicio ya tiene cargadas de fondo dos listas: `height_in` y `weight_lb`. Estas contienen la altura y el peso de los jugadores de la MLB en forma de listas normales y corrientes. También tienes a tu disposición dos arrays de `numpy`: `np_weight_lb` y `np_height_in`.

`@instructions`
- Indexa `np_weight_lb` mostrando por pantalla el elemento que está en el índice 50.
- Muestra por pantalla un subconjunto de `np_height_in` que contenga los elementos desde el índice 100 hasta el índice 110, **este último incluido**.

`@hint`
- Asegúrate de introducir tus operaciones de indexación dentro de una llamada a `print()`.
- Utiliza `[100:111]` para obtener los elementos desde el índice 100 hasta el índice 110 (este último incluido).

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
msg = "No tienes que cambiar ni eliminar las variables predefinidas."
Ex().multi(
    check_object("np_height_in", missing_msg=msg).has_equal_value(incorrect_msg=msg),
    check_object("np_weight_lb", missing_msg=msg).has_equal_value(incorrect_msg=msg)
)

Ex().has_printout(0)
Ex().has_printout(1)

success_msg("¡Bien hecho! Es hora de aprender algo nuevo: ¡matrices 2D de NumPy!")
```

---

## Matrices de NumPy 2D

```yaml
type: VideoExercise
key: 1241efac7a
xp: 50
```

`@projector_key`
ae3238dcc7feb9adecfee0c395fc8dc8

---

## Tu primera matriz de NumPy 2D

```yaml
type: NormalExercise
key: 5cb045bb13
lang: python
xp: 100
skills:
  - 2
```

Antes de trabajar con los datos reales de la MLB, vamos a intentar crear un array `numpy` 2D a partir de una pequeña lista de listas.

En este ejercicio, `baseball` es una lista de listas. La lista principal contiene 4 elementos. Cada uno de estos elementos es una lista que contiene la altura y el peso de 4 jugadores de béisbol, en este orden. `baseball` ya está codificado para ti en el script.

`@instructions`
- Usa `np.array()` para crear una matriz `numpy` de 2D a partir de `baseball`. Nómbrala `np_baseball`.
- Muestra por pantalla el tipo de `np_baseball`.
- Muestra por pantalla el atributo `shape` de `np_baseball`. Usa `np_baseball.shape`.

`@hint`
- `baseball` ya está codificado para tú en el script. Llama a `np.array()` sobre él y almacena el array 2D resultante de `numpy` en `np_baseball`.
- Usa `print()` en combinación con `type()` para la segunda instrucción.
- `np_baseball.shape` te dará las dimensiones de `np_baseball`. Asegúrate de envolver una llamada a `print()` alrededor de ello.

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
msg = "No tienes que cambiar ni eliminar las variables predefinidas."
Ex().check_object("baseball", missing_msg=msg).has_equal_value(incorrect_msg=msg)
Ex().has_import("numpy", same_as=False)

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

success_msg("¡Genial! ¡Ahora estás listo para convertir los datos reales de la MLB en un array 2D de `numpy`!")
```

---

## Datos de béisbol en 2D

```yaml
type: NormalExercise
key: 5df25d0b7b
lang: python
xp: 100
skills:
  - 2
```

Te das cuenta de que tiene más sentido reestructurar toda esta información en una matriz `numpy` bidimensional.

Tienes una lista de listas en Python. En esta lista de listas, cada sublista representa la altura y el peso de un único jugador de béisbol. El nombre de esta lista es `baseball` y ya se ha cargado previamente (aunque no la veas en pantalla).

Almacena los datos como una matriz bidimensional para desbloquear la funcionalidad adicional de `numpy`.

`@instructions`
- Usa `np.array()` para crear una matriz `numpy` 2D a partir de `baseball`. Nómbrala `np_baseball`.
- Muestra por pantalla el atributo `shape` de `np_baseball`.

`@hint`
- `baseball` ya está disponible en el entorno de Python. Llama a `np.array()` pasándole esta variable y guarda el array bidimensional `numpy` resultante en `np_baseball`.
- `np_baseball.shape` te dará las dimensiones de `np_baseball`. Asegúrate de envolverlo con una llamada a `print()`.

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

success_msg("¡Genial! ¡Es hora de mostrar algunas características impresionantes de los arreglos multidimensionales de `numpy`!")
```

---

## Crear subconjuntos de matrices de NumPy 2D

```yaml
type: NormalExercise
key: aeca4977f0
lang: python
xp: 100
skills:
  - 2
```

Si tu matriz 2D `numpy` tiene una estructura regular, es decir, cada fila y columna tiene un número fijo de valores, las formas complicadas de seleccionar subconjuntos se vuelven muy fáciles. Echa un vistazo al código de abajo, donde se extraen los elementos `"a"` y `"c"` de una lista de listas.

```
# numpy
import numpy as np
np_x = np.array(x)
np_x[:, 0]
```

Los índices antes de la coma se refieren a las filas, mientras que los que van después de la coma se refieren a las columnas. El `:` es para segmentar; en este ejemplo, le indica a Python que incluya todas las filas.

`@instructions`
- Muestra por pantalla la fila número 50 de `np_baseball`.
- Crea una nueva variable, `np_weight_lb`, que contenga toda la segunda columna de `np_baseball`.
- Selecciona la altura (primera columna) del jugador de béisbol número 124 en `np_baseball` y muéstrala por pantalla.

`@hint`
- Necesitas el índice de fila 49 en la primera instrucción. Más concretamente, querrás usar `[49, :]`.
- Para seleccionar toda la segunda columna, necesitarás `[:, 1]`.
- Para la última instrucción, usa `[123, 0]`; no olvides envolverlo todo en una instrucción `print()`.

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
msg = "No tienes que cambiar o eliminar las variables predefinidas."
Ex().multi(
    has_import("numpy", same_as = False),
    check_object("np_baseball", missing_msg=msg).has_equal_value(incorrect_msg = msg)
)

Ex().has_printout(0)

Ex().check_object('np_weight_lb').has_equal_value(incorrect_msg = "Puedes usar `np_baseball[:,1]` para definir `np_weight_lb`. Esto seleccionará toda la primera columna.")

Ex().has_printout(1)

success_msg("¡Esto va bien!")
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

Los arrays bidimensionales de `numpy` pueden realizar cálculos elemento a elemento, igual que los arrays de una sola dimensión. Ya tienes el código para `numpy`.

Te proporcionamos el código de `np_baseball`; vuelve a ser una matriz de `numpy` con 3 columnas que representan la altura (en pulgadas), el peso (en libras) y la edad (en años). Tienes `baseball` disponible como una lista de listas normal y `updated` como una matriz de numpy.

`@instructions`
- Has conseguido obtener los cambios en altura, peso y edad de todos los jugadores de béisbol. Está disponible como una matriz `numpy` 2D, `updated`. Añade `np_baseball` y `updated`, y muestra el resultado por pantalla.
- Quieres convertir las unidades de altura y peso al sistema métrico (metros y kilogramos, respectivamente). Como primer paso, crea una matriz `numpy` con tres valores: `0.0254`, `0.453592` y `1`. Nombra esta matriz `conversion`.
- Multiplica `np_baseball` por `conversion` y muestra el resultado por pantalla.

`@hint`
- `np_baseball + updated` realizará una suma elemento a elemento de los dos arrays de `numpy`.
- Crea un array de `numpy` con `np.array()`; el argumento de entrada debe ser una lista normal de Python con tres elementos.
- `np_baseball * conversion` funcionará directamente, sin necesidad de hacer nada más. ¡Pruébalo! Eso sí, asegúrate de meterlo dentro de una llamada a `print()`.

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

msg = "No tienes que cambiar ni eliminar las variables predefinidas."
Ex().check_object("np_baseball", missing_msg=msg).has_equal_value(incorrect_msg=msg)

Ex().has_printout(0)

Ex().check_correct(
    has_printout(1),
    check_correct(
        check_object('conversion').has_equal_value(),
        check_function('numpy.array', index=1).check_args(0).has_equal_value()
    )    
)

success_msg("¡Buen trabajo! Observa cómo con muy poco código, puedes cambiar todos los valores en tu estructura de datos `numpy` de una manera muy específica. ¡Esto será muy útil en tu futuro como científico de datos!")
```

---

## NumPy: estadística básica

```yaml
type: VideoExercise
key: 287995e488
xp: 50
```

`@projector_key`
34495ba457d74296794d2a122c9b6e19

---

## Media frente a mediana

```yaml
type: NormalExercise
key: 509c588eb6
lang: python
xp: 100
skills:
  - 2
```

Ahora ya sabes cómo usar funciones `numpy` para hacerte una mejor idea de tus datos. 

Los datos de béisbol están disponibles como una matriz `numpy` 2D con 3 columnas (altura, peso, edad) y 1015 filas. El nombre de esta matriz `numpy` es `np_baseball`. Sin embargo, después de reestructurar los datos, te das cuenta de que algunos valores de altura son inusualmente altos. Sigue las instrucciones y descubre qué estadístico resumido es el más adecuado si estás tratando con los llamados _valores atípicos_. `np_baseball` está disponible.

`@instructions`
- Crea un array de `numpy` llamado `np_height_in` que sea igual a la primera columna de `np_baseball`.
- Muestra por pantalla la media de `np_height_in`.
- Muestra por pantalla la mediana de `np_height_in`.

`@hint`
- Utiliza la indexación bidimensional (2D) de `numpy`: parte de la solución consiste en hacer `[:,0]`.
- Si has importado `numpy` como `np`, puedes usar `np.mean()` para calcular la media de un array de NumPy. No te olvides de incluir una llamada a `print()`.
- Para la última instrucción, utiliza `np.median()`.

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

Ex().check_object("np_height_in").has_equal_value(incorrect_msg = "Puedes usar `np_baseball[:,0]` para seleccionar la primera columna de `np_baseball`"),

Ex().check_correct(
    has_printout(0),
    check_function('numpy.mean').has_equal_value()
)

Ex().check_correct(
    has_printout(1),
    check_function('numpy.median').has_equal_value()
)

success_msg("Una altura promedio de 1586 pulgadas, eso no suena bien, ¿verdad? Sin embargo, la mediana no parece verse afectada por los valores atípicos: 74 pulgadas tiene mucho sentido. Siempre es una buena idea verificar tanto la mediana como la media, para tener una idea sobre la distribución general de todo el conjunto de datos.")
```

---

## Explorar los datos del béisbol

```yaml
type: NormalExercise
key: '4409948807'
lang: python
xp: 100
skills:
  - 2
```

Como la media y la mediana están tan alejadas, decides quejarte a la MLB. Encuentran el error y te envían los datos corregidos. De nuevo está disponible como una matriz NumPy 2D `np_baseball`, con tres columnas.

El script de Python en el editor ya incluye código para mostrar mensajes informativos con las distintas estadísticas resumidas y `numpy` ya está cargado como `np`. ¿Puedes terminar el trabajo? `np_baseball` está disponible.

`@instructions`
- El código para mostrar la altura media ya está incluido. Completa el código para la altura mediana.
- Usa `np.std()` en la primera columna de `np_baseball` para calcular `stddev`. 
- ¿Los jugadores grandes suelen pesar más? Usa `np.corrcoef()` para almacenar la correlación entre la primera y la segunda columna de `np_baseball` en `corr`.

`@hint`
- Usa `np.median()` para calcular la mediana. ¡Asegúrate de seleccionar primero la columna correcta!
- Selecciona la misma columna al calcular la desviación estándar con `np.std()`.
- Usa `np_baseball[:, 0]` y `np_baseball[:, 1]` para seleccionar la primera y la segunda columna; estas son las entradas de `np.corrcoef()`.

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
msg = "No deberías cambiar o eliminar la variable `avg` predefinida."
Ex().check_object("avg", missing_msg=msg).has_equal_value(incorrect_msg=msg)

missing = "¿Has usado `np.median()` para calcular la mediana?"
incorrect = "Para calcular `med`, pasa la primera columna de `np_baseball` a `numpy.median()`. El ejemplo de `np.mean()` muestra cómo se hace."
Ex().check_correct(
  check_object("med").has_equal_value(),
  check_function("numpy.median", index=0, missing_msg=missing).check_args(0).has_equal_value(incorrect_msg=incorrect)
)

missing = "¿Has usado `np.std()` para calcular la desviación estándar?"
incorrect = "Para calcular `stddev`, pasa la primera columna de `np_baseball` a `numpy.std()`. El ejemplo de `np.mean()` muestra cómo se hace."
Ex().check_correct(
  check_object("stddev").has_equal_value(),
  check_function("numpy.std", index=0, missing_msg=missing).check_args(0).has_equal_value(incorrect_msg=incorrect)
)

missing = "¿Has usado `np.corrcoef()` para calcular la correlación?"
incorrect1 = "Para calcular `corr`, el primer argumento de `np.corrcoef()` debería ser la primera columna de `np_baseball`, similar a cómo lo hiciste antes."
incorrect2 = "Para calcular `corr`, el segundo argumento de `np.corrcoef()` debería ser la segunda columna de `np_baseball`. En lugar de `[:,0]`, usa `[:,1]` esta vez."
Ex().check_correct(
  check_object("corr").has_equal_value(),
  check_function("numpy.corrcoef", index=0, missing_msg=missing).multi(
    check_args(0, missing_msg=incorrect1).has_equal_value(incorrect_msg=incorrect1),
    check_args(1, missing_msg=incorrect2).has_equal_value(incorrect_msg=incorrect2)
  )
)

success_msg("¡Gran trabajo! Has construido una base sólida - ahora es el momento de usar todas tus nuevas habilidades de ciencia de datos para resolver más desafíos y tener un impacto.")
```

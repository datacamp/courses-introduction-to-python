---
title: Insert title here
key: ae3238dcc7feb9adecfee0c395fc8dc8
video_link:
  mp3: >-
    https://videos.datacamp.com/mp3/translations/course_735/es-ES/f4b74251-5b21-4042-b838-1c3be34409a6.mp3
---

## Matrices de NumPy 2D

```yaml
type: TitleSlide
key: 0cc8abf493
```

`@lower_third`
name: Hugo Bowne-Anderson
title: Data Scientist at DataCamp

`@script`
¡Bien hecho, leyenda! Ahora recreemos las matrices numpy del vídeo anterior.


---

## Tipos de matrices de NumPy

```yaml
type: FullSlide
key: 1b9db47fd2
code_zoom: 100
```

`@part1`
```py
import numpy as np
np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
np_weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])
```

```py
type(np_height)
```

```out
numpy.ndarray
```

```py
type(np_weight)
```

```out
numpy.ndarray
```

`@script`
Si preguntas por el tipo de estas matrices, Python te dice que son numpy.ndarray. numpy dot indica que es un tipo que se definió en el paquete numpy. ndarray alude a una matriz n-dimensional. Las matrices np_height y np_weight son unidimensionales, pero es perfectamente posible crear matrices bidimensionales, tridimensionales e incluso de siete dimensiones. En este vídeo, solo nos quedaremos con las bidimensionales.


---

## Matrices de NumPy 2D

```yaml
type: FullSlide
key: ebb550dcba
code_zoom: 71
```

`@part1`
```py
np_2d = np.array([[1.73, 1.68, 1.71, 1.89, 1.79],
                  [65.4, 59.2, 63.6, 88.4, 68.7]])
```{{1}}
```py
np_2d
```{{2}}

```out
array([[ 1.73,  1.68,  1.71,  1.89,  1.79],
       [65.4 , 59.2 , 63.6 , 88.4 , 68.7 ]])
```{{2}}

```py
np_2d.shape
```{{3}}

```out
(2, 5) # 2 rows, 5 columns
```{{3}}

```py
np.array([[1.73, 1.68, 1.71, 1.89, 1.79],
          [65.4, 59.2, 63.6, 88.4, "68.7"]])
```{{4}}

```out
array([['1.73', '1.68', '1.71', '1.89', '1.79'],
       ['65.4', '59.2', '63.6', '88.4', '68.7']], dtype='<U32')
```{{4}}

`@script`
Puedes crear una matriz numpy 2D a partir de una lista Python normal de listas. Intentemos crear una matriz numpy para todos los datos de altura y peso de tu familia, como esta.

Si imprimes np_2d ahora, verás que es una estructura de datos rectangular: cada sublista de la lista corresponde a una fila de la matriz numpy bidimensional. En np_2d.shape, puedes ver que efectivamente tenemos 2 filas y 5 columnas. shape es un atributo de la matriz np2d que proporciona más información sobre la estructura de los datos.

Ten en cuenta que la sintaxis para acceder a un atributo se parece un poco a la llamada a un método, pero no son lo mismo. Recuerda que los métodos tienen corchetes después y, como puedes ver aquí, los atributos no.

También para las matrices 2D se aplica la regla NumPy: una matriz solo puede contener un único tipo. Si cambias un flotante por una cadena, todos los elementos de la matriz se convertirán en cadenas, para terminar con una matriz homogénea.


---

## Subconjuntos

```yaml
type: FullSlide
key: e71d2fc8b8
code_zoom: 80
```

`@part1`
```out
           0       1       2       3       4
           
array([[  1.73,   1.68,   1.71,   1.89,   1.79],     0
       [  65.4,   59.2,   63.6,   88.4,   68.7]])    1
```

```py
np_2d[0]
```

```out
array([1.73, 1.68, 1.71, 1.89, 1.79])
```

`@script`
Piensa en la matriz numpy 2D como una lista mejorada de listas: puedes realizar cálculos en las matrices, como mostré anteriormente, y hacer formas más avanzadas de subconjuntos.

Supongamos que quieres la primera fila y, a continuación, el tercer elemento de esa fila. Para seleccionar la fila, necesitas el índice 0 entre corchetes. No te olvides de la indexación cero.

Para seleccionar el tercer elemento, puedes ampliar la misma llamada con otro par de corchetes, esta vez con el índice 2.


---

## Subconjuntos

```yaml
type: FullSlide
key: 57a1fb1581
disable_transition: true
code_zoom: 80
```

`@part1`
```out
           0       1       2       3       4
           
array([[  1.73,   1.68,   1.71,   1.89,   1.79],     0
       [  65.4,   59.2,   63.6,   88.4,   68.7]])    1
```

```py
np_2d[0][2]
```

```out
1.71
```

```py
np_2d[0, 2]
```{{1}}

```out
1.71
```{{1}}

`@script`
Así. Básicamente, seleccionas la fila y, a continuación, desde esa fila seleccionas otra cosa.

Existe otra forma de crear subconjuntos, con corchetes simples y una coma. Esta llamada devuelve exactamente el mismo valor que antes. El valor antes de la coma especifica la fila; el valor después de la coma especifica la columna. Se devuelven las intersecciones de las filas y columnas que has especificado. Una vez que te acostumbras, esta sintaxis es más intuitiva y abre más posibilidades.


---

## Subconjuntos

```yaml
type: FullSlide
key: feb75c975c
disable_transition: true
code_zoom: 80
```

`@part1`
```out
           0       1       2       3       4
           
array([[  1.73,   1.68,   1.71,   1.89,   1.79],     0
       [  65.4,   59.2,   63.6,   88.4,   68.7]])    1
```

```py
np_2d[:, 1:3]
```{{1}}

```out
array([[ 1.68,  1.71],
       [59.2 , 63.6 ]])
```{{1}}

```py
np_2d[1, :]
```{{2}}

```out
array([65.4, 59.2, 63.6, 88.4, 68.7])
```{{2}}

`@script`
Supongamos que deseas seleccionar la altura y el peso del segundo y tercer miembro de la familia. Quieres ambas filas, así que pones dos puntos antes de la coma. Solo quieres la segunda y tercera columna, por lo que introduces los índices 1 a 3 después de la coma. Recuerda que el tercer índice no está incluido aquí. La intersección nos da una matriz 2D con 2 filas y 2 columnas:

Del mismo modo, puedes seleccionar el peso de todos los miembros de la familia de esta manera: solo quieres la segunda fila, por lo que pones 1 antes de la coma. Quieres todas las columnas, por lo que utilizas dos puntos después de la coma. La intersección nos da toda la segunda fila.

Por último, las matrices numpy 2D te permiten realizar cálculos por elementos, del mismo modo que lo hacías con las matrices numpy 1D. Eso es algo


---

## ¡Vamos a practicar!

```yaml
type: FinalSlide
key: 6047b27c09
```

`@script`
con lo que puedes experimentar en los ejercicios, además de crear y formar subconjuntos de matrices numpy 2D. ¡Emocionante!

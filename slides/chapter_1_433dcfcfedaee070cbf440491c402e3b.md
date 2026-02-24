---
title: Insert title here
key: 433dcfcfedaee070cbf440491c402e3b
video_link:
  mp3: >-
    https://videos.datacamp.com/mp3/translations/course_735/es-ES/c82b875a-ad57-4c2e-a44c-b1abb44c988b.mp3
---

## Variables y tipos

```yaml
type: TitleSlide
key: dc8b62f1c8
```

`@lower_third`
name: Hugo Bowne-Anderson
title: Data Scientist at DataCamp

`@script`
¡Bien hecho! Bienvenido de nuevo. Está claro que Python es una gran calculadora. Sin embargo, si deseas realizar cálculos más complejos, te recomendamos guardar los valores mientras escribes el código.


---

## Variable

```yaml
type: FullSlide
key: 36ec318b41
```

`@part1`
- Nombre específico, con distinción entre mayúsculas y minúsculas

- Llama al valor mediante el nombre de la variable{{1}}

- 1,79 m - 68,7 kg{{2}}

```py
height = 1.79
weight = 68.7
```{{3}}
```py
height
```{{4}}

```out
1.79
```{{4}}

`@script`
Para ello, define una variable con un nombre específico que distinga entre mayúsculas y minúsculas. Una vez creada (o declarada) una variable de este tipo, puedes recuperar su valor escribiendo el nombre de la variable.

Supongamos que mides tu altura y peso en unidades métricas: 1,79 metros y 68,7 kilogramos. Puedes asignar estos valores a dos variables, llamadas height y weight, con un signo igual:

Si ahora escribes el nombre de la variable, height,

Python busca el nombre de la variable, recupera su valor y lo imprime.


---

## Calcular IMC

```yaml
type: TwoColumns
key: fe1b10a93b
code_zoom: 80
```

`@part1`
```py
height = 1.79
weight = 68.7
```
```py
height
```

```out
1.79
```

$$ \text{BMI} = \frac{\text{weight}}{\text{height}^2} $${{1}}

`@part2`
```py
68.7 / 1.79 ** 2
```{{2}}

```out
21.4413
```{{2}}

```py
weight / height ** 2
```{{3}}

```out
21.4413
```{{3}}

```py
bmi = weight / height ** 2
bmi
```{{4}}

```out
21.4413
```{{4}}

`@script`
Ahora calcularemos el índice de masa corporal (IMC) de la siguiente manera, con el peso en kilogramos y la altura en metros. Puedes hacerlo con los valores reales, pero también utilizar las variables height y weight, como aquí. Cada vez que escribes el nombre de la variable, le estás pidiendo a Python que lo cambie por el valor real de la variable. weight corresponde a 68,7 y height, a 1,79.

Por último, en esta versión Python almacena el resultado en una nueva variable, bmi. bmi ahora contiene el mismo valor que calculaste anteriormente.

En Python, las variables se utilizan constantemente. Ayudan a que el código sea reproducible.


---

## Reproducibilidad

```yaml
type: FullSlide
key: 9980f47f9d
```

`@part1`
```py
height = 1.79
weight = 68.7
bmi = weight / height ** 2
print(bmi)
```

```out
21.4413
```

`@script`
Supongamos que el código para crear las variables height, weight y bmi se encuentra en un script, como este. Si ahora deseas volver a calcular el IMC para otro peso,


---

## Reproducibilidad

```yaml
type: FullSlide
key: a4e899f00f
disable_transition: true
```

`@part1`
```py
height = 1.79
weight = 74.2 # <-
bmi = weight / height ** 2
print(bmi)
```

```out
23.1578
```

`@script`
puedes cambiar la declaración de la variable weight y volver a ejecutar el script. El IMC cambia en consecuencia, ya que el valor de la variable weight también ha cambiado.

Hasta ahora, solo hemos trabajado con valores numéricos, como la altura y el peso.


---

## Tipos de Python

```yaml
type: FullSlide
key: 9d86084ad4
```

`@part1`
```py
type(bmi)
```{{1}}

```out
float
```{{1}}

```py
day_of_week = 5
type(day_of_week)
```{{2}}

```out
int
```{{2}}

`@script`
En Python, todos estos números tienen un tipo específico. Puedes comprobar el tipo de un valor con la función type. Para ver el tipo de nuestro valor de IMC, escribe type y luego bmi entre paréntesis. Puedes ver que es un flotante, que es la forma en que Python representa un número real (es decir, un número que puede tener una parte entera y una parte fraccionaria). Python también tiene un tipo para números enteros: int, como en este ejemplo.

Sin embargo, para dedicarte a la ciencia de datos, necesitarás algo más que enteros y flotantes.


---

## Tipos de Python (2)

```yaml
type: FullSlide
key: d971d34e6a
```

`@part1`
```py
x = "body mass index"
y = 'this works too'
```{{1}}
```py
type(y)
```{{2}}

```out
str
```{{2}}

```py
z = True
type(z)
```{{3}}

```out
bool
```{{3}}

`@script`
Python dispone de muchos otros tipos de datos. Los más comunes son las cadenas y los booleanos.

Una cadena es la forma que tiene Python de representar texto. Puedes utilizar tanto comillas simples como dobles para construir una cadena, como podemos ver en estos ejemplos. Si imprimes el tipo de la última variable, verás que es str, la abreviatura de cadena en inglés, string.

Booleano es un tipo de dato que puede ser True o False. Puedes pensar en ello como sí y no en el lenguaje cotidiano. Los booleanos serán muy útiles en el futuro (por ejemplo, para realizar operaciones de filtrado en los datos).

Hay algo especial en los tipos de datos de Python.


---

## Tipos de Python (3)

```yaml
type: FullSlide
key: 24601e2af0
```

`@part1`
```py
2 + 3
```{{1}}

```out
5
```{{1}}

```py
'ab' + 'cd'
```{{2}}

```out
'abcd'
```{{2}}

- Diferentes tipos = diferentes comportamientos{{3}}

`@script`
Echa un vistazo a esta línea de código, que suma dos números enteros, y luego a esta línea de código, que suma dos cadenas.

Para los números enteros, se sumaron los valores, mientras que para las cadenas, se pegaron juntas. El operador más se comportaba de forma diferente según el tipo de datos. Este es un principio general: el comportamiento del código depende de los tipos con los que estés trabajando.

En los ejercicios siguientes, crearás tus primeras variables y experimentarás con algunos de los tipos de datos de Python. Nos vemos en el próximo vídeo para explicaros todo sobre las listas.


---

## ¡Vamos a practicar!

```yaml
type: FinalSlide
key: b7fc40db4d
```

`@script`
Empecemos a programar. Estoy deseando verte en el próximo capítulo, donde crearás gráficos de Python aún más impresionantes.

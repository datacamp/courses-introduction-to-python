---
title_meta: Capítulo 1
title: Conceptos básicos de Python
description: >-
  Introducción a los conceptos básicos de Python. Aprende a usar Python de forma
  interactiva y mediante un script. Crea tus primeras variables y familiarízate
  con los tipos de datos básicos de Python.
attachments:
  slides_link: 'https://projector-video-pdf-converter.datacamp.com/735/chapter1.pdf'
free_preview: true
lessons:
  - nb_of_exercises: 5
    title: ¡Hola Python!
  - nb_of_exercises: 8
    title: Variables y tipos
---

## ¡Hola Python!

```yaml
type: VideoExercise
key: f644a48d5d
xp: 50
```

`@projector_key`
d8fcd4c930027fa4e1c3870c7e7e0ff1

---

## ¿Cuándo usar Python?

```yaml
type: MultipleChoiceExercise
key: 9703b117fb
lang: python
xp: 50
skills:
  - 2
```

Python es un lenguaje bastante versátil. ¿Para qué aplicaciones puedes usar Python?

`@possible_answers`
- Quieres hacer algunos cálculos rápidos.
- Para tu nuevo negocio, deseas desarrollar un sitio web basado en bases de datos.
- Tu jefe te pide que limpies y analices los resultados de la última encuesta de satisfacción.
- Todo lo anterior.

`@hint`
Hugo mencionó en el vídeo que Python puede usarse para construir prácticamente cualquier software.

`@pre_exercise_code`
```{python}

```

`@sct`
```{python}
msg1 = "Incorrecto. Python puede hacer cálculos simples y rápidos, ¡pero es mucho más que eso!"
msg2 = "Incorrecto. Existe un framework muy popular para crear sitios web basados en bases de datos (Django), pero Python puede hacer mucho más."
msg3 = "Incorrecto. Python es una herramienta poderosa para analizar datos, pero también se puede utilizar para otros fines."
msg4 = "¡Correcto! Python es un lenguaje extremadamente versátil."
Ex().has_chosen(4, [msg1, msg2, msg3, msg4])
```

---

## La interface de Python

```yaml
type: NormalExercise
key: bdc52f0e19
lang: python
xp: 100
skills:
  - 2
```

Presiona _Ejectuar Codígo_ para ejecutar tu primer código de Python con Datacamp y ver el resultado.

Observa la ventana `script.py`; aquí es donde puedes escribir código Python para resolver ejercicios. Puedes presionar _Ejectuar Codígo_ y _Enviar Respuesta_ tantas veces como quieras. Si tienes problemas, puedes hacer clic en _Obtener Sugerencia_ y, en última instancia, en _Obtener Solución_.

También puedes utilizar el shell de IPython de forma interactiva escribiendo comandos y presionando Enter. Ahí no se comprobará la exactitud de tu código, por lo que es una excelente forma de experimentar.

`@instructions`
- Experimenta en el shell de IPython; escribe `5 / 8`, por ejemplo.
- Añade otra línea de código a `script.py`, `print(7 + 10)`, para comprobar la respuesta.
- Presiona _Enviar Respuesta_ para ejecutar el script de Python y recibir comentarios.

`@hint`
- Añade `print(7 + 10)` bajo el `# Imprime la suma de 7 y 10` y presiona _Enviar Respuesta_ para comprobar si tu código es correcto.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Por ejemplo, ¡no modifiques!
print(5 / 8)

# Imprime la suma de 7 y 10
____
```

`@solution`
```{python}
# Por ejemplo, ¡no modifiques!
print(5 / 8)

# Pon el código aquí abajo
print(7 + 10)
```

`@sct`
```{python}
Ex().has_printout(1, not_printed_msg = "__JINJA__:Has usado `{{sol_call}}` para imprimir la suma de 7 y 10?")
success_msg("Excelente! Vamos al siguiente!")
```

---

## ¿Algún comentario?

```yaml
type: NormalExercise
key: 7c4a738a13
lang: python
xp: 100
skills:
  - 2
```

Algo que Hugo no mencionó en sus vídeos es que puedes añadir **comentarios** a tus scripts de Python. Los comentarios son importantes para garantizar que tú y los demás podáis entender de qué trata tu código.

Para añadir comentarios a tu script de Python, puedes utilizar el símbolo `#`. Estos comentarios no se ejecutan como código Python, por lo que no influirán en el resultado. Por ejemplo, el comentario en el editor `# División`; se ignora por completo durante la ejecución.

`@instructions`
Encima de `print(7 + 10)`, añade el comentario
```
# Suma
```

`@hint`
Para este ejercicio solo tienes que añadir una línea de comentarios. No se ejecutará como código Python. Añade `# Suma` justo encima de `print(7 + 10)`.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# División
print(5 / 8)


print(7 + 10)
```

`@solution`
```{python}
# División
print(5 / 8)

# Suma
print(7 + 10)
```

`@sct`
```{python}
Ex().has_code("#\s*(\w+)[\s.!?]*print\s*\(\s*7", not_typed_msg = "Asegúrate de añadir el comentario justo antes de `print(7 + 10)`.")
success_msg("¡Genial!")
```

---

## Python como calculadora

```yaml
type: NormalExercise
key: 0f7c039428
lang: python
xp: 100
skills:
  - 2
```

Python funciona muy bien para realizar cálculos básicos. Puedes realizar sumas, restas, multiplicaciones y divisiones, y también acepta operaciones más avanzadas como:

- Exponenciación: `**`. Este operador eleva el número de la izquierda a la potencia del número de la derecha. Por ejemplo, `3**4` es `3` elevado a la `4` y dará `81`.
- Modulo: `%`. Este operador devuelve el resto de la división del número a la izquierda por el número de la derecha. Por ejemplo, `18 % 7` es igual a `4` porque `7` cabe en `18` dos veces (7 x 2 = 14), lo que deja un resto de `4` (18 - 14 = 4).

El código del script ofrece algunos ejemplos.

¡Ahora es tu turno de practicar!

`@instructions`
- Cambia los valores de los números que se muestran para ver cómo Python realiza la suma y la resta.
- Cambia los valores de los números que se muestran para ver cómo funcionan la multiplicación, la división, el módulo y la exponenciación en Python.
- Calcula e imprime 2 elevado a la 5.

`@hint`
- La sintaxis de "el poder de" es `**`.

`@pre_exercise_code`
```{python}
 
```

`@sample_code`
```{python}
# Suma, resta
print(5 + 5)
print(5 - 5)

# Multiplicación, división, módulo y exponenciación
print(3 * 5)
print(10 / 2)
print(18 % 7)
print(4 ** 2)

# Calcula dos elevado a la cinco
print(____)
```

`@solution`
```{python}
# Suma, resta
print(5 + 5)
print(5 - 5)

# Multiplicación, división, módulo y exponenciación
print(3 * 5)
print(10 / 2)
print(18 % 7)
print(4 ** 2)

# Calcula dos elevado a la cinco
print(2 ** 5)
```

`@sct`
```{python}
Ex().has_printout(6, not_printed_msg = "¿Has utilizado `print (2 ** 5) ` para imprimir el resultado de tus cálculos?")
success_msg("Eso es correcto! Python te puede ayudar con operaciones matemáticas, algo que será de utilidad para tus análisis de datos")
```

---

## Variables y tipos

```yaml
type: VideoExercise
key: c2e396792e
xp: 50
```

`@projector_key`
433dcfcfedaee070cbf440491c402e3b

---

## Asignación de variables

```yaml
type: NormalExercise
key: 4bf65ad83e
lang: python
xp: 100
skills:
  - 2
```

En Python, una variable permite hacer referencia a un valor con un nombre. Para crear una variable `x` con un valor de `5`, usa `=`, como en este ejemplo:

```
x = 5
```

Ahora puedes usar el nombre de esta variable, `x`, en lugar del valor real, `5`.

Recuerda que = en Python significa _asignación_, ¡no comprobación de igualdad!

`@instructions`
- Crea la variable `savings` con un valor de `100`.
- Comprueba esta variable escribiendo `print(savings)` en el script.

`@hint`
- Escribe `savings = 100` para crear la variable `savings`.
- Tras crear la variable `savings`, puedes escribir `print(savings)`.

`@pre_exercise_code`
```{python}
 
```

`@sample_code`
```{python}
# Crea la variable llamada savings


# Imprime savings

```

`@solution`
```{python}
# Crea la variable llamada savings
savings = 100

# Imprime savings
print(savings)
```

`@sct`
```{python}
Ex().check_object("savings").has_equal_value(incorrect_msg="Asigna 100 a la variable `savings`.")
Ex().has_printout(0, not_printed_msg = "Imprime `savings`, la variable que creaste, con `print(savings) `.")
success_msg("Excelente! Intentemos ahora hacer cálculos con esta variable!")
```

---

## Cálculos con variables

```yaml
type: NormalExercise
key: ff06cedeb4
lang: python
xp: 100
skills:
  - 2
```

La fórmula para calcular cuánto dinero tendrías después de 7 años al invertir $100 por año con una rentabilidad del 10% es la siguiente:

```
100 * 1.1 ** 7
```

Esto se conoce como interés compuesto.

En lugar de calcular con los valores reales, puede utilizar variables. La variable savings que creamos en el ejercicio anterior representa los $100 con los que comenzamos. ¡Depende de ti crear una nueva variable que represente la versión `1.1` y volver a hacer los cálculos!

`@instructions`
- Crea la variable `growth_multiplier` con valor de `1.1`.
- Crea una variable, `result`, igual a la cantidad de dinero que habrás ahorrado después de `7` años.
- Imprime el valor de `result`.

`@hint`
- Para crear la variable `growth_multiplier`, puedes escribir `growth_multiplier = 1.1`.
- Usando como base el bloque de código de ejemplo del ejercicio, sustituye `100` por `savings` y `1.1` por `growth_multiplier`: `savings * growth_multiplier ** 7`.
- Usa la función [`print()`](https://docs.python.org/3/library/functions.html#print) para imprimir el valor de una variable.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Crea la variable savings
savings = 100

# Crea la variable growth_multiplier


# Calcula result


# Imprime result

```

`@solution`
```{python}
# Crea la variable savings
savings = 100

# Crea la variable growth_multiplier
growth_multiplier = 1.1

# Calcula result
result = savings * growth_multiplier ** 7

# Imprime result
print(result)
```

`@sct`
```{python}
Ex().check_object("savings", missing_msg="La variable savings se definió automáticamente, ¡no la elimines!").has_equal_value (incorrect_msg="La variable savings debería valer `100`, tal y como se definió para ti."),
Ex().check_object("growth_multiplier") .has_equal_value(incorrect_msg= "¿Has asignado el valor correcto a growth_multiplier?")
Ex().check_correct(
  check_object("result").has_equal_value(incorrect_msg="¿ Has usado `*` y `**` para calcular result?"),
  multi(
    has_code("savings\s*\*\s*\(*\s*growth_multiplier", not_typed_msg = "¿Multiplicaste `savings` por `growth_multiplier ** 7`?"),      
    has_code("growth_multiplier\s*\*\*\s*7", not_typed_msg = "¿Has elevado `growth_multiplier` a la potencia de `7` usando `**`?")
  )
)

Ex().has_printout(0, not_printed_msg="Recuerda imprimir `result` al final del script.")
success_msg("¡Genial!")
```

---

## Otros tipos de variables

```yaml
type: NormalExercise
key: 006b48561f
lang: python
xp: 100
skills:
  - 2
```

En el ejercicio anterior, trabajamos con dos tipos de datos de Python:

- `int` o integer: número sin parte fraccionaria. `savings`, con un valor `100`, es un ejemplo de número integer (entero).
- `float` o floating point: número que tiene una parte entera y una fraccionaria, separadas por un punto. `growth_multiplier`, con un valor `1.1`, es un ejemplo de número floating point (punto flotante o flotante).

Además de los tipos de datos numéricos, hay otros dos tipos de datos muy comunes:

- `str` o string: un tipo para representar texto. Puedes utilizar comillas simples o dobles para crear una cadena de carácteres (string en inglés).
- `bool` o booleano: un tipo para representar valores lógicos. Solo puede ser `True` o `False` (¡La capitalización es importante!).

`@instructions`
- Crea una nueva cadena (string), `desc`, con el valor `"compound interest"`.
- Crea un nuevo booleano, `profitable`, con el valor `True`.

`@hint`
- Para crear una variable en Python, utiliza `=`. Asegúrate de escribir la cadena (string) entre comillas simples o dobles.
- Solo existen dos valores booleanos en Python: `True` y `False`. No funcionará si usamos `TRUE`, `true`, `FALSE`, `false` u otros.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Crea la variable desc


# Crea la variable profitable

```

`@solution`
```{python}
# Crea la variable desc
desc = "compound interest"

# Crea la variable profitable
profitable = True
```

`@sct`
```{python}
Ex().check_object("desc").has_equal_value(incorrect_msg = "Hmm, hay algo incorrecto en tu variable `desc`. Revisa la ortografía y asegúrate de que has usado comillas.")
Ex().check_object("profitable").has_equal_value(incorrect_msg = "Usaste la capitalización correcta para el booleano? Recuerda que no lleva comillas.")
success_msg("Muy bien!")
```

---

## Adivina el tipo

```yaml
type: MultipleChoiceExercise
key: b35f67514c
lang: python
xp: 50
skills:
  - 2
```

Para averiguar el tipo de un valor o de una variable que hace referencia a ese valor, puedes utilizar la función [`type()`](https://docs.python.org/3/library/functions.html#type). Supongamos que has definido una variable `a`, pero has olvidado el tipo de esa variable. Para determinar el tipo de `a`, simplemente ejecuta:

```
type(a)
```

Ya hemos creado tres variables: `a`, `b` y `c`. Puedes utilizar el shell de IPython para descubrir su tipo. ¿Cuál de las siguientes opciones es correcta?

`@possible_answers`
- `a` es de tipo `int`, `b` es de tipo `str`, `c` es de tipo `bool`
- `a` es de tipo `float`, `b` es de tipo `bool`, `c` es de tipo `str`
- `a` es de tipo `float`, `b` es de tipo `str`, `c` es de tipo `bool`
- `a` es de tipo `int`, `b` es de tipo `bool`, `c` es de tipo `str`

`@hint`
Utiliza type(a), type(b) y type(c) dentro del shell de IPython para conocer los tipos de las variables.

`@pre_exercise_code`
```{python}
a = 100*1.1**7
b = "True"
c = False
```

`@sct`
```{python}
msg1 = "El tipo de `a` no es `int`. Prueba `type (a)` y compruébalo tu mismo."
msg2 = "`b` no es un `bool`, ¡es un `str`! El hecho de que `True` esté entre comillas dobles lo convierte en una cadena (string)."
msg3 = "¡Perfecto!"
msg4 = "Ninguno de los tipos de variable es correcto. Prueba `type(a) `y ve de qué tipo es esta variable."
Ex().has_chosen(3, [msg1, msg2, msg3, msg4])
```

---

## Operaciones con otros tipos

```yaml
type: NormalExercise
key: 4d0d83cc02
lang: python
xp: 100
skills:
  - 2
```

Hugo mencionó que los diferentes tipos se comportan de manera diferente en Python.

Cuando sumas dos cadenas (strings), por ejemplo, obtendrás un comportamiento diferente al que se obtienen al sumar dos números enteros o dos booleanos.

En el script ya se han creado algunas variables de diferentes tipos. Depende de ti utilizarlos correctamente.

`@instructions`
- Calcula el producto de `savings` y `growth_multiplier`. Guarda el resultado en `year1`.
- ¿Cuál crees que será el tipo resultante? Descúbrelo imprimiendo el tipo de `year1`.
- Calcula la suma de `desc` y `desc` y almacena el resultado en una nueva variable `doubledesc`.
- Imprime `dobledesc`. ¿Esperabas eso?

`@hint`
- Asigna `growth_multiplier * savings` a una nueva variable, `year1`.
- Para imprimir el tipo de una variable `x`, utiliza `print(type (x))`.
- Asigna `desc + desc` a una nueva variable, `doubledesc`.
- Para imprimir una variable `x`, escribe `print(x)` en el script.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
savings = 100
growth_multiplier = 1.1
desc = "compound interest"

# Asigna el producto de savings y growth_multiplier a year1


# Imprime el tipo de year1


# Asigna la suma de desc y desc a doubledesc


# Imprime doubledesc

```

`@solution`
```{python}
savings = 100
growth_multiplier = 1.1
desc = "compound interest"

# Asigna el producto de savings y growth_multiplier a year1
year1 = savings * growth_multiplier

# Imprime el tipo de year1
print(type(year1))

# Asigna la suma de desc y desc a doubledesc
doubledesc = desc + desc

# Imprime doubledesc
print(doubledesc)
```

`@sct`
```{python}
# predefined
msg = "No es necesario cambiar ni eliminar las variables predefinidas."

Ex().multi(
    check_object('savings', missing_msg=msg).has_equal_value(incorrect_msg=msg),
    check_object('growth_multiplier', missing_msg=msg).has_equal_value(incorrect_msg=msg),
    check_object('desc', missing_msg=msg).has_equal_value(incorrect_msg=msg)
)

# check year1 and printout
Ex().multi(
    check_object("year1").has_equal_value(incorrect_msg="Multiplica `savings` y `growth_multiplier` para crear la variable `year1`."),
    has_printout(0, not_printed_msg = "__JINJA__:Usa `{{sol_call}}` para imprimir el tipo de `year1`.")
)

# check doubledesc and printout
Ex().multi(
    check_object("doubledesc").has_equal_value(incorrect_msg = "¿Has guardado el resultado de `desc + desc` en `doubledesc`?"),
    has_printout(1, not_printed_msg = "No olvides imprimir `doubledesc`.")
)

success_msg("Muy bien. Observa como `desc + desc` pega `\"compound interest\"` con `\"compound interest\"`.")
```

---

## Conversión de tipos

```yaml
type: NormalExercise
key: 085bb602b9
lang: python
xp: 100
skills:
  - 2
```

Usar el operador `+` para pegar dos cadenas puede resultar muy útil para crear mensajes personalizados.

Supongamos, por ejemplo, que has calculado el rendimiento de la inversión y deseas resumir los resultados en una sola cadena.

Para ello, tendrás que convertir de forma explícita los tipos de tus variables para que todas sean del tipo string. Más específicamente, necesitarás `str()` para convertir un valor en una cadena. `str(savings)`, por ejemplo, convertirá el entero `savings` en una cadena.

Funciones similares como [`int()`](https://docs.python.org/3/library/functions.html#int), [`float()`](https://docs.python.org/3/library/functions.html#float) y [`bool()`](https://docs.python.org/3/library/functions.html#bool) te ayudarán a convertir valores de Python a cualquier tipo.

`@instructions`
- Presiona _Ejecutar Código_ para ejecutar el código. Intenta entender el mensaje de error.
- Corrige el código de forma que la impresión se ejecute sin errores; utiliza la función [`str()`](https://docs.python.org/3/library/functions.html#func-str) para convertir las variables `savings` y `result` en cadenas. 
- Convierte la variable `pi_string` en un elemento flotante y almacena este elemento como una nueva variable, `pi_float`.

`@hint`
- El mensaje de error al ejecutar el código por primera vez te indica que tenemos un error en la línea 6 en el que al menos una de las variables no es un string.
- ¡Deberíamos usar [`str()`](https://docs.python.org/3/library/functions.html#func-str) dos veces!
- Usa [`float()`](https://docs.python.org/3/library/functions.html#float) con `pi_string` y almacena el resultado en `pi_float`.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Definición de savings y result
savings = 100
result = 100 * 1.10 ** 7

# Arregla la impresión
print("Empecé con $" + savings + "y ahora tengo $" + result + ".  ¡Impresionante!")

# Definición de pi_string
pi_string = "3.1415926"

# Convierte pi_string en float: pi_float
pi_float =
```

`@solution`
```{python}
# Definición de savings y result
savings = 100
result = 100 * 1.10 ** 7

# Arregla la impresión
print("Empecé con $" + str(savings) + " y ahora tengo $" + str(result) + ".  ¡Impresionante!")

# Definición de pi_string
pi_string = "3.1415926"

# Convierte pi_string en float: pi_float
pi_float = float(pi_string)
```

`@sct`
```{python}

# Asegúrate de que los valores predefinidos no se modifiquen
msg = "No es necesario cambiar ni eliminar las variables predefinidas."
Ex().multi(
    check_object("savings", missing_msg=msg).has_equal_value(incorrect_msg=msg),
    check_object("result", missing_msg=msg).has_equal_value(incorrect_msg=msg)
)

Ex().check_correct(
    has_printout(0),
    multi(
        check_function("str", 0).check_args(0).has_equal_value(incorrect_msg="Dentro del comando `print()`, asegúrate de convertir el valor de `savings` en una cadena con `str(savings)`."),
        check_function("str", 1).check_args(0).has_equal_value(incorrect_msg="Dentro del comando `print()`, asegúrate de convertir `result` en una cadena usando `str(result)`.")
    )
)

# check pi_float
Ex().check_correct(
    check_object("pi_float").has_equal_value(),
    multi(
        check_object("pi_string").has_equal_value(),
        check_function("float", missing_msg = "Para convertir `pi_string` en un flotante, asegúrate de usar la función `float()`.").has_equal_value(incorrect_msg="Usa `float(pi_string)` para crear la variable `pi_float`.")
    )
)

success_msg("¡Genial! Tienes una utilidad de alrededor de $95; ¡bastante impresionante!")
```

---

## ¿Python puede con todo?

```yaml
type: MultipleChoiceExercise
key: 3e5f0bdf3a
lang: python
xp: 50
skills:
  - 2
```

Ahora que sabes algo más sobre la combinación de diferentes fuentes de información, echemos un vistazo a las cuatro expresiones de Python que aparecen a continuación.
¿Cuál de estas opciones generará un error? ¡Puedes copiar y pegar este código en el Shell de IPython para averiguarlo!

`@possible_answers`
- `"Puedo sumar números enteros, como" + str(5) + "a las cadenas."`
- `"Dije " + ("Hola " * 2) + "¡Hola!"`
- `"La respuesta correcta a este ejercicio de opción múltiple es la respuesta número" + 2`
- `True + False`

`@hint`
Copia y pega las diferentes expresiones en el shell de IPython e intenta averiguar cuál produce un error.

`@pre_exercise_code`
```{python}

```

`@sct`
```{python}
msg1 = "Incorrecto, este comando funciona perfectamente."
msg2 = "Es completamente posible 'multiplicar cadenas' en Python..."
msg3 = "Correcto!  Como no estamos convirtiendo `2` a cadena usando [str()](https://docs.python.org/3/library/functions.html#func-str),  esta opción generará un error."
msg4 = "`True + False` no genera un error. Usa la consola para comprobarlo"
Ex().has_chosen(3, [msg1, msg2, msg3, msg4])
```

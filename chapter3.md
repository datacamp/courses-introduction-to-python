---
title_meta: Capítulo 3
title: Funciones y paquetes
description: >-
  Aprenderás a utilizar funciones, métodos y paquetes para aprovechar con
  eficiencia el código que han escrito brillantes desarrolladores de Python. El
  objetivo es reducir la cantidad de código que necesitas para resolver
  problemas difíciles.
attachments:
  slides_link: 'https://projector-video-pdf-converter.datacamp.com/735/chapter3.pdf'
lessons:
  - nb_of_exercises: 4
    title: Funciones
  - nb_of_exercises: 4
    title: Métodos
  - nb_of_exercises: 4
    title: Paquetes
---

## Funciones

```yaml
type: VideoExercise
key: 5c5f365930
xp: 50
```

`@projector_key`
1204d914b0e53100529827e07441ee6c

---

## Funciones conocidas

```yaml
type: NormalExercise
key: c422ee929b
lang: python
xp: 100
skills:
  - 2
```

De forma predeterminada, Python ofrece un montón de funciones integradas para facilitarte la vida como científico de datos. Ya conoces dos de esas funciones: `print()` y `type()`. También hay funciones como `str()`, `int()`, `bool()` y `float()` para cambiar de tipo de datos. Puedes informarte sobre ellas [aquí.](https://docs.python.org/3/library/functions.html) También son funciones integradas.

Llamar a una función es fácil. Para obtener el tipo de `3.0` y almacenar el resultado como nueva variable, `result`, puedes utilizar lo siguiente:

```
result = type(3.0)
```

`@instructions`
- Utiliza `print()` en combinación con `type()` para imprimir el tipo de `var1`.
- Utiliza `len()` para obtener la [longitud de la lista](https://docs.python.org/3/library/functions.html#len) `var1`. Escríbela en una llamada a `print()` para imprimirla directamente.
- Utiliza `int()` para convertir `var2` en un [entero](https://docs.python.org/3/library/functions.html#int). Almacena el resultado como `out2`.

`@hint`
- Llama a la función `type()` del siguiente modo: `type(var1)`.
- Llama a `print()` como ya has hecho tantas veces. Solo tienes que escribir entre paréntesis la variable que quieres imprimir.
- `int(x)` convertirá `x` en un entero.

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
msg = "No tienes que cambiar ni eliminar las variables predefinidas."
Ex().check_object("var1", missing_msg=msg).has_equal_value(incorrect_msg=msg)
Ex().check_object("var2", missing_msg=msg).has_equal_value(incorrect_msg=msg)

patt = "__JINJA__:Asegúrate de imprimir el %s de `var1` con `{{sol_call}}`."
Ex().has_printout(0, not_printed_msg = patt % 'tipo')
Ex().has_printout(1, not_printed_msg = patt % 'longitud')

int_miss_msg = "¿Has usado `int()` para convertir `var2` en un entero?"
int_incorr_msg = "¿Has pasado `var2` a `int()`?"
Ex().check_correct(
  check_object("out2").has_equal_value(incorrect_msg="Llamaste a `int()` correctamente; ahora asegúrate de asignar el resultado de esta llamada a `out2`."),
  check_function("int", missing_msg=int_miss_msg).has_equal_value(incorrect_msg=int_incorr_msg)
)
success_msg("¡Buen trabajo! La función `len()` es extremadamente útil; también funciona en cadenas para contar el número de caracteres.")
```

---

## ¡Ayuda!

```yaml
type: MultipleChoiceExercise
key: 679b852978
lang: python
xp: 50
skills:
  - 2
```

Quizá ya conozcas el nombre de una función de Python, pero aún tienes que averiguar cómo utilizarla. Irónicamente, tienes que pedir información sobre una función con otra función: `help()`. En IPython concretamente, también puedes utilizar `?` antes del nombre de la función.

Para obtener ayuda sobre la función `max()`, por ejemplo, puedes utilizar una de estas llamadas:

```
help(max)
?max
```

Utiliza el terminal IPython para abrir la [documentación](https://docs.python.org/3/library/functions.html#pow) sobre `pow()`. Para ello, escribe `?pow` o `help(pow)` y pulsa **Intro**.

¿Cuál de las siguientes afirmaciones es cierta?

`@possible_answers`
- `pow()` recibe tres argumentos: `base`, `exp` y `mod`. Sin `mod`, la función devolverá un error.
- `pow()` recibe tres argumentos obligatorios: `base`, `exp` y `None`.
- `pow()` requiere los argumentos `base` y `exp`; `mod` es opcional.
- `pow()` recibe dos argumentos: `exp` y `mod`. Si falta `exp`, se produce un error.

`@hint`
- Los argumentos opcionales se establecen en `=` con respecto a un valor predeterminado, que la función utilizará si no se especifica ese argumento.

`@pre_exercise_code`
```{python}

```

`@sct`
```{python}
msg1 = "No del todo. `mod` tiene un valor predeterminado que se usará si no especificas un valor."
msg2 = "Incorrecto. `None` es el valor predeterminado para el argumento `mod`."
msg3 = "¡Perfecto! Usar `help()` puede ayudarte a entender cómo funcionan las funciones, ¡desatando todo su potencial!"
msg4 = "Incorrecto. `pow()` toma tres argumentos, uno de los cuales tiene un valor predeterminado."
Ex().has_chosen(3, [msg1, msg2, msg3, msg4])
```

---

## Varios argumentos

```yaml
type: NormalExercise
key: e30486d7c1
lang: python
xp: 100
skills:
  - 2
```

En el ejercicio anterior, identificaste los argumentos opcionales consultando la documentación con `help()`. Ahora aplicarás esto para cambiar el comportamiento de la función `sorted()`.

Echa un vistazo a la [documentación](https://docs.python.org/3/library/functions.html#sorted) de `sorted()` escribiendo `help(sorted)` en el terminal IPython.

Verás que `sorted()` recibe tres argumentos: `iterable`, `key` y `reverse`. En este ejercicio solo tendrás que especificar `iterable` y `reverse`, no `key`.

Se han creado dos listas para ti.

¿Puedes pegarlas y ordenarlas en orden descendente?

`@instructions`
- Utiliza `+` para fusionar el contenido de `first` y `second` en una nueva lista: `full`.
- Llama a `sorted()` y, en `full`, y especifica que el argumento `reverse` sea `True`. Guarda la lista ordenada como `full_sorted`.
- Termina imprimiendo `full_sorted`.

`@hint`
- Suma `first` y `second` como si fueran dos números y asigna el resultado a `full`.
- Utiliza `sorted()` con dos entradas: `full` y `reverse=True`.
- Para imprimir una variable, utiliza `print()`.

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
msg = "No tienes que cambiar ni eliminar las variables `first` y `second` ya existentes."
Ex().multi(
  check_object("first", missing_msg=msg).has_equal_value(incorrect_msg=msg),
  check_object("second", missing_msg=msg).has_equal_value(incorrect_msg=msg)
)
Ex().check_correct(
  check_object("full_sorted").has_equal_value(incorrect_msg="Asegúrate de asignar el resultado de llamar a `sorted()` a `full_sorted`."),
  check_function("sorted").multi(
    check_args(0).has_equal_value(),
    check_args('reverse').has_equal_value()
  )
)

success_msg("¡Genial! Ve al video sobre métodos en Python.")
```

---

## Métodos

```yaml
type: VideoExercise
key: 2b66cb66b1
xp: 50
```

`@projector_key`
8e387776f3a264a745128b68aa8d8f83

---

## Métodos de cadena

```yaml
type: NormalExercise
key: 4039302ee0
lang: python
xp: 100
skills:
  - 2
```

Las cadenas tienen un montón de métodos. Sigue atentamente las instrucciones para descubrir algunos de ellos. Si quieres descubrirlos con más detalle, siempre puedes escribir `help(str)` en el terminal IPython.

Ya se ha creado una cadena `place` para que experimentes con ella.

`@instructions`
- Utiliza el [método](https://docs.python.org/3/library/stdtypes.html#str.upper) `.upper()` en `place` y almacena el resultado en `place_up`. Utiliza la sintaxis de llamada a métodos que aprendiste en el vídeo anterior.
- Imprime `place` y `place_up`. ¿Cambiaron ambos?
- Imprime el número de oes de la variable `place` llamando a `.count()` en `place` y pasando la letra `'o'` como entrada al método. ¡Estamos hablando de la variable `place`, no de la palabra `"place"`!

`@hint`
- Puedes llamar al método `.upper()` en `place` sin ninguna entrada adicional.
- Para imprimir una variable `x`, puedes escribir `print(x)`.
- Asegúrate de escribir tu llamada a `place.count(____)` en una función `print()` para que puedas imprimirla.

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
msg = "No tienes que cambiar ni eliminar las variables predefinidas."
Ex().check_object("place", missing_msg=msg).has_equal_value(incorrect_msg=msg)

patt = "No olvides imprimir `%s`."
Ex().has_printout(0, not_printed_msg=patt % "place")
Ex().check_correct(
    has_printout(1, not_printed_msg=patt % "place_up"),
    check_correct(
        check_object("place_up").has_equal_value(incorrect_msg="Asigna el resultado de tu llamada `place.upper()` a `place_up`."),
        check_function("place.upper", signature=False)
    )
)    

# check count of place
Ex().check_correct(
  has_printout(2, not_printed_msg = "Has calculado bien el número de o's en `place`; ahora asegúrate de envolver la llamada `place.count('o')` en una función `print()` para imprimir el resultado."),
  check_function("place.count", signature=False).check_args(0).has_equal_value()
)

success_msg("¡Bien hecho! Observa en las impresiones que el método `upper()` no cambia el objeto en el que se llama. ¡Esto será diferente para las listas en el próximo ejercicio!")
```

---

## Métodos de lista

```yaml
type: NormalExercise
key: 0dbe8ed695
lang: python
xp: 100
skills:
  - 2
```

Las cadenas no son los únicos tipos de Python que tienen métodos asociados. Las listas, los flotantes, los enteros y los booleanos también son tipos que tienen un montón de métodos útiles. En este ejercicio, experimentarás con:

- `.index()`, para obtener el índice del primer elemento de una lista que coincida con su entrada, y
- `.count()`, para obtener el número de veces que aparece un elemento en una lista.

Trabajarás en la lista con la superficie de distintas partes de una casa: `areas`.

`@instructions`
- Utiliza el método `.index()` para obtener el índice del elemento de `areas` que es igual a `20.0`. Imprime este índice.
- Llama a `.count()` en `areas` para saber cuántas veces aparece `9.50` en la lista. De nuevo, simplemente imprime este número.

`@hint`
- Para imprimir el índice, escribe la llamada a `areas.index(___)` en una función `print()`.
- Para imprimir el número de veces que aparece un elemento `x` en la lista, escribe la llamada a `areas.count(___)` en una función `print()`.

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
predef_msg = "No tienes que cambiar ni eliminar la lista predefinida `areas`."

Ex().check_object("areas", missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg)

Ex().check_function("print", index=0).check_args(0).check_function('areas.index', signature=False).check_args(0).has_equal_value()


Ex().check_function("print", index=1).check_args(0).check_function('areas.count', signature=False).has_equal_value()

success_msg("¡Bien hecho! Estos fueron ejemplos de métodos de `list` que no cambiaron la lista en la que fueron llamados.")
```

---

## Métodos de lista (2)

```yaml
type: NormalExercise
key: 1fbeab82d0
lang: python
xp: 100
skills:
  - 2
```

La mayoría de los métodos de lista cambian la lista en la que se llaman. Algunos ejemplos son:

- `.append()`, que añade un elemento a la lista en la que se llama.
- `.remove()`, que [elimina](https://docs.python.org/3/library/stdtypes.html#typesseq-mutable) el primer elemento de una lista que coincida con la entrada.
- `.reverse()`, que [invierte](https://docs.python.org/3/library/stdtypes.html#typesseq-mutable) el orden de los elementos de la lista en la que se llama.

Trabajarás en la lista con la superficie de distintas partes de la casa: `areas`.

`@instructions`
- Utiliza `.append()` dos veces para volver a añadir el tamaño de la caseta de piscina y del garaje: `24.5` y `15.45`, respectivamente. Asegúrate de añadirlos en este orden.
- Imprime `areas`.
- Utiliza el método `.reverse()` para invertir el orden de los elementos en `areas`.
- Vuelve a imprimir `areas`.

`@hint`
- Para la primera instrucción, utiliza la llamada a `areas.append(___)` dos veces.
- Para imprimir una variable `x`, basta con escribir `print(x)`.
- El método `.reverse()` no requiere entradas adicionales; basta con utilizar la notación de puntos y paréntesis vacíos: `.reverse()`.
- Para imprimir una variable `x`, basta con escribir `print(x)`.

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

success_msg("¡Genial!")
```

---

## Paquetes

```yaml
type: VideoExercise
key: ab96a17c5e
xp: 50
```

`@projector_key`
cedcfb34350be8545599768f96695cdd

---

## Importar paquete

```yaml
type: NormalExercise
key: 7432a6376f
lang: python
xp: 100
skills:
  - 2
```

Supongamos que quieres calcular la circunferencia y el área de un círculo. He aquí cómo son esas fórmulas:

$$C = 2 \pi r$$
$$A = \pi r^2 $$

En lugar de escribir el número de `pi`, puedes utilizar el paquete `math` que contiene el número.

Como referencia, `**` es el símbolo de la potenciación. Por ejemplo, `3**4` es `3` elevado a `4` y dará `81`.

`@instructions`
- Importa el paquete `math`.
- Utiliza `math.pi` para calcular la circunferencia del círculo y almacenarla en `C`.
- Utiliza `math.pi` para calcular el área del círculo y almacenarla en `A`.

`@hint`
- Puedes utilizar simplemente `import math` y, luego, hacer referencia a `pi` con `math.pi`.
- Utiliza la ecuación del texto de la tarea para hallar `C`. Utiliza `*`.
- Utiliza la ecuación del texto de la tarea para hallar `A`. Utiliza `*` y `**`.

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
patt = "Tu cálculo de `%s` no es del todo correcto. Asegúrate de usar `math.pi`."
Ex().multi(
  has_import('math', same_as=False),
  check_object('C').has_equal_value(incorrect_msg=patt%'C'),
  check_object('A').has_equal_value(incorrect_msg=patt%'A')
)

Ex().multi(
  has_printout(0, not_printed_msg = "__JINJA__:Mantén `{{sol_call}}` ahí para imprimir la circunferencia."),
  has_printout(1, not_printed_msg = "__JINJA__:Mantén `{{sol_call}}` ahí para imprimir el área.")
)

success_msg("¡Bien! Si sabes cómo manejar funciones de paquetes, el poder de muchos programadores de Python está a tu alcance.")
```

---

## Importación selectiva

```yaml
type: NormalExercise
key: fe65eff50a
lang: python
xp: 100
skills:
  - 2
```

Las importaciones generales, como `import math`, ponen a tu disposición **toda** la funcionalidad del paquete `math`. Sin embargo, si decides utilizar solo una parte concreta de un paquete, siempre puedes hacer que tu importación sea más selectiva:

```
from math import pi
```

Vuelve a intentar lo mismo, pero esta vez utiliza solo `pi`.

`@instructions`
- Realiza una importación selectiva del paquete `math` en la que solo importes la función `pi`.
- Utiliza `pi` para calcular la circunferencia del círculo y almacenarla en `C`.
- Utiliza `pi` para calcular el área del círculo y almacenarla en `A`.

`@hint`
- Utiliza `from math import pi` para hacer la importación selectiva.
- Ahora puedes utilizar `pi` solo.

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
patt = "Tu cálculo de `%s` no es del todo correcto. Asegúrate de usar solo `pi`."

Ex().has_import("math.pi", not_imported_msg = "Asegúrate de importar `pi` del paquete `math`. Deberías usar la notación `from ___ import ___`.",)

Ex().multi(
  check_object('C').has_equal_value(incorrect_msg=patt%'C'),
  check_object('A').has_equal_value(incorrect_msg=patt%'A')
)

Ex().multi(
  has_printout(0, not_printed_msg = "__JINJA__:Mantén `{{sol_call}}` ahí para imprimir la circunferencia."),
  has_printout(1, not_printed_msg = "__JINJA__:Mantén `{{sol_call}}` ahí para imprimir el área.")
)

success_msg("¡Bien hecho! Pasa al siguiente ejercicio.")
```

---

## Diferentes formas de importar

```yaml
type: MultipleChoiceExercise
key: f1b2675a2a
lang: python
xp: 50
skills:
  - 2
```

Hay varias formas de importar paquetes y módulos en Python. Dependiendo de la llamada a la importación, tendrás que utilizar un código Python diferente.

Supongamos que quieres utilizar la [función](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.inv.html) `inv()`, que está en el subpaquete `linalg` del paquete `scipy`. Quieres poder utilizar esta función del siguiente modo:

```
my_inv([[1,2], [3,4]])
```

¿Qué declaración `import` necesitarás para ejecutar el código anterior sin errores?

`@possible_answers`
- `import scipy`
- `import scipy.linalg`
- `from scipy.linalg import my_inv`
- `from scipy.linalg import inv as my_inv`

`@hint`
- Prueba las distintas sentencias import en el terminal IPython y comprueba cuál de ellas hace que la línea `my_inv([[1, 2], [3, 4]])` se ejecute sin errores. Pulsa **Intro** para ejecutar el código que has escrito.

`@pre_exercise_code`
```{python}

```

`@sct`
```{python}
msg1 = msg2 = msg3 = "Incorrecto, inténtalo de nuevo. Prueba las diferentes declaraciones de importación en la consola de IPython y ve cuál hace que la línea `my_inv([[1, 2], [3, 4]])` se ejecute sin errores."
msg4 = "¡Correcto! La palabra `as` te permite crear un nombre local para la función que estás importando: `inv()` ahora está disponible como `my_inv()`."
Ex().has_chosen(4, [msg1, msg2, msg3, msg4])
```

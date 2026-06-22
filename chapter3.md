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

De forma nativa, Python ofrece un montón de funciones integradas para hacerte la vida más fácil como científico de datos. Ya conoces dos de ellas: `print()` y `type()`. También hay funciones como `str()`, `int()`, `bool()` y `float()` para cambiar entre tipos de datos. Puedes obtener más información sobre ellas [aquí](https://docs.python.org/3/library/functions.html); todas estas también son funciones integradas.

Llamar a una función es fácil. Para obtener el tipo de `3.0` y guardar la salida como una nueva variable, `result`, puedes usar lo siguiente:

```
result = type(3.0)
```

`@instructions`
- Utiliza `print()` en combinación con `type()` para mostrar por pantalla el tipo de `var1`.
- Utiliza `len()` para obtener la [longitud de la lista](https://docs.python.org/3/library/functions.html#len) `var1`. Introdúcelo dentro de una llamada a `print()` para mostrar el resultado directamente por pantalla.
- Utiliza `int()` para convertir `var2` en un [entero](https://docs.python.org/3/library/functions.html#int). Guarda el resultado como `out2`.

`@hint`
- Llama a la función `type()` así: `type(var1)`.
- Llama a `print()` como lo has hecho tantas veces antes. Simplemente coloca la variable que quieres mostrar entre paréntesis.
- `int(x)` convertirá `x` a un entero.

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

Quizá ya conozcas el nombre de una función de Python, pero aún tienes que averiguar cómo usarla. Irónicamente, tienes que pedir información sobre una función con otra función: `help()`. En IPython específicamente, también puedes usar `?` antes del nombre de la función.

Para obtener ayuda sobre la función `max()`, por ejemplo, puedes usar una de estas llamadas:

```
help(max)
?max
```

Usa el shell de IPython para abrir la [documentación](https://docs.python.org/3/library/functions.html#pow) sobre `pow()`. Para ello, escribe `?pow` o `help(pow)` y pulsa **Intro**.

¿Cuál de las siguientes afirmaciones es verdadera?

`@possible_answers`
- `pow()` toma tres argumentos: `base`, `exp` y `mod`. Sin `mod`, la función devolverá un error.
- `pow()` toma tres argumentos obligatorios: `base`, `exp` y `None`.
- `pow()` requiere los argumentos `base` y `exp`; `mod` es opcional.
- `pow()` toma dos argumentos: `exp` y `mod`. La ausencia de `exp` provoca un error.

`@hint`
Los argumentos opcionales se establecen en `=` con respecto a un valor predeterminado, que la función utilizará si no se especifica ese argumento.

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

En el ejercicio anterior identificaste los argumentos opcionales consultando la documentación con `help()`. Ahora vas a aplicar esto mismo para cambiar el comportamiento de la función `sorted()`.

Consulta la [documentación](https://docs.python.org/3/library/functions.html#sorted) sobre `sorted()` escribiendo `help(sorted)` en el shell IPython.

Verás que `sorted()` admite tres argumentos: `iterable`, `key` y `reverse`. En este ejercicio solo tendrás que especificar `iterable` y `reverse`, no `key`.

Ya tienes dos listas creadas.

¿Podrías unirlas y ordenarlas en orden descendente?

`@instructions`
- Utiliza `+` para unir los elementos de `first` y `second` en una nueva lista: `full`.
- Llama a la función `sorted()` y en `full` especifica que el argumento `reverse` tiene que ser `True`. Guarda la lista ordenada con el nombre `full_sorted`.
- Para terminar, muestra `full_sorted` por pantalla.

`@hint`
- Suma `first` y `second` como si fueran dos números y asigna el resultado a `full`.
- Usa `sorted()` con dos entradas: `full` y `reverse=True`.
- Para mostrar una variable por pantalla, utiliza `print()`.

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

Las cadenas de texto (o strings) vienen con un buen número de métodos integrados. Sigue atentamente las instrucciones para descubrir algunos de ellos. Si quieres explorarlos con más detalle, siempre puedes escribir `help(str)` en el shell de IPython.

Ya se ha creado una cadena `place` para que experimentes con ella.

`@instructions`
- Usa el [método] `.upper()` (https://docs.python.org/3/library/stdtypes.html#str.upper) en `place` y guarda el resultado en `place_up`. Usa la sintaxis para llamar a métodos que aprendiste en el vídeo anterior.
- Muestra por pantalla `place` y `place_up`. ¿Han cambiado ambos?
- Muestra por pantalla el número de veces que aparece la letra «o» en la variable `place` llamando a `.count()` en `place` y pasando la letra `'o'` como entrada al método. ¡Nos referimos a la variable `place`, no de la palabra `"place"`!

`@hint`
- Puedes llamar al método `.upper()` en `place` sin necesidad de pasarle ningún argumento adicional.
- Para mostrar una variable `x` por pantalla, puedes escribir `print(x)`.
- Asegúrate de introducir tu llamada a `place.count(____)` dentro de una función `print()` para que se muestre por pantalla.

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

Las cadenas de texto no son los únicos tipos de datos en Python que tienen métodos asociados. Las listas, los decimales, los enteros y los booleanos también son tipos que traen de serie un buen puñado de métodos útiles. En este ejercicio vas a experimentar con:

- `.index()`, para obtener el índice del primer elemento de una lista que coincida con el argumento de entrada, y
- `.count()`, para obtener el número de veces que un elemento aparece en una lista.

Trabajarás con la lista que contiene el área de diferentes estancias de una casa: `areas`.

`@instructions`
- Utiliza el método `.index()` para obtener el índice del elemento de `areas` que sea igual a `20.0`. Muestra este índice en pantalla.
- Llama al método `.count()` en `areas` para averiguar cuántas veces aparece `9.50` en la lista. De nuevo, simplemente muestra este número por pantalla.

`@hint`
- Para mostrar el índice por pantalla, envuelve la llamada `areas.index(___)` en una función `print()`.
- Para mostrar el número de veces que un elemento `x` aparece en la lista, envuelve la llamada `areas.count(___)` en una función `print()`.

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

La mayoría de los métodos de listas cambiarán la lista sobre la que se llaman. Algunos ejemplos son:

- `.append()`, que añade un elemento a la lista sobre la que se llama,
- `.remove()`, que [elimina](https://docs.python.org/3/library/stdtypes.html#typesseq-mutable) el primer elemento de una lista que coincide con la entrada, y
- `.reverse()`, que [invierte](https://docs.python.org/3/library/stdtypes.html#typesseq-mutable) el orden de los elementos de la lista sobre la que se llama.

Trabajarás con la lista con el área de distintas partes de la casa: `areas`.

`@instructions`
- Usa `.append()` dos veces para volver a añadir el tamaño de la casa de la piscina y del garaje: `24.5` y `15.45`, respectivamente. Asegúrate de añadirlos en este orden.
- Muestra `areas` por pantalla.
- Usa el método `.reverse()` para invertir el orden de los elementos en `areas`.
- Muestra `areas` por pantalla una vez más.

`@hint`
- Para la primera instrucción, usa la llamada `areas.append(___)` dos veces.
- Para mostrar por pantalla una variable `x`, simplemente escribe `print(x)`.
- El método `.reverse()` no requiere entradas adicionales; solo usa la notación de punto y paréntesis vacíos: `.reverse()`.
- Para mostrar una variable `x`, simplemente escribe `print(x)`.

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

Digamos que quieres calcular la circunferencia y el área de un círculo. Así es como se ven esas fórmulas:

$$C = 2 \pi r$$
$$A = \pi r^2 $$

En lugar de escribir el número para `pi`, puedes usar el paquete `math` que contiene el número

Como referencia, `**` es el símbolo que se utiliza para la exponenciación. Por ejemplo, `3**4` es `3` elevado a `4` y dará `81`.

`@instructions`
- Importa el paquete `math`.
- Usa `math.pi` para calcular la circunferencia del círculo y guárdala en `C`.
- Usa `math.pi` para calcular el área del círculo y guárdala en `A`.

`@hint`
- Puedes simplemente usar `import math`, y luego referirte a `pi` con `math.pi`.
- Usa la ecuación del texto del ejercicio para encontrar `C`. Usa `*`
- Usa la ecuación del texto del ejercicio para encontrar `A`. Usa `*` y `**`.

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

Las importaciones generales, como `import math`, ponen a tu disposición **toda** la funcionalidad del paquete `math`. Sin embargo, si decides usar solo una parte específica de un paquete, siempre puedes hacer que tu importación sea más selectiva:

```
from math import pi
```

Intenta lo mismo otra vez, pero esta vez usa solo `pi`.

`@instructions`
- Realiza una importación selectiva del paquete `math` en la que solo importes la función `pi`.
- Usa `pi` para calcular la circunferencia del círculo y guárdala en `C`.
- Usa `pi` para calcular el área del círculo y guárdala en `A`.

`@hint`
- Utiliza `from math import pi` para realizar la importación selectiva.
- ¡Y ya está! ¡Ahora ya puedes usar `pi` por sí solo!

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

Existen varias formas de importar paquetes y módulos en Python. Dependiendo de cómo realices la importación, tendrás que utilizar un código de Python u otro.

Supón que quieres utilizar la [función](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.inv.html) `inv()`, que se encuentra en el subpaquete `linalg` del paquete `scipy`. Quieres poder utilizar esta función de la siguiente manera:

```
my_inv([[1,2], [3,4]])
```

¿Qué instrucción `import` necesitarás para poder ejecutar el código anterior sin que se produzca ningún error?

`@possible_answers`
- `import scipy`
- `import scipy.linalg`
- `from scipy.linalg import my_inv`
- `from scipy.linalg import inv as my_inv`

`@hint`
- Prueba las diferentes instrucciones de importación en el terminal IPython y mira cuál de ellas hace que la línea `my_inv([[1, 2], [3, 4]])` se ejecute sin errores. Pulsa **Intro** para ejecutar el código que hayas escrito.

`@pre_exercise_code`
```{python}

```

`@sct`
```{python}
msg1 = msg2 = msg3 = "Incorrecto, inténtalo de nuevo. Prueba las diferentes declaraciones de importación en la consola de IPython y ve cuál hace que la línea `my_inv([[1, 2], [3, 4]])` se ejecute sin errores."
msg4 = "¡Correcto! La palabra `as` te permite crear un nombre local para la función que estás importando: `inv()` ahora está disponible como `my_inv()`."
Ex().has_chosen(4, [msg1, msg2, msg3, msg4])
```

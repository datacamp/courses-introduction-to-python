---
title_meta: Capítulo 3
title: Funciones y Paquetes
description: >-
  Aprenderás a usar funciones, métodos y paquetes para aprovechar de manera
  eficiente el código que ya escrito por brillantes desarrolladores de Python.
  ¡El objetivo es reducir la cantidad de código necesario para resolver
  problemas desafiantes!
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

## Funciones comunes

```yaml
type: NormalExercise
key: c422ee929b
lang: python
xp: 100
skills:
  - 2
```

Python ofrece un montón de funciones integradas para facilitar tu trabajo como científico de datos. Ya conoces dos funciones de este tipo: [`print()`](https://docs.python.org/3/library/functions.html#print) y [`type()`](https://docs.python.org/3/library/functions.html#type). También has usado las funciones [`str()`](https://docs.python.org/3/library/functions.html#func-str), [`int()`](https://docs.python.org/3/library/functions.html#int), [`bool()`](https://docs.python.org/3/library/functions.html#bool) y [`float()`](https://docs.python.org/3/library/functions.html#float) para cambiar los tipos de datos. Estas también son funciones integradas.

Llamar a una función es sencillo. Para obtener el tipo de `3.0` y almacenar la salida como una nueva variable, `result`, podemos usar lo siguiente:

```
result = type(3.0)
```

La formula general para llamar funciones y guardar el resultado en una variable es:

```
output = function_name(input)
```

`@instructions`
- Usa [`print()`](https://docs.python.org/3/library/functions.html#print) en combinación con [`type()`](https://docs.python.org/3/library/functions.html#type) para imprimir el tipo de `var1`.
- Usa [`len()`](https://docs.python.org/3/library/functions.html#len) para obtener la longitud de la lista `var1`. Envuelve el resultado en una llamada a [`print()`](https://docs.python.org/3/library/functions.html#print) para imprimirlo directamente.
- Usa [`int()`](https://docs.python.org/3/library/functions.html#int) para convertir `var2` a un número entero. Almacena el resultado como `out2`.

`@hint`
- Llama a la función [`type()`](https://docs.python.org/3/library/functions.html#type) así: `type(var1)`.
- Llama [`a print()`](https://docs.python.org/3/library/functions.html#print) como lo hicimos tantas veces antes. Simplemente pon la variable que deseas imprimir entre paréntesis.
- `int(x)` convertirá a `x` en un número entero.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Crea las variables var1 y var2
var1 = [1, 2, 3, 4]
var2 = True

# Imprime el tipo de var1


# Imprime la longitud de var1


# Convierte var2 a un entero: var2

```

`@solution`
```{python}
# Crea las variables var1 y var2
var1 = [1, 2, 3, 4]
var2 = True

# Imprime el tipo de var1
print(type(var1))

# Imprime la longitud de var1
print(len(var1))

# Convierte var2 a un entero: var2
out2 = int(var2)
```

`@sct`
```{python}
msg = "No es necesario cambiar ni eliminar las variables predefinidas."
Ex().check_object("var1", missing_msg=msg).has_equal_value(incorrect_msg=msg)
Ex().check_object("var2", missing_msg=msg).has_equal_value(incorrect_msg=msg)

patt = "__JINJA__: asegúrate de imprimir el %s de `var1` con `{{sol_call}}`."
Ex().has_printout(0, not_printed_msg = patt % 'type')
Ex().has_printout(1, not_printed_msg = patt % 'length')

int_miss_msg = "¿Has usado [`int()`](https://docs.python.org/3/library/functions.html#int) para convertir `var2` en número entero?"
int_incorr_msg = "¿Has pasado `var2` a [`int()`](https://docs.python.org/3/library/functions.html#int)?"
Ex().check_correct(
  check_object("out2").has_equal_value(incorrect_msg="Llamaste a `int()` correctamente; ahora asegúrate de asignar el resultado a `out2`."),
  check_function("int", missing_msg=int_miss_msg).has_equal_value(incorrect_msg=int_incorr_msg)
)
success_msg("¡Genial! La función `len()` es extremadamente útil; ¡también funciona en cadenas para contar el número de caracteres!")
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

Tal vez ya conozcas el nombre de una función de Python, pero aún así tienes que descubrir cómo usarla. Irónicamente, debes solicitar información sobre una función con otra función: [`help()`](https://docs.python.org/3/library/functions.html#help). En IPython específicamente, también puedes usar `?` antes del nombre de la función.

Para obtener ayuda sobre la función [`max()`](https://docs.python.org/3/library/functions.html#max), por ejemplo, puedes usar una de estas llamadas:

```
help(max)
?max
```

Utiliza el IPython Shell para abrir la documentación sobre [`pow()`](https://docs.python.org/3/library/functions.html#pow). ¿Cuál de los siguientes enunciados es verdadero?

`@possible_answers`
- `pow()` toma tres argumentos: `base`, `exp` y `mod`. Si no especificas `mod`, la función devolverá un error.
- `pow()` toma tres argumentos: `base`, `exp` y `None`.  Todos estos argumentos son necesarios.
- `pow()` toma tres argumentos: `base`, `exp` y `mod`. `base` y `exp` son argumentos obligatorios, `mod` es un argumento opcional.
- `pow()` toma dos argumentos: `exp` y `mod`. Si no especificas `exp`, la función devolverá un error.

`@hint`
- Los argumentos opcionales se establecen `=` en un valor predeterminado, que la función usará si no se especifica ese argumento.

`@pre_exercise_code`
```{python}

```

`@sct`
```{python}
msg1 = "No exactamente. `mod` tiene un valor predeterminado que se usará si no especificas un valor."
msg2 = "Incorrecto. `None` es el valor predeterminado para el argumento `mod`."
msg3 = "¡Perfecto! Usando `help()` puedes comprender mejor cómo funcionan las funciones, liberando todo su potencial!"
msg4 = "Incorrecto. `pow()` toma tres argumentos, uno de los cuales tiene un valor predeterminado."
Ex().has_chosen(3, [msg1, msg2, msg3, msg4])
```

---

## Argumentos Múltiples

```yaml
type: NormalExercise
key: e30486d7c1
lang: python
xp: 100
skills:
  - 2
```

En el ejercicio anterior, identificamos argumentos opcionales al ver la documentación usando `help()`. Ahora aplicaremos este concepto para cambiar el comportamiento de la función `sorted()` .

Echa un vistazo a la documentación de [`sorted()`](https://docs.python.org/3/library/functions.html#sorted) escribiendo `help(sorted)` en el IPython Shell.

Verás que [`sorted()`](https://docs.python.org/3/library/functions.html#sorted) toma tres argumentos: `iterable`, `key` y `reverse`.

`key=None` significa que si no especificamos el argumento `key`, será `None`. `reverse=False` significa que si no especificamos el argumento `reverse`, será `False`de forma predeterminada.

En este ejercicio, solo tendrás que especificar `iterable` y `reverse`, no `key`. El primer argumento que pasemos a [`sorted()`](https://docs.python.org/3/library/functions.html#sorted) coincidirá con el argumento `iterable` , pero ¿qué pasa con el segundo argumento? Para decirle a Python que deseamos especificar `reverse` sin cambiar nada sobre `key`, puedes usar `=` para asignarle un nuevo valor:

```
sorted(____, reverse=____)
```

Se han creado dos listas para ti. ¿Puedes pegarlas y ordenarlas en orden descendente?

Nota: Por ahora, podemos decir que un [_iterable_](https://docs.python.org/3/glossary.html#term-iterable) es cualquier colección de objetos, por ejemplo, una Lista.

`@instructions`
- Usa `+` para fusionar los contenidos de `first` y `second` en una nueva lista: `full`.
- Llama a [`sorted()`](https://docs.python.org/3/library/functions.html#sorted) con `full` y especifica que el argumento `reverse` es `True`. Guarda la lista ordenada como `full_sorted`.
- Termina imprimiendo `full_sorted`.

`@hint`
- Suma `first` y `second` como si fueran dos números y asigna el resultado a `full`.
- Usa [`sorted()`](https://docs.python.org/3/library/functions.html#sorted) con dos argumentos: `full` y `reverse=True`.
- Para imprimir una variable, usa [`print()`](https://docs.python.org/3/library/functions.html#print).

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Crea las listas first y second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# Combina first y second: full


# Ordena full en orden descendente: full_sorted


# Imprime full_sorted

```

`@solution`
```{python}
# Crea las listas first y second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# Combina first y second: full
full = first + second

# Ordena full en orden descendente: full_sorted
full_sorted = sorted(full, reverse=True)

# Imprime full_sorted
print(full_sorted)
```

`@sct`
```{python}
msg = "No tienes que cambiar o eliminar las variables `first` y `second`ya existentes."
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

success_msg("Muy bien! Vamos al video sobre los métodos en Python.")
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

## Métodos de cadenas

```yaml
type: NormalExercise
key: 4039302ee0
lang: python
xp: 100
skills:
  - 2
```

Las cadenas(strings) cuentan con un montón de métodos. Sigue atentamente las instrucciones para descubrir algunos de ellos. Si deseas descubrirlos con más detalle, siempre puedes escribir `help(str)` en el IPython Shell.

Ya se ha creado una cadena `place` para que experimentes.

`@instructions`
- Usa el método [`upper()`](https://docs.python.org/3/library/stdtypes.html#str.upper) en `place` y almacena el resultado en `place_up`. Usa la sintaxis para llamar a los métodos que aprendimos en el video anterior.
- Imprime `place` y `place_up`. Ambos cambiaron?
- Imprime el número de veces que aparece la letra o en la variable `place` llamando a [`count()`](https://docs.python.org/3/library/stdtypes.html#str.count) con `place` y pasando la letra `'o'` como entrada al método. ¡Estamos hablando de la variable `place`, no de la palabra `"place"`!

`@hint`
- Puedes llamar al método [`upper()`](https://docs.python.org/3/library/stdtypes.html#str.upper) con `place` sin ningún argumento adicional.
- Para imprimir una variable `x`, puedes usar `print(x)`.
- Asegúrate de incluir tu llamada `place.count(____)` dentro de la función [`print()`](https://docs.python.org/3/library/functions.html#print) para que puedas imprimirla.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# cadena para experimentar con: place
place = "poolhouse"

# Usa upper() en place: place_up


# Imprime place y place_up


# Imprime el número de o en place

```

`@solution`
```{python}
# cadena para experimentar con: place
place = "poolhouse"

# Usa upper() en place: place_up
place_up = place.upper()

# Imprime place y place_up
print(place)
print(place_up)

# Imprime el número de o en place
print(place.count('o'))
```

`@sct`
```{python}
msg = "No es necesario cambiar ni eliminar las variables predefinidas."
Ex().check_object("place", missing_msg=msg).has_equal_value(incorrect_msg=msg)

patt = "No olvides imprimir `%s`."
Ex().has_printout(0, not_printed_msg=patt % "place")
Ex().check_correct(
    has_printout(1, not_printed_msg=patt % "place_up"),
    check_correct(
        check_object("place_up").has_equal_value(incorrect_msg="Asigna el resultado de tu llamada a `place.upper()` a `place_up`."),
        check_function("place.upper", signature=False)
    )
)    

# check count of place
Ex().check_correct(
  has_printout(2, not_printed_msg = "Has calculado bien el número de veces que aparece la letra o en `place`; ahora asegúrate de envolver la llamada `place.count('o')` en `print()` para imprimir el resultado.")
  check_function("place.count", signature=False).check_args(0).has_equal_value()
)

success_msg("Muy bien! Observa en las impresiones que el método [upper()](https://docs.python.org/3/library/stdtypes.html#str.upper) no cambia el objeto con el que se llama. ¡Esto será diferente con las listas del próximo ejercicio!")
```

---

## Métodos de listas

```yaml
type: NormalExercise
key: 0dbe8ed695
lang: python
xp: 100
skills:
  - 2
```

Las cadenas no son los únicos tipos de Python que tienen métodos asociados. Las listas, los flotantes, los enteros y los booleanos también son tipos que tienen un montón de métodos útiles. En este ejercicio, experimentarás con:

- [`index()`](https://docs.python.org/3/library/stdtypes.html#str.index), para obtener el índice del primer elemento de una lista que coincide con su entrada y
- [`count()`](https://docs.python.org/3/library/stdtypes.html#str.count), para obtener el número de veces que aparece un elemento en una lista.

Estarás trabajando en la lista con el área de diferentes partes de una casa: `areas`.

`@instructions`
- Usa el método [`index()`](https://docs.python.org/3/library/stdtypes.html#str.index) para obtener el índice del elemento en `areas` que es igual a `20.0`. Imprime este índice.
- Llama a [`count()`](https://docs.python.org/3/library/stdtypes.html#str.count) con `areas` para averiguar cuántas veces aparece `9.50` en la lista. Nuevamente, simplemente imprima este número.

`@hint`
- Para imprimir el índice, envuelve la llamada `areas.index(___)` en una función [`print()`](https://docs.python.org/3/library/functions.html#print) .
- Para imprimir el número de veces que aparece un elemento `x` en la lista, envuelve la llamada `areas.count(___)` en una función [`print()`](https://docs.python.org/3/library/functions.html#print) .

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Crea la lista areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Imprime el índice del elemento 20.0


# Imprime con qué frecuencia aparece 9.50 en areas


```

`@solution`
```{python}
# Crea la lista areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Imprime el índice del elemento 20.0
print(areas.index(20.0))

# Imprime con qué frecuencia aparece 9.50 en areas
print(areas.count(9.50))
```

`@sct`
```{python}
predef_msg = "No es necesario cambiar ni eliminar las variables predefinidas."

Ex().check_object("areas", missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg)

Ex().check_function("print", index=0).check_args(0).check_function('areas.index', signature=False).check_args(0).has_equal_value()


Ex().check_function("print", index=1).check_args(0).check_function('areas.count', signature=False).has_equal_value()

success_msg("Muy bien! Estos fueron ejemplos de métodos de `listas` que no cambiaron la lista sobre la que fueron llamados.")
```

---

## Métodos de listas (2)

```yaml
type: NormalExercise
key: 1fbeab82d0
lang: python
xp: 100
skills:
  - 2
```

La mayoría de los métodos de lista cambiarán la lista con la que se les llama. Los ejemplos son:

- [`append()`](https://docs.python.org/3/library/stdtypes.html#typesseq-mutable), que agrega un elemento a la lista con la que se llama,
- [`remove()`](https://docs.python.org/3/library/stdtypes.html#typesseq-mutable), que elimina el primer elemento de la lista que coincide con la entrada, y
- [`reverse()`](https://docs.python.org/3/library/stdtypes.html#typesseq-mutable), que invierte el orden de los elementos en la lista con la que se llama.

Estarás trabajando en la lista con el área de diferentes partes de la casa: `areas`.

`@instructions`
- Usa [`append()`](https://docs.python.org/3/library/stdtypes.html#typesseq-mutable) dos veces para agregar el tamaño de la casa de la piscina y el garaje nuevamente: `24.5` y `15.45`, respectivamente. Asegúrate de agregarlos en este orden.
- Imprime`areas`
- Utiliza el método [`reverse()`](https://docs.python.org/3/library/stdtypes.html#typesseq-mutable) para invertir el orden de los elementos en `areas`.
- Imprime `areas` una vez más.

`@hint`
- Para la primera instrucción, usa la llamada `areas.append(___)` dos veces.
- Para imprimir una variable `x`, simplemente escribe `print(x)`.
- El método [`reverse()`](https://docs.python.org/3/library/stdtypes.html#typesseq-mutable) no requiere entradas adicionales; simplemente usa la notación de punto (dot notation) y paréntesis vacíos: `.reverse()`.
- Para imprimir una variable `x`, simplemente escribe `print(x)`.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Crea la lista areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Usa append dos veces para agregar el tamaño de la casa de la piscina y el garaje



# Imprime areas


# Invierte el orden de los elementos en areas


# Imprime areas
```

`@solution`
```{python}
# Crea la lista areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Usa append dos veces para agregar el tamaño de la casa de la piscina y el garaje
areas.append(24.5)
areas.append(15.45)

# Imprime areas
print(areas)

# Invierte el orden de los elementos en areas
areas.reverse()

# Imprime areas
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

## Importando paquetes

```yaml
type: NormalExercise
key: 7432a6376f
lang: python
xp: 100
skills:
  - 2
```

Como científico de datos, algunas nociones de geometría nunca están de más. Vamos a refrescar algunos de los conceptos básicos.

Para un elegante algoritmo de agrupamiento, deseas encontrar la circunferencia, $C$, y el área, $A$, de un círculo. Cuando el radio del círculo es `r`, puedes calcular $C$ y $A$ como:

$$C = 2 \pi r$$
$$A = \pi r^2 $$

Para usar la constante `pi`, necesitaremos el paquete `math`. La variable `r` ya está codificada en el script. Completa el código para calcular `C` y `A` y ve cómo las función [`print()`](https://docs.python.org/3/library/functions.html#print) crea buenas impresiones.

`@instructions`
- Importa el paquete `math`. Ahora puedes accesar la constante `pi` usando `math.pi.`
- Calcula la circunferencia del círculo y guárdala en `C.`
- Calcula el área del círculo y guárdala en `A`.

`@hint`
- Simplemente puedes usar `import math`y luego referirte a `pi` con `math.pi`.
- Usa la ecuación en el texto para encontrar `C`. Usa `*`
- Usa la ecuación en el texto de la tarea para encontrar `A`. Usa `*` y `**`.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Importa el paquete math


# Definición de radio
r = 0.43

# Calcula C
C = 0

# Calcula A
A = 0

# Imprime
print("Circunferencia: " + str(C))
print("Area: " + str(A))
```

`@solution`
```{python}
# Importa el paquete math
import math

# Definición de radio
r = 0.43

# Calcula C
C = 2 * r * math.pi

# Calcula A
A = math.pi * r ** 2

# Imprime
print("Circunferencia: " + str(C))
print("Area: " + str(A))
```

`@sct`
```{python}
msg = "No es necesario cambiar ni eliminar las variables predefinidas."
patt = "Tu cálculo de `%s` no es correcto. Asegúrate de usar `math.pi`."
Ex().multi(
  check_object('r', missing_msg=msg).has_equal_value(incorrect_msg=msg),
  has_import('math', same_as=False),
  check_object('C').has_equal_value(incorrect_msg=patt%'C'),
  check_object('A').has_equal_value(incorrect_msg=patt%'A')
)

Ex().multi(
  has_printout(0, not_printed_msg = "__JINJA__:Mantén `{{sol_call}}` ahí para imprimir la circunferencia."),
  has_printout(1, not_printed_msg = "__JINJA__:Mantén `{{sol_call}}` ahí para imprimir el área.")
)

success_msg("Muy bien! Si sabes cómo manejar las funciones de los paquetes, ¡el poder de _muchos_ programadores de Python está al alcance de tu mano!")
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

Las importaciones generales, como `import math`, ponen a tu disposición **todas** las funciones del paquete `math`. Sin embargo, si decides usar solo una parte específica de un paquete, siempre puedes hacer que tu importación sea más selectiva:

```
from math import pi
```

Digamos que la órbita de la Luna alrededor del planeta Tierra es un círculo perfecto, con un radio `r` (en km) que se define en el script.

`@instructions`
- Realiza una importación selectiva desde el paquete `math` donde solo importas la función `radians` .
- Calcula la distancia recorrida por la Luna en 12 grados de su órbita. Asigna el resultado a `dist`. Puedes calcular esto como `r * phi`, donde `r` es el radio y `phi` es el ángulo en radianes. Para convertir un ángulo en grados a un ángulo en radianes, usa la función [`radians()`](https://docs.python.org/3/library/math.html#math.radians), que acabas de importar.
- Imprime `dist`.

`@hint`
- Usa `from math import radians` para hacer la importación selectiva.
- Y ya con eso puedes usar la función [`radians()`](https://docs.python.org/3/library/math.html#math.radians). Pasa a la función el número 12 para obtener el ángulo en radianes.
- Para imprimir una variable `x`, simplemente escribe `print(x)`.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Importa radians del paquete math


# Definición de radio
r = 192500

# Distancia de viaje de la Luna sobre 12 grados. Guárdala en dist.


# Imprime dist

```

`@solution`
```{python}
# Importa radians del paquete math
from math import radians

# Definición de radio
r = 192500

# Distancia de viaje de la Luna sobre 12 grados. Guárdala en dist.
dist = r * radians(12)

# Imprime dist
print(dist)
```

`@sct`
```{python}
msg = "No es necesario cambiar ni eliminar las variables predefinidas."
Ex().check_object("r", missing_msg=msg).has_equal_value(incorrect_msg=msg)

Ex().has_import("math.radians", not_imported_msg = "Asegúrate de importar [`radians()`](https://docs.python.org/3/library/math.html#math.radians) del paquete `math`. Debes utilizar la notación `from ___ import ___`.", correct_as_msg = "No establezcas ningún alias para [`radians()`](https://docs.python.org/3/library/math.html#math.radians). Simplemente escribe `from math import radians`.")

Ex().check_correct(
  check_object("dist").has_equal_value(),
  check_function("math.radians", signature=False).check_args(0).has_equal_value()
)

Ex().has_printout(0)

success_msg("Muy bien! Vamos al siguiente ejercicio.")
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

Hay varias formas de importar paquetes y módulos en Python. Dependiendo del tipo de importación, deberás usar un código de Python diferente.

Supón que deseas utilizar la función [`inv()`](http://docs.scipy.org/doc/numpy-1.10.0/reference/generated/numpy.linalg.inv.html), que se encuentra en el subpaquete `linalg` del paquete `scipy`. Deseas poder utilizar esta función de la siguiente manera:

```
my_inv([[1,2], [3,4]])
```

¿Qué declaración `de importación` se necesita para ejecutar el código anterior sin error?

`@possible_answers`
- `import scipy`
- `import scipy.linalg`
- `from scipy.linalg import my_inv`
- `from scipy.linalg import inv as my_inv`

`@hint`
Prueba las diferentes declaraciones de importación en el shell de IPython y ve cuál hace que la línea `my_inv([[1, 2], [3, 4]])` se ejecute sin errores.

`@pre_exercise_code`
```{python}

```

`@sct`
```{python}
msg1 = msg2 = msg3 = "Incorrecto, intenta nuevamente. Prueba las diferentes declaraciones de importación en el shell de IPython y ve cuál hace que la línea `my_inv([[1, 2], [3, 4]])` se ejecute sin errores."
msg4 = "¡Correcto! La palabra `as` te permite crear un nombre local para la función que estás importando: `inv()` ahora está disponible como `my_inv()`."
Ex().has_chosen(4, [msg1, msg2, msg3, msg4])
```

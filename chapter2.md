---
title_meta: Capítulo 2
title: Listas Python
description: >-
  Aprende a almacenar datos en listas, acceder a ellos y manipularlos, el primer
  paso para trabajar con eficiencia con grandes cantidades de datos.
attachments:
  slides_link: 'https://projector-video-pdf-converter.datacamp.com/735/chapter2.pdf'
lessons:
  - nb_of_exercises: 4
    title: Listas Python
  - nb_of_exercises: 4
    title: Crear subconjuntos de listas
  - nb_of_exercises: 5
    title: Manipular listas
---

## Listas Python

```yaml
type: VideoExercise
key: a5886d213f
xp: 50
```

`@projector_key`
a0530c4542f10988847b2dbb91f717c3

---

## Crear una lista

```yaml
type: NormalExercise
key: e6c527bf41
lang: python
xp: 100
skills:
  - 2
```

Una lista es un **tipo de datos compuesto**; puedes agrupar valores, así:

```
a = "is"
b = "nice"
my_list = ["my", "list", a, b]
```

Después de medir la estatura de tu familia, decides recopilar información sobre la casa en la que vives. Las superficies de las distintas partes de tu casa se almacenan en variables separadas en el ejercicio.

`@instructions`
- Crea una lista, `areas`, que contenga el área del vestíbulo (`hall`), la cocina (`kit`), el cuarto de estar (`liv`), el dormitorio (`bed`) y el cuarto de baño (`bath`), en este orden. Utiliza las variables predefinidas.
- Imprime `areas` con la función `print()`.

`@hint`
- Puedes utilizar las variables ya creadas para construir la lista: `areas = [hall, kit, ...]`.
- Asegúrate de utilizar corchetes, `[]`, en lugar de paréntesis, `()`.
- No necesitas utilizar comillas cuando almacenes variables en una lista.
- Escribe `print(areas)` para imprimir la lista al enviarla.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Create list areas


# Print areas

```

`@solution`
```{python}
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Create list areas
areas = [hall, kit, liv, bed, bath]

# Print areas
print(areas)
```

`@sct`
```{python}
predef_msg = "¡No elimines ni edites las variables predefinidas!"
areas_msg = "Define `areas` como la lista que contiene todas las variables de área, en el orden correcto: `[hall, kit, liv, bed, bath]`. Cuidado con los errores tipográficos. ¡La lista no debería contener nada más!"

Ex().check_correct(
    has_printout(0, not_printed_msg = "__JINJA__:¿Has usado `{{sol_call}}` para imprimir la lista `areas` al final de tu script?"),
    check_correct(
        check_object("areas").has_equal_value(incorrect_msg = areas_msg),
        multi(
            check_object('hall', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
            check_object('kit', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
            check_object('liv', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
            check_object('bed', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
            check_object('bath', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg)
        )
    )
)

success_msg("¡Bien hecho! Una lista es mucho mejor aquí, ¿verdad?")
```

---

## Crear listas con diferentes tipos

```yaml
type: NormalExercise
key: 1702a8bcdc
lang: python
xp: 100
skills:
  - 2
```

Aunque no es muy habitual, una lista también puede contener una mezcla de tipos de Python, como cadenas, flotantes y booleanos.

Ahora vas a añadir los nombres de las habitaciones a tu lista, para que puedas ver fácilmente el nombre y el tamaño de la habitación juntos.

Se te ha proporcionado parte del código para que puedas empezar. ¡Presta atención aquí! `"bathroom"` es una cadena, mientras que `bath` es una variable que representa el flotante `9.50` que especificaste antes.

`@instructions`
- Termina el código que crea la lista `areas`. Construye la lista de modo que contenga primero el nombre de cada habitación como cadena y luego su superficie. En otras palabras, añade las cadenas `"hallway"`, `"kitchen"` y `"bedroom"` en los lugares adecuados.
- Vuelve a imprimir `areas`; ¿la impresión es esta vez más informativa?

`@hint`
- Los cuatro primeros elementos de la lista `areas` se programan como `["hallway", hall, "kitchen", kit, ...`.
- Una cadena tendrá que ir entre comillas, `""`.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Adapt list areas
areas = [____, hall, ____, kit, "living room", liv, ____, bed, "bathroom", bath]

# Print areas
____
```

`@solution`
```{python}
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Adapt list areas
areas = ["hallway", hall, "kitchen", kit, "living room", liv, "bedroom", bed, "bathroom", bath]

# Print areas
print(areas)
```

`@sct`
```{python}
objs = ["hall", "kit", "liv", "bed", "bath"]
predef_msg = "¡No elimines ni edites las variables predefinidas!"
areas_msg = "No asignaste el valor correcto a `areas`. Revisa las instrucciones nuevamente. Asegúrate de colocar el nombre de la habitación antes de la variable que contiene el área cada vez. ¡El orden importa aquí! Ten cuidado con los errores tipográficos."

Ex().check_correct(
  check_object("areas").has_equal_value(incorrect_msg = areas_msg),
  multi([ check_object(obj, missing_msg = predef_msg).has_equal_value(incorrect_msg = predef_msg) for obj in objs])
)

Ex().has_printout(0, not_printed_msg = "__JINJA__:¿Has usado `{{sol_call}}` para imprimir la lista `areas` al final de tu script?")

success_msg("¡Bien hecho! Esta lista contiene tanto cadenas como números decimales, pero eso no es un problema para Python.")
```

---

## Lista de listas

```yaml
type: NormalExercise
key: 9158c577b0
lang: python
xp: 100
skills:
  - 2
```

Como científico de datos, a menudo tratarás con muchos datos, y tendrá sentido agrupar algunos de estos datos.

En lugar de crear una lista que contenga cadenas y flotantes que representen los nombres y las superficies de las habitaciones de tu casa, puedes crear una lista de listas.

Recuerda: `"hallway"` es una cadena, mientras que `hall` es una variable que representa el flotante `11.25` que especificaste antes.

`@instructions`
- Termina la lista de listas para que contenga también los datos del dormitorio y del cuarto de baño. ¡Asegúrate de introducirlos en orden!
- Imprime `house`; ¿tiene más sentido esta forma de estructurar tus datos?

`@hint`
- Añade _sublistas_ a la lista `house` añadiendo `["bedroom", bed]` y `["bathroom", bath]` dentro de los corchetes.
- Recuerda incluir una coma, `,`, después de cada sublista.
- Para imprimir una variable `x`, escribe `print(x)` en una nueva línea.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# House information as list of lists
house = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv],
        ____,
        ____]

# Print out house
____
```

`@solution`
```{python}
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# House information as list of lists
house = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv],
         ["bedroom", bed],
         ["bathroom", bath]]

# Print out house
print(house)
```

`@sct`
```{python}
predef_msg = "¡No elimines ni edites las variables predefinidas!"
house_msg = "No asignaste el valor correcto a `house`. Revisa las instrucciones nuevamente. Extiende la lista de listas para que incorpore una lista para cada par de nombre de habitación y área de habitación. ¡Presta atención al orden y a los errores tipográficos!"

Ex().check_correct(
    check_object("house").has_equal_value(incorrect_msg = house_msg),
    multi(
        check_object('hall', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
        check_object('kit', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
        check_object('liv', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
        check_object('bed', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
        check_object('bath', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg)
    )
)

Ex().has_printout(0, not_printed_msg = "__JINJA__:¿Has usado `{{sol_call}}` para imprimir el contenido de `house`?")

success_msg("¡Genial! ¡Prepárate para aprender sobre la indexación de listas!")
```

---

## Crear subconjuntos de listas

```yaml
type: VideoExercise
key: c076b5a69c
xp: 50
```

`@projector_key`
fc15ba5cb9485456df8589130b519ea3

---

## Crea subconjuntos y vencerás

```yaml
type: NormalExercise
key: c3ce582e32
lang: python
xp: 100
skills:
  - 2
```

Crear subconjuntos de listas de Python es pan comido. Observa el ejemplo de código siguiente, que crea una lista `x` y luego selecciona "b" en ella. Recuerda que este es el segundo elemento, por lo que tiene el índice 1. También puedes utilizar la indexación negativa.

```
x = ["a", "b", "c", "d"]
x[1]
x[-3] # same result!
```

¿Recuerdas la lista `areas` de antes, que contenía tanto cadenas como flotantes? Su definición ya está en el script. ¿Puedes añadir el código correcto para crear subconjuntos de Python?

`@instructions`
- Imprime el segundo elemento de la lista `areas` (tiene el valor `11.25`).
- Crea subconjuntos e imprime el último elemento de `areas`, que es `9.50`. ¡Utilizar un índice negativo tiene sentido en este caso!
- Selecciona el número que representa la superficie del cuarto de estar (`20.0`) e imprímelo.

`@hint`
- Utiliza `x[1]` para seleccionar el segundo elemento de una lista `x`.
- Utiliza `x[-1]` para seleccionar el último elemento de una lista `x`.
- Asegúrate de escribir tus operaciones de creación de subconjuntos en una llamada a `print()`.
- El número que representa la superficie del cuarto de estar es el 6.º elemento de la lista, así que aquí necesitarás `[5]`. ¡`area[4]` mostraría la cadena!

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Print out second element from areas
print(areas[____])

# Print out last element from areas
print(areas[____])

# Print out the area of the living room
print(areas[____])
```

`@solution`
```{python}
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Print out second element from areas
print(areas[1])

# Print out last element from areas
print(areas[-1])

# Print out the area of the living room
print(areas[5])
```

`@sct`
```{python}
msg = "No elimines ni edites la lista `areas` predefinida."
Ex().check_object("areas", missing_msg = msg).has_equal_value(incorrect_msg = msg)
Ex().has_printout(0, not_printed_msg = "Revisa tu código para imprimir el segundo elemento en `areas`, que está en el índice `1`.")
Ex().has_printout(1, not_printed_msg = "Revisa tu código para imprimir el último elemento en `areas`, que está en el índice `-1`.")
Ex().has_printout(2, not_printed_msg = "Revisa tu código para imprimir el área de la sala de estar. Está en el índice `5`.")
success_msg("¡Buen trabajo!")
```

---

## Slices

```yaml
type: NormalExercise
key: 7f08642d18
lang: python
xp: 100
skills:
  - 2
```

Seleccionar valores individuales de una lista es solo parte de la historia. También es posible usar _slices_ en tu lista, lo que significa seleccionar varios elementos de tu lista. Utiliza la siguiente sintaxis:

```
my_list[start:end]
```

El índice `start` se incluirá, mientras que el índice `end` _no_. Sin embargo, también es posible no especificar estos índices. Si no especificas el índice `start`, Python deduce que quieres empezar el slice al principio de la lista.

`@instructions`
- Usa slices para crear una lista, `downstairs`, que contenga los 6 primeros elementos de `areas`.
- Crea `upstairs`, que consiste en los últimos `4` elementos de `areas`. Esta vez, simplifica los slices omitiendo el índice `end`.
- Imprime tanto `downstairs` como `upstairs` utilizando `print()`.

`@hint`
- Utiliza los corchetes `[0:6]` para obtener los seis primeros elementos de una lista.
- Para obtener todo excepto los 5 primeros elementos de una lista, `l`, utilizarías `l[5:]`.
- Añade dos llamadas a `print()` para imprimir `downstairs` y `upstairs`.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Use slicing to create downstairs
downstairs = areas[____]

# Use slicing to create upstairs
upstairs = areas[____]

# Print out downstairs and upstairs
____
____
```

`@solution`
```{python}
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Use slicing to create downstairs
downstairs = areas[0:6]

# Use slicing to create upstairs
upstairs = areas[6:]

# Print out downstairs and upstairs
print(downstairs)
print(upstairs)
```

`@sct`
```{python}
msg = "No elimines ni edites la lista `areas` predefinida."
Ex().check_object("areas", missing_msg = msg).has_equal_value(incorrect_msg = msg)

patt = "`%s` es incorrecto. Usa `areas[%s]` y el corte para seleccionar los elementos que quieres, o algo equivalente."
Ex().check_object("downstairs").has_equal_value(incorrect_msg = patt % ('downstairs', '0:6'))
Ex().check_object("upstairs").has_equal_value(incorrect_msg = patt % ("upstairs",":6"))

Ex().has_printout(0, not_printed_msg="¿Has impreso `downstairs` después de calcularlo?")
Ex().has_printout(1, not_printed_msg="¿Has impreso `upstairs` después de calcularlo?")

success_msg("¡Genial!")
```

---

## Crear subconjuntos de listas de listas

```yaml
type: NormalExercise
key: dbbbd306cf
xp: 100
```

Una lista Python también puede contener otras listas.

Para crear subconjuntos de listas de listas, puedes utilizar la misma técnica que antes: los corchetes. Esto sería algo así para una lista, `house`:

```
house[2][0]
```

`@instructions`
- Crea subconjuntos de la lista `house` para obtener el flotante `9.5`.

`@hint`
- Desglosa esto paso a paso. Primero quieres llegar al último elemento de la lista, `["bathroom", 9.50]`. Recuerda que el índice del último elemento es `-1`.
- A continuación, quieres obtener el segundo elemento de `["bathroom", 9.50]`, que está en el índice `1`.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
house = [["hallway", 11.25],
         ["kitchen", 18.0],
         ["living room", 20.0],
         ["bedroom", 10.75],
         ["bathroom", 9.50]]

# Subset the house list
house___
```

`@solution`
```{python}
house = [["hallway", 11.25],
         ["kitchen", 18.0],
         ["living room", 20.0],
         ["bedroom", 10.75],
         ["bathroom", 9.50]]

# Subset the house list
house[-1][1]
```

`@sct`
```{python}
Ex().check_or(
  has_code("house[-1][1]", pattern=False),
  has_code("house[4][1]", pattern=False)
)

success_msg("¡Correctomundo! La última pieza del rompecabezas de la lista es la manipulación.")
```

---

## Manipular listas

```yaml
type: VideoExercise
key: d7fe818b3a
xp: 50
```

`@projector_key`
355ed52d2fb0d67508c6a311b7cbc6d3

---

## Sustituir elementos de la lista

```yaml
type: NormalExercise
key: 4e1bba1b55
lang: python
xp: 100
skills:
  - 2
```

Para sustituir elementos de la lista, debes crear subconjuntos de la lista y asignar nuevos valores a los subconjuntos. Puedes seleccionar elementos sueltos o cambiar slices enteros de la lista a la vez.

En este ejercicio y en los siguientes, seguirás trabajando con la lista `areas` que contiene los nombres y las superficies de las distintas habitaciones de una casa.

`@instructions`
- Actualiza la superficie del cuarto de baño para que sea `10.50` metros cuadrados en lugar de `9.50`. Para ello, utiliza la indexación negativa.
- ¡Haz la lista `areas` más actual! Cambia `"living room"` por `"chill zone"`. Esta vez no utilices la indexación negativa.

`@hint`
- Para actualizar la superficie del cuarto de baño, identifica el subconjunto de la superficie del cuarto de baño (¡es el último elemento de la lista!).
- A continuación, sustituye el valor por la nueva superficie del cuarto de baño asignándola a este subconjunto.
- Haz lo mismo para actualizar el nombre `"living room"`, que está en el índice 4.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Correct the bathroom area


# Change "living room" to "chill zone"

```

`@solution`
```{python}
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Correct the bathroom area
areas[-1] = 10.50

# Change "living room" to "chill zone"
areas[4] = "chill zone"
```

`@sct`
```{python}
bathroom_msg = 'Puedes usar `areas[-1] = 10.50` para actualizar el área del baño.'
chillzone_msg = 'Puedes usar `areas[4] = "chill zone"` para actualizar el nombre de la sala de estar.'
Ex().check_correct(
  check_object('areas').has_equal_value(incorrect_msg = 'Tus cambios a `areas` no resultaron en la lista correcta. ¿Estás seguro de que usaste las operaciones de subconjunto correctas? ¡Cuando tengas dudas, puedes usar una pista!'),
  multi(
    has_equal_value(expr_code='areas[-1]', override=10.50, incorrect_msg = bathroom_msg),
    has_equal_value(expr_code='areas[4]', override='chill zone', incorrect_msg = chillzone_msg),
  )
)
success_msg('¡Genial! Como mostró el ejemplo de código, también puedes cortar una lista y reemplazarla con otra lista para actualizar múltiples elementos en un solo comando.')
```

---

## Ampliar una lista

```yaml
type: NormalExercise
key: ff0fe8d967
lang: python
xp: 100
skills:
  - 2
```

Si puedes cambiar elementos de una lista, seguro que quieres poder añadirle elementos, ¿no? Puedes utilizar el operador `+`:

```
x = ["a", "b", "c", "d"]
y = x + ["e", "f"]
```

Acabas de ganar la lotería, ¡impresionante! Decides construir una caseta de piscina y un garaje. ¿Puedes añadir la información a la lista `areas`?

`@instructions`
- Utiliza el operador `+` para pegar la lista `["poolhouse", 24.5]` al final de la lista `areas`. Guarda la lista resultante como `areas_1`.
- Amplía aún más `areas_1` añadiendo datos sobre tu garaje. Añade la cadena `"garage"` y el flotante `15.45`. Llama `areas_2` a la lista resultante.

`@hint`
- Sigue el ejemplo de código de la tarea. `x` es aquí `areas`, y `["e", "f"]` es `["poolhouse", 24.5]`.
- Para añadir más elementos a `areas_1`, utiliza `areas_1 + ["element", 123]`.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create the areas list and make some changes
areas = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0,
         "bedroom", 10.75, "bathroom", 10.50]

# Add poolhouse data to areas, new list is areas_1
areas_1 = ____

# Add garage data to areas_1, new list is areas_2
areas_2 = ____
```

`@solution`
```{python}
# Create the areas list (updated version)
areas = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0,
         "bedroom", 10.75, "bathroom", 10.50]

# Add poolhouse data to areas, new list is areas_1
areas_1 = areas + ["poolhouse", 24.5]

# Add garage data to areas_1, new list is areas_2
areas_2 = areas_1 + ["garage", 15.45]
```

`@sct`
```{python}
msg = "No elimines ni edites la lista `areas` predefinida."
Ex().check_object("areas", missing_msg = msg).has_equal_value(incorrect_msg = msg)
Ex().check_object("areas_1").has_equal_value(incorrect_msg = "Usa `areas + [\"poolhouse\", 24.5]` para crear `areas_1`. ¡Cuidado con los errores tipográficos!")
Ex().check_object("areas_2").has_equal_value(incorrect_msg = "Usa `areas_1 + [\"garage\", 15.45]` para crear `areas_2`. ¡Cuidado con los errores tipográficos!")
success_msg("¡Genial! ¡La lista está tomando forma!")
```

---

## Eliminar elementos de la lista

```yaml
type: NormalExercise
key: 85f792356e
xp: 100
```

Por último, también puedes eliminar elementos de tu lista. Puedes hacerlo con la declaración `del`:

```
x = ["a", "b", "c", "d"]
del x[1]
```

Presta atención: en cuanto eliminas un elemento de una lista, cambian todos los índices de los elementos que vienen después del elemento eliminado.

Por desgracia, la cantidad que ganaste con la lotería no es tan grande y parece que no se va a hacer la caseta de piscina. Tendrás que eliminarla de la lista. Decides eliminar la cadena y el flotante correspondientes de la lista `areas`.

`@instructions`
- Elimina la cadena y el flotante correspondientes a `"poolhouse"` de tu lista `areas`.
- Imprime la lista `areas` actualizada.

`@hint`
- Tendrás que utilizar `del` dos veces para eliminar dos elementos. Sin embargo, ¡ten cuidado con el cambio de índices!

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
areas = ["hallway", 11.25, "kitchen", 18.0,
        "chill zone", 20.0, "bedroom", 10.75,
         "bathroom", 10.50, "poolhouse", 24.5,
         "garage", 15.45]

# Delete the poolhouse items from the list


# Print the updated list

```

`@solution`
```{python}
areas = ["hallway", 11.25, "kitchen", 18.0,
        "chill zone", 20.0, "bedroom", 10.75,
         "bathroom", 10.50, "poolhouse", 24.5,
         "garage", 15.45]

# Delete the poolhouse items from the list
del areas[10]
del areas[10]

# Print the updated list
print(areas)
```

`@sct`
```{python}
Ex().check_or(
  multi(
    has_code("del areas[10]", pattern=False),
    has_code("del areas[10]", pattern=False)
  ),
  has_code("del areas[-4:-2]", pattern=False),
  has_code("del(areas[-4:-2])", pattern=False),
  multi(
    has_code("del(areas[10])", pattern=False),
    has_code("del(areas[10])", pattern=False)
  ),
  has_code("del areas[10:12]", pattern=False),
  has_code("del(areas[10:12])", pattern=False),
  multi(
    has_code("del areas[-4]", pattern=False),
    has_code("del areas[-3]", pattern=False)
  ),
  multi(
    has_code("del(areas[-4])", pattern=False),
    has_code("del(areas[-3])", pattern=False)
  )
)

Ex().has_printout(0, not_printed_msg="¿Has impreso `areas` después de eliminar la cadena y el flotante de poolhouse?")
success_msg("¡Correcto! Más adelante aprenderás formas más fáciles de eliminar elementos específicos de las listas en Python.")
```

---

## Funcionamiento interno de las listas

```yaml
type: NormalExercise
key: af72db9915
lang: python
xp: 100
skills:
  - 2
```

En este ejercicio se te ha proporcionado algo de código, una lista con el nombre `areas` y una copia llamada `areas_copy`.

Actualmente se cambia el primer elemento de la lista `areas_copy` y se imprime la lista `areas`. Si pulsas el botón de ejecución de código verás que, aunque has cambiado `areas_copy`, el cambio también se aplica a la lista `areas`. Eso es porque `areas` y `areas_copy` apuntan a la misma lista.

Si quieres impedir que los cambios de `areas_copy` también se apliquen en `areas`, tendrás que hacer una copia más explícita de la lista `areas` con `list()` o utilizando `[:]`.

`@instructions`
- Cambia el segundo comando, que crea la variable `areas_copy`, de forma que `areas_copy` sea una copia explícita de `areas`. Después de tu edición, los cambios realizados en `areas_copy` no deben afectar a `areas`. Envía la respuesta para comprobarlo.

`@hint`
- Cambia la llamada a `areas_copy = areas`. En lugar de asignar `areas`, puedes asignar `list(areas)` o `areas[:]`.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Change this command
areas_copy = areas

# Change areas_copy
areas_copy[0] = 5.0

# Print areas
print(areas)
```

`@solution`
```{python}
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Change this command
areas_copy = list(areas)

# Change areas_copy
areas_copy[0] = 5.0

# Print areas
print(areas)
```

`@sct`
```{python}
Ex().check_correct(
  check_object("areas_copy").has_equal_value(incorrect_msg = "Parece que `areas_copy` no se ha actualizado correctamente."),
  check_function("list", missing_msg = "Asegúrate de usar `list(areas)` para crear un `areas_copy`.")
)

mmsg = "No elimines la lista `areas` predefinida."
imsg = "Asegúrate de editar SOLO la copia, no la lista `areas` original. Revisa la descripción del ejercicio si no estás seguro de cómo crear una copia."
Ex().check_correct(
  check_object("areas", missing_msg = mmsg).has_equal_value(incorrect_msg = imsg),
  check_function("list", missing_msg = "Asegúrate de usar `list(areas)` para crear un `areas_copy`.")
)

success_msg("¡Bien hecho! La diferencia entre copias explícitas y basadas en referencias es sutil, pero puede ser realmente importante. Trata de recordar cómo se almacena una lista en la memoria de la computadora.")
```

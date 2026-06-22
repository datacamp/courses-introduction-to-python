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

Una lista es un **tipo de datos compuesto**; te permite agrupar varios valores a la vez, de esta manera:

```
a = "is"
b = "nice"
my_list = ["my", "list", a, b]
```

Después de medir la altura de tu familia, decides recopilar algo de información sobre la casa en la que vives. Las áreas de las distintas partes de tu casa se almacenan en variables separadas en el ejercicio.

`@instructions`
- Crea una lista, `areas`, que contenga el área del vestíbulo (`hall`), la cocina (`kit`), el cuarto de estar (`liv`), el dormitorio (`bed`) y el cuarto de baño (`bath`), en este orden. Usa las variables predefinidas.
- Muestra por pantalla la lista `areas` con la función `print()`.

`@hint`
- Puedes usar las variables que ya se han creado para construir la lista: `areas = [hall, kit, ...]`.
- Asegúrate de usar corchetes `[]` en lugar de paréntesis `()`.
- No necesitas usar comillas al almacenar variables dentro de una lista.
- Escribe `print(areas)` para mostrar la lista al enviar.

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

Aunque no suele ser lo habitual, una lista también puede contener una mezcla de tipos de Python, incluyendo cadenas, valores decimales y booleanos.

Ahora vas a añadir los nombres de las habitaciones a tu lista, para que puedas ver fácilmente tanto el nombre como el tamaño de la habitación juntos.

Te facilitamos parte del código para que empieces. ¡Presta atención! `"bathroom"` es una cadena, mientras que `bath` es una variable que representa el valor decimal `9.50` que especificaste anteriormente.

`@instructions`
- Completa el código que crea la lista `areas`. Estructura la lista de forma que contenga primero el nombre de cada habitación como una cadena de texto y, a continuación, su superficie. Es decir, añade las cadenas `"hallway"`, `"kitchen"` y `"bedroom"` en los lugares correspondientes.
- Muestra por pantalla `areas` de nuevo. ¿Resulta más informativo el resultado esta vez?

`@hint`
- Los primeros cuatro elementos de la lista `areas` se codifican como `["hallway", hall, "kitchen", kit, ...`.
- Una cadena deberá estar entre comillas `""`.

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

Como científico de datos, a menudo tendrás que manejar grandes volúmenes de datos, por lo que será práctico agruparlos.

En lugar de crear una lista con cadenas de texto y decimales para representar los nombres y las superficies de las habitaciones de tu casa, puedes crear una lista de listas.

Recuerda: `"hallway"` es una cadena, mientras que `hall` es la variable que representa el valor decimal `11.25` que has definido anteriormente.

`@instructions`
- Completa la lista de listas para que también contenga los datos del dormitorio y del baño. ¡Asegúrate de introducirlos en orden!
- Muestra por pantalla la variable `house`; ¿te parece que esta forma de estructurar tus datos tiene más sentido?

`@hint`
- Añade _sublists_ a la lista `house` añadiendo `["bedroom", bed]` y `["bathroom", bath]` dentro de los corchetes.
- Recuerda incluir una coma `,` después de cada sublista.
- Para mostrar una variable `x`, escribe `print(x)` en una nueva línea.

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

Hacer indexación (o subsetting) con las listas de Python es pan comido. Fíjate en el siguiente ejemplo de código, donde se crea una lista `x` y luego se selecciona el elemento "b". Recuerda que este es el segundo elemento, por lo que tiene el índice 1. También puedes utilizar la indexación negativa:

```
x = ["a", "b", "c", "d"]
x[1]
x[-3] # same result!
```

¿Te acuerdas de la lista `areas` de antes, la que contenía tanto cadenas de texto como decimales? Su definición ya está incluida en el script. ¿Podrías añadir el código correcto para realizar algunas indexaciones en Python?

`@instructions`
- Muestra por pantalla el segundo elemento de la lista `areas` (tiene el valor `11.25`).
- Indexa y muestra por pantalla el último elemento de `areas`, que es `9.50`. ¡Lo más lógico aquí es utilizar un índice negativo!
- Selecciona el número que representa el área del salón (`20.0`) y muéstralo por pantalla.

`@hint`
- Usa `x[1]` para seleccionar el segundo elemento de una lista `x`.
- Usa `x[-1]` para seleccionar el último elemento de una lista `x`.
- Asegúrate de envolver tus operaciones de subconjunto en una llamada a `print()`.
- El número que representa el área del salón es el 6.º elemento de la lista, así que necesitarás `[5]` aquí. `area[4]` mostraría la cadena de texto.

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

## Segmentación

```yaml
type: NormalExercise
key: 7f08642d18
lang: python
xp: 100
skills:
  - 2
```

Seleccionar valores individuales de una lista es solo una parte de la historia. También es posible _segmentar_ tu lista, lo que significa seleccionar varios elementos a la vez. Utiliza la siguiente sintaxis:

```
my_list[start:end]
```

El índice `start` se incluirá, mientras que el índice `end` no se incluye. Sin embargo, también es posible no especificar estos índices. Si dejas en blanco el índice `start`, Python deduce que quieres empezar la segmentación desde el principio de la lista.

`@instructions`
- Utiliza la segmentación para crear una lista, `downstairs`, que contenga los primeros 6 elementos de `areas`.
- Crea `upstairs` como los últimos `4` elementos de `areas`. Esta vez, simplifica la segmentación omitiendo el índice `end`.
- Muestra por pantalla tanto `downstairs` como `upstairs` usando `print()`.

`@hint`
- Usa los corchetes `[0:6]` para obtener los seis primeros elementos de una lista.
- Para obtener todo excepto los 5 primeros elementos de una lista, `l`, usarías `l[5:]`.
- Añade dos llamadas a `print()` para mostrar `downstairs` y `upstairs` en pantalla.

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

Una lista de Python también puede contener otras listas.

Para obtener subconjuntos de listas de listas, puedes utilizar la misma técnica que antes: los corchetes. En el caso de una lista llamada `house`, el código tendría este aspecto::

```
house[2][0]
```

`@instructions`
- Filtra la lista `house` para obtener el decimal `9.5`.

`@hint`
- Vamos a desglosarlo paso a paso. En primer lugar, queremos llegar al último elemento de la lista: `["bathroom", 9.50]`. Recuerda que el índice del último elemento es `-1`.
- A continuación, queremos obtener el segundo elemento de `["bathroom", 9.50]`, que está en el índice `1`.

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

Para reemplazar elementos de una lista, selecciona un subconjunto de la lista y asigna nuevos valores al subconjunto. Puedes seleccionar elementos individuales o cambiar segmentos completos de la lista de una vez.

Para este ejercicio y los siguientes, seguirás trabajando con la lista `areas` que contiene los nombres y las áreas de distintas estancias de una casa.

`@instructions`
- Actualiza el área del baño a `10.50` metros cuadrados en lugar de `9.50` usando indexación negativa.
- ¡Haz que la lista `areas` sea más moderna! Cambia `"living room"` a `"chill zone"`. No uses indexación negativa esta vez.

`@hint`
- Para actualizar el área del baño, identifica el subconjunto del área del baño (¡es el último elemento de la lista!).
- Luego, reemplaza el valor con la nueva área del baño asignándola a este subconjunto.
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

Si puedes cambiar elementos en una lista, seguro que quieres poder añadir elementos a ella, ¿verdad? Para ello, puedes utilizar el operador `+`:

```
x = ["a", "b", "c", "d"]
y = x + ["e", "f"]
```

¡Te acaba de tocar la lotería, qué pasada! Decides construir una caseta para la piscina y un garaje. ¿Podrías añadir esta información a la lista `areas`?

`@instructions`
- Utiliza el operador `+` para añadir la lista `["poolhouse", 24.5]` al final de la lista `areas`. Guarda la lista resultante con el nombre `areas_1`.
- Amplía aún más `areas_1` añadiendo los datos de tu garaje. Añade la cadena de texto `"garage"` y el decimal `15.45`. Nombra a la lista resultante `areas_2`.

`@hint`
- Sigue el ejemplo de código del ejercicio. En este caso, `x` corresponde a `areas`, y `["e", "f"]` corresponde a `["poolhouse", 24.5]`.
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

Por último, también puedes eliminar elementos de una lista. Para ello, puedes utilizar la instrucción `del`:

```
x = ["a", "b", "c", "d"]
del x[1]
```

Presta mucha atención: en cuanto eliminas un elemento de una lista, ¡los índices de todos los elementos que van detrás cambian automáticamente!

Desafortunadamente, parece que con el dinero de la lotería no te alcanza para la caseta de la piscina y vas a tener que quitarla de la lista. En concreto, debes eliminar tanto la cadena de texto como el decimal correspondiente de la lista `areas`.

`@instructions`
- Elimina la cadena de texto y el decimal correspondientes a `"poolhouse"` de la lista `areas`.
- Muestra por pantalla la lista `areas` actualizada.

`@hint`
- Tendrás que usar `del` dos veces para eliminar dos elementos. ¡Pero ten cuidado, ya que los índices irán cambiando!

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

En este ejercicio ya te proporcionamos una parte del código: una lista llamada `areas` y una copia llamada `areas_copy`.

En este momento, se modifica el primer elemento de la lista `areas_copy` y se muestra por pantalla la lista `areas`. Si pulsas el botón de ejecutar código, verás que, a pesar de haber modificado `areas_copy`, el cambio también se aplica en la lista `areas`. Esto se debe a que tanto `areas` como `areas_copy` apuntan a la misma lista.

Si quieres evitar que los cambios en `areas_copy` afecten también a `areas`, tendrás que hacer una copia más explícita de la lista `areas` utilizando `list()` o mediante el operador `[:]`.

`@instructions`
- Modifica la segunda instrucción, la que crea la variable `areas_copy`, de modo que `areas_copy` sea una copia explícita de `areas`. Tras el cambio, las modificaciones que hagas en `areas_copy` no deberían afectar a `areas`. Envía la respuesta para comprobarlo.

`@hint`
- Cambia la llamada `areas_copy = areas`. En lugar de asignar `areas`, puedes asignar `list(areas)` o `areas[:]`.

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

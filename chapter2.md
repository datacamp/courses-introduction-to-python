---
title_meta: Capítulo 2
title: Listas en Python
description: >-
  Aprende a almacenar, acceder y manipular datos en listas: el primer paso para
  trabajar de manera eficiente con grandes cantidades de datos.
attachments:
  slides_link: 'https://projector-video-pdf-converter.datacamp.com/735/chapter2.pdf'
lessons:
  - nb_of_exercises: 5
    title: Listas en Python
  - nb_of_exercises: 6
    title: Subdividiendo Listas
  - nb_of_exercises: 5
    title: Manipulación de listas
---

## Listas en Python

```yaml
type: VideoExercise
key: a5886d213f
xp: 50
```

`@projector_key`
a0530c4542f10988847b2dbb91f717c3

---

## Crea una lista

```yaml
type: NormalExercise
key: e6c527bf41
lang: python
xp: 100
skills:
  - 2
```

A diferencia de `int`, `bool,` etc., una lista es un **tipo de datos compuesto**; puedes agrupar valores:

```
a = "is"
b = "nice"
my_list = ["my", "list", a, b]
```

Después de medir las alturas de los miembros de tu familia, decides recopilar información sobre la casa en la que vives. Las áreas de las diferentes partes de su casa se almacenan en variables separadas por ahora, como se muestra en el script.

`@instructions`
- Crea una lista, `areas`, que contenga el área del pasillo (`hall`), cocina (`kit`), sala de estar (`liv`), dormitorio (`bed`) y baño (`bath`), en este orden. Utiliza las variables predefinidas.
- Imprime `areas` con la función [`print()`](https://docs.python.org/3/library/functions.html#print).

`@hint`
- Puedes usar las variables que ya han sido creadas para construir la lista: `areas = [hall, kit, ...]`.
- Pon `print(areas)` en tu secuencia de comandos para imprimir al presionar Enviar Respuesta.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# variables de área (en metros cuadrados)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Crea la lista areas


# Imprime areas


```

`@solution`
```{python}
# Variables de área (en metros cuadrados)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Crea la lista areas
areas = [hall, kit, liv, bed, bath]

# Imprime areas
print(areas)
```

`@sct`
```{python}
predef_msg = "¡No elimines ni edites las variables predefinidas!"
areas_msg = "Define `areas` como la lista que contiene todas las variables de área, en el orden correcto: `[hall, kit, liv, bed, bath]`. Cuidado con los errores tipográficos. ¡La lista no debe contener nada más!"

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

success_msg("¡Bien! Una lista es mucho mejor, ¿no?")
```

---

## Crea una lista con diferentes tipos

```yaml
type: NormalExercise
key: 1702a8bcdc
lang: python
xp: 100
skills:
  - 2
```

Una lista puede contener cualquier tipo de Python. Aunque no es muy común, una lista también puede contener una combinación de tipos de Python, como cadenas, flotantes, booleanos, etc.

La impresión del ejercicio anterior no fue completamente satisfactoria. Es solo una lista de números que representan las áreas, pero no se puede saber qué área corresponde a qué parte de la casa.

El código en el editor es la primera parte de una solución. Para algunas de las áreas, el nombre de la habitación correspondiente ya está antes. ¡Presta atención aquí! `"bathroom"` es una cadena, mientras que `bath` es una variable que representa el flotante `9.50` que se especificó anteriormente.

`@instructions`
- Termina el código que crea la lista `areas`. Crea la lista de modo que la lista contenga primero el nombre de cada habitación como una cadena (string) y luego su área. En otras palabras, agrega las cadenas `"hallway"`, `"kitchen"` y `"bedroom"` en los lugares apropiados.
- Imprime `areas` de nuevo; ¿La impresión es más informativa esta vez?

`@hint`
Los primeros 4 elementos de `areas` de la lista se codifican como `["hallway", hall, "kitchen", kit, ...`.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# variables de área (en metros cuadrados)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Modifica la lista areas
areas = [hall, kit, "living room", liv, bed, "bathroom", bath]

# Imprime areas

```

`@solution`
```{python}
# variables de área (en metros cuadrados)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Modifica la lista areas
areas = ["hallway", hall, "kitchen", kit, "living room", liv, "bedroom", bed, "bathroom", bath]

# Imprime areas
print(areas)
```

`@sct`
```{python}
objs = ["hall", "kit", "liv", "bed", "bath"]
predef_msg = "¡No elimines ni edites las variables predefinidas!"
areas_msg = "No asignaste el valor correcto a `areas`. Echa otro vistazo a las instrucciones. Asegúrate de colocar el nombre de la habitación antes de la variable que contiene el área. ¡El orden importa! Cuidado con los errores tipográficos."

Ex().check_correct(
  check_object("areas").has_equal_value(incorrect_msg = areas_msg),
  multi([ check_object(obj, missing_msg = predef_msg).has_equal_value(incorrect_msg = predef_msg) for obj in objs])
)

Ex().has_printout(0, not_printed_msg = "__JINJA__:¿Has utilizado `{{sol_call}}` para imprimir la lista `areas` al final de su script?")

success_msg("¡Bien! Esta lista contiene cadenas y flotantes, ¡pero eso no es un problema para Python!")
```

---

## Selecciona la lista válida

```yaml
type: MultipleChoiceExercise
key: 416b80a405
lang: python
xp: 50
skills:
  - 2
```

Una lista puede contener cualquier tipo de Python. Pero una lista en sí también es un tipo en Python. ¡Esto significa que una lista también puede contener una lista! Python se está volviendo más loco cada minuto, pero no temas, solo recuerda la sintaxis de la lista:

```
my_list = [el1, el2, el3]
```

¿Puedes señalar cuáles de las siguientes líneas de código de Python son maneras válidas de crear una lista?

A. `[1, 3, 4, 2]`
B. `[[1, 2, 3], [4, 5, 7]]`
C. `[1 + 2, "a" * 5, 3]`

`@possible_answers`
- A, B y C
- B
- B y C
- C

`@hint`
Prueba todas las diferentes líneas en el shell de Python y ve cuáles generan un error. ¿Tal vez ninguno de ellos falle?

`@pre_exercise_code`
```{python}

```

`@sct`
```{python}
msg1 = "¡Correcto! Por raros que parezcan, todos estos comandos son maneras válidas de crear una lista de Python."
msg2 = "¡El comando B es válido, pero no es el único!"
msg3 = "Tanto el comando B como el C son válidos; ¿qué pasa con el comando A? Pruébalo en la consola."
msg4 = "¡El comando C es válido, pero no es el único!"
Ex().has_chosen(1,[msg1,msg2,msg3,msg4])
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

Como científico de datos, a menudo trabajarás con una gran cantidad de datos y tendrá sentido agrupar algunos de estos datos.

En lugar de crear una lista plana que contenga cadenas y flotantes, que representen los nombres y las áreas de las habitaciones de la casa, puedes crear una lista de listas. El script en el editor puede darte una idea.

No te confundas aquí: `"hallway"` es una cadena, mientras que `hall` es una variable que representa el flotante `11.25` que se especificó anteriormente.

`@instructions`
- Termina la lista de listas para que contenga también los datos de bedroom (dormitorio) y bathroom (baño). ¡Asegúrate de ingresarlos en orden!
- Imprime `house`; ¿Tiene más sentido esta forma de estructurar los datos?
- Imprime el tipo de `house`. ¿Seguimos lidiando con una lista?

`@hint`
- Agrega _sublistas_ a la lista `house` agregando `["bedroom", bed]` y `["bathrrom", bath]` dentro de los corchetes.
- Para imprimir una variable `x`, escribe `print(x)` en una nueva línea en el script de Python.
- Para imprimir el tipo de una variable `x`, puedes usar `print(type(x))`.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# variables de área (en metros cuadrados)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# información de la casa como lista de listas
house = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv]]

# imprime house


# Imprime el tipo de house

```

`@solution`
```{python}
# variables de área (en metros cuadrados)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# información de la casa como lista de listas
house = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv],
         ["bedroom", bed],
         ["bathroom", bath]]

# imprime house
print(house)

# Imprime el tipo de house
print(type(house))
```

`@sct`
```{python}
predef_msg = "¡No elimines ni edites las variables predefinidas!"
house_msg = "No asignaste el valor correcto a `casa`. Echa otro vistazo a las instrucciones. Amplía la lista de listas para que incorpore una lista para cada par de nombre de habitación y área de la habitación. ¡Cuidado con el orden y los errores tipográficos!"

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

Ex().has_printout(0, not_printed_msg = "__JINJA__: ¿Has utilizado `{{sol_call}}` para imprimir el contenido de `house`?")
Ex().has_printout(1, not_printed_msg = "__JINJA__: ¿Has utilizado `{{sol_call}}` para imprimir el tipo de variable de `house` ?")

success_msg("¡Genial! ¡Prepárate para aprender sobre sub sets de listas!")
```

---

## Subdividiendo Listas

```yaml
type: VideoExercise
key: c076b5a69c
xp: 50
```

`@projector_key`
fc15ba5cb9485456df8589130b519ea3

---

## Subdivide y conquista

```yaml
type: NormalExercise
key: c3ce582e32
lang: python
xp: 100
skills:
  - 2
```

Subdividir listas en Python es pan comido. Toma el ejemplo de código a continuación, que crea una lista `x` y luego selecciona "b" de ella. Recuerda que este es el segundo elemento, por lo que tiene índice 1. También puedes utilizar indexación negativa.

```
x = ["a", "b", "c", "d"]
x[1]
x[-3] # ¡mismo resultado!
```

¿Recuerdas la lista `areas` de antes, que contenía cadenas y flotantes? Su definición ya está en el script. ¿Puedes agregar el código correcto para subdividir con Python?

`@instructions`
- Imprime el segundo elemento de la lista `areas` (tiene el valor `11.25`).
- Selecciona e imprime el último elemento de `areas`, esto es `9.50`. ¡Usar un índice negativo tiene sentido en esta situación!
- Selecciona el número que representa el área de living room (`20.0`) e imprímelo.

`@hint`
- Usa `x[1]` para seleccionar el segundo elemento de una lista `x`. Asegúrate de envolver la operación con la función [`print()`](https://docs.python.org/3/library/functions.html#print).
- Usa `x[-1]` para seleccionar el último elemento de la lista `x`. Asegúrate de envolver la operación con la función [`print()`](https://docs.python.org/3/library/functions.html#print).
- El número que representa el área de living room es el sexto elemento de la lista, por lo que necesitarás `[5]`.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Crea la lista areas
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Imprime el segundo elemento de areas
print(areas[_])

# Imprime el último elemento de areas
print(areas[__])

# Imprime el área de la sala
print(areas[_])
```

`@solution`
```{python}
# Crea la lista areas
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Imprime el segundo elemento de areas
print(areas[1])

# Imprime el último elemento de areas
print(areas[-1])

# Imprime el área de la sala
print(areas[5])
```

`@sct`
```{python}
msg = "No elimines ni edites la lista `areas` predefinida."
Ex().check_object("areas", missing_msg = msg).has_equal_value(incorrect_msg = msg)
Ex().has_printout(0, not_printed_msg = "Revisa tu código para imprimir el segundo elemento de `areas`, que está en el índice `1`.")
Ex().has_printout(1, not_printed_msg = "Revisa tu código para imprimir el último elemento de `areas`, que está en el índice `-1`.")
Ex().has_printout(2, not_printed_msg = "Revisa tu código para imprimir el área de living room. Está en el índice `5`.")
success_msg("¡Buen trabajo!")
```

---

## Subdivide y calcula

```yaml
type: NormalExercise
key: 58c969f11f
lang: python
xp: 100
skills:
  - 2
```

Después de extraer valores de una lista, puedes usarlos para realizar cálculos adicionales. Toma este ejemplo, donde se extraen el segundo y cuarto elemento de una lista `x` . Las cadenas resultantes se pegan juntas usando el operador `+` :

```
x = ["a", "b", "c", "d"]
print(x[1] + x[3])
```

`@instructions`
- Con una combinación de sub sets de lista y asignación de variables, crea una nueva variable, `eat_sleep_area`, que contenga la suma del área de kitchen (cocina) y el área de bedroom (dormitorio).
- Imprime la nueva variable `eat_sleep_area`.

`@hint`
- Suma `areas[3]` con `areas[-3]` para calcular `eat_sleep_area`.
- Imprime `eat_sleep_area`: `print(eat_sleep_area)`.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Crea la lista areas
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Suma del área de kitchen y bedroom: eat_sleep_area


# Imprime la variable eat_sleep_area

```

`@solution`
```{python}
# Crea la lista areas
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Suma del área de kitchen y bedroom: eat_sleep_area
eat_sleep_area = areas[3] + areas[-3]

# Imprime la variable eat_sleep_area
print(eat_sleep_area)
```

`@sct`
```{python}
msg = "No elimines ni edites la lista `areas` predefinida."
Ex().check_object("areas", missing_msg = msg).has_equal_value(incorrect_msg = msg)
Ex().check_object("eat_sleep_area").has_equal_value(incorrect_msg = "Asegúrate de asignar el valor correcto a `eat_sleep_area`. Necesitarás sumar `areas[3]` y `areas[-3]`.")
Ex().has_printout(0, not_printed_msg = "¡No olvides imprimir `eat_sleep_area` después de calcularla!")
success_msg("¡Bellissimo!")
```

---

## Cortando y rebanando

```yaml
type: NormalExercise
key: 7f08642d18
lang: python
xp: 100
skills:
  - 2
```

Seleccionar valores individuales de una lista es solo una parte de la historia. También es posible _subdividir_ la lista, lo que significa seleccionar varios elementos de una lista. Se utiliza la siguiente sintaxis:

```
mi_lista[inicio:fin]
```

Se incluirá el índice `inicio` , mientras que el índice `fin` _no será incluido_.

El ejemplo de código siguiente muestra un ejemplo. Una lista con `"b"` y `"c"`, correspondientes a los índices 1 y 2, se seleccionan de una lista `x`:

```
x = ["a", "b", "c", "d"]
x[1:3]
```

Los elementos con índice 1 y 2 serán incluidos, mientras que el elemento con índice 3 no.

`@instructions`
- Usa la subdivisión para crear una lista, `downstairs`, que contenga los primeros 6 elementos de `areas`.
- Haz algo similar para crear una nueva variable, `upstairs`, que contenga los últimos 4 elementos de `areas`.
- Imprime tanto `downstairs` como `upstairs` usando [`print()`](https://docs.python.org/3/library/functions.html#print).

`@hint`
- Usa los corchetes `[0:6]` para construir `downstairs`.
- Use los corchetes `[6:10]` para construir `upstairs`.
- Simplemente agregue dos llamadas a [`print()`](https://docs.python.org/3/library/functions.html#print) al script para imprimir `downstairs` y `upstairs`.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Crea la lista areas
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Subdivide areas para crear downstairs


# Subdivide areas para crear upstairs


# Imprime downstairs y upstairs
```

`@solution`
```{python}
# Crea la lista areas
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Subdivide areas para crear downstairs
downstairs = areas[0:6]

# Subdivide areas para crear upstairs
upstairs = areas[6:10]

# Imprime downstairs y upstairs
print(downstairs)
print(upstairs)
```

`@sct`
```{python}
msg = "No elimines ni edites la lista `areas` predefinida."
Ex().check_object("areas", missing_msg = msg).has_equal_value(incorrect_msg = msg)

patt = "`%s` es incorrecto. Utiliza `areas[%s]` y subdivide para seleccionar los elementos que desees, o algo equivalente."
Ex().check_object("downstairs").has_equal_value(incorrect_msg = patt % ('downstairs', '0:6'))
Ex().check_object("upstairs").has_equal_value(incorrect_msg = patt % ('upstairs', '6:10'))

Ex().has_printout(0, not_printed_msg="¿Has impreso `downstairs` después de calcularla?")
Ex().has_printout(1, not_printed_msg="¿Imprimiste `upstairs` después de calcularla?")

success_msg("¡Genial!")
```

---

## Cortando y rebanando (2)

```yaml
type: NormalExercise
key: dfc9a168a3
lang: python
xp: 100
skills:
  - 2
```

En el video, Hugo discutió por primera vez la sintaxis en la que especificas dónde comenzar y dónde terminar la porción de tu lista:

```
my_list[begin:end]
```

Sin embargo, también es posible no especificar estos índices. Si no especificas el índice `begin`, Python entiende de que deseas comenzar el segmento al principio de la lista. Si no especificas el índice `end`, el segmento irá hasta el último elemento de la lista. Para experimentar con esto, prueba los siguientes comandos en IPython Shell:

```
x = ["a", "b", "c", "d"]
x[:2]
x[2:]
x[:]
```

`@instructions`
- Vuelve a crear `downstairs`, como los primeros `6` elementos de `areas`. Esta vez, simplifica el corte omitiendo el índice `begin`.
- Crea `upstairs` nuevamente, como los últimos `4` elementos de `areas`. Esta vez, simplifica el corte omitiendo el índice `end`.

`@hint`
- Para obtener los primeros 5 elementos de una lista, `l`, puedes usar `l[:5]`.
- Para obtener todo excepto los primeros 5 elementos, usaríamos `l[5:]`.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Crea la lista areas
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Corte alternativo para crear downstairs


# Corte alternativo para crear upstairs

```

`@solution`
```{python}
# Crea la lista areas
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Corte alternativo para crear downstairs
downstairs = areas[:6]

# Corte alternativo para crear upstairs
upstairs = areas[6:]
```

`@sct`
```{python}
msg = "No elimines ni edites la lista `areas` predefinida."
Ex().check_object("areas", missing_msg = msg).has_equal_value(incorrect_msg = msg)

patt = "Tu definición de `%s` es incorrecta. Utiliza `areas[...]` y subdivisión para seleccionar los elementos necesarios. Podrías usar `%s` donde están los puntos, por ejemplo."
Ex().check_object("downstairs").has_equal_value(incorrect_msg = patt % ("downstairs",":6"))
Ex().check_object("upstairs").has_equal_value(incorrect_msg = patt % ("upstairs",":6"))

success_msg("¡Maravilloso!")
```

---

## Subdividiendo listas de listas

```yaml
type: MultipleChoiceExercise
key: dbbbd306cf
lang: python
xp: 50
skills:
  - 2
```

Vimos que una lista de Python puede contener prácticamente cualquier cosa; incluso otras listas! Para crear subconjuntos de listas de listas, se puede usar la misma técnica que antes: corchetes. Prueba los comandos del siguiente ejemplo de código en IPython Shell:

```
x = [["a", "b", "c"],
     ["d", "e", "f"],
     ["g", "h", "i"]]
x[2][0]
x[2][:2]
```

`x[2]` da como resultado una lista, que se puede subdividir a su vez agregando corchetes adicionales.

¿Qué obtendremos usando `house[-1][1]`? `house`, la lista de listas que creamos anteriormente, ya está definida en el espacio de trabajo. Puedes experimentar con ella en el IPython Shell.

`@possible_answers`
- Un flotante: el área de la kitchen (cocina)
- Una cadena: `"kitchen"`
- Un flotante: el área de bathroom (baño)
- Una cadena: `"bathroom"`

`@hint`
`house[-1]` selecciona el último elemento de `house`, que es la lista `["bathroom", 9.50]`. ¿Cuál es el resultado si luego subdividimos a su vez esta lista usando `[1]`? ¡Siempre puedes probar el comando en el IPython Shell!

`@pre_exercise_code`
```{python}
house = [["hallway", 11.25],
["kitchen", 18.0],
["living room", 20.0],
["bedroom", 10.75],
["bathroom", 9.50]]
```

`@sct`
```{python}
msg1 = msg2 = "Incorrecto. `house[-1]` selecciona el último elemento de `house`, que es la lista `[\"bathroom\", 9.50]`."
msg3 = "¡Correcto! La última pieza de este rompecabezas es la manipulación de listas."
msg4 = "Incorrecto. `house[-1]` de hecho selecciona la lista que representa la información de bathroom, pero `[1]` selecciona el segundo elemento de la sublista, no el primero. ¡Python usa indexación basada en cero!"
Ex().has_chosen(3, [msg1, msg2, msg3, msg4])
```

---

## Manipulación de listas

```yaml
type: VideoExercise
key: d7fe818b3a
xp: 50
```

`@projector_key`
355ed52d2fb0d67508c6a311b7cbc6d3

---

## Reemplazar elementos de una lista

```yaml
type: NormalExercise
key: 4e1bba1b55
lang: python
xp: 100
skills:
  - 2
```

Reemplazar elementos de una lista es bastante fácil. Simplemente subdivide la lista y asigna nuevos valores al sub set. Puedes seleccionar elementos individuales o puedes cambiar segmentos completos de lista a la vez.

Usa el IPython Shell para experimentar con los siguientes comandos. ¿Puedes decir qué está pasando y por qué?

```
x = ["a", "b", "c", "d"]
x[1] = "r"
x[2:] = ["s", "t"]
```

Para este ejercicio y los siguientes, continuaremos trabajando en la lista `areas` que contiene los nombres y las áreas de las diferentes habitaciones de una casa.

`@instructions`
- Actualiza el área del área de bathroom (baño) para que sea de 10.50 metros cuadrados en lugar de 9.50.
- ¡Hagamos que la lista `areas` esté más a la moda! Cambia `"living room"` por `"chill zone"`.

`@hint`
- Usa `areas[-1] = ___` para actualizar el área de bathroom. ¿Puedes llenar los espacios en blanco?
- Del mismo modo, puedes usar `areas[4] = ___` para actualizar el elemento `"living room"`.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Crea la lista areas
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Correge el área de bathroom


# Cambia "living room" a "chill zone"

```

`@solution`
```{python}
# Crea la lista areas
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Correge el área de bathroom
areas[-1] = 10.50

# Cambia "living room" a "chill zone"
areas[4] = "chill zone"
```

`@sct`
```{python}
bathroom_msg = 'Puedes usar `areas[-1] = 10.50` para actualizar el área de bathroom.'
chillzone_msg = 'Puedes usar `areas[4] = "chill zone"` para actualizar el nombre de living room.'
Ex().check_correct(
  check_object('areas').has_equal_value(incorrect_msg = 'Los cambios a `areas` no arrojaron la lista correcta. ¿Estás seguro de que usaste las operaciones de subdivisión correctas? En caso de duda, ¡puedes obtener una sugerencia!'),
  multi(
    has_equal_value(expr_code='areas[-1]', override=10.50, incorrect_msg = bathroom_msg),
    has_equal_value(expr_code='areas[4]', override='chill zone', incorrect_msg = chillzone_msg),
  )
)
success_msg('¡Genial! Como se ve en el ejemplo, podemos dividir una lista y reemplazarla con otra lista para actualizar varios elementos en un solo comando.')
```

---

## Extender una lista

```yaml
type: NormalExercise
key: ff0fe8d967
lang: python
xp: 100
skills:
  - 2
```

Si podemos cambiar elementos de una lista, seguro que es posible agregarle elementos, ¿no? Puedes usar el operador `+` :

```
x = ["a", "b", "c", "d"]
y = x + ["e", "f"]
```

Acabas de ganar la lotería, ¡Felicidades! Decides construir una casa junto a la piscina (poolhouse) y un garaje (garage). ¿Puedes agregar la información a la lista `areas`?

`@instructions`
- Use el operador `+` para pegar la lista `["poolhouse", 24.5]` al final de la lista `areas`. Almacena la lista resultante como `areas_1`.
- Amplía aún más `areas_1` agregando los datos de su garaje. Agrega la cadena `"garage"` y el flotante `15.45`. Nombra la lista resultante `areas_2`.

`@hint`
- Sigue el ejemplo de código del ejercicio de arriba. `x` es `areas`, y `["e", "f"]` es `["poolhouse", 24.5]`.
- Para agregar más elementos a `areas_1`, usa `areas_1 + ["elemento", 123]`.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Crea la lista areas y realiza algunos cambios.
areas = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0,
         "bedroom", 10.75, "bathroom", 10.50]

# Agrega datos de poolhouse a areas, la nueva lista es areas_1


# Agrega los datos de garage a areas_1, la nueva lista es areas_2

```

`@solution`
```{python}
# Crea la lista areas (versión actualizada)
areas = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0,
         "bedroom", 10.75, "bathroom", 10.50]

# Agrega datos de poolhouse a areas, la nueva lista es areas_1
areas_1 = areas + ["poolhouse", 24.5]

# Agrega los datos de garage a areas_1, la nueva lista es areas_2
areas_2 = areas_1 + ["garage", 15.45]
```

`@sct`
```{python}
msg = "No elimines ni edites la lista `areas` predefinida."
Ex().check_object("areas", missing_msg = msg).has_equal_value(incorrect_msg = msg)
Ex().check_object("areas_1").has_equal_value(incorrect_msg = "Usa `areas + [\\"poolhouse\\", 24.5]` para crear `areas_1`. ¡Cuidado con los errores tipográficos!")
Ex().check_object("areas_2").has_equal_value(incorrect_msg = "Usa `areas_1 + [\\"garage\\", 15.45]` para crear `areas_2`. ¡Cuidado con los errores tipográficos!")
success_msg("¡Genial! ¡La lista va muy bien!")
```

---

## Eliminar elementos de una lista

```yaml
type: MultipleChoiceExercise
key: 85f792356e
lang: python
xp: 50
skills:
  - 2
```

Finalmente, también se puede eliminar elementos de la lista. Podemos hacer esto con el comando `del` :

```
x = ["a", "b", "c", "d"]
del(x[1])
```

Pongamos atención aquí: tan pronto como se elimina un elemento de una lista, ¡los índices de los elementos que vienen después del elemento eliminado cambian!

La versión actualizada y extendida de `areas` que construímos en los ejercicios anteriores se codifica a continuación. Puedes copiar y pegar esto en el IPython Shell para experimentar con el resultado.

```
areas = ["hallway", 11.25, "kitchen", 18.0,
        "chill zone", 20.0, "bedroom", 10.75,
        "bathroom", 10.50, "poolhouse", 24.5,
        "garage", 15.45]
```

¡Hubo un error! La cantidad que ganaste con la lotería no es tan grande después de todo y parece que la casa de la piscina ya no será posible. Decides entonces eliminar la cadena correspondiente y el flotante de la lista `areas` .

El signo `;` se utiliza para colocar mas de un comando en la misma línea. Los siguientes dos fragmentos de código son equivalentes:

```
# Misma línea
comando1; comando2

# Líneas separadas
comando1
comando2
```

¿Cuál de los fragmentos de código hace lo que necesitamos?

`@possible_answers`
- `del(areas[10]); del(areas[11])`
- `del(areas[10:11])`
- `del(areas[-4:-2])`
- `del(areas[-3]); del(areas[-4])`

`@hint`
Simplemente puedes probar todas las diferentes opciones para ver si funcionan. Solo asegúrese de redefinir la lista `areas` nuevamente antes de probar una nueva opción.

`@pre_exercise_code`
```{python}
areas = ["hallway", 11.25, "kitchen", 18.0,
        "chill zone", 20.0, "bedroom", 10.75,
        "bathroom", 10.50, "poolhouse", 24.5,
        "garage", 15.45]
```

`@sct`
```{python}
msg1 = "Si primero eliminas `areas[10]`, todos los elementos después del índice 10 se mueven un lugar. Si luego ejecutas `del(areas[11])`, estás eliminando el elemento que estaba originalmente en el índice `12`."
msg2 = "`areas[10:11])` solo seleccionará el elemento en el índice `10`."
msg3 = "¡Correcto! Más adelante aprenderás maneras más sencillas de eliminar elementos específicos de las listas en Python."
msg4 = "Este fragmento de código no eliminará correctamente la información relacionada con la piscina.  Intenta otra vez."
Ex().has_chosen(3, [msg1, msg2, msg3, msg4])
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

Al final del video, Hugo explicó el funcionamiento interno de las listas de Python. En este ejercicio obtendrás algo de experiencia práctica con esto.

El código de Python en el script crea una lista llamada `areas` y una copia llamada `areas_copy`. A continuación, se cambia el primer elemento de la lista `areas_copy` y se imprime la lista `areas` . Si presiona _Ejecutar Código_, verás que, aunque hayamos cambiado `areas_copy`, el cambio también tiene efecto en la lista `areas`. Esto es porque `areas` y `areas_copy` apuntan a la misma lista.

Si deseas evitar que los cambios en `areas_copy` también tengan efecto en `areas`, tendrás que hacer una copia explícita de la lista `areas. Puedes hacer esto con [`list()`](https://docs.python.org/3/library/functions.html#func-list) o usando `[:]`.

`@instructions`
Cambia el segundo comando, que crea la variable `areas_copy`, de modo que `areas_copy` sea una copia explícita de `areas`. Después de la edición, los cambios realizados en `areas_copy` no deberían afectar a `areas`. Envía la respuesta para verificar esto.

`@hint`
Cambia la línea `areas_copy = areas`. En lugar de asignar `areas`, puedes asignar `list(areas)` o `areas[:]`.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Crea la lista areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Crea areas_copy
areas_copy = areas

# Cambiar areas_copy
areas_copy[0] = 5.0

# Imprime areas
print(areas)
```

`@solution`
```{python}
# Crea la lista areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Crea areas_copy
areas_copy = list(areas)

# Cambiar areas_copy
areas_copy[0] = 5.0

# Imprime areas
print(areas)
```

`@sct`
```{python}
Ex().check_correct(
  check_object("areas_copy").has_equal_value(incorrect_msg = "Parece que `areas_copy` no se actualizó correctamente"),
  check_function("list", missing_msg = "Asegúrate de usar `list(areas)` para crear `areas_copy`").
)

mmsg = "No elimines la lista `areas` predefinida".
imsg = "Asegúrate de editar SÓLO la copia (areas_copy), no la lista `areas` original. Echa otro vistazo a la descripción del ejercicio si no estás seguro de cómo crear una copia."
Ex().check_correct(
  check_object("areas", missing_msg = mmsg).has_equal_value(incorrect_msg = imsg),
  check_function("list", missing_msg = "Asegúrate de usar `list(areas)` para crear `areas_copy`").
)

success_msg("¡Bien! La diferencia entre las copias explícitas y las basadas en referencias es sutil, pero puede resultar ser realmente importante. Trata de tener en cuenta cómo se almacena una lista en la memoria de la computadora.")
```

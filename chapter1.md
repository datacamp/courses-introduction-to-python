---
title_meta: Capítulo 1
title: Conceptos básicos de Python
description: >-
  Una introducción a los conceptos básicos de Python. Aprende a utilizar Python
  de forma interactiva y mediante un script. Crea tus primeras variables y
  familiarízate con los tipos de datos básicos de Python.
attachments:
  slides_link: 'https://projector-video-pdf-converter.datacamp.com/735/chapter1.pdf'
free_preview: true
lessons:
  - nb_of_exercises: 3
    title: '¡Hola, Python!'
  - nb_of_exercises: 5
    title: Variables y tipos
---

## ¡Hola, Python!

```yaml
type: VideoExercise
key: f644a48d5d
xp: 50
```

`@projector_key`
d8fcd4c930027fa4e1c3870c7e7e0ff1

---

## Tu primer código Python

```yaml
type: NormalExercise
key: bdc52f0e19
lang: python
xp: 100
skills:
  - 2
```

¡Es hora de ejecutar tu primer código Python!

Ve al código y pulsa el botón de ejecución de código para ver el resultado.

`@instructions`
- Pulsa el botón de ejecución de código para ver el resultado de `print(5 / 8)`.

`@hint`
- Ejecuta el código antes de enviar tu respuesta para que tengas tiempo de explorar el resultado.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Hit run code to see the output!
print(5 / 8)
```

`@solution`
```{python}
# Hit run code to see the output!
print(5 / 8)
```

`@sct`
```{python}
Ex().has_printout(0, not_printed_msg = "__JINJA__:¿Has usado `{{sol_call}}` para imprimir `5 / 8`?")
success_msg("¡Genial! ¡Vamos al siguiente!")
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

Python es perfectamente adecuado para hacer cálculos básicos. Puede hacer sumas, restas, multiplicaciones y divisiones.

El código del script ofrece algunos ejemplos.

Ahora es tu turno de practicar escribiendo código.

`@instructions`
- Imprime el resultado de restar `5` a `5` en `# Subtraction` con `print()`.
- Imprime el resultado de multiplicar `3` por `5` en `# Multiplication`.

`@hint`
- Tendrás que utilizar `print()` para generar una salida.
- Puedes restar con `-` y multiplicar con `*`.

`@pre_exercise_code`
```{python}
 
```

`@sample_code`
```{python}
# Addition and division
print(4 + 5)
print(10 / 2)

# Subtraction
print()

# Multiplication

```

`@solution`
```{python}
# Addition and division
print(4 + 5)
print(10 / 2)

# Subtraction
print(5 - 5)

# Multiplication
print(3 * 5)
```

`@sct`
```{python}
Ex().has_printout(0, not_printed_msg = "¿Has usado `print(4 + 5)` para imprimir el resultado de tu suma?")

Ex().has_printout(1, not_printed_msg = "¿Has usado `print(5 - 5)` para imprimir el resultado de tu resta?")

Ex().has_printout(2, not_printed_msg = "¿Has usado `print(3 * 5)` para imprimir el resultado de tu multiplicación?")

Ex().has_printout(3, not_printed_msg = "¿Has usado `print(10 / 2)` para imprimir el resultado de tu división?")

success_msg("¡Eso es correcto! Python puede ayudarte a hacer cálculos, una característica que será útil para el análisis a medida que desarrollemos nuestras habilidades con los datos.")
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

En Python, una variable te permite referirte a un valor con un nombre. Para crear una variable `x` con un valor de `5`, debes utilizar `=`, como en este ejemplo:

```
x = 5
```

Ahora puedes utilizar el nombre de esta variable, `x`, en lugar del valor real, `5`.

Recuerda que `=` en Python significa _asignación_, no igualdad. Pruébalo en el ejercicio sustituyendo `____` por tu código.

`@instructions`
- Crea una variable `savings` con el valor de `100`.
- Comprueba esta variable escribiendo `print(savings)` en el script.

`@hint`
- Escribe `savings = 100` para crear la variable `savings`.
- Después de crear la variable `savings`, puedes escribir `print(savings)`.
- Tu código final no debe incluir ningún `____`.

`@pre_exercise_code`
```{python}
 
```

`@sample_code`
```{python}
# Create a variable savings
____

# Print out savings
____
```

`@solution`
```{python}
# Create a variable savings
savings = 100

# Print out savings
print(savings)
```

`@sct`
```{python}
Ex().check_object("savings").has_equal_value(incorrect_msg="Asigna `100` a la variable `savings`.")
Ex().has_printout(0, not_printed_msg = "Imprime `savings`, la variable que creaste, con `print(savings)`.")
success_msg("¡Genial! ¡Ahora intentemos hacer algunos cálculos con esta variable!")
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

Ya has creado una variable de ahorro, así que ¡empecemos a ahorrar!

En lugar de calcular con los valores reales, puedes utilizar variables.

¿Cuánto dinero habrías ahorrado dentro de cuatro meses si ahorraras $10 cada mes?

`@instructions`
- Crea una variable `monthly_savings` igual a `10` y otra variable `num_months` igual a `4`.
- Multiplica `monthly_savings` por `num_months` y asígnalo a `new_savings`.
- Imprime el valor de `new_savings`.

`@hint`
- Puedes hacer cálculos con variables del mismo modo que con números, así que, en lugar de `10 * 4`, sustituye los números por las variables.
- Utiliza `print()` para ver la cantidad en `new_savings`.
- ¡Escribe correctamente las variables!

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create the variables monthly_savings and num_months



# Multiply monthly_savings and num_months
new_savings = ____

# Print new_savings

```

`@solution`
```{python}
# Create the variables monthly_savings and num_months
monthly_savings = 10
num_months = 4

# Multiply monthly_savings and num_months
new_savings = monthly_savings * num_months

# Print new_savings
print(new_savings)
```

`@sct`
```{python}
Ex().check_object("monthly_savings").has_equal_value(incorrect_msg = "¿Guardaste `10` en `monthly_savings` usando `monthly_savings = 10`?")
Ex().check_object("num_months").has_equal_value(incorrect_msg = "¿Guardaste `4` en `num_months` usando `num_months = 4`?")
Ex().check_object("new_savings").has_equal_value(incorrect_msg = "¿Usaste las variables y símbolos correctos para multiplicar? Se esperaba `monthly_savings * num_months` pero obtuviste otra cosa.")
# Ex().check_object("total_savings").has_equal_value(incorrect_msg = "¿Usaste las variables y símbolos correctos para sumar? Se esperaba `savings + new_savings` pero obtuviste otra cosa.")

Ex().has_printout(0, not_printed_msg="Recuerda imprimir `new_savings` al final de tu script.")

success_msg("¡Tienes $40 en nuevos ahorros!")
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

En el ejercicio anterior, trabajaste con el tipo de datos entero de Python:

- `int` o entero: un número sin parte fraccionaria. `savings`, con el valor `100`, es un ejemplo de entero.

Además de los tipos de datos numéricos, hay otros tres tipos de datos muy comunes:

- `float` o punto flotante: un número que tiene una parte entera y otra fraccionaria, separadas por un punto. `1.1` es un ejemplo de flotante.
- `str` o cadena: un tipo para representar texto. Puedes utilizar comillas simples o dobles para construir una cadena.
- `bool` o booleano: un tipo para representar valores lógicos. Solo puede ser `True` o `False` (¡las mayúsculas son importantes!).

`@instructions`
- Crea un nuevo flotante, `half`, con el valor `0.5`.
- Crea una nueva cadena, `intro`, con el valor `"Hello! How are you?"`.
- Crea un nuevo booleano, `is_good`, con el valor `True`.

`@hint`
- Para crear una variable en Python, utiliza `=`. Asegúrate de escribir tu cadena entre comillas simples o dobles.
- En Python solo existen dos valores booleanos: `True` y `False`. `TRUE`, `true`, `FALSE`, `false` y otras versiones no se aceptan.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create a variable half


# Create a variable intro


# Create a variable is_good

```

`@solution`
```{python}
# Create a variable half
half = 0.5

# Create a variable intro
intro = "Hello! How are you?"

# Create a variable is_good
is_good = True
```

`@sct`
```{python}
Ex().check_object("half").has_equal_value(incorrect_msg = "¿Guardaste el float, `0.5` en `half`?")

Ex().check_object("intro").has_equal_value(incorrect_msg = "Hmm, algo está incorrecto en tu variable `intro`. Revisa la ortografía y asegúrate de haber usado comillas.")

Ex().check_object("is_good").has_equal_value(incorrect_msg = "¿Capitalizaste el valor booleano? Recuerda que no necesitas usar comillas aquí.")

success_msg("¡Bien hecho!")
```

---

## Operaciones con otros tipos

```yaml
type: BulletExercise
key: 4d0d83cc02
xp: 100
```

En Python existen distintos tipos de variables. Puedes ver el tipo de una variable utilizando `type()`. Por ejemplo, para ver el tipo de `a`, ejecuta lo siguiente: `type(a)`.

Los distintos tipos se comportan de forma diferente en Python. Cuando sumes dos cadenas, por ejemplo, obtendrás un comportamiento diferente que cuando sumes dos enteros o dos booleanos.

Es hora de que lo pruebes.

`@pre_exercise_code`
```{python}

```

***

```yaml
type: NormalExercise
key: f4e91c4ae9
xp: 50
```

`@instructions`
- Suma `savings` y `new_savings` y asígnalo a `total_savings`.
- Utiliza `type()` para imprimir el tipo resultante de `total_savings`.

`@hint`
- Asigna `savings + new_savings` a una nueva variable, `total_savings`.
- Para imprimir el tipo de una variable `x`, utiliza `print(type(x))`.

`@sample_code`
```{python}
savings = 100
new_savings = 40

# Calculate total_savings using savings and new_savings
____
print(total_savings)

# Print the type of total_savings
print(____)
```

`@solution`
```{python}
savings = 100
new_savings = 40

# Calculate total_savings using savings and new_savings
total_savings = savings + new_savings
print(total_savings)

# Print the type of total_savings
print(type(total_savings))
```

`@sct`
```{python}
# predefined
msg = "No tienes que cambiar ni eliminar las variables predefinidas."

Ex().multi(
    check_object('savings', missing_msg=msg).has_equal_value(incorrect_msg=msg),
    check_object('new_savings', missing_msg=msg).has_equal_value(incorrect_msg=msg)
)

Ex().multi(
    check_object("total_savings").has_equal_value(incorrect_msg="Suma `savings` y `new_savings` para crear la variable `total_savings`."),
    has_printout(1, not_printed_msg = "__JINJA__:Usa `{{sol_call}}` para imprimir el tipo de `total_savings`.")
)
```

***

```yaml
type: NormalExercise
key: f54fbf9bd9
xp: 50
```

`@instructions`
- Calcula la suma de `intro` y `intro` y asigna el resultado a `doubleintro`.
- Imprime `doubleintro`. ¿Te lo esperabas?

`@hint`
- Asigna `intro + intro` a una nueva variable, `doubleintro`.
- Para imprimir una variable `x`, escribe `print(x)` en el script.

`@sample_code`
```{python}
intro = "Hello! How are you?"

# Assign sum of intro and intro to doubleintro
____

# Print out doubleintro
print(____)
```

`@solution`
```{python}
intro = "Hello! How are you?"

# Assign sum of intro and intro to doubleintro
doubleintro = intro + intro

# Print out doubleintro
print(doubleintro)
```

`@sct`
```{python}
# predefined
msg = "No tienes que cambiar ni eliminar las variables predefinidas."

Ex().check_object('intro', missing_msg=msg).has_equal_value(incorrect_msg=msg)

Ex().multi(
    check_object("doubleintro").has_equal_value(incorrect_msg  = "¿Has almacenado el resultado de `intro + intro` en `doubleintro`?"),
    has_printout(0, not_printed_msg = "No olvides imprimir `doubleintro`.")
)

success_msg("Bien. Observa cómo `intro + intro` hace que `\"Hello! How are you?\"` y `\"Hello! How are you?\"` se unan.")
```

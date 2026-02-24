---
title: Insert title here
key: d8fcd4c930027fa4e1c3870c7e7e0ff1
video_link:
  mp3: >-
    https://videos.datacamp.com/mp3/translations/course_735/es-ES/e2b0deee-4235-4405-92bf-f99115ae3582.mp3
---

## ¡Hola, Python!

```yaml
type: TitleSlide
key: f743ca8c41
```

`@lower_third`
name: Hugo Bowne-Anderson
title: Data Scientist at DataCamp

`@script`
¡Hola! Me llamo Hugo y seré tu profesor en Introducción a Python para la ciencia de datos.

Soy científico de datos y formador en DataCamp.


---

## Cómo aprenderás

```yaml
type: FullSlide
key: 30ee08a725
disable_transition: true
```

`@part1`
![Interfaz de DataCamp](https://assets.datacamp.com/img/translations/es-ES/production/repositories/288/datasets/729574d2168960686381caefe79baf5978e27d0d/liveexercise.gif)

`@script`
En este curso, aprenderás sobre Python para la ciencia de datos a través de lecciones en vídeo, como esta, y ejercicios interactivos. Tendrás tu propia sesión de Python, donde podrás experimentar e intentar encontrar el código correcto para resolver las instrucciones. Aprenderás de forma práctica mientras recibes comentarios personalizados e inmediatos sobre tu trabajo.


---

## Python

```yaml
type: FullSlide
key: 3f23b93572
```

`@part1`
![guido-hba.png](https://assets.datacamp.com/img/translations/es-ES/production/repositories/288/datasets/fb3e4b8dc114529dafffb37d33f2b2244210d40f/guido-hba.png = 38){{1}}

- Uso general: crear cualquier cosa.{{2}}

- Código abierto. Gratis.{{3}}

- Paquetes de Python, también para ciencia de datos{{4}}

	- Muchas aplicaciones y campos{{5}}

`@script`
Python fue creado por Guido Van Rossum. Aquí puedes ver una foto mía con Guido. Lo que comenzó como un proyecto por gusto pronto se convirtió en un lenguaje de programación generalizado: hoy en día, puedes usar Python para crear prácticamente cualquier tipo de software. ¿Cómo llegamos a esto? Bueno, en primer lugar, Python es de código abierto. Su uso es gratuito. En segundo lugar, es muy fácil crear paquetes en Python, que es código que puedes compartir con otras personas para resolver problemas específicos. Con el paso del tiempo, se han desarrollado cada vez más paquetes diseñados específicamente para la ciencia de datos. Supongamos que quieres crear unas visualizaciones atractivas de las ventas de tu empresa. Existe un paquete para eso. ¿Y qué tal si te conectas a una base de datos para analizar las mediciones de los sensores? También hay un paquete para eso.
A menudo, se hace referencia a Python como la navaja suiza de los lenguajes de programación, ya que permite hacer prácticamente de todo.
En este curso, comenzaremos a desarrollar tus habilidades de programación en ciencia de datos poco a poco, así que presta atención para descubrir todo el potencial de este lenguaje.


---

## Terminal IPython

```yaml
type: FullSlide
key: 43a91a7217
```

`@part1`
**Ejecutar comandos de Python**

![ipython_shell.png](https://assets.datacamp.com/img/translations/es-ES/production/repositories/288/datasets/a9e8440bb8fbd49e4a73e4c36ef1cd677c0dd55f/pyexercise.png = 95)

`@script`
Ahora que eres todo oídos, comencemos a experimentar con Python. Empezaré por el


---

## Terminal IPython

```yaml
type: FullSlide
key: 9c51ee700d
disable_transition: true
```

`@part1`
**Ejecutar comandos de Python**

![ipython_shell_highlighted.png](https://assets.datacamp.com/img/translations/es-ES/production/repositories/288/datasets/dd43cc0183b15b43a072eb0fbab4caa72dee9250/pyexercise_shell.jpg = 95)

`@script`
terminal Python, un lugar donde puedes escribir código Python y ver los resultados inmediatamente. En la interfaz de ejercicios de DataCamp, este terminal se integra aquí. Empecemos por algo sencillo y usemos Python como calculadora.


---

## Terminal IPython

```yaml
type: FullSlide
key: 524e4c20a7
disable_transition: true
```

`@part1`
&nbsp;

![Cálculos en el terminal IPython de DataCamp](https://assets.datacamp.com/img/translations/es-ES/production/repositories/288/datasets/cee32b788a62e4b9a1234ccde56ac9ebb49cfa72/shelladdition.gif = 95)

`@script`
Déjame escribir 4 + 5 y pulsar Intro. Python interpreta lo que has escrito e imprime el resultado del cálculo, 9. El terminal Python que se utiliza aquí no es el original; utilizamos IPython, abreviatura de Interactive Python, una versión mejorada del Python habitual que te resultará útil más adelante.

IPython fue creado por Fernando Pérez y forma parte del ecosistema más amplio de Jupyter. Aparte de trabajar interactivamente con Python, también puedes ejecutar los llamados


---

## Script de Python

```yaml
type: FullSlide
key: 78ef256bc0
```

`@part1`
- Archivos de texto: `.py`{{1}}

- Lista de comandos de Python{{2}}

- Similar a escribir en el terminal IPython{{3}}

![Script de Python en DataCamp](https://assets.datacamp.com/img/translations/es-ES/production/repositories/288/datasets/59f196e96536543a4fb8801228019fc4106f3791/pyexercise_script.jpg = 78){{3}}

`@script`
scripts de Python. Estos scripts de Python son archivos de texto con la extensión (punto) py. Básicamente, es una lista de comandos de Python que se ejecutan, casi como si estuvieras escribiendo los comandos en el terminal, línea por línea.


---

## Script de Python

```yaml
type: FullSlide
key: 717d124175
disable_transition: true
```

`@part1`
![GIF: escribe 4 + 5 en el script y pulsa enviar respuesta. No se muestra ningún resultado.](https://assets.datacamp.com/img/translations/es-ES/production/repositories/288/datasets/2f96e979012e15329cc158d1e0f496aac3539f45/scriptnoprint.gif = 95)

`@script`
Ahora pondremos el comando anterior en un script, que se puede encontrar aquí, en la interfaz de DataCamp. El siguiente paso es ejecutar el script; para ello, haremos clic en Enviar respuesta. Si ejecutas este script en la interfaz de DataCamp, no aparecerá nada en el panel de salida. Debes utilizar explícitamente print en los scripts si deseas generar salida durante la ejecución.


---

## Script de Python

```yaml
type: FullSlide
key: c7a9d02fb6
disable_transition: true
code_zoom: 90
```

`@part1`
![python_script_print.gif](https://assets.datacamp.com/img/translations/es-ES/production/repositories/288/datasets/8b13d046bb54dcb11aa49f0da7363781129d1561/scriptwithprint.gif = 95)

- Utiliza `print()` para generar resultados a partir del script.

`@script`
Envolvamos nuestro cálculo anterior en una llamada de impresión y volvamos a ejecutar el script. Esta vez se genera el mismo resultado que antes. ¡Genial! Poner tu código en scripts de Python en lugar de volver a escribir manualmente cada paso de forma interactiva te ayudará a mantener la estructura y evitará tener que volver a escribir todo una y otra vez si deseas realizar un cambio. Simplemente, realiza el cambio en el script y vuelve a ejecutar todo.


---

## Interfaz de DataCamp

```yaml
type: FullSlide
key: 693ba1cd14
```

`@part1`
![Captura de pantalla de la interfaz de DataCamp](https://assets.datacamp.com/img/translations/es-ES/production/repositories/288/datasets/a9e8440bb8fbd49e4a73e4c36ef1cd677c0dd55f/pyexercise.png)

`@script`
Ahora que ya tienes una idea sobre las diferentes formas de trabajar con Python, te sugiero que pases a los ejercicios. Utiliza el terminal IPython para experimentar y el editor de scripts de Python para codificar la respuesta real. Si haces clic en Enviar respuesta, el script se ejecutará y se comprobará que sea correcto.


---

## ¡Vamos a practicar!

```yaml
type: FinalSlide
key: 7445cd202e
```

`@script`
Empieza a programar y no te olvides de divertirte.

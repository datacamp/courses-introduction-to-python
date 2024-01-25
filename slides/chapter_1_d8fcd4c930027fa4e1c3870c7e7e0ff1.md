---
title: Insert title here
key: d8fcd4c930027fa4e1c3870c7e7e0ff1
video_link:
  hls: >-
    https://videos.datacamp.com/transcoded/course_735/hls-Lesson
    test_1706190998084.master.m3u8
  mp4: 'https://videos.datacamp.com/raw/course_735/Lesson test_1706190998084.mp4'
transformations:
  translateX: 50
  translateY: 0
  scale: 1
---

## Hello Python!

```yaml
type: TitleSlide
key: f743ca8c41
```

`@lower_third`
name: Hugo Bowne-Anderson
title: Data Scientist at DataCamp

`@script`
Hola, mi nombre es Hugo y seré tu anfitrión para Introducción a Python para Ciencia de Datos.

Soy un científico de datos y educador en DataCamp y anfitrión del podcast DataFramed, que debes revisar.

---

## How you will learn

```yaml
type: FullSlide
key: 30ee08a725
disable_transition: true
```

`@part1`
![DataCamp Interface](https://assets.datacamp.com/production/repositories/288/datasets/aeed94c06eb3da9b688eb7ead884366f88539e30/dc_ui.gif)

`@script`
En este curso, aprenderás Python para Ciencia de Datos a través de lecciones en vídeo, como ésta, y ejercicios interactivos. Tendrás tu propia sesión de Python en la que podrás experimentar e intentar dar con el código correcto para resolver las instrucciones. Estás aprendiendo haciendo, mientras recibes retroalimentación personalizada e instantánea sobre tu trabajo.

---

## Python

```yaml
type: FullSlide
key: 3f23b93572
```

`@part1`
![guido-hba.png](https://assets.datacamp.com/production/repositories/288/datasets/fb3e4b8dc114529dafffb37d33f2b2244210d40f/guido-hba.png = 38){{1}}

- General purpose: build anything{{2}}

- Open source! Free!{{3}}

- Python packages, also for data science{{4}}

	- Many applications and fields{{5}}

- Version 3.x - https://www.python.org/downloads/{{6}}

`@script`
Python fue concebido por Guido Van Rossum. Aquí puedes ver una foto mía con Guido. Lo que empezó como un proyecto de hobby, pronto se convirtió en un lenguaje de programación de propósito general: hoy en día, puedes usar Python para construir prácticamente cualquier pieza de software. Pero, ¿cómo ha ocurrido esto? En primer lugar, Python es de código abierto. Su uso es gratuito. En segundo lugar, es muy fácil construir paquetes en Python, que es código que puedes compartir con otras personas para resolver problemas específicos. A lo largo del tiempo, se han desarrollado cada vez más de estos paquetes construidos específicamente para la ciencia de datos. Supongamos que quieres hacer algunas visualizaciones extravagantes de las ventas de tu empresa. Hay un paquete para eso. ¿O qué tal conectarse a una base de datos para analizar las mediciones de un sensor? También hay un paquete para eso.
La gente a menudo se refiere a Python como la navaja suiza de los lenguajes de programación, ya que puedes hacer casi cualquier cosa con él.
En este curso, vamos a empezar a construir sus habilidades de codificación de ciencia de datos poco a poco, así que asegúrese de quedarse para ver lo poderoso que el lenguaje puede ser.

Nuestros cursos se centran en Python 3. Para instalar Python 3 en tu propio sistema, sigue los pasos en esta URL.

---

## IPython Shell

```yaml
type: FullSlide
key: 43a91a7217
```

`@part1`
**Execute Python commands**

![ipython_shell.png](https://assets.datacamp.com/production/repositories/288/datasets/4eee529b34a70821e3a7b5d4d7ce5a929f81225e/ipython_shell.png)

`@script`
Ahora que eres todo ojos y oídos para Python, empecemos a experimentar. Empezaré con el

---

## IPython Shell

```yaml
type: FullSlide
key: 9c51ee700d
disable_transition: true
```

`@part1`
**Execute Python commands**

![ipython_shell_highlighted.png](https://assets.datacamp.com/production/repositories/288/datasets/d4d2c4150da85cc755c22967b400027525daa5ac/ipython_shell_highlighted.png)

`@script`
Python shell, un lugar donde puede escribir código Python y ver inmediatamente los resultados. En la interfaz de ejercicios de DataCamp, este shell está incrustado aquí. Empecemos de forma sencilla y utilicemos Python como calculadora.

---

## IPython Shell

```yaml
type: FullSlide
key: 524e4c20a7
disable_transition: true
```

`@part1`
&nbsp;

![Calculations in DataCamp's IPython shell](https://assets.datacamp.com/production/repositories/288/datasets/2770f695cc46744fde190fc3a41cdc5bd01b5514/ipython_shell.gif)

`@script`
Déjame teclear 4 + 5, y pulsa Intro. Python interpreta lo que has tecleado e imprime el resultado de tu cálculo, 9. El shell de Python que se utiliza aquí no es en realidad el original; estamos utilizando IPython, abreviatura de Interactive Python (Python Interactivo), que es una especie de versión mejorada del Python normal que será útil más adelante.

IPython fue creado por Fernando Pérez y forma parte del amplio ecosistema Jupyter. Aparte de trabajar interactivamente con Python, también puedes hacer que Python ejecute las llamadas

---

## Python Script

```yaml
type: FullSlide
key: 78ef256bc0
```

`@part1`
- Text files - `.py`{{1}}

- List of Python commands{{2}}

- Similar to typing in IPython Shell{{3}}

![Python script in DataCamp](https://assets.datacamp.com/production/repositories/288/datasets/9f41e51af11fff99081aa31fb3dd2a352bb4ac96/python_script.png = 78){{3}}

`@script`
scripts de python. Estos scripts python son simplemente archivos de texto con la extensión (punto) py. Es básicamente una lista de comandos Python que se ejecutan, casi como si estuvieras escribiendo los comandos en el shell tú mismo, línea por línea.

---

## Python Script

```yaml
type: FullSlide
key: 717d124175
disable_transition: true
```

`@part1`
![GIF: typing 4 + 5 in the script and hitting submit answer. No output is shown.](https://assets.datacamp.com/production/repositories/288/datasets/ae0ccbf815741750fdb2ebb4bb7bbf5b14b707d0/python_script_noprint.gif = 96)

`@script`
Pongamos ahora el comando de antes en un script, que se encuentra aquí en la interfaz de DataCamp. El siguiente paso es ejecutar el script haciendo clic en "Enviar respuesta". Si ejecuta este script en la interfaz de DataCamp, no aparecerá nada en el panel de salida. Esto se debe a que, si desea generar resultados durante la ejecución del script, debe utilizar explícitamente la opción de impresión.

---

## Python Script

```yaml
type: FullSlide
key: c7a9d02fb6
disable_transition: true
code_zoom: 90
```

`@part1`
![python_script_print.gif](https://assets.datacamp.com/production/repositories/288/datasets/2d3ab5a6fc88d905270498c03d74442500e47fcf/python_script_print.gif = 96)

- Use `print()` to generate output from script

`@script`
Envolvamos nuestro cálculo anterior en una llamada a print, y volvamos a ejecutar el script. Esta vez, se genera la misma salida que antes, ¡genial! Poner tu código en scripts Python en lugar de volver a escribir manualmente cada paso interactivamente te ayudará a mantener la estructura y evitar volver a escribir todo una y otra vez si quieres hacer un cambio; simplemente haces el cambio en el script, y vuelves a ejecutar todo.

---

## DataCamp Interface

```yaml
type: FullSlide
key: 693ba1cd14
```

`@part1`
![Screenshot of DataCamp interface](https://assets.datacamp.com/production/repositories/288/datasets/6e9856e39fc8e942896d9c91f78d3739ebdbba30/dc_ui.png)

`@script`
Ahora que ya tienes una idea de las diferentes formas de trabajar con Python, te sugiero que te dirijas a los ejercicios. Utiliza IPython Shell para experimentar, y utiliza el editor de scripts de Python para codificar la respuesta real. Si haces clic en Enviar respuesta, tu script se ejecutará y se comprobará si es correcto.

---

## Let's practice!

```yaml
type: FinalSlide
key: 7445cd202e
```

`@script`
Ponte a codificar y no olvides divertirte.

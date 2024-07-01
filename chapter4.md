---
title_meta: Capítulo 4
title: NumPy
description: >-
  O NumPy é um pacote Python fundamental para você praticar a ciência de dados
  com eficiência. Aprenda a trabalhar com ferramentas poderosas na matriz NumPy
  e comece a explorar dados.
attachments:
  slides_link: 'https://projector-video-pdf-converter.datacamp.com/735/chapter4.pdf'
lessons:
  - nb_of_exercises: 5
    title: Numpy
  - nb_of_exercises: 5
    title: Matrizes Numpy 2D
  - nb_of_exercises: 3
    title: 'Numpy: Estatísticas básicas'
---

## NumPy

```yaml
type: VideoExercise
key: f4545baa53
xp: 50
```

`@projector_key`
a0487c26210f6b71ea98f917734cea3a

---

## Sua primeira matriz NumPy

```yaml
type: NormalExercise
key: 84cab9d170
lang: python
xp: 100
skills:
  - 2
```

Agora você vai mergulhar no mundo do beisebol. Ao longo do caminho, você se familiarizará com os conceitos básicos do `numpy`, um pacote avançado para fazer ciência de dados.

Uma lista `baseball` já foi definida no script Python, representando a altura de alguns jogadores de beisebol em centímetros. Você pode adicionar algum código para criar uma matriz `numpy` a partir dela?

`@instructions`
- Importe o pacote `numpy` como `np`, para que você possa fazer referência a `numpy` com `np`.
- Use [`np.array()`](http://docs.scipy.org/doc/numpy-1.10.0/glossary.html#term-array) para criar uma matriz `numpy` a partir de `baseball`. Dê a essa matriz o nome de `np_baseball`.
- Imprima o tipo de `np_baseball` para verificar se você acertou.

`@hint`
- `import numpy as np` você pode fazer isso. Agora, você precisa usar `np.fun_name()` sempre que quiser usar uma função `numpy`.
- [`np.array()`](http://docs.scipy.org/doc/numpy-1.10.0/glossary.html#term-array) deve receber a entrada `baseball`. Atribua o resultado da chamada de função a `np_baseball`.
- Para imprimir o tipo de uma variável `x`, basta digitar `print(type(x))`.

`@pre_exercise_code`
```{python}
import numpy as np
```

`@sample_code`
```{python}
# Import the numpy package as np


baseball = [180, 215, 210, 210, 188, 176, 209, 200]

# Create a numpy array from baseball: np_baseball


# Print out type of np_baseball

```

`@solution`
```{python}
# Import the numpy package as np
import numpy as np

baseball = [180, 215, 210, 210, 188, 176, 209, 200]

# Create a NumPy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out type of np_baseball
print(type(np_baseball))
```

`@sct`
```{python}
predef_msg = "Você não precisa alterar ou remover as variáveis predefinidas."
Ex().has_import("numpy")
Ex().check_correct(
  check_object("np_baseball"),
  multi(
    check_object("baseball", missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
    check_function("numpy.array").check_args(0).has_equal_ast()
  )
)

Ex().has_printout(0)
success_msg("Ótimo trabalho!")
```

---

## Altura dos jogadores de beisebol

```yaml
type: NormalExercise
key: e7e25a89ea
lang: python
xp: 100
skills:
  - 2
```

Você é um grande fã de beisebol. Você decide ligar para o site MLB (Major League Baseball) e pedir mais algumas estatísticas sobre a altura dos principais jogadores. Eles transmitem dados sobre mais de mil jogadores, que são armazenados como uma lista regular do Python: `height_in`. A altura é expressa em polegadas. Você pode criar uma matriz `numpy` com ela e converter as unidades para metros?

`height_in` já está disponível e o pacote `numpy` está carregado, para que você possa começar imediatamente (Fonte: stat.ucla.edu).

`@instructions`
- Crie uma matriz `numpy` a partir de `height_in`. Dê a essa nova matriz o nome de `np_height_in`.
- Imprimir `np_height_in`.
- Multiplique `np_height_in` por `0.0254` para converter todas as medidas de altura de polegadas para metros. Armazene os novos valores em uma nova matriz, `np_height_m`.
- Imprima o site `np_height_m` e verifique se a saída faz sentido.

`@hint`
- Use [`np.array()`](http://docs.scipy.org/doc/numpy-1.10.0/glossary.html#term-array) e passe-o para `height`. Armazene o resultado em `np_height_in`.
- Para imprimir uma variável `x`, digite `print(x)` no script Python.
- Faça os cálculos como se `np_height_in` fosse um único número: `np_height_in * conversion_factor` é parte da resposta.
- Para imprimir uma variável `x`, digite `print(x)` no script Python.

`@pre_exercise_code`
```{python}
import pandas as pd
mlb = pd.read_csv("http://assets.datacamp.com/course/intro_to_python/baseball.csv")
height_in = mlb['Height'].tolist()
import numpy as np
```

`@sample_code`
```{python}
# Import numpy
import numpy as np

# Create a numpy array from height_in: np_height_in


# Print out np_height_in


# Convert np_height_in to m: np_height_m


# Print np_height_m

```

`@solution`
```{python}
# Import numpy
import numpy as np

# Create a numpy array from height_in: np_height_in
np_height_in = np.array(height_in)

# Print out np_height_in
print(np_height_in)

# Convert np_height_in to m: np_height_m
np_height_m = np_height_in * 0.0254

# Print np_height_m
print(np_height_m)
```

`@sct`
```{python}
Ex().has_import("numpy", same_as = False)

Ex().check_correct(
  has_printout(0),
  check_correct(
    check_object('np_height_in').has_equal_value(),
    check_function('numpy.array').check_args(0).has_equal_ast()
  )
)

Ex().check_correct(
  has_printout(1),
  check_object("np_height_m").has_equal_value(incorrect_msg = "Use `np_height_in * 0.0254` para calcular `np_height_m`.")
)

success_msg("Legal! Num piscar de olhos, `numpy` realiza multiplicações em mais de 1000 medições de altura.")

```

---

## Efeitos colaterais do NumPy

```yaml
type: MultipleChoiceExercise
key: 3662ff6637
lang: python
xp: 50
skills:
  - 2
```

`numpy` é excelente para fazer aritmética vetorial. Se você comparar sua funcionalidade com as listas Python comuns, no entanto, algumas coisas mudaram.

Em primeiro lugar, as matrizes `numpy` não podem conter elementos com tipos diferentes.
Em segundo lugar, os operadores aritméticos típicos, como `+`, `-`, `*` e `/` têm um significado diferente para listas regulares do Python e matrizes `numpy`.

Algumas linhas de código foram fornecidas para você. Experimente e escolha a que mais combina com você:

```
np.array([True, 1, 2]) + np.array([3, 4, False])
```

O pacote `numpy` já foi importado como `np`.

`@possible_answers`
- `np.array([True, 1, 2, 3, 4, False])`
- `np.array([4, 3, 0]) + np.array([0, 2, 2])`
- `np.array([1, 1, 2]) + np.array([3, 4, -1])`
- `np.array([0, 1, 2, 3, 4, 5])`

`@hint`
- Copie os diferentes trechos de código e cole-os no Shell IPython. Pressione **Enter** para executar o código e ver qual saída corresponde à gerada por `np.array([True, 1, 2]) + np.array([3, 4, False])`.

`@pre_exercise_code`
```{python}
import numpy as np
```

`@sct`
```{python}
msg1 = msg3 = msg4 = "Incorreto. Experimente os diferentes blocos de código e veja qual corresponde ao bloco de código alvo."
msg2 = "Ótimo trabalho! `True` é convertido para 1, `False` é convertido para 0."
Ex().has_chosen(2, [msg1, msg2, msg3, msg4])
```

---

## Subconjunto de matrizes NumPy

```yaml
type: NormalExercise
key: fcb2a9007b
lang: python
xp: 100
skills:
  - 2
```

O subconjunto (usando a notação de colchetes em listas ou matrizes) funciona exatamente da mesma forma com listas e matrizes.

Este exercício já tem duas listas, `height_in` e `weight_lb`, carregadas em segundo plano para você. Elas contêm a altura e o peso dos jogadores do MLB como listas regulares. Ele também tem duas listas de matriz `numpy`, `np_weight_lb` e `np_height_in`, preparadas para você.

`@instructions`
- Subconjunto `np_weight_lb` imprimindo o elemento no índice 50.
- Imprima uma subvariedade de `np_height_in` que contenha os elementos no índice 100 até o índice 110 **, inclusive**.

`@hint`
- Certifique-se de envolver uma chamada `print()` em suas operações de subconjunto.
- Use `[100:111]` para obter os elementos do índice 100 até o índice 110, inclusive.

`@pre_exercise_code`
```{python}
import pandas as pd
mlb = pd.read_csv("http://assets.datacamp.com/course/intro_to_python/baseball.csv")
height_in = mlb['Height'].tolist()
weight_lb = mlb['Weight'].tolist()
```

`@sample_code`
```{python}
import numpy as np

np_weight_lb = np.array(weight_lb)
np_height_in = np.array(height_in)

# Print out the weight at index 50


# Print out sub-array of np_height_in: index 100 up to and including index 110

```

`@solution`
```{python}
import numpy as np

np_weight_lb = np.array(weight_lb)
np_height_in = np.array(height_in)

# Print out the weight at index 50
print(np_weight_lb[50])

# Print out sub-array of np_height_in: index 100 up to and including index 110
print(np_height_in[100:111])
```

`@sct`
```{python}
Ex().has_import("numpy", same_as=False)
msg = "Você não precisa alterar ou remover as variáveis predefinidas."
Ex().multi(
    check_object("np_height_in", missing_msg=msg).has_equal_value(incorrect_msg = msg),
    check_object("np_weight_lb", missing_msg=msg).has_equal_value(incorrect_msg = msg)
)

Ex().has_printout(0)
Ex().has_printout(1)

success_msg("Legal! Hora de aprender algo novo: arrays 2D do NumPy!")
```

---

## Matrizes 2D NumPy

```yaml
type: VideoExercise
key: 1241efac7a
xp: 50
```

`@projector_key`
ae3238dcc7feb9adecfee0c395fc8dc8

---

## Sua primeira matriz 2D do NumPy

```yaml
type: NormalExercise
key: 5cb045bb13
lang: python
xp: 100
skills:
  - 2
```

Antes de trabalhar nos dados reais do MLB, vamos tentar criar uma matriz 2D `numpy` a partir de uma pequena lista de listas.

Neste exercício, `baseball` é uma lista de listas. A lista principal contém 4 elementos. Cada um desses elementos é uma lista que contém a altura e o peso de 4 jogadores de beisebol, nessa ordem. `baseball` já está codificado para você no script.

`@instructions`
- Use [`np.array()`](http://docs.scipy.org/doc/numpy-1.10.0/glossary.html#term-array) para criar uma matriz 2D `numpy` a partir de `baseball`. Dê a você o nome `np_baseball`.
- Imprima o tipo de `np_baseball`.
- Imprima o atributo `shape` de `np_baseball`. Use `np_baseball.shape`.

`@hint`
- `baseball` já está codificado para você no script. Chame [`np.array()`](http://docs.scipy.org/doc/numpy-1.10.0/glossary.html#term-array) e armazene a matriz 2D `numpy` resultante em `np_baseball`.
- Use [`print()`](https://docs.python.org/3/library/functions.html#print) em combinação com [`type()`](https://docs.python.org/3/library/functions.html#type) para a segunda instrução.
- `np_baseball.shape` Você terá as dimensões do site `np_baseball`. Certifique-se de envolver uma chamada [`print()`](https://docs.python.org/3/library/functions.html#print) ao redor dele.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
import numpy as np

baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

# Create a 2D numpy array from baseball: np_baseball


# Print out the type of np_baseball


# Print out the shape of np_baseball

```

`@solution`
```{python}
import numpy as np

baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

# Create a 2D numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out the type of np_baseball
print(type(np_baseball))

# Print out the shape of np_baseball
print(np_baseball.shape)
```

`@sct`
```{python}
msg = "Você não precisa alterar ou remover as variáveis predefinidas."
Ex().check_object("baseball", missing_msg=msg).has_equal_value(incorrect_msg = msg)
Ex().has_import("numpy", same_as = False)

Ex().check_correct(
    multi(
        has_printout(0),
        has_printout(1)
    ),
    check_correct(
        check_object('np_baseball').has_equal_value(),
        check_function('numpy.array').check_args(0).has_equal_ast()
    )
)

success_msg("Ótimo! Agora você está pronto para converter os dados reais da MLB para um array 2D `numpy`!")
```

---

## Dados de beisebol em formato 2D

```yaml
type: NormalExercise
key: 5df25d0b7b
lang: python
xp: 100
skills:
  - 2
```

Você percebe que faz mais sentido reestruturar todas essas informações em uma matriz 2D `numpy`.

Você tem uma lista de listas do Python. Nessa lista de listas, cada sub-lista representa a altura e o peso de um único jogador de beisebol. O nome dessa lista é `baseball` e ela já foi carregada para você (embora você não consiga vê-la).

Armazene os dados como uma matriz 2D para desbloquear a funcionalidade extra do site `numpy`.

`@instructions`
- Use [`np.array()`](http://docs.scipy.org/doc/numpy-1.10.0/glossary.html#term-array) para criar uma matriz 2D `numpy` a partir de `baseball`. Dê a você o nome `np_baseball`.
- Imprima o atributo `shape` de `np_baseball`.

`@hint`
- `baseball` já está disponível no ambiente Python. Chame [`np.array()`](http://docs.scipy.org/doc/numpy-1.10.0/glossary.html#term-array) e armazene a matriz 2D `numpy` resultante em `np_baseball`.
- `np_baseball.shape` Você terá as dimensões do site `np_baseball`. Certifique-se de envolver uma chamada `print()`em torno dele.

`@pre_exercise_code`
```{python}
import pandas as pd
baseball = pd.read_csv("http://assets.datacamp.com/course/intro_to_python/baseball.csv")[['Height', 'Weight']].to_numpy().tolist()
import numpy as np
```

`@sample_code`
```{python}
import numpy as np

# Create a 2D numpy array from baseball: np_baseball
np_baseball = 

# Print out the shape of np_baseball

```

`@solution`
```{python}
import numpy as np

# Create a 2D numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out the shape of np_baseball
print(np_baseball.shape)
```

`@sct`
```{python}
Ex().has_import("numpy", same_as = False)

Ex().check_correct(
    has_printout(0),
    check_correct(
        check_object('np_baseball').has_equal_value(),
        check_function('numpy.array').check_args(0).has_equal_ast()
    )
)

success_msg("Legal! Hora de mostrar alguns recursos incríveis dos arrays multidimensionais do `numpy`!")
```

---

## Subconjunto de matrizes NumPy 2D

```yaml
type: NormalExercise
key: aeca4977f0
lang: python
xp: 100
skills:
  - 2
```

Se a sua matriz 2D `numpy` tiver uma estrutura regular, ou seja, cada linha e coluna tiver um número fixo de valores, as formas complicadas de subconjunto se tornarão muito fáceis. Dê uma olhada no código abaixo, onde os elementos `"a"` e `"c"` são extraídos de uma lista de listas.

```
# numpy
import numpy as np
np_x = np.array(x)
np_x[:, 0]
```

Os índices antes da vírgula se referem às linhas, enquanto os índices após a vírgula se referem às colunas. O endereço `:` é para fatiar; neste exemplo, ele diz ao Python para incluir todas as linhas.

`@instructions`
- Imprima a 50ª linha de `np_baseball`.
- Crie uma nova variável, `np_weight_lb`, contendo toda a segunda coluna de `np_baseball`.
- Selecione a altura (primeira coluna) do 124º jogador de beisebol em `np_baseball` e imprima-a.

`@hint`
- Você precisa do índice de linha 49 na primeira instrução! Mais especificamente, você deverá usar `[49, :]`.
- Para selecionar toda a segunda coluna, você precisará de `[:, 1]`.
- Para a última instrução, use `[123, 0]`; não se esqueça de envolver tudo isso em uma instrução. [`print()`](https://docs.python.org/3/library/functions.html#print) declaração.

`@pre_exercise_code`
```{python}
import pandas as pd
baseball = pd.read_csv("http://assets.datacamp.com/course/intro_to_python/baseball.csv")[['Height', 'Weight']].to_numpy().tolist()
import numpy as np
```

`@sample_code`
```{python}
import numpy as np

np_baseball = np.array(baseball)

# Print out the 50th row of np_baseball


# Select the entire second column of np_baseball: np_weight_lb


# Print out height of 124th player

```

`@solution`
```{python}
import numpy as np

np_baseball = np.array(baseball)

# Print out the 50th row of np_baseball
print(np_baseball[49,:])

# Select the entire second column of np_baseball: np_weight_lb
np_weight_lb = np_baseball[:,1]

# Print out height of 124th player
print(np_baseball[123, 0])
```

`@sct`
```{python}
msg = "Você não precisa alterar ou remover as variáveis predefinidas."
Ex().multi(
    has_import("numpy", same_as = False),
    check_object("np_baseball", missing_msg=msg).has_equal_value(incorrect_msg = msg)
)

Ex().has_printout(0)

Ex().check_object('np_weight_lb').has_equal_value(incorrect_msg = "Você pode usar `np_baseball[:,1]` para definir `np_weight_lb`. Isso selecionará toda a primeira coluna.")

Ex().has_printout(1)

success_msg("Isso está indo bem!")
```

---

## Aritmética 2D

```yaml
type: NormalExercise
key: 1c2378b677
lang: python
xp: 100
skills:
  - 2
```

As matrizes 2D `numpy` podem realizar cálculos elemento a elemento, como as matrizes `numpy`.

`np_baseball` está codificado para você; trata-se novamente de uma matriz 2D `numpy` com 3 colunas que representam altura (em polegadas), peso (em libras) e idade (em anos). `baseball` está disponível como uma lista regular de listas e `updated` está disponível como uma matriz 2D numpy.

`@instructions`
- Você conseguiu obter as alterações de altura, peso e idade de todos os jogadores de beisebol. Ele está disponível como uma matriz 2D `numpy`, `updated`. Adicione `np_baseball` e `updated` e imprima o resultado.
- Você deseja converter as unidades de altura e peso para o sistema métrico (metros e quilogramas, respectivamente). Como primeira etapa, crie uma matriz `numpy` com três valores: `0.0254`, `0.453592` e `1`. Dê a essa matriz o nome de `conversion`.
- Multiplique `np_baseball` por `conversion` e imprima o resultado.

`@hint`
- `np_baseball + updated` fará uma soma de elementos das duas matrizes `numpy`.
- Crie uma matriz `numpy` com `np.array()`; a entrada é uma lista regular do Python com três elementos.
- `np_baseball * conversion` funcionará, sem trabalho extra. Experimente! Certifique-se de envolvê-lo em uma chamada para `print()`.

`@pre_exercise_code`
```{python}
import pandas as pd
import numpy as np
baseball = pd.read_csv("http://assets.datacamp.com/course/intro_to_python/baseball.csv")[['Height', 'Weight', 'Age']].to_numpy().tolist()
n = len(baseball)
updated = np.array(pd.read_csv("http://assets.datacamp.com/course/intro_to_python/update.csv", header = None))
import numpy as np
```

`@sample_code`
```{python}
import numpy as np

np_baseball = np.array(baseball)

# Print out addition of np_baseball and updated


# Create numpy array: conversion


# Print out product of np_baseball and conversion

```

`@solution`
```{python}
import numpy as np

np_baseball = np.array(baseball)

# Print out addition of np_baseball and updated
print(np_baseball + updated)

# Create numpy array: conversion
conversion = np.array([0.0254, 0.453592, 1])

# Print out product of np_baseball and conversion
print(np_baseball * conversion)
```

`@sct`
```{python}
Ex().has_import("numpy")

msg = "Você não precisa alterar ou remover as variáveis predefinidas."
Ex().check_object("np_baseball", missing_msg=msg).has_equal_value(incorrect_msg = msg)

Ex().has_printout(0)

Ex().check_correct(
    has_printout(1),
    check_correct(
        check_object('conversion').has_equal_value(),
        check_function('numpy.array', index = 1).check_args(0).has_equal_value()
    )    
)

success_msg("Ótimo trabalho! Note como com muito pouco código, você pode alterar todos os valores na sua estrutura de dados `numpy` de uma maneira muito específica. Isso será muito útil no seu futuro como cientista de dados!")
```

---

## NumPy: Estatísticas básicas

```yaml
type: VideoExercise
key: 287995e488
xp: 50
```

`@projector_key`
34495ba457d74296794d2a122c9b6e19

---

## Média versus mediana

```yaml
type: NormalExercise
key: 509c588eb6
lang: python
xp: 100
skills:
  - 2
```

Agora você sabe como usar as funções do `numpy` para ter uma noção melhor dos seus dados. 

Os dados do beisebol estão disponíveis como uma matriz 2D `numpy` com 3 colunas (altura, peso, idade) e 1015 linhas. O nome dessa matriz `numpy` é `np_baseball`. Depois de reestruturar os dados, no entanto, você percebe que alguns valores de altura estão anormalmente altos. Siga as instruções e descubra qual estatística resumida é mais adequada se você estiver lidando com os chamados _outliers_. `np_baseball` está disponível.

`@instructions`
- Crie uma matriz `numpy` `np_height_in` que seja igual à primeira coluna de `np_baseball`.
- Imprima a média de `np_height_in`.
- Imprima a mediana de `np_height_in`.

`@hint`
- Use o subconjunto 2D `numpy`: `[:,0]` é uma parte da solução.
- Se `numpy` for importado como `np`, você poderá usar [`np.mean()`](http://docs.scipy.org/doc/numpy-1.10.0/reference/generated/numpy.mean.html) para obter a média de uma matriz NumPy. Não se esqueça de incluir uma [`print()`](https://docs.python.org/3/library/functions.html#print) chamada.
- Para a última instrução, use [`np.median()`](http://docs.scipy.org/doc/numpy-1.10.0/reference/generated/numpy.median.html).

`@pre_exercise_code`
```{python}
import pandas as pd
np_baseball = pd.read_csv("http://assets.datacamp.com/course/intro_to_python/baseball.csv")[['Height', 'Weight', 'Age']].to_numpy()
np_baseball[slice(0, 1015, 50), 0] = np_baseball[slice(0, 1015, 50), 0]*1000
import numpy as np
```

`@sample_code`
```{python}
import numpy as np

# Create np_height_in from np_baseball


# Print out the mean of np_height_in


# Print out the median of np_height_in

```

`@solution`
```{python}
import numpy as np

# Create np_height_in from np_baseball
np_height_in = np_baseball[:,0]

# Print out the mean of np_height_in
print(np.mean(np_height_in))

# Print out the median of np_height_in
print(np.median(np_height_in))
```

`@sct`
```{python}
Ex().has_import("numpy", same_as = False)

Ex().check_object("np_height_in").has_equal_value(incorrect_msg = "Você pode usar `np_baseball[:,0]` para selecionar a primeira coluna de `np_baseball`"),

Ex().check_correct(
    has_printout(0),
    check_function('numpy.mean').has_equal_value()
)

Ex().check_correct(
    has_printout(1),
    check_function('numpy.median').has_equal_value()
)

success_msg("Uma altura média de 1586 polegadas, isso não parece certo, não é? No entanto, a mediana não parece ser afetada pelos valores atípicos: 74 polegadas faz todo o sentido. Sempre é uma boa ideia verificar tanto a mediana quanto a média, para ter uma ideia sobre a distribuição geral de todo o conjunto de dados.")

```

---

## Explore os dados do beisebol

```yaml
type: NormalExercise
key: '4409948807'
lang: python
xp: 100
skills:
  - 2
```

Como a média e a mediana estão muito distantes, você decide reclamar no site MLB. Eles encontram o erro e enviam os dados corrigidos para você. Ele está novamente disponível como uma matriz 2D NumPy `np_baseball`, com três colunas.

O script Python no editor já inclui o código para imprimir mensagens informativas com as diferentes estatísticas resumidas e o site `numpy` já está carregado como `np`. Você pode terminar o trabalho? `np_baseball` está disponível.

`@instructions`
- O código para imprimir a altura média já está incluído. Complete o código para a altura média. Substitua `None` pelo código correto.
- Use [`np.std()`](http://docs.scipy.org/doc/numpy-1.10.0/reference/generated/numpy.std.html) na primeira coluna de `np_baseball` para calcular `stddev`. Substitua `None` pelo código correto.
- Os grandes jogadores tendem a ser mais pesados? Use [`np.corrcoef()`](http://docs.scipy.org/doc/numpy-1.10.0/reference/generated/numpy.corrcoef.html) para armazenar a correlação entre a primeira e a segunda coluna de `np_baseball` em `corr`. Substitua `None` pelo código correto.

`@hint`
- Use [`np.median()`](http://docs.scipy.org/doc/numpy-1.10.0/reference/generated/numpy.median.html) para calcular a mediana. Certifique-se de selecionar a coluna correta primeiro!
- Subsetar a mesma coluna ao calcular o desvio padrão com [`np.std()`](http://docs.scipy.org/doc/numpy-1.10.0/reference/generated/numpy.std.html).
- Use `np_baseball[:, 0]` e `np_baseball[:, 1]` para selecionar a primeira e a segunda colunas; essas são as entradas para o [`np.corrcoef()`](http://docs.scipy.org/doc/numpy-1.10.0/reference/generated/numpy.corrcoef.html).

`@pre_exercise_code`
```{python}
import pandas as pd
np_baseball = pd.read_csv("http://assets.datacamp.com/course/intro_to_python/baseball.csv")[['Height', 'Weight', 'Age']].to_numpy()
import numpy as np
```

`@sample_code`
```{python}
avg = np.mean(np_baseball[:,0])
print("Average: " + str(avg))

# Print median height
med = ____
print("Median: " + str(med))

# Print out the standard deviation on height
stddev = ____
print("Standard Deviation: " + str(stddev))

# Print out correlation between first and second column
corr = ____
print("Correlation: " + str(corr))
```

`@solution`
```{python}
avg = np.mean(np_baseball[:,0])
print("Average: " + str(avg))

# Print median height
med = np.median(np_baseball[:,0])
print("Median: " + str(med))

# Print out the standard deviation on height
stddev = np.std(np_baseball[:,0])
print("Standard Deviation: " + str(stddev))

# Print out correlation between first and second column
corr = np.corrcoef(np_baseball[:,0], np_baseball[:,1])
print("Correlation: " + str(corr))
```

`@sct`
```{python}
msg = "Você não deve alterar ou remover a variável `avg` predefinida."
Ex().check_object("avg", missing_msg=msg).has_equal_value(incorrect_msg=msg)

missing = "Você usou `np.median()` para calcular a mediana?"
incorrect = "Para calcular `med`, passe a primeira coluna de `np_baseball` para `numpy.median()`. O exemplo de `np.mean()` mostra como é feito."
Ex().check_correct(
  check_object("med").has_equal_value(),
  check_function("numpy.median", index=0, missing_msg=missing).check_args(0).has_equal_value(incorrect_msg=incorrect)
)

missing = "Você usou `np.std()` para calcular o desvio padrão?"
incorrect = "Para calcular `stddev`, passe a primeira coluna de `np_baseball` para `numpy.std()`. O exemplo de `np.mean()` mostra como é feito."
Ex().check_correct(
  check_object("stddev").has_equal_value(),
  check_function("numpy.std", index=0, missing_msg=missing).check_args(0).has_equal_value(incorrect_msg=incorrect)
)

missing = "Você usou `np.corrcoef()` para calcular a correlação?"
incorrect1 = "Para calcular `corr`, o primeiro argumento para `np.corrcoef()` deve ser a primeira coluna de `np_baseball`, semelhante ao que fez antes."
incorrect2 = "Para calcular `corr`, o segundo argumento para `np.corrcoef()` deve ser a segunda coluna de `np_baseball`. Em vez de `[:,0]`, use `[:,1]` desta vez."
Ex().check_correct(
  check_object("corr").has_equal_value(),
  check_function("numpy.corrcoef", index=0, missing_msg=missing).multi(
    check_args(0, missing_msg=incorrect1).has_equal_value(incorrect_msg=incorrect1),
    check_args(1, missing_msg=incorrect2).has_equal_value(incorrect_msg=incorrect2)
  )
)

success_msg("Ótimo! Hora de usar todas as suas novas habilidades em ciência de dados no último exercício!")

```

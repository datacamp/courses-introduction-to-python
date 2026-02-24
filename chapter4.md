---
title_meta: Capítulo 4
title: NumPy
description: >-
  O NumPy é um pacote Python fundamental para a prática eficiente da ciência de
  dados. Aprenda a trabalhar com ferramentas poderosas em uma matriz do NumPy e
  comece a analisar dados.
attachments:
  slides_link: 'https://projector-video-pdf-converter.datacamp.com/735/chapter4.pdf'
lessons:
  - nb_of_exercises: 5
    title: Numpy
  - nb_of_exercises: 5
    title: Matrizes 2D do NumPy
  - nb_of_exercises: 3
    title: 'Numpy: estatísticas básicas'
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

## Sua primeira matriz do NumPy

```yaml
type: NormalExercise
key: 84cab9d170
lang: python
xp: 100
skills:
  - 2
```

Agora você vai mergulhar no mundo do beisebol. Ao longo do caminho, você se familiarizará com os conceitos básicos de `numpy`, um pacote avançado para fazer ciência de dados.

Uma lista `baseball` já foi definida no script Python, representando a altura de alguns jogadores de beisebol em centímetros. Você pode incluir um código para criar uma matriz do `numpy` a partir dela?

`@instructions`
- Importe o pacote `numpy` como `np`, para que você possa fazer referência a `numpy` com `np`.
- Use `np.array()` para criar uma matriz do `numpy` a partir de `baseball`. Chame essa matriz de `np_baseball`.
- Imprima o tipo de `np_baseball` para conferir se está certo.

`@hint`
- `import numpy as np` resolve o problema. Agora, você precisa usar `np.fun_name()` sempre que quiser utilizar uma função do `numpy`.
- `np.array()` deve receber a entrada `baseball`. Atribua o resultado da chamada da função a `np_baseball`.
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
predef_msg = "Você não precisa mudar ou remover as variáveis predefinidas."
Ex().has_import("numpy")
Ex().check_correct(
  check_object("np_baseball"),
  multi(
    check_object("baseball", missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
    check_function("numpy.array").check_args(0).has_equal_ast()
  )
)

Ex().has_printout(0)
success_msg("Mandou bem!")
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

Você é um grande fã de beisebol. Você decide ligar para a MLB (Major League Baseball) e pedir mais algumas estatísticas sobre a altura dos principais jogadores. Ela transmite dados sobre mais de mil jogadores, que são armazenados como uma lista comum do Python: `height_in`. A altura está expressa em polegadas. Você consegue criar uma matriz do `numpy` com ela e converter a unidade em metros?

`height_in` já está disponível e o pacote `numpy` está carregado, portanto você pode começar imediatamente (fonte: stat.ucla.edu).

`@instructions`
- Crie uma matriz do `numpy` a partir de `height_in`. Chame essa nova matriz de `np_height_in`.
- Imprima `np_height_in`.
- Multiplique `np_height_in` por `0.0254` para converter todas as medidas de altura de polegadas em metros. Armazene os novos valores em uma nova matriz, `np_height_m`.
- Imprima `np_height_m` e verifique se a saída faz sentido.

`@hint`
- Use `np.array()` e passe `height` nela. Armazene o resultado em `np_height_in`.
- Para imprimir uma variável `x`, digite `print(x)` no script Python.
- Faça os cálculos como se `np_height_in` fosse um único número: `np_height_in * conversion_factor` é parte da resposta.
- Para imprimir uma variável `x`, digite `print(x)` no script Python.

`@pre_exercise_code`
```{python}
import pandas as pd
mlb = pd.read_csv("https://assets.datacamp.com/course/intro_to_python/baseball.csv")
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

success_msg("Legal! Num piscar de olhos, o `numpy` realiza multiplicações em mais de 1000 medições de altura.")
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

O `numpy` é ótimo para fazer aritmética vetorial. Mas, se você comparar como funciona com as listas normais do Python, algumas coisas são diferentes.

Primeiro,`numpy`as matrizes não podem ter elementos de tipos diferentes. Se você misturar tipos, como booleanos e inteiros, eles `numpy`são automaticamente convertidos para um tipo comum. Booleanos como`True`e`False`são tratados como`1`e`0`quando combinados com números, então a matriz acaba como inteiros.

Em segundo lugar, os operadores aritméticos típicos, como `+`, `-`, `*` e `/`, têm um significado diferente nas listas comuns do Python e matrizes do `numpy`.

Escolha o código que dá o seguinte resultado:

```
np.array([True, 1, 2]) + np.array([3, 4, False])
```

O pacote `numpy` já foi importado como `np`. Você pode rodar cada opção no IPython Shell pra ver o resultado.

`@possible_answers`
- `np.array([True, 1, 2, 3, 4, False])`
- `np.array([4, 3, 0]) + np.array([0, 2, 2])`
- `np.array([1, 1, 2]) + np.array([3, 4, -1])`
- `np.array([0, 1, 2, 3, 4, 5])`

`@hint`
- Copie os diferentes trechos de código e cole-os no Shell IPython. Aperte **Enter** para executar o código e veja qual saída corresponde à gerada por `np.array([True, 1, 2]) + np.array([3, 4, False])`.

`@pre_exercise_code`
```{python}
import numpy as np
```

`@sct`
```{python}
msg1 = msg3 = msg4 = "Incorreto. Experimente os diferentes blocos de código e veja qual deles corresponde ao bloco de código alvo."
msg2 = "Ótimo trabalho! `True` é convertido para 1, `False` é convertido para 0."
Ex().has_chosen(2, [msg1, msg2, msg3, msg4])
```

---

## Subdivisão de matrizes do NumPy

```yaml
type: NormalExercise
key: fcb2a9007b
lang: python
xp: 100
skills:
  - 2
```

A subdivisão (uso da notação de colchetes com listas ou matrizes) funciona exatamente da mesma forma com listas e matrizes.

Este exercício já tem duas listas, `height_in` e `weight_lb`, carregadas em segundo plano para você. Elas contêm a altura e o peso dos jogadores da MLB como listas comuns. Também tem duas listas em matrizes do `numpy`, `np_weight_lb` e `np_height_in`, prontas para você.

`@instructions`
- Subdivida `np_weight_lb` imprimindo o elemento no índice 50.
- Imprima uma submatriz de `np_height_in` que contenha os elementos no índice 100 até o índice 110 **, incluindo este último**.

`@hint`
- Lembre-se de envolver uma chamada `print()` nas operações de subdivisão.
- Use `[100:111]` para obter os elementos do índice 100 até o índice 110, incluindo este último.

`@pre_exercise_code`
```{python}
import pandas as pd
mlb = pd.read_csv("https://assets.datacamp.com/course/intro_to_python/baseball.csv")
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
msg = "Você não precisa mudar ou remover as variáveis predefinidas."
Ex().multi(
    check_object("np_height_in", missing_msg=msg).has_equal_value(incorrect_msg=msg),
    check_object("np_weight_lb", missing_msg=msg).has_equal_value(incorrect_msg=msg)
)

Ex().has_printout(0)
Ex().has_printout(1)

success_msg("Legal! Hora de aprender algo novo: arrays 2D do NumPy!")
```

---

## Matrizes 2D do NumPy

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

Antes de trabalhar com os dados reais da MLB, vamos tentar criar uma matriz 2D do `numpy` a partir de uma pequena lista de listas.

Neste exercício, `baseball` é uma lista de listas. A lista principal contém 4 elementos. Cada um desses elementos é uma lista que contém a altura e o peso de 4 jogadores de beisebol, nessa ordem. `baseball` já está codificado para você no script.

`@instructions`
- Use `np.array()` para criar uma matriz 2D do `numpy` a partir de `baseball`. Chame-a de `np_baseball`.
- Imprima o tipo de `np_baseball`.
- Imprima o atributo `shape` de `np_baseball`. Use `np_baseball.shape`.

`@hint`
- `baseball` já está codificado para você no script. Chame `np.array()` com ela e armazene a matriz 2D resultante do `numpy` em `np_baseball`.
- Use `print()` em combinação com `type()` na segunda instrução.
- `np_baseball.shape` apresenta as dimensões de `np_baseball`. Lembre-se de envolvê-lo em uma chamada `print()`.

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
msg = "Você não precisa mudar ou remover as variáveis predefinidas."
Ex().check_object("baseball", missing_msg=msg).has_equal_value(incorrect_msg=msg)
Ex().has_import("numpy", same_as=False)

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

success_msg("Ótimo! Agora você está pronto para converter os dados reais da MLB em um array 2D do `numpy`!")
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

Você percebe que faz mais sentido reestruturar todas essas informações em uma matriz 2D do `numpy`.

Você tem uma lista de listas no Python. Nessa lista de listas, cada sublista representa a altura e o peso de um único jogador de beisebol. O nome dessa lista é `baseball`, e ela já foi carregada para você (mesmo que não consiga ver).

Armazene os dados como uma matriz 2D para ter acesso a mais funcionalidades do `numpy`.

`@instructions`
- Use `np.array()` para criar uma matriz 2D do `numpy` a partir de `baseball`. Chame-a de `np_baseball`.
- Imprima o atributo `shape` de `np_baseball`.

`@hint`
- `baseball` já está disponível no ambiente Python. Chame `np.array()` com ela e armazene a matriz 2D resultante do `numpy` em `np_baseball`.
- `np_baseball.shape` apresenta as dimensões de `np_baseball`. Lembre-se de envolvê-lo em uma chamada `print()`.

`@pre_exercise_code`
```{python}
import pandas as pd
baseball = pd.read_csv("https://assets.datacamp.com/course/intro_to_python/baseball.csv")[['Height', 'Weight']].to_numpy().tolist()
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

success_msg("Massa! Hora de mostrar alguns recursos incríveis dos arrays multidimensionais do `numpy`!")
```

---

## Subdivisão de matrizes 2D do NumPy

```yaml
type: NormalExercise
key: aeca4977f0
lang: python
xp: 100
skills:
  - 2
```

Se sua matriz 2D do `numpy` tiver uma estrutura regular, ou seja, cada linha e coluna tiver um número fixo de valores, as formas complicadas de subdivisão ficarão muito fáceis. Dê uma olhada no código abaixo, em que os elementos `"a"` e `"c"` são extraídos de uma lista de listas.

```
# numpy
import numpy as np
np_x = np.array(x)
np_x[:, 0]
```

Os índices antes da vírgula se referem às linhas, enquanto os índices após a vírgula se referem às colunas. O `:` serve para fatiar; neste exemplo, ele diz ao Python para incluir todas as linhas.

`@instructions`
- Imprima a 50ª linha de `np_baseball`.
- Crie uma nova variável, `np_weight_lb`, contendo a segunda coluna inteira de `np_baseball`.
- Selecione a altura (primeira coluna) do 124º jogador de beisebol em `np_baseball` e imprima-a.

`@hint`
- Você precisa do índice de linha 49 na primeira instrução! Mais especificamente, você deve usar `[49, :]`.
- Para selecionar a segunda coluna inteira, você precisa de `[:, 1]`.
- Na última instrução, use `[123, 0]`; não se esqueça de envolver tudo em uma instrução `print()`.

`@pre_exercise_code`
```{python}
import pandas as pd
baseball = pd.read_csv("https://assets.datacamp.com/course/intro_to_python/baseball.csv")[['Height', 'Weight']].to_numpy().tolist()
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

success_msg("Está indo bem!")
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

Matrizes 2D do `numpy` podem fazer cálculos elemento por elemento, como matrizes do `numpy`.

`np_baseball` está codificado para você; trata-se novamente de uma matriz 2D do `numpy` com 3 colunas que representam altura (em polegadas), peso (em libras) e idade (em anos). `baseball` está disponível como uma lista de listas comum, e `updated` está disponível como uma matriz 2D do numpy.

`@instructions`
- Você conseguiu obter as alterações de altura, peso e idade de todos os jogadores de beisebol. Estão disponíveis como uma matriz 2D do `numpy`, `updated`. Some `np_baseball` e `updated` e imprima o resultado.
- Você deseja converter as unidades de altura e peso para o sistema métrico (metros e quilogramas, respectivamente). Como primeira etapa, crie uma matriz do `numpy` com três valores: `0.0254`, `0.453592` e `1`. Chame essa matriz de `conversion`.
- Multiplique `np_baseball` por `conversion` e imprima o resultado.

`@hint`
- `np_baseball + updated` faz uma soma de elementos das duas matrizes do `numpy`.
- Crie uma matriz do `numpy` com `np.array()`; a entrada é uma lista comum do Python com três elementos.
- `np_baseball * conversion` resolve o problema, sem trabalho extra. Experimente! Lembre-se de envolvê-lo em uma chamada `print()`.

`@pre_exercise_code`
```{python}
import pandas as pd
import numpy as np
baseball = pd.read_csv("https://assets.datacamp.com/course/intro_to_python/baseball.csv")[['Height', 'Weight', 'Age']].to_numpy().tolist()
n = len(baseball)
updated = np.array(pd.read_csv("https://assets.datacamp.com/course/intro_to_python/update.csv", header = None))
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

msg = "Você não precisa mudar ou remover as variáveis predefinidas."
Ex().check_object("np_baseball", missing_msg=msg).has_equal_value(incorrect_msg=msg)

Ex().has_printout(0)

Ex().check_correct(
    has_printout(1),
    check_correct(
        check_object('conversion').has_equal_value(),
        check_function('numpy.array', index=1).check_args(0).has_equal_value()
    )    
)

success_msg("Ótimo trabalho! Note como com muito pouco código, você pode mudar todos os valores na sua estrutura de dados `numpy` de uma maneira muito específica. Isso será muito útil no seu futuro como cientista de dados!")
```

---

## NumPy: estatísticas básicas

```yaml
type: VideoExercise
key: 287995e488
xp: 50
```

`@projector_key`
34495ba457d74296794d2a122c9b6e19

---

## Média x mediana

```yaml
type: NormalExercise
key: 509c588eb6
lang: python
xp: 100
skills:
  - 2
```

Agora você sabe como usar as funções do `numpy` para ter uma noção melhor dos dados. 

Os dados de beisebol estão disponíveis como uma matriz 2D do `numpy` com 3 colunas (altura, peso e idade) e 1015 linhas. O nome dessa matriz do `numpy` é `np_baseball`. Após reestruturar os dados, no entanto, você percebe que alguns valores de altura estão acima do normal. Siga as instruções e descubra qual estatística de resumo é mais adequada se você estiver lidando com os chamados _valores discrepantes_. `np_baseball` está disponível.

`@instructions`
- Crie uma matriz do `numpy` chamada `np_height_in` que seja igual à primeira coluna de `np_baseball`.
- Imprima a média de `np_height_in`.
- Imprima a mediana de `np_height_in`.

`@hint`
- Use uma subdivisão 2D do `numpy`: `[:,0]` faz parte da solução.
- Se `numpy` for importado como `np`, você poderá usar `np.mean()` para calcular a média de uma matriz do NumPy. Não se esqueça de incluir uma chamada `print()`.
- Na última instrução, use `np.median()`.

`@pre_exercise_code`
```{python}
import pandas as pd
np_baseball = pd.read_csv("https://assets.datacamp.com/course/intro_to_python/baseball.csv")[['Height', 'Weight', 'Age']].to_numpy()
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

success_msg("Uma altura média de 1586 polegadas, isso não parece certo, né? No entanto, a mediana não parece ser afetada pelos outliers: 74 polegadas faz todo sentido. É sempre uma boa ideia verificar tanto a mediana quanto a média, para ter uma ideia sobre a distribuição geral de todo o conjunto de dados.")
```

---

## Analise os dados de beisebol

```yaml
type: NormalExercise
key: '4409948807'
lang: python
xp: 100
skills:
  - 2
```

Como a média e a mediana estão muito distantes, você decide reclamar com a MLB. Ela encontra o erro e envia os dados corrigidos para você. Mais uma vez, eles estão disponíveis como uma matriz 2D do NumPy chamada `np_baseball`, com três colunas.

O script Python no editor já inclui um código para imprimir mensagens informativas com as diferentes estatísticas de resumo, e `numpy` já foi carregado como `np`. Você consegue terminar o trabalho? `np_baseball` está disponível.

`@instructions`
- O código para imprimir a altura média já está incluído. Complete o código da altura mediana.
- Use `np.std()` com a primeira coluna de `np_baseball` para calcular `stddev`. 
- Os jogadores grandes tendem a ser mais pesados? Use `np.corrcoef()` para armazenar em `corr` a correlação entre a primeira e a segunda colunas de `np_baseball`.

`@hint`
- Use `np.median()` para calcular a mediana. Lembre-se de selecionar a coluna correta primeiro!
- Subdivida a mesma coluna ao calcular o desvio-padrão com `np.std()`.
- Use `np_baseball[:, 0]` e `np_baseball[:, 1]` para selecionar a primeira e a segunda colunas; essas são as entradas de `np.corrcoef()`.

`@pre_exercise_code`
```{python}
import pandas as pd
np_baseball = pd.read_csv("https://assets.datacamp.com/course/intro_to_python/baseball.csv")[['Height', 'Weight', 'Age']].to_numpy()
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
incorrect1 = "Para calcular `corr`, o primeiro argumento para `np.corrcoef()` deve ser a primeira coluna de `np_baseball`, assim como fez antes."
incorrect2 = "Para calcular `corr`, o segundo argumento para `np.corrcoef()` deve ser a segunda coluna de `np_baseball`. Em vez de `[:,0]`, use `[:,1]` desta vez."
Ex().check_correct(
  check_object("corr").has_equal_value(),
  check_function("numpy.corrcoef", index=0, missing_msg=missing).multi(
    check_args(0, missing_msg=incorrect1).has_equal_value(incorrect_msg=incorrect1),
    check_args(1, missing_msg=incorrect2).has_equal_value(incorrect_msg=incorrect2)
  )
)

success_msg("Ótimo trabalho! Você construiu uma base sólida - agora é hora de usar todas as suas novas habilidades em ciência de dados para resolver mais desafios e causar um impacto.")
```

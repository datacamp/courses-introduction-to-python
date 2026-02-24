---
title: Insert title here
key: ae3238dcc7feb9adecfee0c395fc8dc8
video_link:
  mp3: >-
    https://videos.datacamp.com/mp3/translations/course_735/pt-BR/804e770f-43b1-4fe7-994b-afbd781ff2ba.mp3
---

## Matrizes 2D do NumPy

```yaml
type: TitleSlide
key: 0cc8abf493
```

`@lower_third`
name: Hugo Bowne-Anderson
title: Data Scientist at DataCamp

`@script`
Muito bem, você é demais! Agora vamos recriar as matrizes NumPy do vídeo anterior.


---

## Tipos de matrizes do NumPy

```yaml
type: FullSlide
key: 1b9db47fd2
code_zoom: 100
```

`@part1`
```py
import numpy as np
np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
np_weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])
```

```py
type(np_height)
```

```out
numpy.ndarray
```

```py
type(np_weight)
```

```out
numpy.ndarray
```

`@script`
Se você perguntar qual é o tipo dessas matrizes, o Python vai dizer que são numpy ponto ndarray. O numpy ponto mostra que é um tipo que foi definido no pacote numpy. ndarray significa matriz n-dimensional. As matrizes np underline height e np underline weight são unidimensionais, mas dá para criar matrizes bidimensionais, tridimensionais e até mesmo de sete dimensões! Mas vamos ficar com duas neste vídeo.


---

## Matrizes 2D do NumPy

```yaml
type: FullSlide
key: ebb550dcba
code_zoom: 71
```

`@part1`
```py
np_2d = np.array([[1.73, 1.68, 1.71, 1.89, 1.79],
                  [65.4, 59.2, 63.6, 88.4, 68.7]])
```{{1}}
```py
np_2d
```{{2}}

```out
array([[ 1.73,  1.68,  1.71,  1.89,  1.79],
       [65.4 , 59.2 , 63.6 , 88.4 , 68.7 ]])
```{{2}}

```py
np_2d.shape
```{{3}}

```out
(2, 5) # 2 rows, 5 columns
```{{3}}

```py
np.array([[1.73, 1.68, 1.71, 1.89, 1.79],
          [65.4, 59.2, 63.6, 88.4, "68.7"]])
```{{4}}

```out
array([['1.73', '1.68', '1.71', '1.89', '1.79'],
       ['65.4', '59.2', '63.6', '88.4', '68.7']], dtype='<U32')
```{{4}}

`@script`
Você pode criar uma matriz 2D do NumPy a partir de uma lista de listas comum do Python. Vamos tentar criar uma matriz do NumPy com todos os dados de altura e peso da sua família, como esta.

Agora, se você imprimir np underline 2d, vai ver que é uma estrutura de dados retangular. Cada sublista da lista corresponde a uma linha da matriz bidimensional do NumPy. Com np underline 2d ponto shape, dá para ver que realmente temos duas linhas e cinco colunas. Dizemos que shape é um atributo da matriz np2d que apresenta mais informações sobre a estrutura dos dados.

Observe que a sintaxe para acessar um atributo é parecida com a chamada de um método, mas não é a mesma! Lembre-se de que os métodos têm parênteses depois e, como dá para ver aqui, os atributos não têm.

A regra do NumPy também vale para matrizes 2D: uma matriz pode armazenar somente um tipo. Se você mudar um float para string, todos os elementos da matriz serão convertidos em strings, para que a matriz fique homogênea.


---

## Divisão em subconjuntos

```yaml
type: FullSlide
key: e71d2fc8b8
code_zoom: 80
```

`@part1`
```out
           0       1       2       3       4
           
array([[  1.73,   1.68,   1.71,   1.89,   1.79],     0
       [  65.4,   59.2,   63.6,   88.4,   68.7]])    1
```

```py
np_2d[0]
```

```out
array([1.73, 1.68, 1.71, 1.89, 1.79])
```

`@script`
Pense na matriz 2D do NumPy como uma lista de listas melhorada: dá para fazer cálculos com as matrizes, como mostrei antes, e usar formas mais avançadas de divisão em subconjuntos.

Suponha que você queira a primeira linha e o terceiro elemento dessa linha. Para selecionar a linha, você precisa do índice zero entre colchetes. Não se esqueça de que a indexação começa no zero.

Para selecionar o terceiro elemento, você pode estender a mesma chamada com outro par de colchetes, desta vez com o índice dois,


---

## Divisão em subconjuntos

```yaml
type: FullSlide
key: 57a1fb1581
disable_transition: true
code_zoom: 80
```

`@part1`
```out
           0       1       2       3       4
           
array([[  1.73,   1.68,   1.71,   1.89,   1.79],     0
       [  65.4,   59.2,   63.6,   88.4,   68.7]])    1
```

```py
np_2d[0][2]
```

```out
1.71
```

```py
np_2d[0, 2]
```{{1}}

```out
1.71
```{{1}}

`@script`
assim. Basicamente, você seleciona a linha e, em seguida, faz outra seleção nessa linha.

Também tem outra forma de fazer a divisão em subconjuntos, usando colchetes simples e vírgula. Esta chamada retorna exatamente o mesmo valor de antes. O valor antes da vírgula é a linha, e o valor depois da vírgula é a coluna. É retornada a interseção das linhas e colunas que foram especificadas. Depois que você se acostumar, essa sintaxe vai parecer mais intuitiva e abrir mais possibilidades.


---

## Divisão em subconjuntos

```yaml
type: FullSlide
key: feb75c975c
disable_transition: true
code_zoom: 80
```

`@part1`
```out
           0       1       2       3       4
           
array([[  1.73,   1.68,   1.71,   1.89,   1.79],     0
       [  65.4,   59.2,   63.6,   88.4,   68.7]])    1
```

```py
np_2d[:, 1:3]
```{{1}}

```out
array([[ 1.68,  1.71],
       [59.2 , 63.6 ]])
```{{1}}

```py
np_2d[1, :]
```{{2}}

```out
array([65.4, 59.2, 63.6, 88.4, 68.7])
```{{2}}

`@script`
Suponha que você queira escolher a altura e o peso da segunda e terceira pessoas da família. Você quer as duas linhas, então coloca dois pontos antes da vírgula. Você quer só a segunda e a terceira colunas, então coloca os índices um a três depois da vírgula. Lembre-se de que o terceiro índice não é incluído aqui. A interseção nos dá uma matriz 2D com duas linhas e duas colunas.

Da mesma forma, você pode escolher o peso de todos os familiares assim: se você quiser só a segunda linha, coloque um antes da vírgula. Se quiser todas as colunas, use dois pontos depois da vírgula. A interseção nos dá a segunda linha inteira.

Por fim, as matrizes 2D do NumPy permitem fazer cálculos elemento a elemento, da mesma forma que fizemos com matrizes 1D do NumPy. Isso é algo


---

## Vamos praticar!

```yaml
type: FinalSlide
key: 6047b27c09
```

`@script`
que você pode testar nos exercícios, além de criar e subdividir matrizes 2D do NumPy! Empolgante.

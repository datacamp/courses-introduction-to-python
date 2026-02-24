---
title: Insert title here
key: 433dcfcfedaee070cbf440491c402e3b
video_link:
  mp3: >-
    https://videos.datacamp.com/mp3/translations/course_735/pt-BR/b1fc94b5-1952-4b79-89f1-b64e3d1e4b46.mp3
---

## Variáveis e tipos

```yaml
type: TitleSlide
key: dc8b62f1c8
```

`@lower_third`
name: Hugo Bowne-Anderson
title: Data Scientist at DataCamp

`@script`
Bom trabalho, e que bom ter você de volta! Está claro que o Python é uma ótima calculadora. Mas, se você quiser fazer cálculos mais complexos, é melhor “salvar” os valores enquanto estiver programando.


---

## Variável

```yaml
type: FullSlide
key: 36ec318b41
```

`@part1`
- Nome específico, com distinção entre maiúsculas e minúsculas

- Chamar um valor usando o nome da variável{{1}}

- 1,79 m – 68,7 kg{{2}}

```py
height = 1.79
weight = 68.7
```{{3}}
```py
height
```{{4}}

```out
1.79
```{{4}}

`@script`
Você pode fazer isso definindo uma variável com um nome específico, que diferencia maiúsculas de minúsculas. Depois de criar ou declarar essa variável, você pode chamar o valor dela digitando o nome da variável.

Imagine que você mediu sua altura e peso: você tem um metro e setenta e nove e pesa sessenta e oito vírgula sete quilos. Você pode atribuir esses valores a duas variáveis, chamadas “height” e “weight”, usando o sinal de igual.

Agora, se você digitar o nome da variável, “height”,

o Python procura o nome da variável, recupera o valor dela e o imprime na tela.


---

## Cálculo do IMC

```yaml
type: TwoColumns
key: fe1b10a93b
code_zoom: 80
```

`@part1`
```py
height = 1.79
weight = 68.7
```
```py
height
```

```out
1.79
```

$$ \text{IMC} = \frac{\text{peso}}{\text{altura}^2} $${{1}}

`@part2`
```py
68.7 / 1.79 ** 2
```{{2}}

```out
21.4413
```{{2}}

```py
weight / height ** 2
```{{3}}

```out
21.4413
```{{3}}

```py
bmi = weight / height ** 2
bmi
```{{4}}

```out
21.4413
```{{4}}

`@script`
Agora vamos calcular o Índice de Massa Corporal, ou IMC, da seguinte forma, usando o peso em quilos e a altura em metros. Você pode fazer isso com os valores reais, mas também pode usar as variáveis “height” e “weight”, como feito aqui. Toda vez que você digita o nome da variável, está pedindo ao Python que o substitua pelo valor real da variável. “weight” corresponde a sessenta e oito ponto sete, e “height” a um ponto setenta e nove.

Por fim, esta versão faz o Python armazenar o resultado em uma nova variável, bmi, que significa IMC em inglês. Agora, bmi tem o mesmo valor que você calculou antes.

Em Python, são usadas variáveis o tempo todo. Elas ajudam a tornar o código reproduzível.


---

## Reprodutibilidade

```yaml
type: FullSlide
key: 9980f47f9d
```

`@part1`
```py
height = 1.79
weight = 68.7
bmi = weight / height ** 2
print(bmi)
```

```out
21.4413
```

`@script`
Suponha que o código para criar as variáveis height, weight e bmi esteja em um script, como este. Se você quiser recalcular o IMC de outro peso,


---

## Reprodutibilidade

```yaml
type: FullSlide
key: a4e899f00f
disable_transition: true
```

`@part1`
```py
height = 1.79
weight = 74.2 # <-
bmi = weight / height ** 2
print(bmi)
```

```out
23.1578
```

`@script`
basta mudar a declaração da variável weight e rodar o script de novo. bmi reflete essa alteração, porque o valor da variável weight também mudou.

Até agora, trabalhamos somente com valores numéricos, como altura e peso.


---

## Tipos de objeto Python

```yaml
type: FullSlide
key: 9d86084ad4
```

`@part1`
```py
type(bmi)
```{{1}}

```out
float
```{{1}}

```py
day_of_week = 5
type(day_of_week)
```{{2}}

```out
int
```{{2}}

`@script`
Em Python, todos esses números têm um tipo específico. Você pode ver o tipo de um valor com a função type. Para ver o tipo do valor de bmi, basta escrever type e, em seguida, bmi entre parênteses. Observe que é um float, que é como o Python representa um número real, ou seja, um número que pode ter uma parte inteira e uma parte fracionária. O Python também tem um tipo para inteiros, int, como neste exemplo.

Mas, para fazer ciência de dados, você vai precisar de mais do que inteiros e floats.


---

## Tipos de objeto Python (2)

```yaml
type: FullSlide
key: d971d34e6a
```

`@part1`
```py
x = "body mass index"
y = 'this works too'
```{{1}}
```py
type(y)
```{{2}}

```out
str
```{{2}}

```py
z = True
type(z)
```{{3}}

```out
bool
```{{3}}

`@script`
O Python tem vários outros tipos de dados. Os mais comuns são strings e booleanos.

Uma string é a maneira que o Python usa para representar textos. Você pode usar tanto aspas simples quanto aspas duplas para criar uma string, como dá para ver nestes exemplos. Ao imprimir o tipo da última variável, vemos que é str, abreviação de string.

Um booleano é um tipo que pode ser verdadeiro ou falso. É como “sim” e “não” na linguagem do dia a dia. Os booleanos vão ser bem úteis mais adiante, para fazer operações de filtragem nos dados, por exemplo.

Tem algo especial nos tipos de dados do Python.


---

## Tipos de objeto Python (3)

```yaml
type: FullSlide
key: 24601e2af0
```

`@part1`
```py
2 + 3
```{{1}}

```out
5
```{{1}}

```py
'ab' + 'cd'
```{{2}}

```out
'abcd'
```{{2}}

- Tipo diferente = comportamento diferente!{{3}}

`@script`
Dê uma olhada nesta linha de código, que soma dois números inteiros, e depois nesta linha de código, que soma duas strings.

No caso dos inteiros, os valores foram somados, enquanto as strings foram concatenadas. O operador “mais” se comportou de forma diferente conforme o tipo de dados. Esse é um princípio geral: o funcionamento do código depende dos tipos com os quais estamos trabalhando.

Nos exercícios a seguir, você vai criar as primeiras variáveis e testar alguns tipos de dados do Python. A gente se vê no próximo vídeo para explicar tudo sobre listas.


---

## Vamos praticar!

```yaml
type: FinalSlide
key: b7fc40db4d
```

`@script`
Vamos começar a programar! Mal posso esperar para ver você no próximo capítulo, em que você vai criar gráficos ainda mais incríveis em Python.

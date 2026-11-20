---
title_meta: Capítulo 1
title: Noções básicas de Python
description: >-
  Introdução aos conceitos básicos do Python. Aprenda a usar o Python de forma
  interativa e por meio de um script. Crie suas primeiras variáveis e
  familiarize-se com os tipos de dados básicos do Python.
attachments:
  slides_link: 'https://projector-video-pdf-converter.datacamp.com/735/chapter1.pdf'
free_preview: true
lessons:
  - nb_of_exercises: 3
    title: 'Olá, Python!'
  - nb_of_exercises: 5
    title: Variáveis e tipos
---

## Olá, Python!

```yaml
type: VideoExercise
key: f644a48d5d
xp: 50
```

`@projector_key`
d8fcd4c930027fa4e1c3870c7e7e0ff1

---

## Seu primeiro código Python

```yaml
type: NormalExercise
key: bdc52f0e19
lang: python
xp: 100
skills:
  - 2
```

É hora de rodar seu primeiro código Python!

Vá até o código e clique no botão “Executar código” para ver o resultado.

`@instructions`
- Clique no botão “Executar código” para ver o resultado de `print(5 / 8)`.

`@hint`
- Execute o código antes de enviar sua resposta, para você ter tempo de ver o resultado.

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
Ex().has_printout(0, not_printed_msg = "__JINJA__:Você usou `{{sol_call}}` para imprimir `5 / 8`?")
success_msg("Ótimo! Vamos para a próxima!")
```

---

## O Python como calculadora

```yaml
type: NormalExercise
key: 0f7c039428
lang: python
xp: 100
skills:
  - 2
```

O Python é perfeito para fazer cálculos básicos. Ele pode fazer adição, subtração, multiplicação e divisão.

O código no script fornece alguns exemplos.

Agora é a sua vez de treinar escrevendo um pouco de código.

`@instructions`
- Imprima o resultado de `5` menos `5` embaixo de `# Subtraction` usando `print()`.
- Imprima o resultado de `3` multiplicado por `5` embaixo de `# Multiplication`.

`@hint`
- Você precisa usar `print()` para gerar uma saída.
- Você pode subtrair com `-` e multiplicar com `*`.

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
Ex().has_printout(0, not_printed_msg = "Você usou `print(4 + 5)` para imprimir o resultado da sua soma?")

Ex().has_printout(1, not_printed_msg = "Você usou `print(5 - 5)` para imprimir o resultado da sua subtração?")

Ex().has_printout(2, not_printed_msg = "Você usou `print(3 * 5)` para imprimir o resultado da sua multiplicação?")

Ex().has_printout(3, not_printed_msg = "Você usou `print(10 / 2)` para imprimir o resultado da sua divisão?")

success_msg("Está correto! Python pode te ajudar a fazer cálculos, uma característica que será útil para análise à medida que desenvolvemos nossas habilidades com dados.")
```

---

## Variáveis e tipos

```yaml
type: VideoExercise
key: c2e396792e
xp: 50
```

`@projector_key`
433dcfcfedaee070cbf440491c402e3b

---

## Atribuição de variáveis

```yaml
type: NormalExercise
key: 4bf65ad83e
lang: python
xp: 100
skills:
  - 2
```

Em Python, uma variável permite que você faça referência a um valor com um nome. Para criar uma variável `x` com valor `5`, usamos `=`, como neste exemplo:

```
x = 5
```

Agora você pode usar o nome dessa variável, `x`, em vez do valor real, `5`.

Lembre-se de que `=` em Python significa _atribuição_, ele não testa a igualdade! Faça o teste no exercício substituindo `____` pelo seu código.

`@instructions`
- Crie uma variável chamada `savings` com valor `100`.
- Verifique essa variável digitando `print(savings)` no script.

`@hint`
- Digite `savings = 100` para criar a variável `savings`.
- Depois de criar a variável `savings`, você pode digitar `print(savings)`.
- O código final não deve incluir nenhum `____`.

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
Ex().check_object("savings").has_equal_value(incorrect_msg="Atribua `100` à variável `savings`.")
Ex().has_printout(0, not_printed_msg = "Imprima `savings`, a variável que você criou, com `print(savings)`.")
success_msg("Ótimo! Vamos tentar fazer alguns cálculos com essa variável agora!")
```

---

## Cálculos com variáveis

```yaml
type: NormalExercise
key: ff06cedeb4
lang: python
xp: 100
skills:
  - 2
```

Agora que você criou uma variável chamada “savings”, vamos começar a economizar!

Em vez de calcular com os valores reais, você pode usar variáveis.

Quanto dinheiro você teria economizado daqui a quatro meses se economizasse $10 por mês?

`@instructions`
- Crie uma variável `monthly_savings` igual a `10` e outra variável `num_months` igual a `4`.
- Multiplique `monthly_savings` por `num_months` e atribua o resultado a `new_savings`.
- Imprima o valor de `new_savings`.

`@hint`
- Você pode fazer cálculos com variáveis da mesma forma do que com números. Portanto, em vez de `10 * 4`, substitua os números pelas variáveis!
- Use `print()` para ver o valor de `new_savings`.
- Lembre-se de escrever as variáveis corretamente!

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
Ex().check_object("monthly_savings").has_equal_value(incorrect_msg = "Você salvou `10` em `monthly_savings` usando `monthly_savings = 10`?")
Ex().check_object("num_months").has_equal_value(incorrect_msg = "Você salvou `4` em `num_months` usando `num_months = 4`?")
Ex().check_object("new_savings").has_equal_value(incorrect_msg = "Você usou as variáveis e símbolos corretos para multiplicar? Esperado `monthly_savings * num_months`, mas obteve algo diferente.")
# Ex().check_object("total_savings").has_equal_value(incorrect_msg = "Você usou as variáveis e símbolos corretos para somar? Esperado `savings + new_savings`, mas obteve algo diferente.")

Ex().has_printout(0, not_printed_msg="Lembre-se de imprimir `new_savings` no final do seu script.")

success_msg("Você tem $40 em novas economias!")
```

---

## Outros tipos de variáveis

```yaml
type: NormalExercise
key: 006b48561f
lang: python
xp: 100
skills:
  - 2
```

No exercício anterior, você trabalhou com o tipo de dados número inteiro do Python:

- `int` ou inteiro: um número sem uma parte fracionária. `savings`, com valor `100`, é um exemplo de número inteiro.

Além dos tipos de dados numéricos, há três outros tipos de dados muito comuns:

- `float` ou ponto flutuante: número que tem uma parte inteira e uma parte fracionária, separadas por um ponto. `1.1` é um exemplo de float.
- `str` ou string: tipo usado para representar texto. Você pode usar aspas simples ou duplas para criar uma string.
- `bool` ou booleano: tipo usado para representar valores lógicos. Pode ser apenas `True` ou `False` (a distinção entre maiúsculas e minúsculas é importante!).

`@instructions`
- Crie um novo float, `half`, com o valor `0.5`.
- Crie uma nova string, `intro`, com o valor `"Hello! How are you?"`.
- Crie um novo booleano, `is_good`, com o valor `True`.

`@hint`
- Para criar uma variável em Python, use `=`. Lembre-se de colocar a string entre aspas simples ou duplas.
- Existem apenas dois valores booleanos em Python: `True` e `False`. `TRUE`, `true`, `FALSE`, `false` e outras versões não são aceitas.

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
Ex().check_object("half").has_equal_value(incorrect_msg = "Você salvou o float, `0.5` em `half`?")

Ex().check_object("intro").has_equal_value(incorrect_msg = "Hmm, algo está incorreto na sua variável `intro`. Verifique a ortografia e certifique-se de que você usou aspas.")

Ex().check_object("is_good").has_equal_value(incorrect_msg = "Você capitalizou o valor booleano? Lembre-se de que não precisa usar aspas aqui.")

success_msg("Legal!")
```

---

## Operações com outros tipos

```yaml
type: BulletExercise
key: 4d0d83cc02
xp: 100
```

Existem variáveis de diferentes tipos no Python. Você pode ver o tipo de uma variável usando `type()`. Por exemplo: para ver o tipo de `a`, execute `type(a)`.

Diferentes tipos se comportam de maneira diferente em Python. Ao somar duas strings, por exemplo, temos um comportamento diferente de quando somamos dois inteiros ou dois booleanos.

É sua vez de testar isso.

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
- Some `savings` a `new_savings` e atribua o resultado a `total_savings`.
- Use `type()` para imprimir o tipo resultante de `total_savings`.

`@hint`
- Atribua `savings + new_savings` a uma nova variável, `total_savings`.
- Para imprimir o tipo de uma variável `x`, use `print(type(x))`.

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
msg = "Você não precisa mudar ou remover as variáveis predefinidas."

Ex().multi(
    check_object('savings', missing_msg=msg).has_equal_value(incorrect_msg=msg),
    check_object('new_savings', missing_msg=msg).has_equal_value(incorrect_msg=msg)
)

Ex().multi(
    check_object("total_savings").has_equal_value(incorrect_msg="Adicione `savings` e `new_savings` para criar a variável `total_savings`."),
    has_printout(1, not_printed_msg = "__JINJA__:Use `{{sol_call}}` para imprimir o tipo de `total_savings`.")
)
```

***

```yaml
type: NormalExercise
key: f54fbf9bd9
xp: 50
```

`@instructions`
- Calcule a soma de `intro` e `intro` e atribua o resultado a `doubleintro`.
- Imprima `doubleintro`. Você esperava por isso?

`@hint`
- Atribua `intro + intro` a uma nova variável, `doubleintro`.
- Para imprimir uma variável `x`, escreva `print(x)` no script.

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
msg = "Você não precisa mudar ou remover as variáveis predefinidas."

Ex().check_object('intro', missing_msg=msg).has_equal_value(incorrect_msg=msg)

Ex().multi(
    check_object("doubleintro").has_equal_value(incorrect_msg  = "Você armazenou o resultado de `intro + intro` em `doubleintro`?"),
    has_printout(0, not_printed_msg = "Não se esqueça de imprimir `doubleintro`.")
)

success_msg("Legal. Note como `intro + intro` faz com que `\"Hello! How are you?\"` e `\"Hello! How are you?\"` sejam colados juntos.")
```

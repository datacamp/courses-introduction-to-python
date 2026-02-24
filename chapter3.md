---
title_meta: Capítulo 3
title: Funções e pacotes
description: >-
  Você aprenderá a usar funções, métodos e pacotes para aproveitar com
  eficiência o código que os brilhantes desenvolvedores do Python escreveram. O
  objetivo é reduzir a quantidade de código necessária para resolver problemas
  desafiadores!
attachments:
  slides_link: 'https://projector-video-pdf-converter.datacamp.com/735/chapter3.pdf'
lessons:
  - nb_of_exercises: 4
    title: Funções
  - nb_of_exercises: 4
    title: Métodos
  - nb_of_exercises: 4
    title: Pacotes
---

## Funções

```yaml
type: VideoExercise
key: 5c5f365930
xp: 50
```

`@projector_key`
1204d914b0e53100529827e07441ee6c

---

## Funções familiares

```yaml
type: NormalExercise
key: c422ee929b
lang: python
xp: 100
skills:
  - 2
```

O Python oferece uma série de funções integradas para facilitar a vida de um cientista de dados. Você já conhece duas dessas funções: `print()` e `type()`. Também existem funções como `str()`, `int()`, `bool()` e `float()` para trocar o tipo de dados. Saiba mais sobre elas [aqui.](https://docs.python.org/3/library/functions.html) Essas também são funções integradas.

Chamar uma função é fácil. Para obter o tipo de `3.0` e armazenar a saída como uma nova variável, `result`, você pode usar o seguinte:

```
result = type(3.0)
```

`@instructions`
- Use `print()` em combinação com `type()` para imprimir o tipo de `var1`.
- Use `len()` para obter o [tamanho da lista](https://docs.python.org/3/library/functions.html#len) `var1`. Envolva-o em uma chamada `print()` para imprimi-lo diretamente.
- Use `int()` para converter `var2` em um [inteiro](https://docs.python.org/3/library/functions.html#int). Armazene a saída como `out2`.

`@hint`
- Chame a função `type()` da seguinte forma: `type(var1)`.
- Chame `print()` como você já fez diversas vezes. Basta colocar a variável que deseja imprimir entre parênteses.
- `int(x)` converte `x` em um número inteiro.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create variables var1 and var2
var1 = [1, 2, 3, 4]
var2 = True

# Print out type of var1
____

# Print out length of var1
____

# Convert var2 to an integer: out2
out2 = ____
```

`@solution`
```{python}
# Create variables var1 and var2
var1 = [1, 2, 3, 4]
var2 = True

# Print out type of var1
print(type(var1))

# Print out length of var1
print(len(var1))

# Convert var2 to an integer: out2
out2 = int(var2)
```

`@sct`
```{python}
msg = "Você não precisa mudar ou remover as variáveis predefinidas."
Ex().check_object("var1", missing_msg=msg).has_equal_value(incorrect_msg=msg)
Ex().check_object("var2", missing_msg=msg).has_equal_value(incorrect_msg=msg)

patt = "__JINJA__:Certifique-se de imprimir o %s de `var1` com `{{sol_call}}`."
Ex().has_printout(0, not_printed_msg = patt % 'tipo')
Ex().has_printout(1, not_printed_msg = patt % 'comprimento')

int_miss_msg = "Você usou `int()` para transformar `var2` em um inteiro?"
int_incorr_msg = "Você passou `var2` para `int()`?"
Ex().check_correct(
  check_object("out2").has_equal_value(incorrect_msg="Você chamou `int()` corretamente; agora certifique-se de atribuir o resultado dessa chamada a `out2`."),
  check_function("int", missing_msg=int_miss_msg).has_equal_value(incorrect_msg=int_incorr_msg)
)
success_msg("Ótimo trabalho! A função `len()` é extremamente útil; ela também funciona em strings para contar o número de caracteres!")
```

---

## Ajuda!

```yaml
type: MultipleChoiceExercise
key: 679b852978
lang: python
xp: 50
skills:
  - 2
```

Talvez você já saiba o nome de uma função Python, mas ainda precise descobrir como usá-la. Por ironia, você precisa pedir informações sobre uma função usando outra função: `help()`. Especificamente no IPython, você também pode usar `?` antes do nome da função.

Para receber ajuda sobre a função `max()`, por exemplo, você pode usar uma destas chamadas:

```
help(max)
?max
```

Use o Shell IPython para abrir a [documentação](https://docs.python.org/3/library/functions.html#pow) sobre `pow()`. Para fazer isso, digite `?pow` ou `help(pow)` e aperte **Enter**.

Qual das seguintes afirmações é verdadeira?

`@possible_answers`
- `pow()` recebe três argumentos: `base`, `exp` e `mod`. Se você não especificar `mod`, a função vai retornar um erro.
- `pow()` deve receber três argumentos: `base`, `exp` e `None`.
- `pow()` precisa dos argumentos `base` e `exp`; `mod` é opcional.
- `pow()` recebe dois argumentos: `exp` e `mod`. Quando `exp` está faltando, o resultado é um erro.

`@hint`
- Os argumentos opcionais são definidos `=` com um valor padrão, que a função usará se o argumento não for especificado.

`@pre_exercise_code`
```{python}

```

`@sct`
```{python}
msg1 = "Não exatamente. `mod` tem um valor padrão que será usado se você não especificar um valor."
msg2 = "Incorreto. `None` é o valor padrão para o argumento `mod`."
msg3 = "Perfeito! Usar `help()` pode te ajudar a entender como as funções funcionam, liberando todo o seu potencial!"
msg4 = "Incorreto. `pow()` aceita três argumentos, um dos quais tem um valor padrão."
Ex().has_chosen(3, [msg1, msg2, msg3, msg4])
```

---

## Vários argumentos

```yaml
type: NormalExercise
key: e30486d7c1
lang: python
xp: 100
skills:
  - 2
```

No exercício anterior, você identificou argumentos opcionais ao visualizar a documentação com `help()`. Agora você aplicará isso para alterar o comportamento da função `sorted()`.

Dê uma olhada na [documentação](https://docs.python.org/3/library/functions.html#sorted) de `sorted()` digitando `help(sorted)` no Shell IPython.

Você verá que `sorted()` recebe três argumentos: `iterable`, `key` e `reverse`. Neste exercício, você só precisa especificar `iterable` e `reverse`, e não `key`.

Duas listas foram criadas para você.

Você pode combiná-las e classificá-las em ordem decrescente?

`@instructions`
- Use `+` para combinar o conteúdo de `first` e `second` em uma nova lista: `full`.
- Chame `sorted()` com `full` e especifique o argumento `reverse` como sendo `True`. Salve a lista ordenada como `full_sorted`.
- Para finalizar, imprima `full_sorted`.

`@hint`
- Some `first` e `second` como se fossem dois números e atribua o resultado a `full`.
- Use `sorted()` com duas entradas: `full` e `reverse=True`.
- Para imprimir uma variável, use `print()`.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create lists first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# Paste together first and second: full
full = ____ + ____

# Sort full in descending order: full_sorted
full_sorted = ____

# Print out full_sorted
____
```

`@solution`
```{python}
# Create lists first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# Paste together first and second: full
full = first + second

# Sort full in descending order: full_sorted
full_sorted = sorted(full, reverse=True)

# Print out full_sorted
print(full_sorted)
```

`@sct`
```{python}
msg = "Você não precisa mudar ou remover as variáveis `first` e `second` já existentes."
Ex().multi(
  check_object("first", missing_msg=msg).has_equal_value(incorrect_msg=msg),
  check_object("second", missing_msg=msg).has_equal_value(incorrect_msg=msg)
)
Ex().check_correct(
  check_object("full_sorted").has_equal_value(incorrect_msg="Certifique-se de atribuir o resultado da chamada de `sorted()` a `full_sorted`."),
  check_function("sorted").multi(
    check_args(0).has_equal_value(),
    check_args('reverse').has_equal_value()
  )
)

success_msg("Legal! Vá para o vídeo sobre métodos em Python.")
```

---

## Métodos

```yaml
type: VideoExercise
key: 2b66cb66b1
xp: 50
```

`@projector_key`
8e387776f3a264a745128b68aa8d8f83

---

## Métodos de strings

```yaml
type: NormalExercise
key: 4039302ee0
lang: python
xp: 100
skills:
  - 2
```

As strings vêm com vários métodos. Siga atentamente as instruções para descobrir alguns. Se quiser descobri-los com mais detalhes, você sempre tem a opção de digitar `help(str)` no Shell IPython.

Uma string `place` já foi criada para você experimentar.

`@instructions`
- Use o [método](https://docs.python.org/3/library/stdtypes.html#str.upper) `.upper()` com `place` e armazene o resultado em `place_up`. Use a sintaxe para chamar métodos que você aprendeu no vídeo anterior.
- Imprima `place` e `place_up`. Ambas mudaram?
- Imprima o número de letras “o” na variável `place` chamando `.count()` com `place` e passando a letra `'o'` como entrada no método. Estamos falando da variável `place`, não da palavra `"place"`!

`@hint`
- Você pode chamar o método `.upper()` com `place` sem mais nenhuma entrada.
- Para imprimir uma variável `x`, você pode escrever `print(x)`.
- Lembre-se de envolver sua chamada `place.count(____)` em uma função `print()` para imprimi-la.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# string to experiment with: place
place = "poolhouse"

# Use upper() on place
place_up = 

# Print out place and place_up



# Print out the number of o's in place

```

`@solution`
```{python}
# string to experiment with: place
place = "poolhouse"

# Use upper() on place
place_up = place.upper()

# Print out place and place_up
print(place)
print(place_up)

# Print out the number of o's in place
print(place.count('o'))
```

`@sct`
```{python}
msg = "Você não precisa mudar ou remover as variáveis predefinidas."
Ex().check_object("place", missing_msg=msg).has_equal_value(incorrect_msg=msg)

patt = "Não se esqueça de imprimir `%s`."
Ex().has_printout(0, not_printed_msg=patt % "place")
Ex().check_correct(
    has_printout(1, not_printed_msg=patt % "place_up"),
    check_correct(
        check_object("place_up").has_equal_value(incorrect_msg="Atribua o resultado da sua chamada `place.upper()` a `place_up`."),
        check_function("place.upper", signature=False)
    )
)    

# check count of place
Ex().check_correct(
  has_printout(2, not_printed_msg = "Você calculou o número de o's em `place` corretamente; agora certifique-se de envolver a chamada `place.count('o')` em uma função `print()` para imprimir o resultado."),
  check_function("place.count", signature=False).check_args(0).has_equal_value()
)

success_msg("Legal! Note pelos prints que o método `upper()` não altera o objeto no qual é chamado. Isso será diferente para listas no próximo exercício!")
```

---

## Métodos de listas

```yaml
type: NormalExercise
key: 0dbe8ed695
lang: python
xp: 100
skills:
  - 2
```

As strings não são os únicos tipos Python que têm métodos associados a elas. Listas, floats, inteiros e booleanos também são tipos que vêm com vários métodos úteis. Neste exercício, você fará experiências com:

- `.index()` para obter o índice do primeiro elemento de uma lista que corresponda à sua entrada e
- `.count()` para obter o número de vezes que um elemento aparece em uma lista.

Você trabalhará na lista com a área de diferentes partes de uma casa: `areas`.

`@instructions`
- Use o método `.index()` para obter o índice do elemento de `areas` que é igual a `20.0`. Imprima esse índice.
- Chame `.count()` com `areas` para descobrir quantas vezes `9.50` aparece na lista. Novamente, basta imprimir esse número.

`@hint`
- Para imprimir o índice, envolva a chamada `areas.index(___)` em uma função `print()`.
- Para imprimir o número de vezes que um elemento `x` ocorre na lista, envolva a chamada `areas.count(___)` em uma função `print()`.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Print out the index of the element 20.0


# Print out how often 9.50 appears in areas

```

`@solution`
```{python}
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Print out the index of the element 20.0
print(areas.index(20.0))

# Print out how often 9.50 appears in areas
print(areas.count(9.50))
```

`@sct`
```{python}
predef_msg = "Você não precisa mudar ou remover a lista predefinida `areas`."

Ex().check_object("areas", missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg)

Ex().check_function("print", index=0).check_args(0).check_function('areas.index', signature=False).check_args(0).has_equal_value()


Ex().check_function("print", index=1).check_args(0).check_function('areas.count', signature=False).has_equal_value()

success_msg("Legal! Estes foram exemplos de métodos de `list` que não mudaram a lista na qual foram chamados.")
```

---

## Métodos de listas (2)

```yaml
type: NormalExercise
key: 1fbeab82d0
lang: python
xp: 100
skills:
  - 2
```

A maioria dos métodos de listas altera a lista em que são chamados. Alguns exemplos são:

- `.append()`, que adiciona um elemento à lista em que é chamado;
- `.remove()`, que [remove](https://docs.python.org/3/library/stdtypes.html#typesseq-mutable) o primeiro elemento de uma lista que corresponde à entrada; e
- `.reverse()`, que [inverte](https://docs.python.org/3/library/stdtypes.html#typesseq-mutable) a ordem dos elementos da lista em que é chamado.

Você trabalhará na lista com a área de diferentes partes da casa: `areas`.

`@instructions`
- Use `.append()` duas vezes para acrescentar o tamanho de <i>poolhouse</i> (anexo à piscina) e <i>garage </i>(garagem): `24.5` e `15.45`, respectivamente. Lembre-se de adicioná-los nesta ordem.
- Imprima `areas`.
- Use o método `.reverse()` para inverter a ordem dos elementos de `areas`.
- Imprima `areas` mais uma vez.

`@hint`
- Na primeira instrução, use a chamada `areas.append(___)` duas vezes.
- Para imprimir uma variável `x`, basta escrever `print(x)`.
- O método `.reverse()` não requer outras entradas; basta usar a notação de ponto e parênteses vazios: `.reverse()`.
- Para imprimir uma variável `x`, basta escrever `print(x)`.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Use append twice to add poolhouse and garage size



# Print out areas


# Reverse the orders of the elements in areas


# Print out areas

```

`@solution`
```{python}
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Use append twice to add poolhouse and garage size
areas.append(24.5)
areas.append(15.45)

# Print out areas
print(areas)

# Reverse the orders of the elements in areas
areas.reverse()

# Print out areas
print(areas)
```

`@sct`
```{python}
Ex().multi(
  check_function("areas.append", index=0, signature=False).check_args(0).has_equal_value(),
  check_function("areas.append", index=1, signature=False).check_args(0).has_equal_value(),
  check_function("print", index=0).check_args(0).has_equal_ast(),
  check_function("areas.reverse", index=0, signature=False),
  check_function("print", index=1).check_args(0).has_equal_ast()
)

success_msg("Mandou bem!")
```

---

## Pacotes

```yaml
type: VideoExercise
key: ab96a17c5e
xp: 50
```

`@projector_key`
cedcfb34350be8545599768f96695cdd

---

## Importação de pacote

```yaml
type: NormalExercise
key: 7432a6376f
lang: python
xp: 100
skills:
  - 2
```

Suponha que você queira calcular a circunferência e a área de um círculo. Veja como são essas fórmulas:

$$C = 2 \pi r$$
$$A = \pi r^2 $$

Em vez de digitar o número referente a `pi`, você pode usar o pacote `math`, que contém o número.

Apenas para constar, `**` é o símbolo da exponenciação. Por exemplo: `3**4` significa `3` elevado à `4`.ª potência, que é igual a `81`.

`@instructions`
- Importe o pacote `math`.
- Use `math.pi` para calcular a circunferência do círculo e armazene-a em `C`.
- Use `math.pi` para calcular a área do círculo e armazene-a em `A`.

`@hint`
- Você pode simplesmente usar `import math` e, em seguida, fazer referência a `pi` com `math.pi`.
- Use a equação no texto do exercício para encontrar `C`. Use `*`
- Use a equação no texto do exercício para encontrar `A`. Use `*` e `**`.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Import the math package
import ____

# Calculate C
C = 2 * 0.43 * ____

# Calculate A
A = ____ * 0.43 ** 2

print("Circumference: " + str(C))
print("Area: " + str(A))
```

`@solution`
```{python}
# Import the math package
import math

# Calculate C
C = 2 * 0.43 * math.pi

# Calculate A
A = math.pi * 0.43 ** 2

print("Circumference: " + str(C))
print("Area: " + str(A))
```

`@sct`
```{python}
patt = "Seu cálculo de `%s` não está totalmente correto. Certifique-se de usar `math.pi`."
Ex().multi(
  has_import('math', same_as=False),
  check_object('C').has_equal_value(incorrect_msg=patt%'C'),
  check_object('A').has_equal_value(incorrect_msg=patt%'A')
)

Ex().multi(
  has_printout(0, not_printed_msg = "__JINJA__:Mantenha `{{sol_call}}` aí para imprimir a circunferência."),
  has_printout(1, not_printed_msg = "__JINJA__:Mantenha `{{sol_call}}` aí para imprimir a área.")
)

success_msg("Legal! Se você sabe como lidar com funções de pacotes, o poder de muitos programadores Python está ao seu alcance!")
```

---

## Importação seletiva

```yaml
type: NormalExercise
key: fe65eff50a
lang: python
xp: 100
skills:
  - 2
```

As importações gerais, como `import math`, disponibilizam **todas** as funções do pacote `math`. No entanto, caso decida usar apenas uma parte específica de um pacote, sempre tem a opção tornar a importação mais seletiva:

```
from math import pi
```

Tente de novo, mas desta vez use somente `pi`.

`@instructions`
- Realize uma importação seletiva do pacote `math` importando apenas a função `pi`.
- Use `pi` para calcular a circunferência do círculo e armazene-a em `C`.
- Use `pi` para calcular a área do círculo e armazene-a em `A`.

`@hint`
- Use `from math import pi` para fazer a importação seletiva.
- Agora você pode usar o `pi` sozinho!

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Import pi function of math package
from math import ____

# Calculate C
C = 2 * 0.43 * ____

# Calculate A
A = ____ * 0.43 ** 2

print("Circumference: " + str(C))
print("Area: " + str(A))
```

`@solution`
```{python}
# Import pi function of math package
from math import pi

# Calculate C
C = 2 * 0.43 * pi

# Calculate A
A = pi * 0.43 ** 2

print("Circumference: " + str(C))
print("Area: " + str(A))
```

`@sct`
```{python}
patt = "Seu cálculo de `%s` não está totalmente correto. Certifique-se de usar apenas `pi`."

Ex().has_import("math.pi", not_imported_msg = "Certifique-se de importar `pi` do pacote `math`. Você deve usar a notação `from ___ import ___`.",)

Ex().multi(
  check_object('C').has_equal_value(incorrect_msg=patt%'C'),
  check_object('A').has_equal_value(incorrect_msg=patt%'A')
)

Ex().multi(
  has_printout(0, not_printed_msg = "__JINJA__:Mantenha `{{sol_call}}` aí para imprimir a circunferência."),
  has_printout(1, not_printed_msg = "__JINJA__:Mantenha `{{sol_call}}` aí para imprimir a área.")
)

success_msg("Legal! Vá para o próximo exercício.")
```

---

## Diferentes formas de importação

```yaml
type: MultipleChoiceExercise
key: f1b2675a2a
lang: python
xp: 50
skills:
  - 2
```

Há várias maneiras de importar pacotes e módulos no Python. Dependendo da chamada de importação, deve ser usado um código Python diferente.

Suponha que você queira usar a [função](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.inv.html) `inv()`, que faz parte do subpacote `linalg` do pacote `scipy`. Você deseja poder usar essa função da seguinte forma:

```
my_inv([[1,2], [3,4]])
```

Qual instrução `import` é necessária para executar o código acima sem erros?

`@possible_answers`
- `import scipy`
- `import scipy.linalg`
- `from scipy.linalg import my_inv`
- `from scipy.linalg import inv as my_inv`

`@hint`
- Experimente as diferentes instruções de importação no Shell IPython e veja qual delas faz com que a linha `my_inv([[1, 2], [3, 4]])` seja executada sem erros. Clique em **Enter** para rodar o código que você digitou.

`@pre_exercise_code`
```{python}

```

`@sct`
```{python}
msg1 = msg2 = msg3 = "Incorreto, tente novamente. Experimente os diferentes comandos de importação no shell do IPython e veja qual deles faz a linha `my_inv([[1, 2], [3, 4]])` rodar sem erros."
msg4 = "Correto! A palavra `as` permite que você crie um nome local para a função que está importando: `inv()` agora está disponível como `my_inv()`."
Ex().has_chosen(4, [msg1, msg2, msg3, msg4])
```

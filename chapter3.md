---
title_meta: Capítulo 3
title: Funções e pacotes
description: >-
  Você aprenderá a usar funções, métodos e pacotes para aproveitar com
  eficiência o código que os brilhantes desenvolvedores de Python escreveram. O
  objetivo é reduzir a quantidade de código que você precisa para resolver
  problemas desafiadores!
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

O Python oferece uma série de funções integradas para facilitar a vida de você como cientista de dados. Você já conhece duas dessas funções: [`print()`](https://docs.python.org/3/library/functions.html#print) e [`type()`](https://docs.python.org/3/library/functions.html#type). Há também funções como [`str()`](https://docs.python.org/3/library/functions.html#func-str), [`int()`](https://docs.python.org/3/library/functions.html#int), [`bool()`](https://docs.python.org/3/library/functions.html#bool) e [`float()`](https://docs.python.org/3/library/functions.html#float) para você alternar entre os tipos de dados. Essas também são funções incorporadas.

Chamar uma função é fácil. Para obter o tipo de `3.0` e armazenar a saída como uma nova variável, `result`, você pode usar o seguinte:

```
result = type(3.0)
```

`@instructions`
- Use [`print()`](https://docs.python.org/3/library/functions.html#print) em combinação com [`type()`](https://docs.python.org/3/library/functions.html#type) para imprimir o tipo de `var1`.
- Use [`len()`](https://docs.python.org/3/library/functions.html#len) para obter o comprimento da lista `var1`. Envolva-o em uma chamada [`print()`](https://docs.python.org/3/library/functions.html#print) para que você possa imprimi-lo diretamente.
- Use [`int()`](https://docs.python.org/3/library/functions.html#int) para converter `var2` em um número inteiro. Armazene a saída como `out2`.

`@hint`
- Chame a função [`type()`](https://docs.python.org/3/library/functions.html#type) da seguinte forma: `type(var1)`.
- Ligue para você [`print()`](https://docs.python.org/3/library/functions.html#print) como você fez tantas vezes antes. Basta colocar a variável que você deseja imprimir entre parênteses.
- `int(x)` converterá `x` em um número inteiro.

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
msg = "Você não precisa alterar ou remover as variáveis predefinidas."
Ex().check_object("var1", missing_msg=msg).has_equal_value(incorrect_msg=msg)
Ex().check_object("var2", missing_msg=msg).has_equal_value(incorrect_msg=msg)

patt = "__JINJA__:Certifique-se de imprimir o %s de `var1` com `{{sol_call}}`."
Ex().has_printout(0, not_printed_msg = patt % 'tipo')
Ex().has_printout(1, not_printed_msg = patt % 'comprimento')

int_miss_msg = "Você usou [`int()`](https://docs.python.org/3/library/functions.html#int) para fazer um inteiro de `var2`?"
int_incorr_msg = "Você passou `var2` para [`int()`](https://docs.python.org/3/library/functions.html#int)?"
Ex().check_correct(
  check_object("out2").has_equal_value(incorrect_msg="Você chamou `int()` corretamente; agora certifique-se de atribuir o resultado dessa chamada a `out2`."),
  check_function("int", missing_msg=int_miss_msg).has_equal_value(incorrect_msg=int_incorr_msg)
)
success_msg("Ótimo trabalho! A função `len()` é extremamente útil; ela também funciona em strings para contar o número de caracteres!")

```

---

## Você pode me ajudar!

```yaml
type: MultipleChoiceExercise
key: 679b852978
lang: python
xp: 50
skills:
  - 2
```

Talvez você já saiba o nome de uma função Python, mas ainda precisa descobrir como usá-la. Ironicamente, você precisa solicitar informações sobre uma função com outra função: `help()`. Em IPython especificamente, você também pode usar `?` antes do nome da função.

Para obter ajuda sobre a função `max()`, por exemplo, você pode usar uma dessas chamadas:

```
help(max)
?max
```

Use o shell IPython para abrir a documentação sobre [`pow()`](https://docs.python.org/3/library/functions.html#pow). Para isso, digite `?pow` ou `help(pow)` e pressione **Enter**.

Qual das seguintes afirmações é verdadeira?

`@possible_answers`
- `pow()` recebe três argumentos: `base`, `exp`, e `mod`. Sem `mod`, a função retornará um erro.
- `pow()` recebe três argumentos necessários: `base`, `exp`, e `None`.
- `pow()` requer os argumentos `base` e `exp`; `mod` é opcional.
- `pow()` recebe dois argumentos: `exp` e `mod`. A falta do endereço `exp` resulta em um erro.

`@hint`
- Os argumentos opcionais são definidos `=` como um valor padrão, que a função usará se esse argumento não for especificado.

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

## Argumentos múltiplos

```yaml
type: NormalExercise
key: e30486d7c1
lang: python
xp: 100
skills:
  - 2
```

No exercício anterior, você identificou argumentos opcionais ao visualizar a documentação com `help()`. Agora você aplicará isso para alterar o comportamento da função `sorted()`.

Dê uma olhada na documentação do [`sorted()`](https://docs.python.org/3/library/functions.html#sorted) digitando `help(sorted)` no shell ython IP.

Você verá que `sorted()` recebe três argumentos: `iterable`, `key`, e `reverse`. Neste exercício, você só precisará especificar `iterable` e `reverse`, não `key`.

Duas listas foram criadas para você.

Você pode colá-los e classificá-los em ordem decrescente?

`@instructions`
- Use `+` para mesclar o conteúdo de `first` e `second` em uma nova lista: `full`.
- Chame `sorted()` e em `full` e especifique o argumento `reverse` para ser `True`. Salve a lista ordenada como `full_sorted`.
- Para finalizar, imprima o site `full_sorted`.

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
msg = "Você não precisa alterar ou remover as variáveis `first` e `second` já existentes."
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

## Métodos de cadeia de caracteres

```yaml
type: NormalExercise
key: 4039302ee0
lang: python
xp: 100
skills:
  - 2
```

As cadeias de caracteres vêm com vários métodos. Siga atentamente as instruções para descobrir algumas delas. Se quiser descobri-los com mais detalhes, você sempre pode digitar `help(str)` no Shell IPython.

Uma string `place` já foi criada para você experimentar.

`@instructions`
- Use o método [`.upper()`](https://docs.python.org/3/library/stdtypes.html#str.upper) em `place` e armazene o resultado em `place_up`. Use a sintaxe para chamar métodos que você aprendeu no vídeo anterior.
- Imprima os sites `place` e `place_up`. Ambos mudaram?
- Imprima o número de o's na variável `place` chamando [`.count()`](https://docs.python.org/3/library/stdtypes.html#str.count) em `place` e passando a letra `'o'` como entrada para o método. Estamos falando sobre a variável `place`, não sobre a palavra `"place"`!

`@hint`
- Você pode chamar o método [`.upper()`](https://docs.python.org/3/library/stdtypes.html#str.upper) em `place` sem nenhuma entrada adicional.
- Para imprimir uma variável `x`, você pode escrever `print(x)`.
- Certifique-se de envolver sua chamada `place.count(____)` em uma função [`print()`](https://docs.python.org/3/library/functions.html#print) para que você a imprima.

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
msg = "Você não precisa alterar ou remover as variáveis predefinidas."
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
  has_printout(2, not_printed_msg = "Você calculou corretamente o número de 'o's em `place`; agora certifique-se de envolver a chamada `place.count('o')` em uma função `print()` para imprimir o resultado."),
  check_function("place.count", signature=False).check_args(0).has_equal_value()
)

success_msg("Legal! Note pelos resultados impressos que o método [upper()](https://docs.python.org/3/library/stdtypes.html#str.upper) não altera o objeto no qual é chamado. Isso será diferente para listas no próximo exercício!")

```

---

## Métodos de listagem

```yaml
type: NormalExercise
key: 0dbe8ed695
lang: python
xp: 100
skills:
  - 2
```

As cadeias de caracteres não são os únicos tipos Python que têm métodos associados a elas. Listas, floats, inteiros e booleanos também são tipos que vêm com vários métodos úteis. Neste exercício, você fará experiências com:

- [`.index()`](https://docs.python.org/3/library/stdtypes.html#str.index)para obter o índice do primeiro elemento de uma lista que corresponde à sua entrada e
- [`.count()`](https://docs.python.org/3/library/stdtypes.html#str.count)para obter o número de vezes que um elemento aparece em uma lista.

Você trabalhará na lista com a área de diferentes partes de uma casa: `areas`.

`@instructions`
- Use o método [`.index()`](https://docs.python.org/3/library/stdtypes.html#str.index) para obter o índice do elemento em `areas` que é igual a `20.0`. Imprima este índice.
- Ligue para [`.count()`](https://docs.python.org/3/library/stdtypes.html#str.count) Em `areas`, você saberá quantas vezes `9.50` aparece na lista. Novamente, basta imprimir esse número.

`@hint`
- Para imprimir o índice, envolva a chamada `areas.index(___)` em uma função [`print()`](https://docs.python.org/3/library/functions.html#print) função.
- Para imprimir o número de vezes que um elemento `x` ocorre na lista, envolva a chamada `areas.count(___)` em uma função [`print()`](https://docs.python.org/3/library/functions.html#print) função.

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
predef_msg = "Você não precisa alterar ou remover a lista predefinida `areas`."

Ex().check_object("areas", missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg)

Ex().check_function("print", index=0).check_args(0).check_function('areas.index', signature=False).check_args(0).has_equal_value()

Ex().check_function("print", index=1).check_args(0).check_function('areas.count', signature=False).has_equal_value()

success_msg("Legal! Estes foram exemplos de métodos de `list` que não alteraram a lista em que foram chamados.")
```

---

## Métodos de listagem (2)

```yaml
type: NormalExercise
key: 1fbeab82d0
lang: python
xp: 100
skills:
  - 2
```

A maioria dos métodos de lista altera a lista em que são chamados. Os exemplos são:

- [`.append()`](https://docs.python.org/3/library/stdtypes.html#typesseq-mutable)que adiciona um elemento à lista em que é chamado,
- [`.remove()`](https://docs.python.org/3/library/stdtypes.html#typesseq-mutable)que remove o primeiro elemento de uma lista que corresponde à entrada, e
- [`.reverse()`](https://docs.python.org/3/library/stdtypes.html#typesseq-mutable)que inverte a ordem dos elementos da lista em que é chamado.

Você trabalhará na lista com a área de diferentes partes da casa: `areas`.

`@instructions`
- Use [`.append()`](https://docs.python.org/3/library/stdtypes.html#typesseq-mutable) duas vezes para adicionar novamente o tamanho da casa da piscina e da garagem: `24.5` e `15.45`, respectivamente. Certifique-se de adicioná-los nesta ordem.
- Imprimir `areas`
- Use o método [`.reverse()`](https://docs.python.org/3/library/stdtypes.html#typesseq-mutable) para inverter a ordem dos elementos em `areas`.
- Imprima o site `areas` mais uma vez.

`@hint`
- Para a primeira instrução, use a chamada `areas.append(___)` duas vezes.
- Para imprimir uma variável `x`, basta escrever `print(x)`.
- O método [`.reverse()`](https://docs.python.org/3/library/stdtypes.html#typesseq-mutable) não requer entradas adicionais; basta usar a notação de ponto e parênteses vazios: `.reverse()`.
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

success_msg("Ótimo!")

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

## Pacote de importação

```yaml
type: NormalExercise
key: 7432a6376f
lang: python
xp: 100
skills:
  - 2
```

Digamos que você queira calcular a circunferência e a área de um círculo. Veja a seguir como são essas fórmulas:

$$C = 2 \pi r$$
$$A = \pi r^2 $$

Em vez de digitar o número para `pi`, você pode usar o pacote `math` que contém o número

Para referência, `**` é o símbolo de exponenciação. Por exemplo, `3**4` é `3` à potência de `4` e dará a você `81`.

`@instructions`
- Importe o pacote `math`.
- Use `math.pi` para calcular a circunferência do círculo e armazená-la em `C`.
- Use `math.pi` para calcular a área do círculo e armazená-la em `A`.

`@hint`
- Você pode simplesmente usar `import math` e, em seguida, fazer referência a `pi` com `math.pi`.
- Use a equação no texto do exercício para encontrar `C`. Usar `*`
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
  has_printout(0, not_printed_msg = "__JINJA__:Mantenha `{{sol_call}}` lá para imprimir a circunferência."),
  has_printout(1, not_printed_msg = "__JINJA__:Mantenha `{{sol_call}}` lá para imprimir a área.")
)

success_msg("Legal! Se você sabe como lidar com funções de pacotes, o poder de _muitos_ programadores Python está ao seu alcance!")
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

As importações gerais, como `import math`, disponibilizam para você **todas as** funcionalidades do pacote `math`. No entanto, se você decidir usar apenas uma parte específica de um pacote, sempre poderá tornar sua importação mais seletiva:

```
from math import pi
```

Tente fazer a mesma coisa novamente, mas desta vez use apenas `pi`.

`@instructions`
- Execute uma importação seletiva do pacote `math` em que você importa apenas a função `pi`.
- Use `math.pi` para calcular a circunferência do círculo e armazená-la em `C`.
- Use `math.pi` para calcular a área do círculo e armazená-la em `A`.
- Imprimir `dist`.

`@hint`
- Use o site `from math import pi` para fazer a importação seletiva.
- Agora, você pode usar o `pi` por conta própria!
- Para imprimir uma variável `x`, basta digitar `print(x)`.

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

success_msg("Bom trabalho! Vá para o próximo exercício.")

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

Há várias maneiras de importar pacotes e módulos para o Python. Dependendo da chamada de importação, você terá que usar um código Python diferente.

Suponha que você queira usar a função [`inv()`](http://docs.scipy.org/doc/numpy-1.10.0/reference/generated/numpy.linalg.inv.html)que está no subpacote `linalg` do pacote `scipy`. Você deseja poder usar essa função da seguinte forma:

```
my_inv([[1,2], [3,4]])
```

De qual instrução `import` você precisará para executar o código acima sem erros?

`@possible_answers`
- `import scipy`
- `import scipy.linalg`
- `from scipy.linalg import my_inv`
- `from scipy.linalg import inv as my_inv`

`@hint`
- Experimente as diferentes instruções de importação no shell IPython e veja qual delas faz com que a linha `my_inv([[1, 2], [3, 4]])` seja executada sem erros. Pressione **Enter** para executar o código que você digitou.

`@pre_exercise_code`
```{python}

```

`@sct`
```{python}
msg1 = msg2 = msg3 = "Incorreto, tente novamente. Experimente as diferentes instruções de importação no shell IPython e veja qual delas faz com que a linha `my_inv([[1, 2], [3, 4]])` seja executada sem erros."
msg4 = "Correto! A palavra `as` permite que você crie um nome local para a função que está importando: `inv()` agora está disponível como `my_inv()`."
Ex().has_chosen(4, [msg1, msg2, msg3, msg4])
```

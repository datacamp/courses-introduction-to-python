---
title_meta: Capítulo 2
title: Listas Python
description: >-
  Aprenda a armazenar, acessar e manipular dados em listas: a primeira etapa
  para trabalhar de forma eficiente com grandes quantidades de dados.
attachments:
  slides_link: 'https://projector-video-pdf-converter.datacamp.com/735/chapter2.pdf'
lessons:
  - nb_of_exercises: 4
    title: Listas Python
  - nb_of_exercises: 4
    title: Listas de subconjuntos
  - nb_of_exercises: 5
    title: Manipulação de listas
---

## Listas Python

```yaml
type: VideoExercise
key: a5886d213f
xp: 50
```

`@projector_key`
a0530c4542f10988847b2dbb91f717c3

---

## Criar uma lista

```yaml
type: NormalExercise
key: e6c527bf41
lang: python
xp: 100
skills:
  - 2
```

Uma lista é um **tipo de dados composto**; você pode agrupar valores, assim:

```
a = "is"
b = "nice"
my_list = ["my", "list", a, b]
```

Depois de medir a altura da sua família, você decide coletar algumas informações sobre a casa em que está morando. As áreas das diferentes partes de sua casa são armazenadas em variáveis separadas no exercício.

`@instructions`
- Crie uma lista, `areas`, que contenha a área do corredor (`hall`), cozinha (`kit`), sala de estar (`liv`), quarto (`bed`) e banheiro (`bath`), nesta ordem. Use as variáveis predefinidas.
- Imprima `areas` com a função `print()`.

`@hint`
- Você pode usar as variáveis que já foram criadas para criar a lista: `areas = [hall, kit, ...]`.
- Certifique-se de usar colchetes `[]` em vez de parênteses `()`.
- Você não precisa usar aspas ao armazenar variáveis em uma lista.
- Digite `print(areas)` para imprimir a lista ao enviá-la.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Create list areas


# Print areas

```

`@solution`
```{python}
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Create list areas
areas = [hall, kit, liv, bed, bath]

# Print areas
print(areas)
```

`@sct`
```{python}
predef_msg = "Não remova ou edite as variáveis predefinidas!"
areas_msg = "Defina `areas` como a lista contendo todas as variáveis de área, na ordem correta: `[hall, kit, liv, bed, bath]`. Cuidado com erros de digitação. A lista não deve conter mais nada!"

Ex().check_correct(
    has_printout(0, not_printed_msg = "__JINJA__:Você usou `{{sol_call}}` para imprimir a lista `areas` no final do seu script?"),
    check_correct(
        check_object("areas").has_equal_value(incorrect_msg = areas_msg),
        multi(
            check_object('hall', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
            check_object('kit', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
            check_object('liv', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
            check_object('bed', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
            check_object('bath', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg)
        )
    )
)

success_msg("Legal! Uma lista é bem melhor aqui, não é?")

```

---

## Criar listas com diferentes tipos

```yaml
type: NormalExercise
key: 1702a8bcdc
lang: python
xp: 100
skills:
  - 2
```

Embora não seja muito comum, uma lista também pode conter uma mistura de tipos Python, incluindo strings, floats e booleanos.

Agora você adicionará os nomes dos quartos à sua lista, para que possa ver facilmente o nome e o tamanho do quarto juntos.

Alguns dos códigos foram fornecidos para que você possa começar. Preste atenção aqui! `"bathroom"` é uma string, enquanto `bath` é uma variável que representa o float `9.50` que você especificou anteriormente.

`@instructions`
- Conclua o código que cria a lista `areas`. Crie a lista de modo que ela contenha primeiro o nome de cada cômodo como uma cadeia de caracteres e, em seguida, sua área. Em outras palavras, adicione as cadeias de caracteres `"hallway"`, `"kitchen"` e `"bedroom"` nos locais apropriados.
- Imprima novamente o site `areas`; dessa vez, a impressão é mais informativa?

`@hint`
- Os primeiros quatro elementos da lista `areas` são codificados como `["hallway", hall, "kitchen", kit, ...`.
- Uma cadeia de caracteres precisará estar entre aspas `""`.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Adapt list areas
areas = [____, hall, ____, kit, "living room", liv, ____, bed, "bathroom", bath]

# Print areas
____
```

`@solution`
```{python}
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Adapt list areas
areas = ["hallway", hall, "kitchen", kit, "living room", liv, "bedroom", bed, "bathroom", bath]

# Print areas
print(areas)
```

`@sct`
```{python}
objs = ["hall", "kit", "liv", "bed", "bath"]
predef_msg = "Não remova ou edite as variáveis predefinidas!"
areas_msg = "Você não atribuiu o valor correto a `areas`. Dê outra olhada nas instruções. Certifique-se de colocar o nome da sala antes da variável que contém a área cada vez. A ordem importa aqui! Cuidado com erros de digitação."

Ex().check_correct(
  check_object("areas").has_equal_value(incorrect_msg = areas_msg),
  multi([ check_object(obj, missing_msg = predef_msg).has_equal_value(incorrect_msg = predef_msg) for obj in objs])
)

Ex().has_printout(0, not_printed_msg = "__JINJA__:Você usou `{{sol_call}}` para imprimir a lista `areas` no final do seu script?")

success_msg("Legal! Esta lista contém tanto strings quanto floats, mas isso não é um problema para o Python!")
```

---

## Lista de listas

```yaml
type: NormalExercise
key: 9158c577b0
lang: python
xp: 100
skills:
  - 2
```

Como cientista de dados, você geralmente lida com muitos dados, e faz sentido agrupar alguns desses dados.

Em vez de criar uma lista contendo strings e floats, representando os nomes e as áreas dos cômodos da sua casa, você pode criar uma lista de listas.

Lembre-se: `"hallway"` é uma cadeia de caracteres, enquanto `hall` é uma variável que representa o float `11.25` que você especificou anteriormente.

`@instructions`
- Termine a lista de listas para que ela também contenha os dados do quarto e do banheiro. Certifique-se de que você os insira em ordem!
- Imprima `house`; essa forma de estruturar seus dados faz mais sentido para você?

`@hint`
- Adicione _sublistas_ à lista `house` acrescentando `["bedroom", bed]` e `["bathroom", bath]` dentro dos colchetes.
- Para imprimir uma variável `x`, escreva `print(x)` em uma nova linha.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# House information as list of lists
house = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv],
        ____,
        ____]

# Print out house
____
```

`@solution`
```{python}
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# House information as list of lists
house = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv],
         ["bedroom", bed],
         ["bathroom", bath]]

# Print out house
print(house)
```

`@sct`
```{python}
predef_msg = "Não remova ou edite as variáveis predefinidas!"
house_msg = "Você não atribuiu o valor correto a `house`. Dê outra olhada nas instruções. Estenda a lista de listas para que ela incorpore uma lista para cada par de nome de sala e área da sala. Atenção à ordem e aos erros de digitação!"

Ex().check_correct(
    check_object("house").has_equal_value(incorrect_msg = house_msg),
    multi(
        check_object('hall', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
        check_object('kit', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
        check_object('liv', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
        check_object('bed', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
        check_object('bath', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg)
    )
)

Ex().has_printout(0, not_printed_msg = "__JINJA__:Você usou `{{sol_call}}` para imprimir o conteúdo de `house`?")

success_msg("Ótimo! Prepare-se para aprender sobre subdefinição de listas!")
```

---

## Listas de subconjuntos

```yaml
type: VideoExercise
key: c076b5a69c
xp: 50
```

`@projector_key`
fc15ba5cb9485456df8589130b519ea3

---

## Subconjunto e conquista

```yaml
type: NormalExercise
key: c3ce582e32
lang: python
xp: 100
skills:
  - 2
```

O subconjunto de listas Python é muito fácil. Veja o exemplo de código abaixo, que cria uma lista `x` e, em seguida, seleciona "b" nela. Lembre-se de que esse é o segundo elemento, portanto, tem índice 1. Você também pode usar a indexação negativa.

```
x = ["a", "b", "c", "d"]
x[1]
x[-3] # same result!
```

Você se lembra da lista `areas` de antes, que contém strings e floats? Sua definição já está no script. Você pode adicionar o código correto para fazer alguma subconfiguração do Python?

`@instructions`
- Imprima o segundo elemento da lista `areas` (ele tem o valor `11.25`).
- Faça um subconjunto e imprima o último elemento de `areas`, sendo `9.50`. Usar um índice negativo faz sentido aqui!
- Selecione o número que representa a área da sala de estar (`20.0`) e imprima-o.

`@hint`
- Use `x[1]` para selecionar o segundo elemento de uma lista `x`.
- Use `x[-1]` para selecionar o último elemento de uma lista `x`.
- Certifique-se de envolver suas operações de subconjunto em uma chamada `print()`.
- O número que representa a área da sala de estar é o sexto elemento da lista, portanto, você precisará de `[5]` aqui. `area[4]` mostraria a string!

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Print out second element from areas
print(areas[____])

# Print out last element from areas
print(areas[____])

# Print out the area of the living room
print(areas[____])
```

`@solution`
```{python}
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Print out second element from areas
print(areas[1])

# Print out last element from areas
print(areas[-1])

# Print out the area of the living room
print(areas[5])
```

`@sct`
```{python}
msg = "Não remova ou edite a lista `areas` predefinida."
Ex().check_object("areas", missing_msg = msg).has_equal_value(incorrect_msg = msg)
Ex().has_printout(0, not_printed_msg = "Dê outra olhada no seu código para imprimir o segundo elemento em `areas`, que está no índice `1`.")
Ex().has_printout(1, not_printed_msg = "Dê outra olhada no seu código para imprimir o último elemento em `areas`, que está no índice `-1`.")
Ex().has_printout(2, not_printed_msg = "Dê outra olhada no seu código para imprimir a área da sala de estar. Está no índice `5`.")
success_msg("Bom trabalho!")
```

---

## Fatiar e cortar em cubos

```yaml
type: NormalExercise
key: 7f08642d18
lang: python
xp: 100
skills:
  - 2
```

A seleção de valores individuais em uma lista é apenas uma parte da história. Também é possível _dividir_ sua lista, o que significa selecionar vários elementos da lista. Use a seguinte sintaxe:

```
my_list[start:end]
```

O índice `start` será incluído, enquanto o índice `end` _não_ será. No entanto, também é possível não especificar esses índices. Se você não especificar o índice `start`, o Python entenderá que você deseja iniciar a fatia no início da lista.

`@instructions`
- Use o fatiamento para criar uma lista, `downstairs`, que contém os primeiros 6 elementos de `areas`.
- Crie `upstairs`, como os últimos elementos de `4` de `areas`. Desta vez, simplifique o fatiamento omitindo o índice `end`.
- Imprima os sites `downstairs` e `upstairs` usando `print()`.

`@hint`
- Use os colchetes `[0:6]` para obter os seis primeiros elementos de uma lista.
- Para obter tudo, exceto os 5 primeiros elementos de uma lista, `l`, você usaria `l[5:]`.
- Adicione duas chamadas `print()` para imprimir `downstairs` e `upstairs`.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Use slicing to create downstairs
downstairs = areas[____]

# Use slicing to create upstairs
upstairs = areas[____]

# Print out downstairs and upstairs
____
____
```

`@solution`
```{python}
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Use slicing to create downstairs
downstairs = areas[0:6]

# Use slicing to create upstairs
upstairs = areas[6:]

# Print out downstairs and upstairs
print(downstairs)
print(upstairs)
```

`@sct`
```{python}
msg = "Não remova ou edite a lista `areas` predefinida."
Ex().check_object("areas", missing_msg = msg).has_equal_value(incorrect_msg = msg)

patt = "`%s` está incorreto. Use `areas[%s]` e fatiamento para selecionar os elementos que você deseja, ou algo equivalente."
Ex().check_object("downstairs").has_equal_value(incorrect_msg = patt % ('downstairs', '0:6'))
Ex().check_object("upstairs").has_equal_value(incorrect_msg = patt % ("upstairs",":6"))

Ex().has_printout(0, not_printed_msg="Você imprimiu `downstairs` após calculá-lo?")
Ex().has_printout(1, not_printed_msg="Você imprimiu `upstairs` após calculá-lo?")

success_msg("Ótimo!")
```

---

## Subconjunto de listas de listas

```yaml
type: NormalExercise
key: dbbbd306cf
xp: 100
```

Uma lista Python também pode conter outras listas.

Para subconjunto de listas de listas, você pode usar a mesma técnica de antes: colchetes. Isso seria algo assim para uma lista, `x`:

```
x[2][0]
```

`@instructions`
- Faça um subconjunto da lista `house` para obter o float `9.5`.

`@hint`
- Você pode detalhar isso passo a passo. Primeiro, você deseja chegar ao último elemento da lista, `["bathroom", 9.50]`. Lembre-se de que o índice do último elemento é `-1`.
- Em seguida, você deseja obter o segundo elemento de `["bathroom", 9.50]`, que está no índice `1`.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
house = [["hallway", 11.25],
         ["kitchen", 18.0],
         ["living room", 20.0],
         ["bedroom", 10.75],
         ["bathroom", 9.50]]

# Subset the house list
house___
```

`@solution`
```{python}
house = [["hallway", 11.25],
         ["kitchen", 18.0],
         ["living room", 20.0],
         ["bedroom", 10.75],
         ["bathroom", 9.50]]

# Subset the house list
house[-1][1]
```

`@sct`
```{python}
Ex().has_code("house[-1][1]", pattern=False)

success_msg("Correctomundo! A última peça do quebra-cabeça da lista é a manipulação.")
```

---

## Manipulação de listas

```yaml
type: VideoExercise
key: d7fe818b3a
xp: 50
```

`@projector_key`
355ed52d2fb0d67508c6a311b7cbc6d3

---

## Substituir elementos da lista

```yaml
type: NormalExercise
key: 4e1bba1b55
lang: python
xp: 100
skills:
  - 2
```

Para substituir elementos da lista, você faz um subconjunto da lista e atribui novos valores ao subconjunto. Você pode selecionar elementos individuais ou alterar fatias inteiras da lista de uma só vez.

Para este e os próximos exercícios, você continuará trabalhando na lista `areas` que contém os nomes e as áreas dos diferentes cômodos de uma casa.

`@instructions`
- Atualize a área do banheiro para `10.50` metros quadrados em vez de `9.50`.
- Deixe a lista do `areas` mais moderna! Altere `"living room"` para `"chill zone"`.

`@hint`
- Para atualizar a área do banheiro, identifique o subconjunto da área do banheiro (é o último item da lista!).
- Em seguida, substitua o valor pela nova área do banheiro, atribuindo-o a esse subconjunto.
- Faça o mesmo para atualizar o nome `"living room"`, que está no índice 4.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Correct the bathroom area


# Change "living room" to "chill zone"

```

`@solution`
```{python}
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Correct the bathroom area
areas[-1] = 10.50

# Change "living room" to "chill zone"
areas[4] = "chill zone"
```

`@sct`
```{python}
bathroom_msg = 'Você pode usar `areas[-1] = 10.50` para atualizar a área do banheiro.'
chillzone_msg = 'Você pode usar `areas[4] = "chill zone"` para atualizar o nome da sala de estar.'
Ex().check_correct(
  check_object('areas').has_equal_value(incorrect_msg = 'Suas alterações em `areas` não resultaram na lista correta. Você tem certeza de que usou as operações de subconjunto corretas? Em caso de dúvida, você pode usar uma dica!'),
  multi(
    has_equal_value(expr_code='areas[-1]', override=10.50, incorrect_msg = bathroom_msg),
    has_equal_value(expr_code='areas[4]', override='chill zone', incorrect_msg = chillzone_msg),
  )
)
success_msg('Legal! Como o exemplo de código mostrou, você também pode fatiar uma lista e substituí-la por outra lista para atualizar vários elementos em um único comando.')
```

---

## Estender uma lista

```yaml
type: NormalExercise
key: ff0fe8d967
lang: python
xp: 100
skills:
  - 2
```

Se você pode alterar elementos em uma lista, com certeza quer poder adicionar elementos a ela, certo? Você pode usar o operador `+`:

```
x = ["a", "b", "c", "d"]
y = x + ["e", "f"]
```

Você acabou de ganhar na loteria, incrível! Você decide construir uma casa para a piscina e uma garagem. Você pode adicionar as informações à lista `areas`?

`@instructions`
- Use o operador `+` para colar a lista `["poolhouse", 24.5]` no final da lista `areas`. Armazene a lista resultante como `areas_1`.
- Amplie ainda mais o site `areas_1` adicionando dados sobre sua garagem. Adicione a string `"garage"` e o float `15.45`. Nomeie a lista resultante como `areas_2`.

`@hint`
- Siga o exemplo de código na atribuição. `x` é `areas` aqui, e `["e", "f"]` é `["poolhouse", 24.5]`.
- Para adicionar mais elementos a `areas_1`, use `areas_1 + ["element", 123]`.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create the areas list and make some changes
areas = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0,
         "bedroom", 10.75, "bathroom", 10.50]

# Add poolhouse data to areas, new list is areas_1
areas_1 = ____

# Add garage data to areas_1, new list is areas_2
areas_2 = ____
```

`@solution`
```{python}
# Create the areas list (updated version)
areas = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0,
         "bedroom", 10.75, "bathroom", 10.50]

# Add poolhouse data to areas, new list is areas_1
areas_1 = areas + ["poolhouse", 24.5]

# Add garage data to areas_1, new list is areas_2
areas_2 = areas_1 + ["garage", 15.45]
```

`@sct`
```{python}
msg = "Não remova ou edite a lista `areas` predefinida."
Ex().check_object("areas", missing_msg = msg).has_equal_value(incorrect_msg = msg)
Ex().check_object("areas_1").has_equal_value(incorrect_msg = "Use `areas + [\"poolhouse\", 24.5]` para criar `areas_1`. Cuidado com erros de digitação!")
Ex().check_object("areas_2").has_equal_value(incorrect_msg = "Use `areas_1 + [\"garage\", 15.45]` para criar `areas_2`. Cuidado com erros de digitação!")
success_msg("Legal! A lista está tomando forma!")
```

---

## Excluir elementos da lista

```yaml
type: NormalExercise
key: 85f792356e
xp: 100
```

Por fim, você também pode remover elementos da sua lista. Você pode fazer isso com a declaração `del`:

```
x = ["a", "b", "c", "d"]
del x[1]
```

Preste atenção aqui: assim que você remove um elemento de uma lista, todos os índices dos elementos que vêm depois do elemento excluído mudam!

Infelizmente, a quantia que você ganhou na loteria não é tão grande assim e parece que a casa da piscina não vai acontecer. Você precisará removê-lo da lista. Você decide remover a string e o float correspondentes da lista `areas`.

`@instructions`
- Exclua a string e o float para `"poolhouse"` da lista `areas`.
- Imprima a lista atualizada do site `areas`.

`@hint`
- Você precisará usar `del` duas vezes para excluir dois elementos. Mas tenha cuidado ao alterar os índices!

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
areas = ["hallway", 11.25, "kitchen", 18.0,
        "chill zone", 20.0, "bedroom", 10.75,
         "bathroom", 10.50, "poolhouse", 24.5,
         "garage", 15.45]

# Delete the poolhouse from the list


# Print the updated list

```

`@solution`
```{python}
areas = ["hallway", 11.25, "kitchen", 18.0,
        "chill zone", 20.0, "bedroom", 10.75,
         "bathroom", 10.50, "poolhouse", 24.5,
         "garage", 15.45]

# Delete the poolhouse from the list
del areas[10]
del areas[10]

# Print the updated list
print(areas)
```

`@sct`
```{python}
Ex().multi(
  has_code("del areas[10]", pattern=False),
  has_code("del areas[10]", pattern=False)
)

Ex().has_printout(0, not_printed_msg="Você imprimiu `areas` após remover a string e o float de poolhouse?")
success_msg("Correto! Você aprenderá maneiras mais fáceis de remover elementos específicos de listas Python mais tarde.")
```

---

## Funcionamento interno das listas

```yaml
type: NormalExercise
key: af72db9915
lang: python
xp: 100
skills:
  - 2
```

Alguns códigos foram fornecidos para você neste exercício: uma lista com o nome `areas` e uma cópia chamada `areas_copy`.

Atualmente, o primeiro elemento da lista `areas_copy` é alterado e a lista `areas` é impressa. Se você pressionar o botão executar código, verá que, embora tenha alterado `areas_copy`, a alteração também terá efeito na lista `areas`. Isso ocorre porque `areas` e `areas_copy` apontam para a mesma lista.

Se quiser evitar que as alterações em `areas_copy` também tenham efeito em `areas`, você terá de fazer uma cópia mais explícita da lista `areas` com `list()` ou usando `[:]`.

`@instructions`
- Altere o segundo comando, que cria a variável `areas_copy`, de modo que `areas_copy` seja uma cópia explícita de `areas`. Depois que você editar, as alterações feitas em `areas_copy` não deverão afetar `areas`. Envie a resposta para você verificar isso.

`@hint`
- Altere a chamada `areas_copy = areas`. Em vez de atribuir `areas`, você pode atribuir `list(areas)` ou `areas[:]`.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Change this command
areas_copy = areas

# Change areas_copy
areas_copy[0] = 5.0

# Print areas
print(areas)
```

`@solution`
```{python}
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Change this command
areas_copy = list(areas)

# Change areas_copy
areas_copy[0] = 5.0

# Print areas
print(areas)
```

`@sct`
```{python}
Ex().check_correct(
  check_object("areas_copy").has_equal_value(incorrect_msg = "Parece que `areas_copy` não foi atualizado corretamente."),
  check_function("list", missing_msg = "Certifique-se de usar `list(areas)` para criar um `areas_copy`.")
)

mmsg = "Não remova a lista `areas` predefinida."
imsg = "Certifique-se de editar SOMENTE a cópia, não a lista original `areas`. Dê outra olhada na descrição do exercício se não tiver certeza de como criar uma cópia."
Ex().check_correct(
  check_object("areas", missing_msg = mmsg).has_equal_value(incorrect_msg = imsg),
  check_function("list", missing_msg = "Certifique-se de usar `list(areas)` para criar um `areas_copy`.")
)

success_msg("Legal! A diferença entre cópias explícitas e baseadas em referência é sutil, mas pode ser realmente importante. Tente lembrar como uma lista é armazenada na memória do computador.")
```

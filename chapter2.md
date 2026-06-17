---
title_meta: Chapitre 2
title: Listes en Python
description: "Apprenez à stocker, accéder et manipuler des données dans des listes\_: la première étape pour travailler efficacement avec de très grandes quantités de données."
attachments:
  slides_link: 'https://projector-video-pdf-converter.datacamp.com/735/chapter2.pdf'
lessons:
  - nb_of_exercises: 4
    title: Listes en Python
  - nb_of_exercises: 4
    title: Sous-ensembles de listes
  - nb_of_exercises: 5
    title: Manipuler les listes
---

## Listes en Python

```yaml
type: VideoExercise
key: a5886d213f
xp: 50
```

`@projector_key`
a0530c4542f10988847b2dbb91f717c3

---

## Créer une liste

```yaml
type: NormalExercise
key: e6c527bf41
lang: python
xp: 100
skills:
  - 2
```

Une liste est un **type de données composé**; vous pouvez regrouper des valeurs comme ceci :

```
a = "is"
b = "nice"
my_list = ["my", "list", a, b]
```

Après avoir mesuré la taille des membres de votre famille, vous décidez de recueillir quelques informations sur la maison où vous habitez. Les superficies des différentes pièces de votre maison sont stockées dans des variables distinctes dans l'exercice.

`@instructions`
- Créez une liste, `areas`, qui contient la superficie du corridor (`hall`), de la cuisine (`kit`), du salon (`liv`), de la chambre (`bed`) et de la salle de bain (`bath`), dans cet ordre. Utilisez les variables déjà définies.
- Affichez `areas` avec la fonction `print()`.

`@hint`
- Vous pouvez utiliser les variables déjà créées pour construire la liste : `areas = [hall, kit, ...]`.
- Assurez-vous d'utiliser des crochets `[]` plutôt que des parenthèses `()`.
- Vous n'avez pas besoin de guillemets lorsque vous stockez des variables dans une liste.
- Tapez `print(areas)` pour afficher la liste au moment de **Soumettre la réponse**.

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
predef_msg = "Ne supprimez pas et n'éditez pas les variables prédéfinies !"
areas_msg = "Définissez `areas` comme la liste contenant toutes les variables de surface, dans l'ordre correct : `[hall, kit, liv, bed, bath]`. Faites attention aux fautes de frappe. La liste ne doit rien contenir d'autre !"

Ex().check_correct(
    has_printout(0, not_printed_msg = "__JINJA__:Avez-vous utilisé `{{sol_call}}` pour imprimer la liste `areas` à la fin de votre script ?"),
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

success_msg("Bien joué ! Une liste est bien meilleure ici, n'est-ce pas ?")
```

---

## Créer des listes avec différents types

```yaml
type: NormalExercise
key: 1702a8bcdc
lang: python
xp: 100
skills:
  - 2
```

Même si ce n'est pas très courant, une liste peut aussi contenir un mélange de types Python, dont des chaînes, des nombres à virgule flottante et des booléens.

Vous allez maintenant ajouter les noms des pièces à votre liste, pour pouvoir voir facilement à la fois le nom de la pièce et sa superficie.

Une partie du code est déjà fournie pour vous mettre en route. Attention ici ! `"bathroom"` est une chaîne de caractères, alors que `bath` est une variable qui représente le nombre flottant `9.50` que vous avez défini plus tôt.

`@instructions`
- Complétez le code qui crée la liste `areas`. Construisez la liste de sorte qu'elle contienne d'abord le nom de chaque pièce comme chaîne de caractères, puis sa superficie. Autrement dit, ajoutez les chaînes `"hallway"`, `"kitchen"` et `"bedroom"` aux bons endroits.
- Affichez de nouveau `areas` ; l'affichage est-il plus informatif cette fois-ci ?

`@hint`
- Les quatre premiers éléments de la liste `areas` sont codés comme `["hallway", hall, "kitchen", kit, ...`.
- Une chaîne de caractères doit être entre guillemets `""`.

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
predef_msg = "Ne supprimez pas et n'éditez pas les variables prédéfinies !"
areas_msg = "Vous n'avez pas assigné la valeur correcte à `areas`. Consultez à nouveau les instructions. Assurez-vous de placer le nom de la pièce avant la variable contenant la superficie à chaque fois. L'ordre est important ici ! Faites attention aux fautes de frappe."

Ex().check_correct(
  check_object("areas").has_equal_value(incorrect_msg = areas_msg),
  multi([ check_object(obj, missing_msg = predef_msg).has_equal_value(incorrect_msg = predef_msg) for obj in objs])
)

Ex().has_printout(0, not_printed_msg = "__JINJA__:Avez-vous utilisé `{{sol_call}}` pour imprimer la liste `areas` à la fin de votre script ?")

success_msg("Bien joué ! Cette liste contient à la fois des chaînes de caractères et des nombres à virgule flottante, mais ce n'est pas un problème pour Python !")
```

---

## Liste de listes

```yaml
type: NormalExercise
key: 9158c577b0
lang: python
xp: 100
skills:
  - 2
```

En tant que spécialiste des données, vous manipulerez souvent de grandes quantités de données, et il sera logique d'en regrouper certaines.

Plutôt que de créer une liste contenant des chaînes de caractères et des nombres à virgule flottante pour représenter les noms et les superficies des pièces de votre maison, vous pouvez créer une liste de listes.

Rappel : `"hallway"` est une chaîne de caractères, tandis que `hall` est une variable qui représente le nombre à virgule flottante `11.25` que vous avez défini plus tôt.

`@instructions`
- Complétez la liste de listes pour qu'elle contienne aussi les données de la chambre et de la salle de bain. Assurez-vous de les saisir dans cet ordre !
- Affichez `house` ; cette façon d'organiser vos données est-elle plus logique ?

`@hint`
- Ajoutez des _sous-listes_ à la liste `house` en insérant `["bedroom", bed]` et `["bathroom", bath]` entre les crochets.
- N'oubliez pas d'ajouter une virgule `,` après chaque sous-liste.
- Pour afficher une variable `x`, écrivez `print(x)` sur une nouvelle ligne.

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
predef_msg = "Ne supprimez pas et n'éditez pas les variables prédéfinies !"
house_msg = "Vous n'avez pas assigné la valeur correcte à `house`. Consultez à nouveau les instructions. Étendez la liste de listes pour qu'elle incorpore une liste pour chaque paire de nom de pièce et de surface de pièce. Faites attention à l'ordre et aux fautes de frappe !"

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

Ex().has_printout(0, not_printed_msg = "__JINJA__:Avez-vous utilisé `{{sol_call}}` pour imprimer le contenu de `house` ?")

success_msg("Super ! Préparez-vous à apprendre le sous-ensemble de listes !")
```

---

## Sous-ensembles de listes

```yaml
type: VideoExercise
key: c076b5a69c
xp: 50
```

`@projector_key`
fc15ba5cb9485456df8589130b519ea3

---

## Sous-ensembles et victoire

```yaml
type: NormalExercise
key: c3ce582e32
lang: python
xp: 100
skills:
  - 2
```

Créer des sous-ensembles dans des listes Python, c'est tout simple. Regardez l'exemple ci-dessous, qui crée une liste `x` puis sélectionne « b » dedans. N'oubliez pas que c'est le deuxième élément, donc son indice est 1. Vous pouvez aussi utiliser des indices négatifs.

```
x = ["a", "b", "c", "d"]
x[1]
x[-3] # même résultat !
```

Vous vous souvenez de la liste `areas` plus tôt, qui contient à la fois des chaînes et des nombres à virgule flottante ? Sa définition est déjà dans le script. Pouvez-vous ajouter le code adéquat pour faire quelques sous-ensembles en Python ?

`@instructions`
- Affichez le deuxième élément de la liste `areas` (sa valeur est `11.25`).
- Créez un sous-ensemble et affichez le dernier élément de `areas`, soit `9.50`. Utiliser un indice négatif est logique ici !
- Sélectionnez le nombre qui représente la superficie du salon (`20.0`) et affichez-le.

`@hint`
- Utilisez `x[1]` pour sélectionner le deuxième élément d'une liste `x`.
- Utilisez `x[-1]` pour sélectionner le dernier élément d'une liste `x`.
- Assurez-vous d'entourer vos opérations de sous-ensemble d'un appel à `print()`.
- Le nombre qui correspond à la superficie du salon est le 6e élément de la liste, donc vous aurez besoin de `[5]` ici. `area[4]` afficherait la chaîne de caractères !

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
msg = "Ne supprimez pas et n'éditez pas la liste prédéfinie `areas`."
Ex().check_object("areas", missing_msg = msg).has_equal_value(incorrect_msg = msg)
Ex().has_printout(0, not_printed_msg = "Jetez un autre coup d'œil à votre code pour imprimer le deuxième élément dans `areas`, qui est à l'index `1`.")
Ex().has_printout(1, not_printed_msg = "Jetez un autre coup d'œil à votre code pour imprimer le dernier élément dans `areas`, qui est à l'index `-1`.")
Ex().has_printout(2, not_printed_msg = "Jetez un autre coup d'œil à votre code pour imprimer la superficie du salon. Elle est à l'index `5`.")
success_msg("Bon travail !")
```

---

## Découper en tranches

```yaml
type: NormalExercise
key: 7f08642d18
lang: python
xp: 100
skills:
  - 2
```

Sélectionner des valeurs uniques dans une liste n'est qu'une partie de l'histoire. Vous pouvez aussi faire une _tranche_ (slice) de votre liste, c'est‑à‑dire sélectionner plusieurs éléments à la fois. Utilisez la syntaxe suivante :

```
my_list[start:end]
```

L'indice `start` est inclus, tandis que l'indice `end` ne l'est _pas_. Il est toutefois possible de ne pas préciser ces indices. Si vous n'indiquez pas l'indice de `start`, Python comprend que vous voulez commencer la tranche au début de la liste.

`@instructions`
- Utilisez le découpage pour créer une liste `downstairs` qui contient les 6 premiers éléments de `areas`.
- Créez `upstairs` avec les `4` derniers éléments de `areas`. Cette fois, simplifiez le découpage en omettant l'indice de `end`.
- Affichez `downstairs` et `upstairs` avec `print()`.

`@hint`
- Utilisez les crochets `[0:6]` pour obtenir les six premiers éléments d'une liste.
- Pour obtenir tout sauf les 5 premiers éléments d'une liste `l`, utilisez `l[5:]`.
- Ajoutez deux appels à `print()` pour afficher `downstairs` et `upstairs`.

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
msg = "Ne supprimez pas et n'éditez pas la liste prédéfinie `areas`."
Ex().check_object("areas", missing_msg = msg).has_equal_value(incorrect_msg = msg)

patt = "`%s` est incorrect. Utilisez `areas[%s]` et le découpage pour sélectionner les éléments que vous souhaitez, ou quelque chose d'équivalent."
Ex().check_object("downstairs").has_equal_value(incorrect_msg = patt % ('downstairs', '0:6'))
Ex().check_object("upstairs").has_equal_value(incorrect_msg = patt % ("upstairs",":6"))

Ex().has_printout(0, not_printed_msg="Avez-vous imprimé `downstairs` après l'avoir calculé ?")
Ex().has_printout(1, not_printed_msg="Avez-vous imprimé `upstairs` après l'avoir calculé ?")

success_msg("Super !")
```

---

## Sous-ensemble de listes de listes

```yaml
type: NormalExercise
key: dbbbd306cf
xp: 100
```

Une liste Python peut aussi contenir d'autres listes.

Pour extraire des éléments de listes de listes, vous pouvez utiliser la même technique qu'auparavant : des crochets. Pour une liste `house`, cela donnerait quelque chose comme :

```
house[2][0]
```

`@instructions`
- Créez un sous-ensemble de la liste `house` pour obtenir le nombre à virgule flottante `9.5`.

`@hint`
- Procédez étape par étape. D'abord, accédez au dernier élément de la liste, `["bathroom", 9.50]`. Rappel : l'indice du dernier élément est `-1`.
- Ensuite, récupérez le deuxième élément de `["bathroom", 9.50]`, qui se trouve à l'indice `1`.

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
Ex().check_or(
  has_code("house[-1][1]", pattern=False),
  has_code("house[4][1]", pattern=False)
)

success_msg("Correctomundo! Le dernier élément du casse-tête de la liste est la manipulation.")
```

---

## Manipuler des listes

```yaml
type: VideoExercise
key: d7fe818b3a
xp: 50
```

`@projector_key`
355ed52d2fb0d67508c6a311b7cbc6d3

---

## Remplacer des éléments de liste

```yaml
type: NormalExercise
key: 4e1bba1b55
lang: python
xp: 100
skills:
  - 2
```

Pour remplacer des éléments d'une liste, vous isolez un sous-ensemble de la liste et vous lui assignez de nouvelles valeurs. Vous pouvez sélectionner des éléments uniques ou modifier des tranches entières de la liste d'un seul coup.

Pour cet exercice et les suivants, vous continuerez à travailler avec la liste `areas`, qui contient les noms et superficies des différentes pièces d'une maison.

`@instructions`
- Mettez à jour la superficie de la salle de bain à `10.50` mètres carrés au lieu de `9.50` en utilisant l'indexation négative.
- Rendez la liste `areas` plus tendance! Remplacez `"living room"` par `"chill zone"`. N'utilisez pas l'indexation négative cette fois-ci.

`@hint`
- Pour mettre à jour la superficie de la salle de bain, repérez la partie correspondante (c'est le dernier élément de la liste!).
- Remplacez ensuite la valeur par la nouvelle superficie en l'assignant à ce sous-ensemble.
- Faites de même pour mettre à jour le nom `"living room"`, qui se trouve à l'indice 4.

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
bathroom_msg = 'Vous pouvez utiliser `areas[-1] = 10.50` pour mettre à jour la superficie de la salle de bain.'
chillzone_msg = 'Vous pouvez utiliser `areas[4] = "chill zone"` pour mettre à jour le nom du salon.'
Ex().check_correct(
  check_object('areas').has_equal_value(incorrect_msg = 'Vos modifications de `areas` n\'ont pas abouti à la liste correcte. Êtes-vous sûr d\'avoir utilisé les bonnes opérations de sous-ensemble ? En cas de doute, vous pouvez utiliser un indice !'),
  multi(
    has_equal_value(expr_code='areas[-1]', override=10.50, incorrect_msg = bathroom_msg),
    has_equal_value(expr_code='areas[4]', override='chill zone', incorrect_msg = chillzone_msg),
  )
)
success_msg('Super ! Comme l\'exemple de code l\'a montré, vous pouvez également découper une liste et la remplacer par une autre liste pour mettre à jour plusieurs éléments en une seule commande.')
```

---

## Allonger une liste

```yaml
type: NormalExercise
key: ff0fe8d967
lang: python
xp: 100
skills:
  - 2
```

Si vous pouvez modifier des éléments dans une liste, vous voudrez certainement pouvoir y ajouter des éléments, n'est-ce pas? Vous pouvez utiliser l'opérateur `+` :

```
x = ["a", "b", "c", "d"]
y = x + ["e", "f"]
```

Vous venez de gagner à la loterie, génial! Vous décidez de construire une remise avec piscine et un garage. Pouvez-vous ajouter ces renseignements à la liste `areas`?

`@instructions`
- Utilisez l'opérateur `+` pour coller la liste `["poolhouse", 24.5]` à la fin de la liste `areas`. Enregistrez la liste obtenue dans `areas_1`.
- Allongez ensuite `areas_1` en ajoutant les données sur votre garage. Ajoutez la chaîne `"garage"` et le nombre à virgule flottante `15.45`. Nommez la liste obtenue `areas_2`.

`@hint`
- Suivez l'exemple de code dans l'énoncé. Ici, `x` correspond à `areas`, et `["e", "f"]` correspond à `["poolhouse", 24.5]`.
- Pour ajouter d'autres éléments à `areas_1`, utilisez `areas_1 + ["element", 123]`.

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
msg = "Ne supprimez pas et n'éditez pas la liste prédéfinie `areas`."
Ex().check_object("areas", missing_msg = msg).has_equal_value(incorrect_msg = msg)
Ex().check_object("areas_1").has_equal_value(incorrect_msg = "Utilisez `areas + [\"poolhouse\", 24.5]` pour créer `areas_1`. Faites attention aux fautes de frappe !")
Ex().check_object("areas_2").has_equal_value(incorrect_msg = "Utilisez `areas_1 + [\"garage\", 15.45]` pour créer `areas_2`. Faites attention aux fautes de frappe !")
success_msg("Super ! La liste prend forme agréablement !")
```

---

## Supprimer des éléments d'une liste

```yaml
type: NormalExercise
key: 85f792356e
xp: 100
```

Enfin, vous pouvez aussi retirer des éléments de votre liste. Pour ce faire, utilisez l'instruction `del` :

```
x = ["a", "b", "c", "d"]
del x[1]
```

Attention : dès que vous supprimez un élément d'une liste, les index des éléments qui suivent l'élément supprimé changent tous !

Malheureusement, le montant que vous avez gagné à la loterie n'est finalement pas si élevé et il semble que l'« poolhouse » ne se réalisera pas. Vous devez l'enlever de la liste. Vous décidez de supprimer la chaîne de caractères et le nombre à virgule flottante correspondants de la liste `areas`.

`@instructions`
- Supprimez la chaîne et le nombre à virgule flottante pour `"poolhouse"` de votre liste `areas`.
- Affichez la liste `areas` mise à jour.

`@hint`
- Vous devrez utiliser `del` deux fois pour supprimer deux éléments. Attention : les index changent !

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
areas = ["hallway", 11.25, "kitchen", 18.0,
        "chill zone", 20.0, "bedroom", 10.75,
         "bathroom", 10.50, "poolhouse", 24.5,
         "garage", 15.45]

# Delete the poolhouse items from the list


# Print the updated list

```

`@solution`
```{python}
areas = ["hallway", 11.25, "kitchen", 18.0,
        "chill zone", 20.0, "bedroom", 10.75,
         "bathroom", 10.50, "poolhouse", 24.5,
         "garage", 15.45]

# Delete the poolhouse items from the list
del areas[10]
del areas[10]

# Print the updated list
print(areas)
```

`@sct`
```{python}
Ex().check_or(
  multi(
    has_code("del areas[10]", pattern=False),
    has_code("del areas[10]", pattern=False)
  ),
  has_code("del areas[-4:-2]", pattern=False),
  has_code("del(areas[-4:-2])", pattern=False),
  multi(
    has_code("del(areas[10])", pattern=False),
    has_code("del(areas[10])", pattern=False)
  ),
  has_code("del areas[10:12]", pattern=False),
  has_code("del(areas[10:12])", pattern=False),
  multi(
    has_code("del areas[-4]", pattern=False),
    has_code("del areas[-3]", pattern=False)
  ),
  multi(
    has_code("del(areas[-4])", pattern=False),
    has_code("del(areas[-3])", pattern=False)
  )
)

Ex().has_printout(0, not_printed_msg="Avez-vous affiché `areas` après avoir supprimé la chaîne et le flottant de poolhouse ?")
success_msg("Correct ! Vous apprendrez plus tard des moyens plus faciles de supprimer des éléments spécifiques des listes Python.")
```

---

## Fonctionnement interne des listes

```yaml
type: NormalExercise
key: af72db9915
lang: python
xp: 100
skills:
  - 2
```

Du code vous est fourni pour cet exercice : une liste nommée `areas` et une copie appelée `areas_copy`.

À l'heure actuelle, on modifie le premier élément de la liste `areas_copy`, puis on affiche la liste `areas`. Si vous cliquez sur le bouton Exécuter le code, vous verrez que même si vous avez modifié `areas_copy`, le changement s'applique aussi à la liste `areas`. C'est parce que `areas` et `areas_copy` pointent vers la même liste.

Si vous voulez éviter que des changements dans `areas_copy` aient aussi un effet dans `areas`, vous devez faire une copie explicite de la liste `areas` avec `list()` ou en utilisant `[:]`.

`@instructions`
- Modifiez la deuxième commande, qui crée la variable `areas_copy`, pour que `areas_copy` soit une copie explicite de `areas`. Après votre modification, les changements apportés à `areas_copy` ne devraient pas affecter `areas`. Soumettez la réponse pour vérifier.

`@hint`
- Modifiez l'appel `areas_copy = areas`. Au lieu d'assigner `areas`, vous pouvez assigner `list(areas)` ou `areas[:]`.

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
  check_object("areas_copy").has_equal_value(incorrect_msg = "Il semble que `areas_copy` n'a pas été mis à jour correctement."),
  check_function("list", missing_msg = "Assurez-vous d'utiliser `list(areas)` pour créer un `areas_copy`.")
)

mmsg = "Ne supprimez pas la liste prédéfinie `areas`."
imsg = "Assurez-vous de modifier UNIQUEMENT la copie, pas la liste originale `areas`. Consultez à nouveau la description de l'exercice si vous n'êtes pas sûr de savoir comment créer une copie."
Ex().check_correct(
  check_object("areas", missing_msg = mmsg).has_equal_value(incorrect_msg = imsg),
  check_function("list", missing_msg = "Assurez-vous d'utiliser `list(areas)` pour créer un `areas_copy`.")
)

success_msg("Bien joué ! La différence entre les copies explicites et basées sur des références est subtile, mais peut être vraiment importante. Essayez de garder à l'esprit comment une liste est stockée dans la mémoire de l'ordinateur.")
```

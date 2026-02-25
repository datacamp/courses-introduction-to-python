---
title_meta: Chapitre 2
title: Listes Python
description: "Apprenez à stocker, consulter et manipuler des données dans des listes\_: la première étape pour travailler efficacement avec d'énormes quantités de données."
attachments:
  slides_link: 'https://projector-video-pdf-converter.datacamp.com/735/chapter2.pdf'
lessons:
  - nb_of_exercises: 4
    title: Listes Python
  - nb_of_exercises: 4
    title: Listes de sous-ensembles
  - nb_of_exercises: 5
    title: Manipulation de listes
---

## Listes Python

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

Une liste est un **type de données composé** ; vous pouvez regrouper des valeurs, comme ceci :

```
a = "is"
b = "nice"
my_list = ["my", "list", a, b]
```

Après avoir mesuré la taille des membres de votre famille, vous décidez de recueillir des informations sur la maison dans laquelle vous vivez. Les surfaces des différentes parties de votre maison sont stockées dans des variables distinctes dans l'exercice.

`@instructions`
- Créez une liste, `areas`, qui contient la zone du couloir (`hall`), de la cuisine (`kit`), du salon (`liv`), de la chambre (`bed`) et de la salle de bain (`bath`), dans cet ordre. Utilisez les variables prédéfinies.
- Affichez `areas` avec la fonction `print()`.

`@hint`
- Vous pouvez utiliser les variables déjà créées pour construire la liste : `areas = [hall, kit, ...]`.
- Veillez à utiliser des crochets `[]` plutôt que des parenthèses `()`.
- Il n'est pas nécessaire d'utiliser des guillemets pour stocker des variables dans une liste.
- Tapez `print(areas)` pour afficher la liste lors de l’envoi.

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

## Créez des listes de différents types

```yaml
type: NormalExercise
key: 1702a8bcdc
lang: python
xp: 100
skills:
  - 2
```

Bien que cela ne soit pas vraiment courant, une liste peut également contenir un mélange de types Python, y compris des chaînes, des flottants et des booléens.

Vous allez maintenant ajouter les noms des chambres à votre liste, afin de pouvoir facilement voir le nom et la taille de la chambre ensemble.

Une partie du code vous a été fournie pour vous aider à démarrer. Attention ! `"bathroom"` est une chaîne, tandis que `bath` est une variable qui représente le flottant `9.50` que vous avez spécifié plus tôt.

`@instructions`
- Terminez le code qui crée la liste `areas`. Construisez la liste de manière à ce qu'elle contienne d'abord le nom de chaque pièce sous forme de chaîne, puis sa superficie. En d'autres termes, ajoutez les chaînes `"hallway"`, `"kitchen"` et `"bedroom"` aux endroits appropriés.
- Affichez à nouveau la variable `areas` ; est-ce que l'affichage est plus informatif cette fois-ci ?

`@hint`
- Les quatre premiers éléments de la liste `areas` sont codés comme `["hallway", hall, "kitchen", kit, ...`.
- Une chaîne devra être mise entre guillemets `""`.

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
areas_msg = "Vous n'avez pas assigné la valeur correcte à `areas`. Consultez à nouveau les instructions. Assurez-vous de placer le nom de la pièce avant la variable contenant la surface à chaque fois. L'ordre est important ici ! Faites attention aux fautes de frappe."

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

En tant qu’expert en science des données, vous serez souvent amené à traiter un grand nombre de données, et il sera judicieux de regrouper certaines d'entre elles.

Au lieu de créer une liste contenant des chaînes et des flottants, représentant les noms et les surfaces des pièces de votre maison, vous pouvez créer une liste de listes.

Rappelez-vous : `"hallway"` est une chaîne, tandis que `hall` est une variable qui représente le flottant `11.25` que vous avez spécifié plus tôt.

`@instructions`
- Terminez la liste des listes de manière à ce qu'elle contienne également les données relatives à la chambre et à la salle de bains. Attention à bien les saisir dans l'ordre !
- Affichez `house` ; cette façon de structurer vos données est-elle plus logique ?

`@hint`
- Ajoutez des _sous-listes_ à la liste `house` en ajoutant `["bedroom", bed]` et `["bathroom", bath]` entre crochets.
- N'oubliez pas d'inclure une virgule `,` après chaque sous-liste.
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

## Listes de sous-ensembles

```yaml
type: VideoExercise
key: c076b5a69c
xp: 50
```

`@projector_key`
fc15ba5cb9485456df8589130b519ea3

---

## Sous-ensemble et conquête

```yaml
type: NormalExercise
key: c3ce582e32
lang: python
xp: 100
skills:
  - 2
```

Effectuer des sous-ensembles de listes Python est très facile. Prenez l'exemple de code ci-dessous, qui crée une liste `x` et y sélectionne « b ». Rappelez-vous qu'il s'agit du deuxième élément, et qu'il a donc l'index 1. Vous pouvez également utiliser l'indexation négative.

```
x = ["a", "b", "c", "d"]
x[1]
x[-3] # same result!
```

Vous vous souvenez de la liste `areas` de tout à l'heure, contenant à la fois des chaînes et des nombres flottants ? Sa définition figure déjà dans le script. Pouvez-vous ajouter le code correct pour effectuer un sous-ensemble Python ?

`@instructions`
- Affichez le deuxième élément de la liste `areas` (il a la valeur `11.25`).
- Créez un sous-ensemble et affichez le dernier élément de `areas`, soit `9.50`. L'utilisation d'un index négatif est judicieuse dans ce cas.
- Sélectionnez le nombre représentant la surface du salon (`20.0`) et affichez-le.

`@hint`
- Utilisez `x[1]` pour sélectionner le deuxième élément d'une liste `x`.
- Utilisez `x[-1]` pour sélectionner le dernier élément d'une liste `x`.
- Veillez à intégrer vos opérations de sous-ensemble dans un appel à `print()`.
- Le nombre représentant la surface du salon est le 6ème élément de la liste, vous aurez donc besoin de `[5]` ici. `area[4]` afficherait la chaîne.

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
Ex().has_printout(2, not_printed_msg = "Jetez un autre coup d'œil à votre code pour imprimer la surface du salon. Elle est à l'index `5`.")
success_msg("Bon travail !")
```

---

## Découper et manipuler

```yaml
type: NormalExercise
key: 7f08642d18
lang: python
xp: 100
skills:
  - 2
```

La sélection de valeurs individuelles dans une liste n'est qu'une partie de l'histoire. Il est également possible de _découper_ votre liste, c'est-à-dire de sélectionner plusieurs éléments dans votre liste. Utilisez la syntaxe suivante :

```
my_list[start:end]
```

L'index `start` sera inclus, tandis que l'index `end` ne le sera _pas_. Cependant, il est également possible de ne pas spécifier ces index. Si vous ne spécifiez pas l'index `start`, Python suppose que vous voulez commencer votre tranche au début de votre liste.

`@instructions`
- Utilisez le découpage pour créer une liste, `downstairs`, qui contient les 6 premiers éléments de `areas`.
- Créez `upstairs`, comme le dernier des éléments `4` de `areas`. Cette fois, simplifiez le découpage en omettant l'index `end`.
- Affichez à la fois `downstairs` et `upstairs` en utilisant `print()`.

`@hint`
- Utilisez les crochets `[0:6]` pour obtenir les six premiers éléments d'une liste.
- Pour obtenir tout sauf les 5 premiers éléments d'une liste, `l`, vous devez utiliser `l[5:]`.
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

Une liste Python peut également contenir d'autres listes.

Pour subdiviser des listes de listes, vous pouvez utiliser la même technique que précédemment : les crochets. Cela donnerait quelque chose comme ceci pour une liste, `house` :

```
house[2][0]
```

`@instructions`
- Créez un sous-ensemble de la liste `house` pour obtenir le flottant `9.5`.

`@hint`
- Procédez étape par étape. Vous voulez d'abord atteindre le dernier élément de la liste, `["bathroom", 9.50]`. Rappelons que l'index du dernier élément est `-1`.
- Ensuite, vous voulez obtenir le deuxième élément de `["bathroom", 9.50]`, qui se trouve à l'index `1`.

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

success_msg("Correctomundo ! Le dernier élément du puzzle de la liste est la manipulation.")
```

---

## Manipulation de listes

```yaml
type: VideoExercise
key: d7fe818b3a
xp: 50
```

`@projector_key`
355ed52d2fb0d67508c6a311b7cbc6d3

---

## Remplacer les éléments de la liste

```yaml
type: NormalExercise
key: 4e1bba1b55
lang: python
xp: 100
skills:
  - 2
```

Pour remplacer des éléments d'une liste, vous devez subdiviser la liste et attribuer de nouvelles valeurs au sous-ensemble. Vous pouvez sélectionner des éléments individuels ou modifier des tranches de liste entières en une seule fois.

Pour cet exercice et les suivants, vous continuerez à travailler sur la liste `areas` qui contient les noms et les surfaces des différentes pièces d'une maison.

`@instructions`
- Mettez à jour la superficie de la salle de bain pour qu'elle soit de `10.50` mètres carrés au lieu de `9.50` en utilisant l'indexation négative.
- Rendez la liste `areas` plus tendance. Remplacez `"living room"` par `"chill zone"`. N'utilisez pas l'indexation négative cette fois-ci.

`@hint`
- Pour mettre à jour la salle de bains, identifiez le sous-ensemble de la salle de bains (c'est le dernier élément de la liste !).
- Remplacez ensuite la valeur par la nouvelle salle de bains en l'affectant à ce sous-ensemble.
- Faites de même pour mettre à jour le nom `"living room"`, qui se trouve à l'index 4.

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
bathroom_msg = 'Vous pouvez utiliser `areas[-1] = 10.50` pour mettre à jour la surface de la salle de bain.'
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

## Prolonger une liste

```yaml
type: NormalExercise
key: ff0fe8d967
lang: python
xp: 100
skills:
  - 2
```

Si vous pouvez modifier les éléments d'une liste, vous souhaitez certainement pouvoir y ajouter des éléments, n'est-ce pas ? Vous pouvez utiliser l'opérateur `+` :

```
x = ["a", "b", "c", "d"]
y = x + ["e", "f"]
```

Vous venez de gagner à la loterie, génial ! Vous décidez de construire un abri de piscine et un garage. Pouvez-vous ajouter l'information à la liste `areas` ?

`@instructions`
- Utilisez l'opérateur `+` pour coller la liste `["poolhouse", 24.5]` à la fin de la liste `areas`. Enregistrez la liste résultante sous `areas_1`.
- Vous pouvez étendre le site `areas_1` en y ajoutant des données sur votre garage. Ajoutez la chaîne `"garage"` et le flottant `15.45`. Nommez la liste résultante `areas_2`.

`@hint`
- Suivez l'exemple de code dans l’énoncé. `x` est `areas` ici, et `["e", "f"]` est `["poolhouse", 24.5]`.
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
success_msg("Super ! La liste prend une belle forme !")
```

---

## Supprimer des éléments de la liste

```yaml
type: NormalExercise
key: 85f792356e
xp: 100
```

Enfin, vous pouvez également supprimer des éléments de votre liste. Vous pouvez le faire à l'aide de la déclaration `del` :

```
x = ["a", "b", "c", "d"]
del x[1]
```

Attention : dès que vous supprimez un élément d'une liste, les index des éléments qui suivent l'élément supprimé changent tous !

Malheureusement, le montant que vous avez gagné à la loterie n'est pas si élevé et il semble que vous ne pourrez pas construire l’abri de piscine. Vous devrez le supprimer de la liste. Vous décidez de supprimer la chaîne et le nombre flottant correspondants de la liste `areas`.

`@instructions`
- Supprimez de votre liste `areas` la chaîne et le flottant correspondants à `"poolhouse"`.
- Affichez la liste mise à jour de `areas`.

`@hint`
- Vous devrez utiliser `del` deux fois pour supprimer deux éléments. Attention toutefois aux changements d'index !

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
success_msg("Correct ! Vous apprendrez plus tard des moyens plus simples de supprimer des éléments spécifiques des listes Python.")
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

Du code vous a été fourni pour cet exercice : une liste portant le nom `areas` et une copie nommée `areas_copy`.

Actuellement, le premier élément de la liste `areas_copy` est modifié et la liste `areas` est affichée. Si vous appuyez sur le bouton d'exécution du code, vous constaterez que, bien que vous ayez modifié `areas_copy`, la modification est également prise en compte dans la liste `areas`. En effet, `areas` et `areas_copy` renvoient à la même liste.

Si vous souhaitez éviter que les modifications apportées à `areas_copy` ne s’appliquent également à `areas`, vous devrez effectuer une copie plus explicite de la liste `areas` à l'aide de `list()` ou de `[:]`.

`@instructions`
- Modifiez la deuxième commande, qui crée la variable `areas_copy`, de telle sorte que `areas_copy` soit une copie explicite de `areas`. Après votre modification, les changements apportés à `areas_copy` ne devraient pas affecter `areas`. Envoyez la réponse pour le vérifier.

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
  check_object("areas_copy").has_equal_value(incorrect_msg = "Il semble que `areas_copy` n'ait pas été mis à jour correctement."),
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

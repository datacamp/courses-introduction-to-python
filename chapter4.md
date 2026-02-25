---
title_meta: Chapitre 4
title: NumPy
description: >-
  NumPy est un paquet Python fondamental pour pratiquer efficacement la science
  des données. Apprenez à travailler avec les puissants outils du tableau NumPy
  et commencez à explorer des données.
attachments:
  slides_link: 'https://projector-video-pdf-converter.datacamp.com/735/chapter4.pdf'
lessons:
  - nb_of_exercises: 5
    title: NumPy
  - nb_of_exercises: 5
    title: Tableaux NumPy 2D
  - nb_of_exercises: 3
    title: "NumPy\_: Statistiques de base"
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

## Votre premier tableau NumPy

```yaml
type: NormalExercise
key: 84cab9d170
lang: python
xp: 100
skills:
  - 2
```

Vous allez maintenant plonger dans le monde du baseball. En cours de route, vous vous familiariserez avec les bases de `numpy`, un logiciel puissant pour la science des données.

Une liste `baseball` a déjà été définie dans le script Python, représentant la taille de certains joueurs de baseball en centimètres. Pouvez-vous ajouter du code pour créer un tableau `numpy` à partir de celui-ci ?

`@instructions`
- Importez le paquet `numpy` en tant que `np`, afin de pouvoir faire référence à `numpy` avec `np`.
- Utilisez `np.array()` pour créer un tableau `numpy` à partir de `baseball`. Nommez ce tableau `np_baseball`.
- Affichez le type de `np_baseball` pour vérifier que vous avez fait le bon choix.

`@hint`
- `import numpy as np` fera l'affaire. Désormais, vous devez utiliser `np.fun_name()` chaque fois que vous souhaitez utiliser une fonction `numpy`.
- `np.array()` devrait prendre en charge l'entrée `baseball`. Affectez le résultat de l'appel de la fonction à `np_baseball`.
- Pour afficher le type d'une variable `x`, tapez simplement `print(type(x))`.

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
predef_msg = "Vous n'avez pas besoin de changer ou de supprimer les variables prédéfinies."
Ex().has_import("numpy")
Ex().check_correct(
  check_object("np_baseball"),
  multi(
    check_object("baseball", missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
    check_function("numpy.array").check_args(0).has_equal_ast()
  )
)

Ex().has_printout(0)
success_msg("Bon travail !")
```

---

## Taille des joueurs de baseball

```yaml
type: NormalExercise
key: e7e25a89ea
lang: python
xp: 100
skills:
  - 2
```

Vous êtes un grand fan de baseball. Vous décidez de contacter la Ligue majeure de baseball (MLB) et de vous renseigner sur la taille des principaux joueurs. Ils transmettent des données sur plus d'un millier de joueurs, qui sont stockées sous la forme d'une liste Python ordinaire : `height_in`. La hauteur est exprimée en pouces. Pouvez-vous en faire un tableau `numpy` et convertir les unités en mètres ?

`height_in` est déjà disponible et le paquet `numpy` est chargé, vous pouvez donc commencer immédiatement (source : stat.ucla.edu).

`@instructions`
- Créez un tableau `numpy` à partir de `height_in`. Nommez ce nouveau tableau `np_height_in`.
- Affichez `np_height_in`.
- Multipliez `np_height_in` par `0.0254` pour convertir toutes les mesures de hauteur de pouces en mètres. Stockez les nouvelles valeurs dans un nouveau tableau, `np_height_m`.
- Affichez `np_height_m` et vérifiez si le résultat a un sens.

`@hint`
- Utilisez `np.array()` et transmettez-lui `height`. Enregistrez le résultat dans `np_height_in`.
- Pour afficher une variable `x`, tapez `print(x)` dans le script Python.
- Effectuez les calculs comme si `np_height_in` était un seul nombre : `np_height_in * conversion_factor` fait partie de la réponse.
- Pour afficher une variable `x`, tapez `print(x)` dans le script Python.

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
  check_object("np_height_m").has_equal_value(incorrect_msg = "Utilisez `np_height_in * 0.0254` pour calculer `np_height_m`.")
)

success_msg("Bien joué ! En un clin d'œil, `numpy` effectue des multiplications sur plus de 1000 mesures de hauteur.")
```

---

## Effets secondaires de NumPy

```yaml
type: MultipleChoiceExercise
key: 3662ff6637
lang: python
xp: 50
skills:
  - 2
```

`numpy` est idéal pour faire de l'arithmétique vectorielle. Cependant, si l'on compare ses fonctionnalités à celles des listes Python classiques, certaines différences apparaissent.

Tout d'abord, les tableaux `numpy` ne peuvent pas contenir d'éléments de types différents. Si vous mélangez plusieurs types, tels que des booléens et des entiers, ceux-ci`numpy` sont automatiquement convertis en un type commun. Les booléens tels que`True`et`False`sont traités comme`1`et`0`lorsqu'ils sont combinés avec des nombres, de sorte que le tableau se présente sous forme d'entiers.

Deuxièmement, les opérateurs arithmétiques usuels, tels que `+`, `-`, `*` et `/`, ont une signification différente pour les listes Python ordinaires et les tableaux `numpy`.

Veuillez sélectionner le code qui produit le résultat suivant :

```
np.array([True, 1, 2]) + np.array([3, 4, False])
```

Le paquet `numpy` est déjà importé en tant que `np`. Vous pouvez exécuter chaque option dans le shell IPython pour visualiser le résultat.

`@possible_answers`
- `np.array([True, 1, 2, 3, 4, False])`
- `np.array([4, 3, 0]) + np.array([0, 2, 2])`
- `np.array([1, 1, 2]) + np.array([3, 4, -1])`
- `np.array([0, 1, 2, 3, 4, 5])`

`@hint`
- Copiez les différents morceaux de code et collez-les dans le shell IPython. Appuyez sur la touche **Entrée** pour exécuter le code et voir quel résultat correspond à celui généré par `np.array([True, 1, 2]) + np.array([3, 4, False])`.

`@pre_exercise_code`
```{python}
import numpy as np
```

`@sct`
```{python}
msg1 = msg3 = msg4 = "Incorrect. Essayez les différents morceaux de code et voyez lequel correspond au morceau de code cible."
msg2 = "Bon travail ! `True` est converti en 1, `False` est converti en 0."
Ex().has_chosen(2, [msg1, msg2, msg3, msg4])
```

---

## Créer des sous-ensembles de tableaux NumPy

```yaml
type: NormalExercise
key: fcb2a9007b
lang: python
xp: 100
skills:
  - 2
```

Le sous-ensemble (en utilisant la notation entre crochets sur les listes ou les tableaux) fonctionne exactement de la même manière avec les listes et les tableaux.

Deux listes, `height_in` et `weight_lb`, sont déjà chargées en arrière-plan pour cet exercice. Ces listes contiennent la taille et le poids des joueurs de la Ligue majeure de baseball (MLB) sous forme de listes classiques. Il y a également deux listes de tableaux `numpy`, `np_weight_lb` et `np_height_in`, préparées pour vous.

`@instructions`
- Créez un sous-ensemble `np_weight_lb` en affichant l'élément à l'index 50.
- Affichez un sous-réseau de `np_height_in` qui contient les éléments à l'index 100 jusqu'à l'index 110 **inclus.**

`@hint`
- Veillez à entourer vos opérations de sous-ensemble d'un appel à `print()`.
- Utilisez `[100:111]` pour obtenir les éléments de l'index 100 jusqu'à l'index 110 inclus.

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
msg = "Vous n'avez pas besoin de modifier ou de supprimer les variables prédéfinies."
Ex().multi(
    check_object("np_height_in", missing_msg=msg).has_equal_value(incorrect_msg=msg),
    check_object("np_weight_lb", missing_msg=msg).has_equal_value(incorrect_msg=msg)
)

Ex().has_printout(0)
Ex().has_printout(1)

success_msg("Bien joué ! Il est temps d'apprendre quelque chose de nouveau : les tableaux NumPy 2D !")
```

---

## Tableaux NumPy 2D

```yaml
type: VideoExercise
key: 1241efac7a
xp: 50
```

`@projector_key`
ae3238dcc7feb9adecfee0c395fc8dc8

---

## Votre premier tableau NumPy 2D

```yaml
type: NormalExercise
key: 5cb045bb13
lang: python
xp: 100
skills:
  - 2
```

Avant de travailler sur les données réelles de la Ligue majeure de baseball (MLB), essayons de créer un tableau `numpy` 2D à partir d'une petite liste de listes.

Dans cet exercice, `baseball` est une liste de listes. La liste principale contient 4 éléments. Chacun de ces éléments est une liste contenant la taille et le poids de 4 joueurs de baseball, dans cet ordre. `baseball` est déjà codé pour vous dans le script.

`@instructions`
- Utilisez `np.array()` pour créer un tableau `numpy` 2D à partir de `baseball`. Donnez-lui le nom : `np_baseball`.
- Affichez le type de `np_baseball`.
- Affichez l'attribut `shape` de `np_baseball`. Utilisez `np_baseball.shape`.

`@hint`
- `baseball` est déjà codé pour vous dans le script. Appelez `np.array()` et stockez le tableau `numpy` 2D résultant dans `np_baseball`.
- Utilisez `print()` en combinaison avec `type()` pour la deuxième instruction.
- `np_baseball.shape` vous donnera les dimensions de `np_baseball`. Veillez à l'insérer dans un appel à `print()`.

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
msg = "Vous n'avez pas besoin de changer ou de supprimer les variables prédéfinies."
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

success_msg("Super ! Vous êtes prêt à convertir les données réelles de la MLB en un tableau 2D `numpy` maintenant !")
```

---

## Données de baseball en 2D

```yaml
type: NormalExercise
key: 5df25d0b7b
lang: python
xp: 100
skills:
  - 2
```

Vous vous rendez compte qu'il est plus logique de restructurer toutes ces informations dans un tableau `numpy` 2D.

Vous avez une liste Python de listes. Dans cette liste de listes, chaque sous-liste représente la taille et le poids d'un joueur de baseball. Le nom de cette liste est `baseball` et elle a déjà été chargée pour vous (bien que vous ne puissiez pas la voir).

Stockez les données sous forme de tableau 2D pour débloquer les fonctionnalités supplémentaires de `numpy`.

`@instructions`
- Utilisez `np.array()` pour créer un tableau `numpy` 2D à partir de `baseball`. Donnez-lui le nom : `np_baseball`.
- Affichez l'attribut `shape` de `np_baseball`.

`@hint`
- `baseball` est déjà disponible dans l'environnement Python. Appelez `np.array()` et stockez le tableau `numpy` 2D résultant dans `np_baseball`.
- `np_baseball.shape` vous donnera les dimensions de `np_baseball`. Veillez à l'entourer d'un appel à `print()`.

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

success_msg("Impressionnant ! Il est temps de montrer quelques fonctionnalités impressionnantes des tableaux `numpy` multidimensionnels !")
```

---

## Créer des sous-ensembles de tableaux NumPy 2D

```yaml
type: NormalExercise
key: aeca4977f0
lang: python
xp: 100
skills:
  - 2
```

Si votre tableau `numpy` 2D a une structure régulière, c'est-à-dire que chaque ligne et chaque colonne a un nombre fixe de valeurs, il devient très facile de créer des sous-ensembles complexes. Regardez le code ci-dessous où les éléments `"a"` et `"c"` sont extraits d'une liste de listes.

```
# numpy
import numpy as np
np_x = np.array(x)
np_x[:, 0]
```

Les index avant la virgule se réfèrent aux lignes, tandis que les index après la virgule se réfèrent aux colonnes. L’opérateur `:` sert à découper ; dans cet exemple, il indique à Python d'inclure toutes les lignes.

`@instructions`
- Affichez la 50e ligne de `np_baseball`.
- Créez une nouvelle variable, `np_weight_lb`, contenant toute la deuxième colonne de `np_baseball`.
- Sélectionnez la taille (première colonne) du 124e joueur de baseball sur `np_baseball` et affichez-la.

`@hint`
- Vous avez besoin de l'index de ligne 49 dans la première instruction. Plus précisément, vous devez utiliser `[49, :]`.
- Pour sélectionner toute la deuxième colonne, vous aurez besoin de `[:, 1]`.
- Pour la dernière instruction, utilisez `[123, 0]` ; n'oubliez pas d'inclure l’ensemble dans une déclaration `print()`.

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
msg = "Vous n'avez pas à changer ou supprimer les variables prédéfinies."
Ex().multi(
    has_import("numpy", same_as = False),
    check_object("np_baseball", missing_msg=msg).has_equal_value(incorrect_msg = msg)
)

Ex().has_printout(0)

Ex().check_object('np_weight_lb').has_equal_value(incorrect_msg = "Vous pouvez utiliser `np_baseball[:,1]` pour définir `np_weight_lb`. Cela sélectionnera toute la première colonne.")

Ex().has_printout(1)

success_msg("Cela se passe bien !")
```

---

## Arithmétique 2D

```yaml
type: NormalExercise
key: 1c2378b677
lang: python
xp: 100
skills:
  - 2
```

Les tableaux `numpy` 2D peuvent effectuer des calculs élément par élément, comme les tableaux `numpy`.

`np_baseball` est codé pour vous ; il s'agit à nouveau d'un tableau `numpy` 2D avec 3 colonnes représentant la taille (en pouces), le poids (en livres) et l'âge (en années). `baseball` est disponible sous forme de liste normale de listes et `updated` est disponible sous forme de tableau 2D numpy.

`@instructions`
- Vous avez réussi à mettre la main sur les changements de taille, de poids et d'âge de tous les joueurs de base-ball. Il est disponible sous la forme d'un tableau 2D `numpy`, `updated`. Additionnez `np_baseball` et `updated` et affichez le résultat.
- Vous souhaitez convertir les unités de taille et de poids en unités métriques (mètres et kilogrammes, respectivement). Dans un premier temps, créez un tableau `numpy` avec trois valeurs : `0.0254`, `0.453592` et `1`. Nommez ce tableau `conversion`.
- Multipliez `np_baseball` par `conversion` et affichez le résultat.

`@hint`
- `np_baseball + updated` effectuera une addition élément par élément des deux tableaux `numpy`.
- Créez un tableau `numpy` avec `np.array()` ; l'entrée est une liste Python normale avec trois éléments.
- `np_baseball * conversion` fonctionnera, sans travail supplémentaire. Essayez-le ! Veillez à l'inclure dans un appel à `print()`.

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

msg = "Vous n'avez pas besoin de changer ou de supprimer les variables prédéfinies."
Ex().check_object("np_baseball", missing_msg=msg).has_equal_value(incorrect_msg=msg)

Ex().has_printout(0)

Ex().check_correct(
    has_printout(1),
    check_correct(
        check_object('conversion').has_equal_value(),
        check_function('numpy.array', index=1).check_args(0).has_equal_value()
    )    
)

success_msg("Bon travail ! Remarquez comment avec très peu de code, vous pouvez changer toutes les valeurs dans votre structure de données `numpy` de manière très spécifique. Cela vous sera très utile dans votre avenir en tant que data scientist !")
```

---

## NumPy : Statistiques de base

```yaml
type: VideoExercise
key: 287995e488
xp: 50
```

`@projector_key`
34495ba457d74296794d2a122c9b6e19

---

## Moyenne par rapport à la médiane

```yaml
type: NormalExercise
key: 509c588eb6
lang: python
xp: 100
skills:
  - 2
```

Vous savez maintenant comment utiliser les fonctions de `numpy` pour avoir une meilleure idée de vos données. 

Les données relatives au baseball sont disponibles sous la forme d'un tableau `numpy` 2D comportant 3 colonnes (taille, poids, âge) et 1015 lignes. Le nom de ce tableau `numpy` est `np_baseball`. Cependant, après avoir restructuré les données, vous remarquez que certaines valeurs de hauteur sont anormalement élevées. Suivez les instructions et découvrez quelle statistique récapitulative est la mieux adaptée si vous avez affaire à des _valeurs aberrantes_. `np_baseball` est disponible.

`@instructions`
- Créez le tableau `numpy` `np_height_in` qui est égal à la première colonne de `np_baseball`.
- Affichez la moyenne de `np_height_in`.
- Affichez la médiane de `np_height_in`.

`@hint`
- Utiliser le sous-ensemble `numpy` 2D : `[:,0]` fait partie de la solution.
- Si `numpy` est importé en tant que `np`, vous pouvez utiliser `np.mean()` pour obtenir la moyenne d'un tableau NumPy. N'oubliez pas d'ajouter un appel à `print()`.
- Pour la dernière instruction, utilisez `np.median()`.

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

Ex().check_object("np_height_in").has_equal_value(incorrect_msg = "Vous pouvez utiliser `np_baseball[:,0]` pour sélectionner la première colonne de `np_baseball`"),

Ex().check_correct(
    has_printout(0),
    check_function('numpy.mean').has_equal_value()
)

Ex().check_correct(
    has_printout(1),
    check_function('numpy.median').has_equal_value()
)

success_msg("Une hauteur moyenne de 1586 pouces, cela ne semble pas correct, n'est-ce pas ? Cependant, la médiane ne semble pas affectée par les valeurs aberrantes : 74 pouces ont parfaitement du sens. Il est toujours judicieux de vérifier à la fois la médiane et la moyenne, pour avoir une idée de la distribution globale de l'ensemble des données.")
```

---

## Explorez les données sur le baseball

```yaml
type: NormalExercise
key: '4409948807'
lang: python
xp: 100
skills:
  - 2
```

Étant donné que la moyenne et la médiane sont très éloignées l'une de l'autre, vous décidez de vous adresser à la Ligue majeure de baseball (MLB). Ils trouvent l'erreur et vous envoient les données corrigées. Il est à nouveau disponible sous la forme d'un tableau NumPy 2D `np_baseball`, avec trois colonnes.

Le script Python dans l'éditeur comprend déjà du code pour afficher des messages informatifs avec les différentes statistiques sommaires et `numpy` est déjà chargé en tant que `np`. Pouvez-vous terminer le travail ? `np_baseball` est disponible.

`@instructions`
- Le code permettant d'afficher la hauteur moyenne est déjà inclus. Complétez le code pour la hauteur médiane.
- Utilisez `np.std()` sur la première colonne de `np_baseball` pour calculer `stddev`. 
- Les grands joueurs ont-ils tendance à être plus lourds ? Utilisez `np.corrcoef()` pour stocker la corrélation entre la première et la deuxième colonne de `np_baseball` dans `corr`.

`@hint`
- Utilisez `np.median()` pour calculer la médiane. Attention à sélectionner d'abord la bonne colonne.
- Sous-ensemble de la même colonne pour le calcul de l'écart-type avec `np.std()`.
- Utilisez `np_baseball[:, 0]` et `np_baseball[:, 1]` pour sélectionner la première et la deuxième colonne ; ce sont les entrées de `np.corrcoef()`.

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
msg = "Vous ne devriez pas changer ou supprimer la variable prédéfinie `avg`."
Ex().check_object("avg", missing_msg=msg).has_equal_value(incorrect_msg=msg)

missing = "Avez-vous utilisé `np.median()` pour calculer la médiane ?"
incorrect = "Pour calculer `med`, passez la première colonne de `np_baseball` à `numpy.median()`. L'exemple de `np.mean()` montre comment cela se fait."
Ex().check_correct(
  check_object("med").has_equal_value(),
  check_function("numpy.median", index=0, missing_msg=missing).check_args(0).has_equal_value(incorrect_msg=incorrect)
)

missing = "Avez-vous utilisé `np.std()` pour calculer l'écart type ?"
incorrect = "Pour calculer `stddev`, passez la première colonne de `np_baseball` à `numpy.std()`. L'exemple de `np.mean()` montre comment cela se fait."
Ex().check_correct(
  check_object("stddev").has_equal_value(),
  check_function("numpy.std", index=0, missing_msg=missing).check_args(0).has_equal_value(incorrect_msg=incorrect)
)

missing = "Avez-vous utilisé `np.corrcoef()` pour calculer la corrélation ?"
incorrect1 = "Pour calculer `corr`, le premier argument de `np.corrcoef()` doit être la première colonne de `np_baseball`, comme nous l'avons fait auparavant."
incorrect2 = "Pour calculer `corr`, le second argument de `np.corrcoef()` doit être la deuxième colonne de `np_baseball`. Au lieu de `[:,0]`, utilisez `[:,1]` cette fois."
Ex().check_correct(
  check_object("corr").has_equal_value(),
  check_function("numpy.corrcoef", index=0, missing_msg=missing).multi(
    check_args(0, missing_msg=incorrect1).has_equal_value(incorrect_msg=incorrect1),
    check_args(1, missing_msg=incorrect2).has_equal_value(incorrect_msg=incorrect2)
  )
)

success_msg("Excellent travail ! Vous avez construit une base solide - il est maintenant temps d'utiliser toutes vos nouvelles compétences en science des données pour résoudre plus de défis et avoir un impact.")
```

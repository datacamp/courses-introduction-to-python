---
title_meta: Chapitre 4
title: NumPy
description: >-
  NumPy est un progiciel Python fondamental pour pratiquer efficacement la
  science des données. Apprenez à travailler avec des outils puissants dans le
  tableau NumPy et amorcez l'exploration de données.
attachments:
  slides_link: 'https://projector-video-pdf-converter.datacamp.com/735/chapter4.pdf'
lessons:
  - nb_of_exercises: 5
    title: NumPy
  - nb_of_exercises: 5
    title: Tableaux NumPy 2D
  - nb_of_exercises: 3
    title: "NumPy\_: statistiques de base"
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

Vous allez maintenant plonger dans le monde du baseball. Au passage, vous vous familiariserez avec les bases de `numpy`, un puissant module pour faire de la science des données.

Une liste `baseball` a déjà été définie dans le script Python; elle représente la taille de certains joueurs de baseball en centimètres. Pouvez-vous ajouter du code pour créer un tableau `numpy` à partir de celle‑ci?

`@instructions`
- Importez le module `numpy` sous le nom `np`, afin de pouvoir référer à `numpy` avec `np`.
- Utilisez `np.array()` pour créer un tableau `numpy` à partir de `baseball`. Nommez ce tableau `np_baseball`.
- Affichez le type de `np_baseball` pour vérifier que tout est correct.

`@hint`
- `import numpy as np` fera l'affaire. Vous devrez ensuite utiliser `np.fun_name()` chaque fois que vous voulez appeler une fonction de `numpy`.
- `np.array()` doit recevoir `baseball` en entrée. Assignez le résultat de cet appel de fonction à `np_baseball`.
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
predef_msg = "Vous n'avez pas à modifier ou supprimer les variables prédéfinies."
Ex().has_import("numpy")
Ex().check_correct(
  check_object("np_baseball"),
  multi(
    check_object("baseball", missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
    check_function("numpy.array").check_args(0).has_equal_ast()
  )
)

Ex().has_printout(0)
success_msg("Bon travail!")
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

Vous êtes un grand amateur de baseball. Vous décidez d'appeler la MLB (Major League Baseball) pour obtenir plus de statistiques sur la taille des joueurs principaux. On vous transmet des données sur plus d'un millier de joueurs, stockées dans une liste Python ordinaire : `height_in`. Les tailles sont en pouces. Pouvez-vous créer un tableau `numpy` à partir de ces données et convertir les unités en mètres?

`height_in` est déjà disponible et le paquet `numpy` est chargé, donc vous pouvez commencer tout de suite (Source : stat.ucla.edu).

`@instructions`
- Créez un tableau `numpy` à partir de `height_in`. Nommez ce nouveau tableau `np_height_in`.
- Affichez `np_height_in`.
- Multipliez `np_height_in` par `0.0254` pour convertir toutes les mesures de taille de pouces en mètres. Stockez les nouvelles valeurs dans un nouveau tableau, `np_height_m`.
- Affichez `np_height_m` et vérifiez si le résultat est logique.

`@hint`
- Utilisez `np.array()` et passez-lui `height`. Stockez le résultat dans `np_height_in`.
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

success_msg("Bien! En un clin d'œil, `numpy` effectue des multiplications sur plus de 1000 mesures de hauteur.")
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

`numpy` est excellent pour effectuer de l'arithmétique vectorielle. Toutefois, si vous comparez ses fonctionnalités à celles des listes Python ordinaires, certains comportements diffèrent.

D'abord, les tableaux `numpy` ne peuvent pas contenir des éléments de types différents. Si vous mélangez des types, comme des booléens et des entiers, `numpy` les convertit automatiquement vers un type commun. Les booléens comme `True` et `False` sont traités comme `1` et `0` lorsqu'ils sont combinés à des nombres, donc le tableau devient une suite d'entiers.

Ensuite, les opérateurs arithmétiques habituels, comme `+`, `-`, `*` et `/`, n'ont pas la même signification pour les listes Python et pour les tableaux `numpy`.

Sélectionnez le code qui produit la sortie suivante :

```
np.array([True, 1, 2]) + np.array([3, 4, False])
```

Le module `numpy` est déjà importé sous le nom `np`. Vous pouvez exécuter chaque option dans l'IPython Shell pour voir le résultat.

`@possible_answers`
- `np.array([True, 1, 2, 3, 4, False])`
- `np.array([4, 3, 0]) + np.array([0, 2, 2])`
- `np.array([1, 1, 2]) + np.array([3, 4, -1])`
- `np.array([0, 1, 2, 3, 4, 5])`

`@hint`
- Copiez les différents extraits de code et collez-les dans l'IPython Shell. Appuyez sur **enter** pour exécuter le code et voir quelle sortie correspond à celle produite par `np.array([True, 1, 2]) + np.array([3, 4, False])`.

`@pre_exercise_code`
```{python}
import numpy as np
```

`@sct`
```{python}
msg1 = msg3 = msg4 = "Incorrect. Essayez les différents morceaux de code et voyez lequel correspond au morceau de code cible."
msg2 = "Bon travail! `True` est converti en 1, `False` est converti en 0."
Ex().has_chosen(2, [msg1, msg2, msg3, msg4])
```

---

## Sous-ensembles de tableaux NumPy

```yaml
type: NormalExercise
key: fcb2a9007b
lang: python
xp: 100
skills:
  - 2
```

Le sous-ensemblage (l'utilisation des crochets sur des listes ou des tableaux) fonctionne exactement de la même façon avec les listes et les tableaux.

Dans cet exercice, deux listes, `height_in` et `weight_lb`, sont déjà chargées en arrière-plan pour vous. Elles contiennent la taille et le poids des joueurs de la MLB sous forme de listes ordinaires. Deux tableaux `numpy`, `np_weight_lb` et `np_height_in`, sont aussi prêts pour vous.

`@instructions`
- Créez un sous-ensemble de `np_weight_lb` en affichant l'élément à l'indice 50.
- Affichez un sous-tableau de `np_height_in` qui contient les éléments de l'indice 100 jusqu'à **et y compris** l'indice 110.

`@hint`
- Assurez-vous d'entourer vos opérations de sous-ensemble avec un appel à `print()`.
- Utilisez `[100:111]` pour obtenir les éléments de l'indice 100 jusqu'à l'indice 110 inclusivement.

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
msg = "Vous n'avez pas besoin de changer ou de supprimer les variables prédéfinies."
Ex().multi(
    check_object("np_height_in", missing_msg=msg).has_equal_value(incorrect_msg = msg),
    check_object("np_weight_lb", missing_msg=msg).has_equal_value(incorrect_msg = msg)
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

Avant de travailler avec les véritables données de la MLB, créons un tableau `numpy` 2D à partir d'une petite liste de listes.

Dans cet exercice, `baseball` est une liste de listes. La liste principale contient 4 éléments. Chacun de ces éléments est une liste contenant, dans cet ordre, la taille et le poids de 4 joueurs de baseball. `baseball` est déjà défini pour vous dans le script.

`@instructions`
- Utilisez `np.array()` pour créer un tableau `numpy` 2D à partir de `baseball`. Nommez-le `np_baseball`.
- Affichez le type de `np_baseball`.
- Affichez l'attribut `shape` de `np_baseball`. Utilisez `np_baseball.shape`.

`@hint`
- `baseball` est déjà défini pour vous dans le script. Appelez `np.array()` dessus et stockez le tableau `numpy` 2D obtenu dans `np_baseball`.
- Utilisez `print()` avec `type()` pour la deuxième instruction.
- `np_baseball.shape` vous donnera les dimensions de `np_baseball`. Assurez-vous d'entourer cela d'un appel à `print()`.

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
Ex().check_object("baseball", missing_msg=msg).has_equal_value(incorrect_msg = msg)
Ex().has_import("numpy", same_as = False)

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

Vous réalisez qu'il est plus logique de restructurer toute cette information dans un tableau `numpy` 2D.

Vous avez une liste de listes en Python. Dans cette liste de listes, chaque sous-liste représente la taille et le poids d'un joueur de baseball. Le nom de cette liste est `baseball` et elle a déjà été chargée pour vous (même si vous ne la voyez pas).

Enregistrez les données sous forme de tableau 2D pour profiter des fonctionnalités supplémentaires de `numpy`.

`@instructions`
- Utilisez `np.array()` pour créer un tableau `numpy` 2D à partir de `baseball`. Nommez-le `np_baseball`.
- Affichez l'attribut `shape` de `np_baseball`.

`@hint`
- `baseball` est déjà disponible dans l'environnement Python. Appelez `np.array()` dessus et stockez le tableau `numpy` 2D obtenu dans `np_baseball`.
- `np_baseball.shape` vous donnera les dimensions de `np_baseball`. Assurez-vous d'entourer cet appel d'un `print()`.

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

success_msg("Impressionnant ! Il est temps de montrer quelques fonctionnalités impressionnantes des tableaux multi-dimensionnels de `numpy` !")
```

---

## Sous-ensembles dans des tableaux NumPy 2D

```yaml
type: NormalExercise
key: aeca4977f0
lang: python
xp: 100
skills:
  - 2
```

Si votre tableau `numpy` 2D a une structure régulière, c'est-à-dire que chaque rangée et chaque colonne contient un nombre fixe de valeurs, créer des sous-ensembles complexes devient très simple. Regardez le code ci-dessous où les éléments `"a"` et `"c"` sont extraits d'une liste de listes.

```
# numpy
import numpy as np
np_x = np.array(x)
np_x[:, 0]
```

Les index avant la virgule renvoient aux rangées, tandis que ceux après la virgule renvoient aux colonnes. Le `:` sert au découpage (slicing); dans cet exemple, il indique à Python d'inclure toutes les rangées.

`@instructions`
- Affichez la 50e rangée de `np_baseball`.
- Créez une nouvelle variable, `np_weight_lb`, qui contient toute la deuxième colonne de `np_baseball`.
- Sélectionnez la taille (première colonne) du 124e joueur de baseball dans `np_baseball` et affichez-la.

`@hint`
- Vous avez besoin de la rangée d'index 49 dans la première consigne ! Plus précisément, vous voudrez utiliser `[49, :]`.
- Pour sélectionner toute la deuxième colonne, utilisez `[:, 1]`.
- Pour la dernière consigne, utilisez `[123, 0]`; n'oubliez pas d'englober le tout dans un appel à `print()`.

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
msg = "Vous n'avez pas besoin de changer ou de supprimer les variables prédéfinies."
Ex().multi(
    has_import("numpy", same_as = False),
    check_object("np_baseball", missing_msg=msg).has_equal_value(incorrect_msg = msg)
)

Ex().has_printout(0)

Ex().check_object('np_weight_lb').has_equal_value(incorrect_msg = "Vous pouvez utiliser `np_baseball[:,1]` pour définir `np_weight_lb`. Cela sélectionnera la première colonne entière.")

Ex().has_printout(1)

success_msg("Tout se passe bien !")
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

Les tableaux `numpy` 2D peuvent effectuer des calculs élément par élément, tout comme les tableaux `numpy`.

`np_baseball` est déjà défini pour vous; c'est encore un tableau `numpy` 2D avec 3 colonnes représentant la taille (en pouces), le poids (en livres) et l'âge (en années). `baseball` est disponible comme liste de listes ordinaire et `updated` est disponible comme tableau `numpy` 2D.

`@instructions`
- Vous avez réussi à obtenir les changements de taille, de poids et d'âge de tous les joueurs de baseball. Ils sont disponibles dans un tableau `numpy` 2D, `updated`. Additionnez `np_baseball` et `updated`, puis affichez le résultat.
- Vous souhaitez convertir les unités de taille et de poids au système métrique (mètres et kilogrammes, respectivement). Comme première étape, créez un tableau `numpy` avec trois valeurs : `0.0254`, `0.453592` et `1`. Nommez ce tableau `conversion`.
- Multipliez `np_baseball` par `conversion` et affichez le résultat.

`@hint`
- `np_baseball + updated` fera une addition élément par élément des deux tableaux `numpy`.
- Créez un tableau `numpy` avec `np.array()`; l'entrée est une liste Python ordinaire de trois éléments.
- `np_baseball * conversion` fonctionnera tel quel. Essayez-le! N'oubliez pas de l'entourer d'un appel à `print()`.

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
Ex().check_object("np_baseball", missing_msg=msg).has_equal_value(incorrect_msg = msg)

Ex().has_printout(0)

Ex().check_correct(
    has_printout(1),
    check_correct(
        check_object('conversion').has_equal_value(),
        check_function('numpy.array', index = 1).check_args(0).has_equal_value()
    )    
)

success_msg("Bon travail! Remarquez comment avec très peu de code, vous pouvez changer toutes les valeurs dans votre structure de données `numpy` de manière très spécifique. Cela vous sera très utile dans votre avenir en tant que data scientist!")
```

---

## NumPy : statistiques de base

```yaml
type: VideoExercise
key: 287995e488
xp: 50
```

`@projector_key`
34495ba457d74296794d2a122c9b6e19

---

## Moyenne ou médiane

```yaml
type: NormalExercise
key: 509c588eb6
lang: python
xp: 100
skills:
  - 2
```

Vous savez maintenant utiliser les fonctions de `numpy` pour mieux comprendre vos données.

Les données de baseball sont offertes sous forme d'un tableau `numpy` 2D avec 3 colonnes (taille, poids, âge) et 1015 lignes. Le nom de ce tableau `numpy` est `np_baseball`. Après avoir restructuré les données, vous remarquez toutefois que certaines valeurs de taille sont anormalement élevées. Suivez les instructions pour découvrir quelle statistique sommaire convient le mieux lorsque vous traitez des valeurs aberrantes (outliers). `np_baseball` est disponible.

`@instructions`
- Créez le tableau `numpy` `np_height_in` qui correspond à la première colonne de `np_baseball`.
- Affichez la moyenne de `np_height_in`.
- Affichez la médiane de `np_height_in`.

`@hint`
- Utilisez le sous-ensemble 2D de `numpy` : `[:,0]` fait partie de la solution.
- Si `numpy` est importé sous le nom `np`, vous pouvez utiliser `np.mean()` pour obtenir la moyenne d'un tableau NumPy. N'oubliez pas d'ajouter un appel à `print()`.
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

## Explorer les données de baseball

```yaml
type: NormalExercise
key: '4409948807'
lang: python
xp: 100
skills:
  - 2
```

Comme la moyenne et la médiane sont très éloignées, vous décidez de porter plainte à la MLB. Ils trouvent l'erreur et vous envoient les données corrigées. Elles sont de nouveau offertes comme un tableau NumPy 2D `np_baseball`, avec trois colonnes.

Le script Python dans l'éditeur inclut déjà du code pour afficher des messages informatifs avec différentes statistiques sommaires, et `numpy` est déjà importé sous le nom `np`. Pouvez-vous terminer le travail? `np_baseball` est disponible.

`@instructions`
- Le code pour afficher la taille moyenne est déjà inclus. Complétez le code pour la taille médiane.
- Utilisez `np.std()` sur la première colonne de `np_baseball` pour calculer `stddev`.
- Les grands joueurs ont-ils tendance à être plus lourds? Utilisez `np.corrcoef()` pour stocker la corrélation entre les première et deuxième colonnes de `np_baseball` dans `corr`.

`@hint`
- Utilisez `np.median()` pour calculer la médiane. Assurez-vous de sélectionner d'abord la bonne colonne!
- Sélectionnez la même colonne lorsque vous calculez l'écart type avec `np.std()`.
- Utilisez `np_baseball[:, 0]` et `np_baseball[:, 1]` pour sélectionner les première et deuxième colonnes; ce sont les paramètres d'entrée de `np.corrcoef()`.

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
incorrect1 = "Pour calculer `corr`, le premier argument de `np.corrcoef()` devrait être la première colonne de `np_baseball`, comme vous l'avez fait auparavant."
incorrect2 = "Pour calculer `corr`, le deuxième argument de `np.corrcoef()` devrait être la deuxième colonne de `np_baseball`. Au lieu de `[:,0]`, utilisez `[:,1]` cette fois."
Ex().check_correct(
  check_object("corr").has_equal_value(),
  check_function("numpy.corrcoef", index=0, missing_msg=missing).multi(
    check_args(0, missing_msg=incorrect1).has_equal_value(incorrect_msg=incorrect1),
    check_args(1, missing_msg=incorrect2).has_equal_value(incorrect_msg=incorrect2)
  )
)

success_msg("Excellent travail ! Vous avez construit une base solide - il est maintenant temps d'utiliser toutes vos nouvelles compétences en science des données pour relever plus de défis et avoir un impact.")
```

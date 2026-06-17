---
title_meta: Chapitre 3
title: Fonctions et progiciels
description: "Vous apprendrez à utiliser des fonctions, des méthodes et des progiciels pour exploiter efficacement le code écrit par d'excellentes et d'excellents développeurs Python. L'objectif est de réduire la quantité de code nécessaire pour résoudre des problèmes complexes\_!"
attachments:
  slides_link: 'https://projector-video-pdf-converter.datacamp.com/735/chapter3.pdf'
lessons:
  - nb_of_exercises: 4
    title: Fonctions
  - nb_of_exercises: 4
    title: Méthodes
  - nb_of_exercises: 4
    title: Progiciels
---

## Fonctions

```yaml
type: VideoExercise
key: 5c5f365930
xp: 50
```

`@projector_key`
1204d914b0e53100529827e07441ee6c

---

## Fonctions familières

```yaml
type: NormalExercise
key: c422ee929b
lang: python
xp: 100
skills:
  - 2
```

D'emblée, Python offre un lot de fonctions intégrées qui vous simplifient la vie comme scientifique des données. Vous en connaissez déjà deux : `print()` et `type()`. Il existe aussi des fonctions comme `str()`, `int()`, `bool()` et `float()` pour passer d'un type de données à un autre. Vous pouvez en apprendre davantage [ici.](https://docs.python.org/3/library/functions.html) Ce sont aussi des fonctions intégrées.

Appeler une fonction, c'est simple. Pour obtenir le type de `3.0` et enregistrer le résultat dans une nouvelle variable, `result`, vous pouvez utiliser ce qui suit :

```
result = type(3.0)
```

`@instructions`
- Utilisez `print()` avec `type()` pour afficher le type de `var1`.
- Utilisez `len()` pour obtenir la [longueur de la liste](https://docs.python.org/3/library/functions.html#len) `var1`. Encapsulez-le dans un appel à `print()` pour l'afficher directement.
- Utilisez `int()` pour convertir `var2` en [entier](https://docs.python.org/3/library/functions.html#int). Enregistrez le résultat sous `out2`.

`@hint`
- Appelez la fonction `type()` ainsi : `type(var1)`.
- Appelez `print()` comme vous l'avez fait tant de fois. Placez simplement la variable à afficher entre parenthèses.
- `int(x)` convertira `x` en entier.

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
msg = "Vous n'avez pas besoin de changer ou de supprimer les variables prédéfinies."
Ex().check_object("var1", missing_msg=msg).has_equal_value(incorrect_msg=msg)
Ex().check_object("var2", missing_msg=msg).has_equal_value(incorrect_msg=msg)

patt = "__JINJA__:Assurez-vous d'imprimer le %s de `var1` avec `{{sol_call}}`."
Ex().has_printout(0, not_printed_msg = patt % 'type')
Ex().has_printout(1, not_printed_msg = patt % 'length')

int_miss_msg = "Avez-vous utilisé `int()` pour créer un entier à partir de `var2`?"
int_incorr_msg = "Avez-vous passé `var2` à `int()`?"
Ex().check_correct(
  check_object("out2").has_equal_value(incorrect_msg="Vous avez appelé `int()` correctement; assurez-vous maintenant d'assigner le résultat de cet appel à `out2`."),
  check_function("int", missing_msg=int_miss_msg).has_equal_value(incorrect_msg=int_incorr_msg)
)
success_msg("Bon travail! La fonction `len()` est extrêmement utile; elle fonctionne également sur les chaînes de caractères pour compter le nombre de caractères!")
```

---

## À l'aide !

```yaml
type: MultipleChoiceExercise
key: 679b852978
lang: python
xp: 50
skills:
  - 2
```

Vous connaissez peut-être déjà le nom d'une fonction Python, mais vous devez encore comprendre comment l'utiliser. Paradoxalement, vous devez demander des infos sur une fonction avec une autre fonction : `help()`. Dans IPython en particulier, vous pouvez aussi utiliser `?` avant le nom de la fonction.

Pour obtenir de l'aide sur la fonction `max()`, par exemple, vous pouvez utiliser l'un des appels suivants :

```
help(max)
?max
```

Servez-vous du Shell IPython pour ouvrir la [documentation](https://docs.python.org/3/library/functions.html#pow) de `pow()`. Pour ce faire, tapez `?pow` ou `help(pow)` puis appuyez sur **Enter**.

Laquelle des affirmations suivantes est vraie ?

`@possible_answers`
- `pow()` accepte trois arguments : `base`, `exp` et `mod`. Sans `mod`, la fonction retournera une erreur.
- `pow()` accepte trois arguments obligatoires : `base`, `exp` et `None`.
- `pow()` exige les arguments `base` et `exp` ; `mod` est facultatif.
- `pow()` accepte deux arguments : `exp` et `mod`. Si `exp` est manquant, cela entraîne une erreur.

`@hint`
- Les arguments optionnels sont associés avec `=` à une valeur par défaut, que la fonction utilisera si cet argument n'est pas précisé.

`@pre_exercise_code`
```{python}

```

`@sct`
```{python}
msg1 = "Pas tout à fait. `mod` a une valeur par défaut qui sera utilisée si vous ne spécifiez pas de valeur."
msg2 = "Incorrect. `None` est la valeur par défaut pour l'argument `mod`."
msg3 = "Parfait ! Utiliser `help()` peut vous aider à comprendre comment fonctionnent les fonctions, libérant ainsi tout leur potentiel !"
msg4 = "Incorrect. `pow()` prend trois arguments, dont l'un a une valeur par défaut."
Ex().has_chosen(3, [msg1, msg2, msg3, msg4])
```

---

## Arguments multiples

```yaml
type: NormalExercise
key: e30486d7c1
lang: python
xp: 100
skills:
  - 2
```

Dans l'exercice précédent, vous avez repéré des arguments optionnels en consultant la documentation avec `help()`. Vous allez maintenant appliquer cela pour modifier le comportement de la fonction `sorted()`.

Consultez la [documentation](https://docs.python.org/3/library/functions.html#sorted) de `sorted()` en tapant `help(sorted)` dans le Shell IPython.

Vous verrez que `sorted()` prend trois arguments : `iterable`, `key` et `reverse`. Dans cet exercice, vous n'aurez qu'à préciser `iterable` et `reverse`, pas `key`.

Deux listes ont été créées pour vous.

Pouvez-vous les combiner et les trier par ordre décroissant ?

`@instructions`
- Utilisez `+` pour fusionner le contenu de `first` et `second` dans une nouvelle liste : `full`.
- Appelez `sorted()` sur `full` et indiquez l'argument `reverse` à `True`. Enregistrez la liste triée dans `full_sorted`.
- Terminez en affichant `full_sorted`.

`@hint`
- Additionnez `first` et `second` comme s'il s'agissait de deux nombres et affectez le résultat à `full`.
- Utilisez `sorted()` avec deux paramètres : `full` et `reverse=True`.
- Pour afficher une variable, utilisez `print()`.

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
msg = "Vous n'avez pas besoin de changer ou de supprimer les variables `first` et `second` déjà présentes."
Ex().multi(
  check_object("first", missing_msg=msg).has_equal_value(incorrect_msg=msg),
  check_object("second", missing_msg=msg).has_equal_value(incorrect_msg=msg)
)
Ex().check_correct(
  check_object("full_sorted").has_equal_value(incorrect_msg="Assurez-vous d'assigner le résultat de l'appel à `sorted()` à `full_sorted`."),
  check_function("sorted").multi(
    check_args(0).has_equal_value(),
    check_args('reverse').has_equal_value()
  )
)

success_msg("Super ! Passez à la vidéo sur les méthodes Python.")
```

---

## Méthodes

```yaml
type: VideoExercise
key: 2b66cb66b1
xp: 50
```

`@projector_key`
8e387776f3a264a745128b68aa8d8f83

---

## Méthodes sur les chaînes de caractères

```yaml
type: NormalExercise
key: 4039302ee0
lang: python
xp: 100
skills:
  - 2
```

Les chaînes de caractères offrent plusieurs méthodes. Suivez attentivement les instructions pour en découvrir quelques-unes. Pour aller plus loin, vous pouvez toujours taper `help(str)` dans le Shell IPython.

Une chaîne `place` a déjà été créée pour que vous puissiez faire des essais.

`@instructions`
- Utilisez la [méthode](https://docs.python.org/3/library/stdtypes.html#str.upper) `.upper()` sur `place` et enregistrez le résultat dans `place_up`. Utilisez la syntaxe d'appel de méthodes vue dans la vidéo précédente.
- Affichez `place` et `place_up`. Est-ce que les deux ont changé?
- Affichez le nombre de « o » dans la variable `place` en appelant `.count()` sur `place` et en passant la lettre `'o'` comme paramètre à la méthode. On parle bien de la variable `place`, pas du mot « "place" » !

`@hint`
- Vous pouvez appeler la méthode `.upper()` sur `place` sans aucun autre paramètre.
- Pour afficher une variable `x`, vous pouvez écrire `print(x)`.
- Assurez-vous d'englober votre appel `place.count(____)` dans une fonction `print()` afin d'en afficher le résultat.

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
msg = "Vous n'avez pas besoin de changer ou de supprimer les variables prédéfinies."
Ex().check_object("place", missing_msg=msg).has_equal_value(incorrect_msg=msg)

patt = "N'oubliez pas d'imprimer `%s`."
Ex().has_printout(0, not_printed_msg=patt % "place")
Ex().check_correct(
    has_printout(1, not_printed_msg=patt % "place_up"),
    check_correct(
        check_object("place_up").has_equal_value(incorrect_msg="Assignez le résultat de votre appel `place.upper()` à `place_up`."),
        check_function("place.upper", signature=False)
    )
)    

# check count of place
Ex().check_correct(
  has_printout(2, not_printed_msg = "Vous avez bien calculé le nombre de o dans `place`; assurez-vous maintenant d'encapsuler l'appel `place.count('o')` dans une fonction `print()` pour imprimer le résultat."),
  check_function("place.count", signature=False).check_args(0).has_equal_value()
)

success_msg("Bien joué ! Remarquez à partir des impressions que la méthode `upper()` ne modifie pas l'objet sur lequel elle est appelée. Ce sera différent pour les listes dans le prochain exercice !")
```

---

## Méthodes de liste

```yaml
type: NormalExercise
key: 0dbe8ed695
lang: python
xp: 100
skills:
  - 2
```

Les chaînes de caractères ne sont pas les seuls types Python dotés de méthodes. Les listes, les nombres à virgule flottante, les entiers et les booléens offrent aussi plusieurs méthodes utiles. Dans cet exercice, vous allez expérimenter :

- `.index()`, pour obtenir l'indice du premier élément d'une liste qui correspond à l'argument fourni, et
- `.count()`, pour obtenir le nombre de fois qu'un élément apparaît dans une liste.

Vous travaillerez avec la liste des superficies de différentes parties d'une maison : `areas`.

`@instructions`
- Utilisez la méthode `.index()` pour obtenir l'indice de l'élément dans `areas` qui est égal à `20.0`. Affichez cet indice.
- Appelez `.count()` sur `areas` pour savoir combien de fois `9.50` apparaît dans la liste. Là encore, affichez simplement ce nombre.

`@hint`
- Pour afficher l'indice, encapsulez l'appel à `areas.index(___)` dans une fonction `print()`.
- Pour afficher le nombre de fois qu'un élément `x` apparaît dans la liste, encapsulez l'appel à `areas.count(___)` dans une fonction `print()`.

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
predef_msg = "Vous n'avez pas à changer ou supprimer la liste prédéfinie `areas`."

Ex().check_object("areas", missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg)

Ex().check_function("print", index=0).check_args(0).check_function('areas.index', signature=False).check_args(0).has_equal_value()


Ex().check_function("print", index=1).check_args(0).check_function('areas.count', signature=False).has_equal_value()

success_msg("Bien joué! Ce sont des exemples de méthodes `list` qui n'ont pas modifié la liste sur laquelle elles ont été appelées.")
```

---

## Méthodes de liste (2)

```yaml
type: NormalExercise
key: 1fbeab82d0
lang: python
xp: 100
skills:
  - 2
```

La plupart des méthodes de liste modifient la liste sur laquelle elles sont appelées. Voici des exemples :

- `.append()`, qui ajoute un élément à la liste sur laquelle elle est appelée,
- `.remove()`, qui [retire](https://docs.python.org/3/library/stdtypes.html#typesseq-mutable) de la liste la première occurrence correspondant à l'entrée, et
- `.reverse()`, qui [inverse](https://docs.python.org/3/library/stdtypes.html#typesseq-mutable) l'ordre des éléments de la liste sur laquelle elle est appelée.

Vous allez travailler avec la liste des superficies des différentes pièces de la maison : `areas`.

`@instructions`
- Utilisez `.append()` deux fois pour ajouter de nouveau la superficie de l'annexe piscine et du garage : `24.5` et `15.45`, respectivement. Assurez-vous de les ajouter dans cet ordre.
- Affichez `areas`.
- Utilisez la méthode `.reverse()` pour inverser l'ordre des éléments de `areas`.
- Affichez de nouveau `areas`.

`@hint`
- Pour la première consigne, utilisez l'appel `areas.append(___)` deux fois.
- Pour afficher une variable `x`, écrivez simplement `print(x)`.
- La méthode `.reverse()` ne nécessite aucun paramètre supplémentaire; utilisez simplement la notation point et des parenthèses vides : `.reverse()`.
- Pour afficher une variable `x`, écrivez simplement `print(x)`.

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

success_msg("Excellent !")
```

---

## Forfaits

```yaml
type: VideoExercise
key: ab96a17c5e
xp: 50
```

`@projector_key`
cedcfb34350be8545599768f96695cdd

---

## Importer un paquet

```yaml
type: NormalExercise
key: 7432a6376f
lang: python
xp: 100
skills:
  - 2
```

Disons que vous voulez calculer la circonférence et l'aire d'un cercle. Voici les formules :

$$C = 2 \pi r$$
$$A = \pi r^2 $$

Plutôt que de taper la valeur de `pi`, vous pouvez utiliser le paquet `math` qui la contient.

Pour référence, `**` est l'opérateur d'exponentiation. Par exemple, `3**4` correspond à `3` à la puissance `4` et donne `81`.

`@instructions`
- Importez le paquet `math`.
- Utilisez `math.pi` pour calculer la circonférence du cercle et stockez-la dans `C`.
- Utilisez `math.pi` pour calculer l'aire du cercle et stockez-la dans `A`.

`@hint`
- Vous pouvez simplement utiliser `import math`, puis faire référence à `pi` avec `math.pi`.
- Utilisez l'équation dans l'énoncé pour calculer `C`. Utilisez `*`.
- Utilisez l'équation dans l'énoncé pour calculer `A`. Utilisez `*` et `**`.

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
patt = "Votre calcul de `%s` n'est pas tout à fait correct. Assurez-vous d'utiliser `math.pi`."
Ex().multi(
  has_import('math', same_as=False),
  check_object('C').has_equal_value(incorrect_msg=patt%'C'),
  check_object('A').has_equal_value(incorrect_msg=patt%'A')
)

Ex().multi(
  has_printout(0, not_printed_msg = "__JINJA__:Gardez `{{sol_call}}` là-dedans pour imprimer la circonférence."),
  has_printout(1, not_printed_msg = "__JINJA__:Gardez `{{sol_call}}` là-dedans pour imprimer la surface.")
)

success_msg("Bien joué ! Si vous savez comment gérer les fonctions des packages, la puissance de nombreux programmeurs Python est à votre portée !")
```

---

## Import sélectif

```yaml
type: NormalExercise
key: fe65eff50a
lang: python
xp: 100
skills:
  - 2
```

Les imports généraux, comme `import math`, rendent **toutes** les fonctionnalités du paquet `math` disponibles. Toutefois, si vous n'avez besoin que d'une partie précise d'un paquet, vous pouvez toujours faire un import plus ciblé :

```
from math import pi
```

Faites la même chose, mais cette fois, utilisez seulement `pi`.

`@instructions`
- Effectuez un import sélectif du paquet `math` pour n'importer que la fonction `pi`.
- Utilisez `pi` pour calculer la circonférence du cercle et stockez-la dans `C`.
- Utilisez `pi` pour calculer l'aire du cercle et stockez-la dans `A`.

`@hint`
- Utilisez `from math import pi` pour faire un import sélectif.
- Vous pouvez maintenant utiliser `pi` directement!

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
patt = "Votre calcul de `%s` n'est pas tout à fait correct. Assurez-vous d'utiliser uniquement `pi`."

Ex().has_import("math.pi", not_imported_msg = "Assurez-vous d'importer `pi` du package `math`. Vous devriez utiliser la notation `from ___ import ___`.",)

Ex().multi(
  check_object('C').has_equal_value(incorrect_msg=patt%'C'),
  check_object('A').has_equal_value(incorrect_msg=patt%'A')
)

Ex().multi(
  has_printout(0, not_printed_msg = "__JINJA__:Gardez `{{sol_call}}` là-dedans pour imprimer la circonférence."),
  has_printout(1, not_printed_msg = "__JINJA__:Gardez `{{sol_call}}` là-dedans pour imprimer la surface.")
)

success_msg("Bien joué ! Passez à l'exercice suivant.")
```

---

## Différentes façons d'importer

```yaml
type: MultipleChoiceExercise
key: f1b2675a2a
lang: python
xp: 50
skills:
  - 2
```

Il existe plusieurs façons d'importer des progiciels et des modules en Python. Selon la commande d'importation, vous devrez écrire du code Python différent.

Supposons que vous vouliez utiliser la [fonction](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.inv.html) `inv()`, qui se trouve dans le sous-paquet `linalg` du paquet `scipy`. Vous souhaitez pouvoir utiliser cette fonction ainsi :

```
my_inv([[1,2], [3,4]])
```

Quelle instruction `import` vous permettra d'exécuter le code ci-dessus sans erreur ?

`@possible_answers`
- `import scipy`
- `import scipy.linalg`
- `from scipy.linalg import my_inv`
- `from scipy.linalg import inv as my_inv`

`@hint`
- Essayez les différentes instructions d'importation dans le shell IPython et voyez laquelle permet d'exécuter la ligne `my_inv([[1, 2], [3, 4]])` sans erreur. Appuyez sur **enter** pour exécuter le code que vous avez saisi.

`@pre_exercise_code`
```{python}

```

`@sct`
```{python}
msg1 = msg2 = msg3 = "Incorrect, essayez à nouveau. Essayez les différentes instructions d'importation dans le shell IPython et voyez laquelle permet à la ligne `my_inv([[1, 2], [3, 4]])` de s'exécuter sans erreurs."
msg4 = "Correct ! Le mot `as` vous permet de créer un nom local pour la fonction que vous importez : `inv()` est maintenant disponible sous le nom `my_inv()`."
Ex().has_chosen(4, [msg1, msg2, msg3, msg4])
```

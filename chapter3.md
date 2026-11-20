---
title_meta: Chapitre 3
title: Fonctions et paquets
description: "Vous apprendrez à utiliser les fonctions, les méthodes et les paquets pour exploiter efficacement le code écrit par de brillants développeurs Python. L'objectif est de réduire la quantité de code dont vous avez besoin pour résoudre des problèmes complexes\_!"
attachments:
  slides_link: 'https://projector-video-pdf-converter.datacamp.com/735/chapter3.pdf'
lessons:
  - nb_of_exercises: 4
    title: Fonctions
  - nb_of_exercises: 4
    title: Méthodes
  - nb_of_exercises: 4
    title: Paquets
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

Python propose d'emblée un grand nombre de fonctions intégrées pour vous faciliter la vie en tant qu’expert en science des données. Vous connaissez déjà deux de ces fonctions : `print()` et `type()`. Il existe également des fonctions telles que `str()`, `int()`, `bool()` et `float()` pour passer d'un type de données à un autre. Vous pouvez les découvrir [ici.](https://docs.python.org/3/library/functions.html) Il s'agit également de fonctions intégrées.

Il est facile d'appeler une fonction. Pour obtenir le type de `3.0` et stocker le résultat dans une nouvelle variable, `result`, vous pouvez utiliser ce qui suit :

```
result = type(3.0)
```

`@instructions`
- Utilisez `print()` en combinaison avec `type()` pour afficher le type de `var1`.
- Utilisez `len()` pour obtenir la [longueur de la liste](https://docs.python.org/3/library/functions.html#len) `var1`. Intégrez-le dans un appel à `print()` pour l'afficher directement.
- Utilisez `int()` pour convertir `var2` en un [nombre entier](https://docs.python.org/3/library/functions.html#int). Enregistrez le résultat sous `out2`.

`@hint`
- Appelez la fonction `type()` comme suit : `type(var1)`.
- Appelez `print()` comme vous l'avez fait tant de fois auparavant. Mettez simplement entre parenthèses la variable que vous souhaitez afficher.
- `int(x)` convertira `x` en un entier.

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

int_miss_msg = "Avez-vous utilisé `int()` pour créer un entier à partir de `var2` ?"
int_incorr_msg = "Avez-vous passé `var2` à `int()` ?"
Ex().check_correct(
  check_object("out2").has_equal_value(incorrect_msg="Vous avez appelé `int()` correctement ; assurez-vous maintenant d'assigner le résultat de cet appel à `out2`."),
  check_function("int", missing_msg=int_miss_msg).has_equal_value(incorrect_msg=int_incorr_msg)
)
success_msg("Bon travail ! La fonction `len()` est extrêmement utile ; elle fonctionne également sur les chaînes de caractères pour compter le nombre de caractères !")
```

---

## À l’aide !

```yaml
type: MultipleChoiceExercise
key: 679b852978
lang: python
xp: 50
skills:
  - 2
```

Vous connaissez peut-être déjà le nom d'une fonction Python, mais vous ne savez pas encore comment l'utiliser. Ironiquement, vous devez demander des informations sur une fonction à l'aide d'une autre fonction : `help()`. Dans IPython en particulier, vous pouvez également utiliser « `?` » avant le nom de la fonction.

Pour obtenir de l'aide sur la fonction `max()`, par exemple, vous pouvez utiliser l'un de ces appels :

```
help(max)
?max
```

Utilisez le shell IPython pour ouvrir la [documentation](https://docs.python.org/3/library/functions.html#pow) sur `pow()`. Pour ce faire, tapez `?pow` ou `help(pow)` et appuyez sur la touche **Entrée.**

Lequel des énoncés suivants est vrai ?

`@possible_answers`
- `pow()` prend trois arguments : `base`, `exp`, et `mod`. Sans `mod`, la fonction renverra une erreur.
- `pow()` prend trois arguments obligatoires : `base`, `exp`, et `None`.
- `pow()` nécessite les arguments `base` et `exp`; `mod` est facultatif.
- `pow()` prend deux arguments : `exp` et `mod`. L'absence de `exp` entraîne une erreur.

`@hint`
- Les arguments facultatifs sont spécifiés `=` à une valeur par défaut, que la fonction utilisera si cet argument n'est pas spécifié.

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

Dans l'exercice précédent, vous avez identifié les arguments optionnels en consultant la documentation avec `help()`. Vous allez maintenant l'appliquer pour modifier le comportement de la fonction `sorted()`.

Consultez la [documentation](https://docs.python.org/3/library/functions.html#sorted) de `sorted()` en saisissant `help(sorted)` dans le shell IPython.

Vous verrez que `sorted()` prend trois arguments : `iterable`, `key`, et `reverse`. Dans cet exercice, vous ne devrez spécifier que `iterable` et `reverse`, et non `key`.

Deux listes ont été créées pour vous.

Pouvez-vous les coller ensemble et les trier par ordre décroissant ?

`@instructions`
- Utilisez `+` pour fusionner le contenu de `first` et `second` dans une nouvelle liste : `full`.
- Appelez `sorted()` sur `full` et spécifiez que l'argument `reverse` est `True`. Enregistrez la liste triée sous `full_sorted`.
- Terminez en affichant `full_sorted`.

`@hint`
- Additionnez `first` et `second` comme s'il s'agissait de deux nombres et affectez le résultat à `full`.
- Utilisez `sorted()` avec deux entrées : `full` et `reverse=True`.
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
msg = "Vous n'avez pas besoin de changer ou de supprimer les variables `first` et `second` déjà existantes."
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

## Méthodes de chaînes

```yaml
type: NormalExercise
key: 4039302ee0
lang: python
xp: 100
skills:
  - 2
```

Les chaînes sont accompagnées d'un certain nombre de méthodes. Suivez attentivement les instructions pour découvrir certaines d'entre elles. Si vous souhaitez les découvrir plus en détail, vous pouvez toujours saisir `help(str)` dans le shell IPython.

Une chaîne `place` a déjà été créée pour que vous puissiez l'expérimenter.

`@instructions`
- Utilisez la [méthode](https://docs.python.org/3/library/stdtypes.html#str.upper) `.upper()` sur `place` et stockez le résultat dans `place_up`. Utilisez la syntaxe d'appel des méthodes que vous avez apprise dans la vidéo précédente.
- Affichez `place` et `place_up`. Observez-vous un changement ?
- Affichez le nombre de o sur la variable `place` en appelant `.count()` sur `place` et en passant la lettre `'o'` en entrée de la méthode. Il s’agit de la variable `place`, et non du mot `"place"`.

`@hint`
- Vous pouvez appeler la méthode `.upper()` sur `place` sans aucune entrée supplémentaire.
- Pour afficher une variable `x`, vous pouvez taper `print(x)`.
- Veillez à intégrer votre appel à `place.count(____)` dans une fonction `print()` afin de l'afficher.

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
  has_printout(2, not_printed_msg = "Vous avez bien calculé le nombre de 'o' dans `place`; assurez-vous maintenant d'encapsuler l'appel `place.count('o')` dans une fonction `print()` pour imprimer le résultat."),
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

Les chaînes ne sont pas les seuls types Python auxquels des méthodes sont associées. Les listes, les flottants, les entiers et les booléens sont également des types accompagnés d'un grand nombre de méthodes utiles. Dans cet exercice, vous allez expérimenter avec :

- `.index()` pour obtenir l'index du premier élément d'une liste qui correspond à son entrée et
- `.count()` pour obtenir le nombre de fois qu'un élément apparaît dans une liste.

Vous travaillerez sur la liste des surfaces des différentes parties d'une maison : `areas`.

`@instructions`
- Utilisez la méthode `.index()` pour obtenir l'index de l'élément de `areas` qui est égal à `20.0`. Affichez cet index.
- Appelez `.count()` sur `areas` pour savoir combien de fois `9.50` apparaît dans la liste. Là encore, il vous suffit d'afficher ce numéro.

`@hint`
- Pour afficher l'index, intégrez l'appel à `areas.index(___)` dans une fonction `print()`.
- Pour afficher le nombre de fois qu'un élément `x` apparaît dans la liste, intégrez l'appel `areas.count(___)` dans une fonction `print()`.

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
predef_msg = "Vous n'avez pas besoin de changer ou de supprimer la liste prédéfinie `areas`."

Ex().check_object("areas", missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg)

Ex().check_function("print", index=0).check_args(0).check_function('areas.index', signature=False).check_args(0).has_equal_value()

Ex().check_function("print", index=1).check_args(0).check_function('areas.count', signature=False).has_equal_value()

success_msg("Bien ! Ce sont des exemples de méthodes `list` qui n'ont pas modifié la liste sur laquelle elles ont été appelées.")
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

La plupart des méthodes de liste modifient la liste sur laquelle elles sont appelées. En voici quelques exemples :

- `.append()` qui ajoute un élément à la liste sur laquelle il est appelé,
- `.remove()` qui [supprime](https://docs.python.org/3/library/stdtypes.html#typesseq-mutable) le premier élément d'une liste qui correspond à l'entrée, et
- `.reverse()`qui [inverse](https://docs.python.org/3/library/stdtypes.html#typesseq-mutable) l' ordre des éléments de la liste sur laquelle elle est appelée.

Vous travaillerez sur la liste avec la superficie des différentes parties de la maison : `areas`.

`@instructions`
- Utilisez deux fois `.append()` pour ajouter à nouveau la taille de l’abri de piscine et du garage : `24.5` et `15.45`, respectivement. Attention à les ajouter dans cet ordre.
- Affichez `areas`
- Utilisez la méthode `.reverse()` pour inverser l'ordre des éléments dans `areas`.
- Affichez à nouveau `areas`.

`@hint`
- Pour la première instruction, utilisez deux fois l'appel `areas.append(___)`.
- Pour afficher une variable `x`, il suffit de taper `print(x)`.
- La méthode `.reverse()` ne nécessite pas de données supplémentaires ; il suffit d'utiliser la notation par points et des parenthèses vides : `.reverse()`.
- Pour afficher une variable `x`, il suffit de taper `print(x)`.

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

success_msg("Super !")
```

---

## Paquets

```yaml
type: VideoExercise
key: ab96a17c5e
xp: 50
```

`@projector_key`
cedcfb34350be8545599768f96695cdd

---

## Paquet d'importation

```yaml
type: NormalExercise
key: 7432a6376f
lang: python
xp: 100
skills:
  - 2
```

Supposons que vous souhaitiez calculer la circonférence et l'aire d'un cercle. Voici à quoi ressemblent ces formules :

$$C = 2 \pi r$$
$$A = \pi r^2 $$

Plutôt que de taper le nombre `pi`, vous pouvez utiliser le paquet `math` qui contient ce nombre

Pour information, `**` est le symbole de l'exponentiation. Par exemple, `3**4` est `3` à la puissance de `4` et donnera `81`.

`@instructions`
- Importez le package `math`.
- Utilisez `math.pi` pour calculer la circonférence du cercle et stockez-la dans `C`.
- Utilisez `math.pi` pour calculer l'aire du cercle et stockez-la dans `A`.

`@hint`
- Vous pouvez simplement utiliser `import math`, puis faire référence à `pi` avec `math.pi`.
- Utilisez l'équation dans le texte de l’énoncé pour trouver `C`. Utilisez .
- Utilisez l'équation dans le texte de l’énoncé pour trouver `A`. Utilisez `*` et `**`.

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

Les importations générales, comme `import math`, mettent à votre disposition **toutes** les fonctionnalités du paquet `math`. Toutefois, si vous décidez de n'utiliser qu'une partie spécifique d'un paquet, vous pouvez toujours rendre votre importation plus sélective :

```
from math import pi
```

Réessayez la même chose, mais cette fois-ci, utilisez uniquement `pi`.

`@instructions`
- Effectuez un import sélectif à partir du paquet `math` en n'important que la fonction `pi`.
- Utilisez `pi` pour calculer la circonférence du cercle et stockez-la dans `C`.
- Utilisez `pi` pour calculer l'aire du cercle et stockez-la dans `A`.

`@hint`
- Utilisez `from math import pi` pour effectuer l'importation sélective.
- Désormais, vous pouvez utiliser `pi` seul !

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
  has_printout(0, not_printed_msg = "__JINJA__:Gardez `{{sol_call}}` pour afficher la circonférence."),
  has_printout(1, not_printed_msg = "__JINJA__:Gardez `{{sol_call}}` pour afficher l'aire.")
)

success_msg("Bien joué ! Passez à l'exercice suivant.")
```

---

## Différentes manières d'importer

```yaml
type: MultipleChoiceExercise
key: f1b2675a2a
lang: python
xp: 50
skills:
  - 2
```

Il existe plusieurs façons d'importer des paquets et des modules dans Python. En fonction de l'appel à l'importation, vous devrez utiliser un code Python différent.

Supposons que vous souhaitiez utiliser la [fonction](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.inv.html) `inv()`, qui se trouve dans le sous-paquet `linalg` du paquet `scipy`. Vous souhaitez pouvoir utiliser cette fonction de la manière suivante :

```
my_inv([[1,2], [3,4]])
```

De quelle déclaration `import` avez-vous besoin pour exécuter le code ci-dessus sans erreur ?

`@possible_answers`
- `import scipy`
- `import scipy.linalg`
- `from scipy.linalg import my_inv`
- `from scipy.linalg import inv as my_inv`

`@hint`
- Essayez les différentes instructions d'importation dans le shell IPython et voyez laquelle permet d'exécuter la ligne `my_inv([[1, 2], [3, 4]])` sans erreur. Appuyez sur la touche **Entrée** pour exécuter le code que vous avez saisi.

`@pre_exercise_code`
```{python}

```

`@sct`
```{python}
msg1 = msg2 = msg3 = "Incorrect, essayez à nouveau. Essayez les différentes instructions d'importation dans le shell IPython et voyez laquelle permet à la ligne `my_inv([[1, 2], [3, 4]])` de s'exécuter sans erreurs."
msg4 = "Correct ! Le mot `as` vous permet de créer un nom local pour la fonction que vous importez : `inv()` est maintenant disponible sous le nom `my_inv()`."
Ex().has_chosen(4, [msg1, msg2, msg3, msg4])
```

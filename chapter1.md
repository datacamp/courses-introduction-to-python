---
title_meta: Chapitre 1
title: Notions de base de Python
description: >-
  Une introduction aux concepts de base de Python. Apprenez à utiliser Python de
  manière interactive et au moyen d'un script. Créez vos premières variables et
  familiarisez-vous avec les types de données fondamentaux de Python.
attachments:
  slides_link: 'https://projector-video-pdf-converter.datacamp.com/735/chapter1.pdf'
free_preview: true
lessons:
  - nb_of_exercises: 3
    title: "Bonjour, Python\_!"
  - nb_of_exercises: 5
    title: Variables et types
---

## Bonjour, Python !

```yaml
type: VideoExercise
key: f644a48d5d
xp: 50
```

`@projector_key`
d8fcd4c930027fa4e1c3870c7e7e0ff1

---

## Votre premier code Python

```yaml
type: NormalExercise
key: bdc52f0e19
lang: python
xp: 100
skills:
  - 2
```

C'est le moment d'exécuter votre premier code Python!

Allez au code et cliquez sur le bouton Exécuter le code pour voir le résultat.

`@instructions`
- Cliquez sur le bouton Exécuter le code pour voir le résultat de `print(5 / 8)`.

`@hint`
- Exécutez d'abord le code avant de Soumettre la réponse afin d'avoir le temps d'examiner le résultat.

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
Ex().has_printout(0, not_printed_msg = "__JINJA__:Avez-vous utilisé `{{sol_call}}` pour imprimer `5 / 8`?")
success_msg("Super ! Passons à la suivante !")
```

---

## Python comme calculatrice

```yaml
type: NormalExercise
key: 0f7c039428
lang: python
xp: 100
skills:
  - 2
```

Python convient parfaitement aux calculs de base. Il peut faire de l'addition, de la soustraction, de la multiplication et de la division.

Le code dans le script donne quelques exemples.

À vous de pratiquer maintenant en écrivant votre propre code.

`@instructions`
- Affichez le résultat de la soustraction de `5` par `5` sous `# Subtraction` à l'aide de `print()`.
- Affichez le résultat de la multiplication de `3` par `5` sous `# Multiplication`.

`@hint`
- Vous devrez utiliser `print()` pour générer un résultat.
- Vous pouvez soustraire avec `-` et multiplier avec `*`.

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
Ex().has_printout(0, not_printed_msg = "Avez-vous utilisé `print(4 + 5)` pour afficher le résultat de votre somme ?")

Ex().has_printout(1, not_printed_msg = "Avez-vous utilisé `print(5 - 5)` pour afficher le résultat de votre soustraction ?")

Ex().has_printout(2, not_printed_msg = "Avez-vous utilisé `print(3 * 5)` pour afficher le résultat de votre multiplication ?")

Ex().has_printout(3, not_printed_msg = "Avez-vous utilisé `print(10 / 2)` pour afficher le résultat de votre division ?")

success_msg("C'est correct ! Python peut vous aider à faire les calculs, une caractéristique qui sera utile pour l'analyse à mesure que nous développons nos compétences en matière de données.")
```

---

## Variables et types

```yaml
type: VideoExercise
key: c2e396792e
xp: 50
```

`@projector_key`
433dcfcfedaee070cbf440491c402e3b

---

## Affectation de variable

```yaml
type: NormalExercise
key: 4bf65ad83e
lang: python
xp: 100
skills:
  - 2
```

En Python, une variable vous permet de référer à une valeur par un nom. Pour créer une variable `x` ayant la valeur `5`, vous utilisez `=`, comme dans cet exemple :

```
x = 5
```

Vous pouvez maintenant utiliser le nom de cette variable, `x`, au lieu de la valeur elle-même, `5`.

Rappelez-vous que `=` en Python signifie une _affectation_; cela ne teste pas l'égalité ! Essayez-le dans l'exercice en remplaçant `____` par votre code.

`@instructions`
- Créez une variable `savings` avec la valeur `100`.
- Vérifiez cette variable en tapant `print(savings)` dans le script.

`@hint`
- Tapez `savings = 100` pour créer la variable `savings`.
- Après avoir créé la variable `savings`, vous pouvez taper `print(savings)`.
- Votre code final ne doit contenir aucun `____`.

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
Ex().check_object("savings").has_equal_value(incorrect_msg="Assignez `100` à la variable `savings`.")
Ex().has_printout(0, not_printed_msg = "Affichez `savings`, la variable que vous avez créée, avec `print(savings)`.")
success_msg("Super ! Essayons maintenant de faire quelques calculs avec cette variable !")
```

---

## Calculs avec des variables

```yaml
type: NormalExercise
key: ff06cedeb4
lang: python
xp: 100
skills:
  - 2
```

Vous avez maintenant créé une variable d'épargne, alors commençons à mettre de côté!

Au lieu de calculer avec les valeurs elles-mêmes, vous pouvez utiliser des variables.

Combien d'argent auriez-vous économisé dans quatre mois si vous mettiez 10 $ de côté chaque mois?

`@instructions`
- Créez une variable `monthly_savings` égale à `10` et `num_months` égale à `4`.
- Multipliez `monthly_savings` par `num_months` et affectez le résultat à `new_savings`.
- Affichez la valeur de `new_savings`.

`@hint`
- Vous pouvez faire des calculs avec des variables de la même façon qu'avec des nombres, donc au lieu de `10 * 4`, remplacez les nombres par les variables!
- Utilisez `print()` pour voir le montant dans `new_savings`.
- Assurez-vous d'orthographier correctement les noms de variables!

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
Ex().check_object("monthly_savings").has_equal_value(incorrect_msg = "Avez-vous enregistré `10` dans `monthly_savings` en utilisant `monthly_savings = 10`?")
Ex().check_object("num_months").has_equal_value(incorrect_msg = "Avez-vous enregistré `4` dans `num_months` en utilisant `num_months = 4`?")
Ex().check_object("new_savings").has_equal_value(incorrect_msg = "Avez-vous utilisé les bonnes variables et symboles pour multiplier ? Attendu `monthly_savings * num_months` mais obtenu autre chose.")
# Ex().check_object("total_savings").has_equal_value(incorrect_msg = "Avez-vous utilisé les bonnes variables et symboles pour ajouter ? Attendu `savings + new_savings` mais obtenu autre chose.")

Ex().has_printout(0, not_printed_msg="N'oubliez pas d'imprimer `new_savings` à la fin de votre script.")

success_msg("Vous avez 40 $ en nouvelles économies !")
```

---

## Autres types de variables

```yaml
type: NormalExercise
key: 006b48561f
lang: python
xp: 100
skills:
  - 2
```

Dans l'exercice précédent, vous avez travaillé avec le type de données entier en Python :

- `int`, ou entier : un nombre sans partie décimale. `savings`, avec la valeur `100`, est un exemple d'entier.

En plus des types numériques, il existe trois autres types de données très courants :

- `float`, ou nombre à virgule flottante : un nombre qui comporte une partie entière et une partie décimale, séparées par un point. `1.1` est un exemple de float.
- `str`, ou chaîne de caractères : un type qui représente du texte. Vous pouvez utiliser des guillemets simples ou doubles pour créer une chaîne.
- `bool`, ou booléen : un type qui représente des valeurs logiques. Il ne peut être que `True` ou `False` (la casse est importante!).

`@instructions`
- Créez un nouveau float, `half`, avec la valeur `0.5`.
- Créez une nouvelle chaîne de caractères, `intro`, avec la valeur `"Hello! How are you?"`.
- Créez un nouveau booléen, `is_good`, avec la valeur `True`.

`@hint`
- Pour créer une variable en Python, utilisez `=`. Assurez-vous d'entourer votre chaîne de caractères avec des guillemets simples ou doubles.
- Il n'existe que deux valeurs booléennes en Python : `True` et `False`. `TRUE`, `true`, `FALSE`, `false` et autres variantes ne seront pas acceptées.

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
Ex().check_object("half").has_equal_value(incorrect_msg = "Avez-vous enregistré le flottant, `0.5` dans `half`?")

Ex().check_object("intro").has_equal_value(incorrect_msg = "Hmm, quelque chose est incorrect dans votre variable `intro`. Vérifiez l'orthographe et assurez-vous d'avoir utilisé des guillemets.")

Ex().check_object("is_good").has_equal_value(incorrect_msg = "Avez-vous mis en majuscule la valeur booléenne? N'oubliez pas que vous n'avez pas besoin d'utiliser des guillemets ici.")

success_msg("Bien joué!")
```

---

## Opérations avec d'autres types

```yaml
type: BulletExercise
key: 4d0d83cc02
xp: 100
```

En Python, les variables peuvent être de différents types. Pour connaître le type d'une variable, utilisez `type()`. Par exemple, pour voir le type de `a`, exécutez : `type(a)`.

Les types se comportent différemment en Python. Si vous additionnez deux chaînes de caractères, par exemple, le résultat sera différent de l'addition de deux entiers ou de deux booléens.

À vous de tester tout ça.

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
- Additionnez `savings` et `new_savings`, puis assignez le résultat à `total_savings`.
- Utilisez `type()` pour afficher le type obtenu de `total_savings`.

`@hint`
- Assignez `savings + new_savings` à une nouvelle variable, `total_savings`.
- Pour afficher le type d'une variable `x`, utilisez `print(type(x))`.

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
msg = "Vous n'avez pas à changer ou supprimer les variables prédéfinies."

Ex().multi(
    check_object('savings', missing_msg=msg).has_equal_value(incorrect_msg=msg),
    check_object('new_savings', missing_msg=msg).has_equal_value(incorrect_msg=msg)
)

Ex().multi(
    check_object("total_savings").has_equal_value(incorrect_msg="Ajoutez `savings` et `new_savings` pour créer la variable `total_savings`."),
    has_printout(1, not_printed_msg = "__JINJA__:Utilisez `{{sol_call}}` pour afficher le type de `total_savings`.")
)
```

***

```yaml
type: NormalExercise
key: f54fbf9bd9
xp: 50
```

`@instructions`
- Calculez la somme de `intro` et `intro` et assignez le résultat à `doubleintro`.
- Affichez `doubleintro`. Étiez-vous surpris du résultat?

`@hint`
- Assignez `intro + intro` à une nouvelle variable, `doubleintro`.
- Pour afficher une variable `x`, écrivez `print(x)` dans le script.

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
msg = "Vous n'avez pas à changer ou supprimer les variables prédéfinies."

Ex().check_object('intro', missing_msg=msg).has_equal_value(incorrect_msg=msg)

Ex().multi(
    check_object("doubleintro").has_equal_value(incorrect_msg  = "Avez-vous stocké le résultat de `intro + intro` dans `doubleintro`?"),
    has_printout(0, not_printed_msg = "N'oubliez pas d'imprimer `doubleintro`.")
)

success_msg("Bien. Remarquez comment `intro + intro` fait que `\"Hello! How are you?\"` et `\"Hello! How are you?\"` sont collés ensemble.")
```

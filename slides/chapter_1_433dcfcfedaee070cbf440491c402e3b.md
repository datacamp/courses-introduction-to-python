---
title: Insert title here
key: 433dcfcfedaee070cbf440491c402e3b
video_link:
  mp3: >-
    https://videos.datacamp.com/mp3/translations/course_735/fr-FR/f8f527aa-52de-4b1c-80bf-f14050db619e.mp3
---

## Variables et types

```yaml
type: TitleSlide
key: dc8b62f1c8
```

`@lower_third`
name: Hugo Bowne-Anderson
title: Data Scientist at DataCamp

`@script`
On poursuit les efforts ! Il est évident que Python est une excellente calculatrice. Si vous souhaitez effectuer des calculs plus complexes, il est recommandé d'enregistrer les valeurs au fur et à mesure que vous codez.


---

## Variable

```yaml
type: FullSlide
key: 36ec318b41
```

`@part1`
- Nom spécifique, sensible à la casse

- Appeler une valeur via le nom d'une variable{{1}}

- 1,79 m - 68,7 kg{{2}}

```py
height = 1.79
weight = 68.7
```{{3}}
```py
height
```{{4}}

```out
1.79
```{{4}}

`@script`
Vous pouvez le faire en définissant une variable avec un nom spécifique, sensible à la casse. Une fois que vous avez créé (ou déclaré) une telle variable, vous pouvez ensuite appeler sa valeur en saisissant le nom de la variable.

Supposons que vous mesuriez votre taille et votre poids en unités métriques : vous mesurez 1 mètre 79 et pesez 68 virgule 7 kilos. Vous pouvez attribuer ces valeurs à deux variables, nommées height et weight, à l'aide d'un signe égal :

Si vous tapez maintenant le nom de la variable, height,

Python recherche le nom de la variable, récupère sa valeur et l'affiche.


---

## Calculer l'IMC (BMI)

```yaml
type: TwoColumns
key: fe1b10a93b
code_zoom: 80
```

`@part1`
```py
height = 1.79
weight = 68.7
```
```py
height
```

```out
1.79
```

$$ \text{BMI} = \frac{\text{weight}}{\text{height}^2} $${{1}}

`@part2`
```py
68.7 / 1.79 ** 2
```{{2}}

```out
21.4413
```{{2}}

```py
weight / height ** 2
```{{3}}

```out
21.4413
```{{3}}

```py
bmi = weight / height ** 2
bmi
```{{4}}

```out
21.4413
```{{4}}

`@script`
Calculons maintenant l'indice de masse corporelle, ou IMC, qui se calcule comme suit, avec le poids en kilogrammes et la taille en mètres. Vous pouvez procéder ainsi avec les valeurs réelles, mais vous pouvez également utiliser les variables hauteur et poids, comme illustré ici. Chaque fois que vous tapez le nom de la variable, vous demandez à Python de le remplacer par la valeur réelle de la variable. weight correspond à 68 virgule 7 et height à 1 virgule 79.

Enfin, cette version utilise Python pour stocker le résultat dans une nouvelle variable, bmi. bmi contient désormais la même valeur que celle que vous avez calculée précédemment.

En Python, les variables sont utilisées tout le temps. Elles contribuent à rendre votre code reproductible.


---

## Reproductibilité

```yaml
type: FullSlide
key: 9980f47f9d
```

`@part1`
```py
height = 1.79
weight = 68.7
bmi = weight / height ** 2
print(bmi)
```

```out
21.4413
```

`@script`
Supposons que le code permettant de créer les variables hauteur, poids et IMC se trouve dans un script, comme ceci. Si vous souhaitez maintenant recalculer l'IMC pour un autre poids,


---

## Reproductibilité

```yaml
type: FullSlide
key: a4e899f00f
disable_transition: true
```

`@part1`
```py
height = 1.79
weight = 74.2 # <-
bmi = weight / height ** 2
print(bmi)
```

```out
23.1578
```

`@script`
vous pouvez simplement modifier la déclaration de la variable « weight » et relancer le script. L'IMC change en conséquence, car la valeur de la variable weight a également changé.

Jusqu'à présent, nous avons uniquement travaillé avec des valeurs numériques, telles que la taille et le poids.


---

## Types Python

```yaml
type: FullSlide
key: 9d86084ad4
```

`@part1`
```py
type(bmi)
```{{1}}

```out
float
```{{1}}

```py
day_of_week = 5
type(day_of_week)
```{{2}}

```out
int
```{{2}}

`@script`
En Python, ces nombres ont tous un type spécifique. Vous pouvez vérifier le type d'une valeur à l'aide de la fonction type. Pour connaître le type de notre valeur IMC, il suffit d'écrire « type » puis « IMC » entre parenthèses. Vous pouvez constater qu'il s'agit d'un nombre flottant, qui est la manière dont Python représente un nombre réel, c'est-à-dire un nombre qui peut avoir une partie entière et une partie fractionnaire. Python dispose également d'un type pour les entiers : int, comme dans cet exemple.

Pour faire de la science des données, vous aurez toutefois besoin de plus que des entiers et des flottants.


---

## Types Python (2)

```yaml
type: FullSlide
key: d971d34e6a
```

`@part1`
```py
x = "body mass index"
y = 'this works too'
```{{1}}
```py
type(y)
```{{2}}

```out
str
```{{2}}

```py
z = True
type(z)
```{{3}}

```out
bool
```{{3}}

`@script`
Python propose de nombreux autres types de données. Les plus courants sont les chaînes et les booléens.

Une chaîne est la manière dont Python représente le texte. Vous pouvez utiliser des guillemets doubles ou simples pour créer une chaîne, comme le montrent les exemples suivants. Si vous affichez le type de la dernière variable ici, vous constaterez qu'il s'agit de S T R, abréviation de string.

Le booléen est un type qui peut prendre la valeur True ou False. Ils équivalent à un oui ou un non dans le langage courant. Les booléens seront très utiles à l'avenir, par exemple pour effectuer des opérations de filtrage sur vos données.

Les types de données Python ont quelque chose de particulier.


---

## Types Python (3)

```yaml
type: FullSlide
key: 24601e2af0
```

`@part1`
```py
2 + 3
```{{1}}

```out
5
```{{1}}

```py
'ab' + 'cd'
```{{2}}

```out
'abcd'
```{{2}}

- Différent type = différent comportement !{{3}}

`@script`
Veuillez examiner cette ligne de code, qui additionne deux nombres entiers, puis cette ligne de code, qui additionne deux chaînes.

Pour les nombres entiers, les valeurs ont été additionnées, tandis que pour les chaînes, elles ont été collées les unes à la suite des autres. L'opérateur plus se comportait différemment selon les types de données. Il s'agit d'un principe général : le comportement du code dépend des types avec lesquels vous travaillez.

Dans les exercices qui suivent, vous allez créer vos premières variables et expérimenter certains types de données Python. Je vous invite à visionner la prochaine vidéo pour une explication détaillée sur les listes.


---

## Passons à la pratique !

```yaml
type: FinalSlide
key: b7fc40db4d
```

`@script`
Commençons à coder, j'ai hâte de vous retrouver dans le prochain chapitre où vous créerez des graphiques Python encore plus impressionnants.

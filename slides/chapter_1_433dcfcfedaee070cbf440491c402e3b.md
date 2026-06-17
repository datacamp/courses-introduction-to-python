---
title: Insert title here
key: 433dcfcfedaee070cbf440491c402e3b
video_link:
  mp3: >-
    https://videos.datacamp.com/mp3/translations/course_735/fr-CA/97fef76f-69fa-4722-bd18-e9a74a8b9da8-57f64f5671a16265962717475ebe27d9.mp3
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
Bravo et bon retour! On voit tout de suite que Python fait un excellent calculateur. Mais si vous voulez faire des calculs plus complexes, vous aurez envie de « sauvegarder » des valeurs pendant que vous codez.

---

## Variable

```yaml
type: FullSlide
key: 36ec318b41
```

`@part1`
- Nom précis, sensible à la casse

- Récupérer la valeur via le nom de la variable{{1}}

- 1,79 m - 68,7 kg{{2}}

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
Vous pouvez le faire en définissant une variable, avec un nom précis, sensible à la casse. Une fois que vous créez (ou déclarez) cette variable, vous pouvez ensuite rappeler sa valeur en tapant son nom.

Supposons que vous mesuriez votre taille et votre poids, en unités métriques: vous mesurez un-mètre-soixante-dix-neuf et pesez soixante-huit-virgule-sept kilogrammes. Vous pouvez attribuer ces valeurs à deux variables, nommées height et weight, avec un signe égal:

Si vous tapez maintenant le nom de la variable, height,

Python cherche le nom de la variable, récupère sa valeur et l'affiche.

---

## Calculer l'IMC

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

$$ \text{IMC} = \frac{\text{poids}}{\text{taille}^2} $${{1}}

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
Calculons maintenant l'indice de masse corporelle, ou I-M-C, qui se calcule ainsi, avec le poids en kilogrammes et la taille en mètres. Vous pouvez le faire avec les valeurs réelles, mais vous pouvez tout aussi bien utiliser les variables height et weight, comme ici. Chaque fois que vous tapez le nom d'une variable, vous demandez à Python de le remplacer par la valeur réelle de la variable. weight correspond à soixante-huit-virgule-sept, et height à un-virgule-soixante-dix-neuf.

Enfin, cette version demande à Python d'enregistrer le résultat dans une nouvelle variable, bmi. bmi contient maintenant la même valeur que celle que vous avez calculée plus tôt.

En Python, on utilise des variables tout le temps. Elles aident à rendre votre code reproductible.

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
Supposons que le code pour créer les variables height, weight et bmi se trouve dans un script, comme ceci. Si vous voulez maintenant recalculer le I-M-C pour un autre poids,

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
il suffit de modifier la déclaration de la variable weight et de relancer le script. Le I-M-C change en conséquence, parce que la valeur de la variable weight a aussi changé.

Jusqu'ici, nous avons seulement travaillé avec des valeurs numériques, comme la taille et le poids.

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
En Python, ces nombres ont tous un type précis. Vous pouvez vérifier le type d'une valeur avec la fonction type. Pour voir le type de notre valeur bmi, écrivez simplement type avec bmi entre parenthèses. Vous voyez que c'est un float, la façon dont Python représente un nombre réel, donc un nombre qui peut avoir une partie entière et une partie décimale. Python a aussi un type pour les entiers: int, comme dans cet exemple.

Pour faire de la science des données, vous aurez toutefois besoin de plus que des int et des float.

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
Python offre une foule d'autres types de données. Les plus courants sont les chaînes de caractères et les booléens.

Une chaîne, c'est la façon de Python de représenter du texte. Vous pouvez utiliser à la fois des guillemets doubles et simples pour créer une chaîne, comme on le voit dans ces exemples. Si vous affichez le type de la dernière variable ici, vous voyez que c'est str, pour string.

Le booléen est un type qui peut être True ou False. On peut l'associer à « Oui » et « Non » dans le langage courant. Les booléens seront très utiles plus tard, par exemple pour filtrer vos données.

Il y a quelque chose de particulier au sujet des types de données en Python.

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

- Type différent = comportement différent !{{3}}

`@script`
Regardez cette ligne de code, qui additionne deux entiers, et ensuite cette ligne de code, qui additionne deux chaînes.

Pour les entiers, les valeurs ont été additionnées, tandis que pour les chaînes, elles ont été collées l'une à l'autre. L'opérateur plus s'est comporté différemment selon les types de données. C'est un principe général: le comportement du code dépend des types avec lesquels vous travaillez.

Dans les exercices qui suivent, vous créerez vos premières variables et vous expérimenterez certains des types de données de Python. On se retrouve dans la prochaine vidéo pour tout expliquer au sujet des listes.

---

## Passons à la pratique !

```yaml
type: FinalSlide
key: b7fc40db4d
```

`@script`
Passons au code, et j'ai bien hâte de vous retrouver au prochain chapitre où vous créerez des graphiques Python encore plus impressionnants.

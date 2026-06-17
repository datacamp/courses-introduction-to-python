---
title: Insert title here
key: ae3238dcc7feb9adecfee0c395fc8dc8
video_link:
  mp3: >-
    https://videos.datacamp.com/mp3/translations/course_735/fr-CA/d924b616-0cd3-49e1-9467-09ac92618db7-c1ad7c68e2f68758f97f03fa1a9b6a84.mp3
---

## Tableaux NumPy 2D

```yaml
type: TitleSlide
key: 0cc8abf493
```

`@lower_third`
name: Hugo Bowne-Anderson
title: Data Scientist at DataCamp

`@script`
Bravo, champion ou championne! Recréons maintenant les tableaux numpy de la vidéo précédente.

---

## Type des tableaux NumPy

```yaml
type: FullSlide
key: 1b9db47fd2
code_zoom: 100
```

`@part1`
```py
import numpy as np
np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
np_weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])
```

```py
type(np_height)
```

```out
numpy.ndarray
```

```py
type(np_weight)
```

```out
numpy.ndarray
```

`@script`
Si vous demandez le type de ces tableaux, Python vous indique qu'il s'agit de numpy.ndarray. Le point numpy vous dit que c'est un type défini dans le paquet numpy. ndarray signifie tableau à n dimensions. Les tableaux np_height et np_weight sont des tableaux à une dimension, mais il est tout à fait possible de créer des tableaux à deux dimensions, trois dimensions, et même à sept dimensions! Restons-en toutefois à deux dans cette vidéo.

---

## Tableaux NumPy 2D

```yaml
type: FullSlide
key: ebb550dcba
code_zoom: 71
```

`@part1`
```py
np_2d = np.array([[1.73, 1.68, 1.71, 1.89, 1.79],
                  [65.4, 59.2, 63.6, 88.4, 68.7]])
```{{1}}
```py
np_2d
```{{2}}

```out
array([[ 1.73,  1.68,  1.71,  1.89,  1.79],
       [65.4 , 59.2 , 63.6 , 88.4 , 68.7 ]])
```{{2}}

```py
np_2d.shape
```{{3}}

```out
(2, 5) # 2 lignes, 5 colonnes
```{{3}}

```py
np.array([[1.73, 1.68, 1.71, 1.89, 1.79],
          [65.4, 59.2, 63.6, 88.4, "68.7"]])
```{{4}}

```out
array([['1.73', '1.68', '1.71', '1.89', '1.79'],
       ['65.4', '59.2', '63.6', '88.4', '68.7']], dtype='<U32')
```{{4}}

`@script`
Vous pouvez créer un tableau numpy deux D à partir d'une liste de listes Python classique. Essayons de créer un seul tableau numpy pour regrouper toutes les données de taille et de poids de votre famille, comme ceci.

Si vous affichez np_2d maintenant, vous verrez qu'il s'agit d'une structure de données rectangulaire : chaque sous-liste de la liste correspond à une ligne dans le tableau numpy deux D. Avec np_2d.shape, vous voyez que nous avons bel et bien deux lignes et cinq colonnes. shape est ce qu'on appelle un attribut du tableau np_2d, qui peut vous donner plus d'information sur la structure des données.

Notez que la syntaxe pour accéder à un attribut ressemble un peu à l'appel d'une méthode, mais ce n'est pas la même chose! Rappelez-vous que les méthodes ont des parenthèses après elles et, comme vous le voyez ici, les attributs n'en ont pas.

Toujours pour les tableaux deux D, la règle NumPy s'applique : un tableau ne peut contenir qu'un seul type. Si vous changez un nombre à virgule flottante pour une chaîne de caractères, tous les éléments du tableau seront convertis en chaînes, afin d'obtenir un tableau homogène.

---

## Sous-ensembles

```yaml
type: FullSlide
key: e71d2fc8b8
code_zoom: 80
```

`@part1`
```out
           0       1       2       3       4
           
array([[  1.73,   1.68,   1.71,   1.89,   1.79],     0
       [  65.4,   59.2,   63.6,   88.4,   68.7]])    1
```

```py
np_2d[0]
```

```out
array([1.73, 1.68, 1.71, 1.89, 1.79])
```

`@script`
Vous pouvez voir le tableau numpy deux D comme une version améliorée d'une liste de listes : vous pouvez effectuer des calculs sur les tableaux, comme je l'ai montré plus tôt, et vous pouvez faire des découpages plus avancés.

Supposons que vous vouliez la première ligne, puis le troisième élément de cette ligne. Pour sélectionner la ligne, vous avez besoin de l'indice zéro entre crochets. N'oubliez pas que l'indexation commence à zéro.

Pour ensuite sélectionner le troisième élément, vous pouvez prolonger le même appel avec une autre paire de crochets, cette fois avec l'indice deux,

---

## Sous-ensembles

```yaml
type: FullSlide
key: 57a1fb1581
disable_transition: true
code_zoom: 80
```

`@part1`
```out
           0       1       2       3       4
           
array([[  1.73,   1.68,   1.71,   1.89,   1.79],     0
       [  65.4,   59.2,   63.6,   88.4,   68.7]])    1
```

```py
np_2d[0][2]
```

```out
1.71
```

```py
np_2d[0, 2]
```{{1}}

```out
1.71
```{{1}}

`@script`
comme ceci. En gros, vous sélectionnez la ligne, puis à partir de cette ligne, vous faites une autre sélection.

Il existe aussi une autre façon de découper, en utilisant une seule paire de crochets et une virgule. Cet appel renvoie exactement la même valeur qu'avant. La valeur avant la virgule précise la ligne, la valeur après la virgule précise la colonne. L'intersection des lignes et colonnes que vous avez indiquées est renvoyée. Une fois que vous vous y habituez, cette syntaxe est plus intuitive et ouvre plus de possibilités.

---

## Sous-ensembles

```yaml
type: FullSlide
key: feb75c975c
disable_transition: true
code_zoom: 80
```

`@part1`
```out
           0       1       2       3       4
           
array([[  1.73,   1.68,   1.71,   1.89,   1.79],     0
       [  65.4,   59.2,   63.6,   88.4,   68.7]])    1
```

```py
np_2d[:, 1:3]
```{{1}}

```out
array([[ 1.68,  1.71],
       [59.2 , 63.6 ]])
```{{1}}

```py
np_2d[1, :]
```{{2}}

```out
array([65.4, 59.2, 63.6, 88.4, 68.7])
```{{2}}

`@script`
Supposons que vous vouliez sélectionner la taille et le poids du deuxième et du troisième membre de la famille. Vous voulez les deux lignes, donc vous mettez deux-points avant la virgule. Vous ne voulez que la deuxième et la troisième colonne, donc vous mettez les indices un à trois après la virgule. Rappelez-vous que le troisième indice n'est pas inclus ici. L'intersection nous donne un tableau deux D avec deux lignes et deux colonnes :

De la même façon, vous pouvez sélectionner le poids de tous les membres de la famille ainsi : vous ne voulez que la deuxième ligne, donc mettez un avant la virgule. Vous voulez toutes les colonnes, donc utilisez deux-points après la virgule. L'intersection nous donne toute la deuxième ligne.

Enfin, les tableaux numpy deux D vous permettent de faire des calculs élément par élément, exactement comme vous l'avez fait avec les tableaux numpy une D. C'est quelque chose

---

## Passons à la pratique !

```yaml
type: FinalSlide
key: 6047b27c09
```

`@script`
que vous pouvez expérimenter dans les exercices, en plus de créer et de découper des tableaux numpy deux D! Enthousiasmant

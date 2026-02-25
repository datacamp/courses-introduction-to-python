---
title: Insert title here
key: ae3238dcc7feb9adecfee0c395fc8dc8
video_link:
  mp3: >-
    https://videos.datacamp.com/mp3/translations/course_735/fr-FR/f96b4b20-c676-4227-972b-94e80ef95e52.mp3
---

## Tableaux 2D NumPy

```yaml
type: TitleSlide
key: 0cc8abf493
```

`@lower_third`
name: Hugo Bowne-Anderson
title: Data Scientist at DataCamp

`@script`
Bravo, vous êtes une légende ! Recréons maintenant les tableaux numpy de la vidéo précédente.


---

## Types de tableaux NumPy

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
Si vous demandez le type de ces tableaux, Python vous répond qu'il s'agit de numpy.ndarray. numpy dot vous indique qu'il s'agit d'un type défini dans le paquet numpy. ndarray signifie tableau n-dimensionnel. Les tableaux np tiret height et np tiret weight sont des tableaux unidimensionnels, mais il est tout à fait possible de créer des tableaux bidimensionnels, tridimensionnels, voire septidimensionnels. Toutefois, restons-en à deux dans cette vidéo.


---

## Tableaux 2D NumPy

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
(2, 5) # 2 rows, 5 columns
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
Vous pouvez créer un tableau numpy 2D à partir d'une liste Python classique de listes. Essayons de créer un tableau numpy pour toutes les données de taille et de poids de votre famille, comme ceci.

Si vous affichez np tiret 2d maintenant, vous constaterez qu'il s'agit d'une structure de données rectangulaire : Chaque sous-liste de la liste correspond à une ligne dans le tableau numpy bidimensionnel. À partir de np tiret 2D point shape, vous pouvez constater que nous avons bien 2 lignes et 5 colonnes. shape est un attribut du tableau N P 2 D qui fournit des informations supplémentaires sur la structure des données.

Veuillez noter que la syntaxe permettant d'accéder à un attribut ressemble quelque peu à celle utilisée pour appeler une méthode, mais il ne s'agit pas de la même chose. N'oubliez pas que les méthodes sont suivies de parenthèses, contrairement aux attributs, comme vous pouvez le constater ici.

Pour les tableaux 2D également, la règle NumPy s'applique : un tableau ne peut contenir qu'un seul type. Si vous convertissez un nombre flottant en chaîne, tous les éléments du tableau seront convertis en chaînes, afin d'obtenir un tableau homogène.


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
Vous pouvez considérer le tableau numpy 2D comme une liste de listes améliorée : vous pouvez effectuer des calculs sur les tableaux, comme je l'ai montré précédemment, et vous pouvez utiliser des méthodes plus avancées pour créer des sous-ensembles.

Supposons que vous souhaitiez obtenir la première ligne, puis le troisième élément de cette ligne. Pour sélectionner la ligne, vous devez utiliser l'index 0 entre crochets. N'oubliez pas l'indexation zéro.

Pour sélectionner ensuite le troisième élément, vous pouvez étendre le même appel avec une autre paire de crochets, cette fois avec l'index 2,


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
comme ceci. En substance, vous sélectionnez la ligne, puis vous effectuez une autre sélection à partir de cette ligne.

Il existe également une autre méthode pour créer des sous-ensembles, en utilisant des crochets simples et une virgule. Cet appel renvoie exactement la même valeur qu'auparavant. La valeur avant la virgule spécifie la ligne, la valeur après la virgule spécifie la colonne. L'intersection des lignes et des colonnes que vous avez spécifiées est renvoyée. Une fois que vous vous y serez habitué, cette syntaxe vous semblera plus intuitive et vous offrira davantage de possibilités.


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
Supposons que vous souhaitiez sélectionner la taille et le poids du deuxième et du troisième membre de la famille. Vous souhaitez conserver les deux lignes, vous devez donc insérer un deux-points avant la virgule. Vous ne souhaitez conserver que les deuxième et troisième colonnes, vous devez donc saisir les index 1 à 3 après la virgule. Veuillez noter que le troisième index n'est pas inclus ici. L'intersection nous donne un tableau 2D avec 2 lignes et 2 colonnes :

De la même manière, vous pouvez sélectionner le poids de tous les membres de la famille comme suit : vous ne souhaitez que la deuxième ligne, donc placez 1 avant la virgule. Vous souhaitez avoir toutes les colonnes, vous devez donc utiliser deux points après la virgule. L'intersection nous donne toute la deuxième ligne.

Enfin, les tableaux numpy 2D vous permettent d'effectuer des calculs élément par élément, de la même manière que vous le faisiez avec les tableaux numpy 1D. C'est quelque chose


---

## Passons à la pratique !

```yaml
type: FinalSlide
key: 6047b27c09
```

`@script`
que vous pouvez tester dans les exercices, tout en créant et en sous-divisant des tableaux numpy 2D. Génial, non ?

---
title: Insert title here
key: d8fcd4c930027fa4e1c3870c7e7e0ff1
video_link:
  mp3: >-
    https://videos.datacamp.com/mp3/translations/course_735/fr-CA/a3bc2f0d-7cec-448d-900e-3a91fc6e16ab-37d99a1bf87389dd35b1e6b9f3bd7fe4.mp3
---

## Bonjour Python !

```yaml
type: TitleSlide
key: f743ca8c41
```

`@lower_third`
name: Hugo Bowne-Anderson
title: Data Scientist at DataCamp

`@script`
Bonjour, je m'appelle Hugo et je serai votre hôte pour Introduction à Python pour la science des données.

Je suis scientifique des données et formateur chez DataCamp.

---

## Comment vous allez apprendre

```yaml
type: FullSlide
key: 30ee08a725
disable_transition: true
```

`@part1`
![Interface DataCamp](https://assets.datacamp.com/img/translations/fr-CA/production/repositories/288/datasets/729574d2168960686381caefe79baf5978e27d0d/liveexercise.gif)

`@script`
Dans ce cours, vous allez apprendre Python pour la science des données au moyen de leçons vidéo, comme celle-ci, et d'exercices interactifs. Vous obtenez votre propre session Python où vous pouvez expérimenter et essayer de trouver le bon code pour résoudre les consignes. Vous apprenez en le faisant, tout en recevant une rétroaction personnalisée et instantanée sur votre travail.

---

## Python

```yaml
type: FullSlide
key: 3f23b93572
```

`@part1`
![guido-hba.png](https://assets.datacamp.com/img/translations/fr-CA/production/repositories/288/datasets/fb3e4b8dc114529dafffb37d33f2b2244210d40f/guido-hba.png = 38){{1}}

- Usage général : créer n'importe quoi{{2}}

- Code source ouvert ! Gratuit !{{3}}

- Forfaits Python, aussi pour la science des données{{4}}

	- De nombreuses applications et domaines{{5}}

`@script`
Python a été conçu par Guido Van Rossum. Ici, vous pouvez voir une photo de moi avec Guido. Ce qui a commencé comme un passe-temps est vite devenu un langage de programmation polyvalent : de nos jours, vous pouvez utiliser Python pour créer pratiquement n'importe quel logiciel. Mais comment en est-on arrivé là? D'abord, Python est à source ouverte. Il est gratuit. Ensuite, il est très facile de créer des modules en Python, c'est-à-dire du code que vous pouvez partager avec d'autres pour résoudre des problèmes précis. Avec le temps, de plus en plus de ces modules spécifiquement conçus pour la science des données ont été développés. Supposons que vous vouliez faire de belles visualisations des ventes de votre entreprise. Il y a un module pour ça. Ou encore vous connecter à une base de données pour analyser des mesures de capteurs? Il y a aussi un module pour ça.
On qualifie souvent Python de couteau suisse des langages de programmation, puisque vous pouvez presque tout faire avec.
Dans ce cours, nous allons développer vos compétences de codage en science des données petit à petit, alors assurez-vous de rester avec nous pour voir à quel point le langage peut être puissant.

---

## IPython Shell

```yaml
type: FullSlide
key: 43a91a7217
```

`@part1`
**Exécuter des commandes Python**

![ipython_shell.png](https://assets.datacamp.com/img/translations/fr-CA/production/repositories/288/datasets/a9e8440bb8fbd49e4a73e4c36ef1cd677c0dd55f/pyexercise.png = 95)

`@script`
Maintenant que vous êtes tout ouïe pour Python, commençons à expérimenter. Je vais débuter avec le

---

## IPython Shell

```yaml
type: FullSlide
key: 9c51ee700d
disable_transition: true
```

`@part1`
**Exécuter des commandes Python**

![ipython_shell_highlighted.png](https://assets.datacamp.com/img/translations/fr-CA/production/repositories/288/datasets/dd43cc0183b15b43a072eb0fbab4caa72dee9250/pyexercise_shell.jpg = 95)

`@script`
terminal Python, un endroit où vous pouvez taper du code Python et voir immédiatement les résultats. Dans l'interface des exercices de DataCamp, ce terminal est intégré ici. Commençons simplement et utilisons Python comme calculatrice.

---

## IPython Shell

```yaml
type: FullSlide
key: 524e4c20a7
disable_transition: true
```

`@part1`
&nbsp;

![Calculs dans l'IPython Shell de DataCamp](https://assets.datacamp.com/img/translations/fr-CA/production/repositories/288/datasets/cee32b788a62e4b9a1234ccde56ac9ebb49cfa72/shelladdition.gif = 95)

`@script`
Je tape quatre plus cinq, puis j'appuie sur Entrée. Python interprète ce que vous avez écrit et affiche le résultat de votre calcul, neuf. Le terminal Python utilisé ici n'est pas l'original; nous utilisons IPython, pour Python interactif, une version bonifiée du Python régulier qui sera utile plus tard.

IPython a été créé par Fernando Pérez et fait partie de l'écosystème Jupyter au sens large. En plus de travailler de façon interactive avec Python, vous pouvez aussi faire exécuter par Python ce qu'on appelle des

---

## Script Python

```yaml
type: FullSlide
key: 78ef256bc0
```

`@part1`
- Fichiers texte - `.py`{{1}}

- Suite de commandes Python{{2}}

- Semblable à la saisie dans IPython Shell{{3}}

![Script Python dans DataCamp](https://assets.datacamp.com/img/translations/fr-CA/production/repositories/288/datasets/59f196e96536543a4fb8801228019fc4106f3791/pyexercise_script.jpg = 78){{3}}

`@script`
scripts Python. Ces scripts Python sont simplement des fichiers texte avec l'extension point py. C'est essentiellement une liste de commandes Python exécutées presque comme si vous tapiez vous-même les commandes dans le terminal, ligne par ligne.

---

## Script Python

```yaml
type: FullSlide
key: 717d124175
disable_transition: true
```

`@part1`
![GIF : saisie de 4 + 5 dans le script et clic sur Soumettre la réponse. Aucun résultat affiché.](https://assets.datacamp.com/img/translations/fr-CA/production/repositories/288/datasets/2f96e979012e15329cc158d1e0f496aac3539f45/scriptnoprint.gif = 95)

`@script`
Plaçons maintenant la commande d'avant dans un script, que vous trouvez ici dans l'interface de DataCamp. L'étape suivante consiste à exécuter le script en cliquant sur "Submit Answer". Si vous exécutez ce script dans l'interface de DataCamp, il n'y a rien dans le volet de sortie. C'est parce que vous devez explicitement utiliser print dans les scripts si vous voulez générer une sortie à l'exécution.

---

## Script Python

```yaml
type: FullSlide
key: c7a9d02fb6
disable_transition: true
code_zoom: 90
```

`@part1`
![python_script_print.gif](https://assets.datacamp.com/img/translations/fr-CA/production/repositories/288/datasets/8b13d046bb54dcb11aa49f0da7363781129d1561/scriptwithprint.gif = 95)

- Utilisez `print()` pour afficher un résultat depuis le script

`@script`
Encapsulons notre calcul précédent dans un appel à print, puis relançons le script. Cette fois, la même sortie qu'auparavant est générée, parfait! Mettre votre code dans des scripts Python au lieu de retaper chaque étape manuellement en mode interactif vous aidera à garder une structure et à éviter de tout retaper sans cesse si vous voulez apporter une modification; il suffit de changer le script et de relancer le tout.

---

## Interface DataCamp

```yaml
type: FullSlide
key: 693ba1cd14
```

`@part1`
![Capture d'écran de l'interface DataCamp](https://assets.datacamp.com/img/translations/fr-CA/production/repositories/288/datasets/a9e8440bb8fbd49e4a73e4c36ef1cd677c0dd55f/pyexercise.png)

`@script`
Maintenant que vous avez une idée des différentes façons de travailler avec Python, je vous suggère de passer aux exercices. Utilisez le terminal IPython pour expérimenter, et utilisez l'éditeur de scripts Python pour coder la vraie réponse. Si vous cliquez sur Submit Answer, votre script sera exécuté et vérifié pour en confirmer l'exactitude.

---

## Passons à la pratique !

```yaml
type: FinalSlide
key: 7445cd202e
```

`@script`
Au travail, et surtout, amusez-vous!

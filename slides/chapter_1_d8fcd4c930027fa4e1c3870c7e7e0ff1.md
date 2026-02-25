---
title: Insert title here
key: d8fcd4c930027fa4e1c3870c7e7e0ff1
video_link:
  mp3: >-
    https://videos.datacamp.com/mp3/translations/course_735/fr-FR/fd1d43cb-ad03-40c4-bf0c-27c5a0e3ab36.mp3
---

## Bonjour Python !

```yaml
type: TitleSlide
key: f743ca8c41
```

`@lower_third`
name: Hugo Bowne-Anderson
title: Data Scientist at DataCamp

`@script`
Bonjour, je m'appelle Hugo et je serai votre animateur pour le cours de présentation de Python pour la science des données.

Je suis data scientist et formateur chez DataCamp.


---

## Ce que vous allez apprendre et comment

```yaml
type: FullSlide
key: 30ee08a725
disable_transition: true
```

`@part1`
![Interface DataCamp](https://assets.datacamp.com/img/translations/fr-FR/production/repositories/288/datasets/729574d2168960686381caefe79baf5978e27d0d/liveexercise.gif)

`@script`
Dans ce cours, vous apprendrez Python pour la science des données grâce à des leçons vidéo, comme celle-ci, et à des exercices interactifs. Vous disposez de votre propre session Python où vous pouvez expérimenter et essayer de trouver le code correct pour résoudre les instructions. Vous apprenez en pratiquant, tout en recevant des commentaires personnalisés et instantanés sur votre travail.


---

## Python

```yaml
type: FullSlide
key: 3f23b93572
```

`@part1`
![guido-hba.png](https://assets.datacamp.com/img/translations/fr-FR/production/repositories/288/datasets/fb3e4b8dc114529dafffb37d33f2b2244210d40f/guido-hba.png = 38){{1}}

- Polyvalent : pour tout type de projet{{2}}

- Open source ! Gratuit !{{3}}

- Paquets Python, également pour la science des données{{4}}

	- De nombreuses applications dans des domaines variés{{5}}

`@script`
Python a été conçu par Guido Van Rossum. Ici, vous pouvez voir une photo de moi avec Guido. Ce qui a commencé comme un projet amateur est rapidement devenu un langage de programmation polyvalent : aujourd'hui, Python peut être utilisé pour développer pratiquement n'importe quel type de logiciel. Comment cela est-il arrivé ? Tout d'abord, Python est open source. Son utilisation est gratuite. Deuxièmement, il est très facile de créer des paquets en Python, qui sont des codes que vous pouvez partager avec d'autres personnes pour résoudre des problèmes spécifiques. Au fil du temps, de plus en plus de ces paquets spécialement conçus pour la science des données ont été développés. Supposons que vous souhaitiez créer des visualisations sophistiquées des ventes de votre entreprise. Il existe un paquet adapté à cela. Ou que diriez-vous de vous connecter à une base de données pour analyser les mesures des capteurs ? Il existe également un paquet pour cela.
Les gens qualifient souvent Python de « couteau suisse » des langages de programmation, car il permet de réaliser presque toutes les tâches.
Dans ce cours, nous commencerons à développer progressivement vos compétences en codage dans le domaine de la science des données. Nous vous invitons donc à rester avec nous pour découvrir toute la puissance de ce langage.


---

## Shell IPython

```yaml
type: FullSlide
key: 43a91a7217
```

`@part1`
**Exécutez des commandes Python**

![ipython_shell.png](https://assets.datacamp.com/img/translations/fr-FR/production/repositories/288/datasets/a9e8440bb8fbd49e4a73e4c36ef1cd677c0dd55f/pyexercise.png = 95)

`@script`
Maintenant que vous êtes prêt à découvrir Python, commençons à expérimenter. Je commencerai par le


---

## Shell IPython

```yaml
type: FullSlide
key: 9c51ee700d
disable_transition: true
```

`@part1`
**Exécutez des commandes Python**

![ipython_shell_highlighted.png](https://assets.datacamp.com/img/translations/fr-FR/production/repositories/288/datasets/dd43cc0183b15b43a072eb0fbab4caa72dee9250/pyexercise_shell.jpg = 95)

`@script`
shell Python, un endroit où vous pouvez saisir du code Python et voir immédiatement les résultats. Dans l'interface d'exercices de DataCamp, ce shell est intégré ici. Commençons par quelque chose de simple et utilisons Python comme calculatrice.


---

## Shell IPython

```yaml
type: FullSlide
key: 524e4c20a7
disable_transition: true
```

`@part1`
&nbsp;

![Calculs dans le shell IPython de DataCamp](https://assets.datacamp.com/img/translations/fr-FR/production/repositories/288/datasets/cee32b788a62e4b9a1234ccde56ac9ebb49cfa72/shelladdition.gif = 95)

`@script`
Permettez-moi de saisir 4 + 5, puis d'appuyer sur Entrée. Python interprète ce que vous avez saisi et affiche le résultat de votre calcul, 9. Le shell Python utilisé ici n'est en réalité pas l'original. Nous utilisons IPython, abréviation d’Interactive Python, qui est une version améliorée de Python standard qui nous sera utile plus tard.

IPython a été créé par Fernando Pérez et fait partie de l'écosystème Jupyter plus large. Outre le travail interactif avec Python, vous pouvez également exécuter Python dans ce que l'on appelle des


---

## Script Python

```yaml
type: FullSlide
key: 78ef256bc0
```

`@part1`
- Fichiers texte - `.py`{{1}}

- Liste des commandes Python{{2}}

- Similaire à la saisie dans le shell IPython{{3}}

![Script Python dans DataCamp](https://assets.datacamp.com/img/translations/fr-FR/production/repositories/288/datasets/59f196e96536543a4fb8801228019fc4106f3791/pyexercise_script.jpg = 78){{3}}

`@script`
scripts Python. Ces scripts Python sont de simples fichiers texte avec l'extension (point) py. Il s'agit essentiellement d'une liste de commandes Python qui sont exécutées, presque comme si vous tapiez vous-même les commandes dans le shell, ligne par ligne.


---

## Script Python

```yaml
type: FullSlide
key: 717d124175
disable_transition: true
```

`@part1`
![GIF : saisir 4 + 5 dans le script et cliquer sur « Soumettre la réponse ». Aucune sortie n'est affichée.](https://assets.datacamp.com/img/translations/fr-FR/production/repositories/288/datasets/2f96e979012e15329cc158d1e0f496aac3539f45/scriptnoprint.gif = 95)

`@script`
Intégrons maintenant la commande précédente dans un script, disponible ici dans l'interface DataCamp. L'étape suivante consiste à exécuter le script en cliquant sur « Soumettre la réponse ». Si vous exécutez ce script dans l'interface DataCamp, rien ne s'affiche dans le volet de sortie. C'est parce que vous devez explicitement utiliser print dans les scripts si vous souhaitez générer une sortie pendant l'exécution.


---

## Script Python

```yaml
type: FullSlide
key: c7a9d02fb6
disable_transition: true
code_zoom: 90
```

`@part1`
![python_script_print.gif](https://assets.datacamp.com/img/translations/fr-FR/production/repositories/288/datasets/8b13d046bb54dcb11aa49f0da7363781129d1561/scriptwithprint.gif = 95)

- Utilisez `print()` pour générer une sortie à partir du script

`@script`
Enveloppons notre calcul précédent dans un appel print, puis relançons le script. Cette fois-ci, le résultat obtenu est identique au précédent, c’est super ! En plaçant votre code dans des scripts Python plutôt que de retaper manuellement chaque étape de manière interactive, vous conserverez une structure claire et éviterez de tout retaper à chaque fois que vous souhaitez apporter une modification. Il vous suffira alors de modifier le script et de relancer l'ensemble du processus.


---

## Interface DataCamp

```yaml
type: FullSlide
key: 693ba1cd14
```

`@part1`
![Capture d'écran de l'interface DataCamp](https://assets.datacamp.com/img/translations/fr-FR/production/repositories/288/datasets/a9e8440bb8fbd49e4a73e4c36ef1cd677c0dd55f/pyexercise.png)

`@script`
Maintenant que vous avez une idée des différentes façons de travailler avec Python, je vous suggère de passer aux exercices. Utilisez le shell IPython pour vos essais et l'éditeur de script Python pour coder la réponse définitive. Si vous cliquez sur Soumettre la réponse, votre script sera exécuté et vérifié pour s'assurer que tout est correct.


---

## Passons à la pratique !

```yaml
type: FinalSlide
key: 7445cd202e
```

`@script`
Commencez à coder et n'oubliez pas de vous amuser !

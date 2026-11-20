---
title_meta: Capitolul 4
title: NumPy
description: >-
  NumPy este un pachet Python fundamental pentru practicarea eficientă a
  științei datelor. Învață să lucrezi cu instrumentele puternice ale array-ului
  NumPy și începe să explorezi date.
attachments:
  slides_link: 'https://projector-video-pdf-converter.datacamp.com/735/chapter4.pdf'
lessons:
  - nb_of_exercises: 5
    title: NumPy
  - nb_of_exercises: 5
    title: Array-uri NumPy 2D
  - nb_of_exercises: 3
    title: 'NumPy: Statistici de bază'
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

## Primul tău array NumPy

```yaml
type: NormalExercise
key: 84cab9d170
lang: python
xp: 100
skills:
  - 2
```

Acum vei pătrunde în lumea baseball-ului. Pe parcurs, te vei familiariza cu noțiunile de bază ale `numpy`, un pachet puternic pentru data science.

O listă numită `baseball` a fost deja definită în scriptul Python și reprezintă înălțimea unor jucători de baseball în centimetri. Poți adăuga cod pentru a crea un array `numpy` din ea?

`@instructions`
- Importă pachetul `numpy` ca `np`, astfel încât să îl poți referi prin `np`.
- Folosește `np.array()` pentru a crea un array `numpy` din `baseball`. Numește acest array `np_baseball`.
- Afișează tipul variabilei `np_baseball` pentru a verifica că totul este corect.

`@hint`
- `import numpy as np` face exact ce ai nevoie. De acum, folosește `np.fun_name()` ori de câte ori vrei să apelezi o funcție din `numpy`.
- `np.array()` ar trebui să primească `baseball` ca intrare. Atribuie rezultatul apelului funcției variabilei `np_baseball`.
- Pentru a afișa tipul unei variabile `x`, scrie pur și simplu `print(type(x))`.

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
predef_msg = "Nu trebuie să modificați sau să eliminați variabilele predefinite."
Ex().has_import("numpy")
Ex().check_correct(
  check_object("np_baseball"),
  multi(
    check_object("baseball", missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
    check_function("numpy.array").check_args(0).has_equal_ast()
  )
)

Ex().has_printout(0)
success_msg("Foarte bine!")
```

---

## Înălțimea jucătorilor de baseball

```yaml
type: NormalExercise
key: e7e25a89ea
lang: python
xp: 100
skills:
  - 2
```

Ești un mare fan al baseballului. Decizi să contactezi MLB (Major League Baseball) și să ceri mai multe statistici despre înălțimea jucătorilor principali. Primești date despre mai mult de o mie de jucători, stocate ca o listă Python obișnuită: `height_in`. Înălțimea este exprimată în inch-uri. Poți crea un array `numpy` din aceasta și să convertești unitățile în metri?

`height_in` este deja disponibilă, iar pachetul `numpy` este încărcat, deci poți începe imediat (Sursă: stat.ucla.edu).

`@instructions`
- Creează un array `numpy` din `height_in`. Numește noul array `np_height_in`.
- Afișează `np_height_in`.
- Înmulțește `np_height_in` cu `0.0254` pentru a converti toate măsurătorile de înălțime din inch-uri în metri. Stochează noile valori într-un array nou, `np_height_m`.
- Afișează `np_height_m` și verifică dacă rezultatul are sens.

`@hint`
- Folosește `np.array()` și transmite-i `height`. Stochează rezultatul în `np_height_in`.
- Pentru a afișa o variabilă `x`, scrie `print(x)` în scriptul Python.
- Efectuează calculele ca și cum `np_height_in` ar fi un număr simplu: `np_height_in * conversion_factor` face parte din răspuns.
- Pentru a afișa o variabilă `x`, scrie `print(x)` în scriptul Python.

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
  check_object("np_height_m").has_equal_value(incorrect_msg = "Utilizați `np_height_in * 0.0254` pentru a calcula `np_height_m`.")
)

success_msg("Excelent! Într-o clipită, `numpy` efectuează înmulțiri pe mai mult de 1000 de măsurători de înălțime.")
```

---

## Efecte secundare ale NumPy

```yaml
type: MultipleChoiceExercise
key: 3662ff6637
lang: python
xp: 50
skills:
  - 2
```

`numpy` este excelent pentru operații aritmetice pe vectori. Totuși, dacă îl compari cu listele obișnuite din Python, vei observa câteva diferențe importante.

În primul rând, array-urile `numpy` nu pot conține elemente de tipuri diferite. Dacă amesteci tipuri, cum ar fi valori booleene și numere întregi, `numpy` le convertește automat la un tip comun. Valorile booleene `True` și `False` sunt tratate ca `1`, respectiv `0` atunci când sunt combinate cu numere, astfel că array-ul ajunge să conțină numere întregi.

În al doilea rând, operatorii aritmetici obișnuiți, precum `+`, `-`, `*` și `/`, au o semnificație diferită pentru listele Python și pentru array-urile `numpy`.

Selectează codul care produce același rezultat ca:

```
np.array([True, 1, 2]) + np.array([3, 4, False])
```

Biblioteca `numpy` este deja importată ca `np`. Poți rula fiecare opțiune în Shell-ul IPython pentru a vedea rezultatul.

`@possible_answers`
- `np.array([True, 1, 2, 3, 4, False])`
- `np.array([4, 3, 0]) + np.array([0, 2, 2])`
- `np.array([1, 1, 2]) + np.array([3, 4, -1])`
- `np.array([0, 1, 2, 3, 4, 5])`

`@hint`
- Copiază fragmentele de cod și inserează-le în Shell-ul IPython. Apasă **Enter** pentru a rula codul și vezi care rezultat corespunde celui generat de `np.array([True, 1, 2]) + np.array([3, 4, False])`.

`@pre_exercise_code`
```{python}
import numpy as np
```

`@sct`
```{python}
msg1 = msg3 = msg4 = "Incorect. Încercați diferitele fragmente de cod și vedeți care dintre ele corespunde fragmentului de cod țintă."
msg2 = "Foarte bine! `True` este convertit în 1, `False` este convertit în 0."
Ex().has_chosen(2, [msg1, msg2, msg3, msg4])
```

---

## Subsetarea array-urilor NumPy

```yaml
type: NormalExercise
key: fcb2a9007b
lang: python
xp: 100
skills:
  - 2
```

Subsetarea (folosind notația cu paranteze pătrate pe liste sau array-uri) funcționează exact la fel atât pentru liste, cât și pentru array-uri.

Acest exercițiu are deja două liste, `height_in` și `weight_lb`, încărcate în fundal. Acestea conțin înălțimea și greutatea jucătorilor MLB ca liste obișnuite. De asemenea, sunt pregătite două array-uri `numpy`, `np_weight_lb` și `np_height_in`.

`@instructions`
- Subsetează `np_weight_lb` afișând elementul de la indexul 50.
- Afișează un sub-array din `np_height_in` care conține elementele de la indexul 100 până la indexul 110 **inclusiv**.

`@hint`
- Asigură-te că încadrezi operațiile de subsetare într-un apel `print()`.
- Folosește `[100:111]` pentru a obține elementele de la indexul 100 până la indexul 110 inclusiv.

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
msg = "Nu trebuie să modificați sau să eliminați variabilele predefinite."
Ex().multi(
    check_object("np_height_in", missing_msg=msg).has_equal_value(incorrect_msg = msg),
    check_object("np_weight_lb", missing_msg=msg).has_equal_value(incorrect_msg = msg)
)

Ex().has_printout(0)
Ex().has_printout(1)

success_msg("Excelent! Este timpul să învățați ceva nou: array-uri NumPy 2D!")
```

---

## Array-uri NumPy 2D

```yaml
type: VideoExercise
key: 1241efac7a
xp: 50
```

`@projector_key`
ae3238dcc7feb9adecfee0c395fc8dc8

---

## Primul tău array NumPy 2D

```yaml
type: NormalExercise
key: 5cb045bb13
lang: python
xp: 100
skills:
  - 2
```

Înainte de a lucra cu datele reale din MLB, hai să creăm un array 2D `numpy` dintr-o listă mică de liste.

În acest exercițiu, `baseball` este o listă de liste. Lista principală conține 4 elemente. Fiecare dintre aceste elemente este o listă cu înălțimea și greutatea a 4 jucători de baseball, în această ordine. `baseball` este deja definit în script.

`@instructions`
- Folosește `np.array()` pentru a crea un array 2D `numpy` din `baseball`. Numește-l `np_baseball`.
- Afișează tipul lui `np_baseball`.
- Afișează atributul `shape` al lui `np_baseball`. Folosește `np_baseball.shape`.

`@hint`
- `baseball` este deja definit în script. Apelează `np.array()` pe el și stochează array-ul 2D `numpy` rezultat în `np_baseball`.
- Folosește `print()` împreună cu `type()` pentru a doua instrucțiune.
- `np_baseball.shape` îți va oferi dimensiunile lui `np_baseball`. Asigură-te că îl încadrezi într-un apel `print()`.

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
msg = "Nu trebuie să modificați sau să eliminați variabilele predefinite."
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

success_msg("Excelent! Acum sunteți pregătit să convertiți datele reale MLB într-un array `numpy` 2D!")
```

---

## Date de baseball în format 2D

```yaml
type: NormalExercise
key: 5df25d0b7b
lang: python
xp: 100
skills:
  - 2
```

Îți dai seama că are mai mult sens să restructurezi toate aceste informații într-un array 2D `numpy`.

Ai o listă de liste în Python. În această listă de liste, fiecare sublista reprezintă înălțimea și greutatea unui singur jucător de baseball. Numele acestei liste este `baseball` și a fost deja încărcată pentru tine (chiar dacă nu o poți vedea).

Stochează datele ca un array 2D pentru a debloca funcționalitățile suplimentare ale `numpy`.

`@instructions`
- Folosește `np.array()` pentru a crea un array 2D `numpy` din `baseball`. Numește-l `np_baseball`.
- Afișează atributul `shape` al lui `np_baseball`.

`@hint`
- `baseball` este deja disponibil în mediul Python. Apelează `np.array()` pe acesta și stochează array-ul 2D `numpy` rezultat în `np_baseball`.
- `np_baseball.shape` îți va oferi dimensiunile lui `np_baseball`. Asigură-te că adaugi un apel `print()` în jurul acestuia.

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

success_msg("Excelent! Este timpul să prezentați câteva caracteristici remarcabile ale array-urilor `numpy` multidimensionale!")
```

---

## Subsetting în array-uri NumPy 2D

```yaml
type: NormalExercise
key: aeca4977f0
lang: python
xp: 100
skills:
  - 2
```

Dacă array-ul tău `numpy` 2D are o structură regulată, adică fiecare rând și coloană are un număr fix de valori, metodele de subsetting devin foarte simple. Uită-te la codul de mai jos, unde elementele `"a"` și `"c"` sunt extrase dintr-o listă de liste.

```
# numpy
import numpy as np
np_x = np.array(x)
np_x[:, 0]
```

Indexurile dinaintea virgulei se referă la rânduri, iar cele de după virgulă se referă la coloane. `:` este folosit pentru slicing; în acest exemplu, îi spune lui Python să includă toate rândurile.

`@instructions`
- Afișează rândul 50 din `np_baseball`.
- Creează o variabilă nouă, `np_weight_lb`, care să conțină întreaga a doua coloană din `np_baseball`.
- Selectează înălțimea (prima coloană) a celui de-al 124-lea jucător de baseball din `np_baseball` și afișeaz-o.

`@hint`
- La prima instrucțiune, ai nevoie de rândul cu indexul 49! Mai exact, vei folosi `[49, :]`.
- Pentru a selecta întreaga a doua coloană, folosește `[:, 1]`.
- Pentru ultima instrucțiune, folosește `[123, 0]`; nu uita să incluzi totul într-un `print()`.

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
msg = "Nu trebuie să modificați sau să eliminați variabilele predefinite."
Ex().multi(
    has_import("numpy", same_as = False),
    check_object("np_baseball", missing_msg=msg).has_equal_value(incorrect_msg = msg)
)

Ex().has_printout(0)

Ex().check_object('np_weight_lb').has_equal_value(incorrect_msg = "Puteți utiliza `np_baseball[:,1]` pentru a defini `np_weight_lb`. Aceasta va selecta întreaga primă coloană.")

Ex().has_printout(1)

success_msg("Merge bine!")
```

---

## Aritmetică 2D

```yaml
type: NormalExercise
key: 1c2378b677
lang: python
xp: 100
skills:
  - 2
```

Array-urile `numpy` 2D pot efectua calcule element cu element, la fel ca array-urile `numpy` obișnuite.

`np_baseball` este deja definit pentru tine; este din nou un array `numpy` 2D cu 3 coloane reprezentând înălțimea (în inci), greutatea (în livre) și vârsta (în ani). `baseball` este disponibil ca o listă de liste Python obișnuită, iar `updated` este disponibil ca un array numpy 2D.

`@instructions`
- Ai reușit să obții datele despre modificările de înălțime, greutate și vârstă ale tuturor jucătorilor de baseball. Acestea sunt disponibile ca un array `numpy` 2D numit `updated`. Adună `np_baseball` și `updated`, apoi afișează rezultatul.
- Vrei să convertești unitățile de înălțime și greutate la sistemul metric (metri și respectiv kilograme). Ca prim pas, creează un array `numpy` cu trei valori: `0.0254`, `0.453592` și `1`. Numește acest array `conversion`.
- Înmulțește `np_baseball` cu `conversion` și afișează rezultatul.

`@hint`
- `np_baseball + updated` va efectua o sumă element cu element a celor două array-uri `numpy`.
- Creează un array `numpy` cu `np.array()`; argumentul de intrare este o listă Python obișnuită cu trei elemente.
- `np_baseball * conversion` va funcționa fără pași suplimentari. Încearcă! Asigură-te că înveți rezultatul într-un apel `print()`.

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

msg = "Nu trebuie să modificați sau să eliminați variabilele predefinite."
Ex().check_object("np_baseball", missing_msg=msg).has_equal_value(incorrect_msg = msg)

Ex().has_printout(0)

Ex().check_correct(
    has_printout(1),
    check_correct(
        check_object('conversion').has_equal_value(),
        check_function('numpy.array', index = 1).check_args(0).has_equal_value()
    )    
)

success_msg("Excelent! Observați cum, cu foarte puțin cod, puteți modifica toate valorile din structura de date `numpy` într-un mod foarte specific. Acest lucru vă va fi foarte util în viitorul dumneavoastră ca om de știință al datelor!")
```

---

## NumPy: Statistici de bază

```yaml
type: VideoExercise
key: 287995e488
xp: 50
```

`@projector_key`
34495ba457d74296794d2a122c9b6e19

---

## Medie versus mediană

```yaml
type: NormalExercise
key: 509c588eb6
lang: python
xp: 100
skills:
  - 2
```

Acum știi cum să folosești funcțiile `numpy` pentru a înțelege mai bine datele tale.

Datele despre baseball sunt disponibile ca un array `numpy` 2D cu 3 coloane (înălțime, greutate, vârstă) și 1015 rânduri. Numele acestui array `numpy` este `np_baseball`. După restructurarea datelor, observi că unele valori ale înălțimii sunt neobișnuit de mari. Urmează instrucțiunile și descoperă care statistică descriptivă este cea mai potrivită atunci când lucrezi cu așa-numiții _outliers_. `np_baseball` este disponibil.

`@instructions`
- Creează array-ul `numpy` `np_height_in` egal cu prima coloană din `np_baseball`.
- Afișează media valorilor din `np_height_in`.
- Afișează mediana valorilor din `np_height_in`.

`@hint`
- Folosește subsetting 2D cu `numpy`: `[:,0]` face parte din soluție.
- Dacă `numpy` este importat ca `np`, poți folosi `np.mean()` pentru a calcula media unui array NumPy. Nu uita să adaugi și un apel `print()`.
- Pentru ultima instrucțiune, folosește `np.median()`.

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

Ex().check_object("np_height_in").has_equal_value(incorrect_msg = "Puteți utiliza `np_baseball[:,0]` pentru a selecta prima coloană din `np_baseball`"),

Ex().check_correct(
    has_printout(0),
    check_function('numpy.mean').has_equal_value()
)

Ex().check_correct(
    has_printout(1),
    check_function('numpy.median').has_equal_value()
)

success_msg("O înălțime medie de 1586 de inci — asta nu sună corect, nu-i așa? Cu toate acestea, mediana nu pare să fie afectată de valorile extreme: 74 de inci pare perfect rezonabil. Este întotdeauna o idee bună să verificați atât mediana, cât și media, pentru a obține o imagine de ansamblu asupra distribuției întregului set de date.")
```

---

## Explorează datele despre baseball

```yaml
type: NormalExercise
key: '4409948807'
lang: python
xp: 100
skills:
  - 2
```

Deoarece media și mediana sunt atât de diferite, decizi să depui o reclamație la MLB. Aceștia descoperă eroarea și îți trimit datele corectate. Ele sunt din nou disponibile ca un array NumPy 2D numit `np_baseball`, cu trei coloane.

Scriptul Python din editor conține deja cod care afișează mesaje informative cu diferitele statistici sumare, iar `numpy` este deja importat ca `np`. Poți finaliza exercițiul? `np_baseball` este disponibil.

`@instructions`
- Codul pentru afișarea înălțimii medii este deja inclus. Completează codul pentru calcularea medianaei înălțimii.
- Folosește `np.std()` pe prima coloană din `np_baseball` pentru a calcula `stddev`.
- Jucătorii mai înalți tind să fie și mai grei? Folosește `np.corrcoef()` pentru a stoca corelația dintre prima și a doua coloană din `np_baseball` în `corr`.

`@hint`
- Folosește `np.median()` pentru a calcula mediana. Asigură-te că selectezi mai întâi coloana corectă!
- Selectează aceeași coloană când calculezi deviația standard cu `np.std()`.
- Folosește `np_baseball[:, 0]` și `np_baseball[:, 1]` pentru a selecta prima și a doua coloană; acestea sunt argumentele pentru `np.corrcoef()`.

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
msg = "Nu ar trebui să modificați sau să eliminați variabila predefinită `avg`."
Ex().check_object("avg", missing_msg=msg).has_equal_value(incorrect_msg=msg)

missing = "Ați folosit `np.median()` pentru a calcula mediana?"
incorrect = "Pentru a calcula `med`, transmiteți prima coloană a `np_baseball` către `numpy.median()`. Exemplul cu `np.mean()` arată cum se procedează."
Ex().check_correct(
  check_object("med").has_equal_value(),
  check_function("numpy.median", index=0, missing_msg=missing).check_args(0).has_equal_value(incorrect_msg=incorrect)
)

missing = "Ați folosit `np.std()` pentru a calcula abaterea standard?"
incorrect = "Pentru a calcula `stddev`, transmiteți prima coloană a `np_baseball` către `numpy.std()`. Exemplul cu `np.mean()` arată cum se procedează."
Ex().check_correct(
  check_object("stddev").has_equal_value(),
  check_function("numpy.std", index=0, missing_msg=missing).check_args(0).has_equal_value(incorrect_msg=incorrect)
)

missing = "Ați folosit `np.corrcoef()` pentru a calcula corelația?"
incorrect1 = "Pentru a calcula `corr`, primul argument al funcției `np.corrcoef()` ar trebui să fie prima coloană a `np_baseball`, similar cu modul în care ați procedat anterior."
incorrect2 = "Pentru a calcula `corr`, al doilea argument al funcției `np.corrcoef()` ar trebui să fie a doua coloană a `np_baseball`. În loc de `[:,0]`, utilizați `[:,1]` de această dată."
Ex().check_correct(
  check_object("corr").has_equal_value(),
  check_function("numpy.corrcoef", index=0, missing_msg=missing).multi(
    check_args(0, missing_msg=incorrect1).has_equal_value(incorrect_msg=incorrect1),
    check_args(1, missing_msg=incorrect2).has_equal_value(incorrect_msg=incorrect2)
  )
)

success_msg("Excelent! Ați construit o bază solidă - acum este momentul să utilizați toate noile dumneavoastră competențe de știința datelor pentru a rezolva mai multe provocări și a avea un impact.")
```

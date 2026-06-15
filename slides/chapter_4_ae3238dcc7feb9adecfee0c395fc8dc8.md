---
title: Insert title here
key: ae3238dcc7feb9adecfee0c395fc8dc8
video_link:
  mp3: >-
    https://videos.datacamp.com/mp3/translations/course_735/ro-RO/b5145237-faed-4d3a-aaa0-12c66af67ad8-40deac584fe5f3581f7eb2aa1b2c3b1e.mp3
---

## Array-uri NumPy 2D

```yaml
type: TitleSlide
key: 0cc8abf493
```

`@lower_third`
name: Hugo Bowne-Anderson
title: Data Scientist at DataCamp

`@script`
Felicitări! Hai să recreăm acum array-urile numpy din videoclipul anterior.

---

## Tipul array-urilor NumPy

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
Dacă verifici tipul acestor array-uri, Python îți spune că sunt numpy.ndarray. Partea cu numpy punct îți arată că este un tip definit în pachetul numpy. ndarray vine de la „array n-dimensional". Array-urile np_height și np_weight sunt unidimensionale, dar poți crea fără probleme array-uri cu 2, 3 sau chiar 7 dimensiuni. În videoclipul acesta ne oprim la 2 dimensiuni.

---

## Array-uri NumPy 2D

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
Poți crea un array numpy 2D dintr-o listă de liste obișnuită în Python. Hai să creăm un singur array numpy pentru toate datele de înălțime și greutate ale familiei tale, ca în exemplul de față.

Dacă afișezi np_2d, vei vedea că are o structură dreptunghiulară. Fiecare sublista din lista inițială corespunde unui rând în array-ul numpy 2D. Din np_2d.shape poți vedea că avem 2 rânduri și 5 coloane. shape este un atribut al array-ului np_2d și îți oferă informații despre structura datelor.

Reținem că sintaxa pentru accesarea unui atribut seamănă cu apelarea unei metode, dar nu sunt același lucru. Metodele au paranteze rotunde după ele, pe când atributele nu au.

Și pentru array-urile 2D se aplică regula numpy: un array poate conține un singur tip de date. Dacă schimbi un număr zecimal într-un șir de caractere, toate elementele array-ului vor fi convertite la șiruri de caractere, pentru a păstra un array omogen.

---

## Subsetting

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
Poți vedea array-ul numpy 2D ca pe o versiune îmbunătățită a listei de liste. Poți face calcule pe array-uri, cum am arătat anterior, și poți folosi metode mai avansate de selecție.

Să spunem că vrei primul rând și apoi al treilea element din acel rând. Pentru a selecta rândul, folosești indexul 0 între paranteze pătrate. Nu uita de indexarea care începe de la zero.

Pentru a selecta al treilea element, poți extinde același apel cu o altă pereche de paranteze pătrate, de data aceasta cu indexul 2.

---

## Subsetting

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
Practic, selectezi mai întâi rândul, apoi faci o altă selecție din acel rând.

Există și o metodă alternativă de selecție, folosind o singură pereche de paranteze pătrate și o virgulă. Acest apel returnează exact aceeași valoare ca înainte. Valoarea dinaintea virgulei specifică rândul, iar valoarea de după virgulă specifică coloana. Se returnează intersecția dintre rândurile și coloanele specificate. Odată ce te obișnuiești cu ea, această sintaxă este mai intuitivă și oferă mai multe posibilități.

---

## Subsetting

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
Să spunem că vrei să selectezi înălțimea și greutatea celui de-al doilea și celui de-al treilea membru al familiei. Vrei ambele rânduri, așa că pui două puncte înaintea virgulei. Vrei doar coloanele 2 și 3, deci pui indicii de la 1 la 3 după virgulă. Ține minte că al treilea index nu este inclus. Intersecția ne dă un array 2D cu 2 rânduri și 2 coloane.

Similar, poți selecta greutatea tuturor membrilor familiei astfel: vrei doar al doilea rând, deci pui 1 înaintea virgulei. Vrei toate coloanele, deci folosești două puncte după virgulă. Intersecția ne dă întregul al doilea rând.

În plus, array-urile numpy 2D îți permit să faci calcule element cu element, la fel cum ai făcut cu array-urile numpy 1D. Asta este ceva

---

## Să exersăm!

```yaml
type: FinalSlide
key: 6047b27c09
```

`@script`
cu care poți experimenta în exerciții, alături de crearea și selecția în array-uri numpy 2D. Mult succes!

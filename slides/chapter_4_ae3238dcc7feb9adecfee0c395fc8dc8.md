---
title: Insert title here
key: ae3238dcc7feb9adecfee0c395fc8dc8
video_link:
  mp3: >-
    https://videos.datacamp.com/mp3/translations/course_735/cs-CZ/f7731d9e-2d4e-4207-820c-e5c748258dfa-e7f60d1f836541b17cd7f2af335dfef0.mp3
---

## 2D NumPy pole

```yaml
type: TitleSlide
key: 0cc8abf493
```

`@lower_third`
name: Hugo Bowne-Anderson
title: Data Scientist at DataCamp

`@script`
Skvělá práce! Pojďme teď znovu vytvořit numpy pole z předchozího videa.

---

## Typ NumPy polí

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
Když se zeptáš na typ těchto polí, Python ti odpoví, že se jedná o numpy.ndarray. Numpy dot ti říká, že jde o typ definovaný v balíčku numpy. ndarray znamená n-rozměrné pole. Pole np_height a np_weight jsou jednorozměrná, ale klidně můžeš vytvořit dvourozměrná, trojrozměrná, nebo dokonce sedmirozměrná pole! V tomto videu se ale zaměříme na dvourozměrná.

---

## 2D NumPy pole

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
Dvourozměrné numpy pole můžeš vytvořit z běžného Python seznamu seznamů. Zkusme vytvořit jedno numpy pole pro všechna data o výšce a váze členů tvé rodiny, takhle.

Pokud teď vypíšeš np_2d, uvidíš, že má obdélníkovou strukturu: každý podseznam odpovídá jednomu řádku dvourozměrného numpy pole. Z np_2d.shape zjistíš, že máme skutečně 2 řádky a 5 sloupců. shape je takzvaný atribut pole np_2d, který ti poskytne více informací o tom, jak datová struktura vypadá.

Všimni si, že syntaxe pro přístup k atributu vypadá trochu jako volání metody, ale není to totéž! Metody mají za sebou kulaté závorky, a jak vidíš, atributy je nemají.

Pro dvourozměrná pole platí stejné pravidlo NumPy: pole může obsahovat pouze jeden datový typ. Pokud změníš jedno desetinné číslo na řetězec, všechny prvky pole se převedou na řetězce, aby pole zůstalo homogenní.

---

## Podsekce

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
Dvourozměrné numpy pole si můžeš představit jako vylepšený seznam seznamů: můžeš provádět výpočty s poli, jak jsem ukázal dříve, a máš k dispozici pokročilejší způsoby výběru prvků.

Řekněme, že chceš první řádek a z něj třetí prvek. K výběru řádku použiješ index 0 v hranatých závorkách. Nezapomeň na indexování od nuly.

Pro výběr třetího prvku pak rozšíříš stejný zápis o další pár hranatých závorek, tentokrát s indexem 2.

---

## Podsekce

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
takhle. V podstatě vyberéš řádek a z něj pak provedéš další výběr.

Existuje také alternativní způsob výběru pomocí jednoduchých hranatých závorek s čárkou. Tento zápis vrátí úplně stejnou hodnotu jako předchozí. Hodnota před čárkou určuje řádek, hodnota za čárkou určuje sloupec. Výsledkem je průsečík zadaných řádků a sloupců. Jakmile si na tento způsob zvykneš, připadne ti přirozenější a otevírá více možností.

---

## Podsekce

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
Řekněme, že chceš vybrat výšku a váhu druhého a třetího člena rodiny. Chceš oba řádky, takže před čárku napíšeš dvojtečku. Chceš pouze druhý a třetí sloupec, takže za čárku napíšeš indexy 1 až 3. Pamatuj, že třetí index už není zahrnutý. Průsečík nám vrátí dvourozměrné pole se 2 řádky a 2 sloupci.

Podobně můžeš vybrat váhu všech členů rodiny takto: chceš pouze druhý řádek, takže před čárku napíšeš 1. Chceš všechny sloupce, takže za čárku napíšeš dvojtečku. Průsečík nám vrátí celý druhý řádek.

A konečně, dvourozměrná numpy pole ti umožňují provádět výpočty po prvcích, stejně jako jednorozměrná numpy pole. To je něco,

---

## Pojďme procvičovat!

```yaml
type: FinalSlide
key: 6047b27c09
```

`@script`
co si můžeš vyzkoušet v cvičeních, spolu s vytvářením a výběrem prvků z dvourozměrných numpy polí. Těš se!

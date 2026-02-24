---
title: Insert title here
key: ae3238dcc7feb9adecfee0c395fc8dc8
video_link:
  mp3: >-
    https://videos.datacamp.com/mp3/translations/course_735/tr-TR/dbe63afc-ede3-4b1c-a84e-22e61f22db50.mp3
---

## 2D NumPy Dizileri

```yaml
type: TitleSlide
key: 0cc8abf493
```

`@lower_third`
name: Hugo Bowne-Anderson
title: Data Scientist at DataCamp

`@script`
Aferin, harikasın! Şimdi önceki videodaki numpy dizilerini yeniden oluşturalım.

---

## NumPy Dizilerinin Türü

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
Bu dizilerin türünü sorarsan, Python bunların numpy.ndarray olduğunu söyler. numpy nokta, bunun numpy paketinde tanımlanmış bir tür olduğunu gösterir. ndarray, n-boyutlu dizi demektir. np_height ve np_weight dizileri tek boyutludur, ama iki boyutlu, üç boyutlu, hatta yedi boyutlu diziler oluşturmak da gayet mümkün! Yine de bu videoda iki boyutta kalalım.

---

## 2D NumPy Dizileri

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
(2, 5) # 2 satır, 5 sütun
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
Normal bir Python iç içe liste yapısından iki boyutlu bir numpy dizisi oluşturabilirsin. Ailenin tüm boy ve kilo verileri için tek bir numpy dizisi oluşturmaya çalışalım, şöyle.

Şimdi np_2d’yi yazdırırsan, dikdörtgen bir veri yapısı olduğunu görürsün: Listedeki her alt liste, iki boyutlu numpy dizisinde bir satıra karşılık gelir. np_2d.shape’e bakınca gerçekten iki satır ve beş sütun olduğunu görürsün. shape, np_2d dizisinin bir özniteliğidir; veri yapısının nasıl göründüğüne dair daha çok bilgi verir.

Bir özniteliğe erişme söz diziminin, bir yöntemi çağırmaya benzediğine dikkat et, ama aynı şey değiller! Yöntemlerin ardından parantez gelir; burada gördüğün gibi, özniteliklerde yoktur.

Ayrıca iki boyutlu diziler için de NumPy kuralı geçerli: Bir dizi yalnızca tek bir tür içerebilir. Bir kayan sayıyı metne çevirirsen, dizideki tüm öğeler de metne dönüştürülür ve homojen bir dizi elde edilir.

---

## Alt Kümeleme

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
İki boyutlu numpy dizisini, geliştirilmiş bir iç içe liste gibi düşünebilirsin: Üzerinde hesaplamalar yapabilirsin, az önce gösterdiğim gibi, ve daha gelişmiş alt kümeleme yolları kullanabilirsin.

Diyelim ki ilk satırı ve o satırdaki üçüncü öğeyi istiyorsun. Satırı seçmek için köşeli parantez içinde sıfır indeksine ihtiyacın var. Sıfırdan başlayan indekslemeyi unutma.

Üçüncü öğeyi seçmek için aynı çağrıyı bir köşeli parantez daha ekleyerek genişletebilirsin; bu kez indeks ikiyle,

---

## Alt Kümeleme

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
şu şekilde. Temelde önce satırı seçiyorsun, sonra o satırdan bir seçim daha yapıyorsun.

Tek köşeli parantez ve virgül kullanarak alternatif bir alt kümeleme yolu da var. Bu çağrı, az öncekiyle tam olarak aynı değeri döndürür. Virgülden önceki değer satırı, virgülden sonraki değer sütunu belirtir. Belirttiğin satır ve sütunların kesişimi döner. Alışınca bu söz dizimi daha sezgisel gelir ve daha çok imkan sunar.

---

## Alt Kümeleme

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
Diyelim ki ikinci ve üçüncü aile üyesinin boy ve kilosunu seçmek istiyorsun. Her iki satırı da istiyorsun, bu yüzden virgülden önce iki nokta koy. Yalnızca ikinci ve üçüncü sütunu istiyorsun, bu nedenle virgülden sonra birden üçe kadar olan indeksleri yaz. Burada üçüncü indeksin dahil edilmediğini hatırla. Kesişim bize iki satır ve iki sütunlu bir iki boyutlu dizi verir:

Benzer şekilde, tüm aile üyelerinin kilosunu şöyle seçebilirsin: Yalnızca ikinci satırı istiyorsun, o yüzden virgülden önce bire koy. Tüm sütunları istiyorsun, bu yüzden virgülden sonra iki nokta kullan. Kesişim, tüm ikinci satırı verir.

Son olarak, iki boyutlu numpy dizileri, tıpkı tek boyutlu dizilerde yaptığın gibi, öğe bazında hesaplamalar yapmana imkan tanır. Bu da

---

## Hadi pratik yapalım!

```yaml
type: FinalSlide
key: 6047b27c09
```

`@script`
egzersizlerde deneyebileceğin bir şey; iki boyutlu numpy dizileri oluşturmayı ve alt kümeler oluşturmayı da dene! Heyecan verici

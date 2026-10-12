---
title_meta: Bölüm 4
title: NumPy
description: >-
  NumPy, veri bilimini verimli bir şekilde uygulamayı sağlayan temel bir Python
  paketidir. NumPy dizisinde güçlü araçlarla çalışmayı öğrenin ve veri keşfine
  başlayın.
attachments:
  slides_link: 'https://projector-video-pdf-converter.datacamp.com/735/chapter4.pdf'
lessons:
  - nb_of_exercises: 5
    title: Numpy
  - nb_of_exercises: 5
    title: 2D Numpy Dizileri
  - nb_of_exercises: 3
    title: 'Numpy: Temel İstatistikler'
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

## İlk NumPy Diziniz

```yaml
type: NormalExercise
key: 84cab9d170
lang: python
xp: 100
skills:
  - 2
```

Şimdi beyzbol dünyasına dalacaksınız. Bu süreçte, veri bilimini uygulamak için güçlü bir paket olan `numpy` hakkında temel bilgiler edineceksiniz.

Python kodunda, bazı beyzbol oyuncularının boylarını santimetre cinsinden gösteren `baseball` adlı bir liste zaten tanımlanmıştır. Bu koddan bir `numpy` dizisi oluşturmak için kod ekleyebilir misiniz?

`@instructions`
- `numpy` paketini `np` olarak içe aktarın, böylece `np`, `numpy` referansı olur.
- `np.array()` fonksiyonunu kullanarak `baseball` tablosundan bir `numpy` dizisi oluşturun. Bu diziye `np_baseball` adını verin.
- `np_baseball` türünü yazdırarak doğru olup olmadığını kontrol edin.

`@hint`
- `import numpy as np` işe yarayacaktır. Şimdi `numpy` fonksiyonunu her kullanmak istediğinizde `np.fun_name()` kullanmanız gerekiyor.
- `np.array()`, `baseball` girdisini almalıdır. Fonksiyon çağrısının sonucunu `np_baseball` tablosuna atayın.
- Bir `x` değişkeninin türünü yazdırmak için `print(type(x))` yazmanız yeterlidir.

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
predef_msg = "Önceden tanımlanmış değişkenleri değiştirmenize veya kaldırmanıza gerek yok."
Ex().has_import("numpy")
Ex().check_correct(
  check_object("np_baseball"),
  multi(
    check_object("baseball", missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
    check_function("numpy.array").check_args(0).has_equal_ast()
  )
)

Ex().has_printout(0)
success_msg("Harika iş!")
```

---

## Beyzbol oyuncularının boyları

```yaml
type: NormalExercise
key: e7e25a89ea
lang: python
xp: 100
skills:
  - 2
```

Büyük bir beyzbol fanatiğisiniz. MLB'yi (Major League Baseball) arayıp önemli oyuncuların boyları hakkında daha fazla istatistik istemeye karar veriyorsunuz. Size binlerce oyuncuya ait verileri aktarıyorlar. Bu veriler normal bir Python listesi olarak depolanmış: `height_in`. Boy inç cinsinden ifade ediliyor. Bundan bir `numpy` dizisi oluşturup birimleri metreye dönüştürebilir misiniz?

`height_in` zaten mevcuttur ve `numpy` paketi yüklenmiştir, bu nedenle hemen başlayabilirsiniz (Kaynak: stat.ucla.edu).

`@instructions`
- `height_in` listesinden bir `numpy` dizisi oluşturun. Bu yeni diziye `np_height_in` adını verin.
- `np_height_in` dizisini yazdırın.
- `np_height_in` değerini `0.0254` ile çarpın, tüm boy ölçülerini inçten metreye dönüştürün. Yeni değerleri `np_height_m` adlı yeni bir diziye kaydedin.
- `np_height_m` sonucunu yazdırın ve çıktının mantıklı olup olmadığını kontrol edin.

`@hint`
- `np.array()` fonksiyonunu kullanın ve `height` listesine aktarın. Sonucu `np_height_in` listesine kaydedin.
- Bir `x` değişkeni yazdırmak için Python koduna `print(x)` yazın.
- Hesaplamaları `np_height_in` tek bir sayıymış gibi yapın: `np_height_in * conversion_factor` yanıtın bir parçasıdır.
- Bir `x` değişkeni yazdırmak için Python koduna `print(x)` yazın.

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
  check_object("np_height_m").has_equal_value(incorrect_msg = "`np_height_m`'yi hesaplamak için `np_height_in * 0.0254` kullanın.")
)

success_msg("Güzel! Göz açıp kapayıncaya kadar, `numpy` 1000'den fazla yükseklik ölçümünde çarpma işlemi gerçekleştirir.")
```

---

## NumPy Yan Etkileri

```yaml
type: MultipleChoiceExercise
key: 3662ff6637
lang: python
xp: 50
skills:
  - 2
```

`numpy` vektör aritmetiği yapmak için harikadır. Ancak, işlevselliğini normal Python listeleriyle karşılaştırırsanız, bazı farklılıklar göze çarpar.

İlk olarak,`numpy`  diziler farklı türdeki öğeleri içeremez. Boolean ve tamsayı gibi türleri karıştırırsanız, bunları otomatik olarak ortak bir türe`numpy` dönüştürür. Boole değerleri`True`  ve  sayılarla `False``0`birleştirildiğinde  ve  `1`olarak değerlendirilir, bu nedenle dizi tamsayılar olarak sonuçlanır.

İkincisi `+`, `-`, `*` ve `/` gibi tipik aritmetik işleçler, normal Python listeleri ve `numpy` dizileri için farklı anlamlara sahiptir.

Aşağıdaki çıktıyı veren kodu seçin:

```
np.array([True, 1, 2]) + np.array([3, 4, False])
```

`numpy` paketi, `np` olarak zaten içe aktarılmıştır. IPython Shell'de her bir seçeneği çalıştırarak çıktıyı görebilirsiniz.

`@possible_answers`
- `np.array([True, 1, 2, 3, 4, False])`
- `np.array([4, 3, 0]) + np.array([0, 2, 2])`
- `np.array([1, 1, 2]) + np.array([3, 4, -1])`
- `np.array([0, 1, 2, 3, 4, 5])`

`@hint`
- Farklı kod öbeklerini kopyalayın ve IPython Shell'e yapıştırın. **Enter** tuşuna basarak kodu çalıştırın ve `np.array([True, 1, 2]) + np.array([3, 4, False])` tarafından oluşturulan çıktı ile hangi çıktının eşleştiğine bakın.

`@pre_exercise_code`
```{python}
import numpy as np
```

`@sct`
```{python}
msg1 = msg3 = msg4 = "Yanlış. Farklı kod parçalarını deneyin ve hangisinin hedef kod parçasıyla eşleştiğini görün."
msg2 = "Harika iş! `True` 1'e, `False` 0'a dönüştürülür."
Ex().has_chosen(2, [msg1, msg2, msg3, msg4])
```

---

## NumPy Dizilerinin Alt Kümelerini Oluşturma

```yaml
type: NormalExercise
key: fcb2a9007b
lang: python
xp: 100
skills:
  - 2
```

Alt küme oluşturma (listelerde veya dizilerde köşeli parantez kullanarak), listelerde ve dizilerde tamamen aynı şekilde çalışır.

Bu egzersiz için arka planda `height_in` ve `weight_lb` adlı iki liste önceden yüklenmiştir. Bunlar MLB oyuncularının boy ve kilolarını normal listeler halinde içermektedir. Ayrıca, sizin için hazırlanmış `np_weight_lb` ve `np_height_in` adlı iki `numpy` dizi listesi bulunmaktadır.

`@instructions`
- Dizin 50’deki elemanı yazdırarak `np_weight_lb` alt kümesi oluşturun.
- `np_height_in` listesinin, dizin 100’den 110’a **kadar olan** elemanları içeren bir alt dizisini yazdırın.

`@hint`
- Alt küme oluşturma işlemlerinizi bir `print()` çağrısıyla sarmaladığınızdan emin olun.
- 100’den 110’a kadar olan elemanları almak için `[100:111]` kullanın.

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
msg = "Önceden tanımlanmış değişkenleri değiştirmenize veya kaldırmanıza gerek yok."
Ex().multi(
    check_object("np_height_in", missing_msg=msg).has_equal_value(incorrect_msg=msg),
    check_object("np_weight_lb", missing_msg=msg).has_equal_value(incorrect_msg=msg)
)

Ex().has_printout(0)
Ex().has_printout(1)

success_msg("Güzel! Yeni bir şey öğrenme zamanı: 2D NumPy dizileri!")
```

---

## 2D NumPy Dizileri

```yaml
type: VideoExercise
key: 1241efac7a
xp: 50
```

`@projector_key`
ae3238dcc7feb9adecfee0c395fc8dc8

---

## İlk 2D NumPy Diziniz

```yaml
type: NormalExercise
key: 5cb045bb13
lang: python
xp: 100
skills:
  - 2
```

Gerçek MLB verileri üzerinde çalışmaya başlamadan önce küçük bir liste listesinden bir 2D `numpy` dizisi oluşturmaya çalışalım.

Bu egzersizde `baseball` bir liste listesidir. Ana liste 4 elemandan oluşur. Bu elemanların her biri, 4 beyzbol oyuncusunun boy ve kilosunu bu sırayla içeren bir listedir. `baseball`, betikte sizin için önceden kodlanmıştır.

`@instructions`
- `np.array()` fonksiyonunu kullanarak `baseball` listesinden bir 2D `numpy` dizisi oluşturun. `np_baseball` olarak adlandırın.
- `np_baseball` türünü yazdırın.
- `np_baseball` listesinin `shape` özniteliğini yazdırın. `np_baseball.shape` fonksiyonunu kullanın.

`@hint`
- `baseball`, betikte sizin için önceden kodlanmıştır. Liste üzerinde `np.array()` çağrısı yapın ve elde edilen 2D `numpy` dizisini `np_baseball` listesine kaydedin.
- İkinci talimat için `print()` fonksiyonunu `type()` ile birlikte kullanın.
- `np_baseball.shape` listesi size `np_baseball` listesinin boyutlarını verecektir. Etrafına bir `print()` çağrısı sarmaladığınızdan emin olun.

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
msg = "Önceden tanımlanmış değişkenleri değiştirmenize veya kaldırmanıza gerek yok."
Ex().check_object("baseball", missing_msg=msg).has_equal_value(incorrect_msg=msg)
Ex().has_import("numpy", same_as=False)

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

success_msg("Harika! Artık gerçek MLB verilerini 2D `numpy` dizisine dönüştürmeye hazırsınız!")
```

---

## 2 boyutlu beyzbol verileri

```yaml
type: NormalExercise
key: 5df25d0b7b
lang: python
xp: 100
skills:
  - 2
```

Tüm bu bilgileri 2 boyutlu bir `numpy` dizisinde yeniden yapılandırmanın daha mantıklı olduğunu fark ediyorsunuz.

Elinizde bir Python liste listesi var. Bu liste listesinde her alt liste tek bir beyzbol oyuncusunun boyunu ve kilosunu temsil etmektedir. Bu listenin adı `baseball` ve sizin için zaten yüklenmiş durumda (ancak göremiyorsunuz).

`numpy` dizisinin ekstra fonksiyonlarını kullanmak için verileri bir 2D dizi olarak kaydedin.

`@instructions`
- `np.array()` fonksiyonunu kullanarak `baseball` listesinden bir 2D `numpy` dizisi oluşturun. `np_baseball` olarak adlandırın.
- `np_baseball` listesinin `shape` özniteliğini yazdırın.

`@hint`
- `baseball` listesi Python ortamında zaten mevcuttur. Liste üzerinde `np.array()` çağrısı yapın ve elde edilen 2D `numpy` dizisini `np_baseball` listesine kaydedin.
- `np_baseball.shape` listesi size `np_baseball` listesinin boyutlarını verecektir. Etrafına bir `print()` çağrısı sarmaladığınızdan emin olun.

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

success_msg("Harika! Çok boyutlu `numpy` dizilerinin bazı etkileyici özelliklerini gösterme zamanı!")
```

---

## 2D NumPy Dizilerinin Alt Kümelerini Oluşturma

```yaml
type: NormalExercise
key: aeca4977f0
lang: python
xp: 100
skills:
  - 2
```

2D `numpy` diziniz düzenli bir yapıya sahipse, yani her satır ve sütun sabit sayıda değere sahipse, karmaşık alt küme oluşturma yöntemleri çok kolay hale gelir. `"a"` ve `"c"` elemanlarının bir liste listesinden çıkarıldığı aşağıdaki koda bakın.

```
# numpy
import numpy as np
np_x = np.array(x)
np_x[:, 0]
```

Virgül öncesindeki dizinler satırları, virgül sonrasındaki dizinler ise sütunları ifade eder. `:` dilimleme içindir. Bu örnekte ise Python’a tüm satırları dahil etmesini söyler.

`@instructions`
- `np_baseball` listesindeki 50. satırı yazdırın.
- `np_baseball` listesinin ikinci sütununun tamamını içeren `np_weight_lb` adlı yeni bir değişken oluşturun.
- `np_baseball` listesinde 124. sırada yer alan beyzbol oyuncusunun boyunu (ilk sütun) seçin ve yazdırın.

`@hint`
- Birinci talimatta 49. satır dizinine ihtiyacınız var! Daha spesifik olarak, `[49, :]` değerini kullanmanız gerekiyor.
- İkinci sütunun tamamını seçmek için `[:, 1]` yazmanız gerekir.
- Son talimatta `[123, 0]` kullanın; hepsini bir `print()` ifadesinde sarmalamayı unutmayın.

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
msg = "Önceden tanımlanmış değişkenleri değiştirmenize veya kaldırmanıza gerek yok."
Ex().multi(
    has_import("numpy", same_as = False),
    check_object("np_baseball", missing_msg=msg).has_equal_value(incorrect_msg = msg)
)

Ex().has_printout(0)

Ex().check_object('np_weight_lb').has_equal_value(incorrect_msg = "`np_weight_lb`'yi tanımlamak için `np_baseball[:,1]` kullanabilirsiniz. Bu, birinci sütunun tamamını seçecektir.")

Ex().has_printout(1)

success_msg("Bu iyi gidiyor!")
```

---

## 2D Aritmetik

```yaml
type: NormalExercise
key: 1c2378b677
lang: python
xp: 100
skills:
  - 2
```

2D `numpy` dizileri, `numpy` dizileri gibi eleman bazında hesaplamalar yapabilir.

`np_baseball` sizin için kodlanmıştır; yine 2 boyutlu bir `numpy` dizisi, 3 sütunda boy (inç cinsinden), kilo (pound cinsinden) ve yaş (yıl cinsinden) değerlerini temsil etmektedir. `baseball` normal bir liste listesidir ve `updated`, 2 boyutlu numpy dizisidir.

`@instructions`
- Tüm beyzbol oyuncularının boy, kilo ve yaş değişikliklerini elde etmeyi başardınız. Bu veriler `updated` adlı bir 2D `numpy` dizisi olarak mevcuttur. `np_baseball` ve `updated` ekleyin ve sonucu yazdırın.
- Boy ve kilo birimlerini metrik birimlere (sırasıyla metre ve kilogram) dönüştürmek istiyorsunuz. İlk adım olarak üç değer içeren bir `numpy` dizisi oluşturun: `0.0254`, `0.453592` ve `1`. Bu diziye `conversion` adını verin.
- `np_baseball` ile `conversion` değerlerini çarpın ve sonucu yazdırın.

`@hint`
- `np_baseball + updated`, iki `numpy` dizisinin eleman bazındaki toplamını hesaplar.
- `np.array()` ile bir `numpy` dizisi oluşturun. Girdi, üç elemanlı normal bir Python listesidir.
- `np_baseball * conversion` ekstra iş gerektirmeden çalışacaktır. Deneyin! Bir `print()` çağrısında sarmaladığınızdan emin olun.

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

msg = "Önceden tanımlanmış değişkenleri değiştirmenize veya kaldırmanıza gerek yok."
Ex().check_object("np_baseball", missing_msg=msg).has_equal_value(incorrect_msg=msg)

Ex().has_printout(0)

Ex().check_correct(
    has_printout(1),
    check_correct(
        check_object('conversion').has_equal_value(),
        check_function('numpy.array', index=1).check_args(0).has_equal_value()
    )    
)

success_msg("Harika iş! Çok az kodla, `numpy` veri yapınızdaki tüm değerleri çok spesifik bir şekilde nasıl değiştirebileceğinizi fark edin. Bu, gelecekte bir veri bilimci olarak sizin için çok faydalı olacak!")
```

---

## NumPy: Temel İstatistikler

```yaml
type: VideoExercise
key: 287995e488
xp: 50
```

`@projector_key`
34495ba457d74296794d2a122c9b6e19

---

## Ortalama ve medyan

```yaml
type: NormalExercise
key: 509c588eb6
lang: python
xp: 100
skills:
  - 2
```

Artık verilerinizi daha iyi anlamak için `numpy` fonksiyonlarını nasıl kullanacağınızı biliyorsunuz. 

Beyzbol verileri, 3 sütun (boy, kilo, yaş) ve 1015 satırdan oluşan 2D `numpy` dizisi olarak mevcuttur. Bu `numpy` dizisinin adı `np_baseball`'dur. Ancak, verileri yeniden yapılandırdıktan sonra bazı boy değerlerinin anormal derecede yüksek olduğunu fark edersiniz. Talimatları izleyin ve sözde _aykırı değerlerle_ uğraşıyorsanız hangi özet istatistiğin en uygun olduğunu keşfedin. Burada `np_baseball` mevcuttur.

`@instructions`
- `np_baseball` listesinin birinci sütununa eşit olan `np_height_in` adlı bir `numpy` dizisi oluşturun.
- `np_height_in` dizisinin ortalamasını yazdırın.
- `np_height_in` dizisinin medyanını yazdırın.

`@hint`
- 2D `numpy` alt kümesi kullanın: `[:,0]` çözümün bir parçasıdır.
- `numpy`, `np` olarak içe aktarılırsa `np.mean()` kullanarak NumPy dizisinin ortalamasını alabilirsiniz. Bir `print()` çağrısı yapmayı unutmayın.
- Son talimat için `np.median()` kullanın.

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

Ex().check_object("np_height_in").has_equal_value(incorrect_msg = "`np_baseball`'dan ilk sütunu seçmek için `np_baseball[:,0]` kullanabilirsiniz"),

Ex().check_correct(
    has_printout(0),
    check_function('numpy.mean').has_equal_value()
)

Ex().check_correct(
    has_printout(1),
    check_function('numpy.median').has_equal_value()
)

success_msg("1586 inçlik ortalama bir yükseklik, kulağa doğru gelmiyor, değil mi? Ancak, medyan aykırı değerlerden etkilenmiş gibi görünmüyor: 74 inç mükemmel bir anlam ifade ediyor. Tüm veri kümesinin genel dağılımı hakkında bir fikir edinmek için her zaman hem medyanı hem de ortalamayı kontrol etmek iyi bir fikirdir.")
```

---

## Beyzbol verilerini keşfetme

```yaml
type: NormalExercise
key: '4409948807'
lang: python
xp: 100
skills:
  - 2
```

Ortalama ve medyan değerleri birbirinden çok uzak olduğu için MLB'ye şikayette bulunmaya karar veriyorsunuz. Hataları buluyorlar ve düzeltilmiş verileri size gönderiyorlar. Yine üç sütunlu bir 2D NumPy dizisi `np_baseball` var.

Editördeki Python kodu, farklı özet istatistikleri içeren bilgilendirici mesajları yazdırmak için gerekli kodu zaten içermektedir ve `numpy`, `np` olarak zaten yüklenmiştir. İşi bitirebilir misiniz? Elinizde `np_baseball` var.

`@instructions`
- Ortalama yüksekliği yazdırmak için gerekli kod zaten dahil edilmiştir. Medyan yüksekliğin kodunu tamamlayın.
- `np_baseball` tablosunun birinci sütununda `np.std()` kullanarak `stddev` değerini hesaplayın. 
- Büyük oyuncular daha ağır olma eğiliminde midir? `np.corrcoef()` kullanarak birinci ve ikinci `np_baseball` sütunları arasındaki korelasyonu `corr` içine kaydedin.

`@hint`
- `np.median()` fonksiyonunu kullanarak medyanı hesaplayın. Önce düzeltmek istediğiniz sütunu seçtiğinizden emin olun!
- `np.std()` ile standart sapmayı hesaplarken aynı sütunun alt kümesini oluşturun.
- `np_baseball[:, 0]` ve `np_baseball[:, 1]` kullanarak birinci ve ikinci sütunları seçin; bunlar `np.corrcoef()` girdileridir.

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
msg = "Tanımlı `avg` değişkenini değiştirmemeli veya kaldırmamalısınız."
Ex().check_object("avg", missing_msg=msg).has_equal_value(incorrect_msg=msg)

missing = "`np.median()` fonksiyonunu kullanarak medyanı hesapladınız mı?"
incorrect = "`med`'i hesaplamak için, `np_baseball`'un ilk sütununu `numpy.median()` fonksiyonuna geçirin. `np.mean()` örneği nasıl yapıldığını gösteriyor."
Ex().check_correct(
  check_object("med").has_equal_value(),
  check_function("numpy.median", index=0, missing_msg=missing).check_args(0).has_equal_value(incorrect_msg=incorrect)
)

missing = "`np.std()` fonksiyonunu kullanarak standart sapmayı hesapladınız mı?"
incorrect = "`stddev`'i hesaplamak için, `np_baseball`'un ilk sütununu `numpy.std()` fonksiyonuna geçirin. `np.mean()` örneği nasıl yapıldığını gösteriyor."
Ex().check_correct(
  check_object("stddev").has_equal_value(),
  check_function("numpy.std", index=0, missing_msg=missing).check_args(0).has_equal_value(incorrect_msg=incorrect)
)

missing = "`np.corrcoef()` fonksiyonunu kullanarak korelasyonu hesapladınız mı?"
incorrect1 = "`corr`'i hesaplamak için, `np.corrcoef()` fonksiyonunun ilk argümanı `np_baseball`'un ilk sütunu olmalıdır, daha önce nasıl yaptıysanız benzer şekilde."
incorrect2 = "`corr`'i hesaplamak için, `np.corrcoef()` fonksiyonunun ikinci argümanı `np_baseball`'un ikinci sütunu olmalıdır. Bu sefer `[:,0]` yerine `[:,1]` kullanın."
Ex().check_correct(
  check_object("corr").has_equal_value(),
  check_function("numpy.corrcoef", index=0, missing_msg=missing).multi(
    check_args(0, missing_msg=incorrect1).has_equal_value(incorrect_msg=incorrect1),
    check_args(1, missing_msg=incorrect2).has_equal_value(incorrect_msg=incorrect2)
  )
)

success_msg("Harika iş! Sağlam bir temel oluşturdunuz - şimdi tüm yeni veri bilimi becerilerinizi kullanarak daha fazla zorluk çözme ve etki yaratma zamanı.")
```

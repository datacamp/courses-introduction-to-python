---
title: Insert title here
key: 433dcfcfedaee070cbf440491c402e3b
video_link:
  mp3: >-
    https://videos.datacamp.com/mp3/translations/course_735/tr-TR/2d9c60d5-c3dc-4aa2-8a55-5cfa4c55bfdf.mp3
---

## Değişkenler ve Türler

```yaml
type: TitleSlide
key: dc8b62f1c8
```

`@lower_third`
name: Hugo Bowne-Anderson
title: Data Scientist at DataCamp

`@script`
Aferin ve tekrar hoş geldin! Python’un harika bir hesap makinesi olduğu açık. Ama daha karmaşık hesaplamalar yapmak istersen, birlikte kod yazarken değerleri "kaydetmek" isteyeceksin.

---

## Değişken

```yaml
type: FullSlide
key: 36ec318b41
```

`@part1`
- Özel, büyük/küçük harfe duyarlı ad

- Değişken adıyla değeri çağırın{{1}}

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
Bunu, büyük-küçük harfe duyarlı belirli bir adla bir değişken tanımlayarak yapabilirsin. Böyle bir değişkeni oluşturduğunda, daha sonra değişken adını yazarak değerine ulaşabilirsin.

Diyelim ki boyunu ve kilonu metrik birimlerle ölçtün: bir nokta yetmiş dokuz metre boyundasın ve altmış sekiz nokta yedi kilogramsın. Bu değerleri eşittir işaretiyle height ve weight adlı iki değişkene atayabilirsin:

Şimdi değişkenin adını, height, yazarsan,

Python bu değişken adını arar, değerini bulur ve ekrana yazdırır.

---

## BMI Hesapla

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

$$ \text{BMI} = \frac{\text{weight}}{\text{height}^2} $${{1}}

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
Şimdi Vücut Kitle İndeksi’ni, yani BMI’yi hesaplayalım. Formül şöyle, ağırlık kilogram, boy metre cinsinden. Bunu doğrudan sayılarla yapabilirsin, ama burada olduğu gibi height ve weight değişkenlerini de kullanabilirsin. Her değişken adını yazdığında, Python’dan onu değişkenin gerçek değeriyle değiştirmesini istiyorsun. weight altmış sekiz nokta yediye, height bir nokta yetmiş dokuza karşılık gelir.

Son olarak, bu sürümde sonucu yeni bir değişkende, bmi’de saklamasını sağladık. bmi şimdi az önce hesapladığın değeri içeriyor.

Python’da değişkenler sürekli kullanılır. Kodunun tekrarlanabilir olmasına yardımcı olur.

---

## Yeniden Üretilebilirlik

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
Diyelim ki height, weight ve bmi değişkenlerini oluşturan kod böyle bir betikte duruyor. Şimdi farklı bir kilo için bmi’yi yeniden hesaplamak istersen,

---

## Yeniden Üretilebilirlik

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
sadece weight değişkeninin tanımını değiştir ve betiği yeniden çalıştır. weight değişkeninin değeri de değiştiği için bmi buna göre güncellenir.

Şimdiye kadar sadece height ve weight gibi sayısal değerlerle çalıştık.

---

## Python Türleri

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
Python’da bu sayıların hepsinin belirli bir türü vardır. Bir değerin türünü type fonksiyonuyla görebilirsin. bmi değerimizin türünü görmek için, parantez içinde type ve ardından bmi yazman yeterli. Bunun float olduğunu görürsün; bu, Python’un gerçek sayıları yani tam ve kesirli kısmı olabilen sayıları temsil etme biçimidir. Python’da tamsayılar için de bir tür vardır: int, şu örnekteki gibi.

Veri bilimi yapmak için ise int ve float’tan daha fazlasına ihtiyaç duyacaksın.

---

## Python Türleri (2)

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
Python’da daha bir sürü veri türü vardır. En yaygın olanları string ve boolean’dır.

String, Python’un metni temsil etme biçimidir. Bu örneklerde gördüğün gibi string oluşturmak için hem çift hem tek tırnak kullanabilirsin. Buradaki son değişkenin türünü yazdırırsan, string’in kısaltması olan str görürsün.

Boolean ise True ya da False olabilen bir türdür. Gündelik dilde “Evet” ve “Hayır” gibi düşünebilirsin. Örneğin verilerini filtrelerken boolean’lar çok işine yarar.

Python veri türleriyle ilgili özel bir durum var.

---

## Python Türleri (3)

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

- Farklı tür = farklı davranış!{{3}}

`@script`
Şu iki satıra bak: biri iki tamsayıyı topluyor, diğeri iki string’i.

Tamsayılarda değerler toplandı, string’lerde ise metinler yan yana eklendi. Artı operatörü, veri türüne göre farklı davrandı. Bu genel bir ilkedir: kodun davranışı, çalıştığın türlere bağlıdır.

Sıradaki alıştırmalarda ilk değişkenlerini oluşturacak ve Python’un bazı veri türleriyle denemeler yapacaksın. Listelerle ilgili her şeyi anlatmak için bir sonraki videoda görüşürüz.

---

## Lass uns üben!

```yaml
type: FinalSlide
key: b7fc40db4d
```

`@script`
Hadi kod yazmaya başla ve bir sonraki bölümde daha da harika Python grafikleri oluştururken seni görmek için sabırsızlanıyorum.

---
title_meta: Bölüm 2
title: Python Listeleri
description: >-
  Büyük miktarda veriyle verimli bir şekilde çalışmanın ilk adımı olarak
  listelerde verileri depolamayı, verilere erişmeyi ve verileri işlemeyi
  öğrenin.
attachments:
  slides_link: 'https://projector-video-pdf-converter.datacamp.com/735/chapter2.pdf'
lessons:
  - nb_of_exercises: 4
    title: Python Listeleri
  - nb_of_exercises: 4
    title: Liste Alt Kümeleri Oluşturma
  - nb_of_exercises: 5
    title: Listeleri İşleme
---

## Python Listeleri

```yaml
type: VideoExercise
key: a5886d213f
xp: 50
```

`@projector_key`
a0530c4542f10988847b2dbb91f717c3

---

## Liste oluşturma

```yaml
type: NormalExercise
key: e6c527bf41
lang: python
xp: 100
skills:
  - 2
```

Liste bir **bileşik veri türüdür**. Listedeki değerleri şunun gibi gruplandırabilirsiniz:

```
a = "is"
b = "nice"
my_list = ["my", "list", a, b]
```

Ailenizdeki herkesin boyunu ölçtükten sonra yaşadığınız ev hakkında bazı bilgiler toplamaya karar veriyorsunuz. Evinizin farklı bölümlerinin alanları, egzersizde ayrı değişkenlerde depolanır.

`@instructions`
- `areas` adlı bir liste oluşturun ve bu listeye sırasıyla koridorun (`hall`), mutfağın (`kit`), oturma odasının (`liv`), yatak odasının (`bed`) ve banyonun (`bath`) alanını yazın. Önceden tanımlanmış değişkenleri kullanın.
- `print()` fonksiyonunu kullanarak `areas` sonucunu yazdırın.

`@hint`
- Listeyi oluşturmak için önceden oluşturulmuş değişkenleri kullanabilirsiniz: `areas = [hall, kit, ...]`.
- `()` gibi parantezler yerine `[]` gibi köşeli parantezler kullandığınızdan emin olun.
- Değişkenleri bir liste içinde depolarken tırnak işaretleri kullanmanıza gerek yoktur.
- Gönderirken listeyi yazdırmak için `print(areas)` yazın.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Create list areas


# Print areas

```

`@solution`
```{python}
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Create list areas
areas = [hall, kit, liv, bed, bath]

# Print areas
print(areas)
```

`@sct`
```{python}
predef_msg = "Önceden tanımlanmış değişkenleri kaldırmayın veya düzenlemeyin!"
areas_msg = "`areas`'ı tüm alan değişkenlerini içeren liste olarak, doğru sırayla tanımlayın: `[hall, kit, liv, bed, bath]`. Yazım hatalarına dikkat edin. Liste başka bir şey içermemelidir!"

Ex().check_correct(
    has_printout(0, not_printed_msg = "__JINJA__:Betik dosyanızın sonunda `areas` listesini yazdırmak için `{{sol_call}}` kullandınız mı?"),
    check_correct(
        check_object("areas").has_equal_value(incorrect_msg = areas_msg),
        multi(
            check_object('hall', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
            check_object('kit', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
            check_object('liv', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
            check_object('bed', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
            check_object('bath', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg)
        )
    )
)

success_msg("Güzel! Burada bir liste çok daha iyi, değil mi?")
```

---

## Farklı türlerde listeler oluşturma

```yaml
type: NormalExercise
key: 1702a8bcdc
lang: python
xp: 100
skills:
  - 2
```

Çok yaygın olmasa da bir liste; dizeler, kayan sayılar ve boole değerleri dahil olmak üzere çeşitli Python türlerini içerebilir.

Şimdi oda adlarını listenize ekleyeceksiniz, böylece oda adını ve büyüklüğünü birlikte kolayca görebileceksiniz.

Başlamanız için size bazı kodlar verilmiştir. Buraya dikkat edin! `"bathroom"` bir dizedir, `bath` ise daha önce belirttiğiniz `9.50` kayan değerini temsil eden bir değişkendir.

`@instructions`
- `areas` listesini oluşturan kodu tamamlayın. Listeyi, önce bir dize olarak her odanın adını ve ardından alanını içerecek şekilde oluşturun. Diğer bir deyişle `"hallway"`, `"kitchen"` ve `"bedroom"` dizelerini uygun yerlere ekleyin.
- `areas` sonucunu tekrar yazdırın; bu sefer çıktı daha bilgilendirici oldu mu?

`@hint`
- `areas` listesinin ilk dört elemanı `["hallway", hall, "kitchen", kit, ...` olarak kodlanmıştır.
- Dize tırnak işaretleri `""` içine alınmalıdır.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Adapt list areas
areas = [____, hall, ____, kit, "living room", liv, ____, bed, "bathroom", bath]

# Print areas
____
```

`@solution`
```{python}
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Adapt list areas
areas = ["hallway", hall, "kitchen", kit, "living room", liv, "bedroom", bed, "bathroom", bath]

# Print areas
print(areas)
```

`@sct`
```{python}
objs = ["hall", "kit", "liv", "bed", "bath"]
predef_msg = "Tanımlı değişkenleri kaldırmayın veya düzenlemeyin!"
areas_msg = "`areas` değişkenine doğru değeri atamadınız. Talimatlara bir kez daha göz atın. Her seferinde oda adını, alanı içeren değişkenin önüne koyduğunuzdan emin olun. Burada sıra önemlidir! Yazım hatalarına dikkat edin."

Ex().check_correct(
  check_object("areas").has_equal_value(incorrect_msg = areas_msg),
  multi([ check_object(obj, missing_msg = predef_msg).has_equal_value(incorrect_msg = predef_msg) for obj in objs])
)

Ex().has_printout(0, not_printed_msg = "__JINJA__:Betiminizin sonunda `areas` listesini yazdırmak için `{{sol_call}}` kullandınız mı?")

success_msg("Güzel! Bu liste hem string hem de float içeriyor, ancak bu Python için bir sorun değil!")
```

---

## Listelerin listesi

```yaml
type: NormalExercise
key: 9158c577b0
lang: python
xp: 100
skills:
  - 2
```

Bir veri bilimcisi olarak, çoğu zaman çok fazla veriyle uğraşacaksınız ve bu verilerin bir kısmını gruplandırmak mantıklı olacak.

Evinizdeki odaların adlarını ve alanlarını temsil eden dizeler ve kayan sayılar içeren bir liste oluşturmak yerine listelerin bir listesini oluşturabilirsiniz.

Unutmayın: `"hallway"` bir dizedir, `hall` ise daha önce belirttiğiniz `11.25` kayan değerini temsil eden bir değişkendir.

`@instructions`
- Liste listesini, yatak odası ve banyo verilerini de içerecek şekilde tamamlayın. Doğru sırayla girdiğinizden emin olun!
- `house` sonucunu yazdırın; verilerinizi bu şekilde yapılandırmak daha mantıklı mı oldu?

`@hint`
- `house` listesine _alt listeler_ eklemek için köşeli parantezlerin içine `["bedroom", bed]` ve `["bathroom", bath]` ekleyin.
- Her alt listeden sonra `,` koymayı unutmayın.
- Bir `x` değişkeni yazdırmak için yeni bir satıra `print(x)` yazın.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# House information as list of lists
house = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv],
        ____,
        ____]

# Print out house
____
```

`@solution`
```{python}
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# House information as list of lists
house = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv],
         ["bedroom", bed],
         ["bathroom", bath]]

# Print out house
print(house)
```

`@sct`
```{python}
predef_msg = "Önceden tanımlanmış değişkenleri kaldırmayın veya düzenlemeyin!"
house_msg = "`house` değişkenine doğru değeri atamadınız. Talimatlara bir kez daha göz atın. Listeyi, her oda adı ve oda alanı çifti için bir liste içerecek şekilde genişletin. Sıralamaya ve yazım hatalarına dikkat edin!"

Ex().check_correct(
    check_object("house").has_equal_value(incorrect_msg = house_msg),
    multi(
        check_object('hall', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
        check_object('kit', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
        check_object('liv', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
        check_object('bed', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
        check_object('bath', missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg)
    )
)

Ex().has_printout(0, not_printed_msg = "__JINJA__:`house` içeriğini yazdırmak için `{{sol_call}}` kullandınız mı?")

success_msg("Harika! Liste alt kümeleme hakkında bilgi edinmeye hazır olun!")
```

---

## Liste Alt Kümeleri Oluşturma

```yaml
type: VideoExercise
key: c076b5a69c
xp: 50
```

`@projector_key`
fc15ba5cb9485456df8589130b519ea3

---

## Alt kümelere böl ve yönet

```yaml
type: NormalExercise
key: c3ce582e32
lang: python
xp: 100
skills:
  - 2
```

Python listelerinin alt kümelerini oluşturmak çocuk oyuncağıdır. `x` listesini oluşturan ve ardından bu listeden "b" seçimi yapan aşağıdaki kod örneğini alın. Bunun ikinci eleman olduğunu, dolayısıyla dizininin 1 olduğunu unutmayın. Negatif dizinlemeyi de kullanabilirsiniz.

```
x = ["a", "b", "c", "d"]
x[1]
x[-3] # same result!
```

Daha önce gördüğümüz, hem dizeleri hem de kayan sayıları içeren `areas` listesini hatırlıyor musunuz? Tanımı zaten kodda var. Python alt kümesi oluşturmak için doğru kodu ekleyebilir misiniz?

`@instructions`
- `areas` listesinden ikinci elemanı yazdırın (`11.25` değerine sahiptir).
- `areas` listesinin alt kümesini oluşturun değeri `9.50` olan son elemanı yazdırın. Burada negatif dizin kullanmak mantıklıdır!
- Oturma odasının alanını temsil eden sayıyı (`20.0`) seçin ve yazdırın.

`@hint`
- `x` listesinin ikinci elemanını seçmek için `x[1]` kullanın.
- `x` listesinin son elemanını seçmek için `x[-1]` kullanın.
- Alt küme oluşturma işlemlerinizi bir `print()` çağrısı ile sarmaladığınızdan emin olun.
- Oturma odasının alanını temsil eden sayı listedeki 6. elemandır, bu nedenle burada `[5]` gerekir. `area[4]` dizeyi gösterir!

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Print out second element from areas
print(areas[____])

# Print out last element from areas
print(areas[____])

# Print out the area of the living room
print(areas[____])
```

`@solution`
```{python}
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Print out second element from areas
print(areas[1])

# Print out last element from areas
print(areas[-1])

# Print out the area of the living room
print(areas[5])
```

`@sct`
```{python}
msg = "Önceden tanımlanmış `areas` listesini kaldırmayın veya düzenlemeyin."
Ex().check_object("areas", missing_msg = msg).has_equal_value(incorrect_msg = msg)
Ex().has_printout(0, not_printed_msg = "Kodunuzu tekrar gözden geçirerek `areas` listesindeki ikinci öğeyi, yani `1` indeksindeki öğeyi yazdırın.")
Ex().has_printout(1, not_printed_msg = "Kodunuzu tekrar gözden geçirerek `areas` listesindeki son öğeyi, yani `-1` indeksindeki öğeyi yazdırın.")
Ex().has_printout(2, not_printed_msg = "Kodunuzu tekrar gözden geçirerek oturma odasının alanını yazdırın. Bu, `5` indeksindedir.")
success_msg("İyi iş!")
```

---

## Dilimlemek ve doğramak

```yaml
type: NormalExercise
key: 7f08642d18
lang: python
xp: 100
skills:
  - 2
```

Bir listeden tek bir değer seçmek, işin sadece bir kısmıdır. Listenizi _dilimlemek_, yani listenizden birden fazla eleman seçmek de mümkündür. Aşağıdaki sözdizimini kullanın:

```
my_list[start:end]
```

`start` dizini dahil edilir ancak `end` dizini dahil _edilmez_. Ancak bu dizinleri belirtmeme seçeneği de mevcuttur. `start` dizinini belirtmezseniz Python, dilimleme işleminin listenin başından başlamasını istediğinizi anlar.

`@instructions`
- Dilimlemeyi kullanarak, `areas` listesindeki ilk 6 elemanı içeren bir `downstairs` listesi oluşturun.
- `areas` listesinin son `4` elemanı olarak `upstairs` listesini oluşturun. Bu kez `end` dizinini atlayarak dilimlemeyi basitleştirin.
- `print()` fonksiyonunu kullanarak `downstairs` ve `upstairs` sonuçlarını yazdırın.

`@hint`
- Bir listenin ilk altı elemanını almak için köşeli parantez içinde `[0:6]` kullanın.
- Bir `l` listesinin ilk 5 elemanı hariç her şeyi almak için `l[5:]` kullanabilirsiniz.
- `downstairs` ve `upstairs` sonucunu yazdırmak için iki `print()` çağrısı ekleyin.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Use slicing to create downstairs
downstairs = areas[____]

# Use slicing to create upstairs
upstairs = areas[____]

# Print out downstairs and upstairs
____
____
```

`@solution`
```{python}
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Use slicing to create downstairs
downstairs = areas[0:6]

# Use slicing to create upstairs
upstairs = areas[6:]

# Print out downstairs and upstairs
print(downstairs)
print(upstairs)
```

`@sct`
```{python}
msg = "Önceden tanımlanmış `areas` listesini kaldırmayın veya düzenlemeyin."
Ex().check_object("areas", missing_msg = msg).has_equal_value(incorrect_msg = msg)

patt = "`%s` yanlıştır. İstediğiniz elemanları seçmek için `areas[%s]` ve dilimlemeyi kullanın veya eşdeğer bir şey yapın."
Ex().check_object("downstairs").has_equal_value(incorrect_msg = patt % ('downstairs', '0:6'))
Ex().check_object("upstairs").has_equal_value(incorrect_msg = patt % ("upstairs",":6"))

Ex().has_printout(0, not_printed_msg="`downstairs` hesapladıktan sonra yazdırdınız mı?")
Ex().has_printout(1, not_printed_msg="`upstairs` hesapladıktan sonra yazdırdınız mı?")

success_msg("Harika!")
```

---

## Listelerin listesinin alt kümelerini oluşturma

```yaml
type: NormalExercise
key: dbbbd306cf
xp: 100
```

Bir Python listesi başka listeler de içerebilir.

Listelerin alt kümelerini oluşturmak için daha önce kullandığımız tekniği kullanabilirsiniz: köşeli parantezler. Bu bir `house` listesi için şunun gibi görünecektir:

```
house[2][0]
```

`@instructions`
- `house` listesinin alt kümesini oluşturarak `9.5` kayan sayısını elde edin.

`@hint`
- Bunu adım adım inceleyelim. Öncelikle `["bathroom", 9.50]` listesinin son elemanına ulaşmak istiyorsunuz. Son elemanın dizininin `-1` olduğunu hatırlayın.
- Ardından `["bathroom", 9.50]` listesindeki ikinci elemanı almanız gerekir, bu eleman da `1` dizininde bulunur.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
house = [["hallway", 11.25],
         ["kitchen", 18.0],
         ["living room", 20.0],
         ["bedroom", 10.75],
         ["bathroom", 9.50]]

# Subset the house list
house___
```

`@solution`
```{python}
house = [["hallway", 11.25],
         ["kitchen", 18.0],
         ["living room", 20.0],
         ["bedroom", 10.75],
         ["bathroom", 9.50]]

# Subset the house list
house[-1][1]
```

`@sct`
```{python}
Ex().check_or(
  has_code("house[-1][1]", pattern=False),
  has_code("house[4][1]", pattern=False)
)

success_msg("Doğru! Liste bulmacasının son parçası manipülasyondur.")
```

---

## Listeleri İşleme

```yaml
type: VideoExercise
key: d7fe818b3a
xp: 50
```

`@projector_key`
355ed52d2fb0d67508c6a311b7cbc6d3

---

## Liste elemanlarını değiştirme

```yaml
type: NormalExercise
key: 4e1bba1b55
lang: python
xp: 100
skills:
  - 2
```

Liste elemanlarını değiştirmek için, listenin alt kümesini oluşturun ve alt kümeye yeni değerler atayın. Elemanları tek tek seçebilir veya tüm liste dilimlerini tek seferde değiştirebilirsiniz.

Bu ve sonraki egzersizlerde bir evdeki farklı odaların adlarını ve alanlarını içeren `areas` listesi üzerinde çalışmaya devam edeceksiniz.

`@instructions`
- Negatif dizinleme kullanarak banyonun alanını `9.50` metrekare yerine `10.50` metrekare olarak güncelleyin.
- `areas` listesini daha modaya uygun hale getirin! `"living room"` adını `"chill zone"` olarak değiştirin. Bu sefer negatif dizinleme kullanmayın.

`@hint`
- Banyo alanını güncellemek için banyo alanının alt kümesini oluşturun (listenin son elemanı!).
- Ardından değeri bu alt kümeye atayarak yeni banyo alanıyla değiştirin.
- 4. dizinde bulunan `"living room"` adını güncellemek için de aynı işlemi yapın.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Correct the bathroom area


# Change "living room" to "chill zone"

```

`@solution`
```{python}
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Correct the bathroom area
areas[-1] = 10.50

# Change "living room" to "chill zone"
areas[4] = "chill zone"
```

`@sct`
```{python}
bathroom_msg = '`areas[-1] = 10.50` ifadesini kullanarak banyo alanını güncelleyebilirsiniz.'
chillzone_msg = '`areas[4] = "chill zone"` ifadesini kullanarak oturma odası adını güncelleyebilirsiniz.'
Ex().check_correct(
  check_object('areas').has_equal_value(incorrect_msg = '`areas` üzerindeki değişiklikleriniz doğru listeyle sonuçlanmadı. Doğru alt küme işlemlerini kullandığınızdan emin misiniz? Şüpheye düştüğünüzde, bir ipucu kullanabilirsiniz!'),
  multi(
    has_equal_value(expr_code='areas[-1]', override=10.50, incorrect_msg = bathroom_msg),
    has_equal_value(expr_code='areas[4]', override='chill zone', incorrect_msg = chillzone_msg),
  )
)
success_msg('Harika! Kod örneğinde gösterildiği gibi, bir listeyi dilimleyebilir ve tek bir komutla birden fazla öğeyi güncellemek için başka bir listeyle değiştirebilirsiniz.')
```

---

## Listeyi genişletme

```yaml
type: NormalExercise
key: ff0fe8d967
lang: python
xp: 100
skills:
  - 2
```

Bir listedeki elemanları değiştirebiliyorsanız listeye eleman ekleyebilmeniz de mümkün olmalıdır, değil mi? `+` işlecini kullanabilirsiniz:

```
x = ["a", "b", "c", "d"]
y = x + ["e", "f"]
```

Muhteşem bir şey oldu ve piyango size çıktı! Havuzlu bir ev ve garaj inşa etmeye karar verdiniz. Bu bilgileri `areas` listesine ekleyebilir misiniz?

`@instructions`
- `+` işlecini kullanarak `["poolhouse", 24.5]` listesini `areas` listesinin sonuna yapıştırın. Elde edilen listeyi `areas_1` olarak kaydedin.
- Garajınızla ilgili bilgileri ekleyerek `areas_1` listesini daha da genişletin. `"garage"` dizesini ve `15.45` kayan sayısını ekleyin. Ortaya çıkan listeye `areas_2` adını verin.

`@hint`
- Ödevdeki kod örneğini takip edin. `x` burada `areas`, `["e", "f"]` ise `["poolhouse", 24.5]` değerine karşılık gelir.
- `areas_1` listesine daha fazla eleman eklemek için `areas_1 + ["element", 123]` komutunu kullanın.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create the areas list and make some changes
areas = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0,
         "bedroom", 10.75, "bathroom", 10.50]

# Add poolhouse data to areas, new list is areas_1
areas_1 = ____

# Add garage data to areas_1, new list is areas_2
areas_2 = ____
```

`@solution`
```{python}
# Create the areas list (updated version)
areas = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0,
         "bedroom", 10.75, "bathroom", 10.50]

# Add poolhouse data to areas, new list is areas_1
areas_1 = areas + ["poolhouse", 24.5]

# Add garage data to areas_1, new list is areas_2
areas_2 = areas_1 + ["garage", 15.45]
```

`@sct`
```{python}
msg = "Önceden tanımlanmış `areas` listesini kaldırmayın veya düzenlemeyin."
Ex().check_object("areas", missing_msg = msg).has_equal_value(incorrect_msg = msg)
Ex().check_object("areas_1").has_equal_value(incorrect_msg = "`areas_1` oluşturmak için `areas + [\"poolhouse\", 24.5]` kullanın. Yazım hatalarına dikkat edin!")
Ex().check_object("areas_2").has_equal_value(incorrect_msg = "`areas_2` oluşturmak için `areas_1 + [\"garage\", 15.45]` kullanın. Yazım hatalarına dikkat edin!")
success_msg("Harika! Liste güzel bir şekilde şekilleniyor!")
```

---

## Liste elemanlarını silme

```yaml
type: NormalExercise
key: 85f792356e
xp: 100
```

Son olarak, listenizden eleman da silebilirsiniz. Bunu `del` ifadesiyle yapabilirsiniz:

```
x = ["a", "b", "c", "d"]
del x[1]
```

Burada dikkatli olun: Bir elemanı listeden kaldırdığınız anda silinen elemanın ardından gelen tüm elemanların dizinleri değişir!

Maalesef piyangoda kazandığınız miktar o kadar da büyük değil ve havuzlu ev hayali suya düşecek gibi görünüyor. Bunu listeden kaldırmanız gerekecek. `areas` listesinden ilgili dizeyi ve kayan sayıyı kaldırmaya karar veriyorsunuz.

`@instructions`
- `areas` listenizden `"poolhouse"` dizesini ve kayan sayısını silin.
- Güncellenen `areas` listesini yazdırın.

`@hint`
- İki elemanı silmek için `del` ifadesini iki kez kullanmanız gerekir. Yine de değişen dizinlere dikkat edin!

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
areas = ["hallway", 11.25, "kitchen", 18.0,
        "chill zone", 20.0, "bedroom", 10.75,
         "bathroom", 10.50, "poolhouse", 24.5,
         "garage", 15.45]

# Delete the poolhouse items from the list


# Print the updated list

```

`@solution`
```{python}
areas = ["hallway", 11.25, "kitchen", 18.0,
        "chill zone", 20.0, "bedroom", 10.75,
         "bathroom", 10.50, "poolhouse", 24.5,
         "garage", 15.45]

# Delete the poolhouse items from the list
del areas[10]
del areas[10]

# Print the updated list
print(areas)
```

`@sct`
```{python}
Ex().check_or(
  multi(
    has_code("del areas[10]", pattern=False),
    has_code("del areas[10]", pattern=False)
  ),
  has_code("del areas[-4:-2]", pattern=False),
  has_code("del(areas[-4:-2])", pattern=False),
  multi(
    has_code("del(areas[10])", pattern=False),
    has_code("del(areas[10])", pattern=False)
  ),
  has_code("del areas[10:12]", pattern=False),
  has_code("del(areas[10:12])", pattern=False),
  multi(
    has_code("del areas[-4]", pattern=False),
    has_code("del areas[-3]", pattern=False)
  ),
  multi(
    has_code("del(areas[-4])", pattern=False),
    has_code("del(areas[-3])", pattern=False)
  )
)

Ex().has_printout(0, not_printed_msg="`areas` listesinden havuz evi dizgesi ve ondalık sayıyı çıkardıktan sonra listeyi yazdırdınız mı?")
success_msg("Doğru! Python listelerinden belirli öğeleri çıkarmanın daha kolay yollarını daha sonra öğreneceksiniz.")
```

---

## Listelerin iç işleyişi

```yaml
type: NormalExercise
key: af72db9915
lang: python
xp: 100
skills:
  - 2
```

Bu egzersizde size bazı kodlar verilmiştir: `areas` adlı bir liste ve `areas_copy` adlı bir kopya.

Şu anda, `areas_copy` listesinin ilk elemanı değiştirildi ve `areas` listesi yazdırıldı. Çalıştır düğmesine basarsanız, `areas_copy` kopyasını değiştirmiş olmanıza rağmen değişikliğin `areas` listesine de uygulandığını göreceksiniz. Bunun nedeni, `areas` listesi ile `areas_copy` kopyasının aynı listeyi işaret etmesidir.

`areas_copy` kopyasındaki değişikliklerin `areas` listesine de uygulanmasını istemiyorsanız `list()` ile veya `[:]` kullanarak `areas` listesinin daha açık bir kopyasını oluşturmanız gerekir.

`@instructions`
- `areas_copy` değişkenini oluşturan ikinci komutu, `areas_copy` kopyası `areas` listesinin açık bir kopyası olacak şekilde değiştirin. Düzenlemenizden sonra `areas_copy` kopyasında yapılan değişiklikler `areas` listesini etkilemeyecektir. Bunu kontrol etmek için yanıtı gönderin.

`@hint`
- `areas_copy = areas` çağrısını değiştirin. `areas` yerine `list(areas)` veya `areas[:]` atayabilirsiniz.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Change this command
areas_copy = areas

# Change areas_copy
areas_copy[0] = 5.0

# Print areas
print(areas)
```

`@solution`
```{python}
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Change this command
areas_copy = list(areas)

# Change areas_copy
areas_copy[0] = 5.0

# Print areas
print(areas)
```

`@sct`
```{python}
Ex().check_correct(
  check_object("areas_copy").has_equal_value(incorrect_msg = "`areas_copy`'nin doğru şekilde güncellenmediği anlaşılıyor."),
  check_function("list", missing_msg = "`areas_copy` oluşturmak için `list(areas)` kullandığınızdan emin olun.")
)

mmsg = "Tanımlı `areas` listesini kaldırmayın."
imsg = "Yalnızca kopyayı düzenlediğinizden emin olun, orijinal `areas` listesini değil. Nasıl bir kopya oluşturacağınızdan emin değilseniz, alıştırma açıklamasına tekrar bakın."
Ex().check_correct(
  check_object("areas", missing_msg = mmsg).has_equal_value(incorrect_msg = imsg),
  check_function("list", missing_msg = "`areas_copy` oluşturmak için `list(areas)` kullandığınızdan emin olun.")
)

success_msg("Güzel! Açık ve referans tabanlı kopyalar arasındaki fark ince ama gerçekten önemli olabilir. Bir listenin bilgisayarın belleğinde nasıl saklandığını aklınızda tutmaya çalışın.")
```

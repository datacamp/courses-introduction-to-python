---
title_meta: Bölüm 3
title: Fonksiyonlar ve Paketler
description: >-
  Python'un parlak geliştiricileri tarafından yazılmış koddan verimli bir
  şekilde yararlanmak için fonksiyonları, yöntemleri ve paketleri nasıl
  kullanacağınızı öğreneceksiniz. Amaç, zorlu sorunları çözmek için gereken kod
  miktarını azaltmaktır!
attachments:
  slides_link: 'https://projector-video-pdf-converter.datacamp.com/735/chapter3.pdf'
lessons:
  - nb_of_exercises: 4
    title: Fonksiyonlar
  - nb_of_exercises: 4
    title: Yöntemler
  - nb_of_exercises: 4
    title: Paketler
---

## Fonksiyonlar

```yaml
type: VideoExercise
key: 5c5f365930
xp: 50
```

`@projector_key`
1204d914b0e53100529827e07441ee6c

---

## Tanıdık fonksiyonlar

```yaml
type: NormalExercise
key: c422ee929b
lang: python
xp: 100
skills:
  - 2
```

Python, veri bilimcisi olarak hayatınızı kolaylaştırmak için bir dizi yerleşik fonksiyon sunar. Bu türden iki fonksiyonu zaten biliyorsunuz: `print()` ve `type()`. Veri türleri arasında geçiş yapmak için `str()`, `int()`, `bool()` ve `float()` gibi fonksiyonlar da bulunur. Bunları [burada](https://docs.python.org/3/library/functions.html) bulabilirsiniz. Bunlar da yerleşik fonksiyonlardır.

Bir fonksiyonu çağırmak kolaydır. `3.0` türünü almak ve çıktıyı yeni bir `result` değişkeni olarak kaydetmek için aşağıdakileri kullanabilirsiniz:

```
result = type(3.0)
```

`@instructions`
- `print()` fonksiyonunu `type()` ile birlikte kullanarak `var1` türünü yazdırabilirsiniz.
- `len()` fonksiyonunu kullanarak `var1`[listesinin uzunluğunu](https://docs.python.org/3/library/functions.html#len) alın. Bir `print()` çağrısında sarmalayarak doğrudan yazdırın.
- `var2` listesini bir [tamsayıya](https://docs.python.org/3/library/functions.html#int) dönüştürmek için `int()` fonksiyonunu kullanın. Çıktıyı `out2` olarak kaydedin.

`@hint`
- `type()` fonksiyonunu şu şekilde çağırın: `type(var1)`.
- Daha önce defalarca yaptığınız gibi `print()` fonksiyonunu çağırın. Yazdırmak istediğiniz değişkeni parantez içine alın.
- `int(x)` fonksiyonu `x` değerini bir tamsayıya dönüştürür.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create variables var1 and var2
var1 = [1, 2, 3, 4]
var2 = True

# Print out type of var1
____

# Print out length of var1
____

# Convert var2 to an integer: out2
out2 = ____
```

`@solution`
```{python}
# Create variables var1 and var2
var1 = [1, 2, 3, 4]
var2 = True

# Print out type of var1
print(type(var1))

# Print out length of var1
print(len(var1))

# Convert var2 to an integer: out2
out2 = int(var2)
```

`@sct`
```{python}
msg = "Önceden tanımlanmış değişkenleri değiştirmenize veya kaldırmanıza gerek yok."
Ex().check_object("var1", missing_msg=msg).has_equal_value(incorrect_msg=msg)
Ex().check_object("var2", missing_msg=msg).has_equal_value(incorrect_msg=msg)

patt = "__JINJA__: `var1`'in %s değerini `{{sol_call}}` ile yazdırdığınızdan emin olun."
Ex().has_printout(0, not_printed_msg = patt % 'tür')
Ex().has_printout(1, not_printed_msg = patt % 'uzunluk')

int_miss_msg = "`var2`'yi bir tamsayı yapmak için `int()` kullandınız mı?"
int_incorr_msg = "`var2`'yi `int()`'e geçirdiniz mi?"
Ex().check_correct(
  check_object("out2").has_equal_value(incorrect_msg="`int()` fonksiyonunu doğru şekilde çağırdınız; şimdi bu çağrının sonucunu `out2`'ye atadığınızdan emin olun."),
  check_function("int", missing_msg=int_miss_msg).has_equal_value(incorrect_msg=int_incorr_msg)
)
success_msg("Harika iş! `len()` fonksiyonu son derece kullanışlıdır; ayrıca karakter sayısını saymak için dizelerde de çalışır!")
```

---

## Yardım!

```yaml
type: MultipleChoiceExercise
key: 679b852978
lang: python
xp: 50
skills:
  - 2
```

Bir Python fonksiyonunun adını zaten biliyor olabilirsiniz ancak nasıl kullanacağınızı yine de anlamanız gerekir. İronik olacak ama bir fonksiyon hakkında bilgi almak için başka bir fonksiyon kullanmanız gerekir: `help()`. Özellikle IPython'da fonksiyon adından önce `?` kullanabilirsiniz.

Örneğin `max()` fonksiyonuyla ilgili yardım almak için şu çağrılardan birini kullanabilirsiniz:

```
help(max)
?max
```

`pow()` fonksiyonuyla ilgili [belgeleri](https://docs.python.org/3/library/functions.html#pow) açmak için IPython Shell’i kullanın. Bunu yapmak için `?pow` veya `help(pow)` yazıp **Enter** tuşuna basın.

Aşağıdaki ifadelerden hangisi doğrudur?

`@possible_answers`
- `pow()` üç bağımsız değişken alır: `base`, `exp` ve `mod`. `mod` olmadan fonksiyon bir hata döndürür.
- `pow()` üç zorunlu bağımsız değişken alır: `base`, `exp` ve `None`.
- `pow()` için `base` ve `exp` bağımsız değişkenleri zorunlu, `mod` ise isteğe bağlıdır.
- `pow()` iki bağımsız değişken alır: `exp` ve `mod`. `exp` bağımsız değişkeninin eksik olması bir hataya neden olur.

`@hint`
- İsteğe bağlı bağımsız değişkenler varsayılan bir değere `=` olarak ayarlanır ve bu değişken belirtilmezse fonksiyon bu değeri kullanır.

`@pre_exercise_code`
```{python}

```

`@sct`
```{python}
msg1 = "Tam olarak değil. `mod` belirtmezseniz varsayılan bir değer kullanılır."
msg2 = "Yanlış. `mod` argümanı için varsayılan değer `None`'dır."
msg3 = "Mükemmel! `help()` kullanmak, fonksiyonların nasıl çalıştığını anlamanıza yardımcı olabilir ve onların tam potansiyelini ortaya çıkarabilir!"
msg4 = "Yanlış. `pow()` üç argüman alır, bunlardan biri varsayılan bir değere sahiptir."
Ex().has_chosen(3, [msg1, msg2, msg3, msg4])
```

---

## Birden fazla bağımsız değişken

```yaml
type: NormalExercise
key: e30486d7c1
lang: python
xp: 100
skills:
  - 2
```

Önceki egzersizde `help()` ile belgeleri görüntüleyerek isteğe bağlı bağımsız değişkenleri belirlediniz. Şimdi bunu `sorted()` fonksiyonunun davranışını değiştirmek için uygulayacaksınız.

IPython Shell’de `help(sorted)` yazarak `sorted()` [belgelerine](https://docs.python.org/3/library/functions.html#sorted) göz atın.

Göreceğiniz gibi `sorted()` üç bağımsız değişken alır: `iterable`, `key` ve `reverse`. Bu egzersizde yalnızca `iterable` ve `reverse` bağımsız değişkenlerini belirtmeniz gerekir, `key` bağımsız değişkenini belirtmenize gerek yoktur.

Sizin için iki liste oluşturulmuştur.

Bunları birleştirip azalan düzende sıralayabilir misiniz?

`@instructions`
- `+` işlecini kullanarak `first` ve `second` içeriklerini yeni bir listede birleştirin: `full`.
- `sorted()` fonksiyonunu çağırın ve `full` listesinde `reverse` bağımsız değişkenini `True` olarak belirtin. Sıralanmış listeyi `full_sorted` olarak kaydedin.
- Son olarak `full_sorted` sonucunu yazdırın.

`@hint`
- `first` ve `second` değerlerini iki sayıymış gibi toplayın ve sonucu `full` değişkenine atayın.
- `sorted()` fonksiyonunu iki girdiyle kullanın: `full` ve `reverse=True`.
- Bir değişken yazdırmak için `print()` fonksiyonunu kullanın.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create lists first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# Paste together first and second: full
full = ____ + ____

# Sort full in descending order: full_sorted
full_sorted = ____

# Print out full_sorted
____
```

`@solution`
```{python}
# Create lists first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# Paste together first and second: full
full = first + second

# Sort full in descending order: full_sorted
full_sorted = sorted(full, reverse=True)

# Print out full_sorted
print(full_sorted)
```

`@sct`
```{python}
msg = "Zaten var olan `first` ve `second` değişkenlerini değiştirmenize veya kaldırmanıza gerek yok."
Ex().multi(
  check_object("first", missing_msg=msg).has_equal_value(incorrect_msg=msg),
  check_object("second", missing_msg=msg).has_equal_value(incorrect_msg=msg)
)
Ex().check_correct(
  check_object("full_sorted").has_equal_value(incorrect_msg="`sorted()` fonksiyonunu çağırmanın sonucunu `full_sorted`'a atadığınızdan emin olun."),
  check_function("sorted").multi(
    check_args(0).has_equal_value(),
    check_args('reverse').has_equal_value()
  )
)

success_msg("Harika! Python yöntemleri hakkında videoya geçin.")
```

---

## Yöntemler

```yaml
type: VideoExercise
key: 2b66cb66b1
xp: 50
```

`@projector_key`
8e387776f3a264a745128b68aa8d8f83

---

## Dize Yöntemleri

```yaml
type: NormalExercise
key: 4039302ee0
lang: python
xp: 100
skills:
  - 2
```

Dizeler bir dizi yöntemle birlikte gelir. Bu yöntemlerden bazılarını keşfetmek için talimatları dikkatlice izleyin. Bunları daha ayrıntılı olarak keşfetmek isterseniz IPython Shell’e `help(str)` yazabilirsiniz.

Denemeler yapmanız için bir `place` dizesi oluşturulmuştur.

`@instructions`
- `place` dizesinde `.upper()` [yöntemini](https://docs.python.org/3/library/stdtypes.html#str.upper) kullanın ve sonucu `place_up` içinde depolayın. Önceki videoda öğrendiğiniz yöntemleri çağırmaya yönelik sözdizimini kullanın.
- `place` ve `place_up` sonuçlarının çıktısını alın. İkisi de değişti mi?
- `place` değişkeni üzerinde `.count()` çağrısı yaparak ve `'o'` harfini yönteme girdi olarak geçirerek `place` değişkenindeki o’ların sayısını yazdırın. `place` değişkeninden bahsediyoruz, `"place"` sözcüğünden değil!

`@hint`
- `place` üzerinde `.upper()` yöntemini herhangi bir ek girdi olmadan çağırabilirsiniz.
- Bir `x` değişkeni yazdırmak için `print(x)` yazın.
- `place.count(____)` çağrınızı yazdırabilmek için bir `print()` fonksiyonunda sarmaladığınızdan emin olun.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# string to experiment with: place
place = "poolhouse"

# Use upper() on place
place_up = 

# Print out place and place_up



# Print out the number of o's in place

```

`@solution`
```{python}
# string to experiment with: place
place = "poolhouse"

# Use upper() on place
place_up = place.upper()

# Print out place and place_up
print(place)
print(place_up)

# Print out the number of o's in place
print(place.count('o'))
```

`@sct`
```{python}
msg = "Önceden tanımlanmış değişkenleri değiştirmek veya kaldırmak zorunda değilsiniz."
Ex().check_object("place", missing_msg=msg).has_equal_value(incorrect_msg=msg)

patt = "`%s` ifadesini yazdırmayı unutmayın."
Ex().has_printout(0, not_printed_msg=patt % "place")
Ex().check_correct(
    has_printout(1, not_printed_msg=patt % "place_up"),
    check_correct(
        check_object("place_up").has_equal_value(incorrect_msg="`place.upper()` çağrınızın sonucunu `place_up` değişkenine atayın."),
        check_function("place.upper", signature=False)
    )
)    

# check count of place
Ex().check_correct(
  has_printout(2, not_printed_msg = "`place` içindeki o'ların sayısını doğru hesapladınız; şimdi `place.count('o')` çağrısını bir `print()` fonksiyonuna sararak sonucu yazdırdığınızdan emin olun."),
  check_function("place.count", signature=False).check_args(0).has_equal_value()
)

success_msg("Güzel! Yazdırmalardan, `upper()` metodunun çağrıldığı nesneyi değiştirmediğini fark edin. Bu, bir sonraki alıştırmada listeler için farklı olacaktır!")
```

---

## Liste Yöntemleri

```yaml
type: NormalExercise
key: 0dbe8ed695
lang: python
xp: 100
skills:
  - 2
```

Kendileriyle ilişkili yöntemleri olan tek Python türleri dizeler değildir. Listeler, kayan sayılar, tamsayılar ve boole değerleri de bir dizi kullanışlı yöntem içeren türlerdir. Bu egzersizde şunları deneyeceksiniz:

- Bir listenin ilk elemanıyla eşleşen dizini almak için `.index()` ve
- Bir elemanın bir listede görünme sayısını almak için `.count()`.

Bir evin farklı bölümlerinin alanlarını içeren bir liste üzerinde çalışacaksınız: `areas`.

`@instructions`
- `.index()` yöntemini kullanarak `areas` listesinde `20.0` ile eşit olan elemanın dizinini alın. Bu dizini yazdırın.
- `9.50` değerinin listede kaç kez geçtiğini öğrenmek için `areas` listesinde `.count()` çağrısı yapın. Bu sayıyı da yazdırın.

`@hint`
- Dizini yazdırmak için `areas.index(___)` çağrısını bir `print()` fonksiyonunda sarmalayın.
- `x` elemanının listede kaç kez göründüğünü yazdırmak için `areas.count(___)` çağrısını bir `print()` fonksiyonunda sarmalayın.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Print out the index of the element 20.0


# Print out how often 9.50 appears in areas

```

`@solution`
```{python}
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Print out the index of the element 20.0
print(areas.index(20.0))

# Print out how often 9.50 appears in areas
print(areas.count(9.50))
```

`@sct`
```{python}
predef_msg = "Önceden tanımlanmış `areas` listesini değiştirmek veya kaldırmak zorunda değilsiniz."

Ex().check_object("areas", missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg)

Ex().check_function("print", index=0).check_args(0).check_function('areas.index', signature=False).check_args(0).has_equal_value()

Ex().check_function("print", index=1).check_args(0).check_function('areas.count', signature=False).has_equal_value()

success_msg("Güzel! Bunlar, çağrıldıkları listeyi değiştirmeyen `list` yöntemlerinin örnekleriydi.")
```

---

## Liste Yöntemleri (2)

```yaml
type: NormalExercise
key: 1fbeab82d0
lang: python
xp: 100
skills:
  - 2
```

Çoğu liste yöntemi, üzerinde çağrıldıkları listeyi değiştirir. Örnekler:

- Çağrıldığı listeye bir eleman ekleyen `.append()`.
- Bir listenin girdiyle eşleşen birinci elemanını [kaldıran](https://docs.python.org/3/library/stdtypes.html#typesseq-mutable) `.remove()` ve
- Üzerinde çağrıldığı listedeki elemanların sırasını [tersine çeviren](https://docs.python.org/3/library/stdtypes.html#typesseq-mutable) `.reverse()`.

Evin farklı bölümlerinin alanlarını içeren liste üzerinde çalışacaksınız: `areas`.

`@instructions`
- `.append()` çağrısını iki kez kullanarak havuzlu evin ve garajın boyutunu tekrar ekleyin: sırasıyla `24.5` ve `15.45`. Bunları bu sırayla eklediğinizden emin olun.
- `areas` listesini yazdırın.
- `.reverse()` yöntemini kullanarak `areas` listesindeki elemanların sırasını tersine çevirin.
- `areas` listesini bir kez daha yazdırın.

`@hint`
- Birinci talimat için `areas.append(___)` çağrısını iki kez kullanın.
- Bir `x` değişkeni yazdırmak için `print(x)` yazın.
- `.reverse()` yöntemi ek girdi gerektirmez; nokta gösterimi ve boş parantezler kullanmanız yeterlidir: `.reverse()`.
- Bir `x` değişkeni yazdırmak için `print(x)` yazın.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Use append twice to add poolhouse and garage size



# Print out areas


# Reverse the orders of the elements in areas


# Print out areas

```

`@solution`
```{python}
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Use append twice to add poolhouse and garage size
areas.append(24.5)
areas.append(15.45)

# Print out areas
print(areas)

# Reverse the orders of the elements in areas
areas.reverse()

# Print out areas
print(areas)
```

`@sct`
```{python}
Ex().multi(
  check_function("areas.append", index=0, signature=False).check_args(0).has_equal_value(),
  check_function("areas.append", index=1, signature=False).check_args(0).has_equal_value(),
  check_function("print", index=0).check_args(0).has_equal_ast(),
  check_function("areas.reverse", index=0, signature=False),
  check_function("print", index=1).check_args(0).has_equal_ast()
)

success_msg("Harika!")
```

---

## Paketler

```yaml
type: VideoExercise
key: ab96a17c5e
xp: 50
```

`@projector_key`
cedcfb34350be8545599768f96695cdd

---

## Paketi içe aktarma

```yaml
type: NormalExercise
key: 7432a6376f
lang: python
xp: 100
skills:
  - 2
```

Bir dairenin çevresini ve alanını hesaplamak istediğinizi varsayalım. Bu formüller şu şekilde görünür:

$$C = 2 \pi r$$
$$A = \pi r^2 $$

`pi` sayısını yazmak yerine sayıyı içeren `math` paketini kullanabilirsiniz.

Referans olarak `**`, üs alma işleminin sembolüdür. Örneğin `3**4`, `3` üzeri `4` anlamına gelip `81` sonucunu verir.

`@instructions`
- `math` paketini içe aktarın.
- `math.pi` fonksiyonunu kullanarak dairenin çevresini hesaplayın ve `C` içinde depolayın.
- `math.pi` fonksiyonunu kullanarak dairenin alanını hesaplayın ve `A` içinde depolayın.

`@hint`
- `import math` paketini kullanarak `math.pi` ile `pi` değerine başvurabilirsiniz.
- Atama metnindeki denklemi kullanarak `C` değerini bulun. `*` kullanın.
- Atama metnindeki denklemi kullanarak `A` değerini bulun. `*` ve `**` kullanın.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Import the math package
import ____

# Calculate C
C = 2 * 0.43 * ____

# Calculate A
A = ____ * 0.43 ** 2

print("Circumference: " + str(C))
print("Area: " + str(A))
```

`@solution`
```{python}
# Import the math package
import math

# Calculate C
C = 2 * 0.43 * math.pi

# Calculate A
A = math.pi * 0.43 ** 2

print("Circumference: " + str(C))
print("Area: " + str(A))
```

`@sct`
```{python}
patt = "`%s` hesaplamanız tam olarak doğru değil. `math.pi` kullanmayı unutmayın."
Ex().multi(
  has_import('math', same_as=False),
  check_object('C').has_equal_value(incorrect_msg=patt%'C'),
  check_object('A').has_equal_value(incorrect_msg=patt%'A')
)

Ex().multi(
  has_printout(0, not_printed_msg = "__JINJA__:`{{sol_call}}` ifadesini orada tutarak çevreyi yazdırın."),
  has_printout(1, not_printed_msg = "__JINJA__:`{{sol_call}}` ifadesini orada tutarak alanı yazdırın.")
)

success_msg("Güzel! Paketlerden gelen fonksiyonlarla nasıl başa çıkacağınızı biliyorsanız, birçok Python programcısının gücü parmaklarınızın ucunda!")
```

---

## Seçici içe aktarma

```yaml
type: NormalExercise
key: fe65eff50a
lang: python
xp: 100
skills:
  - 2
```

`import math` gibi genel içe aktarmalar, `math` paketindeki **tüm** fonksiyonları kullanıma açar. Ancak bir paketin yalnızca belirli bir bölümünü kullanmaya karar verirseniz, içe aktarımı her zaman daha seçici hale getirebilirsiniz:

```
from math import pi
```

Aynı şeyi tekrar deneyin ancak bu sefer sadece `pi` kullanın.

`@instructions`
- `math` paketinden yalnızca `pi` fonksiyonunu içe aktararak seçici bir içe aktarma gerçekleştirin.
- `pi` fonksiyonunu kullanarak dairenin çevresini hesaplayın ve `C` içinde depolayın.
- `pi` fonksiyonunu kullanarak dairenin alanını hesaplayın ve `A` içinde depolayın.

`@hint`
- Seçici içe aktarma işlemini gerçekleştirmek için `from math import pi` komutunu kullanın.
- Artık `pi` fonksiyonunu tek başına kullanabilirsiniz!

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Import pi function of math package
from math import ____

# Calculate C
C = 2 * 0.43 * ____

# Calculate A
A = ____ * 0.43 ** 2

print("Circumference: " + str(C))
print("Area: " + str(A))
```

`@solution`
```{python}
# Import pi function of math package
from math import pi

# Calculate C
C = 2 * 0.43 * pi

# Calculate A
A = pi * 0.43 ** 2

print("Circumference: " + str(C))
print("Area: " + str(A))
```

`@sct`
```{python}
patt = "`%s` hesaplamanız tam olarak doğru değil. Yalnızca `pi` kullanmaya dikkat edin."

Ex().has_import("math.pi", not_imported_msg = "`math` paketinden `pi`'yi içe aktardığınızdan emin olun. `from ___ import ___` notasyonunu kullanmalısınız.",)

Ex().multi(
  check_object('C').has_equal_value(incorrect_msg=patt%'C'),
  check_object('A').has_equal_value(incorrect_msg=patt%'A')
)

Ex().multi(
  has_printout(0, not_printed_msg = "__JINJA__:`{{sol_call}}`'i çevreyi yazdırmak için orada tuttuğunuzdan emin olun."),
  has_printout(1, not_printed_msg = "__JINJA__:`{{sol_call}}`'i alanı yazdırmak için orada tuttuğunuzdan emin olun.")
)

success_msg("Güzel! Bir sonraki alıştırmaya geçin.")
```

---

## İçe aktarmanın farklı yolları

```yaml
type: MultipleChoiceExercise
key: f1b2675a2a
lang: python
xp: 50
skills:
  - 2
```

Python’a paket ve modül aktarmanın birkaç yolu vardır. İçe aktarma çağrısına bağlı olarak farklı Python kodu kullanmanız gerekecektir.

`scipy` paketinin `linalg` alt paketinde bulunan `inv()`[fonksiyonunu](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.inv.html) kullanmak istediğinizi varsayalım. Bu fonksiyonu şu şekilde kullanabilmek istiyorsunuz:

```
my_inv([[1,2], [3,4]])
```

Yukarıdaki kodu hata olmadan çalıştırmak için hangi `import` ifadesine ihtiyacınız olur?

`@possible_answers`
- `import scipy`
- `import scipy.linalg`
- `from scipy.linalg import my_inv`
- `from scipy.linalg import inv as my_inv`

`@hint`
- IPython kabuğunda farklı import ifadeleri deneyin ve hangisinin `my_inv([[1, 2], [3, 4]])` satırının hatasız çalışmasına neden olduğunu görün. Yazdığınız kodu çalıştırmak için **Enter** tuşuna basın.

`@pre_exercise_code`
```{python}

```

`@sct`
```{python}
msg1 = msg2 = msg3 = "Yanlış, tekrar deneyin. Farklı import ifadelerini IPython kabuğunda deneyin ve `my_inv([[1, 2], [3, 4]])` satırının hatasız çalışmasına hangi ifadenin neden olduğunu görün."
msg4 = "Doğru! `as` kelimesi, içe aktardığınız fonksiyon için yerel bir ad oluşturmanıza olanak tanır: `inv()` artık `my_inv()` olarak kullanılabilir."
Ex().has_chosen(4, [msg1, msg2, msg3, msg4])
```

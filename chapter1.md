---
title_meta: Bölüm 1
title: Python’ın Temelleri
description: >-
  Python’ın temel kavramlarına giriş. Python’ı interaktif olarak ve komut
  kullanarak nasıl kullanacağınızı öğrenin. İlk değişkenlerinizi oluşturun ve
  Python’ın temel veri türlerini öğrenin.
attachments:
  slides_link: 'https://projector-video-pdf-converter.datacamp.com/735/chapter1.pdf'
free_preview: true
lessons:
  - nb_of_exercises: 3
    title: Merhaba Python!
  - nb_of_exercises: 5
    title: Değişkenler ve Türler
---

## Merhaba Python!

```yaml
type: VideoExercise
key: f644a48d5d
xp: 50
```

`@projector_key`
d8fcd4c930027fa4e1c3870c7e7e0ff1

---

## İlk Python kodunuz

```yaml
type: NormalExercise
key: bdc52f0e19
lang: python
xp: 100
skills:
  - 2
```

İlk Python kodunuzu çalıştırmanın zamanı geldi!

Koda gidin ve kodu çalıştır düğmesine basarak çıktıyı görün.

`@instructions`
- `print(5 / 8)` komutunun çıktısını görmek için çalıştır düğmesine basın.

`@hint`
- Cevabınızı göndermeden önce çıktıyı incelemek için kodu çalıştırın.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Hit run code to see the output!
print(5 / 8)
```

`@solution`
```{python}
# Hit run code to see the output!
print(5 / 8)
```

`@sct`
```{python}
Ex().has_printout(0, not_printed_msg = "__JINJA__:`{{sol_call}}` ifadesini `5 / 8`'i yazdırmak için kullandınız mı?")
success_msg("Harika! Bir sonrakine geçelim!")
```

---

## Hesap makinesi olarak Python

```yaml
type: NormalExercise
key: 0f7c039428
lang: python
xp: 100
skills:
  - 2
```

Python basit hesaplamalar için mükemmel bir seçimdir. Toplama, çıkarma, çarpma ve bölme işlemlerini yapabilir.

Komuttaki kodda birkaç örnek veriliyor.

Şimdi sıra sizde, kendiniz kod yazarak alıştırma yapın.

`@instructions`
- `print()` fonksiyonunu kullanarak `# Subtraction` altında `5` değerinden `5` çıkarma işleminin sonucunu yazdırın.
- `# Multiplication` altında `3` ile `5` çarpımının sonucunu yazdırın.

`@hint`
- Çıktı oluşturmak için `print()` fonksiyonunu kullanmanız gerekir.
- `-` ile çıkarma, `*` ile çarpma yapabilirsiniz.

`@pre_exercise_code`
```{python}
 
```

`@sample_code`
```{python}
# Addition and division
print(4 + 5)
print(10 / 2)

# Subtraction
print()

# Multiplication

```

`@solution`
```{python}
# Addition and division
print(4 + 5)
print(10 / 2)

# Subtraction
print(5 - 5)

# Multiplication
print(3 * 5)
```

`@sct`
```{python}
Ex().has_printout(0, not_printed_msg = "`print(4 + 5)` ifadesini kullanarak toplamanızın sonucunu yazdırdınız mı?")

Ex().has_printout(1, not_printed_msg = "`print(5 - 5)` ifadesini kullanarak çıkarma işleminizin sonucunu yazdırdınız mı?")

Ex().has_printout(2, not_printed_msg = "`print(3 * 5)` ifadesini kullanarak çarpma işleminizin sonucunu yazdırdınız mı?")

Ex().has_printout(3, not_printed_msg = "`print(10 / 2)` ifadesini kullanarak bölme işleminizin sonucunu yazdırdınız mı?")

success_msg("Bu doğru! Python, matematik yapmanıza yardımcı olabilir, bu da veri becerilerimizi geliştirirken analiz için faydalı olacaktır.")
```

---

## Değişkenler ve Türler

```yaml
type: VideoExercise
key: c2e396792e
xp: 50
```

`@projector_key`
433dcfcfedaee070cbf440491c402e3b

---

## Değişken Atama

```yaml
type: NormalExercise
key: 4bf65ad83e
lang: python
xp: 100
skills:
  - 2
```

Python’da değişken, bir değere ad ile başvurmanıza olanak tanır. `5` değerine sahip bir `x` değişkeni oluşturmak için aşağıdaki örnekte olduğu gibi `=` işlecini kullanırsınız:

```
x = 5
```

Artık bu değişkenin gerçek değeri olan `5` yerine adı olan `x` değerini kullanabilirsiniz.

Unutmayın, Python’da `=`, _atama_ anlamına gelir, eşitliği test etmez! `____` ifadesini kendi kodunuzla değiştirerek egzersizde deneyin.

`@instructions`
- `100` değerine sahip bir `savings` değişkeni oluşturun.
- Komuta `print(savings)` yazarak bu değişkeni kontrol edin.

`@hint`
- `savings` değişkenini oluşturmak için `savings = 100` yazın.
- `savings` değişkenini oluşturduktan sonra `print(savings)` yazabilirsiniz.
- Son kodunuzda `____` bulunmamalıdır.

`@pre_exercise_code`
```{python}
 
```

`@sample_code`
```{python}
# Create a variable savings
____

# Print out savings
____
```

`@solution`
```{python}
# Create a variable savings
savings = 100

# Print out savings
print(savings)
```

`@sct`
```{python}
Ex().check_object("savings").has_equal_value(incorrect_msg="`savings` değişkenine `100` atayın.")
Ex().has_printout(0, not_printed_msg = "`savings` değişkenini `print(savings)` ile yazdırın.")
success_msg("Harika! Şimdi bu değişkenle bazı hesaplamalar yapmayı deneyelim!")
```

---

## Değişkenlerle hesaplamalar

```yaml
type: NormalExercise
key: ff06cedeb4
lang: python
xp: 100
skills:
  - 2
```

Bir savings değişkeni oluşturduğunuza göre para biriktirmeye başlayalım!

Gerçek değerlerle hesaplama yapmak yerine değişkenleri kullanabilirsiniz.

Her ay $10 biriktirseydiniz dört ay sonunda ne kadar para biriktirmiş olurdunuz?

`@instructions`
- `10` değerine eşit bir `monthly_savings` değişkeni ve `4` değerine eşit bir `num_months` değişkeni oluşturun.
- `monthly_savings` değerini `num_months` ile çarpın ve `new_savings` sütununa atayın.
- `new_savings` değerini yazdırın.

`@hint`
- Değişkenlerle de tıpkı sayılarla olduğu gibi hesaplamalar yapabilirsiniz. Bu yüzden `10 * 4` yerine sayıları değişkenlerle değiştirin!
- `new_savings` içinde tutarı görmek için `print()` komutunu kullanın.
- Değişkenleri doğru yazmaya dikkat edin!

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create the variables monthly_savings and num_months



# Multiply monthly_savings and num_months
new_savings = ____

# Print new_savings

```

`@solution`
```{python}
# Create the variables monthly_savings and num_months
monthly_savings = 10
num_months = 4

# Multiply monthly_savings and num_months
new_savings = monthly_savings * num_months

# Print new_savings
print(new_savings)
```

`@sct`
```{python}
Ex().check_object("monthly_savings").has_equal_value(incorrect_msg = "`monthly_savings` değişkenine `monthly_savings = 10` ifadesini kullanarak `10` değerini kaydettiniz mi?")
Ex().check_object("num_months").has_equal_value(incorrect_msg = "`num_months` değişkenine `num_months = 4` ifadesini kullanarak `4` değerini kaydettiniz mi?")
Ex().check_object("new_savings").has_equal_value(incorrect_msg = "Çarpmak için doğru değişkenleri ve sembolleri kullandınız mı? Beklenen `monthly_savings * num_months` ifadesiydi ancak başka bir şey elde edildi.")
# Ex().check_object("total_savings").has_equal_value(incorrect_msg = "Toplamak için doğru değişkenleri ve sembolleri kullandınız mı? Beklenen `savings + new_savings` ifadesiydi ancak başka bir şey elde edildi.")

Ex().has_printout(0, not_printed_msg="Scriptinizin sonunda `new_savings` değerini yazdırmayı unutmayın.")

success_msg("Yeni birikimlerinizde $40 var!")
```

---

## Diğer değişken türleri

```yaml
type: NormalExercise
key: 006b48561f
lang: python
xp: 100
skills:
  - 2
```

Önceki egzersizde tamsayı Python veri türüyle çalıştınız:

- `int` veya tamsayı: kesirli kısmı olmayan sayı. Değeri `100` olan `savings`, bir tamsayı örneğidir.

Sayısal veri türlerinin yanında üç tane daha çok yaygın veri türü vardır:

- `float` veya kayan sayı: bir nokta ile ayrılmış tamsayı ve kesirli kısımdan oluşan sayı. `1.1` bir kayan sayı örneğidir.
- `str` veya dize: metni temsil eden bir tür. Bir dize oluşturmak için tek veya çift tırnak işareti kullanabilirsiniz.
- `bool` veya boole: mantıksal değerleri temsil eden bir tür. Sadece `True` veya `False` olabilir (büyük harf kullanımı önemlidir!).

`@instructions`
- Değeri `0.5` olan `half` adlı yeni bir kayan sayı oluşturun.
- Değeri `"Hello! How are you?"` olan `intro` adlı yeni bir dize oluşturun.
- Değeri `True` olan `is_good` adlı yeni bir boole oluşturun.

`@hint`
- Python’da bir değişken oluşturmak için `=` kullanın. Dizeyi tek veya çift tırnak içine aldığınızdan emin olun.
- Python’da sadece iki boole değeri vardır: `True` ve `False`. `TRUE`, `true`, `FALSE`, `false` ve diğer versiyonlar kabul edilmez.

`@pre_exercise_code`
```{python}

```

`@sample_code`
```{python}
# Create a variable half


# Create a variable intro


# Create a variable is_good

```

`@solution`
```{python}
# Create a variable half
half = 0.5

# Create a variable intro
intro = "Hello! How are you?"

# Create a variable is_good
is_good = True
```

`@sct`
```{python}
Ex().check_object("half").has_equal_value(incorrect_msg = "Float, `0.5` değerini `half` olarak kaydettiniz mi?")

Ex().check_object("intro").has_equal_value(incorrect_msg = "Hmm, `intro` değişkeninizde bir şey yanlış. Yazımı tekrar kontrol edin ve tırnak işaretlerini kullandığınızdan emin olun.")

Ex().check_object("is_good").has_equal_value(incorrect_msg = "Boolean değerini büyük harfle mi yazdınız? Burada tırnak işaretlerine ihtiyacınız olmadığını unutmayın.")

success_msg("Güzel!")
```

---

## Diğer türlerle işlemler

```yaml
type: BulletExercise
key: 4d0d83cc02
xp: 100
```

Python’da değişkenler farklı türlerde olabilir. `type()` fonksiyonunu kullanarak bir değişkenin türünü görebilirsiniz. Örneğin `a` türünü görmek için `type(a)` komutunu yürütün.

Python’da farklı türler farklı şekilde davranır. Örneğin iki dizeyi topladığınızda, iki tamsayı veya iki boole değerini topladığınızda elde edeceğinizden farklı bir sonuç elde edersiniz.

Şimdi bunu deneme zamanı.

`@pre_exercise_code`
```{python}

```

***

```yaml
type: NormalExercise
key: f4e91c4ae9
xp: 50
```

`@instructions`
- `savings` ile `new_savings` değerlerini toplayıp `total_savings` değişkenine atayın.
- Elde edilen `total_savings` türünü yazdırmak için `type()` komutunu kullanın.

`@hint`
- `savings + new_savings` değerini `total_savings` adlı yeni bir değişkene atayın.
- `x` değişkeninin türünü yazdırmak için `print(type(x))` komutunu kullanın.

`@sample_code`
```{python}
savings = 100
new_savings = 40

# Calculate total_savings using savings and new_savings
____
print(total_savings)

# Print the type of total_savings
print(____)
```

`@solution`
```{python}
savings = 100
new_savings = 40

# Calculate total_savings using savings and new_savings
total_savings = savings + new_savings
print(total_savings)

# Print the type of total_savings
print(type(total_savings))
```

`@sct`
```{python}
# predefined
msg = "Önceden tanımlanmış değişkenleri değiştirmek veya kaldırmak zorunda değilsiniz."

Ex().multi(
    check_object('savings', missing_msg=msg).has_equal_value(incorrect_msg=msg),
    check_object('new_savings', missing_msg=msg).has_equal_value(incorrect_msg=msg)
)

Ex().multi(
    check_object("total_savings").has_equal_value(incorrect_msg="`total_savings` değişkenini oluşturmak için `savings` ve `new_savings`'i ekleyin."),
    has_printout(1, not_printed_msg = "__JINJA__:`total_savings`'in türünü yazdırmak için `{{sol_call}}` kullanın.")
)
```

***

```yaml
type: NormalExercise
key: f54fbf9bd9
xp: 50
```

`@instructions`
- `intro` ile `intro` değerlerinin toplamını hesaplayın ve sonucu `doubleintro` değişkenine atayın.
- `doubleintro` değerini yazdırın. Bu sonucu bekliyor muydunuz?

`@hint`
- `intro + intro` değerini `doubleintro` adlı yeni bir değişkene atayın.
- Bir `x` değişkeni yazdırmak için komut dosyasına `print(x)` yazın.

`@sample_code`
```{python}
intro = "Hello! How are you?"

# Assign sum of intro and intro to doubleintro
____

# Print out doubleintro
print(____)
```

`@solution`
```{python}
intro = "Hello! How are you?"

# Assign sum of intro and intro to doubleintro
doubleintro = intro + intro

# Print out doubleintro
print(doubleintro)
```

`@sct`
```{python}
# predefined
msg = "Önceden tanımlanmış değişkenleri değiştirmenize veya kaldırmanıza gerek yok."

Ex().check_object('intro', missing_msg=msg).has_equal_value(incorrect_msg=msg)

Ex().multi(
    check_object("doubleintro").has_equal_value(incorrect_msg  = "`intro + intro` sonucunu `doubleintro` içinde sakladınız mı?"),
    has_printout(0, not_printed_msg = "`doubleintro`'u yazdırmayı unutmayın.")
)

success_msg("Güzel. `intro + intro`'nun `\"Hello! How are you?\"` ve `\"Hello! How are you?\"` ifadelerinin birleştirilmesine neden olduğunu fark edin.")
```

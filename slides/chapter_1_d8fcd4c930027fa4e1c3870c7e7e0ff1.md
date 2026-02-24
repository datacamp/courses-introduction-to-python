---
title: Insert title here
key: d8fcd4c930027fa4e1c3870c7e7e0ff1
video_link:
  mp3: >-
    https://videos.datacamp.com/mp3/translations/course_735/tr-TR/b09d375b-4d83-4701-9913-51d4c37fe376.mp3
---

## Merhaba Python!

```yaml
type: TitleSlide
key: f743ca8c41
```

`@lower_third`
name: Hugo Bowne-Anderson
title: Data Scientist at DataCamp

`@script`
Merhaba, ben Hugo. Veri Bilimi için Python’a Giriş dersinde sana rehberlik edeceğim.

Ben DataCamp’te veri bilimci ve eğitmenim.

---

## Nasıl öğreneceksiniz

```yaml
type: FullSlide
key: 30ee08a725
disable_transition: true
```

`@part1`
![DataCamp Arayüzü](https://assets.datacamp.com/img/translations/tr-TR/production/repositories/288/datasets/729574d2168960686381caefe79baf5978e27d0d/liveexercise.gif)

`@script`
Bu derste, bunun gibi video derslerle ve etkileşimli alıştırmalarla Veri Bilimi için Python öğreneceksin. Kendi Python oturumun olacak; orada deney yap, yönergeleri çözmek için doğru kodu yazmayı dene. Yapa yapa öğreneceksin ve çalışmana anlık, kişiselleştirilmiş geri bildirim alacaksın.

---

## Python

```yaml
type: FullSlide
key: 3f23b93572
```

`@part1`
![guido-hba.png](https://assets.datacamp.com/img/translations/tr-TR/production/repositories/288/datasets/fb3e4b8dc114529dafffb37d33f2b2244210d40f/guido-hba.png = 38){{1}}

- Genel amaçlı: her şeyi inşa edin{{2}}

- Açık kaynak! Ücretsiz!{{3}}

- Python paketleri, veri bilimi için de{{4}}

	- Birçok uygulama ve alan{{5}}

`@script`
Python, Guido Van Rossum tarafından tasarlandı. Burada, Guido ile birlikte bir fotoğrafımı görüyorsun. Bir hobi projesi olarak başlayan şey, kısa sürede genel amaçlı bir programlama diline dönüştü: günümüzde Python ile neredeyse her tür yazılımı geliştirebilirsin. Peki bu nasıl oldu? Öncelikle, Python açık kaynak. Kullanımı ücretsiz. Ayrıca Python’da paketler geliştirmek çok kolay; bunlar, belirli sorunları çözmek için başkalarıyla paylaşabileceğin kod parçaları. Zamanla, veri bilimine özel giderek daha fazla paket geliştirildi. Diyelim ki şirketinin satışlarına dair havalı görselleştirmeler yapmak istiyorsun. Bunun için bir paket var. Ya da sensör ölçümlerini analiz etmek için bir veritabanına bağlanmak istiyorsun. Bunun için de bir paket var.
İnsanlar Python’u, neredeyse her şeyi yapabildiğin için, programlama dillerinin İsviçre çakısı diye anıyor.
Bu kursta, veri bilimi kodlama becerilerini adım adım geliştireceğiz; dilin ne kadar güçlü olduğunu görmek için bizimle kal.

---

## IPython Shell

```yaml
type: FullSlide
key: 43a91a7217
```

`@part1`
**Python komutları çalıştırın**

![ipython_shell.png](https://assets.datacamp.com/img/translations/tr-TR/production/repositories/288/datasets/a9e8440bb8fbd49e4a73e4c36ef1cd677c0dd55f/pyexercise.png = 95)

`@script`
Madem Python için kulak kesildin, hadi denemelere başlayalım. Ben başlıyorum

---

## IPython Shell

```yaml
type: FullSlide
key: 9c51ee700d
disable_transition: true
```

`@part1`
**Python komutları çalıştırın**

![vurgulu ipython_shell_highlighted.png](https://assets.datacamp.com/img/translations/tr-TR/production/repositories/288/datasets/dd43cc0183b15b43a072eb0fbab4caa72dee9250/pyexercise_shell.jpg = 95)

`@script`
Python kabuğuyla; Python kodunu yazıp sonucu anında görebileceğin bir yer. DataCamp’in alıştırma arayüzünde bu kabuk burada gömülü. Basitten başlayalım ve Python’u bir hesap makinesi gibi kullanalım.

---

## IPython Shell

```yaml
type: FullSlide
key: 524e4c20a7
disable_transition: true
```

`@part1`
&nbsp;

![DataCamp'in IPython shell'inde hesaplamalar](https://assets.datacamp.com/img/translations/tr-TR/production/repositories/288/datasets/cee32b788a62e4b9a1234ccde56ac9ebb49cfa72/shelladdition.gif = 95)

`@script`
Dört artı beş yazıp Enter’a basayım. Python yazdıklarını yorumlar ve hesaplamanın sonucunu, yani dokuzu yazdırır. Burada kullanılan Python kabuğu aslında orijinali değil; IPython kullanıyoruz, uzun adıyla Interactive Python. Bu, ileride işimize yarayacak, güçlendirilmiş bir Python sürümü gibi düşünebilirsin.

IPython, Fernando Pérez tarafından oluşturuldu ve daha geniş Jupyter ekosisteminin bir parçası. Python’la etkileşimli çalışmanın yanında, Python’a sözde

---

## Python Betiği

```yaml
type: FullSlide
key: 78ef256bc0
```

`@part1`
- Metin dosyaları - `.py`{{1}}

- Python komutlarının listesi{{2}}

- IPython Shell'de yazmaya benzer{{3}}

![DataCamp'te Python betiği](https://assets.datacamp.com/img/translations/tr-TR/production/repositories/288/datasets/59f196e96536543a4fb8801228019fc4106f3791/pyexercise_script.jpg = 78){{3}}

`@script`
python script’leri de çalıştırabilirsin. Bu python script’leri, uzantısı nokta py olan düz metin dosyalarıdır. Temelde, sanki komutları kabukta satır satır yazıyormuşsun gibi yürütülen Python komutları listesidir.

---

## Python Betiği

```yaml
type: FullSlide
key: 717d124175
disable_transition: true
```

`@part1`
![GIF: betiğe 4 + 5 yazıp yanıtı gönderme. Çıktı yok.](https://assets.datacamp.com/img/translations/tr-TR/production/repositories/288/datasets/2f96e979012e15329cc158d1e0f496aac3539f45/scriptnoprint.gif = 95)

`@script`
Şimdi önceki komutu bir script’in içine koyalım; DataCamp’in arayüzünde burada bulabilirsin. Sonraki adım, “Submit Answer”a tıklayarak script’i çalıştırmak. Script’i DataCamp arayüzünde çalıştırırsan, çıktı bölümünde hiçbir şey görmezsin. Çünkü yürütme sırasında çıktı üretmek istiyorsan, script’lerin içinde açıkça print kullanman gerekir.

---

## Python Betiği

```yaml
type: FullSlide
key: c7a9d02fb6
disable_transition: true
code_zoom: 90
```

`@part1`
![python_script_print.gif](https://assets.datacamp.com/img/translations/tr-TR/production/repositories/288/datasets/8b13d046bb54dcb11aa49f0da7363781129d1561/scriptwithprint.gif = 95)

- Betikten çıktı almak için `print()` kullanın

`@script`
Önceki hesabımızı bir print çağrısına alalım ve script’i yeniden çalıştıralım. Bu kez, öncekiyle aynı çıktı üretildi, harika! Kodunu her adımı elle tekrar yazmak yerine Python script’lerine koymak, düzeni korumana yardım eder ve bir değişiklik yapmak istediğinde her şeyi tekrar yazmaktan kurtarır; değişikliği script’te yap, sonra tamamını yeniden çalıştır.

---

## DataCamp Arayüzü

```yaml
type: FullSlide
key: 693ba1cd14
```

`@part1`
![DataCamp arayüzünün ekran görüntüsü](https://assets.datacamp.com/img/translations/tr-TR/production/repositories/288/datasets/a9e8440bb8fbd49e4a73e4c36ef1cd677c0dd55f/pyexercise.png)

`@script`
Artık Python’la çalışmanın farklı yollarına dair bir fikrin olduğuna göre, alıştırmalara geçmeni öneririm. Deney yapmak için IPython Shell’i kullan ve gerçek cevabı yazmak için Python script düzenleyicisini kullan. “Submit Answer”a tıklarsan, script’in çalıştırılır ve doğruluğu kontrol edilir.

---

## Hadi pratik yapalım!

```yaml
type: FinalSlide
key: 7445cd202e
```

`@script`
Koda dal ve eğlenmeyi unutma!

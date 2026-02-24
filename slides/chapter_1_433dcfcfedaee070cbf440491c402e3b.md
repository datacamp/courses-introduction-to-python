---
title: Insert title here
key: 433dcfcfedaee070cbf440491c402e3b
video_link:
  mp3: >-
    https://videos.datacamp.com/mp3/translations/course_735/id-ID/43f617e9-3188-41f2-854e-44fd52246f32.mp3
---

## Variabel dan Tipe

```yaml
type: TitleSlide
key: dc8b62f1c8
```

`@lower_third`
name: Hugo Bowne-Anderson
title: Data Scientist at DataCamp

`@script`
Kerja bagus, dan selamat datang kembali! Jelas bahwa Python adalah kalkulator yang hebat. Namun, jika Anda ingin melakukan perhitungan yang lebih kompleks, Anda pasti ingin "menyimpan" nilai selama Anda sedang menulis kode.
---

## Variabel

```yaml
type: FullSlide
key: 36ec318b41
```

`@part1`
- Nama yang spesifik dan peka huruf besar-kecil

- Memanggil nilai melalui nama variabel{{1}}

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
Anda bisa melakukan ini dengan mendefinisikan sebuah variabel, dengan nama tertentu yang peka terhadap huruf besar-kecil. Setelah Anda membuat (atau mendeklarasikan) variabel tersebut, Anda bisa memanggil nilainya kapan pun dengan mengetikkan nama variabel tersebut.

Misalkan Anda mengukur tinggi dan berat badan dalam satuan metrik: tinggi Anda 1.79 meter, dan berat 68.7 kilogram. Anda dapat menugaskan nilai-nilai ini ke dua variabel, bernama tinggi badan dan berat badan, dengan tanda sama-dengan:

Jika sekarang Anda mengetik nama variabel, tinggi badan,

Python mencari nama variabel itu, mengambil nilainya, dan mencetaknya.
---

## Hitung Indeks Massa Tubuh (BMI)

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

$$ \text{BMI} = \frac{\text{berat badan}}{\text{tinggi badan}^2} $${{1}}

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
Sekarang, mari hitung Body Mass Index, atau BMI, yang dihitung seperti berikut, dengan berat dalam kilogram dan tinggi dalam meter. Anda bisa melakukannya dengan nilai sebenarnya, tetapi Anda juga bisa memakai variabel tinggi badan dan berat badan, seperti di sini. Setiap kali Anda mengetik nama variabel, Anda meminta Python menggantinya dengan nilai sebenarnya dari variabel itu, berat badan sama dengan 68.7, dan tinggi badan sama dengan 1.79.

Terakhir, versi ini membuat Python menyimpan hasilnya dalam variabel baru, bmi. Sekarang bmi berisi nilai yang sama seperti yang Anda hitung sebelumnya.

Di Python, variabel digunakan sepanjang waktu. Variabel membantu membuat kode Anda dapat direproduksi.
---

## Kemampuan untuk direproduksi

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
Misalkan kode untuk membuat variabel tinggi badan, berat badan, dan bmi ada di dalam sebuah skrip, seperti ini. Jika sekarang Anda ingin menghitung ulang bmi untuk berat yang berbeda,
---

## Kemampuan untuk direproduksi

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
Anda cukup mengubah deklarasi variabel berat badan, lalu menjalankan ulang skripnya. Nilai bmi akan ikut berubah, karena nilai variabel berat badan juga berubah.

Sejauh ini, kita hanya bekerja dengan nilai numerik, seperti tinggi dan berat.
---

## Tipe-tipe Python

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
Di Python, angka-angka ini punya tipe tertentu. Anda bisa memeriksa tipe suatu nilai dengan fungsi type. Untuk melihat tipe dari nilai bmi kita, cukup tulis type lalu bmi di dalam tanda kurung. Anda bisa melihat bahwa tipenya float, cara Python merepresentasikan bilangan riil, yaitu bilangan yang dapat memiliki bagian bulat dan bagian pecahan. Python juga memiliki tipe untuk bilangan bulat: int, seperti contoh ini.

Namun, untuk melakukan data sains, Anda akan butuh lebih dari sekadar int dan float.
---

## Tipe-tipe Python (2)

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
Python memiliki banyak sekali tipe data lainnya. Tipe data yang paling umum adalah string dan boolean.

String adalah cara Python merepresentasikan teks. Anda bisa menggunakan tanda kutip ganda maupun tunggal untuk membuat string, seperti yang terlihat pada contoh ini. Jika Anda mencetak tipe variabel terakhir di sini, Anda akan melihat tipenya adalah str, singkatan dari string.

Boolean adalah tipe yang hanya bisa bernilai True atau False. Anda bisa menganggapnya seperti "Ya" dan "Tidak" dalam bahasa sehari-hari. Boolean akan sangat berguna nanti, misalnya untuk melakukan operasi penyaringan pada data Anda.

Ada hal khusus tentang tipe data Python.
---

## Tipe-tipe Python (3)

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

- Jenis yang berbeda = perilaku yang berbeda!{{3}}

`@script`
Perhatikan baris kode ini yang menjumlahkan dua integer, lalu baris kode ini yang menjumlahkan dua string.

Dua integer tersebut nilainya dijumlahkan, sedangkan untuk dua string teksnya digabungkan menjadi satu. Operator plus berperilaku berbeda untuk tipe data yang berbeda. Ini adalah prinsip umum: bagaimana kode berperilaku tergantung pada tipe yang Anda gunakan.

Dalam latihan setelah ini, Anda akan membuat variabel pertama Anda dan bereksperimen dengan beberapa tipe data Python. Sampai jumpa di video berikutnya untuk membahas semuanya tentang daftar.
---

## Ayo berlatih!

```yaml
type: FinalSlide
key: b7fc40db4d
```

`@script`
Ayo mulai melakukan koding, dan saya tidak sabar bertemu Anda di bab berikutnya saat Anda membangun grafik Python yang lebih menakjubkan lagi.

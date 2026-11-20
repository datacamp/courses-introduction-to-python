---
title_meta: Bab 1
title: Dasar-dasar Python
description: >-
  Pengantar konsep dasar Python. Pelajari cara menggunakan Python secara
  interaktif dan melalui skrip. Buat variabel pertama Anda dan kenali tipe data
  dasar Python.
attachments:
  slides_link: 'https://projector-video-pdf-converter.datacamp.com/735/chapter1.pdf'
free_preview: true
lessons:
  - nb_of_exercises: 3
    title: 'Halo, Python!'
  - nb_of_exercises: 5
    title: Variabel dan Tipe
---

## Halo, Python!

```yaml
type: VideoExercise
key: f644a48d5d
xp: 50
```

`@projector_key`
d8fcd4c930027fa4e1c3870c7e7e0ff1

---

## Kode Python pertama Anda

```yaml
type: NormalExercise
key: bdc52f0e19
lang: python
xp: 100
skills:
  - 2
```

Saatnya menjalankan kode Python pertama Anda!

Buka bagian kode dan tekan tombol jalankan kode untuk melihat hasilnya.

`@instructions`
- Tekan tombol jalankan kode untuk melihat hasil dari `print(5 / 8)`.

`@hint`
- Jalankan kodenya terlebih dahulu sebelum mengirim jawaban Anda agar Anda punya waktu untuk mengeksplorasi hasilnya.

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
Ex().has_printout(0, not_printed_msg = "__JINJA__:Apakah kamu sudah menggunakan `{{sol_call}}` untuk mencetak `5 / 8`?")
success_msg("Bagus! Lanjut ke yang berikutnya!")
```

---

## Python sebagai kalkulator

```yaml
type: NormalExercise
key: 0f7c039428
lang: python
xp: 100
skills:
  - 2
```

Python sangat cocok untuk melakukan perhitungan dasar. Python dapat melakukan penjumlahan, pengurangan, perkalian, dan pembagian.

Kode dalam skrip memberikan beberapa contoh.

Sekarang giliran Anda berlatih dengan menulis beberapa kode sendiri.

`@instructions`
- Cetak hasil pengurangan `5` dengan `5` di bawah `# Subtraction` menggunakan `print()`.
- Cetak hasil perkalian `3` dengan `5` di bawah `# Multiplication`.

`@hint`
- Anda perlu menggunakan `print()` untuk menghasilkan output.
- Anda dapat melakukan pengurangan dengan `-` dan perkalian dengan `*`.

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
Ex().has_printout(0, not_printed_msg = "Apakah kamu sudah menggunakan `print(4 + 5)` untuk mencetak hasil penjumlahanmu?")

Ex().has_printout(1, not_printed_msg = "Apakah kamu sudah menggunakan `print(5 - 5)` untuk mencetak hasil penguranganmu?")

Ex().has_printout(2, not_printed_msg = "Apakah kamu sudah menggunakan `print(3 * 5)` untuk mencetak hasil perkalianmu?")

Ex().has_printout(3, not_printed_msg = "Apakah kamu sudah menggunakan `print(10 / 2)` untuk mencetak hasil pembagianmu?")

success_msg("Itu benar! Python bisa membantumu melakukan perhitungan, sebuah karakteristik yang akan berguna untuk analisis saat kita mengembangkan keterampilan data kita.")
```

---

## Variabel dan Tipe

```yaml
type: VideoExercise
key: c2e396792e
xp: 50
```

`@projector_key`
433dcfcfedaee070cbf440491c402e3b

---

## Penetapan Variabel

```yaml
type: NormalExercise
key: 4bf65ad83e
lang: python
xp: 100
skills:
  - 2
```

Di Python, sebuah variabel memungkinkan Anda merujuk suatu nilai dengan sebuah nama. Untuk membuat variabel `x` dengan nilai `5`, Anda menggunakan `=`, seperti contoh berikut:

```
x = 5
```

Sekarang Anda dapat menggunakan nama variabel ini, `x`, alih-alih nilai sebenarnya, `5`.

Ingat, `=` dalam Python berarti -_penugasan_, bukan untuk menguji kesetaraan! Cobalah pada latihan ini dengan mengganti `____` dengan kode Anda.

`@instructions`
- Buat variabel `savings` dengan nilai `100`.
- Periksa variabel ini dengan mengetik `print(savings)` di skrip.

`@hint`
- Ketik `savings = 100` untuk membuat variabel `savings`.
- Setelah membuat variabel `savings`, Anda dapat mengetik `print(savings)`.
- Kode akhir Anda tidak boleh menyertakan `____`.

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
Ex().check_object("savings").has_equal_value(incorrect_msg="Tetapkan `100` ke variabel `savings`.")
Ex().has_printout(0, not_printed_msg = "Cetak `savings`, variabel yang kamu buat, dengan `print(savings)`.")
success_msg("Bagus! Ayo coba lakukan beberapa perhitungan dengan variabel ini sekarang!")
```

---

## Perhitungan dengan variabel

```yaml
type: NormalExercise
key: ff06cedeb4
lang: python
xp: 100
skills:
  - 2
```

Anda sekarang telah membuat sebuah variabel tabungan, jadi mari mulai menabung!

Alih-alih menghitung dengan nilai sebenarnya, Anda dapat menggunakan variabel.

Berapa banyak uang yang akan Anda tabung empat bulan dari sekarang, jika Anda menabung $10 setiap bulan?

`@instructions`
- Buat variabel `monthly_savings` bernilai `10` dan `num_months` bernilai `4`.
- Kalikan `monthly_savings` dengan `num_months` dan tetapkan ke `new_savings`.
- Cetak nilai `new_savings`.

`@hint`
- Anda dapat melakukan perhitungan dengan variabel sama seperti dengan angka, jadi alih-alih `10 * 4`, gantilah angkanya dengan variabel!
- Gunakan `print()` untuk melihat jumlah dalam `new_savings`.
- Pastikan ejaan nama variabel ditulis dengan benar!

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
Ex().check_object("monthly_savings").has_equal_value(incorrect_msg = "Apakah kamu menyimpan `10` ke `monthly_savings` menggunakan `monthly_savings = 10`?")
Ex().check_object("num_months").has_equal_value(incorrect_msg = "Apakah kamu menyimpan `4` ke `num_months` menggunakan `num_months = 4`?")
Ex().check_object("new_savings").has_equal_value(incorrect_msg = "Apakah kamu menggunakan variabel dan simbol yang benar untuk mengalikan? Diharapkan `monthly_savings * num_months` tetapi mendapatkan sesuatu yang lain.")
# Ex().check_object("total_savings").has_equal_value(incorrect_msg = "Apakah kamu menggunakan variabel dan simbol yang benar untuk menambahkan? Diharapkan `savings + new_savings` tetapi mendapatkan sesuatu yang lain.")

Ex().has_printout(0, not_printed_msg="Ingat untuk mencetak `new_savings` di akhir skripmu.")

success_msg("Kamu punya $40 dalam tabungan baru!")
```

---

## Tipe variabel lainnya

```yaml
type: NormalExercise
key: 006b48561f
lang: python
xp: 100
skills:
  - 2
```

Pada latihan sebelumnya, Anda bekerja dengan tipe data bilangan bulat di Python:

- `int`, atau integer: bilangan tanpa bagian pecahan. `savings` dengan nilai `100` adalah contoh integer.

Selain tipe data numerik tersebut, ada tiga tipe data lain yang sangat umum:

- `float`, atau floating point: bilangan yang memiliki bagian bulat dan pecahan, dipisahkan oleh titik. `1.1` adalah contoh float.
- `str`, atau string: tipe untuk merepresentasikan teks. Anda dapat menggunakan tanda petik tunggal atau ganda untuk membuat string.
- `bool`, atau boolean: tipe untuk merepresentasikan nilai logis. Nilainya hanya bisa `True` atau `False` (penggunaan huruf besar-kecil penting!).

`@instructions`
- Buat float baru, `half`, dengan nilai `0.5`.
- Buat string baru, `intro`, dengan nilai `"Halo! Apa kabar?"`.
- Buat boolean baru, `is_good`, dengan nilai `True`.

`@hint`
- Untuk membuat variabel di Python, gunakan `=`. Pastikan Anda membungkus string dengan tanda petik tunggal atau ganda.
- Hanya ada dua nilai boolean di Python: `True` dan `False`. `TRUE`, `true`, `FALSE`, `false`, dan variasi lainnya tidak akan diterima.

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
Ex().check_object("half").has_equal_value(incorrect_msg = "Apakah kamu menyimpan float, `0.5` ke `half`?")

Ex().check_object("intro").has_equal_value(incorrect_msg = "Hmm, ada yang salah di variabel `intro` kamu. Periksa kembali ejaannya dan pastikan kamu sudah menggunakan tanda kutip.")

Ex().check_object("is_good").has_equal_value(incorrect_msg = "Apakah kamu menggunakan huruf kapital untuk nilai boolean? Ingat, kamu tidak perlu menggunakan tanda kutip di sini.")

success_msg("Bagus!")
```

---

## Operasi dengan tipe lainnya

```yaml
type: BulletExercise
key: 4d0d83cc02
xp: 100
```

Variabel memiliki berbagai tipe dalam Python. Anda dapat melihat tipe sebuah variabel dengan menggunakan fungsi `type()`. Sebagai contoh, untuk melihat tipe dari `a`, jalankan: `type(a)`.

Tipe yang berbeda berperilaku berbeda dalam Python. Misalnya, ketika Anda menjumlahkan dua string, perilakunya akan berbeda dibandingkan saat Anda menjumlahkan dua integer atau dua boolean.

Sekarang saatnya Anda mengujinya.

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
- Tambahkan `savings` dan `new_savings` lalu tetapkan ke `total_savings`.
- Gunakan `type()` untuk mencetak tipe hasil dari `total_savings`.

`@hint`
- Tetapkan `savings + new_savings` ke variabel baru, `total_savings`.
- Untuk mencetak tipe variabel `x`, gunakan `print(type(x))`.

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
msg = "Kamu tidak perlu mengubah atau menghapus variabel yang sudah ditentukan."

Ex().multi(
    check_object('savings', missing_msg=msg).has_equal_value(incorrect_msg=msg),
    check_object('new_savings', missing_msg=msg).has_equal_value(incorrect_msg=msg)
)

Ex().multi(
    check_object("total_savings").has_equal_value(incorrect_msg="Tambahkan `savings` dan `new_savings` untuk membuat variabel `total_savings`."),
    has_printout(1, not_printed_msg = "__JINJA__:Gunakan `{{sol_call}}` untuk mencetak tipe dari `total_savings`.")
)
```

***

```yaml
type: NormalExercise
key: f54fbf9bd9
xp: 50
```

`@instructions`
- Hitung penjumlahan `intro` dan `intro` lalu tetapkan hasilnya ke `doubleintro`.
- Cetak `doubleintro`. Apakah ini sesuai dengan perkiraan Anda?

`@hint`
- Tetapkan `intro + intro` ke variabel baru, `doubleintro`.
- Untuk mencetak variabel `x`, tuliskan `print(x)` di skrip.

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
msg = "Kamu tidak perlu mengubah atau menghapus variabel yang sudah ditentukan."

Ex().check_object('intro', missing_msg=msg).has_equal_value(incorrect_msg=msg)

Ex().multi(
    check_object("doubleintro").has_equal_value(incorrect_msg  = "Apakah kamu sudah menyimpan hasil dari `intro + intro` di `doubleintro`?"),
    has_printout(0, not_printed_msg = "Jangan lupa untuk mencetak `doubleintro`.")
)

success_msg("Bagus. Perhatikan bagaimana `intro + intro` menyebabkan `\"Hello! How are you?\"` dan `\"Hello! How are you?\"` digabungkan.")
```

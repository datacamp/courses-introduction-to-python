---
title_meta: Bab 3
title: Fungsi dan Paket
description: >-
  Anda akan belajar menggunakan fungsi, metode, dan paket untuk memanfaatkan
  kode yang telah ditulis oleh pengembang Python hebat secara efisien. Tujuannya
  adalah mengurangi jumlah kode yang Anda butuhkan untuk menyelesaikan masalah
  yang menantang!
attachments:
  slides_link: 'https://projector-video-pdf-converter.datacamp.com/735/chapter3.pdf'
lessons:
  - nb_of_exercises: 4
    title: Fungsi
  - nb_of_exercises: 4
    title: Metode
  - nb_of_exercises: 4
    title: Paket
---

## Fungsi

```yaml
type: VideoExercise
key: 5c5f365930
xp: 50
```

`@projector_key`
1204d914b0e53100529827e07441ee6c

---

## Fungsi yang familier

```yaml
type: NormalExercise
key: c422ee929b
lang: python
xp: 100
skills:
  - 2
```

Secara bawaan, Python menyediakan sejumlah fungsi bawaan untuk memudahkan pekerjaan Anda sebagai ilmuwan data. Anda sudah mengenal dua di antaranya: `print()` dan `type()`. Ada juga fungsi seperti `str()`, `int()`, `bool()` dan `float()` untuk beralih antar tipe data. Anda dapat mempelajarinya [di sini.](https://docs.python.org/3/library/functions.html) Ini juga termasuk fungsi bawaan.

Memanggil sebuah fungsi itu mudah. Untuk mendapatkan tipe dari `3.0` dan menyimpan outputnya sebagai variabel baru, `result`, Anda bisa menggunakan berikut ini:

```
result = type(3.0)
```

`@instructions`
- Gunakan `print()` bersama `type()` untuk mencetak tipe dari `var1`.
- Gunakan `len()` untuk mendapatkan [panjang daftar](https://docs.python.org/3/library/functions.html#len) `var1`. Bungkus dengan pemanggilan `print()` agar langsung tercetak.
- Gunakan `int()` untuk mengonversi `var2` menjadi [integer](https://docs.python.org/3/library/functions.html#int). Simpan keluarannya sebagai `out2`.

`@hint`
- Panggil fungsi `type()` seperti ini: `type(var1)`.
- Panggil `print()` seperti yang sudah sering Anda lakukan. Cukup letakkan variabel yang ingin Anda cetak di dalam tanda kurung.
- `int(x)` akan mengonversi `x` menjadi bilangan bulat (integer).

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
msg = "Kamu tidak perlu mengubah atau menghapus variabel yang sudah ditentukan."
Ex().check_object("var1", missing_msg=msg).has_equal_value(incorrect_msg=msg)
Ex().check_object("var2", missing_msg=msg).has_equal_value(incorrect_msg=msg)

patt = "__JINJA__:Pastikan untuk mencetak %s dari `var1` dengan `{{sol_call}}`."
Ex().has_printout(0, not_printed_msg = patt % 'tipe')
Ex().has_printout(1, not_printed_msg = patt % 'panjang')

int_miss_msg = "Apakah kamu sudah menggunakan `int()` untuk membuat integer dari `var2`?"
int_incorr_msg = "Apakah kamu sudah memasukkan `var2` ke dalam `int()`?"
Ex().check_correct(
  check_object("out2").has_equal_value(incorrect_msg="Kamu sudah memanggil `int()` dengan benar; sekarang pastikan untuk menetapkan hasil dari pemanggilan ini ke `out2`."),
  check_function("int", missing_msg=int_miss_msg).has_equal_value(incorrect_msg=int_incorr_msg)
)
success_msg("Kerja bagus! Fungsi `len()` sangat berguna; fungsi ini juga bekerja pada string untuk menghitung jumlah karakter!")
```

---

## Tolong!

```yaml
type: MultipleChoiceExercise
key: 679b852978
lang: python
xp: 50
skills:
  - 2
```

Mungkin Anda sudah tahu nama suatu fungsi Python, tetapi Anda masih harus mencari tahu cara menggunakannya. Ironisnya, Anda harus meminta informasi tentang suatu fungsi dengan fungsi lain: `help()`. Khusus di IPython, Anda juga dapat menggunakan `?` sebelum nama fungsi.

Misalnya, untuk mendapatkan bantuan pada fungsi `max()`, Anda dapat menggunakan salah satu pemanggilan berikut:

```
help(max)
?max
```

Gunakan IPython Shell untuk membuka [dokumentasi](https://docs.python.org/3/library/functions.html#pow) tentang `pow()`. Lakukan ini dengan mengetik `?pow` atau `help(pow)` lalu tekan **Enter**.

Mana dari pernyataan berikut yang benar?

`@possible_answers`
- `pow()` menerima tiga argumen: `base`, `exp`, dan `mod`. Tanpa `mod`, fungsi akan mengembalikan error.
- `pow()` menerima tiga argumen wajib: `base`, `exp`, dan `None`.
- `pow()` membutuhkan argumen `base` dan `exp`; `mod` bersifat opsional.
- `pow()` menerima dua argumen: `exp` dan `mod`. Jika `exp` hilang akan terjadi error.

`@hint`
- Argumen opsional diatur dengan `=` ke nilai bawaan yang akan digunakan oleh fungsi jika argumen tersebut tidak ditentukan.

`@pre_exercise_code`
```{python}

```

`@sct`
```{python}
msg1 = "Tidak tepat. `mod` memiliki nilai default yang akan digunakan jika kamu tidak menentukan nilai."
msg2 = "Salah. `None` adalah nilai default untuk argumen `mod`."
msg3 = "Sempurna! Menggunakan `help()` dapat membantumu memahami cara kerja fungsi, memaksimalkan potensinya!"
msg4 = "Salah. `pow()` membutuhkan tiga argumen, salah satunya memiliki nilai default."
Ex().has_chosen(3, [msg1, msg2, msg3, msg4])
```

---

## Berbagai argumen

```yaml
type: NormalExercise
key: e30486d7c1
lang: python
xp: 100
skills:
  - 2
```

Pada latihan sebelumnya, Anda mengidentifikasi argumen opsional dengan melihat dokumentasi menggunakan `help()`. Sekarang Anda akan menerapkannya untuk mengubah perilaku fungsi `sorted()`.

Lihat [dokumentasi](https://docs.python.org/3/library/functions.html#sorted) `sorted()` dengan mengetik `help(sorted)` di IPython Shell.

Anda akan melihat bahwa `sorted()` menerima tiga argumen: `iterable`, `key`, dan `reverse`. Pada latihan ini, Anda hanya perlu menentukan `iterable` dan `reverse`, bukan `key`.

Dua daftar telah dibuat untuk Anda.

Apakah Anda dapat menggabungkan dan mengurutkannya secara menurun?

`@instructions`
- Gunakan `+` untuk menggabungkan isi `first` dan `second` ke dalam daftar baru: `full`.
- Panggil `sorted()` pada `full` dan tentukan argumen `reverse` bernilai `True`. Simpan daftar yang sudah diurutkan sebagai `full_sorted`.
- Akhiri dengan mencetak `full_sorted`.

`@hint`
- Jumlahkan `first` dan `second` seolah-olah keduanya adalah angka dan simpan hasilnya ke `full`.
- Gunakan `sorted()` dengan dua input: `full` dan `reverse=True`.
- Untuk mencetak sebuah variabel, gunakan `print()`.

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
msg = "Kamu tidak perlu mengubah atau menghapus variabel `first` dan `second` yang sudah ada."
Ex().multi(
  check_object("first", missing_msg=msg).has_equal_value(incorrect_msg=msg),
  check_object("second", missing_msg=msg).has_equal_value(incorrect_msg=msg)
)
Ex().check_correct(
  check_object("full_sorted").has_equal_value(incorrect_msg="Pastikan kamu menetapkan hasil pemanggilan `sorted()` ke `full_sorted`."),
  check_function("sorted").multi(
    check_args(0).has_equal_value(),
    check_args('reverse').has_equal_value()
  )
)

success_msg("Keren! Lanjut ke video tentang metode Python.")
```

---

## Metode

```yaml
type: VideoExercise
key: 2b66cb66b1
xp: 50
```

`@projector_key`
8e387776f3a264a745128b68aa8d8f83

---

## Metode String

```yaml
type: NormalExercise
key: 4039302ee0
lang: python
xp: 100
skills:
  - 2
```

String memiliki banyak metode. Ikuti instruksi dengan saksama untuk menemukan beberapa di antaranya. Jika Anda ingin mempelajarinya lebih rinci, Anda selalu bisa mengetik `help(str)` di IPython Shell.

Sebuah string `place` telah dibuat untuk Anda coba.

`@instructions`
- Gunakan [metode](https://docs.python.org/3/library/stdtypes.html#str.upper) `.upper()` pada `place` dan simpan hasilnya ke `place_up`. Gunakan sintaks pemanggilan metode yang Anda pelajari di video sebelumnya.
- Cetak `place` dan `place_up`. Apakah keduanya berubah?
- Cetak jumlah huruf o pada variabel `place` dengan memanggil `.count()` pada `place` dan meneruskan huruf `'o'` sebagai masukan ke metode tersebut. Kita membahas tentang variabel `place`, bukan kata "place"!

`@hint`
- Anda dapat memanggil metode `.upper()` pada `place` tanpa input tambahan.
- Untuk mencetak variabel `x`, Anda dapat menulis `print(x)`.
- Pastikan Anda membungkus pemanggilan `place.count(____)` dalam fungsi `print()` agar hasilnya tercetak.

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
msg = "Kamu tidak perlu mengubah atau menghapus variabel yang sudah ditentukan."
Ex().check_object("place", missing_msg=msg).has_equal_value(incorrect_msg=msg)

patt = "Jangan lupa untuk mencetak `%s`."
Ex().has_printout(0, not_printed_msg=patt % "place")
Ex().check_correct(
    has_printout(1, not_printed_msg=patt % "place_up"),
    check_correct(
        check_object("place_up").has_equal_value(incorrect_msg="Tetapkan hasil dari pemanggilan `place.upper()` kamu ke `place_up`."),
        check_function("place.upper", signature=False)
    )
)    

# check count of place
Ex().check_correct(
  has_printout(2, not_printed_msg = "Kamu sudah menghitung jumlah o di `place` dengan benar; sekarang pastikan untuk membungkus pemanggilan `place.count('o')` dalam fungsi `print()` untuk mencetak hasilnya."),
  check_function("place.count", signature=False).check_args(0).has_equal_value()
)

success_msg("Bagus! Perhatikan dari hasil cetakan bahwa metode `upper()` tidak mengubah objek yang dipanggil. Ini akan berbeda untuk daftar di latihan berikutnya!")
```

---

## Metode Daftar

```yaml
type: NormalExercise
key: 0dbe8ed695
lang: python
xp: 100
skills:
  - 2
```

String bukan satu-satunya tipe Python yang memiliki metode. Daftar, float, integer, dan boolean juga merupakan tipe yang dilengkapi dengan banyak metode berguna. Dalam latihan ini, Anda akan bereksperimen dengan:

- `.index()`, untuk mendapatkan indeks elemen pertama dari sebuah daftar yang cocok dengan masukan, dan
- `.count()`, untuk mendapatkan berapa kali sebuah elemen muncul dalam daftar.

Anda akan bekerja dengan daftar yang berisi luas berbagai bagian rumah: `areas`.

`@instructions`
- Gunakan metode `.index()` untuk mendapatkan indeks elemen di `areas` yang bernilai `20.0`. Cetak indeks ini.
- Panggil `.count()` pada `areas` untuk mengetahui berapa kali `9.50` muncul dalam daftar. Sekali lagi, cetak saja angkanya.

`@hint`
- Untuk mencetak indeks, bungkus pemanggilan `areas.index(___)` dalam fungsi `print()`.
- Untuk mencetak berapa kali sebuah elemen `x` muncul dalam daftar, bungkus pemanggilan `areas.count(___)` dalam fungsi `print()`.

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
predef_msg = "Kamu tidak perlu mengubah atau menghapus daftar `areas` yang sudah ditentukan."

Ex().check_object("areas", missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg)

Ex().check_function("print", index=0).check_args(0).check_function('areas.index', signature=False).check_args(0).has_equal_value()


Ex().check_function("print", index=1).check_args(0).check_function('areas.count', signature=False).has_equal_value()

success_msg("Bagus! Ini adalah contoh metode `list` yang tidak mengubah daftar yang mereka panggil.")
```

---

## Metode Daftar (2)

```yaml
type: NormalExercise
key: 1fbeab82d0
lang: python
xp: 100
skills:
  - 2
```

Sebagian besar metode daftar akan mengubah daftar tempat metode tersebut dipanggil. Contohnya:

- `.append()`, yang menambahkan sebuah elemen ke daftar tempat metode ini dipanggil,
- `.remove()`, yang [menghapus](https://docs.python.org/3/library/stdtypes.html#typesseq-mutable) elemen pertama dari daftar yang cocok dengan input, dan
- `.reverse()`, yang [membalik](https://docs.python.org/3/library/stdtypes.html#typesseq-mutable) urutan elemen pada daftar tempat metode ini dipanggil.

Anda akan bekerja dengan daftar yang berisi area bagian-bagian rumah: `areas`.

`@instructions`
- Gunakan `.append()` dua kali untuk menambahkan ukuran paviliun dekat kolam renang dan garasi lagi: masing-masing `24.5` dan `15.45`. Pastikan menambahkannya dalam urutan ini.
- Cetak `areas`
- Gunakan metode `.reverse()` untuk membalik urutan elemen dalam `areas`.
- Cetak `areas` sekali lagi.

`@hint`
- Untuk instruksi pertama, gunakan pemanggilan `areas.append(___)` sebanyak dua kali.
- Untuk mencetak variabel `x`, cukup tulis `print(x)`.
- Metode `.reverse()` tidak memerlukan input tambahan; cukup gunakan notasi titik dan tanda kurung kosong: `.reverse()`.
- Untuk mencetak variabel `x`, cukup tulis `print(x)`.

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

success_msg("Mantap!")
```

---

## Paket

```yaml
type: VideoExercise
key: ab96a17c5e
xp: 50
```

`@projector_key`
cedcfb34350be8545599768f96695cdd

---

## Impor paket

```yaml
type: NormalExercise
key: 7432a6376f
lang: python
xp: 100
skills:
  - 2
```

Misalkan Anda ingin menghitung keliling dan luas sebuah lingkaran. Berikut rumusnya:

$$C = 2 \pi r$$
$$A = \pi r^2 $$

Alih-alih mengetikkan angka untuk `pi`, Anda dapat menggunakan paket `math` yang berisi nilai tersebut.

Sebagai referensi, `**` adalah simbol pemangkatan. Sebagai contoh, `3**4` berarti `3` pangkat `4` dan menghasilkan `81`.

`@instructions`
- Impor paket `math`.
- Gunakan `math.pi` untuk menghitung keliling lingkaran dan simpan dalam `C`.
- Gunakan `math.pi` untuk menghitung luas lingkaran dan simpan dalam `A`.

`@hint`
- Anda bisa langsung menggunakan `import math`, lalu merujuk `pi` dengan `math.pi`.
- Gunakan persamaan pada teks soal untuk mencari `C`. Gunakan `*`.
- Gunakan persamaan pada teks soal untuk mencari `A`. Gunakan `*` dan `**`.

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
patt = "Perhitungan `%s` kamu tidak terlalu benar. Pastikan untuk menggunakan `math.pi`."
Ex().multi(
  has_import('math', same_as=False),
  check_object('C').has_equal_value(incorrect_msg=patt%'C'),
  check_object('A').has_equal_value(incorrect_msg=patt%'A')
)

Ex().multi(
  has_printout(0, not_printed_msg = "__JINJA__:Tetap gunakan `{{sol_call}}` di sana untuk mencetak keliling."),
  has_printout(1, not_printed_msg = "__JINJA__:Tetap gunakan `{{sol_call}}` di sana untuk mencetak area.")
)

success_msg("Bagus! Jika kamu tahu cara menangani fungsi dari paket, kekuatan banyak programmer Python ada di ujung jari kamu!")
```

---

## Impor selektif

```yaml
type: NormalExercise
key: fe65eff50a
lang: python
xp: 100
skills:
  - 2
```

Impor umum, seperti `import math`, membuat **semua** fungsi dari paket `math` tersedia untuk Anda. Namun, jika Anda hanya akan menggunakan bagian tertentu dari sebuah paket, Anda dapat membuat impor yang lebih selektif:

```
dari math import pi
```

Coba lakukan hal yang sama lagi, tetapi kali ini hanya gunakan `pi`.

`@instructions`
- Lakukan impor selektif dari paket `math` di mana Anda hanya mengimpor fungsi `pi`.
- Gunakan `pi` untuk menghitung keliling lingkaran dan simpan dalam `C`.
- Gunakan `pi` untuk menghitung luas lingkaran dan simpan dalam `A`.

`@hint`
- Gunakan `from math import pi` untuk melakukan impor selektif.
- Sekarang, Anda dapat menggunakan `pi` secara langsung!

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
patt = "Perhitungan `%s` kamu belum benar. Pastikan untuk hanya menggunakan `pi`."

Ex().has_import("math.pi", not_imported_msg = "Pastikan untuk mengimpor `pi` dari paket `math`. Kamu harus menggunakan notasi `from ___ import ___`.",)

Ex().multi(
  check_object('C').has_equal_value(incorrect_msg=patt%'C'),
  check_object('A').has_equal_value(incorrect_msg=patt%'A')
)

Ex().multi(
  has_printout(0, not_printed_msg = "__JINJA__:Pertahankan `{{sol_call}}` di sana untuk mencetak keliling."),
  has_printout(1, not_printed_msg = "__JINJA__:Pertahankan `{{sol_call}}` di sana untuk mencetak luas.")
)

success_msg("Bagus! Lanjut ke latihan berikutnya.")
```

---

## Berbagai cara melakukan import

```yaml
type: MultipleChoiceExercise
key: f1b2675a2a
lang: python
xp: 50
skills:
  - 2
```

Ada beberapa cara untuk mengimpor paket dan modul ke dalam Python. Bergantung pada pemanggilan import, Anda harus menggunakan kode Python yang berbeda.

Misalkan Anda ingin menggunakan [function](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.inv.html) `inv()`, yang berada di subpaket `linalg` dari paket `scipy`. Anda ingin dapat menggunakan fungsi ini sebagai berikut:

```
my_inv([[1,2], [3,4]])
```

Pernyataan `import` mana yang Anda perlukan agar kode di atas dapat dijalankan tanpa error?

`@possible_answers`
- `import scipy`
- `import scipy.linalg`
- `from scipy.linalg import my_inv`
- `from scipy.linalg import inv as my_inv`

`@hint`
- Coba berbagai pernyataan import di shell IPython dan lihat mana yang membuat baris `my_inv([[1, 2], [3, 4]])` berjalan tanpa error. Tekan **enter** untuk menjalankan kode yang Anda ketik.

`@pre_exercise_code`
```{python}

```

`@sct`
```{python}
msg1 = msg2 = msg3 = "Salah, coba lagi. Coba pernyataan impor yang berbeda di shell IPython dan lihat mana yang menyebabkan baris `my_inv([[1, 2], [3, 4]])` berjalan tanpa kesalahan."
msg4 = "Benar! Kata `as` memungkinkan kamu membuat nama lokal untuk fungsi yang kamu impor: `inv()` sekarang tersedia sebagai `my_inv()`."
Ex().has_chosen(4, [msg1, msg2, msg3, msg4])
```

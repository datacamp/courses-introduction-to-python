---
title_meta: Bab 4
title: NumPy
description: >-
  NumPy adalah paket Python yang fundamental untuk mempraktikkan data sains
  secara efisien. Pelajari cara bekerja dengan alat yang kuat pada array NumPy,
  dan mulailah eksplorasi data.
attachments:
  slides_link: 'https://projector-video-pdf-converter.datacamp.com/735/chapter4.pdf'
lessons:
  - nb_of_exercises: 5
    title: Numpy
  - nb_of_exercises: 5
    title: Array NumPy 2D
  - nb_of_exercises: 3
    title: 'NumPy: Statistik Dasar'
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

## NumPy Array Pertama Anda

```yaml
type: NormalExercise
key: 84cab9d170
lang: python
xp: 100
skills:
  - 2
```

Sekarang Anda akan menyelami dunia baseball. Dalam prosesnya, Anda akan menjadi terbiasa dengan dasar-dasar `numpy`, paket yang ampuh untuk melakukan data sains.

Sebuah daftar `baseball` telah didefinisikan dalam skrip Python, mewakili tinggi beberapa pemain baseball dalam sentimeter. Apakah Anda dapat menambahkan kode untuk membuat array `numpy` darinya?

`@instructions`
- Impor paket `numpy` sebagai `np`, sehingga Anda dapat merujuk `numpy` dengan `np`.
- Gunakan `np.array()` untuk membuat array `numpy` dari `baseball`. Beri nama array ini `np_baseball`.
- Cetak tipe dari `np_baseball` untuk memastikan hasilnya benar.

`@hint`
- `import numpy as np` akan menyelesaikannya. Sekarang, Anda harus menggunakan `np.fun_name()` setiap kali ingin memakai fungsi `numpy`.
- `np.array()` harus menerima input `baseball`. Tetapkan hasil pemanggilan fungsi tersebut ke `np_baseball`.
- Untuk mencetak tipe dari sebuah variabel `x`, cukup ketik `print(type(x))`.

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
predef_msg = "Kamu tidak perlu mengubah atau menghapus variabel yang sudah ditentukan."
Ex().has_import("numpy")
Ex().check_correct(
  check_object("np_baseball"),
  multi(
    check_object("baseball", missing_msg=predef_msg).has_equal_value(incorrect_msg=predef_msg),
    check_function("numpy.array").check_args(0).has_equal_ast()
  )
)

Ex().has_printout(0)
success_msg("Kerja bagus!")
```

---

## Tinggi badan pemain baseball

```yaml
type: NormalExercise
key: e7e25a89ea
lang: python
xp: 100
skills:
  - 2
```

Anda adalah penggemar berat baseball. Anda memutuskan untuk menghubungi MLB (Major League Baseball) dan menanyakan suatu statistik tambahan tentang tinggi badan pemain utama. Mereka memberikan data lebih dari seribu pemain, yang disimpan sebagai daftar Python biasa: `height_in`. Tinggi badan dinyatakan dalam inci. Bisakah Anda membuat array `numpy` darinya dan mengonversi satuannya ke meter?

`height_in` sudah tersedia dan paket `numpy` sudah dimuat, sehingga Anda dapat langsung mulai (Sumber: stat.ucla.edu).

`@instructions`
- Buat array `numpy` dari `height_in`. Beri nama array baru ini `np_height_in`.
- Cetak `np_height_in`.
- Kalikan `np_height_in` dengan `0.0254` untuk mengonversi semua ukuran tinggi dari inci ke meter. Simpan nilai baru tersebut dalam array baru, `np_height_m`.
- Cetak `np_height_m` dan periksa apakah outputnya masuk akal.

`@hint`
- Gunakan `np.array()` dan berikan `height` sebagai argumen. Simpan hasilnya dalam `np_height_in`.
- Untuk mencetak variabel `x`, ketik `print(x)` dalam skrip Python.
- Lakukan perhitungan seolah-olah `np_height_in` adalah satu angka: `np_height_in * conversion_factor` merupakan bagian dari jawabannya.
- Untuk mencetak variabel `x`, ketik `print(x)` dalam skrip Python.

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
  check_object("np_height_m").has_equal_value(incorrect_msg = "Gunakan `np_height_in * 0.0254` untuk menghitung `np_height_m`.")
)

success_msg("Bagus! Dalam sekejap mata, `numpy` melakukan perkalian pada lebih dari 1000 pengukuran tinggi.")
```

---

## Efek Samping NumPy

```yaml
type: MultipleChoiceExercise
key: 3662ff6637
lang: python
xp: 50
skills:
  - 2
```

`numpy` sangat baik untuk melakukan aritmetika vektor. Namun, jika Anda membandingkan fungsinya dengan daftar (list) Python biasa, beberapa hal berbeda.

Pertama, array `numpy` tidak dapat berisi elemen dengan tipe yang berbeda. Jika Anda mencampurkan tipe, seperti boolean dan integer, `numpy` akan secara otomatis mengonversinya ke tipe yang sama. Boolean seperti `True` dan `False` diperlakukan sebagai `1` dan `0` saat digabungkan dengan angka, sehingga array akhirnya menjadi integer.

Kedua, operator aritmetika umum seperti `+`, `-`, `*` dan `/` memiliki makna yang berbeda untuk daftar Python biasa dan array `numpy`.

Pilih kode yang menghasilkan keluaran berikut:

```
np.array([True, 1, 2]) + np.array([3, 4, False])
```

Paket `numpy` sudah diimpor sebagai `np`. Anda dapat menjalankan setiap opsi di IPython Shell untuk melihat keluarannya.

`@possible_answers`
- `np.array([True, 1, 2, 3, 4, False])`
- `np.array([4, 3, 0]) + np.array([0, 2, 2])`
- `np.array([1, 1, 2]) + np.array([3, 4, -1])`
- `np.array([0, 1, 2, 3, 4, 5])`

`@hint`
- Salin potongan kode yang berbeda dan tempelkan ke IPython Shell. Tekan **enter** untuk menjalankan kode dan lihat keluaran mana yang cocok dengan yang dihasilkan oleh `np.array([True, 1, 2]) + np.array([3, 4, False])`.

`@pre_exercise_code`
```{python}
import numpy as np
```

`@sct`
```{python}
msg1 = msg3 = msg4 = "Salah. Coba potongan kode yang berbeda dan lihat mana yang cocok dengan potongan kode target."
msg2 = "Kerja bagus! `True` diubah menjadi 1, `False` diubah menjadi 0."
Ex().has_chosen(2, [msg1, msg2, msg3, msg4])
```

---

## Melakukan Subsetting pada Array NumPy

```yaml
type: NormalExercise
key: fcb2a9007b
lang: python
xp: 100
skills:
  - 2
```

Subsetting (menggunakan notasi tanda kurung siku pada daftar atau array) bekerja dengan cara yang sama baik pada daftar maupun array.

Latihan ini sudah memuat dua daftar, `height_in` dan `weight_lb`, di latar belakang untuk Anda. Keduanya berisi tinggi badan dan berat badan pemain MLB sebagai daftar biasa. Latihan ini juga menyiapkan dua array `numpy`, `np_weight_lb` dan `np_height_in`, untuk Anda.

`@instructions`
- Lakukan subsetting pada `np_weight_lb` dengan mencetak elemen pada indeks 50.
- Cetak subarray dari `np_height_in` yang berisi elemen pada indeks 100 hingga **dan termasuk** indeks 110.

`@hint`
- Pastikan untuk membungkus operasi subsetting Anda dengan pemanggilan `print()`.
- Gunakan `[100:111]` untuk mendapatkan elemen dari indeks 100 hingga dan termasuk indeks 110.

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
msg = "Kamu tidak perlu mengubah atau menghapus variabel yang sudah ditentukan."
Ex().multi(
    check_object("np_height_in", missing_msg=msg).has_equal_value(incorrect_msg=msg),
    check_object("np_weight_lb", missing_msg=msg).has_equal_value(incorrect_msg=msg)
)

Ex().has_printout(0)
Ex().has_printout(1)

success_msg("Bagus! Saatnya belajar sesuatu yang baru: array NumPy 2D!")
```

---

## Array NumPy 2D

```yaml
type: VideoExercise
key: 1241efac7a
xp: 50
```

`@projector_key`
ae3238dcc7feb9adecfee0c395fc8dc8

---

## Array NumPy 2D Pertama Anda

```yaml
type: NormalExercise
key: 5cb045bb13
lang: python
xp: 100
skills:
  - 2
```

Sebelum bekerja dengan data MLB yang sebenarnya, mari coba membuat array `numpy` 2D dari sebuah daftar berisi daftar.

Pada latihan ini, `baseball` adalah daftar berisi daftar. Daftar utama berisi 4 elemen. Setiap elemen ini adalah daftar yang berisi tinggi badan dan berat badan dari 4 pemain baseball, dalam urutan tersebut. `baseball` sudah dibuatkan kodenya untuk Anda di skrip.

`@instructions`
- Gunakan `np.array()` untuk membuat array `numpy` 2D dari `baseball`. Beri nama `np_baseball`.
- Cetak tipe dari `np_baseball`.
- Cetak atribut `shape` dari `np_baseball`. Gunakan `np_baseball.shape`.

`@hint`
- `baseball` sudah dibuatkan kodenya untuk Anda di skrip. Panggil `np.array()` dan simpan array `numpy` 2D yang dihasilkan ke `np_baseball`.
- Gunakan `print()` bersama `type()` untuk instruksi kedua.
- `np_baseball.shape` akan memberi Anda dimensi dari `np_baseball`. Pastikan untuk membungkusnya dengan pemanggilan `print()`.

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
msg = "Kamu tidak perlu mengubah atau menghapus variabel yang sudah ditentukan."
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

success_msg("Bagus! Sekarang kamu siap untuk mengonversi data MLB yang sebenarnya menjadi array `numpy` 2D!")
```

---

## Data baseball dalam bentuk 2D

```yaml
type: NormalExercise
key: 5df25d0b7b
lang: python
xp: 100
skills:
  - 2
```

Anda menyadari bahwa akan lebih masuk akal untuk menyusun ulang semua informasi ini dalam array 2D `numpy`.

Anda memiliki daftar Python berisi daftar. Dalam daftar dari banyak daftar ini, setiap subdaftar merepresentasikan tinggi badan dan berat badan seorang pemain baseball. Nama daftar ini adalah `baseball` dan sudah dimuat untuk Anda (meskipun Anda tidak dapat melihatnya).

Simpan data tersebut sebagai array 2D untuk membuka fungsi tambahan `numpy`.

`@instructions`
- Gunakan `np.array()` untuk membuat array 2D `numpy` dari `baseball`. Beri nama `np_baseball`.
- Cetak atribut `shape` dari `np_baseball`.

`@hint`
- `baseball` sudah tersedia di lingkungan Python. Panggil `np.array()` untuknya dan simpan `numpy` array 2D yang dihasilkan ke dalam `np_baseball`.
- `np_baseball.shape` akan memberikan dimensi dari `np_baseball`. Pastikan Anda membungkusnya dengan pemanggilan `print()`.

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

success_msg("Keren! Saatnya pamerin beberapa fitur keren dari array `numpy` multi-dimensi!")
```

---

## Lakukan subsetting pada Array NumPy 2D

```yaml
type: NormalExercise
key: aeca4977f0
lang: python
xp: 100
skills:
  - 2
```

Jika array `numpy` 2D Anda memiliki struktur yang teratur, yaitu setiap baris dan kolom memiliki jumlah nilai yang tetap, cara melakukan subsetting yang rumit menjadi sangat mudah. Perhatikan kode di bawah, tempat elemen `"a"` dan `"c"` diekstrak dari daftar di dalam daftar.

```
# numpy
import numpy as np
np_x = np.array(x)
np_x[:, 0]
```

Pengindeksan sebelum koma merujuk ke baris, sedangkan indeks setelah koma merujuk ke kolom. Tanda `:` digunakan untuk mengiris, pada contoh ini, tanda tersebut memberi tahu Python untuk menyertakan semua baris.

`@instructions`
- Cetak baris ke-50 dari `np_baseball`.
- Buat variabel baru, `np_weight_lb`, yang berisi seluruh kolom kedua dari `np_baseball`.
- Pilih tinggi badan (kolom pertama) dari pemain baseball ke-124 dalam `np_baseball` dan cetak.

`@hint`
- Anda membutuhkan indeks baris 49 pada instruksi pertama! Lebih spesifik, Anda akan menggunakan `[49, :]`.
- Untuk memilih seluruh kolom kedua, Anda memerlukan `[:, 1]`.
- Untuk instruksi terakhir, gunakan `[123, 0]`; jangan lupa membungkusnya dengan pernyataan `print()`.

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
msg = "Kamu tidak perlu mengubah atau menghapus variabel yang sudah ditentukan."
Ex().multi(
    has_import("numpy", same_as = False),
    check_object("np_baseball", missing_msg=msg).has_equal_value(incorrect_msg = msg)
)

Ex().has_printout(0)

Ex().check_object('np_weight_lb').has_equal_value(incorrect_msg = "Kamu bisa menggunakan `np_baseball[:,1]` untuk mendefinisikan `np_weight_lb`. Ini akan memilih seluruh kolom pertama.")

Ex().has_printout(1)

success_msg("Ini berjalan dengan baik!")
```

---

## Aritmetika 2D

```yaml
type: NormalExercise
key: 1c2378b677
lang: python
xp: 100
skills:
  - 2
```

Array `numpy` 2D dapat melakukan perhitungan demi elemen, seperti halnya array `numpy`.

`np_baseball` sudah disiapkan untuk Anda; ini adalah array `numpy` 2D dengan 3 kolom yang merepresentasikan tinggi badan (dalam inci), berat badan (dalam pon), dan usia (dalam tahun). `baseball` tersedia sebagai daftar biasa berisi daftar, dan `updated` tersedia sebagai array `numpy` 2D.

`@instructions`
- Anda berhasil mendapatkan perubahan tinggi badan, berat badan, dan usia semua pemain baseball. Data ini tersedia sebagai array `numpy` 2D, `updated`. Tambahkan `np_baseball` dan `updated` lalu cetak hasilnya.
- Anda ingin mengonversi satuan tinggi dan berat badan ke metrik (masing-masing meter dan kilogram). Sebagai langkah pertama, buat array `numpy` dengan tiga nilai: `0.0254`, `0.453592`, dan `1`. Beri nama array ini `conversion`.
- Kalikan `np_baseball` dengan `conversion` dan cetak hasilnya.

`@hint`
- `np_baseball + updated` akan melakukan penjumlahan per elemen pada dua array `numpy`.
- Buat array `numpy` dengan `np.array()`; input berupa daftar Python biasa dengan tiga elemen.
- `np_baseball * conversion` akan berfungsi tanpa penanganan tambahan. Cobalah! Pastikan membungkusnya dengan pemanggilan `print()`.

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

msg = "Kamu tidak perlu mengubah atau menghapus variabel yang sudah ditentukan."
Ex().check_object("np_baseball", missing_msg=msg).has_equal_value(incorrect_msg=msg)

Ex().has_printout(0)

Ex().check_correct(
    has_printout(1),
    check_correct(
        check_object('conversion').has_equal_value(),
        check_function('numpy.array', index=1).check_args(0).has_equal_value()
    )    
)

success_msg("Kerja bagus! Perhatikan bagaimana dengan sedikit kode, kamu bisa mengubah semua nilai dalam struktur data `numpy` kamu dengan cara yang sangat spesifik. Ini akan sangat berguna di masa depanmu sebagai data scientist!")
```

---

## NumPy: Statistik Dasar

```yaml
type: VideoExercise
key: 287995e488
xp: 50
```

`@projector_key`
34495ba457d74296794d2a122c9b6e19

---

## Rata-rata versus median

```yaml
type: NormalExercise
key: 509c588eb6
lang: python
xp: 100
skills:
  - 2
```

Sekarang Anda tahu cara menggunakan fungsi-fungsi `numpy` untuk memahami data Anda dengan lebih baik.

Data baseball tersedia sebagai array `numpy` 2D dengan 3 kolom (tinggi badan, berat badan, usia) dan 1015 baris. Nama array `numpy` ini adalah `np_baseball`. Namun, setelah menata ulang data, Anda melihat sebagian nilai tinggi badan yang tidak wajar. Ikuti instruksinya dan temukan statistik ringkasan mana yang paling tepat saat Anda berhadapan dengan apa yang disebut sebagai _outlier_. `np_baseball` tersedia.

`@instructions`
- Buat array `numpy` `np_height_in` yang sama dengan kolom pertama dari `np_baseball`.
- Cetak nilai mean dari `np_height_in`.
- Cetak nilai median dari `np_height_in`.

`@hint`
- Gunakan subsetting `numpy` 2D: `[:,0]` adalah bagian dari solusinya.
- Jika `numpy` diimpor sebagai `np`, Anda dapat menggunakan `np.mean()` untuk mendapatkan nilai rata-rata dari array NumPy. Jangan lupa sertakan pemanggilan `print()`.
- Untuk instruksi terakhir, gunakan `np.median()`.

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

Ex().check_object("np_height_in").has_equal_value(incorrect_msg = "Kamu bisa menggunakan `np_baseball[:,0]` untuk memilih kolom pertama dari `np_baseball`"),

Ex().check_correct(
    has_printout(0),
    check_function('numpy.mean').has_equal_value()
)

Ex().check_correct(
    has_printout(1),
    check_function('numpy.median').has_equal_value()
)

success_msg("Rata-rata tinggi 1586 inci, kedengarannya tidak benar, kan? Namun, median tampaknya tidak terpengaruh oleh pencilan: 74 inci masuk akal. Selalu merupakan ide bagus untuk memeriksa baik median maupun mean, untuk mendapatkan gambaran tentang distribusi keseluruhan dari seluruh dataset.")
```

---

## Mengeksplorasi data baseball

```yaml
type: NormalExercise
key: '4409948807'
lang: python
xp: 100
skills:
  - 2
```

Karena mean dan median sangat jauh berbeda, Anda memutuskan untuk mengajukan keluhan ke MLB. Mereka menemukan error dan mengirimkan data yang telah dikoreksi kepada Anda. Data tersebut kembali tersedia sebagai array NumPy 2D `np_baseball`, dengan tiga kolom.

Skrip Python di editor sudah menyertakan kode untuk mencetak pesan informatif dengan berbagai statistik ringkasan dan `numpy` sudah dimuat sebagai `np`. Dapatkah Anda menyelesaikannya? `np_baseball` tersedia.

`@instructions`
- Kode untuk mencetak mean tinggi badan sudah disertakan. Lengkapi kode untuk median tinggi badan.
- Gunakan `np.std()` pada kolom pertama `np_baseball` untuk menghitung `stddev`.
- Apakah pemain yang besar cenderung lebih berat? Gunakan `np.corrcoef()` untuk menyimpan korelasi antara kolom pertama dan kedua `np_baseball` dalam `corr`.

`@hint`
- Gunakan `np.median()` untuk menghitung median. Pastikan Anda memilih kolom yang benar terlebih dahulu!
- Lakukan subsetting pada kolom yang sama saat menghitung simpangan baku dengan `np.std()`.
- Gunakan `np_baseball[:, 0]` dan `np_baseball[:, 1]` untuk memilih kolom pertama dan kedua; ini adalah masukan untuk `np.corrcoef()`.

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
msg = "Kamu seharusnya tidak mengubah atau menghapus variabel `avg` yang sudah ditentukan."
Ex().check_object("avg", missing_msg=msg).has_equal_value(incorrect_msg=msg)

missing = "Apakah kamu sudah menggunakan `np.median()` untuk menghitung median?"
incorrect = "Untuk menghitung `med`, masukkan kolom pertama dari `np_baseball` ke `numpy.median()`. Contoh `np.mean()` menunjukkan caranya."
Ex().check_correct(
  check_object("med").has_equal_value(),
  check_function("numpy.median", index=0, missing_msg=missing).check_args(0).has_equal_value(incorrect_msg=incorrect)
)

missing = "Apakah kamu sudah menggunakan `np.std()` untuk menghitung standar deviasi?"
incorrect = "Untuk menghitung `stddev`, masukkan kolom pertama dari `np_baseball` ke `numpy.std()`. Contoh `np.mean()` menunjukkan caranya."
Ex().check_correct(
  check_object("stddev").has_equal_value(),
  check_function("numpy.std", index=0, missing_msg=missing).check_args(0).has_equal_value(incorrect_msg=incorrect)
)

missing = "Apakah kamu sudah menggunakan `np.corrcoef()` untuk menghitung korelasi?"
incorrect1 = "Untuk menghitung `corr`, argumen pertama untuk `np.corrcoef()` seharusnya adalah kolom pertama dari `np_baseball`, mirip dengan yang dilakukan sebelumnya."
incorrect2 = "Untuk menghitung `corr`, argumen kedua untuk `np.corrcoef()` seharusnya adalah kolom kedua dari `np_baseball`. Alih-alih `[:,0]`, gunakan `[:,1]` kali ini."
Ex().check_correct(
  check_object("corr").has_equal_value(),
  check_function("numpy.corrcoef", index=0, missing_msg=missing).multi(
    check_args(0, missing_msg=incorrect1).has_equal_value(incorrect_msg=incorrect1),
    check_args(1, missing_msg=incorrect2).has_equal_value(incorrect_msg=incorrect2)
  )
)

success_msg("Kerja bagus! Kamu telah membangun fondasi yang kuat - sekarang saatnya menggunakan semua keterampilan data science barumu untuk menyelesaikan lebih banyak tantangan dan memberikan dampak.")
```

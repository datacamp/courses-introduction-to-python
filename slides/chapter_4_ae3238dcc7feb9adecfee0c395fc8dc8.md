---
title: Insert title here
key: ae3238dcc7feb9adecfee0c395fc8dc8
video_link:
  mp3: >-
    https://videos.datacamp.com/mp3/translations/course_735/id-ID/2154dd4d-3e19-4c09-b823-b09c2eb8b9bc.mp3
---

## Array NumPy 2D

```yaml
type: TitleSlide
key: 0cc8abf493
```

`@lower_third`
name: Hugo Bowne-Anderson
title: Data Scientist at DataCamp

`@script`
Kerja bagus, Anda menakjubkan! Sekarang mari kita buat ulang array numpy dari video sebelumnya.
---

## Tipe Array NumPy

```yaml
type: FullSlide
key: 1b9db47fd2
code_zoom: 100
```

`@part1`
```py
import numpy as np
np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
np_weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])
```

```py
type(np_height)
```

```out
numpy.ndarray
```

```py
type(np_weight)
```

```out
numpy.ndarray
```

`@script`
Kalau Anda menanyakan tipe dari banyak array ini, Python memberi tahu bahwa itu numpy.ndarray. Titik numpy menunjukkan bahwa ini adalah tipe yang didefinisikan di paket numpy. ndarray adalah singkatan dari array berdimensi-n. Array np_tinggi badan dan np_berat badan adalah array satu dimensi, tetapi sangat mungkin membuat array 2 dimensi, 3 dimensi, bahkan tujuh dimensi! Namun, di video ini kita tetap fokus pada 2 dimensi.
---

## Array NumPy 2D

```yaml
type: FullSlide
key: ebb550dcba
code_zoom: 71
```

`@part1`
```py
np_2d = np.array([[1.73, 1.68, 1.71, 1.89, 1.79],
                  [65.4, 59.2, 63.6, 88.4, 68.7]])
```{{1}}
```py
np_2d
```{{2}}

```out
array([[ 1.73,  1.68,  1.71,  1.89,  1.79],
       [65.4 , 59.2 , 63.6 , 88.4 , 68.7 ]])
```{{2}}

```py
np_2d.shape
```{{3}}

```out
(2, 5) # 2 rows, 5 columns
```{{3}}

```py
np.array([[1.73, 1.68, 1.71, 1.89, 1.79],
          [65.4, 59.2, 63.6, 88.4, "68.7"]])
```{{4}}

```out
array([['1.73', '1.68', '1.71', '1.89', '1.79'],
       ['65.4', '59.2', '63.6', '88.4', '68.7']], dtype='<U32')
```{{4}}

`@script`
Anda dapat membuat array numpy 2 dimensi dari daftar Python biasa dari banyak daftar. Mari coba membuat satu array numpy untuk semua data tinggi dan berat keluarga Anda, seperti ini.

Jika Anda mencetak np_2d sekarang, Anda akan melihat bahwa ini adalah struktur data berbentuk persegi panjang: Setiap subdaftar pada daftar tersebut sesuai dengan satu baris di array numpy dua dimensi. Dari np_2d.shape, Anda bisa melihat bahwa kita memang memiliki 2 baris dan 5 kolom. shape adalah atribut dari array np2d, yang dapat memberi Anda lebih banyak informasi tentang seperti apa struktur datanya.

Perhatikan bahwa sintaks untuk mengakses atribut mirip seperti memanggil metode, tetapi keduanya tidak sama! Ingat bahwa metode memiliki tanda kurung setelahnya, dan seperti yang Anda lihat di sini, atribut tidak.

Untuk array dua dimensi, aturan NumPy juga berlaku: sebuah array hanya boleh berisi satu jenis tipe. Jika Anda mengubah satu float menjadi string, semua elemen array akan dikonversi menjadi string agar array tetap homogen.
---

## Subsetting

```yaml
type: FullSlide
key: e71d2fc8b8
code_zoom: 80
```

`@part1`
```out
           0       1       2       3       4
           
array([[  1.73,   1.68,   1.71,   1.89,   1.79],     0
       [  65.4,   59.2,   63.6,   88.4,   68.7]])    1
```

```py
np_2d[0]
```

```out
array([1.73, 1.68, 1.71, 1.89, 1.79])
```

`@script`
Anda bisa membayangkan array numpy 2 dimensi sebagai versi daftar yang lebih baik dari banyak daftar: Anda dapat melakukan perhitungan pada array, seperti yang saya tunjukkan sebelumnya, dan Anda bisa melakukan cara-cara subset yang lebih canggih.

Misalkan Anda menginginkan baris pertama, lalu elemen ketiga pada baris tersebut. Untuk memilih barisnya, Anda perlu indeks 0 di dalam tanda kurung siku. Jangan lupa bahwa pengindeksan dimulai dari nol.

Untuk kemudian memilih elemen ketiga, Anda bisa meneruskan pemanggilan yang sama dengan sepasang kurung siku lagi, kali ini dengan indeks 2,
---

## Subsetting

```yaml
type: FullSlide
key: 57a1fb1581
disable_transition: true
code_zoom: 80
```

`@part1`
```out
           0       1       2       3       4
           
array([[  1.73,   1.68,   1.71,   1.89,   1.79],     0
       [  65.4,   59.2,   63.6,   88.4,   68.7]])    1
```

```py
np_2d[0][2]
```

```out
1.71
```

```py
np_2d[0, 2]
```{{1}}

```out
1.71
```{{1}}

`@script`
seperti ini. Pada dasarnya Anda memilih barisnya, lalu dari baris tersebut melakukan seleksi lain lagi.

Ada juga cara alternatif untuk melakukan subset, menggunakan satu pasang kurung siku dan sebuah koma. Pemanggilan ini mengembalikan nilai yang persis sama seperti sebelumnya. Nilai sebelum koma menentukan baris, nilai setelah koma menentukan kolom. Perpotongan baris dan kolom yang Anda tentukan akan dikembalikan. Setelah Anda terbiasa, sintaks ini terasa lebih intuitif dan membuka lebih banyak kemungkinan.
---

## Subsetting

```yaml
type: FullSlide
key: feb75c975c
disable_transition: true
code_zoom: 80
```

`@part1`
```out
           0       1       2       3       4
           
array([[  1.73,   1.68,   1.71,   1.89,   1.79],     0
       [  65.4,   59.2,   63.6,   88.4,   68.7]])    1
```

```py
np_2d[:, 1:3]
```{{1}}

```out
array([[ 1.68,  1.71],
       [59.2 , 63.6 ]])
```{{1}}

```py
np_2d[1, :]
```{{2}}

```out
array([65.4, 59.2, 63.6, 88.4, 68.7])
```{{2}}

`@script`
Misalkan Anda ingin memilih tinggi dan berat anggota keluarga kedua dan ketiga. Anda menginginkan kedua baris, jadi gunakan tanda titik-dua sebelum koma. Anda hanya ingin kolom kedua dan ketiga, jadi masukkan indeks 1 sampai 3 setelah koma. Ingat bahwa indeks ketiga tidak termasuk di sini. Perpotongannya memberi kita array 2 dimensi dengan dua baris dan dua kolom:

Demikian pula, Anda dapat memilih berat badan semua anggota keluarga seperti ini: Anda hanya ingin baris kedua, jadi letakkan 1 sebelum koma. Anda menginginkan semua kolom, jadi gunakan titik-dua setelah koma. Perpotongannya memberi kita seluruh baris kedua.

Terakhir, array numpy dua dimensi memungkinkan Anda melakukan perhitungan elemen-demi-elemen, sama seperti yang Anda lakukan dengan array numpy 1 dimensi. Itu hal yang
---

## Ayo berlatih!

```yaml
type: FinalSlide
key: 6047b27c09
```

`@script`
bisa Anda coba di latihan, bersama dengan membuat dan melakukan subset pada array numpy 2 dimensi! Seru, kan?

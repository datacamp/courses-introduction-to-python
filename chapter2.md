---
title_meta: Bab 2
title: Daftar di Python
description: >-
  Pelajari cara menyimpan, mengakses, dan memanipulasi data dalam daftar,
  langkah pertama untuk bekerja secara efisien dengan data berukuran besar.
attachments:
  slides_link: 'https://projector-video-pdf-converter.datacamp.com/735/chapter2.pdf'
lessons:
  - nb_of_exercises: 4
    title: Daftar di Python
  - nb_of_exercises: 4
    title: Subsetting pada Daftar
  - nb_of_exercises: 5
    title: Memanipulasi Daftar
---

## Daftar Python

```yaml
type: VideoExercise
key: a5886d213f
xp: 50
```

`@projector_key`
a0530c4542f10988847b2dbb91f717c3

---

## Buat sebuah daftar

```yaml
type: NormalExercise
key: e6c527bf41
lang: python
xp: 100
skills:
  - 2
```

Daftar adalah **tipe data majemuk**; Anda dapat mengelompokkan beberapa nilai, seperti berikut:

```
a = "is"
b = "nice"
my_list = ["my", "list", a, b]
```

Setelah mengukur tinggi badan keluarga, Anda memutuskan untuk mengumpulkan beberapa informasi tentang rumah tempat Anda tinggal. Luas dari berbagai bagian rumah Anda disimpan dalam variabel terpisah di latihan ini.

`@instructions`
- Buat sebuah daftar, `areas`, yang berisi luas area untuk hallway (`hall`), kitchen (`kit`), living room (`liv`), bedroom (`bed`), dan bathroom (`bath`), dalam urutan tersebut. Gunakan variabel yang sudah disiapkan.
- Cetak `areas` dengan fungsi `print()`.

`@hint`
- Anda dapat menggunakan variabel yang sudah dibuat untuk membangun daftar: `areas = [hall, kit, ...]`.
- Pastikan untuk menggunakan tanda kurung siku `[]`, bukan kurung biasa `()`.
- Anda tidak perlu menggunakan tanda kutip saat menyimpan variabel di dalam daftar.
- Ketik `print(areas)` untuk mencetak daftar saat mengirimkan.

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
predef_msg = "Jangan hapus atau edit variabel yang sudah ditentukan!"
areas_msg = "Definisikan `areas` sebagai daftar yang berisi semua variabel area, dalam urutan yang benar: `[hall, kit, liv, bed, bath]`. Hati-hati dengan kesalahan ketik. Daftar ini tidak boleh berisi apa pun yang lain!"

Ex().check_correct(
    has_printout(0, not_printed_msg = "__JINJA__:Apakah kamu sudah menggunakan `{{sol_call}}` untuk mencetak daftar `areas` di akhir skripmu?"),
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

success_msg("Bagus! Daftar jauh lebih baik di sini, bukan?")
```

---

## Buat daftar dengan berbagai tipe

```yaml
type: NormalExercise
key: 1702a8bcdc
lang: python
xp: 100
skills:
  - 2
```

Meski tidak terlalu umum, sebuah daftar juga dapat berisi campuran tipe Python termasuk string, float, dan boolean.

Sekarang Anda akan menambahkan nama ruangan ke dalam daftar, sehingga Anda dapat melihat nama dan ukuran ruangan secara bersamaan.

Sebagian kode telah disediakan untuk membantu Anda memulai. Perhatikan baik-baik! `"bathroom"` adalah sebuah string, sedangkan `bath` adalah variabel yang merepresentasikan float `9.50` yang telah Anda tentukan sebelumnya.

`@instructions`
- Selesaikan kode yang membuat daftar `areas`. Bangun daftar tersebut sehingga setiap nama ruangan sebagai string muncul terlebih dahulu, lalu luasnya. Dengan kata lain, tambahkan string `"hallway"`, `"kitchen"`, dan `"bedroom"` pada lokasi yang sesuai.
- Cetak `areas` lagi; apakah kali ini hasil cetaknya lebih informatif?

`@hint`
- Empat elemen pertama dari daftar `areas` dikodekan sebagai `["hallway", hall, "kitchen", kit, ...`.
- Sebuah string harus diapit tanda kutip `""`.

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
predef_msg = "Jangan hapus atau edit variabel yang sudah ditentukan!"
areas_msg = "Kamu belum menetapkan nilai yang benar untuk `areas`. Coba lihat lagi instruksinya. Pastikan untuk menempatkan nama ruangan sebelum variabel yang berisi area setiap kali. Urutannya penting di sini! Hati-hati dengan kesalahan ketik."

Ex().check_correct(
  check_object("areas").has_equal_value(incorrect_msg = areas_msg),
  multi([ check_object(obj, missing_msg = predef_msg).has_equal_value(incorrect_msg = predef_msg) for obj in objs])
)

Ex().has_printout(0, not_printed_msg = "__JINJA__:Apakah kamu sudah menggunakan `{{sol_call}}` untuk mencetak daftar `areas` di akhir skripmu?")

success_msg("Bagus! Daftar ini berisi string dan float, tapi itu bukan masalah untuk Python!")
```

---

## Daftar dari banyak daftar

```yaml
type: NormalExercise
key: 9158c577b0
lang: python
xp: 100
skills:
  - 2
```

Sebagai data ilmuwan, Anda sering berhadapan dengan banyak data, dan masuk akal untuk mengelompokkan sebagian data tersebut.

Alih-alih membuat daftar yang berisi string dan float untuk merepresentasikan nama serta luas ruangan di rumah Anda, Anda dapat membuat daftar yang berisi banyak daftar.

Ingat: `"hallway"` adalah sebuah string, sedangkan `hall` adalah variabel yang merepresentasikan float `11.25` yang Anda tentukan sebelumnya.

`@instructions`
- Lengkapi daftar di dalam daftar sehingga juga mencakup data kamar tidur dan kamar mandi. Pastikan Anda memasukkannya sesuai urutan!
- Cetak `house`; apakah cara menyusun data seperti ini lebih masuk akal?

`@hint`
- Tambahkan _subdaftar_ ke daftar `house` dengan menambahkan `["bedroom", bed]` dan `["bathroom", bath]` di dalam tanda kurung siku.
- Ingat untuk menyertakan koma `,` setelah setiap subdaftar.
- Untuk mencetak variabel `x`, tuliskan `print(x)` pada baris baru.

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
predef_msg = "Jangan hapus atau edit variabel yang sudah ditentukan!"
house_msg = "Kamu belum menetapkan nilai yang benar untuk `house`. Coba lihat lagi instruksinya. Perluas daftar dari daftar sehingga mencakup daftar untuk setiap pasangan nama ruangan dan luas ruangan. Perhatikan urutan dan kesalahan ketik!"

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

Ex().has_printout(0, not_printed_msg = "__JINJA__:Apakah kamu sudah menggunakan `{{sol_call}}` untuk mencetak isi dari `house`?")

success_msg("Bagus! Bersiaplah untuk belajar tentang subset daftar!")
```

---

## Subsetting Daftar

```yaml
type: VideoExercise
key: c076b5a69c
xp: 50
```

`@projector_key`
fc15ba5cb9485456df8589130b519ea3

---

## Lakukan subset dan taklukkan

```yaml
type: NormalExercise
key: c3ce582e32
lang: python
xp: 100
skills:
  - 2
```

Subsetting daftar Python itu mudah sekali. Perhatikan contoh kode di bawah ini, yang membuat daftar `x` lalu memilih "b" darinya. Ingat bahwa ini adalah elemen kedua, sehingga memiliki indeks 1. Anda juga dapat menggunakan pengindeksan negatif.

```
x = ["a", "b", "c", "d"]
x[1]
x[-3] # hasilnya sama!
```

Ingat daftar `areas` dari sebelumnya, yang berisi string dan float? Definisinya sudah ada di skrip. Apakah Anda dapat menambahkan kode yang benar untuk melakukan subsetting di Python?

`@instructions`
- Cetak elemen kedua dari daftar `areas` (nilainya `11.25`).
- Subset dan cetak elemen terakhir dari `areas`, yaitu `9.50`. Menggunakan indeks negatif masuk akal di sini!
- Pilih angka yang merepresentasikan area ruang keluarga (`20.0`) dan cetak hasilnya.

`@hint`
- Gunakan `x[1]` untuk memilih elemen kedua dari sebuah daftar `x`.
- Gunakan `x[-1]` untuk memilih elemen terakhir dari sebuah daftar `x`.
- Pastikan untuk membungkus operasi subsetting Anda dalam pemanggilan `print()`.
- Angka yang merepresentasikan area ruang keluarga adalah elemen ke-6 dalam daftar, jadi Anda perlu `[5]` di sini. `area[4]` akan menampilkan string!

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
msg = "Jangan hapus atau edit daftar `areas` yang sudah ditentukan."
Ex().check_object("areas", missing_msg = msg).has_equal_value(incorrect_msg = msg)
Ex().has_printout(0, not_printed_msg = "Coba lihat lagi kodenya untuk mencetak elemen kedua di `areas`, yang ada di indeks `1`.")
Ex().has_printout(1, not_printed_msg = "Coba lihat lagi kodenya untuk mencetak elemen terakhir di `areas`, yang ada di indeks `-1`.")
Ex().has_printout(2, not_printed_msg = "Coba lihat lagi kodenya untuk mencetak area ruang tamu. Itu ada di indeks `5`.")
success_msg("Kerja bagus!")
```

---

## Mengiris dan memotong

```yaml
type: NormalExercise
key: 7f08642d18
lang: python
xp: 100
skills:
  - 2
```

Memilih satu nilai dari sebuah daftar hanyalah sebagian cerita. Anda juga bisa melakukan _slice_ pada daftar, yaitu memilih beberapa elemen sekaligus dari daftar. Gunakan sintaks berikut:

```
my_list[start:end]
```

Indeks `start` akan disertakan, sedangkan indeks `end` _tidak_ disertakan. Namun, Anda juga bisa tidak menyebutkan indeks tersebut. Jika Anda tidak menyebutkan indeks `start`, Python akan memahami bahwa Anda ingin memulai mengiris dari awal daftar.

`@instructions`
- Gunakan mengiris untuk membuat daftar `downstairs` yang berisi 6 elemen pertama dari `areas`.
- Buat `upstairs` sebagai `4` elemen terakhir dari `areas`. Kali ini, sederhanakan mengiris dengan menghilangkan indeks `end`.
- Cetak `downstairs` dan `upstairs` menggunakan `print()`.

`@hint`
- Gunakan kurung siku `[0:6]` untuk mengambil enam elemen pertama dari sebuah daftar.
- Untuk mengambil semua elemen kecuali 5 elemen pertama dari sebuah daftar `l`, gunakan `l[5:]`.
- Tambahkan dua pemanggilan `print()` untuk mencetak `downstairs` dan `upstairs`.

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
msg = "Jangan hapus atau edit daftar `areas` yang sudah ditentukan."
Ex().check_object("areas", missing_msg = msg).has_equal_value(incorrect_msg = msg)

patt = "`%s` tidak benar. Gunakan `areas[%s]` dan slicing untuk memilih elemen yang kamu inginkan, atau sesuatu yang setara."
Ex().check_object("downstairs").has_equal_value(incorrect_msg = patt % ('downstairs', '0:6'))
Ex().check_object("upstairs").has_equal_value(incorrect_msg = patt % ("upstairs",":6"))

Ex().has_printout(0, not_printed_msg="Apakah kamu sudah mencetak `downstairs` setelah menghitungnya?")
Ex().has_printout(1, not_printed_msg="Apakah kamu sudah mencetak `upstairs` setelah menghitungnya?")

success_msg("Bagus!")
```

---

## Melakukan subsetting daftar dari daftar

```yaml
type: NormalExercise
key: dbbbd306cf
xp: 100
```

Sebuah daftar di Python juga dapat berisi daftar lainnya.

Untuk melakukan subsetting pada daftar yang berisi daftar, Anda dapat menggunakan teknik yang sama seperti sebelumnya: kurung siku. Contohnya untuk sebuah daftar, `house`:

```
house[2][0]
```

`@instructions`
- Subset daftar `house` untuk mendapatkan float `9.5`.

`@hint`
- Uraikan langkah demi langkah. Pertama, ambil elemen terakhir dari daftar, `["bathroom", 9.50]`. Ingat bahwa indeks elemen terakhir adalah `-1`.
- Selanjutnya, ambil elemen kedua dari `["bathroom", 9.50]`, yang berada pada indeks `1`.

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

success_msg("Benar sekali! Bagian terakhir dari teka-teki daftar adalah manipulasi.")
```

---

## Memanipulasi Daftar

```yaml
type: VideoExercise
key: d7fe818b3a
xp: 50
```

`@projector_key`
355ed52d2fb0d67508c6a311b7cbc6d3

---

## Ganti elemen daftar

```yaml
type: NormalExercise
key: 4e1bba1b55
lang: python
xp: 100
skills:
  - 2
```

Untuk mengganti elemen daftar, Anda melakukan subsetting pada daftar dan menugaskan nilai baru ke subset tersebut. Anda bisa memilih elemen tunggal atau mengubah seluruh irisan daftar sekaligus.

Untuk latihan ini dan latihan berikutnya, Anda akan tetap bekerja pada daftar `areas` yang berisi nama dan luas berbagai ruangan di sebuah rumah.

`@instructions`
- Perbarui luas kamar mandi menjadi `10.50` meter persegi alih-alih `9.50` dengan menggunakan pengindeksan negatif.
- Buat daftar `areas` lebih trendi! Mengubah `"living room"` jadi `"chill zone"`. Kali ini jangan gunakan pengindeksan negatif.

`@hint`
- Untuk memperbarui luas kamar mandi identifikasi subset luas kamar mandi (ini adalah item terakhir pada daftar!).
- Lalu, ganti nilainya dengan area kamar mandi yang baru dengan menugaskannya ke subset tersebut.
- Lakukan hal yang sama untuk memperbarui nama `"living room"`, yaitu pada indeks 4.

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
bathroom_msg = 'Kamu bisa menggunakan `areas[-1] = 10.50` untuk memperbarui luas kamar mandi.'
chillzone_msg = 'Kamu bisa menggunakan `areas[4] = "chill zone"` untuk memperbarui nama ruang tamu.'
Ex().check_correct(
  check_object('areas').has_equal_value(incorrect_msg = 'Perubahanmu pada `areas` tidak menghasilkan daftar yang benar. Apakah kamu yakin menggunakan operasi subset yang benar? Jika ragu, kamu bisa menggunakan petunjuk!'),
  multi(
    has_equal_value(expr_code='areas[-1]', override=10.50, incorrect_msg = bathroom_msg),
    has_equal_value(expr_code='areas[4]', override='chill zone', incorrect_msg = chillzone_msg),
  )
)
success_msg('Mantap! Seperti yang ditunjukkan dalam contoh kode, kamu juga bisa memotong daftar dan menggantinya dengan daftar lain untuk memperbarui beberapa elemen dalam satu perintah.')
```

---

## Perluas daftar

```yaml
type: NormalExercise
key: ff0fe8d967
lang: python
xp: 100
skills:
  - 2
```

Jika Anda dapat mengubah elemen dalam sebuah daftar, tentu Anda juga ingin bisa menambahkan elemen ke dalamnya, bukan? Anda dapat menggunakan operator `+`:

```
x = ["a", "b", "c", "d"]
y = x + ["e", "f"]
```

Anda baru saja memenangkan lotre, luar biasa! Anda memutuskan untuk membangun paviliun dekat kolam (poolhouse) dan garasi. Dapatkah Anda menambahkan informasi tersebut ke daftar `area`?

`@instructions`
- Gunakan operator `+` untuk menempelkan daftar `["poolhouse", 24.5]` ke akhir daftar `areas`. Simpan daftar hasilnya sebagai `areas_1`.
- Perluas lagi `areas_1` dengan menambahkan data tentang garasi Anda. Tambahkan string `"garage"` dan float `15.45`. Beri nama list hasilnya `areas_2`.

`@hint`
- Ikuti contoh kode pada tugas. Di sini `x` adalah `areas`, dan `["e", "f"]` adalah `["poolhouse", 24.5]`.
- Untuk menambahkan elemen lebih banyak ke `areas_1`, gunakan `areas_1 + ["element", 123]`.

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
msg = "Jangan hapus atau edit daftar `areas` yang sudah ditentukan."
Ex().check_object("areas", missing_msg = msg).has_equal_value(incorrect_msg = msg)
Ex().check_object("areas_1").has_equal_value(incorrect_msg = "Gunakan `areas + [\"poolhouse\", 24.5]` untuk membuat `areas_1`. Hati-hati dengan kesalahan ketik!")
Ex().check_object("areas_2").has_equal_value(incorrect_msg = "Gunakan `areas_1 + [\"garage\", 15.45]` untuk membuat `areas_2`. Hati-hati dengan kesalahan ketik!")
success_msg("Keren! Daftarnya mulai terbentuk dengan baik!")
```

---

## Hapus elemen daftar

```yaml
type: NormalExercise
key: 85f792356e
xp: 100
```

Terakhir, Anda juga dapat menghapus elemen dari daftar. Anda bisa melakukannya dengan pernyataan `del`:

```
x = ["a", "b", "c", "d"]
del x[1]
```

Perhatikan baik-baik, begitu Anda menghapus satu elemen dari daftar, pengindeksan semua elemen setelah elemen yang dihapus akan berubah!

Sayangnya, jumlah kemenangan lotre Anda ternyata tidak terlalu besar dan sepertinya rencana poolhouse tidak akan terwujud. Anda perlu menghapusnya dari daftar. Anda memutuskan untuk menghapus string dan float yang terkait dari daftar `areas`.

`@instructions`
- Hapus string dan float untuk `"poolhouse"` dari daftar `areas` Anda.
- Cetak daftar `areas` yang telah diperbarui.

`@hint`
- Anda perlu menggunakan `del` dua kali untuk menghapus dua elemen. Namun hati-hati, pengindeksan bisa berubah!

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

Ex().has_printout(0, not_printed_msg="Apakah kamu sudah mencetak `areas` setelah menghapus string dan float poolhouse?")
success_msg("Benar! Kamu akan belajar cara yang lebih mudah untuk menghapus elemen tertentu dari daftar Python nanti.")
```

---

## Cara kerja internal daftar

```yaml
type: NormalExercise
key: af72db9915
lang: python
xp: 100
skills:
  - 2
```

Sejumlah kode telah disediakan untuk Anda dalam latihan ini: sebuah daftar bernama `areas` dan salinannya bernama `areas_copy`.

Saat ini, elemen pertama pada daftar `areas_copy` diubah dan daftar `areas` dicetak. Jika Anda menekan tombol jalankan kode, Anda akan melihat bahwa meskipun Anda mengubah `areas_copy`, perubahan tersebut juga berlaku pada daftar `areas`. Ini karena `areas` dan `areas_copy` menunjuk ke daftar yang sama.

Jika Anda ingin mencegah perubahan di `areas_copy` agar tidak ikut berlaku pada `areas`, Anda harus membuat salinan `areas` secara eksplisit dengan `list()` atau menggunakan `[:]`.

`@instructions`
- Ubah perintah kedua, yang membuat variabel `areas_copy`, sehingga `areas_copy` merupakan salinan eksplisit dari `areas`. Setelah Anda mengeditnya, perubahan yang dilakukan pada `areas_copy` tidak boleh memengaruhi `areas`. Kirim Jawaban untuk memeriksa hasilnya.

`@hint`
- Ubah pemanggilan `areas_copy = areas`. Alih-alih menugaskan `areas`, Anda dapat menugaskan `list(areas)` atau `areas[:]`.

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
  check_object("areas_copy").has_equal_value(incorrect_msg = "Sepertinya `areas_copy` belum diperbarui dengan benar."),
  check_function("list", missing_msg = "Pastikan untuk menggunakan `list(areas)` untuk membuat `areas_copy`.")
)

mmsg = "Jangan hapus daftar `areas` yang sudah ditentukan."
imsg = "Pastikan untuk mengedit HANYA salinannya, bukan daftar `areas` yang asli. Lihat kembali deskripsi latihan jika kamu tidak yakin bagaimana cara membuat salinan."
Ex().check_correct(
  check_object("areas", missing_msg = mmsg).has_equal_value(incorrect_msg = imsg),
  check_function("list", missing_msg = "Pastikan untuk menggunakan `list(areas)` untuk membuat `areas_copy`.")
)

success_msg("Bagus! Perbedaan antara salinan eksplisit dan berbasis referensi itu halus, tetapi bisa sangat penting. Cobalah untuk mengingat bagaimana daftar disimpan dalam memori komputer.")
```

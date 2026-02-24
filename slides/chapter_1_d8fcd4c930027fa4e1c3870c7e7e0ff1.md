---
title: Insert title here
key: d8fcd4c930027fa4e1c3870c7e7e0ff1
video_link:
  mp3: >-
    https://videos.datacamp.com/mp3/translations/course_735/id-ID/8e66ce6b-ae24-4017-80b6-217d0c83b9c6.mp3
---

## Halo Python!

```yaml
type: TitleSlide
key: f743ca8c41
```

`@lower_third`
name: Hugo Bowne-Anderson
title: Data Scientist at DataCamp

`@script`
Hai, nama saya Hugo dan saya akan menjadi pemandu Anda ke Pengantar Python untuk Sains Data.

Saya seorang ilmuwan data dan pendidik di DataCamp.
---

## Bagaimana Anda akan belajar

```yaml
type: FullSlide
key: 30ee08a725
disable_transition: true
```

`@part1`
![Antarmuka DataCamp](https://assets.datacamp.com/img/translations/id-ID/production/repositories/288/datasets/729574d2168960686381caefe79baf5978e27d0d/liveexercise.gif)

`@script`
Di kursus ini, Anda akan belajar Python untuk Sains Data melalui pelajaran video seperti ini, dan latihan interaktif. Anda mendapat sesi Python Anda sendiri tempat Anda bisa bereksperimen dan mencoba menyusun kode yang benar untuk menyelesaikan instruksi. Anda belajar sambil praktik, sambil menerima umpan balik yang disesuaikan dan instan atas pekerjaan Anda.
---

## Python

```yaml
type: FullSlide
key: 3f23b93572
```

`@part1`
![guido-hba.png](https://assets.datacamp.com/img/translations/id-ID/production/repositories/288/datasets/fb3e4b8dc114529dafffb37d33f2b2244210d40f/guido-hba.png = 38){{1}}

- Tujuan umum: membangun apa saja{{2}}

- Sumber terbuka! Gratis!{{3}}

- Paket Python, termasuk untuk ilmu data{{4}}

	- Banyak aplikasi dan bidang{{5}}

`@script`
Python diciptakan oleh Guido Van Rossum. Di sini, Anda bisa melihat foto saya bersama Guido. Satu hal yang awalnya proyek hobi, segera menjadi bahasa pemrograman serbaguna: saat ini, Anda bisa menggunakan Python untuk membangun hampir semua perangkat lunak. Bagaimana ini bisa terjadi? Pertama, Python bersifat sumber terbuka. Gratis untuk digunakan. Kedua, sangat mudah membangun paket di Python, yaitu kumpulan kode yang bisa Anda bagikan dengan orang lain untuk memecahkan masalah tertentu. Seiring waktu, semakin banyak paket yang khusus dibangun untuk sains data telah dikembangkan. Misalnya Anda ingin membuat visualisasi menarik untuk penjualan perusahaan Anda. Ada paket untuk itu. Bagaimana dengan terhubung ke basis data untuk menganalisis pengukuran sensor? Itu juga ada paketnya.
Orang sering menyebut Python bagaikan pisau serbaguna dalam bahasa pemrograman karena Anda bisa melakukan hampir apa pun dengannya.
Di kursus ini, kita akan mulai membangun keterampilan melakukan koding sains data Anda sedikit demi sedikit, jadi pastikan Anda tetap mengikuti untuk melihat betapa efektifnya bahasa ini.
---

## IPython Shell

```yaml
type: FullSlide
key: 43a91a7217
```

`@part1`
**Jalankan perintah Python**

![ipython_shell.png](https://assets.datacamp.com/img/translations/id-ID/production/repositories/288/datasets/a9e8440bb8fbd49e4a73e4c36ef1cd677c0dd55f/pyexercise.png = 95)

`@script`
Sekarang Anda sudah menyiapkan mata dan telinga untuk Python, mari mulai bereksperimen. Saya akan mulai dengan
---

## IPython Shell

```yaml
type: FullSlide
key: 9c51ee700d
disable_transition: true
```

`@part1`
**Jalankan perintah Python**

![ipython_shell_highlighted.png](https://assets.datacamp.com/img/translations/id-ID/production/repositories/288/datasets/dd43cc0183b15b43a072eb0fbab4caa72dee9250/pyexercise_shell.jpg = 95)

`@script`
shell Python, tempat Anda bisa mengetik kode Python dan langsung melihat hasilnya. Di antarmuka latihan DataCamp, shell ini disematkan di sini. Mari mulai dengan sederhana dan gunakan Python sebagai kalkulator.
---

## IPython Shell

```yaml
type: FullSlide
key: 524e4c20a7
disable_transition: true
```

`@part1`
&nbsp;

![Perhitungan di shell IPython DataCamp](https://assets.datacamp.com/img/translations/id-ID/production/repositories/288/datasets/cee32b788a62e4b9a1234ccde56ac9ebb49cfa72/shelladdition.gif = 95)

`@script`
Biarkan saya mengetik 4 + 5, lalu tekan Enter. Python menafsirkan apa yang Anda ketik dan menampilkan hasil perhitungannya, 9. Shell Python yang digunakan di sini sebenarnya bukan yang asli; kita menggunakan IPython, singkatan dari Interactive Python, semacam versi Python biasa yang ditingkatkan yang akan berguna nanti.

IPython dibuat oleh Fernando Pérez dan merupakan bagian dari ekosistem Jupyter yang lebih luas. Selain bekerja interaktif dengan Python, Anda juga bisa membuat Python menjalankan yang disebut
---

## Skrip Python

```yaml
type: FullSlide
key: 78ef256bc0
```

`@part1`
- Berkas teks - `.py`{{1}}

- Daftar perintah Python{{2}}

- Sama seperti mengetik di IPython Shell{{3}}

![Skrip Python di DataCamp](https://assets.datacamp.com/img/translations/id-ID/production/repositories/288/datasets/59f196e96536543a4fb8801228019fc4106f3791/pyexercise_script.jpg =78){{3}}

`@script`
skrip python. Skrip python ini pada dasarnya adalah berkas teks dengan ekstensi titik py. Ini pada dasarnya daftar perintah Python yang dijalankan, seolah-olah Anda mengetik perintahnya sendiri di shell, baris demi baris.
---

## Skrip Python

```yaml
type: FullSlide
key: 717d124175
disable_transition: true
```

`@part1`
![GIF: Mengetik 4 + 5 di skrip dan menekan tombol kirim jawaban. Tidak ada output yang ditampilkan.](https://assets.datacamp.com/img/translations/id-ID/production/repositories/288/datasets/2f96e979012e15329cc158d1e0f496aac3539f45/scriptnoprint.gif = 95)

`@script`
Sekarang mari kita masukkan perintah tadi ke dalam skrip yang bisa Anda temukan di antarmuka DataCamp ini. Langkah berikutnya adalah mengeksekusi skripnya, dengan mengklik "Submit Answer". Jika Anda mengeksekusi skrip ini di antarmuka DataCamp, tidak ada apa pun di panel output. Hal itu karena Anda harus secara eksplisit menggunakan print di dalam skrip jika ingin menghasilkan output saat eksekusi.
---

## Skrip Python

```yaml
type: FullSlide
key: c7a9d02fb6
disable_transition: true
code_zoom: 90
```

`@part1`
![python_script_print.gif](https://assets.datacamp.com/img/translations/id-ID/production/repositories/288/datasets/8b13d046bb54dcb11aa49f0da7363781129d1561/scriptwithprint.gif = 95)

- Gunakan `print()` untuk menghasilkan output dari skrip.

`@script`
Mari kita bungkus perhitungan sebelumnya di dalam pemanggilan print, lalu jalankan ulang skripnya. Kali ini, ouput yang sama seperti sebelumnya muncul, mantap! Menaruh kode Anda di skrip Python alih-alih mengetik ulang setiap langkah secara interaktif akan membantu Anda menjaga struktur dan menghindari mengetik ulang semuanya berkali-kali saat ingin melakukan perubahan; Anda cukup mengubahnya di skrip, lalu jalankan ulang semuanya.
---

## Antarmuka DataCamp

```yaml
type: FullSlide
key: 693ba1cd14
```

`@part1`
![Tangkapan layar antarmuka DataCamp](https://assets.datacamp.com/img/translations/id-ID/production/repositories/288/datasets/a9e8440bb8fbd49e4a73e4c36ef1cd677c0dd55f/pyexercise.png)

`@script`
Sekarang setelah Anda mendapat gambaran tentang berbagai cara bekerja dengan Python, saya sarankan Anda lanjut ke latihan. Gunakan IPython Shell untuk bereksperimen, dan gunakan editor skrip Python untuk menulis jawaban sebenarnya. Jika Anda mengklik Submit Answer, skrip Anda akan dijalankan dan diperiksa kebenarannya.
---

## Ayo berlatih!

```yaml
type: FinalSlide
key: 7445cd202e
```

`@script`
Selamat melakukan koding dan jangan lupa bersenang-senang!

# PPL-Iterator

Project ini merupakan contoh implementasi sederhana dari **Iterator Design Pattern** menggunakan bahasa Python.

## Deskripsi

Iterator Pattern digunakan untuk menelusuri elemen dalam sebuah collection secara berurutan tanpa perlu mengetahui struktur internal dari collection tersebut. Pada program ini, data mahasiswa disimpan dalam `StudentCollection`. Untuk membaca data mahasiswa satu per satu, digunakan objek `StudentIterator`.

## Struktur Program

- `Student` Merepresentasikan data mahasiswa yang memiliki atribut nama.

- `StudentCollection` Berfungsi sebagai tempat penyimpanan kumpulan data mahasiswa.

- `StudentIterator` Berfungsi untuk menelusuri data mahasiswa satu per satu menggunakan method `has_next()` dan `next()`.

## Cara Kerja

Program menambahkan beberapa data mahasiswa ke dalam collection, kemudian membuat iterator untuk membaca data tersebut secara berurutan.

Output program:

```
Ahsin
Naufal
Aziz

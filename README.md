# Design Pattern Implementation in Python

Repository ini berisi contoh implementasi dua design pattern menggunakan bahasa Python, yaitu **Iterator Pattern** dan **Repository Pattern**. Project ini dibuat sebagai bahan pembelajaran untuk memahami bagaimana design pattern membantu membuat struktur kode menjadi lebih rapi, mudah dipahami, dan lebih mudah dikembangkan.

Pada project ini, setiap pattern dibuat dalam contoh sederhana agar konsep utamanya lebih mudah dipahami. Iterator Pattern digunakan untuk membaca daftar mahasiswa secara berurutan, sedangkan Repository Pattern digunakan untuk mengelola data produk melalui class repository.

---

## Daftar Isi

- [Deskripsi Project](#deskripsi-project)
- [Iterator Pattern](#iterator-pattern)
- [Repository Pattern](#repository-pattern)
- [Struktur File](#struktur-file)
- [Cara Menjalankan Program](#cara-menjalankan-program)
- [Kesimpulan](#kesimpulan)

---

## Deskripsi Project

Design pattern adalah pola penyelesaian yang sering digunakan dalam pengembangan perangkat lunak. Dengan menggunakan design pattern, kode dapat dibuat lebih terstruktur karena setiap bagian memiliki tanggung jawab yang lebih jelas.

Dalam repository ini, terdapat dua file utama:

1. `iterator.py`, yang berisi contoh penerapan Iterator Pattern.
2. `repository.py`, yang berisi contoh penerapan Repository Pattern.

Kedua contoh tersebut dibuat secara sederhana, namun tetap menggambarkan fungsi utama dari masing-masing pattern.

---

## Iterator Pattern

Iterator Pattern adalah design pattern yang digunakan untuk mengakses data dalam sebuah collection secara berurutan tanpa perlu mengetahui bagaimana data tersebut disimpan di dalamnya.

Pada contoh ini, data mahasiswa disimpan dalam sebuah collection. Untuk membaca data tersebut satu per satu, program menggunakan iterator. Dengan cara ini, bagian utama program tidak perlu mengakses list mahasiswa secara langsung.

### Tujuan Penggunaan

Iterator Pattern digunakan agar proses membaca data menjadi lebih teratur. Program cukup memanggil iterator untuk mengambil data berikutnya sampai semua data selesai dibaca.

Pattern ini cocok digunakan ketika:

- Data perlu dibaca satu per satu secara berurutan.
- Struktur penyimpanan data tidak ingin ditampilkan langsung ke bagian utama program.
- Collection dapat berubah bentuk, tetapi cara membacanya tetap dibuat konsisten.

### Struktur Class

#### 1. `Student`

Class `Student` digunakan untuk merepresentasikan data mahasiswa.

```python
class Student:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name
```

Class ini memiliki atribut `name` untuk menyimpan nama mahasiswa. Method `get_name()` digunakan untuk mengambil nama mahasiswa tersebut.

#### 2. `StudentIterator`

Class `StudentIterator` digunakan untuk membaca data mahasiswa satu per satu.

```python
class StudentIterator:
    def __init__(self, students):
        self.students = students
        self.position = 0

    def has_next(self):
        return self.position < len(self.students)

    def next(self):
        student = self.students[self.position]
        self.position += 1
        return student
```

Class ini menyimpan daftar mahasiswa dan posisi data yang sedang dibaca. Method `has_next()` digunakan untuk mengecek apakah masih ada data berikutnya, sedangkan method `next()` digunakan untuk mengambil data mahasiswa berikutnya.

#### 3. `StudentCollection`

Class `StudentCollection` digunakan sebagai tempat penyimpanan data mahasiswa.

```python
class StudentCollection:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def create_iterator(self):
        return StudentIterator(self.students)
```

Class ini memiliki method `add_student()` untuk menambahkan mahasiswa ke dalam collection. Method `create_iterator()` digunakan untuk membuat iterator yang akan membaca isi collection tersebut.

### Contoh Penggunaan

```python
students = StudentCollection()
students.add_student(Student("Ahsin"))
students.add_student(Student("Naufal"))
students.add_student(Student("Aziz"))

iterator = students.create_iterator()

while iterator.has_next():
    student = iterator.next()
    print(student.get_name())
```

### Output Program

```bash
Ahsin
Naufal
Aziz
```

Dari output tersebut, dapat dilihat bahwa data mahasiswa ditampilkan satu per satu sesuai urutan data yang dimasukkan.

---

## Repository Pattern

Repository Pattern adalah design pattern yang digunakan untuk memisahkan proses akses data dari logika utama program. Dengan pattern ini, proses seperti menambah, mencari, menampilkan, dan menghapus data ditempatkan dalam class repository.

Pada contoh ini, Repository Pattern digunakan untuk mengelola data produk. Data produk tidak langsung dikelola oleh program utama, tetapi melalui `ProductRepository`.

### Tujuan Penggunaan

Repository Pattern digunakan agar kode yang berhubungan dengan penyimpanan dan pengambilan data berada di tempat yang terpisah. Hal ini membuat kode lebih rapi karena setiap class memiliki peran masing-masing.

Pattern ini cocok digunakan ketika:

- Program memiliki proses pengelolaan data.
- Akses data ingin dipisahkan dari logika utama program.
- Struktur penyimpanan data mungkin berubah di masa depan.
- Program membutuhkan kode yang lebih mudah dirawat dan dikembangkan.

### Struktur Class

#### 1. `Product`

Class `Product` digunakan untuk merepresentasikan data produk.

```python
class Product:
    def __init__(self, product_id, name, price):
        self.id = product_id
        self.name = name
        self.price = price
```

Class ini memiliki tiga atribut, yaitu `id`, `name`, dan `price`. Atribut tersebut digunakan untuk menyimpan ID produk, nama produk, dan harga produk.

#### 2. `ProductRepository`

Class `ProductRepository` digunakan sebagai tempat utama untuk mengelola data produk.

```python
class ProductRepository:
    def __init__(self):
        self.products = []

    def find_all(self):
        return self.products

    def find_by_id(self, product_id):
        for product in self.products:
            if product.id == product_id:
                return product
        return None

    def save(self, product):
        self.products.append(product)

    def delete(self, product_id):
        self.products = [
            product for product in self.products
            if product.id != product_id
        ]
```

Class ini memiliki beberapa method penting:

- `find_all()` digunakan untuk mengambil semua data produk.
- `find_by_id()` digunakan untuk mencari produk berdasarkan ID.
- `save()` digunakan untuk menambahkan produk baru.
- `delete()` digunakan untuk menghapus produk berdasarkan ID.

Dengan adanya repository, bagian lain dari program tidak perlu mengetahui detail bagaimana data produk disimpan atau dihapus.

#### 3. `ProductService`

Class `ProductService` digunakan sebagai penghubung antara program utama dan repository.

```python
class ProductService:
    def __init__(self, repository):
        self.repository = repository

    def add_product(self, product):
        self.repository.save(product)

    def show_products(self):
        return self.repository.find_all()

    def remove_product(self, product_id):
        self.repository.delete(product_id)
```

Class ini tidak menyimpan data secara langsung. Tugasnya adalah memanggil method yang tersedia di `ProductRepository`. Dengan pembagian seperti ini, kode menjadi lebih mudah dibaca karena logika service dan logika akses data tidak dicampur dalam satu tempat.

### Contoh Penggunaan

```python
repository = ProductRepository()
service = ProductService(repository)

service.add_product(Product(1, "Book", 50000))
service.add_product(Product(2, "Keyboard", 150000))

for product in service.show_products():
    print(product.name, product.price)
```

### Output Program

```bash
Book 50000
Keyboard 150000
```

Output tersebut menunjukkan bahwa data produk berhasil ditambahkan melalui service, lalu ditampilkan kembali dari repository.

---

## Struktur File

```bash
.
├── iterator.py
├── repository.py
└── README.md
```

Keterangan:

- `iterator.py` berisi implementasi Iterator Pattern untuk membaca data mahasiswa.
- `repository.py` berisi implementasi Repository Pattern untuk mengelola data produk.
- `README.md` berisi dokumentasi dan penjelasan project.

---

## Cara Menjalankan Program

Pastikan Python sudah terinstall di komputer. Setelah itu, jalankan file sesuai pattern yang ingin diuji.

Untuk menjalankan program Iterator Pattern:

```bash
python iterator.py
```

Untuk menjalankan program Repository Pattern:

```bash
python repository.py
```

---

## Kesimpulan

Berdasarkan implementasi pada project ini, dapat disimpulkan bahwa design pattern membantu membuat kode menjadi lebih terarah dan mudah dipahami.

Iterator Pattern membantu proses membaca data secara berurutan tanpa membuat program utama bergantung langsung pada struktur collection. Sementara itu, Repository Pattern membantu memisahkan logika akses data dari logika utama program, sehingga kode menjadi lebih rapi dan lebih mudah dikembangkan.


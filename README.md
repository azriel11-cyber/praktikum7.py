
Program sederhana untuk mengelola data nilai mahasiswa menggunakan konsep Object-Oriented Programming (OOP) dalam Python.
## Class Diagram


┌─────────────────────────────────┐
│      DaftarNilai                │
├─────────────────────────────────┤
│ - data_mahasiswa: list          │
├─────────────────────────────────┤
│ + __init__()                    │
│ + tambah()                      │
│ + tampilkan()                   │
│ + hapus(nama: string)           │
│ + ubah(nama: string)            │
└─────────────────────────────────┘


### Penjelasan Class Diagram:
- *Class Name*: DaftarNilai
- *Attribute*: 
  - data_mahasiswa: list yang menyimpan data mahasiswa (nama dan nilai)
- *Methods*:
  - __init__(): Constructor untuk inisialisasi list kosong
  - tambah(): Menambahkan data mahasiswa baru
  - tampilkan(): Menampilkan semua data mahasiswa
  - hapus(nama): Menghapus data mahasiswa berdasarkan nama
  - ubah(nama): Mengubah data mahasiswa berdasarkan nama

## Flowchart Program Utama


        START
          |
          v
    ┌─────────────┐
    │  Inisialisasi │
    │  DaftarNilai │
    └──────┬──────┘
           |
           v
    ┌─────────────┐
    │ Tampilkan   │
    │    Menu     │
    └──────┬──────┘
           |
           v
    ┌─────────────┐
    │ Input Pilihan│
    └──────┬──────┘
           |
           v
      ╔═══════════╗
      ║  Pilihan? ║
      ╚═══╤═══════╝
          |
    ┌─────┼─────┬─────┬─────┬─────┐
    v     v     v     v     v     v
   [1]   [2]   [3]   [4]   [5]  [Lain]
    |     |     |     |     |     |
Tambah Tampil Hapus Ubah Keluar Invalid
    |     |     |     |     |     |
    └─────┴─────┴─────┴─────┘     |
           |                      |
           v                      v
    ┌─────────────┐        ┌──────────┐
    │Kembali ke   │        │  Pesan   │
    │   Menu      │        │  Error   │
    └──────┬──────┘        └────┬─────┘
           |                    |
           └────────────────────┘
                    |
                    v
                  END


## Flowchart Method tambah()


        START
          |
          v
    ┌─────────────┐
    │  Tampilkan  │
    │   Header    │
    └──────┬──────┘
           |
           v
    ┌─────────────┐
    │ Input Nama  │
    └──────┬──────┘
           |
           v
    ┌─────────────┐
    │ Input Nilai │
    └──────┬──────┘
           |
           v
    ┌─────────────┐
    │   Tambah ke │
    │data_mahasiswa│
    └──────┬──────┘
           |
           v
    ┌─────────────┐
    │  Tampilkan  │
    │Pesan Sukses │
    └──────┬──────┘
           |
           v
         END


## Flowchart Method tampilkan()


        START
          |
          v
    ┌─────────────┐
    │  Tampilkan  │
    │   Header    │
    └──────┬──────┘
           |
           v
      ╔═══════════╗
      ║   Data    ║
      ║  Kosong?  ║
      ╚═══╤═══════╝
          |
    ┌─────┴─────┐
    |           |
   YA          TIDAK
    |           |
    v           v
┌────────┐  ┌─────────────┐
│ Pesan  │  │  Tampilkan  │
│"Belum  │  │   Tabel     │
│ Ada    │  │   Header    │
│ Data"  │  └──────┬──────┘
└───┬────┘         |
    |              v
    |      ┌─────────────┐
    |      │   Loop      │
    |      │  Setiap     │
    |      │ Mahasiswa   │
    |      └──────┬──────┘
    |             |
    |             v
    |      ┌─────────────┐
    |      │  Tampilkan  │
    |      │  Data Mhs   │
    |      └──────┬──────┘
    |             |
    └─────────────┘
           |
           v
         END


## Flowchart Method hapus(nama)


        START
          |
          v
    ┌─────────────┐
    │   Loop      │
    │   Cari      │
    │   Nama      │
    └──────┬──────┘
           |
           v
      ╔═══════════╗
      ║   Nama    ║
      ║ Ditemukan?║
      ╚═══╤═══════╝
          |
    ┌─────┴─────┐
    |           |
   YA          TIDAK
    |           |
    v           v
┌────────┐  ┌─────────────┐
│ Hapus  │  │  Tampilkan  │
│  Data  │  │    Pesan    │
└───┬────┘  │"Tidak       │
    |       │ Ditemukan"  │
    v       └──────┬──────┘
┌────────┐         |
│ Pesan  │         |
│"Berhasil│        |
│Dihapus"│         |
└───┬────┘         |
    |              |
    └──────┬───────┘
           |
           v
         END


## Flowchart Method ubah(nama)


        START
          |
          v
    ┌─────────────┐
    │   Loop      │
    │   Cari      │
    │   Nama      │
    └──────┬──────┘
           |
           v
      ╔═══════════╗
      ║   Nama    ║
      ║ Ditemukan?║
      ╚═══╤═══════╝
          |
    ┌─────┴─────┐
    |           |
   YA          TIDAK
    |           |
    v           v
┌────────┐  ┌─────────────┐
│ Input  │  │  Tampilkan  │
│  Nama  │  │    Pesan    │
│  Baru  │  │"Tidak       │
└───┬────┘  │ Ditemukan"  │
    |       └──────┬──────┘
    v              |
┌────────┐         |
│ Input  │         |
│ Nilai  │         |
│  Baru  │         |
└───┬────┘         |
    |              |
    v              |
┌────────┐         |
│ Update │         |
│  Data  │         |
└───┬────┘         |
    |              |
    v              |
┌────────┐         |
│ Pesan  │         |
│"Berhasil│        |
│Diubah" │         |
└───┬────┘         |
    |              |
    └──────┬───────┘
           |
           v
         END


## Cara Menjalankan Program

1. Pastikan Python sudah terinstall (Python 3.x)
2. Save file program dengan nama daftar_nilai.py
3. Jalankan program dengan command:
   bash
   python daftar_nilai.py
   

## Fitur Program

1. *Tambah Data*: Menambahkan data mahasiswa baru (nama dan nilai)
2. *Tampilkan Data*: Menampilkan semua data mahasiswa dalam bentuk tabel
3. *Hapus Data*: Menghapus data mahasiswa berdasarkan nama
4. *Ubah Data*: Mengubah data mahasiswa (nama dan nilai) berdasarkan nama
5. *Keluar*: Keluar dari program

## Contoh Penggunaan


========================================
PROGRAM DAFTAR NILAI MAHASISWA
========================================
1. Tambah Data
2. Tampilkan Data
3. Hapus Data
4. Ubah Data
5. Keluar
========================================
Pilih menu (1-5): 1

=== Tambah Data Mahasiswa ===
Masukkan nama: Budi
Masukkan nilai: 85.5
Data Budi berhasil ditambahkan!


## Struktur Data

Data mahasiswa disimpan dalam bentuk list of dictionary:
python
[
    {'nama': 'Budi', 'nilai': 85.5},
    {'nama': 'Ani', 'nilai': 90.0},
    ...
]

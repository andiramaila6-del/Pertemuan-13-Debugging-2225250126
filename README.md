Pertemuan 13 - Debugging, Tracing, Testing, dan Test Case
Nama: Maila Andira Putri
NIM: 2225250126
Kelas: 3A
1. Tujuan
Praktik ini bertujuan menguji program secara sistematis, menemukan penyebab bug, memperbaiki kode, dan memastikan hasil perbaikan melalui pengujian ulang.
2. Kasus yang Diuji
Program mengolah data nilai mahasiswa dengan tiga fungsi:
hitung_rata_rata() untuk menghitung rata-rata.
status() untuk menentukan kelulusan.
nilai_tertinggi() untuk mencari nilai terbesar.
Program awal disimpan pada kasus/praktik_4_program_awal.py. Program yang sudah diperbaiki ada pada praktik/praktik_4_debugging.py.
3. Output Aktual Sebelum Perbaikan
Ketika program awal dijalankan dengan data [80, 60, 90, 70], hasilnya:
Rata-rata: 60.0
Status 60: Tidak lulus
Tertinggi: 0
Hasil tersebut tidak sesuai dengan hasil yang diharapkan.
4. Test Case
ID
Fungsi/Input
Expected
Actual Awal
Status Awal
T1
Rata-rata [80, 60, 90, 70]
75.0
60.0
FAIL
T2
Rata-rata [100, 80]
90.0
36.0
FAIL
T3
Status 60
Lulus
Tidak lulus
FAIL
T4
Status 59
Tidak lulus
Tidak lulus
PASS
T5
Tertinggi [80, 60, 90, 70]
90
0
FAIL
Test tambahan setelah perbaikan:
T6: rata-rata list kosong menghasilkan 0.
T7: nilai tertinggi list kosong menghasilkan None.
5. Bug Report
B01 - Kesalahan perhitungan rata-rata
Gejala: Hasil rata-rata tidak sesuai jumlah data.
Test case: T1 dan T2.
Lokasi: Fungsi hitung_rata_rata().
Akar penyebab: Program selalu membagi jumlah nilai dengan angka 5, padahal jumlah data dapat berbeda.
Perbaikan: Mengganti pembagi menjadi len(nilai) dan menambahkan pemeriksaan list kosong.
B02 - Kesalahan batas kelulusan
Gejala: Nilai 60 dinyatakan tidak lulus.
Test case: T3.
Lokasi: Fungsi status().
Akar penyebab: Operator > tidak memasukkan nilai yang sama dengan 60.
Perbaikan: Mengganti operator menjadi >=.
B03 - Kesalahan mencari nilai tertinggi
Gejala: Program menghasilkan 0, bukan 90.
Test case: T5.
Lokasi: Fungsi nilai_tertinggi().
Akar penyebab: Kondisi perbandingan menggunakan <, sehingga nilai yang lebih besar tidak pernah menggantikan nilai awal 0.
Perbaikan: Memulai nilai tertinggi dari elemen pertama dan menggunakan operator >.
6. Tabel Tracing Nilai Tertinggi
Input: [80, 60, 90, 70]
Langkah
x
Tertinggi sebelum
Tertinggi sesudah
1
60
80
80
2
90
80
90
3
70
90
90
Hasil akhir nilai tertinggi adalah 90.
7. Hasil Retest Setelah Perbaikan
ID
Expected
Actual
Status
T1
75.0
75.0
PASS
T2
90.0
90.0
PASS
T3
Lulus
Lulus
PASS
T4
Tidak lulus
Tidak lulus
PASS
T5
90
90
PASS
T6
0
0
PASS
T7
None
None
PASS
Seluruh test case berhasil setelah perbaikan dan tidak ditemukan regresi pada pengujian tersebut.
8. Cara Menjalankan
Jalankan melalui terminal dari folder utama proyek:
python3 praktik/praktik_4_debugging.py
Jika perintah python3 tidak tersedia, gunakan:
python praktik/praktik_4_debugging.py
9. Refleksi
Melalui praktik ini, saya belajar bahwa program yang dapat dijalankan belum tentu menghasilkan jawaban yang benar. Test case membantu menemukan kesalahan pada perhitungan, batas nilai, dan perbandingan data. Setelah memperbaiki kode, program harus diuji kembali agar kesalahan yang sama tidak muncul dan bagian lain tetap berjalan dengan baik.
10. Sumber dan Bantuan
Bahan Ajar Algoritma dan Pemrograman Pertemuan 13, Dr. Aan Hendrayana, S.Si., M.Pd.
Dokumentasi Python: https://docs.python.org/3/
Dokumentasi Visual Studio Code: https://code.visualstudio.com/docs/python/debugging
Penyusunan dan pengujian akhir dilakukan oleh mahasiswa. Penjelasan serta bantuan AI digunakan sebagai pendamping belajar.
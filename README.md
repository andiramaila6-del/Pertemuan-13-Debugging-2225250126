# Pertemuan 13 — Debugging, Tracing, Testing, dan Test Case

## Identitas Mahasiswa

* **Nama:** Maila Andira Putri
* **NIM:** 2225250126
* **Kelas:** 3A

## Deskripsi

Repository ini berisi hasil praktikum Algoritma dan Pemrograman Pertemuan 13 tentang *Debugging, Tracing, Testing,* dan *Test Case* menggunakan Python.

Praktikum ini membahas proses pengujian program secara sistematis untuk menemukan kesalahan (*bug*), mengetahui penyebab kesalahan, memperbaiki kode, serta melakukan pengujian ulang (*retest*) untuk memastikan program menghasilkan output sesuai dengan yang diharapkan.

## 1. Tujuan Praktikum

1. Menguji program menggunakan beberapa test case.
2. Menemukan kesalahan atau bug pada program.
3. Menelusuri alur eksekusi program menggunakan tracing.
4. Mengidentifikasi penyebab terjadinya kesalahan.
5. Memperbaiki kode program berdasarkan hasil pengujian.
6. Melakukan pengujian ulang setelah perbaikan.
7. Memastikan program menghasilkan output yang sesuai dengan hasil yang diharapkan.

## 2. Kasus yang Diuji

Program yang diuji merupakan program pengolahan data nilai mahasiswa dengan tiga fungsi utama, yaitu:

| Fungsi               | Keterangan                                |
| -------------------- | ----------------------------------------- |
| `hitung_rata_rata()` | Menghitung rata-rata nilai mahasiswa      |
| `status()`           | Menentukan status kelulusan mahasiswa     |
| `nilai_tertinggi()`  | Mencari nilai terbesar dari kumpulan data |

Program awal disimpan pada:

```text
kasus/praktik_4_program_awal.py
```

Sedangkan program yang telah diperbaiki disimpan pada:

```text
praktik/praktik_4_debugging.py
```

## 3. Output Aktual Sebelum Perbaikan

Program awal dijalankan menggunakan data berikut:

```python
nilai = [80, 60, 90, 70]
```

Output aktual sebelum perbaikan:

```text
Rata-rata: 60.0
Status 60: Tidak lulus
Tertinggi: 0
```

Hasil tersebut tidak sesuai dengan hasil yang diharapkan karena terdapat kesalahan pada perhitungan rata-rata, penentuan batas kelulusan, dan pencarian nilai tertinggi.

## 4. Test Case

Pengujian awal dilakukan untuk mengetahui kesalahan pada setiap fungsi program.

| ID | Fungsi/Input                 |    Expected | Actual Awal | Status Awal |
| -- | ---------------------------- | ----------: | ----------: | ----------- |
| T1 | Rata-rata `[80, 60, 90, 70]` |        75.0 |        60.0 | FAIL        |
| T2 | Rata-rata `[100, 80]`        |        90.0 |        36.0 | FAIL        |
| T3 | Status nilai 60              |       Lulus | Tidak lulus | FAIL        |
| T4 | Status nilai 59              | Tidak lulus | Tidak lulus | PASS        |
| T5 | Tertinggi `[80, 60, 90, 70]` |          90 |           0 | FAIL        |

### Test Tambahan Setelah Perbaikan

Selain lima pengujian awal, dilakukan dua pengujian tambahan untuk memastikan program dapat menangani list kosong.

| ID | Fungsi/Input                | Expected |
| -- | --------------------------- | -------- |
| T6 | Rata-rata list kosong       | 0        |
| T7 | Nilai tertinggi list kosong | None     |

## 5. Bug Report

Berdasarkan hasil pengujian awal, ditemukan tiga kesalahan utama pada program.

### B01 — Kesalahan Perhitungan Rata-rata

* **Gejala:** Hasil rata-rata tidak sesuai dengan jumlah data.
* **Test case:** T1 dan T2.
* **Lokasi:** Fungsi `hitung_rata_rata()`.
* **Akar penyebab:** Program selalu membagi jumlah nilai dengan angka 5, padahal jumlah data dapat berbeda.
* **Perbaikan:** Mengganti pembagi menjadi `len(nilai)` dan menambahkan pemeriksaan list kosong.

### B02 — Kesalahan Batas Kelulusan

* **Gejala:** Nilai 60 dinyatakan tidak lulus.
* **Test case:** T3.
* **Lokasi:** Fungsi `status()`.
* **Akar penyebab:** Penggunaan operator `>` tidak memasukkan nilai yang sama dengan 60 sebagai nilai lulus.
* **Perbaikan:** Mengganti operator `>` menjadi `>=`.

### B03 — Kesalahan Mencari Nilai Tertinggi

* **Gejala:** Program menghasilkan nilai 0, bukan 90.
* **Test case:** T5.
* **Lokasi:** Fungsi `nilai_tertinggi()`.
* **Akar penyebab:** Kondisi perbandingan menggunakan operator `<`, sehingga nilai yang lebih besar tidak menggantikan nilai awal 0.
* **Perbaikan:** Memulai nilai tertinggi dari elemen pertama dan menggunakan operator `>`.

## 6. Tabel Tracing Nilai Tertinggi

Tracing dilakukan untuk mengetahui proses perubahan nilai tertinggi ketika program memeriksa setiap elemen dalam list.

**Input:**

```python
nilai = [80, 60, 90, 70]
```

Hasil tracing:

| Langkah |  x | Tertinggi Sebelum | Tertinggi Sesudah |
| ------: | -: | ----------------: | ----------------: |
|       1 | 60 |                80 |                80 |
|       2 | 90 |                80 |                90 |
|       3 | 70 |                90 |                90 |

Berdasarkan proses tracing tersebut, nilai tertinggi yang diperoleh adalah:

```text
Nilai tertinggi: 90
```

## 7. Hasil Retest Setelah Perbaikan

Setelah seluruh bug diperbaiki, dilakukan pengujian ulang untuk memastikan setiap fungsi menghasilkan output yang benar.

| ID |    Expected |      Actual | Status |
| -- | ----------: | ----------: | ------ |
| T1 |        75.0 |        75.0 | PASS   |
| T2 |        90.0 |        90.0 | PASS   |
| T3 |       Lulus |       Lulus | PASS   |
| T4 | Tidak lulus | Tidak lulus | PASS   |
| T5 |          90 |          90 | PASS   |
| T6 |           0 |           0 | PASS   |
| T7 |        None |        None | PASS   |

Seluruh test case berhasil setelah perbaikan dan tidak ditemukan regresi pada pengujian tersebut.

## 8. Cara Menjalankan Program

Pastikan Python telah terpasang dan folder proyek sudah dibuka melalui Visual Studio Code (VS Code).

Jalankan program melalui terminal dari folder utama proyek menggunakan perintah:

```bash
python3 praktik/praktik_4_debugging.py
```

Jika perintah `python3` tidak tersedia, gunakan:

```bash
python praktik/praktik_4_debugging.py
```

Pada Windows, perintah berikut juga dapat digunakan:

```bash
py praktik/praktik_4_debugging.py
```

## 9. Refleksi

Melalui praktik ini, saya belajar bahwa program yang dapat dijalankan belum tentu menghasilkan jawaban yang benar. Test case membantu menemukan kesalahan pada perhitungan, batas nilai, dan perbandingan data. Saya juga memahami bahwa tracing dapat digunakan untuk menelusuri perubahan nilai variabel selama program dijalankan.

Setelah memperbaiki kode, program harus diuji kembali agar kesalahan yang sama tidak muncul dan bagian lain tetap berjalan dengan baik. Dengan demikian, proses debugging, tracing, dan testing sangat penting untuk memastikan program menghasilkan output sesuai dengan yang diharapkan.

## 10. Sumber dan Bantuan

1. Bahan Ajar Algoritma dan Pemrograman Pertemuan 13, Dr. Aan Hendrayana, S.Si., M.Pd.
2. Dokumentasi resmi Python: https://docs.python.org/3/
3. Dokumentasi Visual Studio Code: https://code.visualstudio.com/docs/python/debugging

Penyusunan dan pengujian akhir dilakukan oleh mahasiswa. Penjelasan serta bantuan AI digunakan sebagai pendamping belajar.

## Pengumpulan melalui GitHub

Seluruh file praktikum disusun dalam repository GitHub sesuai dengan struktur folder yang telah ditentukan. File `README.md` digunakan untuk menjelaskan kasus yang diuji, hasil pengujian, bug report, proses tracing, hasil retest, serta refleksi praktikum.

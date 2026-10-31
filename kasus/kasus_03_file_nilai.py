# Contoh kasus tambahan: membaca file nilai dengan penanganan error.
# Buat file nilai.txt di folder yang sama jika ingin menguji bagian berhasil.

def baca_nilai(nama_file):
    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            for nomor, baris in enumerate(file, start=1):
                teks = baris.strip()
                if not teks:
                    continue
                try:
                    nilai = float(teks)
                    print(f"Baris {nomor}: {nilai}")
                except ValueError:
                    print(f"Baris {nomor} tidak valid: {teks}")
    except FileNotFoundError:
        print(f"File tidak ditemukan: {nama_file}")


if __name__ == "__main__":
    baca_nilai("nilai.txt")
# Praktik 4: versi yang sudah diperbaiki

def hitung_rata_rata(nilai):
    if len(nilai) == 0:
        return 0
    return sum(nilai) / len(nilai)


def status(nilai):
    if nilai >= 60:
        return "Lulus"
    return "Tidak lulus"


def nilai_tertinggi(nilai):
    if len(nilai) == 0:
        return None

    tertinggi = nilai[0]
    for x in nilai[1:]:
        if x > tertinggi:
            tertinggi = x
    return tertinggi


def jalankan_test():
    test_case = [
        ("T1 rata-rata 4 data", lambda: hitung_rata_rata([80, 60, 90, 70]), 75.0),
        ("T2 rata-rata 2 data", lambda: hitung_rata_rata([100, 80]), 90.0),
        ("T3 status nilai 60", lambda: status(60), "Lulus"),
        ("T4 status nilai 59", lambda: status(59), "Tidak lulus"),
        ("T5 nilai tertinggi", lambda: nilai_tertinggi([80, 60, 90, 70]), 90),
        ("T6 rata-rata list kosong", lambda: hitung_rata_rata([]), 0),
        ("T7 nilai tertinggi list kosong", lambda: nilai_tertinggi([]), None),
    ]

    semua_lulus = True
    for nama, fungsi, expected in test_case:
        actual = fungsi()
        lulus = actual == expected
        if not lulus:
            semua_lulus = False
        print(f"{nama}: expected={expected}, actual={actual}, "
              f"{'PASS' if lulus else 'FAIL'}")

    return semua_lulus


if __name__ == "__main__":
    nilai = [80, 60, 90, 70]
    print("Rata-rata:", hitung_rata_rata(nilai))
    print("Status 60:", status(60))
    print("Tertinggi:", nilai_tertinggi(nilai))
    print("\nHasil pengujian:")
    jalankan_test()
# Latihan 3: test case batas kelulusan
def status_lulus(nilai):
    if nilai >= 60:
        return "Lulus"
    return "Tidak lulus"


test_case = [
    (59, "Tidak lulus"),
    (60, "Lulus"),
    (61, "Lulus"),
]

for nomor, (input_nilai, expected) in enumerate(test_case, start=1):
    actual = status_lulus(input_nilai)
    status_test = "PASS" if actual == expected else "FAIL"
    print(f"T{nomor}: input={input_nilai}, expected={expected}, "
          f"actual={actual}, {status_test}")
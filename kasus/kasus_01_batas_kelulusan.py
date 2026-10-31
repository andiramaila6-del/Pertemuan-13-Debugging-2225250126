# Kasus 1: Bug batas kelulusan
def status_lulus(nilai):
    if nilai > 60:  # Bug: nilai 60 seharusnya termasuk lulus
        return "Lulus"
    return "Tidak lulus"


for nilai in [59, 60, 61]:
    print(nilai, "->", status_lulus(nilai))
# Kasus 2: Bug rata-rata
def rata_rata(data):
    total = sum(data)
    return total / 5  # Bug: pembagi harus sesuai jumlah data


print(rata_rata([80, 90, 70]))
print(rata_rata([100, 80]))
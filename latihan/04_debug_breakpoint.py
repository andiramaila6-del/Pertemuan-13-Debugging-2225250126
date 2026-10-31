# Latihan 4: pasang breakpoint pada baris total dan return.
def hitung_diskon(total, persen):
    diskon = total * persen / 100
    hasil = total - diskon
    return hasil


harga_awal = 200000
persen_diskon = 10
hasil_akhir = hitung_diskon(harga_awal, persen_diskon)
print("Harga setelah diskon:", hasil_akhir)
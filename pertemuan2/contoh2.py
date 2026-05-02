# Data tuple (tidak boleh diubah)
data_nilai = (70, 85, 70, 90, 85, 90, 75, 70, 80)

# 1. Nilai unik
nilai_unik = set(data_nilai)

# 2. Hitung frekuensi
frekuensi = {}

for nilai in data_nilai:
    if nilai in frekuensi:
        frekuensi[nilai] += 1
    else:
        frekuensi[nilai] = 1

# 3. Cari frekuensi tertinggi
maks = max(frekuensi.values())

# 4. Cari nilai dengan frekuensi tertinggi
tertinggi = [nilai for nilai, jumlah in frekuensi.items() if jumlah == maks]

# 5. Output
print("Nilai unik:", nilai_unik)
print("Frekuensi:", frekuensi)
print("Nilai paling sering muncul:", tertinggi)
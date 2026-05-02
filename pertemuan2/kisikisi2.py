data_nilai = (65, 70, 75, 70, 80, 85, 75, 90, 80, 85, 90)

data = set(data_nilai)

frekuensi ={}

for i in data_nilai:
    if i in frekuensi:
        frekuensi[i] += 1
    else:
        frekuensi[i] = 1

maks = max(frekuensi.values())

tertinggi = [x for x, nilai in frekuensi.items() if nilai == maks]

print("Nilai unik: ", data)
print("Frekuensi: ", frekuensi)
print("Nilai paling banyak muncul: ", tertinggi)

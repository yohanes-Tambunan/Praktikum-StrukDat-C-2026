data_nilai = (80, 75, 90, 80, 85, 90, 70, 75, 85, 90)

hasil = set(data_nilai)

frekuensi = {}
for i in hasil:
    if i in frekuensi:
        frekuensi[i] +=1
    else:
        frekuensi[i] = 1

maks = max(frekuensi.values())

tertinggi = [x for x, nilai in frekuensi.items() if nilai == maks]

print ("nilai unik: ", hasil)
print("frekuensi: ", frekuensi)
print("nilai paling banyak muncul: ", tertinggi)
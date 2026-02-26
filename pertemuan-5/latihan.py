#soal 1
stok_barang = [15, 40, 30, 10, 25]
print(stok_barang[3])
stok_barang.append(5)
print(stok_barang)
stok_barang.sort(reverse = True)
print(stok_barang)
total = sum(stok_barang)
print("Total stok:", total)
rata_rata = sum(stok_barang) / len(stok_barang)
status = "Stok Aman" if rata_rata > 20 else "Waspada"
print("Rata-rata:", rata_rata)
print(status)




#soal 2
data_aktivitas = [("Diki", 88), ("Aqul", 45), ("Abid", 92), ("Rehan", 70)]
for nama, poin in data_aktivitas:
    if poin > 80:
        print(f"{nama} mendapatkan predikat Gold")
    elif 50 <= poin <= 80:
        print(f"{nama} mendapatkan predikat Silver")
    else:
        print(f"{nama} mendapatkan predikat Bronze")

#soal 3
ukm_coding = {"Andi", "Budi", "Caca", "Deni"}
ukm_robotik = {"Caca", "Deni", "Euis", "Fafa"}
hanya_coding= ukm_coding - ukm_robotik
print(hanya_coding)
semua_mahasiswa = ukm_coding | ukm_robotik
print(semua_mahasiswa)
cek_andi = "Andi" in ukm_robotik
print(cek_andi)

#soal 4
gudang_pc = [
{"item": "Monitor", "harga": 1500000, "stok": 5},
{"item": "Keyboard", "harga": 400000, "stok": 12},
{"item": "Mouse", "harga": 250000, "stok": 20}
]
gudang_pc[1]["Kategori"]= "Aksesoris"
print(gudang_pc[1])

gudang_pc.append({"item": "Headset", "harga": 35.000, "stok": 8})
print(gudang_pc[3])

for x in range(len(gudang_pc)):
    print(f'item: {gudang_pc[x]["item"]}total ={gudang_pc[x]["harga"]*gudang_pc[x]["stok"]}')
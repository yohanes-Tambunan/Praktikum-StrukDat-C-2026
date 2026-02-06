#jawaban 1
stock = [15, 50, 30, 25, 40]
stock.append(100)
print(stock)
stock.insert(2, 75)
print(stock)
stock.sort (reverse = True)
print(stock)
rata = 0
for x in stock:
    rata += x
rata_rata = rata / len(stock)
print(stock)
print(rata_rata)


#jawaban 2
barang = ("B001", "Laptop Gaming", 15000000)
print (barang[2])

harga_baru = list(barang)
harga_baru[2] = 14000000
x = tuple(harga_baru)
print(barang)


#jawaban 3
tim_frontend = {"HTML", "CSS", "JavaScript", "React"}
tim_backend = {"Python", "JavaScript", "SQL",
"NodeJS"}

tim_baru = tim_frontend.intersection(tim_backend)
print(tim_baru)

for x in tim_backend:
    print(x)

tim_gabungan = tim_frontend.union(tim_backend)
print(tim_gabungan)

#jawaban 4
nilai_siswa = {
"S01": {"nama": "Dina", "tugas": 80, "uts": 75,
"uas": 85},
"S02": {"nama": "Abdul Harris", "tugas": 90, "uts":
88, "uas": 92},
"S03": {"nama": "Sheila", "tugas": 70, "uts": 65,
"uas": 70}
} 

nilai_siswa["S04"] = {"nama": "Fafa", "tugas": 70, "uts": 80, "uas": 90}
print(nilai_siswa)

print("Nilai akhir setiap siswa: ")
for kode, data in nilai_siswa.items():
    nilai_data=(
        0.2* data["tugas"]+
        0.3* data["uts"]+
        0.5* data ["uas"]
    )
    print(f"{data['nama']} : {nilai_data}")

print("\nSiswa dengan nilai UAS di atas 80:")
for data in nilai_siswa.values():
    if data["uas"]>80:
        print(data["nama"])
        
    






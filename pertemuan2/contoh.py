# Data mahasiswa (list berisi dictionary)
data_mahasiswa = [
    {"nama": "Andi", "jurusan": "Informatika"},
    {"nama": "Budi", "jurusan": "Sistem Informasi"},
    {"nama": "Caca", "jurusan": "Informatika"},
    {"nama": "Deni", "jurusan": "Teknik Elektro"},
    {"nama": "Eka", "jurusan": "Informatika"}
]

# 1. Filter data (hanya Informatika)
hasil_filter = [mhs for mhs in data_mahasiswa if mhs["jurusan"] == "Informatika"]

# 2. Sorting berdasarkan nama
hasil_filter.sort(key=lambda x: x["nama"])

# 3. Tampilkan tabel
print("=== Data Mahasiswa Informatika ===")
print("No | Nama")
print("----------------")

for i in range(len(hasil_filter)):
    print(i+1, "|", hasil_filter[i]["nama"])

# 4. Rekap jumlah
print("----------------")
print("Jumlah mahasiswa:", len(hasil_filter))


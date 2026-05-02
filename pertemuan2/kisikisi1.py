data_karyawan = [
    {"nama": "Andi", "divisi": "IT", "gaji": 5000000},
    {"nama": "Budi", "divisi": "HRD", "gaji": 4500000},
    {"nama": "Caca", "divisi": "IT", "gaji": 5500000},
    {"nama": "Deni", "divisi": "Keuangan", "gaji": 6000000},
    {"nama": "Eka", "divisi": "IT", "gaji": 5200000}
]

data = [buku for buku in data_karyawan if buku ["divisi"]=="IT"]

data.sort(key = lambda x:x ["nama"])

print("===Data Karyawan===")
print("NO |   NAMA   | GAJI")
print("--------------------")

total_gaji = 0

for i in range(len(data)):
    print (i+1, "|", data[i]["nama"], "|", data[i]["gaji"])
    total_gaji += data[i]["gaji"]

print("--------------------")
print("Total karyawan: ", len(data))
print("Total gaji: ", total_gaji)
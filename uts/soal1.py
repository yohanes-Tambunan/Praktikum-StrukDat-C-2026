pengunjung_hari_ini = [
 {"id": "M001", "nama": "Rina", "usia": 20, "kategori": "Fiksi", 
"kembali": False},
 {"id": "M002", "nama": "Hendra", "usia": 23, "kategori": "Sains", 
"kembali": True},
 {"id": "M003", "nama": "Siti", "usia": 19, "kategori": "Fiksi", 
"kembali": False},
 {"id": "M004", "nama": "Taufik", "usia": 21, "kategori": "Hukum", 
"kembali": True},
 {"id": "M005", "nama": "Yuni", "usia": 18, "kategori": "Sains", 
"kembali": False},
 {"id": "M006", "nama": "Bagas", "usia": 22, "kategori": "Hukum", 
"kembali": False},
]

def tampilkan_pengunjung():
    print("===== DATA PENGUNJUNG PERPUSTAKAAN =====")
    print("No | ID   | Nama   | Usia | Kategori | Status")
    print("---------------------------------------------")
    
    for i, p in enumerate(pengunjung_hari_ini, 1):
        status = "Sudah Kembali" if p["kembali"] else "Belum Kembali"
        print(f"{i}  | {p['id']} | {p['nama']} | {p['usia']}  | {p['kategori']} | {status}")

def filter_belum_kembali():
    belum = [p["nama"] for p in pengunjung_hari_ini if not p["kembali"]]
    belum.sort()  
    print("\n===== PENGUNJUNG BELUM KEMBALI =====")
    for i, nama in enumerate(belum, 1):
        print(f"{i}. {nama}")
    print(f"Total belum kembali: {len(belum)} pengunjung")


tampilkan_pengunjung()
filter_belum_kembali()
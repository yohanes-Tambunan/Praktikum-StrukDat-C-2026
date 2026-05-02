def info_perpustakaan():
    info = (
        "Perpustakaan Kampus Terpadu",
        "Jl. Pendidikan No. 5, Pekanbaru",
        "0761-54321"
    )
    
    print("Info Perpustakaan:")
    print("Nama   :", info[0])
    print("Alamat :", info[1])
    print("Telp   :", info[2])

def rekap_kategori():
    buku = ("fiksi", "sains", "hukum")
    data = set(buku)
    print("Nilai unik: ", data)
    print("jumlah kategori", len(data))

    buku = {"fiksi": 2 ,
            "sains": 2 ,
            "hukum": 2
            }
    maks = max(buku.values())
    tertinggi = [x for x, data in buku.items() if data == maks]
    print(buku)
    
    print("Kategori terbanya:", tertinggi)

info_perpustakaan()
rekap_kategori()

    
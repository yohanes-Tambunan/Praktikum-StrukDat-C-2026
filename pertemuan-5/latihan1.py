pengunjung_hari_ini = [
    {"id": "M001", "nama": "Rina", "usia": 20, "kategori": "Fiksi", "kembali": False},
    {"id": "M002", "nama": "Hendra", "usia": 23, "kategori": "Sains", "kembali": True},
    {"id": "M003", "nama": "Siti", "usia": 19, "kategori": "Fiksi", "kembali": False},
    {"id": "M004", "nama": "Taufik", "usia": 21, "kategori": "Hukum", "kembali": True},
    {"id": "M005", "nama": "Yuni", "usia": 18, "kategori": "Sains", "kembali": False},
    {"id": "M006", "nama": "Bagas", "usia": 22, "kategori": "Hukum", "kembali": False},
]

def tampilkan_pengunjung():
    print("===== DATA PENGUNJUNG PERPUSTAKAAN =====")
    print("No | ID   | Nama   | Usia | Kategori | Status")
    print("---------------------------------------------")
    
    for i, p in enumerate(pengunjung_hari_ini, 1):
        status = "Sudah Kembali" if p["kembali"] else "Belum Kembali"
        print(f"{i}  | {p['id']} | {p['nama']} | {p['usia']}  | {p['kategori']} | {status}")

def filter_belum_kembali():
    # list comprehension
    belum = [p["nama"] for p in pengunjung_hari_ini if not p["kembali"]]
    
    belum.sort()  # urut A-Z
    
    print("\n===== PENGUNJUNG BELUM KEMBALI =====")
    for i, nama in enumerate(belum, 1):
        print(f"{i}. {nama}")
    
    print(f"Total belum kembali: {len(belum)} pengunjung")

# jalankan
tampilkan_pengunjung()
filter_belum_kembali()



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
    kategori_unik = set(p["kategori"] for p in pengunjung_hari_ini)
    
    print("\nKategori Buku Unik:", kategori_unik)
    print("Jumlah kategori:", len(kategori_unik))
    
    # hitung per kategori
    rekap = {}
    for p in pengunjung_hari_ini:
        k = p["kategori"]
        rekap[k] = rekap.get(k, 0) + 1
    
    print("\nRekap per kategori:")
    for k, v in rekap.items():
        print(f"{k} : {v} pengunjung")
    
    # cari terbanyak
    max_val = max(rekap.values())
    terbanyak = [k for k, v in rekap.items() if v == max_val]
    
    print(f"\nKategori terbanyak: {', '.join(terbanyak)} ({max_val} pengunjung)")

# jalankan
info_perpustakaan()
rekap_kategori()




class Pengunjung:
    total = 0  # class variable

    def __init__(self, id, nama, kategori):
        self.__id = id
        self.__nama = nama
        self.__kategori = kategori
        Pengunjung.total += 1

    # getter
    def get_id(self):
        return self.__id

    def get_nama(self):
        return self.__nama

    def get_kategori(self):
        return self.__kategori

    def tampilkan_info(self):
        print("ID :", self.__id)
        print("Nama :", self.__nama)
        print("Kategori :", self.__kategori)

    @staticmethod
    def hitung_pengunjung():
        return Pengunjung.total


class PengunjungPrioritas(Pengunjung):
    def __init__(self, id, nama, kategori, prioritas):
        super().__init__(id, nama, kategori)
        self.prioritas = prioritas

    def tampilkan_info(self):
        super().tampilkan_info()
        print("Prioritas :", self.prioritas)
        if self.prioritas == "Mendesak":
            print("** Layani segera! **")


# contoh penggunaan
p1 = Pengunjung("M001", "Rina", "Fiksi")
p2 = PengunjungPrioritas("M007", "Gilang", "Referensi", "Mendesak")

p1.tampilkan_info()
print()
p2.tampilkan_info()

print("\nTotal pengunjung terdaftar:", Pengunjung.hitung_pengunjung())






class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class AntrianPeminjaman:
    def __init__(self):
        self.head = None

    def tambah(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node

    def tampilkan(self):
        print("\n===== ANTRIAN PEMINJAMAN =====")
        current = self.head
        i = 1
        while current:
            d = current.data
            print(f"[{i}] {d['id']} - {d['nama']} | {d['kategori']}")
            current = current.next
            i += 1
        print("Total antrian:", self.hitung())

    def panggil_berikutnya(self):
        if not self.head:
            print("Antrian kosong")
            return
        data = self.head.data
        self.head = self.head.next
        print(f"Silakan masuk: {data['nama']} ({data['id']}) - {data['kategori']}")

    def cari(self, nama):
        current = self.head
        posisi = 1
        while current:
            if current.data["nama"] == nama:
                d = current.data
                print(f"Ditemukan: {d['id']} - {d['nama']} | {d['kategori']} (posisi ke-{posisi})")
                return
            current = current.next
            posisi += 1
        print("Tidak ditemukan")

    def hapus_berdasarkan_id(self, id):
        current = self.head
        prev = None

        while current:
            if current.data["id"] == id:
                if prev is None:
                    self.head = current.next  # hapus head
                else:
                    prev.next = current.next

                print(f"{current.data['nama']} ({id}) berhasil dihapus dari antrian.")
                return
            
            prev = current
            current = current.next

        print("ID tidak ditemukan")

    def hitung(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count


# contoh penggunaan
antrian = AntrianPeminjaman()
antrian.tambah({"id": "M001", "nama": "Rina", "kategori": "Fiksi"})
antrian.tambah({"id": "M002", "nama": "Hendra", "kategori": "Sains"})
antrian.tambah({"id": "M003", "nama": "Siti", "kategori": "Fiksi"})
antrian.tambah({"id": "M004", "nama": "Taufik", "kategori": "Hukum"})

antrian.tampilkan()
antrian.panggil_berikutnya()
antrian.tampilkan()
antrian.hapus_berdasarkan_id("M003")
antrian.tampilkan()
antrian.cari("Taufik")
print("Total antrian:", antrian.hitung())













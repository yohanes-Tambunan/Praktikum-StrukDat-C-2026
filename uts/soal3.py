class Pengunjung:
    total = 0 

    def __init__(self, id, nama, kategori):
        self.__id = id
        self.__nama = nama
        self.__kategori = kategori
        Pengunjung.total += 1

    
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


p1 = Pengunjung("M001", "Rina", "Fiksi")
p2 = PengunjungPrioritas("M007", "Gilang", "Referensi", "Mendesak")

p1.tampilkan_info()
print()
p2.tampilkan_info()

print("\nTotal pengunjung terdaftar:", Pengunjung.hitung_pengunjung())

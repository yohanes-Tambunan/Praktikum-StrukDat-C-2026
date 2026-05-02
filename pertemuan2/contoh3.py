class Produk:
    jumlah_produk = 0  # class variable

    def __init__(self, nama, harga):
        self.__nama = nama          # private
        self.__harga = harga        # private
        Produk.jumlah_produk += 1   # tambah jumlah

    # Getter
    def get_nama(self):
        return self.__nama

    def get_harga(self):
        return self.__harga

    # Method tampilkan info
    def info(self):
        print("Nama:", self.__nama)
        print("Harga:", self.__harga)

    # Static method
    @staticmethod
    def total_produk():
        print("Total produk:", Produk.jumlah_produk)


# Inheritance
class Elektronik(Produk):
    def __init__(self, nama, harga, garansi):
        super().__init__(nama, harga)
        self.garansi = garansi

    # Override method
    def info(self):
        print("Nama:", self.get_nama())
        print("Harga:", self.get_harga())
        print("Garansi:", self.garansi, "bulan")


# Membuat objek
p1 = Elektronik("Laptop", 10000000, 24)
p2 = Elektronik("HP", 5000000, 12)

# Menampilkan info
p1.info()
print("----------------")
p2.info()

print("----------------")
Produk.total_produk()
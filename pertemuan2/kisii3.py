class Kendaraan:
    jumlah_kendaraan = 0

    def __init__ (self, merk, kecepatan):
        self.__merk = merk
        self.__kecepatam = kecepatan
        Kendaraan.jumlah_kendaraan+=1

    def get_merk(self):
        return self.__merk
    
    def get_kecepatan(self):
        return self.__kecepatam

    def info(self):
        print("merk: ", self.__merk)
        print("kecepatan: ", self.__kecepatan)
    
    @staticmethod
    def total_produk():
        print("Jumlah kendaraan: ", Kendaraan.jumlah_kendaraan)

class Mobil(Kendaraan):
    def __init__(self, merk, kecepatan, jenis_bahan_bakar):
        super().__init__ (merk, kecepatan)
        self.jenis_bahan_bakar = jenis_bahan_bakar

    def info(self):
        print("merk: ", self.get_merk(), "km/jam")
        print("kecepatan: ", self.get_kecepatan())
        print("Jenis bahan bakar: ", self.jenis_bahan_bakar)

p1 = Mobil("Ferari", 150 , "Pertamax Ron 100")
p2 = Mobil ("Avanza", 120, "Pertalite")

p1.info()
print("-----------")
p2.info()

print("-----------")
Kendaraan.total_produk()



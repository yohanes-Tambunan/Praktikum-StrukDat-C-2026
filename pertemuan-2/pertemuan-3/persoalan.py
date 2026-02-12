class RumahKu:
    def __init__(self, nama, kecantikan, alamat):
        self.nama= nama
        self.kecantikan = kecantikan
        self.alamat= alamat

    def introduce_self(self):
        print(f"rumahku memiliki sebutan yaitu{self.name}", "kecantikan rumah ku sanga{self.kecantikan}", "alamat rumahku{self.alamat}")

    def alamat_baru(self,alamat_baru):
        self.alamat= alamat_baru
        print(f"saya pindah rumah ke {alamat_baru}")

rumah_satu = RumahKu("rumah kristen", "bagus", "jalan daru daru")
rumah_dua = RumahKu("suci", "keren", "jalan pinang merah")   
rumah_tiga = RumahKu ("anak keren", "rapi", "jalan nangka")   
    
print(rumah_satu.nama)
print(rumah_satu.kecantikan)
print(rumah_satu.alamat)
rumah_satu.alamat_baru("jalan keling")
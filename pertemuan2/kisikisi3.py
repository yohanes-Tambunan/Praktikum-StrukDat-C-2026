class Pegawai:
    jumlah_pegawai = 0
    def __init__ (self, nama, gaji):
        self.__nama = nama
        self.__gaji = gaji
        Pegawai.jumlah_pegawai +=1

    def get_nama (self):
        return self.__nama

    def get_gaji (self):
        return self.__gaji
    
     
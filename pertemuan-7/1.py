plat = ["B 1234 ABC", "D 8888 XYZ", "A 111 TUV", "B 2022 EFG"]

def mencari_ganjil_genap(plat_list):
    ganjil =[]
    genap = []

    for plat in plat_list:
        bagian = plat.split()
        angka = bagian [1]
        terakhir = int(angka[-1])
        if terakhir % 2 == 0:
            genap.append(plat)
        else:
            ganjil.append(plat)
    return ganjil, genap

data = ["B 1234 ABC", "D 8888 XYZ", "A 111 TUV", "B 2022 EFG"]

ganjil, genap = mencari_ganjil_genap(data)

print("Ganjil:", ganjil)
print("Genap:", genap)



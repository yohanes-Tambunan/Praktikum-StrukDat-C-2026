def registrasi_gadget(merk, tipe, harga, sn):
    
    if harga <= 1000000:
        print("Error: Harga harus di atas 1.000.000")
        return None
    if len(sn) < 5:
        print("Error: Serial Number harus minimal 5 karakter")
        return None
    gadget = {
        "merk": merk,
        "tipe": tipe,
        "harga": harga,
        "sn": sn,
        "status": "Tersedia"
    }

    return gadget
inventaris = []

for i in range(3):
    print(f"\nInput Gadget ke-{i+1}")

    merk = input("Merk: ")
    tipe = input("Tipe: ")
    harga = float(input("Harga: "))
    sn = input("Serial Number: ")

    data = registrasi_gadget(merk, tipe, harga, sn)

    if data != None:
        inventaris.append(data)

for item in inventaris:
    print(item)
    

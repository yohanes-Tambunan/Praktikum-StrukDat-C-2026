stok_gadget = [ 
 {'merk': 'Samsung', 'tipe': 'S23', 'harga': 12000000},  
 {'merk': 'Oppo', 'tipe': 'Reno 10', 'harga': 6000000},  
 {'merk': 'Xiaomi', 'tipe': 'Mi 13', 'harga': 10000000},  
 {'merk': 'Iphone', 'tipe': '15 Pro', 'harga': 20000000}, ] 

def filter_harga(data, min_harga, max_harga):
    hasil = []

    for gadget in data:
        if min_harga <= gadget['harga'] <= max_harga:
            hasil.append(gadget)

    return hasil


min_harga = int(input("Input batas bawah: "))
max_harga = int(input("Input batas atas: "))

hasil_filter = filter_harga(stok_gadget, min_harga, max_harga)

if len(hasil_filter) == 0:
    print("Tidak ada gadget dalam rentang harga tersebut.")
else:
    print("\nGadget yang ditemukan:")
    for item in hasil_filter:
        print(item)
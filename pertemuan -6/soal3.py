katalog = [
{'merk': 'Samsung', 'tipe': 'S23', 'sn': 'SAM01', 'stok': 2},
{'merk': 'Oppo', 'tipe': 'Reno 10', 'sn': 'OPP01', 'stok': 5}
]
daftar_merk = set()
def update_stok(katalog, sn_target, jumlah_tambah):
    ditemukan = False

    for gadget in katalog:
        if gadget['sn'] == sn_target:
            if 'stok' in gadget:
                gadget['stok'] += jumlah_tambah
            else:
                gadget['stok'] = jumlah_tambah

            ditemukan = True
            print("Stok berhasil diperbarui")
            break

    if not ditemukan:
        print("SN tidak ditemukan")

    for g in katalog:
        daftar_merk.add(g['merk'])

for i in range(3):
    print(f"\nUpdate stok ke-{i+1}")
    sn = input("Masukkan SN: ")
    jumlah = int(input("Jumlah tambah stok: "))

    update_stok(katalog, sn, jumlah)

print("\nDaftar merk unik:")
print(daftar_merk)
from tabulate import tabulate
from kurs import kurs
from konverter import idr_ke_mata_uang, mata_uang_ke_idr

def tampilkan_kurs():
    data = []
    for kode, nilai in kurs.items():
        data.append([kode, nilai])

    print(tabulate(data, headers=["Mata Uang", "Kurs ke IDR"], tablefmt="grid"))

def main():
    
    print("\n1. IDR ke Mata Uang Lain")
    print("2. Mata Uang Lain ke IDR")

    pilihan = input("Pilih menu (1/2): ")

    if pilihan == "1":
        jumlah = float(input("Masukkan jumlah IDR: "))
        mata_uang = input("Masukkan kode mata uang (USD/EUR/SGD/JPY): ").upper()

        hasil = idr_ke_mata_uang(jumlah, mata_uang)

        if hasil is not None:
            print(f"Hasil konversi: {hasil:.2f} {mata_uang}")
        else:
            print("Kode mata uang tidak ditemukan!")

    elif pilihan == "2":
        jumlah = float(input("Masukkan jumlah: "))
        mata_uang = input("Masukkan kode mata uang (USD/EUR/SGD/JPY): ").upper()

        hasil = mata_uang_ke_idr(jumlah, mata_uang)

        if hasil is not None:
            print(f"Hasil konversi: Rp {hasil:,.2f}")
        else:
            print("Kode mata uang tidak ditemukan!")

    else:
        print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()
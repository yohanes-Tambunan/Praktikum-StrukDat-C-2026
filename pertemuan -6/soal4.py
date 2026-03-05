skema_komisi = (
(100000000, 10),
(50000000, 5),
(20000000, 2),
(0, 0)
)

def hitung_komisi(total_penjualan, skema, index=0):
    target, persen = skema[index]

    if total_penjualan >= target:
        return persen
    else:
        return hitung_komisi(total_penjualan, skema, index + 1)


nama = input("Nama Sales: ")
total = int(input("Total Penjualan: "))

persen = hitung_komisi(total, skema_komisi)
komisi = total * persen / 100

print("\n=== Rincian Komisi ===")
print("Nama Sales:", nama)
print("Total Penjualan:", total)
print("Persen Komisi:", persen, "%")
print("Nominal Komisi:", komisi)
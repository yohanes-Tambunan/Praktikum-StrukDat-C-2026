# Node
class Node:
    def __init__(self, nama):
        self.nama = nama
        self.next = None


# Linked List (Antrian)
class Antrian:
    def __init__(self):
        self.head = None

    # Enqueue (tambah ke belakang)
    def tambah(self, nama):
        node_baru = Node(nama)

        if self.head is None:
            self.head = node_baru
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node_baru

    # Dequeue (hapus dari depan)
    def hapus_depan(self):
        if self.head is None:
            print("Antrian kosong")
        else:
            print("Melayani:", self.head.nama)
            self.head = self.head.next

    # Tampilkan
    def tampil(self):
        if self.head is None:
            print("Antrian kosong")
        else:
            current = self.head
            while current:
                print(current.nama, end=" -> ")
                current = current.next
            print("None")

    # Cari berdasarkan nama
    def cari(self, nama):
        current = self.head
        while current:
            if current.nama == nama:
                print("Ditemukan:", nama)
                return
            current = current.next
        print("Tidak ditemukan")

    # Hapus berdasarkan nama
    def hapus_nama(self, nama):
        current = self.head
        prev = None

        while current:
            if current.nama == nama:
                if prev is None:  # di head
                    self.head = current.next
                else:  # di tengah / akhir
                    prev.next = current.next
                print("Data", nama, "dihapus")
                return
            prev = current
            current = current.next

        print("Data tidak ditemukan")


# ==========================
# Testing program
# ==========================
antrian = Antrian()

antrian.tambah("Andi")
antrian.tambah("Budi")
antrian.tambah("Caca")

print("Antrian:")
antrian.tampil()

print("\nHapus depan:")
antrian.hapus_depan()
antrian.tampil()

print("\nCari data:")
antrian.cari("Budi")

print("\nHapus berdasarkan nama:")
antrian.hapus_nama("Caca")
antrian.tampil()
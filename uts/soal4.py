class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class AntrianPeminjaman:
    def __init__(self):
        self.head = None

    def tambah(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node

    def tampilkan(self):
        print("\n===== ANTRIAN PEMINJAMAN =====")
        current = self.head
        i = 1
        while current:
            d = current.data
            print(f"[{i}] {d['id']} - {d['nama']} | {d['kategori']}")
            current = current.next
            i += 1
        print("Total antrian:", self.hitung())

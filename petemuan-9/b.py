class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__ (self):
        self.head = None

    def tambah_kendaraan(self, plat):
        new_node = Node(plat)

        if self.head is None:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next

        current.next = new_node
        new_node.prev = current

    def tampilkan_maju(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def hapus_kendaraan(self, data):
        current = self.head

        while current:
            if current.data == data:
                if current.prev is None:
                    self.head = current.next
                    if self.head:
                        self.head.prev = None
                else:
                    current.prev.next = current.next
                    if current.next:
                      current.next.prev = current.prev
                return

            current = current.next

y1 = DoublyLinkedList()
y1.tambah_kendaraan("B 1111 AA")
y1.tambah_kendaraan("D 2222 BB")
y1.tambah_kendaraan("A 3333 CC")
y1.tambah_kendaraan("B 4444 DD")
print("Sebelum:")
y1.tampilkan_maju()
y1.hapus_kendaraan("A 3333 CC")
print("Sesudah:")
y1.tampilkan_maju()

class Node:
    def __init__ (self, nama):
        self.data = nama
        self.next = None

class CircularLinkedList:
    def __init__ (self):
        self.head = None

    def tambah_petugas(self, nama):
        new_node = Node(nama)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return
        current = self.head

        while current.next != self.head:
            current = current.next

        current.next = new_node
        new_node.next = self.head

    
    def giliran_berikutnya(self, n):
        if self.head is None:
            print("Belum ada petugas")
            return
        
        current = self.head
        for i in range(1, n+1):
            print(f"Giliran {i}: {current.data}")
            current = current.next

y1 = CircularLinkedList()

y1.tambah_petugas("Andi")
y1.tambah_petugas("Budi")
y1.tambah_petugas("Citra")
y1.tambah_petugas("Dewi")

y1.giliran_berikutnya(6)
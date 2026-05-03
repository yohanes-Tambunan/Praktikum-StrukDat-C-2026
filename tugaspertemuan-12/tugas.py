class Node:
    def __init__(self, id, judul):
        self.id = id
        self.judul = judul
        self.left = None
        self.right = None


class BinarySearchTrees:
    def __init__(self):
        self.root = None
        self.count = 1
    
    def insert(self, id, judul):
        new_node = Node(id, judul)

        if self.root is None:
            self.root = new_node
            return

        current = self.root
        while True:
            if id < current.id:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right

    def search(self, node, target):
        if node is None:
            return None

        if target == node.id:
            return node
        elif target < node.id:
            return self.search(node.left, target)
        else:
            return self.search(node.right, target)

    def traversal_inorder(self, node):
        if node:
            self.traversal_inorder(node.left)
            print(f"{self.count}. {node.id} - {node.judul}")
            self.count += 1
            self.traversal_inorder(node.right)

    def get_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def get_max(self, node):
        current = node
        while current.right is not None:
            current = current.right
        return current

    def height(self, node):
        if node is None:
            return -1

        left = self.height(node.left)
        right = self.height(node.right)

        return max(left, right) + 1

tree = BinarySearchTrees()

print('''
SISTEM KATALOG PERPUSTAKAAN "ILMU TERANG"
=========================================
''')

tree.insert(50, "Dasar Pemrograman")
tree.insert(30, "Struktur Data")
tree.insert(70, "Kecerdasan Buatan")
tree.insert(20, "Matematika Diskrit")
tree.insert(40, "Basis Data")
tree.insert(60, "Jaringan Komputer")
tree.insert(80, "Sistem Operasi")

print("[INFO] Koleksi Buku (In-Order Traversal):")
tree.traversal_inorder(tree.root)

result = tree.search(tree.root, 60)
if result:
    print(f"[SEARCH] ID 60 ditemukan: {result.judul}")
else:
    print("[SEARCH] ID 60 tidak ditemukan")

print(f"[STATISTIK] ID Terkecil: {tree.get_min(tree.root).id}")
print(f"[STATISTIK] ID Terbesar: {tree.get_max(tree.root).id}")

print(f"[INFO] Height: {tree.height(tree.root)}")




        
    
        


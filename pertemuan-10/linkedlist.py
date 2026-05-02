class Node:
    def __init__(self, url):
        self.url = url
        self.next =None

class StackLinkedList:
    def __init__ (self):
        self.top = None
        self.count = 0

    def isEmpty(self):
        return self.count == 0
    
    def push(self, url):
        new_node = Node(url)
        if self.top:
            new_node.next = self.top
        self.top = new_node
        self.count += 1

    def pop(self):
        if self.isEmpty():
            return "riwayat kosong"
        popped_node = self.top
        self.top = self.top.next
        self.count -= 1
        return popped_node.url
    
    def peek(self):
        if self.isEmpty():
            return "riwayat kosong"
        return self.top.url
    
    def size(self):
        return self.count
    
    def traverseAndPrint(self):
        currentNode = self.top
        while currentNode:
            print(currentNode.url)
            currentNode = currentNode.next
        print()

riwayat = StackLinkedList()
riwayat.push("Pildun 2026")
riwayat.push("Ronaldo juara")
riwayat.push("Pildun 2030")
riwayat.push("wasit barca")

print("LinkedList: ")
riwayat.traverseAndPrint()
print("Pop: ", riwayat.pop())
print("Peek: ", riwayat.peek())
print("LinkedList after Pop: ")
riwayat.traverseAndPrint()
print("kosong: ", riwayat.isEmpty())
print("ukuran: ", riwayat.size())




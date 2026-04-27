class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def traverseAndPrint(head):
    currentNode = head
    while currentNode:
        print(currentNode.data, end=" -> ")
        currentNode = currentNode.next
    print("null")       

def sisipkan_VIP(head, plat_baru, plat_target):
    if plat_target.next == None:
        plat_target.next = plat_baru
        return head
    plat_baru.next = plat_target.next
    plat_target.next = plat_baru
    return head
node1 = Node("B 1234 ABC")
node2 = Node("D 8888 XYZ")
node3 = Node("A 1111 TUV")
node4 = Node("B 2022 EFG")


node1.next = node2
node2.next = node3
node3.next = node4
node5 = Node(" RI 1")

node1 = sisipkan_VIP(node1, node5, node4)
traverseAndPrint(node1)

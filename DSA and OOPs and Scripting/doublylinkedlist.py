class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def push(self, nval):
        nnode = Node(nval)
        nnode.next = self.head
        if self.head:
            self.head.prev = nnode
        self.head = nnode

    def printlist(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next


dllist = DoublyLinkedList()
dllist.push(1)
dllist.push(2)
dllist.push(3)
dllist.printlist()
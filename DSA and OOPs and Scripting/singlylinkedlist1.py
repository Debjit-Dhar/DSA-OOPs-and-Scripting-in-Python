class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printlist(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


n = int(input('Enter number of nodes'))
if __name__ == '__main__':
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    llist.head.next = second
    i = 3
    prevnode = second
    while n > 2:
        nextnode = Node(i)
        i += 1
        prevnode.next = nextnode
        prevnode = nextnode
        n -= 1
    llist.printlist()

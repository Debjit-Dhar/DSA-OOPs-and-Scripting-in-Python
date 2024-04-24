class Node:
    def __init__(self,data,next):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def insert_at_end(self,data):
        if self.head is None:
            self.head=Node(data,None)
            return
        iter=self.head
        while iter.next:
            iter=iter.next
        iter.next=Node(data,None)
    def printlist(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next

llist=LinkedList()
llist.insert_at_end(1)
llist.insert_at_end(2)
llist.insert_at_end(3)
llist.printlist()



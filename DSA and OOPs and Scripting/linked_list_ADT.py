class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def init_l(self, data):
        self.head = Node(data)

    def empty_l(self):
        return self.head is None

    def atend_l(self, cur):
        return cur.next is None

    def insert_front(self, target):
        if self.empty_l():
            self.head = target
        else:
            target.next = self.head
            self.head = target

    def insert_after(self, target, prev):
        if prev is None:
            return
        else:
            target.next = prev.next
            prev.next = target

    def delete_front(self):
        if self.head is None:
            return
        else:
            self.head = self.head.next

    def delete_after(self, prev):
        if prev is None:
            return
        elif prev.next is None:
            return
        else:
            prev.next = prev.next.next

lob = LinkedList()
lob.init_l(1)

while True:
    choice = int(input('Enter choice (1 to insert, 2 to delete, 3 to print, any other to exit): '))

    if choice == 1:
        insert_choice = int(input('Enter insert choice (1 for front, 2 after a node): '))

        data = int(input('Enter data: '))
        node_ob = Node(data)

        if insert_choice == 1:
            lob.insert_front(node_ob)
        elif insert_choice == 2:
            # Ask for the node value after which to insert
            node_value = int(input('Enter the value of the node after which to insert: '))

            # Find the node with the specified value
            current_node = lob.head
            while current_node and current_node.data != node_value:
                current_node = current_node.next

            # Insert after the specified node
            if current_node:
                lob.insert_after(node_ob, current_node)
            else:
                print('Node not found.')
    elif choice ==2:
        node_value = int(input('Enter the value of the node to delete: '))
        current_node=lob.head
        if(node_value==current_node.data):
            lob.delete_front()
        else:
            temp=(current_node).next
            while not lob.atend_l(current_node):
                if(temp.data==node_value):
                    lob.delete_after(current_node)
                current_node = current_node.next
                temp=temp.next

    elif choice == 3:
        start = lob.head
        while not lob.atend_l(start):
            print(start.data, end='->')
            start = start.next
        print()

    else:
        break

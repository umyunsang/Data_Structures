class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
class CircularLinkedList:
    def __init__(self):
        self.head = None
    def insert(self, data, new_data):
        newnode = Node(new_data)
        if self.head is None:
            return
        if self.head.data == data:
            newnode.next = self.head.next
            self.head.next = newnode
            return
        current = self.head
        while current.next != self.head:
            if current.data == data:
                newnode.next = current.next
                current.next = newnode
                return
            current = current.next
        if current.data == data:
            current.next = newnode
            newnode.next = self.head
            return

    def delete(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next != self.head:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

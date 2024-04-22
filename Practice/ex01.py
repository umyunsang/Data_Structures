class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data, new_data):
        newnode = Node(new_data)
        if self.head is None:
            return
        current = self.head
        while current.next:
            if current.data == data:
                newnode.next = current.next
                newnode.prev = current
                if current.next:
                    current.next.prev = newnode
                else:
                    self.tail = newnode
                current.next = newnode
                return
            current = current.next

    def delete(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            self.head.prev = None
            return

        current = self.head
        while current.next:
            if current.data == data:
                if current.next:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                    current.prev.next = None
                return
            current = current.next
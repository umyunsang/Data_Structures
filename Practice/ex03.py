class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data, new_data):
        newNode = Node(new_data)
        if self.head is None:
            return
        current = self.head
        while current:
            if current.data == data:
                newNode.next = current.next
                current.next = newNode
                return
            current = current.next

    def delete(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

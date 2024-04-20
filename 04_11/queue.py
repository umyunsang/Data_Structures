class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def isEmpty(self):
        return self.front is None

    def enQueue(self, data):
        new_node = self.Node(data)
        if self.isEmpty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def deQueue(self):
        if self.isEmpty():
            return
        data = self.front.data
        if self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
        return data

    def peek(self):
        if self.isEmpty():
            return
        return self.front.data

    def print_queue(self):
        current = self.front
        while current:
            print(current.data, end=" >> ")
            current = current.next
        print("front")


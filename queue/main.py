from queue import Queue

q = Queue()

q.enQueue(1)
q.enQueue(2)
q.enQueue(3)

q.print_queue()

print("Peek:", q.peek())

print("Dequeue:", q.deQueue())

q.print_queue()

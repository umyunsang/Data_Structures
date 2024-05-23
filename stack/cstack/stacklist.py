class stack_list:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            return print("cstack is Empty")
        return self.items.pop()

    def topItem(self):
        return self.items[-1]

    def isEmpty(self):
        return not self.items

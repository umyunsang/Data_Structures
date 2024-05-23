class Stack:

    # Node 클래스
    class Node:
        def __init__(self, data=None):
            self.data = data
            self.next = None

    ## SigleList 클래스 정의
    def __init__(self):
        self.top = None
        self.size = 0

     ## Head Node 생성
    def create_top(self):
        if self.top is not None:
           return 98, "cstack has already been created"

        self.top = self.Node()
        return 100, "cstack creation completed"

    ### PUSH 동작
    def push(self, data):
        if self.top is None:
           return 99, "No stack was created."

        newNode = self.Node(data)
        newNode.next = self.top
        self.top = newNode
        self.size = self.size + 1
        return 100, "PUSH operation has been completed."

    ### POP 동작
    def pop(self):
        if self.size == 0:
            return 98, "No data exists on the stack."

        last = self.top
        self.top = self.top.next
        last.next = None
        self.size = self.size - 1
        return 100, "POP operation has been completed."

    ### Items on the cstack => print
    def print_items(self):
        current = self.top
        if current.next is None:
            return 98, "Empty cstack."

        print("STACK ITEM LIST")

        while current.next is not None:
            print(current.data, end = " >> ")
            current = current.next

        print("[None]")

    def result_message(self, result):
        code = ""
        if result[0] == 98:
            code = "Warning: "
        elif result[0] == 99:
            code = "Error: "
        else: code = "Success: "

        return print(code + result[1])












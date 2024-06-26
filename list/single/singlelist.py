class SingleList:

    # Node 클래스
    class Node:
        def __init__(self, data=None):
            self.data = data
            self.next = None

    ## SigleList 클래스 정의
    def __init__(self):
        self.head = None

     ## Head Node 생성
    def create_head(self):
        if self.head is not None:
            print("Head Node already exists...")
            return

        self.head = self.Node()

    ### 마지막 위치에 Node 추가
    def node_append(self, data=None):
        if self.head is None:
            print("Error : Head Node is not Create...")
            return

        current = self.head
        while current.next is not None:
            current = current.next

        newNode = self.Node(data)
        current.next = newNode

     ### Which data insert
    def node_insert(self, data, insertData):
        if self.head is None:
            print("Error : Head Node is not Create...")
            return

        current = self.head
        while current.next is not None:
            current = current.next
            if current.data == data:
                newNode = self.Node(insertData)
                newNode.next = current.next
                current.next = newNode
                return

        print("Warning: not Found Data")

    ### Head ~ Last node Print
    def all_print(self):
        current = self.head
        if current.next is None:
            print("Warning: Data Empty....")
            return

        print("All Data List")
        while current.next is not None:
            current = current.next
            print(current.data, end = " >> ")

        print("[None]")

    # Data Edit
    def node_edit(self, data, EditData):
        if self.head is None:
            print("Error : Head Node is not Create...")
            return

        current = self.head
        while current.next is not None:
            current = current.next
            if current.data == data:
                current.data = EditData
                return

        print("Warning: not Found Data")

    # Data Delete
    def node_delete(self, data):
        if self.head is None:
            print("Error: Head Node is not Created...")
            return

        current = self.head

        while current is not None:
            if current.data == data:
                break
            newNode = current
            current = current.next
        if current is None:
            print("Error: Node not found...")
            return
        newNode.next = current.next

    # Find node
    def node_find(self, data):
        if self.head is None:
            print("Error: Head Node is not Created...")
            return

        current = self.head
        slot = 0
        while current is not None:
            if current.data == data:
                return print(f'The entered data : {slot} slot')
            slot += 1
            current = current.next

        print("Error: Node not found...")
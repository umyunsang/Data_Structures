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
           return print("Head Node already exists...")

        self.head = self.Node()
        return print("Successfully!!! Created HEAD-NODE")

    ### 마지막 위치에 Node 추가
    def node_append(self, data):
        if self.head is None:
           return print("Error : Head Node is not Create...")

        current = self.head
        while current.next is not None:
            current = current.next

        newNode = self.Node(data)
        current.next = newNode
        return print("Successfully, appended data!!")

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
                return 100, "Successfully, Inserted data!!"

        return 99, "Warning: not Found Data"

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

    ## modify
    ## raw, change
    def node_modify(self, raw, change):
        if self.head is None:
            return print("Error : Head Node is not Create...")

        current = self.head
        while current.next is not None:
            if current.data == raw:
                current.data = change
                return print("Successfully, modified data!!")

            current = current.next

    ### Delete Node
    ## raw
    def node_delete(self, raw):
        current = self.head

        if current.next is None:
            return print("Warning: Data Empty")

        while current.next is not None:
            if current.next.data == raw:
                current.next = current.next.next
                return print("Successfully, deleted data!!")
            current = current.next
        return print("Warning: not Found Data")












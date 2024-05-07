class CircleList:

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

    ### 마지막 위치에 Node 추가, Node->next = head->next
    def node_append(self, data):
        if self.head is None:
           return 99, "Error : Head Node is not Create..."

        current = self.head
        last = self.head

        while True:
            current = current.next
            if current == None:
                newNode = self.Node(data)
                self.head.next = newNode
                newNode.next = newNode
                return 100, "Successfully, appended data!!"

            if current.next == last.next:
                break;

        newNode = self.Node(data)
        newNode.next = current.next
        current.next = newNode

        return 100, "Successfully, appended data!!"


     ### Which data insert
    def node_insert(self, data, insertData):
        if self.head is None:
            return 99, "Error : Head Node is not Create..."

        current = self.head
        last = self.head

        while True:
            current = current.next
            if current.next == last.next:
                newNode = self.Node(insertData)
                newNode.next = self.head.next

                return 100, "First Position inserted Data...."


        # while current.next != last.next:
        #     current = current.next
        #     if current.data == data:
        #         newNode = self.Node(insertData)
        #         newNode.next = current.next
        #         current.next = newNode
        #         return 100, "Successfully, Inserted data!!"

        return 99, "Warning: not Found Data"

    ### Head ~ Last node Print
    def all_print(self):
        current = self.head
        last = self.head
        if current.next is None:
            print("Warning: Data Empty....")
            return

        print("All Data List")
        while True:
            current = current.next
            print(current.data, end = " >> ")
            if current.next == last.next:
                break;

        print("[None]")









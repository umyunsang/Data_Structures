class doublelinked:

    # Node 클래스
    class Node:
        def __init__(self, data=None):
            self.lnext = None
            self.data = data
            self.rnext = None

    ## SigleList 클래스 정의
    def __init__(self):
        self.head = None
        self.tail = None

     ## Head Node 생성
    def create_ht(self):
        if self.head or self.tail is not None:
           return print("Head, Tail Node already exists...")

        self.head = self.Node()
        self.tail = self.Node()
        return print("Successfully!!! Created HEAD-NODE and TAIL-NODE")

    ### 마지막 위치에 Node 추가
    def node_append(self, data):
        if self.head is None:
           return 99, "Error : Head Node is not Create..."

        # current = self.head
        # while current.rnext is not None:
        #     current = current.rnext

        current = self.tail
        newNode = self.Node(data)
        if self.tail.lnext == None:   #첫번째 데이터인 경우
           self.head.rnext = newNode
           self.tail.lnext = newNode
           newNode.lnext = self.head
           newNode.rnext = self.tail
        else:
           newNode.lnext = self.tail.lnext
           newNode.rnext = self.tail.lnext.rnext
           self.tail.lnext.rnext = newNode
           self.tail.lnext = newNode

        return 100, "Successfully, appended data!!"

     ### Which data insert
    def node_insert(self, data, insertData):
        if self.head is None:
            print("Error : Head Node is not Create...")
            return

        current = self.head
        while current.rnext is not None:
            current = current.rnext
            if current.rnext is None:
                self.node_append(insertData)
                return 100, "Successfully Last position Append"
            if current.data == data:
                newNode = self.Node(insertData)
                newNode.lnext = current
                newNode.rnext = current.rnext
                current.rnext.lnext = newNode
                current.rnext = newNode

                return 100, "Successfully, Inserted data!!"

        return 99, "Warning: not Found Data"

    ### Head ~ Last node Print
    def order_print(self):
        current = self.head
        if current.rnext is None:
            print("Warning: Data Empty....")
            return

        print("In-Order Data List")
        while current.rnext is not None:
            if current.data is not None:
                print(current.data, end = " >> ")
            current = current.rnext

        print("[None]")

    def reverse_print(self):
        current = self.tail
        if current.lnext is None:
            print("Warning: Data Empty....")
            return

        print("Reverse Data List")
        while current is not None:
            if current.data is not None:
                print(current.data, end = " >> ")
            current = current.lnext

        print("[None]")


    def node_modify(self, raw, change):
        if self.head is None:
            print("Error : Head Node is not Create...")
            return

        current = self.head
        while current.rnext is not None:
            if current.data == raw:
                current.data = change
                return 100, "Successfully, Modified data!!"
            current = current.rnext

        return 99, "Warning: not Found Data"

    def node_delete(self, raw):

        if self.head is None:
            print("Error : Head Node is not Create...")
            return

        current = self.head
        while current.rnext is not None:

            if current.data == raw:
                current.lnext.rnext = current.rnext
                current.rnext.lnext = current.lnext

                return 100, "Successfully, Deleted data!!"
            current = current.rnext

        return 99, "Warning: not Found Data"







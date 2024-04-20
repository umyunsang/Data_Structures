class SList:
    class Node:
        def __init__(self, item, link):  # 노드 생성자
            self.item = item
            self.next = link
        # Node 클래스는 연결 리스트의 각 노드를 나타냅니다.
        # item: 노드가 저장하는 데이터를 나타내는 속성입니다.
        # next: 다음 노드를 가리키는 링크(포인터)입니다.

    def __init__(self):  # 연결 리스트 생성자
        self.head = None
        self.size = 0
    # __init__: head를 초기화하여 비어 있는 리스트를 만들고,
    #          size를 0으로 설정합니다.

    def size(self):  # 연결 리스트의 노드 수 리턴
        return self.size

    def is_empty(self):  # 연결 리스트가 empty인지 검사
        return self.size == 0

    def insert_front(self, item):  # 연결 리스트의 맨 앞에 노드 삽입
        if self.is_empty():
            self.head = self.Node(item, None)
        else:
            self.head = self.Node(item, self.head)
        self.size += 1
    # 리스트가 비어 있다면, head에 새로운 노드를 추가합니다.
    # 그렇지 않으면, 새로운 노드를 head로 만들고, 기존의 head를 새로운 노드의 next로 연결합니다.

    def insert_after(self, item, p):  # p가 참조하는 노드 뒤에 노드 삽입
        p.next = self.Node(item, p.next)
        self.size += 1
    # 주어진 노드 p 다음에 새로운 노드를 삽입하는 메서드입니다.
    # p.next가 새로운 노드를 가리키도록 만들고, 새로운 노드는 p의 다음 노드가 됩니다.

    def delete_front(self):  # 연결 리스트의 맨 앞에 있는 노드 삭제
        if self.is_empty():
            print('리스트가 empty 라서 삭제 불가')
        else:
            self.head = self.head.next
            self.size -= 1

    def delete_after(self, p):  # p가 참조하는 노드의 다음 노드를 삭제
        if self.is_empty():
            print('리스트가 empty 라서 삭제 불가')
        t = p.next
        p.next = t.next
        self.size -= 1

    def search(self, target):  # item이 target인 노드를 찾아서 몇 번째 노드인지를 반환
        p = self.head
        for k in range(self.size):
            if target == p.item:
                return k
            p = p.next
        return None

    def print_list(self):  # 연결 리스트를 한 줄에 출력
        p = self.head
        while p:
            if p.next is not None:
                print(p.item, ' -> ', end=' ')
            else:
                print(p.item)
            p = p.next

class EmptyError(Exception):
    pass



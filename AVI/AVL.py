from collections import deque


class AVLNode:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
        self.height = 1


class AVLTree:
    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    #left rotate
    def rotate_left(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        y.left = x
        x.right = T2

        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def insert(self, node, data):
        if not node:
            return AVLNode(data)
        elif data < node.data:
            node.left = self.insert(node.left, data)
        else:
            node.right = self.insert(node.right, data)

        #update height
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

        #calculate balance Factor
        balance = self.get_balance(node)

        #left left case
        if balance > 1 and data < node.left.data:
            pass

        #right right
        if balance < -1 and data > node.right.data:
            return self.rotate_left(node)

        #left right
        if balance > 1 and data > node.left.data:
            pass

        #right left
        if balance < -1 and data < node.right.data:
            pass

        return node

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data, end=" ")
            self.inorder(node.right)

    def levelOrder(self, root):
        if root is None:
            return 0

        queue = deque([root])
        cnt = 0
        while queue:
            size = len(queue)

            cnt = cnt + 1
            print(f"★ LEVEL ", cnt, ": ", end="")
            for _ in range(size):
                node = queue.popleft()
                print(node.data, end=" ")

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            print()

        return

from collections import deque
class AVLNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        bf = self.get_height(node.left) - self.get_height(node.right)
        print("balance: ", bf)
        return bf

    def rotate_right(self, y):
        x = y.left
        T2 = x.right

        # Perform rotation
        x.right = y
        y.left = T2

        # Update heights
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))

        # Return new root
        return x

    def rotate_left(self, x):
        y = x.right
        T2 = y.left

        # Perform rotation
        y.left = x
        x.right = T2

        # Update heights
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        # Return new root
        return y

    def insert(self, node, data):
        # Perform normal BST insertion
        if not node:
            newNode = AVLNode(data)
            print(f"new node data: ", newNode.data)
            print(f"new node height: ", newNode.height)
            print()
            return newNode
        elif data < node.data:
            node.left = self.insert(node.left, data)
        else:
            node.right = self.insert(node.right, data)

        # Update height of this ancestor node
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

        print(f"node data: ", node.data)
        print(f"update node height: ", node.height)
        print()


        # Get the balance factor
        balance = self.get_balance(node)

        # If node becomes unbalanced, then 4 cases arise

        # Left Left Case
        if balance > 1 and data < node.left.data:
            return self.rotate_right(node)

        # Right Right Case
        if balance < -1 and data > node.right.data:
            return self.rotate_left(node)

        # Left Right Case
        if balance > 1 and data > node.left.data:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        # Right Left Case
        if balance < -1 and data < node.right.data:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    def level_order(self, root):
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
                print("{0} ".format(node.data), end="")

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            print()

        return

    def pre_order(self, node):
        if not node:
            return
        print("{0} ".format(node.data), end="")
        self.pre_order(node.left)
        self.pre_order(node.right)

    def in_order(self,node):
        if not node:
            return
        if node:
            self.in_order(node.left)
            print("{0} ".format(node.data), end="")
            self.in_order(node.right)
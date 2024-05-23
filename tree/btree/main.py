from TreeNode import TreeNode


def preorder_recursive(node):
    if node is not None:
        print(node.value, end=' ')
        preorder_recursive(node.left)
        preorder_recursive(node.right)


def inorder_recursive(node):
    if node is not None:
        inorder_recursive(node.left)
        print(node.value, end=' ')
        inorder_recursive(node.right)


def postorder_recursive(node):
    if node is not None:
        postorder_recursive(node.left)
        postorder_recursive(node.right)
        print(node.value, end=' ')


def count_node(node):
    if node is None:
        return 0
    else:
        return count_node(node.left) + count_node(node.right) + 1


def calc_height(node):
    if node is None:
        return 0
    else:
        return max(calc_height(node.right), calc_height(node.left)) + 1


h = TreeNode('H')
d = TreeNode('D', h)
e = TreeNode('E')
b = TreeNode('B', d, e)

f = TreeNode('F')
c = TreeNode('C', f)

root = TreeNode('A', b, c)

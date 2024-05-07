from TreeNode import TreeNode


# 전위 순회
def preorder_recursive(node):
    if node is not None:
        print(node.value, end=' ')
        preorder_recursive(node.left)
        preorder_recursive(node.right)


# 중위 순회
def inorder_recursive(node):
    if node is not None:
        inorder_recursive(node.left)
        print(node.value, end=' ')
        inorder_recursive(node.right)


# 후위 순회
def postorder_recursive(node):
    if node is not None:
        postorder_recursive(node.left)
        postorder_recursive(node.right)
        print(node.value, end=' ')


d = TreeNode('D')
e = TreeNode('E')
b = TreeNode('B', d, e)

f = TreeNode('F')
c = TreeNode('C', f)

root = TreeNode('A', b, c)

print('\n전위 순회 : ')
preorder_recursive(root)
print('\n중위 순회 : ')
inorder_recursive(root)
print('\n후위 순회 : ')
postorder_recursive(root)

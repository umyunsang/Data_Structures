from AVL import *

avl = AVLTree()
root = None

items = [43, 49, 84]

for item in items:
    root = avl.insert(root, item)

avl.level_order(root)
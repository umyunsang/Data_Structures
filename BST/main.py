from BST import *

bst = BST()

items = [80, 60, 99, 48, 68]

for item in items:
    bst.insert(item)

print("BST 레벨 순회 결과")
bst.levelOrder_print()

search_data = 48
result = bst.search(search_data)
if result is None:
    print("데이터가 존재하지 않습니다.")
else:
    print(f'{search_data} 을/를 찾았습니다.')
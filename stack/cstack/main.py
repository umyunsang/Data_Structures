from cStack import cStack

## 단항 연산
# st = cStack()
#
# op = ['+', '-', '*', '/']
# br = ['(', ')']
#
# formula = '(A/B)'
#
# postfix = ''
#
# for i in formula:
#     if i not in op and i not in br:
#         postfix = postfix + i
#     else:
#         st.push(i)
#
#     if len(postfix) == 2:
#         print(postfix + st.topItem())
#         st.pop()
#         postfix = ''


st = cStack()
prec = {
    '*': 3, '/': 3,
    '+': 2, '-': 2,
    '(': 1}

formula = '(A*B)/(C-D)'
postfix = ''

for w in formula:
    if w in prec:
        if st.isEmpty():
            st.push(w)
        else:
            if w == '(':
                st.push(w)
            else:
                while prec.get(w) <= prec.get(st.topItem()):
                    postfix += st.pop()
                    if st.isEmpty(): break
                st.push(w)
    elif w == ')':
        while st.topItem() != '(':
            postfix += st.pop()
        st.pop()
    else:
        postfix += w

while not st.isEmpty():
    postfix += st.pop()

print(postfix)

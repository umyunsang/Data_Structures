def precedence(operator):
    if operator == '+' or operator == '-':
        return 1
    elif operator == '*' or operator == '/':
        return 2
    else:
        return 0  # 괄호의 우선순위는 가장 높음

def infix_to_prefix(infix_expression):
    operators = []
    prefix_expression = []

    for token in reversed(infix_expression):
        if token.isalnum():  # 피연산자인 경우
            prefix_expression.append(token)
        elif token == ')':  # 오른쪽 괄호인 경우
            operators.append(token)
        elif token == '(':  # 왼쪽 괄호인 경우
            while operators and operators[-1] != ')':
                prefix_expression.append(operators.pop())
            operators.pop()  # 왼쪽 괄호는 스택에서 제거
        else:  # 연산자인 경우
            while operators and precedence(operators[-1]) > precedence(token):
                prefix_expression.append(operators.pop())
            operators.append(token)

    while operators:
        prefix_expression.append(operators.pop())

    return ''.join(prefix_expression[::-1])

# 예시 사용
infix_expression = "A/B*C+D"
prefix_expression = infix_to_prefix(infix_expression)
print("중위 표기법:", infix_expression)
print("전위 표기법:", prefix_expression)

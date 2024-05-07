import keyboard
import time
from getkey import getkey


class stack_list:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            return print("Stack is Empty")
        return self.items.pop()

    def topItem(self):
        return self.items[-1]

    def isEmpty(self):
        return not self.items


stk = stack_list()

stk.push("http://www.naver.com")
stk.push("http://www.google.com")
stk.push("http://www.daum.net")
stk.push("http://www.tistory.com")
stk.push("http://www.donga.ac.kr")

print(stk.items)

while True:
    if keyboard.is_pressed('left'):
        time.sleep(0.1)
        stk.pop()
        print(stk.items)
    elif keyboard.is_pressed('q'):
        time.sleep(0.1)
        break

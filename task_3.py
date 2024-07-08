from collections import deque

class Stack:
    def __init__(self):
        self.items = deque()

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]



def main():
    stack = Stack()

    stroke = input("Take stroke: ")
    
    for i in stroke:
        if i == "(":
            stack.push('(')
        elif i == '{':
            stack.push('{')
        elif i == '[':
            stack.push('[')
        elif stack.peek() == '(' and i == ')':
            stack.pop()
        elif stack.peek() == '{' and i == '}':
            stack.pop()
        elif stack.peek() == '[' and i == ']':
            stack.pop()
    
    if stack.is_empty():
        print(f'Строка "{stroke}" є симетричною')
    else:
        print(f'Строка "{stroke}" є несиметричною')


if __name__ == "__main__":
    main()



from collections import deque
from colorama import Fore, Style, init

# Ініціалізація colorama
init()

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

def is_symmetric(stroke):
    stack = Stack()
    matching_pairs = {')': '(', '}': '{', ']': '['}

    for char in stroke:
        if char in "({[":
            stack.push(char)
        elif char in matching_pairs:
            if stack.is_empty() or stack.peek() != matching_pairs[char]:
                return False
            stack.pop()

    return stack.is_empty()

def main():
    stroke = input("Take stroke: ")
    
    if is_symmetric(stroke):
        print(Fore.GREEN + f'Строка "{stroke}" є симетричною' + Style.RESET_ALL)
    else:
        print(Fore.RED + f'Строка "{stroke}" не є симетричною' + Style.RESET_ALL)

if __name__ == "__main__":
    main()

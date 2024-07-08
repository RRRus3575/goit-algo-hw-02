from collections import deque
from colorama import Fore, Style, init

init()

def is_palindrome(str):
    char_deque = deque(str)
    
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False
    return True

def main():
    stroke = input("Take stroke: ")

    if is_palindrome(stroke):
        print(Fore.GREEN + f'The stroke "{stroke}" is a palindrome.' + Style.RESET_ALL)
    else:
        print(Fore.RED + f'The stroke "{stroke}" is not a palindrome.' + Style.RESET_ALL)


if __name__ == "__main__":
    main()

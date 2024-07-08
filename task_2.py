from collections import deque

def is_palindrome(str):
    char_deque = deque(str)
    
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False
    return True

def main():
    stroke = input("Take stroke: ")

    if is_palindrome(stroke):
        print(f'The stroke "{stroke}" is a palindrome.')
    else:
        print(f'The stroke "{stroke}" is not a palindrome.')


if __name__ == "__main__":
    main()

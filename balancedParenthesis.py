'''
Write a function is_balanced(input_str) that takes a string input_str as input and returns True if the parentheses in the string are balanced, and False otherwise. Use a stack to keep track of the parentheses.

Note: You only need to consider the characters ( and ) for this challenge.
'''

def is_balanced(input_str):
    stack = Stack()
    for input in input_str:
        if input == '(':
            stack.push(input)
        elif input == ')':
            pop = stack.pop()
            if pop == None:
                return False
    if stack.peek() == None:
        return True
    else:
        return False
   


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            return None
        return self.items.pop()

    def peek(self):
        if len(self.items) == 0:
            return None
        return self.items[len(self.items) - 1]
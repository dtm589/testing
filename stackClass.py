'''
Implementing a stack class
'''


class Stack:
    def __init__(self):
        self.arrows = []

    def push(self, arrow):
        self.arrows.append(arrow)

    def pop(self):
        if self.arrows:
            return self.arrows.pop()
        return None

    def peek(self):
        if self.arrows:
            return self.arrows[-1]
        return None

    def size(self):
        return len(self.arrows)
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, num):
        self.stack.append(num)

    def pop(self):
        return self.stack.pop()
    
    def size(self):
        return len(self.stack)
    
    def peek(self):
        if (self.size() > 0):
            return self.stack[self.size() - 1]
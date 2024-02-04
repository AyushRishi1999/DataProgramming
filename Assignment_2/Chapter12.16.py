class Stack(list):
    def __init__(self):
        super().__init__()
    def push(self, value):
        self.append(value)
    def pop(self):
        if not self.is_empty():
            return super().pop()
        else:
            raise IndexError("pop from an empty stack")
    def peek(self):
        if not self.is_empty():
            return self[-1]
        else:
            return None
    def is_empty(self):
        return len(self) == 0
    def get_size(self):
        return len(self)

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print("Stack:", stack)
print("Peek:", stack.peek())
print("Pop:", stack.pop())
print("Stack after pop:", stack)
print("Is Empty:", stack.is_empty())
print("Stack Size:", stack.get_size())

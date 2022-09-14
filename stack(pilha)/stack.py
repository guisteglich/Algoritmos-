from typing_extensions import Self


class Stack:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def push(self, data):
        self.items.append(data)
    
    def pop(self):
        if self.size() == 0:
            return None 
        return self.items.pop() 

myStack = Stack()

myStack.push("Google")
myStack.push("Facebook")
myStack.push("Twitter")

print(myStack.items)

myStack.pop()
myStack.pop()
print(myStack.items)
    
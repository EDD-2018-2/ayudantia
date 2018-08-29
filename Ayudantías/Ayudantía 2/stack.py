class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None

class Stack:
    def __init__(self):
        self.head = None
        self.count = 0

    def push(self, data):
        nodo = Node(data)
        if self.empty():
            self.head = nodo
        else:
            nodo.prev = self.head
            self.head = nodo
        self.count += 1

    def pop(self):  
        if self.empty():
            return False
        else:
            self.head = self.head.prev
            self.count -= 1

    def top(self):
        return self.head

    def empty(self):
        return self.head == None

if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.pop()
    print("Tope: ", stack.top().data)


    

class Node:
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority
        self.next = None

class PriorityQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
    
    def empty(self):
        return self.head == None
        
    def push(self, data, priority):
        node = Node(data, priority)
        if self.empty():
            self.head = node
            self.tail = node
            self.count += 1
        else:
            self.tail.next = node
            self.tail = node
            self.count += 1
    def find(self):
        if self.empty():
            return None
        else: 
            temp = self.head
            prev_high_node = temp
            high_node = temp
            while temp.next != None:
                if temp.next.priority > high_node.priority
                    prev_high_node = temp
                    high_node = temp.next
                temp = temp.next
        return prev_high_node, high_node
    def pop(self):
        if self.empty():
            print("Cola vacia")
        elif self.count == 1:
            self.head = None
            self.tail = None
        else:
            prev_dequeue, to_dequeue = self.find()
            if prev_dequeue == to_dequeue:
                self.head = to_dequeue.next
            else:
                prev_dequeue.next = to_dequeue.next
                to_dequeue.next = None
            self.count -= 1
    def front(self):
        if self.empty():
            return None
        return self.head
    def back(self):
        if self.empty():
            return None
        return self.tail
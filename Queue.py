class Queue(object):

    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def enqueue(self,items):
        self.items.insert(0,items)
    
    def dequeue(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)
    
    def totalItems(self):
        return self.items
q = Queue()
print(q.size())
q.enqueue(10)
q.enqueue(11)
q.enqueue(12)
print(q.totalItems())
q.dequeue()
print(q.totalItems())
print(q.totalItems())

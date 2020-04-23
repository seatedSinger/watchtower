class LL_node:
    def __init__(self, value, nextNode = None):
        self.value = value
        self.nextNode = nextNode

class LinkedList:
    def __init__(self, head = None):
        self.head = head
    
    def insert(self, value):
        node = LL_node(value)
        if self.head == None:
            self.head = node
            return
        currentNode = self.head
        while True:
            if currentNode.nextNode is None:
                currentNode.nextNode = node
                break
            currentNode = currentNode.nextNode
    
    def reverse(self):
        curr = self.head
        prev = None
        while curr != None:
            next = curr.nextNode
            curr.nextNode = prev
            prev = curr
            curr = next
        self.head = prev
        return prev

        # prev = None
        # curr = self.head
        # while curr:
        #     next = curr.nextNode
        #     curr.nextNode = prev
        #     prev = curr
        #     curr = next
        # self.head = prev
        # return prev

        # prev = None
        # cur = self.head
        # while cur:
        #     tmp = cur.nextNode
        #     cur.nextNode =  prev
        #     prev = cur
        #     cur = tmp
        # self.head = prev
        # return prev
        
        # current = self.head
        # prev = None
        # while current.nextNode != None:
        #     tmp = current.nextNode
        #     current.nextNode = prev
        #     prev = current
        #     current = tmp
        # current.nextNode = prev
        # self.head = current
    def remove_dupe(self):
        curr = self.head
        while curr and curr.nextNode != None:
            if curr.nextNode.value == curr.value:
                curr.nextNode = curr.nextNode.nextNode
            else:
                curr = curr.nextNode
        return curr


    def printLL(self):
        currentNode = self.head
        while currentNode != None:
            print(currentNode.value,'->',end='')
            currentNode = currentNode.nextNode
        print('None')

l = LinkedList()
l.insert('4')
l.insert('4')
l.insert('5')
l.insert('8')
l.insert('8')
l.insert('8')
l.printLL()
l.reverse()
l.printLL()
l.remove_dupe()
l.printLL()
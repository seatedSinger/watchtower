class Stack:
    def __init__(self):
        self.items = []
    def push(self,items):
        # self.items.append(items)
        self.items.insert(0,items)
    def remove(self):
        self.items.pop()
    def peekMax(self):
        return max(self.items)
    def peekAll(self):
        return self.items
    def top(self):
        return self.items[0]
s = Stack()
s.push(3)
s.push(4)
s.push(5)
s.push(6)
print(s.peekAll())
s.remove()
print(s.peekAll())
# print(s.peekMax())
print(s.top())

'''
HC
1 x  -Push the element x into the stack.
2    -Delete the element present at the top of the stack.
3    -Print the maximum element in the stack.
'''

items = [0]
for i in range(int(input())):
    nums = list(map(int, input().split()))
    if nums[0] == 1:
        items.append(max(nums[1], items[-1]))
    elif nums[0] == 2:
        items.pop()
    else:
        print(items[-1])
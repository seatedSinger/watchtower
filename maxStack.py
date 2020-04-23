class MaxStack:

    def __init__(self):
        self.data = []
        

    def push(self, x):
        # self.data.append(x)
        self.data.insert(0, x)

    def pop(self):
        return self.data.pop(0)

    def top(self):
        return self.data[0]

    def peekMax(self):
        return max(self.data)

    def popMax(self):
        ans = max(self.data)
        self.data.remove(ans)
        return ans




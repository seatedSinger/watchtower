class FirstUnique:

    def __init__(self, nums: List[int]):
        self.q = []
        self.dict = {}
        for i in nums:
            self.add(i)

    def showFirstUnique(self) -> int:
        
        while len(self.q) > 0 and self.dict[self.q[0]] > 1:
            self.q.pop(0)
        if len(self.q) == 0:
            return -1
        else:
            return self.q[0]

    def add(self, value: int) -> None:
        if value in self.dict:
            self.dict[value] += 1
        else:
            self.dict[value] = 1
            self.q.append(value)

################################

import collections
class FirstUnique:

    def __init__(self, nums: List[int]):
        self.deque = collections.deque()
        self.lookup = {}

        for num in nums:
            self.add(num)
    
    def showFirstUnique(self) -> int:
        if len(self.deque) == 0:
            return -1

        while len(self.deque) > 0 and self.deque[0] in self.lookup and self.lookup[self.deque[0]] >= 2:
            self.deque.popleft()

            if len(self.deque) == 0:
                return -1
            return self.deque[0]    

    def add(self, value: int) -> None:
        if value in self.lookup:
            self.lookup[value] += 1
        else:
            self.lookup[value] = 1
        self.deque.append(value)


def inorderTraversal2(self,root):
        ans = []
        stack = []
        while root:
            stack.append(root)
            root = root.left
        # Now root is the most left node
        while stack:
            node = stack[-1] 
            # stack[-1] is always the most left node
            ans.append(node.val)
            if node.right: # has right, repeat pushing all left nodes to stack
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left
            if not node.right:
                # if no right node, pop this node out and find the precessor 
                node = stack.pop(-1)
                while stack and stack[-1].right == node:
                    node = stack.pop(-1)
        return ans    
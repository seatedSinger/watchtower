'''
O(n) | O(w + h) > w is width of tree, size h
'''

from binarytree import build
from collections import deque

root = build(values=[3, 9, 20, 15, 7])

def averageOfLevels(root):
    queue = deque([root])
    res = []

    while queue:
        level = []
        for i in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        res.append(sum(level)/len(level))
    return res

def solution2(root):
    result = []
    level = (root,)
    while level:
      result.append(sum(node.val for node in level) / len(level))
      level = tuple(leaf for node in level for leaf in (node.left, node.right) if leaf)
    return result


print(averageOfLevels(root))
print(solution2(root))

from binarytree import build
from collections import deque

values = [6, 7, 8, 2, 7, 1, 3, 9, None, 1, 4, None, None, None, 5]
root = build(values)
# print(root)
'''
Using dfs1 to find deepest level in Binary Tree
Using dfs2 to collect all nodes which are deepest,
d as second parameter, each time a node is seen with desired depth
it's added to self.res 
'''


def deepestLevelSum(root):
    def dfs1(node):
        if not node:
            return 0
        return 1 + max(dfs1(node.left), dfs1(node.right))

    def dfs2(node, d):
        nonlocal res
        if not node:
            return
        if d == depth:
            res += node.val
        dfs2(node.left, d)
        dfs2(node.right, d)
    res = 0
    depth = dfs1(root)
    dfs2(root, 1)
    return res


print(deepestLevelSum(root))

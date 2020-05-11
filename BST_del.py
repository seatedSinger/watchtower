# class Node:
#     def __init__(self, key):
#         self.val = val
#         self.left = left
#         self.right = right

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
    
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.key)
        inorder(root.right)

def insert(node, key):
    if node is None:
        return Node(key)
    
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right ,key)
    return node

def minValue(node):
    current = node

    while current.left is not None:
        current = current.left
    return current

def delNode(root ,key):
    if not root:
        return root
    
    if key < root.key:
        root.left = delNode(root.left, key)
    elif key > root.key:
        root.right = delNode(root.right , key)
    
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        
        temp = minValue(root.right)
        root.key = temp.key
        root.right = delNode(root.right, temp.key)
    return root


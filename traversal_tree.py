def inOrder(root):
    stack, res = [], []
    node = root

    while stack and node:
        while stack:
            
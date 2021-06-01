def treeToString(t):
    if t is None:
        return ''
    result = str(t.val)
    if t.left:
        result += '(' + treeToString(t.left) + ')'
        if t.right:
            result += '(' + treeToString(t.right) + ')'
    elif t.right:
        result += '()' + '(' + treeToString(t.right) + ')'
    return result

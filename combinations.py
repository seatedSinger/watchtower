n = 4
k = 2

def combine(n ,k):
    res = []
    backtrack(n, k, res, [], 1)
    return res

def backtrack(n, k, res, path, index):
    if len(path) == k:
        res.append(path)
        return
    for i in range(index, n+1):
        backtrack(n ,k, res, path+[i], i+1)
print(combine(n,k))

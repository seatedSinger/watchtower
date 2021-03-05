baseCosts = [2, 3]
toppingCosts = [4, 5, 100]
target = 18

'''
def closestCost(base, top, target):
    res = float('inf')
    top.sort()
    for i in baseCosts:
        dfs(top, target, i)
    return res


def dfs(top, tartget, sums):
    nonlocal res
    if abs(target - sums) < abs(res - target):
        res = sums
    if sums > target:
        return
    for i in range(len(top)):
        dfs(top[i + 1:], target, sums + 0*top[i])
'''

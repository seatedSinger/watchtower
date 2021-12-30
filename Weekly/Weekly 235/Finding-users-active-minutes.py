# O(N) | O(N)
from collections import defaultdict

def findingUserActiveMin(logs, k):
    res = [0] * k
    aux = defaultdict(set)
    for id, times in logs:
        aux[id].add(times)
    for times in aux.values():
        res[len(times)-1] += 1
    return res


def solution2(logs, k):
    res = [0] * k
    aux = {}
    for idx, times in logs:
        aux.setdefault(idx, set()).add(times)
    for v in aux.values():
        if len(v) <= k:
            res[len(v)-1] += 1
    return res


logs = [[1,1],[2,2],[2,3]]
k = 4
print(findingUserActiveMin(logs, k))
print(solution2(logs,k))
logs = [[0,5],[1,2],[0,2],[0,5],[1,3]]
k = 5
print(findingUserActiveMin(logs, k))

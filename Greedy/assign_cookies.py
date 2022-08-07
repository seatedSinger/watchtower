'''
1. Reverse: Give largest cookie to greediest kid who will eat it until
    either there are no more kids or cookies, then return number of cookies consumed
O(NlogN) : N = max(n, m), where n = |s|, m = |g|, then it is O(NlogN)
'''

def assginCookies(g, s):
    g.sort(reverse=True)
    s.sort(reverse=True)
    i, j = 0, 0
    while i < len(g) and j < len(s):
        if g[i] <= s[j]:
            j += 1
        i += 1
    return j


def assginCookies_2(g, s):
    g.sort()
    s.sort()
    i, j = 0, 0
    while i < len(g) and j < len(s):
        if s[j] >= g[i]:
            i += 1
        j += 1
    return i


print(assginCookies([1, 2, 3], [1, 1])) # 1
print(assginCookies([1, 2], [1, 2 ,3])) # 2
print(assginCookies([2, 4, 6, 7], [1, 3, 4, 6, 7])) # 4

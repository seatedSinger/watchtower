# O(10), O(N)

def solution(s):
    map_ = set('aeiouAEIOU')
    a, b = 0, 0
    for i in range(len(s)//2):
        if s[i] in map_:
            a += 1
        if s[-i-1] in map_:
            b += 1
    return a == b

from collections import Counter
def solution2(s):
    vs, n = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'], len(s)//2
    # a, b = Counter(s[:n]), Counter(s[n:])
    a, b = map(Counter, (s[:n], Counter(s[n:])))
    return sum(a[v] for v in vs) == sum(b[v] for v in vs)


s = 'abcdefgh'
print(solution(s))
print(solution2(s))

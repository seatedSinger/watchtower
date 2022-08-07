from collections import defaultdict
import bisect
s = "abc"
t = 'ahbgdc'

def isSubsequence(s, t):
    # for large input follow up
    lookup = defaultdict(list)
    for i, c in enumerate(t):
        lookup[c].append(i)

    cur_place = 0
    for w in s:
        cur_idx = bisect.bisect_left(lookup[w], cur_place)
        if cur_idx >= len(lookup[w]):
            return False
        cur_place = lookup[w][cur_idx] + 1
    return True


def numMatchingSubq(s, t):
    i = 0
    for j in t:
        if s[i] == j:
            i += 1
            if i == len(s):
                return True
    return False


print(numMatchingSubq(s, t))
print(isSubsequence('axc', 'ahbgdc'))
print(isSubsequence(s, t))

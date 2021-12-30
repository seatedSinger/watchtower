from collections import Counter
s = "cbaebabacd"
p = "abc"


def findAnagrams(s, p):
    count = Counter(p)
    pLen = len(p)
    res = []
    L, R = 0, 0
    while R < len(s):
        if s[R] in count:
            count[s[R]] -= 1
            if count[s[R]] >= 0:
                pLen -= 1
        if pLen == 0:
            res.append(L)
        if R == L + len(p) - 1:
            if s[L] in count:
                if count[s[L]] >= 0:
                    pLen += 1
                count[s[L]] += 1
            L += 1
        R += 1
    return res

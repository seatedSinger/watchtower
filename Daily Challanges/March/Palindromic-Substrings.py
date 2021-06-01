# REVIEW : This need further review
# Brute
# O(N3)
def solution1(s):
    res = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            if s[i:j+1] == s[i:j+1][::-1]:
                res += 1
    return res


def solution2(s):
    s = '#' + '#'.join(s) + '#'
    res = []

    for idx in range(len(s)):
        length = 0
        while idx-length >= 0 and idx+length < len(s) and s[idx+length] == s[idx-length]:
            length += 1
        res.append(length)
    print(res)
    print(sum([x//2 for x in res]))


def solution3(s):
    if not s:
        return None
    n = len(s)
    dp = [[False]*n for _ in range(n)]
    res = 0

    for i in reversed(range(n)):
        #* since dp[i][j] depends on dp[i+1][j], so check larget i first
        for j in range(i, len(s)):
            if j - i < 2 and s[i] == s[j]:
                dp[i][j] = True
                res += 1
            elif dp[i+1][j-1] and s[i] == s[j]:
                dp[i][j] = True
                res += 1
    return res




s = 'abc'
d = 'aaa'
# print(solution1(s))
# print(solution1(d))
# print(solution2(s))
print(solution3(s))
print(solution3(d))

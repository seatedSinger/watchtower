s = "abc"
t = 'ahbgdc'


def numMatchingSubq(s, t):
    i = 0
    for j in t:
        if s[i] == j:
            i += 1
            if i == len(s):
                return True
    return False


print(numMatchingSubq(s, t))
print(numMatchingSubq('axc', 'ahbgdc'))

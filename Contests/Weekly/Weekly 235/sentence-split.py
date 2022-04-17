# O(N)

def truncateSentence(s, k):
    # s = s.split()
    # return ' '.join([x for x in s[:k]])
    return ' '.join(s.split(maxsplit=k)[:k])


s = "What is the solution to this problem"
k = 4
print(truncateSentence(s, k))

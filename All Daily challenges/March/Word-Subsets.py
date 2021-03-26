# Time : space O(A + B) Space O(m) [total word length] | A and B no. of total chars in a & b
# union operation

from collections import Counter


def wordSubsets(A, B):
    count = Counter()
    for i in B:
        count |= Counter(i)
    # for i in A:
        # print(count - Counter(i))
    return [x for x in A if not count - Counter(x)]


A = ["amazon", "apple", "facebook", "google", "leetcode"]
B = ["e", "o"]
print(wordSubsets(A, B))
A = ["amazon", "apple", "facebook", "google", "leetcode"]
B = ["e", "oo"]
print(wordSubsets(A, B))
'''
some breakdown:

    count = Counter()
    for i in B:
        count |= Counter(i)
    # return [x for x in A if not count - Counter(x)]
    # x = [x for x in A if not count - Counter(x)]
    for x in A:
        # print(count,'->',Counter(x))
        # print(count.items(),'->', Counter(x).items())
        print(count.items() - Counter(x).items())
    # set        
'''

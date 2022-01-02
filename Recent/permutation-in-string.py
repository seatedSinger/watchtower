# do bunch of Greedy problems

from typing import Counter, DefaultDict


s1, s2 = "ab", "eeeidbaooo"


def permutationString(s1, s2):
    '''
    # this is faster than using regular Hash
    Use the same counter but much more effeciently
    wo pointers i(front) j(last), delete and add accordingly and check for the counts
    '''
    # ctr1 = collections.defaultdict(int)
    # ctr2 = collections.defaultdict(int)
    # for x in s1: ctr1[x] += 1
    # for x in s2[:len(s1)]: ctr2[x] += 1
    # print(c2[s2[i]]) in dict c2 -> access items from s2 at index i

    ctr1 = Counter(s1)
    ctr2 = Counter(s2[:len(s1)])

    i = 0
    j = len(s1)

    while j < len(s2):
        if ctr2 == ctr1:
            return True
        ctr2[s2[i]] -= 1
        if ctr2[s2[i]] < 1:
            ctr2.pop(s2[i])
        ctr2[s2[j]] = ctr2.get(s2[j], 0) + 1
        i += 1
        j += 1

    return ctr2 == ctr1


print(permutationString(s1, s2))

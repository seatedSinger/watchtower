# sort + hash
from collections import Counter
s = ['eat', 'ate', 'apt', 'pat', 'tea', 'now']


def anagram(s):
    # sorting + dict/hash
    aux = {}
    for char in s:
        # f = ''.join(sorted(char))
        f = tuple(sorted(char))
        if f not in aux:
            aux[f] = [char]
        else:
            aux[f].append(char)
    return [x for x in aux.values()]

print(anagram(s))

def solution2(s):
    aux = {}
    for i in s:
        # key = tuple(sorted(i))
        key = ''.join(sorted(i))
        aux[key] = aux.get(key, []) + [i]
    return aux.values()

print(solution2(s))

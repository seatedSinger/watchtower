'''
'''
from itertools import permutations

def distringMatch(s):
    return set((permutations(s)))    


# print(distringMatch("IDID"))

print(set(permutations("DDI")))
print(list(permutations("DDI")))
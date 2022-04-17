from typing import Counter


def numberDiffInt(w):
    s = ''.join(x if x.isdigit() else ' ' for x in w)
    return len(set(x.lstrip('0') for x in s.split()))
    return len(Counter(map(int, s.split())))


a = 'a123bc34d8ef34'
b = 'leet1234code234'
c = 'a1b01c001'

for i in a,b,c:
    print(numberDiffInt(i))

from collections import Counter
s = 'aaabbbcc'
s2 = 'ceabaacb'


def minDel(s):
    count, res, used = Counter(s), 0, set()
    for ch, freq in count.items():
        while freq > 0:
            freq -= 1
            res += 1
        used.add(freq)
    return res


print(minDel(s))

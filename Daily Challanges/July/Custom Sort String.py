from collections import Counter
order = 'cba'
s = 'abcd'


def customSorting(order, s):
    letters = list(order + s)
    count, res = Counter(s), ''
    for l in letters:
        if l in count:
            while count[l] > 0:
                res += l
                count[l] -= 1
    return res


print(customSorting(order, s))

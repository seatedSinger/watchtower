# slack

from collections import defaultdict
s = 'niesevehrtfeev'
mapping = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
}


def slackAnagram(s):
    d = defaultdict()
    for i in s:
        if i not in d:
            d[i] = 0
        d[i] += 1
    return d

def use_digit(d, word_dict, digit):
    for i in word_dict:
        if i not in d or word_dict[i] > d[i]:
            return d, 0
    for i in word_dict:
        d[i] -= word_dict[i]
    return d, use_digit + 1


print(slackAnagram(s))

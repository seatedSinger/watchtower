from collections import defaultdict
import bisect

s = "abcde"
words = ["a", "bb", "acd", "ace"]


def numMatchingSeq(s, words):
    lookup = defaultdict(list)
    # aux = {c: [i] for i, c in enumerate(s)}
    res = 0
    for i, c in enumerate(s):
        lookup[c].append(i)
    for w in words:
        prev = -1
        found = True
        for c in w:
            # tmp = binary_S(lookup[c], prev)
            tmp = bisect.bisect(lookup[c], prev)
            if tmp == len(lookup[c]):
                found = False
                break
            else:
                prev = lookup[c][tmp]
        if found:
            res += 1
    return res


def numMatchingSubq2(S, words):
    word_dict = defaultdict(list)
    count = 0

    for word in words:
        word_dict[word[0]].append(word)

    for char in S:
        words_expecting_char = word_dict[char]
        word_dict[char] = []
        for word in words_expecting_char:
            if len(word) == 1:
                # Finished subsequence!
                count += 1
            else:
                word_dict[word[1]].append(word[1:])

    return count


# print(numMatchingSubq(s, words))

from collections import Counter
import heapq

#* O(nlogn)
#* counter for frequency
#* create list of tuples which'll contain (word, count)
#* Sort by the count and secondary by the word. Note that by negating the count we sort from
#* highest count to lowest instead of the other way around.
#* (Note also that you can't just do a reverse sort or the words themselves would be the wrong way around.)
#* strip of and retrun a list of first k word


def kFrequent(words, k):
    count = Counter(words)
    items = list(count.items())
    return heapq.nsmallest(k, count, key=lambda word: (~count[word], word))
    # items.sort(key=lambda item:(-item[1], item[0]))
    # return [item[0] for item in items[0:k]]


def solution2(words, k):
    d = {}
    for i in words:
        d[i] = d.get(i, 0) + 1
    res = sorted(d, key=lambda word: (-d[word], word))
    return res[:k]


words = ["i", "love", "leetcode", "i", "love", "coding"]
k = 2
print(kFrequent(words, k))
# print(solution2(words, k))
words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
k = 4
print(kFrequent(words, k))
# print(solution2(words, k))

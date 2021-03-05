from collections import Counter
import heapq

def kFrequent(words, k):

    return heapq.nsmallest(k,words)
    # heap = []
    # for v in words:
    #     heapq.heappush(heap, v)
    #     if len(heap) == k:
    #         heapq.heappop(heap)
    # return heap 


words = ["i", "love", "leetcode", "i", "love", "coding"]
k = 2
print(kFrequent(words, k))

words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
k = 4
print(kFrequent(words,k))
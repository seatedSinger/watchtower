'''
sorting | O(n log n)
heap | O(log n) | O(n)
'''
#* origin : (0,0), & Euclidean distance

import heapq


def kClosest(points, k):
    res = []
    for (x, y) in points:
        dist = (x*x + y*y)
        return heapq.nsmallest(k, points, lambda x: x[0] * x[0] + x[1] * x[1])


a = [[3, 3], [5, -1], [-2, 4]]
k = 2
print(kClosest(a, k))

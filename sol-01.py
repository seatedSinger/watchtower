'''
spiral Order
'''
# def spiralOrder(matrix):
#     if not matrix:
#         return []
#     spiral = []
#     while matrix:
#         spiral += matrix.pop(0)
        
#         if matrix and matrix[0]:
#             for row in matrix:
#                 spiral.append(row.pop())
#         if matrix:
#             spiral += matrix.pop()[::-1]
#         if matrix and matrix[0]:
#             for row in matrix[::-1]:
#                 spiral.append(row.pop(0))
#     return spiral
            
# matrix = [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# print(spiralOrder(matrix))

from collections import Counter

arr = [3,3,3,3,5,5,5,2,2,7]


# set_ = set()
# total_count = 0

# for index,count in enumerate(sorted(Counter(arr).values(),reverse=True)):
#     total_count += count

#     if total_count >= len(arr)//2:
#         print(index+1)

import collections
from collections import Counter

def sol(arr):
    l = (len(arr)+1) //2
    c = collections.Counter(arr)
    res = count = 0
    for i,j in c.most_common():
        count += j
        res += 1
        if count >= l:
            return res
print(sol(arr))
print(sol(arr))



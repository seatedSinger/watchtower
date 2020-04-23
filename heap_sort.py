'''
heappush(list,item)
Adds an element to heap, and re-sort it after addition or removal of 
item

heapPop(list)
removes the 1st (smallest) element and return that element.
Heap remains heap so we don't have to call heapify

heapify(list)
list to heap, exists even no access coz it needs to be unchangable
'''

import heapq
from heapq import heappop,heappush

def hep_sort(arr):
    heap = []
    for element in arr:
        heappush(heap,element)
    
    ordered = []

    while heap:
        ordered.append(heappop(heap))
    return ordered

arr = [90,2,5,71,88,11]
print(hep_sort(arr))
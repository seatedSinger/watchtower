nums = [1,-3,2,3,-4] #* 5
nums2 = [2,-5,1,-4,3,-2] #* 8

def maxAbsoluteSum(nums):
    total = []
    # res = float('-inf')
    res = 0
    sum_sofar = 0
    for i in nums:
        sum_sofar += i 
        res = max(sum_sofar, res)
        sum_sofar = max(sum_sofar, 0)


    # ans = float('inf')
    ans = 0
    min_sumSofar = 0
    for i in nums:
        min_sumSofar += i 
        ans = min(min_sumSofar, ans)
        min_sumSofar = min(min_sumSofar, 0)
    total.append(abs(res))
    total.append(abs(ans))
    return max(total)

print(maxAbsoluteSum(nums2))

from itertools import accumulate

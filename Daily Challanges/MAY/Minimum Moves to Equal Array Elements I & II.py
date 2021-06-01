'''
1. Calculate how many decreases we can perform
2. Get mid | median and decrease left to right
O(n) | O(1)
'''
nums = [1, 2, 3]
nums2 = [1, 10, 2, 9]
nums3 = [4, 3, 4]


def minMoves2(nums):
    return sum(nums) - len(nums) * min(nums)

def minMovesII(nums):
    # need median
    median = sorted(nums)[len(nums) // 2]
    res = [abs(i - median) for i in nums]
    return sum(res)


print(minMoves2(nums))
print(minMovesII(nums2))
print(minMovesII(nums3))

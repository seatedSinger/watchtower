'''
Calculate how many decreases we can perform
'''
nums = [1, 2, 3]
nums2 = [1, 10, 2, 9]
nums3 = [4, 3, 4]


def minMoves2(nums):
    return sum(nums) - len(nums) * min(nums)


print(minMoves2(nums))
print(minMoves2(nums2))
print(minMoves2(nums3))

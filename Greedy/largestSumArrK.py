'''
'''

def largestSumK(nums, k):
    nums.sort()
    for i in range(k):
        # if nums[i] == 
        # print(nums[i])
        return sum(x for x in nums)


# print(largestSumK([4, 2, 3], 1))
# print(largestSumK([3, -1, 0, 2], 3))
print(largestSumK([2, -3, -1, 5, -4], 2))

'''
sorting
'''

def minPairSum(nums):
    # nums.sort()
    # res = 0
    # i, j = 0, len(nums) - 1
    # while i <= j:
    #     res = max(res, nums[i] + nums[j])
    #     i +=1
    #     j -= 1
    # return res
    # return max(a + b for a, b in zip(sorted(nums), sorted(nums)[::-1]))
    return list((a + b for a, b in zip(sorted(nums), sorted(nums)[::-1])))
    # return list(zip(sorted(nums), sorted(nums)[::-1]))

print(minPairSum([3, 5, 2, 3]))
print(minPairSum([3, 5, 4, 2, 4, 6]))

'''
2 if -> nums[j] < nums[i] < nums[k] for all 0 <= j < i
1 if -> nums[i - 1] < nums[i] < nums[i + 1]
0 if -> None of prev conditions holds
'''
nums1, nums2, nums3 = [1, 2, 3], [2, 4, 6, 4], [3, 2, 1]
# res = 2, 1, 0


def sumOfBeauties(nums1):
    arr_min = []
    min_ = float('inf')
    pass


print(sumOfBeauties(nums1))

nums = [10, 5, 2, 6]
k = 100


def productLessThanK(nums, k):
    left, prod, res = 0, 1, 0
    # for i, r in enumerate(nums):
    for right in range(len(nums)):
        prod *= nums[right]
        while prod >= k and left <= right:
            prod /= nums[left]
            left += 1
        res += right - left + 1
    return res


print(productLessThanK(nums, 100))

# product of Array except self
nums = [1, 2, 3, 4]
# [24, 12, 8, 6]
nums2 = [-1, 1, 0, -3, 3]
# [0, 0, 9, 0, 0]


def productExceptSelf(nums):
    p = 1
    out = []
    for i in range(len(nums)):
        out.append(p)
        p *= nums[i]
    # return out, p
    p = 1
    for i in range(len(nums) - 1, -1, -1):
        out[i] = out[i] * p
        p *= nums[i]
    return out


def solution2(nums):
    res = [1] * len(nums)
    for i in range(1, len(nums)):
        res[i] = res[i - 1] * nums[i - 1]
    R = 1
    for i in range(len(nums) - 1, -1, -1):
        res[i] *= R
        R *= nums[i]
    return res


print(productExceptSelf(nums))
print(solution2(nums))

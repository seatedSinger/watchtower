# O(N^2) | O(1)
nums = [4, 2, 3, 4]


def validTriangle(nums):
    nums.sort()
    res = 0
    for i in range(len(nums)-1, 1, -1):
        L, R = 0, i - 1
        while L < R:
            if nums[L] + nums[R] > nums[i]:
                res += R - L
                R -= 1
            else:
                L += 1
    return res


print(validTriangle(nums))

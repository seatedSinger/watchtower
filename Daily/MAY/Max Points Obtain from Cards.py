nums = [1, 2, 3, 4, 5, 6, 1]
k = 3


def maxScore(nums, k):
    left = 0
    right = len(nums) - k
    total = sum(nums[right:])
    best = total
    for _ in range(k):
        total += nums[left] - nums[right]
        best = max(best, total)
        left += 1
        right += 1
    return best


print(maxScore(nums, k))


def solution2(nums, k):
    s = sum(nums[:k])
    res = s
    for i in range(1, k+1):
        s += nums[-i] - nums[k-i]
        res = max(res, s)
    return res

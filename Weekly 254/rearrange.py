# Like wiggle sort
def rearrange(nums):
    nums.sort()
    res = []
    l, r = 0, len(nums) - 1
    while len(res) != len(nums):
        res.append(nums[l])
        l += 1
        if l <= r:
            res.append(nums[r])
            r -= 1
    return res


def solution(nums):
    nums.sort()
    # Start Stop Step
    for i in range(1, len(nums), 2):
        nums[i], nums[i - 1] = nums[i - 1], nums[i]
    return nums


print(solution([1, 2, 3, 4, 5]))
print(rearrange([1, 2, 3, 4, 5]))

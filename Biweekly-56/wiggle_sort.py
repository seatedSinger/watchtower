# wiggle
nums = [3, 5, 2, 1, 6, 4]


def wiggleSort(nums):
    for i in range(1, len(nums)):
        should_swap = nums[i] < nums[i - 1] if i % 2 else nums[i] > nums[i - 1]
        if should_swap:
            nums[i], nums[i - 1] = nums[i - 1], nums[i]
    return nums

def solution2(nums):
    for i in range(1, len(nums)):
        if i % 2 and nums[i] <= nums[i - 1] or not i % 2 and nums[i] >= nums[i - 1]:
            nums[i], nums[i - 1] = nums[i - 1], nums[i]
    return nums


print(wiggleSort(nums))
# print(wiggleSort([1, 2, 3, 4]))
print(solution2(nums))
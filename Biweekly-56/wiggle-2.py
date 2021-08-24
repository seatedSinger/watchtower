# rev -> sort half -> low on left | high on right then wiggle

def wiggleSort2(nums):
    k = len(nums)//2
    nums.sort(reverse=True)
    nums[::2], nums[1::2] = nums[k:], nums[0:k]
    return nums


print(wiggleSort2([1, 3, 2, 2, 3, 1]))

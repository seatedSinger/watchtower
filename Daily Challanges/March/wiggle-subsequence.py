#TODO : THIS wiggle
def wiggle(nums):
    left, right, res = 1,1,1
    for i in range(1, len(nums)):
        left = right + 1 if nums[i] < nums[i-1] else left
        right = left + 1 if nums[i] > nums[i-1] else right
        res = max(res, left, right)
    return res


a = [1,7,4,9,2,5]
b = [1,17,5,10,13,15,10,5,16,8]
print(wiggle(a))
print(wiggle(b))

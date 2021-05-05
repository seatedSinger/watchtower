def increasingTriplets(nums):
    first = second = float('inf')
    for i in nums:
        if i <= first:
            first = i
        elif i <= second:
            second = i
        else:
            return True
    return False


nums = [1, 2, 3, 4, 5]
nums2 = [5, 4, 3, 2, 1]
print(increasingTriplets(nums))
print(increasingTriplets(nums2))

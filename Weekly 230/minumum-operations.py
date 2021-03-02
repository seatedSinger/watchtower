# Equal Sum Arrays With Minimum Number of Operations

from collections import Counter


def minOperations(nums1, nums2):
    sum1, sum2 = map(sum, (nums1, nums2))
    if sum1 == sum2:
        return 0
    elif sum1 > sum2:
        larger_sum, smaller_sum = nums1, nums2
    else:
        larger_sum, smaller_sum = nums2, nums1
    diff_sum = abs(sum1 - sum2)
    max_gains = [i - 1 for i in larger_sum]
    min_gains = [6 - i for i in smaller_sum]
    total_gains = max_gains + min_gains
    total_gains.sort(reverse=True)

    count = 0
    target_diff = diff_sum
    for i in range(len(total_gains)):
        target_diff -= total_gains[i]
        count += 1
        if target_diff <= 0:
            return count
    return -1


a = [1, 2, 3, 4, 5, 6]
b = [1, 1, 2, 2, 2, 2]
print(minOperations(a, b))

a = [1,1,1,1,1,1,1]
b = [6]
print(minOperations(a, b))

a = [6,6]
b = [1]
print(minOperations(a,b))

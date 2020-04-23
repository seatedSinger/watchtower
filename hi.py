# nums = 'ABChi hi'

# def sol2(nums):
#     count = 0
#     for i in range(len(nums)-1):
#         if nums[i:i+2] == 'hi':
#             count += 1
#     return count

# print(sol2(nums))
# nums = [3,6,1,0]

# def s_l(nums):
#     new_list = set(nums)
#     new_list.remove(max(new_list))
#     return max(new_list)

# print(s_l(nums))

# max_value = max(nums)
# m = max(item for item in nums if item != max_value)
# print(m)

# class Solution(object):
#     def dominantIndex(self, nums):
#         m = max(nums)
#         if all(m >= 2*x for x in nums if x != m):
#             return nums.index(m)
#         return -1

def in_sort(arr):
    for i in range(len(arr)):
        pos = i
        currentVal = arr[pos]

        while pos > 0 and arr[pos - 1] > currentVal:
            arr[pos] = arr[pos - 1]
            pos = pos - 1
        arr[pos] = currentVal
    return arr
arr = [9,21,4,66,7,88]
print(in_sort(arr))

arr = ["h","e","l","l","o"]

def rev(arr):
    pos = 0
    lenght = len(arr)-1

    while pos < lenght:
        pass
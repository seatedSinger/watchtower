'''
Taking two variables to record length of current ascend and descend
of wiggle sub
Possibilities : if nums[i] > nums[i - 1] then nums[i] is END of ancend Wiggle

- Length of wiggle seq, END in +ve, -ve difference
- Scanning from 2nd to last number
- difference is +ve, concatenate with -ve prefix wiggle subseq
- difference if -ve, concatenate with +ve prefix wiggle subseq
- return longest length of wiggle subseq
'''
def wiggle(nums):
    left, right, res = 1, 1, 1
    for i in range(1, len(nums)):
        left = right + 1 if nums[i] < nums[i-1] else left
        right = left + 1 if nums[i] > nums[i-1] else right
        res = max(res, left, right)
    return res


a = [1, 7, 4, 9, 2, 5]
b = [1, 17, 5, 10, 13, 15, 10, 5, 16, 8]
c = [1, 2, 3, 4]
print(wiggle(a))
print(wiggle(b))
print(wiggle(c))


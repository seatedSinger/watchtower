'''
it = iter(nums) # important and working of next
'''

def arrayPairSum(nums):
    # nums.sort()
    # it = iter(nums)
    # res = 0
    # for x in it:
    #     res += (min(x, next(it)))
    # return res
    # return sum(sorted(nums)[::2])
    print(sorted(nums)[::2])

# print(arrayPairSum([1, 4, 3, 2]))
print(arrayPairSum([6, 2, 6, 5, 1, 2])) # 9 # [1,2,2,5,6]

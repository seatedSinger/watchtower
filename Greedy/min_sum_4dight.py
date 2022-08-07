'''
2160. Minimum Sum of Four Digit Number After Splitting Digits
1. FOUR digits only
Simply, in 4 digits we need to get min pair sum
'''

def minimumSum(num):
    # a, b, c ,d = sorted(str(num))
    # return int(a + c), int(b + d)
    num = sorted(str(num),reverse=True)
    n = len(num)    
    res = 0
    even_iteration = False
    position = 0
    for i in range(n):
        res += int(num[i])*(10**position)
        if even_iteration:
            position += 1
            even_iteration = False
        else:
            even_iteration = True
    return res


print(minimumSum(29325))
# print(minimumSum(4009))

'''
def solution_2(nums):
    a = sorted(str(num))
    return int(a[0] + a[2]) + int(a[1] + a[3])
'''

# s = 'abcabc'


# def favouriteSubsequence(s):
#     # mod = 1e9 + 7
#     an, bn, cn = 0, 0, 0
#     for i in range(len(s)):
#         if s[i] == 'a':
#             an = 1 + 2 * an
#             # print(an)
#         elif s[i] == 'b':
#             bn = an + 2 * bn
#             # print(bn)
#         elif s[i] == 'c':
#             cn = bn + 2 * cn
#             # print(cn)
#     return cn

# def newSol(s):
#     pass

# print(favouriteSubsequence)
nums = [10, 5, 2, 6]
k = 100


def productLessThanK(nums, k):
    left, prod, res = 0, 1, 0
    # for i, r in enumerate(nums):
    for right in range(len(nums)):
        prod *= nums[right]
        while prod >= k and left <= right:
            prod /= nums[left]
            left += 1
        res += right - left + 1
    return res


print(productLessThanK(nums, 100))
print(productLessThanK(nums))
print(productLessThanK(nums))

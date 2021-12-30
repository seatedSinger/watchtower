nums = [10, 5, 2, 6]
k = 100

def solution(nums, k):
    prod, res = 1, 0
    L = 0
    for R in range(len(nums)):
        prod *= nums[R]
        # print(prod)
        while prod >= k and L <= R:
            prod //= nums[L]
            L += 1
        res += R - L + 1
    return res


print(solution(nums, k))

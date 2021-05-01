# O(KN) | O(k)

prices = [2, 4, 1]
k = 2
prices2 = [3, 2, 6, 5, 0, 3]


def maxProfit(prices, k):
    b = [float('inf')] * (k + 1)
    s = [0] * (k + 1)
    print(b, s)
    for p in prices:
        for k in range(1, k + 1):
            b[k] = min(b[k], p - s[k - 1])
            s[k] = max(s[k], p - b[k])
    return s


# print(maxProfit(prices2, k))
# print(maxProfit(prices, 2))

def solution(prices, k):
    dp = [[0] * len(prices) for _ in range(k + 1)]
    for i in range(1, k + 1):
        prev = dp[i - 1][0] - prices[0]
        for j in range(1, len(prices)):
            dp[i][j] = max(dp[i][j - 1], prev + prices[j])
            # print(dp[i][j])
            prev = max(prev, dp[i - 1][j] - prices[j])
            # print(prev)
    return dp[-1][-1]


print(solution(prices, 2))

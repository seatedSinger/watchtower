def maxProfit(prices):
    lowest_soFar = float('inf')
    res = 0
    for i in prices:
        if i <= lowest_soFar:
            lowest_soFar = i
            # print(lowest_soFar)
        res = max(res, i - lowest_soFar)
        # * lowest_soFar = min(lowest_soFar, i)
    return res


def solution2(prices):
    if len(prices) < 1:
        return 0
    max_profit = 0
    min_profit = prices[0]

    for i in range(1, len(prices)):
        if prices[i] < min_profit:
            min_profit = prices[i]
        else:
            max_profit = max(max_profit, prices[i]-min_profit)
    return max_profit


a = [7, 1, 5, 3, 6, 4]
b = [7, 6, 4, 3, 1]
print(maxProfit(a))
print(maxProfit(b))
print(solution2(a))
print(solution2(b))

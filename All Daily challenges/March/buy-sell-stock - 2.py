'''
Need to sell the stock before buying again
keep resetting min_soFar
single pass peak
'''
def maxProfit(prices):
    res = 0
    # ans  = []
    for i in range(1, len(prices)):
        res += max(0,prices[i] - prices[i-1])
        # ans.append((prices[i] - prices[i-1]))
    return res
    # print(ans)

def solution2(prices):
    # max_profit = 0
    res = []
    min_profit = prices[0]
    for i in range(1, len(prices)):
        if prices[i] < min_profit:
            min_profit = prices[i]
        else:
            res.append((prices[i]-min_profit))
            min_profit = prices[i]
    return sum(res)


a = [7,1,5,3,6,4]
print(maxProfit(a))
print(solution2(a))

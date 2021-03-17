'''
Need to sell the stock before buying again
keep resetting min_soFar
'''
def maxProfit(prices):
    res = 0
    for i in range(1, len(prices)):
        res += max(0,prices[i] - prices[i-1])
    return res


print(maxProfit([7,1,5,3,6,4]))

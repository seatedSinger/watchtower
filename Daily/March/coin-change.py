# O(n * k), n = no. of coins | k = amount of money
'''
F(n) = F(n-1) + F(n-3) + F(n-5) + F(n-10)
'''

def coinChange(coins, amount):
    dp = [float('inf') for i in range(amount+1)]
    dp[0] = 0
    for i in range(1, amount+1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i-coin] + 1)
    if dp[-1] == float('inf'):
        return -1
    return dp,dp[-1]

def solution2(coins, amount):
    pass

# TODO : Add bottom up | Top down variations

print(coinChange([1,2,5],11))

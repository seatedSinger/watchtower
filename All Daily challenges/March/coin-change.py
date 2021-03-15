# F(n) = F(n-1) + F(n-3) + F(n-5) + F(n-10)

def coinChange(coins, amount):
    dp = [0] + [float('inf') for i in range(amount)]
    for i in range(1, amount+1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i-coin] + 1)
    if dp[-1] == float('inf'):
        return -1

def second(coins, amount):
    dp1 = [0] + [float('inf') for i in range(amount)]
    for i in range(1, amount + 2):
        for coin in coins:
            if i - coin >= 0:
                pass

#TODO : Add bottom up | Top down variations


print(coinChange([1,2,5],11))

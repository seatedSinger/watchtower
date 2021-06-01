# Need to reset after complition of each transaction
# O(n) | O(1)


def maxProfit(prices):
    minSoFar = minSoFar2 = float('inf')
    # Infinitely large +ve value
    one_profit = two_profit = 0
    for p in prices:
        minSoFar = min(minSoFar, p)
        one_profit = max(one_profit, p - minSoFar)
        minSoFar2 = min(minSoFar2, p - one_profit)
        two_profit = max(two_profit, p - minSoFar2)
    return two_profit


def solution2(prices):
    hold1, hold2 = float("-inf"), float("-inf")
    release1, release2 = 0, 0
    for i in prices:
        release1 = max(release1, hold1 + i)
        hold1 = max(hold1, -i)
        release2 = max(release2, hold2 + i)
        hold2 = max(hold2, release1 - i)
    return release2


a = [3, 3, 5, 0, 0, 3, 1, 4]
b = [1, 2, 3, 4, 5]
c = [7, 6, 4, 3, 1]
print(maxProfit(a))
print(maxProfit(b))
print(maxProfit(c))

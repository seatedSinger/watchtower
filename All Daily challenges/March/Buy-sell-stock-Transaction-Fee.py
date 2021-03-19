def maxProfit(prices, fee):
    pass

'''
First try using a recursive Top Down approach to get max profit.
Then try drawing the recursion tree on paper to figure out sub-problems that can be cached in a table.
Then look at the key/values that the recursion is setting in the table (cache) and under what conditions.
Next develop a bottoms-up DP solution that builds the table mentioned above directly by watching the recursion tree for which values got calculated first, which got done next.
After doing this you'll notice that you're wasting space by using a table because to calculate the next state you only need 2 variables.
When you change the code to use 2 variables, you'll land up with this solution.
'''
prices = [1,3,2,8,4,9]
fee = 2
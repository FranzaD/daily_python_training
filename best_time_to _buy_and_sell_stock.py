# Leetcode Question 27: Best Time to Buy and Sell Stock
# Solved: 
# Big O Notation: O(n) runtime
# Easy
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

# Learned:

max_profit = 0
# each buy day in prices is then compared to each sell day
for buy_day in range(0, len(prices)):
    # bounds ensure the sell days are only after buy days (to avoid unnecessary operations)
    # Ending is inclusive of the last day/index of the prices list
    for sell_day in range(buy_day+1, len(prices)):
        # if difference between buy and sell day is >= 0 then remember that is the max profit found
        profit = prices[sell_day] - prices[buy_day]
        if profit >= max_profit:
            max_profit = profit
# the largest max profit found after all comparisons gets returned
print(max_profit)
# Leetcode Question 27: Best Time to Buy and Sell Stock
# Solved: 8/14/2026
# Big O Notation: O(n) runtime
# Easy
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

# Learned: Seek out the best so far and run comparisons along with obtaining those values. 

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        minimum_price = prices[0]
        
        for current_price in prices:
            if current_price <= minimum_price:
                minimum_price = current_price 
            
            profit = current_price - minimum_price
            
            if profit >= max_profit:
                max_profit = profit
        
        return max_profit
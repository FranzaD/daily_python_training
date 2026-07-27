# Leetcode Question 14: Sqrt(x)
# Solved: 7/27/2026
# Big O Notation: O(log n) runtime since binary search is used here
# Easy
# https://leetcode.com/problems/sqrtx/description/

# Learned: refresher on binary search. floor division, and refining bounds of a loop for precision

# solution passes some test cases but not most cases
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        low = 0
        high = x
        #use floor operator since we need an integer and we cant assume provided x is a perfect square
        mid = (low + high)//2

        # iterate until 
        while low <= high:
            if mid*mid == x:
                return mid
            # if mid overshot x then high needs to be adjusted down
            elif mid*mid > x:
                # we need to adjust the high value so it's slightly lower than mid
                high = mid - 1
                # ensure the mid is an integer with floor division
                mid = (low + high)//2
            # if mid undershot x then low needs to be adjusted up
            elif mid*mid < x:
                # we need to adjust the low value so it's slightly higher than mid
                low = mid + 1
                # ensure the mid is an integer with floor division
                mid = (low + high)//2

        # mid must be the square root if loop is finished
        return mid
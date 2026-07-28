# Leetcode Question 15: Climbing Stairs
# Solved: 7/28/2026
# Big O Notation: O(n) runtime 
# Easy
# https://leetcode.com/problems/climbing-stairs/description/

# Learned: Refreshed Fibonacci sequence, and this was the first taste of dynamic programming

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        prior_steps = 2
        prior_prior_steps = 1
        steps = 3

        # returns values for base cases
        if n == 1:
            return prior_prior_steps
        elif n == 2:
            return prior_steps
        
        # for calculates the current steps while setting up vairables for counting the next
        while steps <= n:
            current_steps = prior_steps + prior_prior_steps
            prior_prior_steps = prior_steps
            prior_steps = current_steps
            steps += 1

        # if loop exits then steps = n
        return current_steps
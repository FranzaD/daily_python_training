# Leetcode Question 14: Sqrt(x)
# Solved: 
# Big O Notation: O() runtime  
# Easy
# https://leetcode.com/problems/sqrtx/description/

# Learned:

# solution passes some test cases but not most cases
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        low = 0
        high = x
        mid = (low + high)//2
        previous_value = 0

        # loop until x is equal to the mid value squared, loop ends only when square root has been found
        while mid*mid != x and previous_value != mid:
            # if mid overshot x then high needs to be adjusted down
            if mid*mid > x:
                high = mid
                # ensure the mid is an integer with floor division
                mid = (low + high)//2
            # if mid undershot x then low needs to be adjusted up
            elif mid*mid < x:
                low = mid
                # ensure the mid is an integer with floor division
                mid = (low + high)//2

            # if close enough integer found the loop convergences on a solution into infinity so I need to stop it if the value found in the former iteration = value in the current iteration
            previous_value = mid

        # mid must be the square root if loop is finished
        return mid
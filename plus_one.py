# Leetcode Question 12: Plus One
# Solved: 7/23/2026
# Big O Notation: O(n) runtime  
# Easy
# https://leetcode.com/problems/plus-one/description/

# Learned: Reinforced iterating backwards through a list and using .extend() for the first time

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # iterate backwards through the array making necessary adjustments and iterating only as far back as necessary
        for i in range(-1, -(len(digits) + 1),-1):
            # for adjusting lists where last digit is not nine
            if digits[i] != 9:
                digits[i] +=1
                return digits
            # when iterating backwards and needing to increment a digit at a higher place turn 9s into zeros until first non-nine digit is found
            elif digits[i] == 9:
                digits[i] = 0
        # if exited the for loop array must be [0,0,0,0] and needs to be extended by one element and the leading element changed to 1
        digits.insert(0, 1)
        return digits
# Leetcode Question 2: Palindrome
# Solved: 7/10/2026 
# Big O Notation: O(log(n)) time
# Easy
# https://leetcode.com/problems/palindrome-number/

# reviewed modulo operation, also learned about the floor division operator // which returns the largest integer less than or equal to the result of the division.
# I also determined that subtracting the modulo from the result and dividing by 10 is another way of getting the floor of the division of a number by 10, which is useful for removing the last digit of a number.
# now tomorrow I'm going to determine how to use these operations in a loop to compare digits for determining if a number is a palindrome.

#Learned:
# reviewed modulo operation, array operations such as reverse() and append().
# Equating two arrays in python just points two variables at the same array, it does not make a copy!
# learned about break statements and if statements in python.
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        #declares both arrays for usage
        original_seq = []
        reversed_seq = []

        # since a palindrome can never be negative
        if x < 0:
            return False
        
        # reverse the number, store in array for comparison
        while True:
                last_digit = x % 10
                x = x//10
                reversed_seq.append(last_digit)
                if x == 0:
                    break 

        #copy over reversed array
        original_seq = list(reversed_seq)

        # reverses the reversed array so original order is re-established
        original_seq.reverse()

        #now conduct comparison
        if original_seq == reversed_seq:
            return True
        
        return False 
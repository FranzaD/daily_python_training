# Leetcode Question 3: Roman to Integer
# Solved: 
# Big O Notation: O(n) runtime
# Easy
# https://leetcode.com/problems/roman-to-integer/

#need to handle the case XIV, must redo logic in loop! - overcomplicated the logic in the loop, need to keep it simple 

# learned that looping should be kept as simple as possible
# also review basic arithmetic operations in python
# got better at running through test cases to refine logic
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # integer that will be a running sum 
        integer = 0

        # create a dictionary that assigns values to each roman numeral to conduct comparisons
        roman_numerals = {"I": 1,"V": 5,"X": 10,"L": 50,"C": 100,"D": 500,"M": 1000}
        
        # iterates through roman numeral to determine integer
        for i in range(len(s)-1):
            # assuming numerals are running largest to smallest
            if roman_numerals[s[i]] >= roman_numerals[s[i+1]]:
                integer += roman_numerals[s[i]]

            # if there's a smaller value numeral leading then there needs to be a different operation
            else:    
                integer -= roman_numerals[s[i]]
        
        # adding the last character's value
        integer += roman_numerals[s[len(s) - 1]]
        
        return integer
        
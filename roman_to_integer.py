# Leetcode Question 3: Roman to Integer
# Solved: 
# Big O Notation: O() time
# Easy
# https://leetcode.com/problems/roman-to-integer/

#need to handle the case XIV, must redo logic in loop!

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # integer that will be a running sum 
        integer = 0

        # create a dictionary that assigns values to each roman numeral to conduct comparisons
        roman_numerals = {"I": 1,"V": 5,"X": 10,"L": 50,"C": 100,"D": 500,"M": 1000,}
        
        # accesses the value of the character at position i
        #roman_numerals[s[i]]
        
        # to check the value of the next character
        #roman_numerals[s[i+1]]

        # iterates through roman numeral to determine integer
        for i in range(len(s)-1):
            # assuming numerals are running largest to smallest
            if roman_numerals[s[i]] > roman_numerals[s[i+1]]:
                integer += roman_numerals[s[i]]
                integer += roman_numerals[s[i+1]]

            # if there's a smaller value numeral leading then there needs to be a different operation
            else:    
                integer += roman_numerals[s[i+1]] - roman_numerals[s[i]]
        
        # add the last integer that got skipped in the comparison loop
        #integer += roman_numerals[s[len(s)]]
        
        return integer

        # when a lesser character is placed before a larger character it indicates subtraction
        # order matters here, so before for loop maybe check to make sure characters are in increasing order?
        # how to make it so characters have an order?

        # if we are working with a string that means it already has an index
        # could create a dict where the  indices are the values, and the roman numeral characters are the keys
        # then check, given this roman numeral, it's index and the other roman numeral and it's index are they in the order largest to smallest? No...there's got to be a better way


        
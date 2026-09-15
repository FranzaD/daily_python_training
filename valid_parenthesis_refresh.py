# Leetcode Question 5: Valid Parentheses
# Solved: 
# Big O Notation: O() 
# # Easy
# https://leetcode.com/problems/valid-parentheses/description/

# attempted 9/14 - 9/15
# refreshing stacks

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dict = {")":"(", "]":"[", "}":"{"}
        #list
        stack = []
        #if string is size 1 or less
        if len(s) <= 1:
            return False

        for char in s:
            if char == "(" or char == "[" or char == "{":
                stack.append(char)
            if char is ")" or "]" or"}":
                if stack.peek(char) is dict[char]:
                    continue
                else:
                    return False
        return True

# Leetcode Question 9: Find the Index of the First Occurrence in a String
# Solved: 
# Big O Notation: O() runtime 
# Easy
# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

# Learned:

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # iterate through each character in string
        for char1 in haystack:
            # iterate through each 
            for char2 in needle:
                if char1 == char2:
                    return char1
        
        return -1

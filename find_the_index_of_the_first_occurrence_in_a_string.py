# Leetcode Question 9: Find the Index of the First Occurrence in a String
# Solved: 
# Big O Notation: O(n*m) runtime when n is the outer loop and m is the inner loop input 
# Easy
# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

# Learned: Reminded of the use of flags and altering the range for a for loop to maximize efficiency

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in range(len(haystack)-len(needle)+1):
            index_found = True
            for j in range(len(needle)):
                if haystack[i+j] != needle[j]:
                    index_found = False
                    break
            if index_found:
                return i
        return -1

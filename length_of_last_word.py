# Leetcode Question 11: Length of Last Word
# Solved: 7/22/2026
# Big O Notation: O(n) runtime  
# Easy
# https://leetcode.com/problems/length-of-last-word/description/

# Learned: It's possible to iterate through a string from the back! 

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        found_word = False
        word_counter = 0

        for i in range(len(s)-1,-1, -1):
            if s[i] != ' ':
                found_word = True
                word_counter += 1
            
            if found_word and s[i] == ' ':
                return word_counter
        
        return word_counter
# Leetcode Question 4: Longest Common Prefix
# Solved: 
# Big O Notation: O() runtime
# Easy
# https://leetcode.com/problems/longest-common-prefix/description/

#initial attempt, overcomplicated logic
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        temp_common_longest_prefix = []
        longest_common_prefix = []

        # first string gets copied over to new list to compare all other strings to it
        longest_common_prefix = [strs[0]]

        #iterate through each string string in the array of strings
        for string in strs:
            # need to make sure it does run through checking the first string against itself
            if common_longest_prefix == strs[0]:
                #skip the following for loop since no need to check the same value against itself
                continue 

                # so this for loop should start when string = 1 and char_index = 0
                # checks the characters against eachother from the list to the array of lists
                for char_index in longest_common_prefix: 

                    # compare characters from one string to another
                    if longest_common_prefix[char_index] != string[char_index]:
                        temp_common_longest_prefix = longest_common_prefix[:char_index]

        return temp_common_longest_prefix
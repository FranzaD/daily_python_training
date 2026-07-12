# Leetcode Question 4: Longest Common Prefix
# Solved: 7/12/2026
# Big O Notation: O(n* m) runtime (where n = number of strings, and m is the length of the smallest string in the list)
# Easy
# https://leetcode.com/problems/longest-common-prefix/description/

# What is the difference in python between list, array, and string?
# A list is a data structure, dynamic, resizable and can store different data types
# An Array in Python is usually just a list, although a numpy.array is th emore efficient data structrue that you remember from C++
# a string is a sequence of characters, immutable, and can be indexed and sliced.

# Learned about the slicing operation for strings and lists in python. The slicing operation allows you to get a subset of a string or list by specifying a start and end index. For example, `my_string[1:4]` would return the substring from index 1 to index 3 (4 is exclusive). Similarly, `my_list[2:5]` would return the elements from index 2 to index 4.

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        #this will be the baseline for comparisons
        reference_word = strs[0]

        # string to hold longest common prefix 
        common_longest_prefix = ""
        
        # stop value, integer
        smallest_string = len(strs[0])

        # finds the smallest word's length in strs
        for word in strs:
            if len(word) < smallest_string:
                smallest_string = len(word) 

        # iterates over the smallest number of characters necessary
        for char_index in range(smallest_string):
            
            # iterates over each word in strs and seeks mismatch
            for word in strs:

                # if the first letter doesnt match return nothing
                if reference_word[char_index] != word[char_index]:
                    
                    # when character's dont match get prefix up to and excluding the last index where a mismatch was found
                    # char index is the stopping index, exlcuded, 
                    common_longest_prefix = reference_word[:char_index]
                    return common_longest_prefix

            # if characters do match then slice segment into common_longest prefix
            # ending is exclusive, if loop got to this point the end needs to be inclusive
            common_longest_prefix = reference_word[:char_index + 1]
    
        # return the reference_word since all word must match for loop to end
        return common_longest_prefix                             
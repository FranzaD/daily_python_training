# Leetcode Question 13: Add Binary
# Solved: 7/26/2026
# Big O Notation: O(n) runtime  
# Easy
# https://leetcode.com/problems/add-binary/description/

# Learned: reminded that string are immutable in python! Also refreshed binary addition logic and was reminded that strings can be initialized as empty (without a space)
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # result string starts with blank space that can be trimmed off at the end with splice()
        result = ""
        carry = 0
        total = 0

        # get strings to be the same size so I dont get an index error in the loop when accessing an index teh smaller string doesn't have
        #determine how many zeros characters to append to the smaller string and append
        size_difference = abs(len(a)-len(b))
        zeros_substring = "0" * size_difference
        if len(a) < len(b):
            a = zeros_substring + a
        else:
            b = zeros_substring + b

        # loop that will compare characters in string a and b
        for i in range(-1, -(len(a)+1), -1):
            # convert strings into integers to calculate total that dictates behavior
            if a[i] == "1":
                total += 1
            if  b[i] == "1":
                total += 1
            if carry == 1:
                total += 1
            
            # inserts correct character into result string based on total
            # indexing result is actually unnecessary (and not possible), appending is enough
            if total == 0:
                result = "0" + result
            if total == 1:
                result = "1" + result
                # after insertion carry can go back to 0
                carry = 0
            if total == 2:
                result = "0" + result
                carry = 1
            if total == 3:
                result = "1" + result
                carry = 1
                # but when should carry be reset? When total = 1 it can be reset

            # reset total for the next comparison(iteration of the loop)
            total = 0

        # loop exited, only thing left to add to the front would be the carry if it has a 1
        if carry == 1:
            result = "1" + result
            return result
        else:
            # carry = 0, just return result string
            return result

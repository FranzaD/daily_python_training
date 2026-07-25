# Leetcode Question 13: Add Binary
# Solved: 
# Big O Notation: O() runtime  
# Easy
# https://leetcode.com/problems/add-binary/description/

# Learned: reminded that string are immutable in python!

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result = a + b
        result_length = 0

        #have carry string assigned just enough zeros to help with the binary addition?
        for i in result:
            carry_string = "0"

        # loop that will compare characters in string a and b and correctly format the result string that will br returned.
        for i in range(-1, -len(result), -1):
            if a[i] != b[i]:
                result[i] = 1
                result_length += 1
            elif a[i] == b[i] == 0:
                result[i] = 0
                result_length += 1
            elif a[i] == b[i] == 1:
                result[i] = 0
                result[i-1] = 1
                # but this means that the next place already has a value in it, does that need to be taken into account in the next iteration of the loop? That a previous one was carried over?

                # or maybe it makes sense to have a carry array, that is originally all zeros, but then carries ones in the right places that way the one that is carried doesnt get overrided.
                result_length += 2
                
        #by the time the loop is over slice off the leading zeros that don't match the result length calculated and return the string
        return result

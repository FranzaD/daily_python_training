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
        # result string starts with blank space that can be trimmed off at the end with splice()
        result = " "
        carry_digit = 0
        total_sum = 0

        # loop that will compare characters in string a and b and a carry digit and correctly format the result string that will br returned.
        for i in range(-1, -len(result), -1):
            #sum characters in strings...but they're characters, not digits.
            # calculate total
            if a[i] == "1":
                total += 1
            if  b[i] == "1":
                total += 1
            if carry == 1:
                total += 1

            # a and b are alternating
            if total == 0:
                result[i] = "0"
            #
            if total == 1:
                result[i] = "1"
            if total == 2:
                result[i] = "1"
                carry = 1
            if total == 3:
                result[i] = "1"
                carry = 1
                # but when should carry be reset?

        return result


# Leetcode Question 5: Valid Parentheses
# Solved: 
# Big O Notation: O() 
# # Easy
# https://leetcode.com/problems/valid-parentheses/description/

# Stack: LIFO - Last In First Out 
    # push add item to the top item
    # pop remove and return the top item

# Queue: FIFO - First In, First Out
    # adding happens in the back
    # removing happens at the front

# Learned that I don't need to rethink the whole logic, just try to add the simpliest solution first and build little by little fo reach test case that fails.
# first leetcode solution I troubleshot without feedback from Claude! Took longer than expected but working through each failed test case and rerunning the code to see which cases passed help me stay on track
# one change in the logic = rerun test cases again. Don't change a bunch of logic at once, just one change at a time and rerun test cases to see if it passes or fails. If it fails, then I know the change I made is wrong and I can revert back to the previous version of the code.
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dict = { ')': '(', ']': '[', '}': '{' }
        
        # this is a list
        stack = []
        # s is a string, so index is the character/bracket itself
        # for loop should end when string is empty, right? unless i should use range
        for bracket in s:
            # if bracket is open, push into stack
            if bracket == '(' or bracket == '{' or bracket == '[':
                stack.append(bracket)

            # if bracket is closed, check top of stack for matching open bracket
            # if match found,  pop open bracket from stack
            # if match not found return false
            # so that the stack doesn't get accessed if it's empty

            if bracket == ')' or bracket == '}' or bracket == ']':
                if stack != []:
                    # is the last element in stack an open bracket? if so then pop off stack
                    if stack[-1] ==  dict[bracket]:
                        stack.pop()
                    # bracket mismatch
                    else: 
                        return False 
                # closing bracket and stack is empty
                else: 
                    return False 

        #if all parantheses had pairs by the end of the for loop it should be empty, otherwise false
        if stack == []:
            return True
        return False
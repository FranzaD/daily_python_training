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
            if bracket == ')' or bracket == '}' or bracket == ']':
                # is the last element in stack an open bracket? if so then pop off stack
                if stack[-1] ==  dict[bracket]:
                    stack.pop()

                # since the open bracket and closing bracket don't match the input string is invalid
                #return False

        #if all parantheses had pairs by the end of the for loop it should be empty, otherwise false
        if stack == []:
            return True
        return False
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

dict = { ')': '(', ']': '[', '}': '{' }

stack = []

# I think this works for the first test case, but it definitely doesn't work for the others
for char in s:
    stack.append(char)
    if char == dict[char]:
        stack.pop(char)
        if len(stack) == 0:
            return True

 


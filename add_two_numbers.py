# Leetcode Question 32: Add Two Numbers
# Solved: 8/18/2026
# Big O Notation: O(n) runtime, O(n) space complexity since the new linkedlist grows propoertionally to the size of the input linked lists. 
# Medium
# https://leetcode.com/problems/add-two-numbers/description/

# Learned: Python evaluates and before or in conditional statements. Reviewed how to create a new object from a class, iterating through a linked list
# and learned that this amount of if statements isn't necessarily an indicator of a poor logical foundation for the solution but rather represents the complexity of the problem.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        l3 = ListNode(val = 0, next = None)
        curr1 = l1
        curr2 = l2
        curr3 = l3
        carry = 0
        
        #iterate through each linked list, taking the sum and assigning the correct digit 
        while curr1 is not None or curr2 is not None or carry != 0:
            # sum .val if current node exists
            if curr1 is not None:
                curr3.val += curr1.val
            # sum .val if current node exists
            if curr2 is not None:
                curr3.val += curr2.val
            # always add in the carry
            curr3.val += carry

            # reset carry onces it's been taken into account in the sum
            carry = 0

            #if value is two digits then I need to carry the next digit over
            if curr3.val > 9:
                carry =  curr3.val // 10
                curr3.val = curr3.val % 10
            
            # move current pointers to whatever next is point to
            if curr1 is not None:
                curr1 = curr1.next
            if curr2 is not None:
                curr2 = curr2.next

            # only create another node if there is another digit to add in from l1, l2, or carry
            if curr1 is not None or curr2 is not None or carry != 0:
                curr3.next = ListNode(val=0, next=None)
                curr3 = curr3.next
        
        # once loop completes sum should be complete?
        return l3
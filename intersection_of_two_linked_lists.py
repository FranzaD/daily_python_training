# Leetcode Question 33: Intersection of Two Linked Lists
# Solved: 
# Big O Notation: O(max(m, n) runtime, O(n) space complexity  
# Easy
# https://leetcode.com/problems/intersection-of-two-linked-lists/

# Learned:

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        currA = headA
        currB = headB
    
        # iterate until intersection found, if at end of linkedlists then return no intersection found
        while currA is not currB:
            # only iterate if either current pointer is not at the end of their respective linkedlist
            if currA is not None:
                currA = currA.next
            if currB is not None:
                currB = currB.next
            
            return "No Intersection"

        # if loop exited then intersection found
        return f"Intesected at {currA.val}"
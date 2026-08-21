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
        while currA is not None:
            while currB is not None:
                # check if current pointers are at the same node
                if currA is currB:
                    return currA
                
                # iterate to the next node
                currB = currB.next
            
            # reset currB to the beginning of the list
            currB = headB
            # iterate to next node to run compare all of listB to
            currA = currA.next
        
        # at loop exit then currA has checked every node against listB and there is no intersection
        return currA
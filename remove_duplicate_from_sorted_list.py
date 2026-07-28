# Leetcode Question 16: Remove Duplicate from Sorted List
# Solved: 
# Big O Notation: O() runtime 
# Easy
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/

# Learned:

#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        current_node = head

        while current_node is not None and current_node.next is not None:
            if current_node.val == current_node.next.val:
                current_node.next = current_node.next.next
                if current_node.val == current_node.next.val:
                    
            current_node = current_node.next

        return head
    # I either need to reevaluate the stopping condition, implement a secondary pointer for 
    # moving through the linked list to help current with comparisions or rewrite the logic since it keps going out of bounds
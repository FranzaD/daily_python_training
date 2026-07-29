# Leetcode Question 16: Remove Duplicate from Sorted List
# Solved: 7/29/2026
# Big O Notation: O(n) runtime 
# Easy
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/

# Learned: Refreshed using else instead of elif, else doesn't require a condition and it's when you want one or the other code snippet to run not both potentially
# - Using a secondary pointer helps in comparing adjacent nodes without losing track of the current node.
# - Always check for None before accessing attributes to avoid runtime errors.

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
        # don't even assign pointers if head is none
        if head is None:
            return head
        else:
            current_node = head
            compare_node = head.next

        while compare_node is not None and head is not None:
            # if adjacent nodes are different, drop the duplicate node
            if current_node.val == compare_node.val:
                current_node.next = compare_node.next
                # drops the duplicate node
                compare_node = current_node.next
                
            # if adjacent nodes are in different iterate along
            else:
                compare_node = compare_node.next        
                current_node = current_node.next

        return head
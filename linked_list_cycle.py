# Leetcode Question 30: Linked List Cycle
# Solved: 8/16/2026
# Big O Notation: O(n) time, O(1) space
# Easy
# https://leetcode.com/problems/linked-list-cycle/description/

# Learned: tortoise and hare technique, using two pointers to traverse a linked list at different speeds to determine if a cycle exists. If the fast pointer (hare) ever meets the slow pointer (tortoise), then a cycle exists in the linked list. If the fast pointer reaches the end of the list (None), then no cycle exists.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow_pointer = head
        fast_pointer = head

        # if head has no node then no cycle exists because no linkedlist exists
        if head is None:
            return False
        # isn't there a risk of fast_pointer going out of bounds?
        # yes it does go out of bounds..
        while fast_pointer.next is not None and fast_pointer.next.next is not None:
            fast_pointer = fast_pointer.next.next
            slow_pointer  = slow_pointer.next

            # if fast_pointer every catches up to slow pointer, cycle exists 
            if fast_pointer == slow_pointer:
                return True
        
        #if fast_pointer is none, linked list is not a cycle 
        return False
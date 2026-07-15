# Leetcode Question 6: Merge Two Sorted Lists
# Solved: 
# Big O Notation: O() runtime 
# Easy
# https://leetcode.com/problems/merge-two-sorted-lists/description/


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        current1 = list1
        current2 = list2
        list3 = list1

        while current1 is not None and current2 is not None:
            # if values are equal chain to list3
            if current1.value == current2.value:
                #move current to next node
                current1 = current1.next
                #attache node to equal node
                list3.next = current2
                
                current2.next = current1.next
                current1.next = current2
                
            
            if current1.value > current2.value:
                current2.next = current1

            if current1.value < current2.value:
                current1.next = current2

        current1 = list1.next
        current2 = list2.next
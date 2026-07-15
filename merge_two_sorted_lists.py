# Leetcode Question 6: Merge Two Sorted Lists
# Solved: 7/15/2026
# Big O Notation: O() runtime 
# Easy
# https://leetcode.com/problems/merge-two-sorted-lists/description/


# Definition for singly-linked list.
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
        list3 = ListNode()
        tail = list3

        while current1 is not None and current2 is not None:
            # if values are equal default to chaining list1 into list 3 first then list2
            if current1.val == current2.val:
                tail.next = current1
                tail = tail.next
                current1 = current1.next
                tail.next = current2
                tail = tail.next
                current2 = current2.next

            # if list 1 value is less than list 2 value
            elif current1.val < current2.val:
                tail.next = current1
                tail = tail.next
                current1 = current1.next
            
            # if list 1 value is greater than list 2 value
            elif current1.val > current2.val:
                tail.next = current2
                tail = tail.next
                current2 = current2.next
        
        # if there is a list with remaining nodes then since it's already order I can just append it to the end of list 3
        if current1 is None:
            tail.next = current2

        if current2 is None:
            tail.next = current1

        # now that lists are spliced together in order then delete the dummy node
        # so output doesn't include a leading null element
        tail = list3
        list3 = tail.next
        return list3
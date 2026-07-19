# Leetcode Question 8: Remove Element
# Solved: 7/18/2026
# Big O Notation: O(n) runtime 
# Easy
# https://leetcode.com/problems/remove-element/description/

# Learned: that I can use an simple else statement if there is only one other alternative option that I'm checking

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        read = 0
        write = 0

        while read != len(nums):
            if nums[read] == val:
                read+=1
            #elif nums[read] != val:
            else:
                nums[write] = nums[read]
                read +=1
                write +=1
        
        return write
            
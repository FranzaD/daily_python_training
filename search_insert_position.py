# Leetcode Question 10: Search Insert Position
# Solved: 
# Big O Notation: O(logn)
# Easy
# https://leetcode.com/problems/search-insert-position/description/

# Learned:

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            elif target <= 0:
                return 0
            elif target > nums[len(nums)-1]:
                return len(nums)
            elif nums[i-1] < target < nums[i+1]:
                return i
# Leetcode Question 10: Search Insert Position
# Solved: 7/21/2026
# Big O Notation: O(logn) runtime since binary search is O(logn)  
# Easy
# https://leetcode.com/problems/search-insert-position/description/

# Learned: reintroduced to binary search using an array (not trees), very tedious logic to run through to make sure I handle all edge cases
# I definitely want more practice with binary search
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        high_index = len(nums)-1
        low_index = 0

        # iterate through the array via binary search only exiting if target is outside hte bounds of the upper and lower bounds
        while low_index <= high_index:
            mid_index = (low_index + high_index)//2
            if nums[mid_index] == target:
                return mid_index
            elif nums[mid_index] > target:
                high_index = mid_index-1
            elif nums[mid_index] < target:
                low_index = mid_index+1
        
        # now low_index broke out of loop since low_index > high_index
        # but then just return the index
        if low_index > high_index:
            return low_index

        if low_index < high_index:
            return high_index
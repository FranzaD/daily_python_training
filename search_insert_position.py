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

        # solution that implements binary search
        high_index = len(nums)-1
        low_index = 0

        # but low_index would never be higher than high_index
        # the other thing I was thinking was using a flag, while glag = false, but then again, I can just break the loop by returning where the index matches the target no need to flag.
        while low_index < high_index:
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
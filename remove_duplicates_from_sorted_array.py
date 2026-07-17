# Leetcode Question 7: Remove Duplicates from Sorted Array
# Solved: 7/17/2026
# Big O Notation: O(n) runtime (the loop only iterates as many times as there are elements in the array)
# Easy
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

# Learned: That in python when people talk about pointers they may just be talking about integers that represent the indices of an array, not an actual memory address like in C++.
# I also learned that in-place modification saves memory because we are not creating a new array, we are just modifying the existing one.
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        write = 0
        read = 1

        while read != len(nums):
            
            if nums[write] == nums[read]:
                read += 1
            
            elif nums[write] != nums[read]:
                unqiue_element = nums[read]
                nums[write + 1] = unqiue_element
                write += 1
                read += 1

        return write + 1
#Leetcode Question 1: Two Sum
# Solved 7/7/2026
# Big O Notation: O(n^2) time

class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+ nums[j] == target:
                    return i, j
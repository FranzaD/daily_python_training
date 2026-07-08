# Leetcode Question 1: Two Sum
# Solved 7/7/2026
# Big O Notation: O(n^2) time
# Easy

# Prompt:
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#You can return the answer in any order.

# Learned: 
# len() returns the count of items in an object in this case the array nums.
# range() returns a number in a sequence from start to stop, at default range(stop) indicates the value where the sequence stops (exclusive).

class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+ nums[j] == target:
                    return i, j


# Optimizing for Runtime 
# O(n) time
# adds value, index pairs to a dictionary while checking to see if value meets criteria for the target
# creates empty dictionary to fill with value, index pairs from nums for quick access and checks to see if value sought was already added to the nums_dict

# Learned:
# enumerate() returns index value pairs, when used with a for loop it allows you to iterate through an array and get the index and value of each item in the array.
# dict is a data structure that stores key-value pairs, allowing for fast lookups of values based on their keys.

class Solution(object):
    def twoSum(self, nums, target):
        nums_dict = {} 
        for i, v in enumerate(nums):
            #determine what the other value should be given the current value
            other = target - v
            # now check if other is in dictionary            
            if other in nums_dict:
                return nums_dict[other], i
            # add current value, index pair to dictionary
            nums_dict[v] = i



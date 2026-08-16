# Leetcode Question 29: Single Number
# Solved: 8/16/2026
# Big O Notation: O(n) runtime
# Easy
# https://leetcode.com/problems/single-number/description/

# Learned: Again only strings are immutable, lists are mutable so when I use methods on a list, I dont need to reassign the variable.

nums = [4,1,2,1,2]

def singleNumber(nums):
    #sort in ascending order to group duplicates together
    nums.sort()

    # iterate over every other index value checking if pairs exist, if not then return the non-duplicate value
    for i in range(0, len(nums), 2):

        #if end of nums is reached, then last value must not have a duplicate, return it
        if i == len(nums) -1:
            return nums[i]

        #if current value doesn't match next value then non-duplicate found, return it
        elif nums[i] != nums[i+1]:
            return nums[i]

print(singleNumber(nums))
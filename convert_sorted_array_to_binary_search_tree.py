# Leetcode Question 21: Convert Sorted Array to Binary Search Tree
# Solved: 
# Big O Notation: O() runtime
# Easy
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/

# Learned:

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """

        # center, needs initially
        mid = len(nums) // 2
        # may be unnecessary
        low = 0
        high = len(nums)
    
        # right subtrees
        high = len(nums)
        low = mid
        mid = (high - low)//2
        return self.sortedArrayToBST(nums[:mid])

        # left subtrees
        low = 0
        high = mid
        mid = (high - low)// 2
        return self.sortedArrayToBST(nums[mid:])

        # base case
        # continue traversing nums until low and high are the same value
        if high == low:
            # not defined yet
            return tree
        
        # if this recieves a list, then I can't pass in anything other than a list, can I use recursion on this function?
        # self.sortedArrayToBST()
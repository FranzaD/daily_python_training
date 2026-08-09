# Leetcode Question 21: Convert Sorted Array to Binary Search Tree
# Solved: 8/8/2026
# Big O Notation: O(n) runtime
# Easy
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/

#Definition for a binary tree node.
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
        # base case, checks if the string is empty
        if not nums:
            return None

        #find middle
        mid = len(nums)//2
     
        #create tree node
        # string slicing is exclusive of mid
        node = TreeNode(nums[mid])
        # list slicing in python, beginning is inclusive, end is exclusive
        node.left = self.sortedArrayToBST(nums[:mid]) #mid excluded
        node.right = self.sortedArrayToBST(nums[mid+1:]) # mid included
        return node
# Leetcode Question 23: Minimum Depth of Binary Tree
# Solved: 8/9/2026
# Big O Notation: O(n) runtime, iterates through each node in binary tree
# Easy
# https://leetcode.com/problems/minimum-depth-of-binary-tree/description/

#Learned: When the issue happens near the beginning of the logic, try to update base cases rather than adjusting if statements at the end.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        # base case: if tree doesn't exist
        if root is None:
            return 0
        # if left subtree doesn't exist, go right
        if root.left is None:
            return self.minDepth(root.right) + 1
        # if right subtree doesn't exist go left
        if root.right is None:
            return self.minDepth(root.left) + 1
        
        # recursively traverses the binary subtrees to determine depth
        left_depth = self.minDepth(root.left) + 1
        right_depth = self.minDepth(root.right) + 1

        # return number of whichever branch (exists) and is less than (past the root)
        if left_depth <= right_depth:
            return left_depth
        else:
            return right_depth
        
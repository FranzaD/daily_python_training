# Leetcode Question 20: Maximum Depth of Binary Tree
# Solved: 8/4/2026
# Big O Notation: O(n) runtime, algorithm iterates through all elements of the binary tree received
# # Easy
# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

# Learned: leveraging recursion for iterating through a tree can really simplify the code.
# Store recursive calls if I need to reuse what is returned

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
    
        # base case if the root points to nothing
        if root is None:
            return 0
        # if a node exists now check branches
        left_depth = self.maxDepth(root.left) 
        right_depth = self.maxDepth(root.right) 

        if left_depth >= right_depth:
            return left_depth + 1
        else:
            return right_depth + 1
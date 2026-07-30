# Leetcode Question 17: Binary Tree Inorder Traversal
# Solved: 7/30/2026
# Big O Notation: O(n) runtime 
# Easy
# https://leetcode.com/problems/binary-tree-inorder-traversal/description/

# Learned: How recursion functions, the mechanics of inorder traversal of trees
# definitely need more practice with recursion, identifying base case of unwind and to handle holding and returning desired output recursively

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        # stop in order travesal (unwind) once None is found for any branch
        if root is None:
            return []
        # list of values found in left branch
        left_values = self.inorderTraversal(root.left)  
        # list of values found in right branch
        right_values = self.inorderTraversal(root.right)
        # return values in the order dictates by inorder traversal left, center, then right
        return left_values + [root.val] + right_values
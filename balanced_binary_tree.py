# Leetcode Question 22: Balanced Binary Tree
# Solved: 8/8/2026
# Big O Notation: O(n) runtime 
# Easy
# https://leetcode.com/problems/binary-tree-balanced/description/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    # this function returns true or false
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        # base case for root
        if root is None:
            return True

        #name of the parameter in function signature needs to be used throuhgout function
        # needs to return integers so that it calculates depth recursively
        def maxDepth(node):
            # base case, if tree is empty
            if node is None:
                return 0
        
            # collect left subtree depth
            left_depth = maxDepth(node.left) + 1
            # collect right subtree depth
            right_depth = maxDepth(node.right) + 1
            # returns the integer that represents the depth of the deepest branch
            return max(left_depth, right_depth) 

        left_depth = maxDepth(root.left)
        right_depth = maxDepth(root.right)

        #checks if current node balanced, if not return false
        if abs(left_depth - right_depth) > 1:
            return False

        # checks if left tree is fully balancec (and right), only returns true if both are true otherwise it returns false
        return self.isBalanced(root.left) and self.isBalanced(root.right)
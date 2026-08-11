# Leetcode Question 24: Path Sum
# Solved: 8/11/2026
# Big O Notation: O(n) runtime, since algorithm iterates through every node in the tree
# Easy
# https://leetcode.com/problems/path-sum/description/

# Learned: the general structure for a top-down solution for a binary tree.
# Here I recognize the pattern where I identify 3 things in order to simplify my approach since I tend to get lost in the details
# 1. id base case (normally root is none)
# 2. if terminal state (normally a leaf node - then determine what to evaluate at that point)
# 3. never use elif, instead opt for a return statement that tries both left and right branches

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    # performs depth first search, checking branch's running sum against targetSum
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """

        if root is None:
            return False
        # check: is this a leaf, AND does the value match exactly?
        if root.left is None and root.right is None:
            return root.val == targetSum
        # otherwise, check both children (with reduced target), combined with OR
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)


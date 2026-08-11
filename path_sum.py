# Leetcode Question 24: Path Sum
# Solved: 
# Big O Notation: O() runtime,
# Easy
# https://leetcode.com/problems/path-sum/description/

#Learned: intial logic

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
        # base case, if root had no node
        if root is None:
            return False
        # check current node if this is a path
        if  targetSum - root.val == 0:
            return True
        # if left available go left
        elif root.left is not None:
            self.hasPathSum(root.left, targetSum - root.val)
        # if right available go right
        elif root.right is not None:
            self.hasPathSum(root.right, targetSum - root.val)
        # if leaf node
        else:
            return False


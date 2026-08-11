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
        # base cases
        if root is None:
            return False

        #immediately begin calculating sum
        # if going down, add
        sum += node.val
        # if going up, subtract
        sum -= node.val

        # if left node exists, traverse
        if node.left is not None:
            hasPathSum(node.left)
        # if not left, go right
        elif node.left is None and node.right is not None:
            hasPathSum(node.right)
        # if leaf found, check sum and then unwind by one node, subtract value
        elif node.left is None and node.right is None:
            if sum == targetSum:
                return True
            else: # target sum not found in this branch, return what? just need to go back up
                sum = sum - node.val
                return node.val


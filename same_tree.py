# Leetcode Question 18: Same Tree
# Solved: 8/3/2026
# Big O Notation: O(n) runtime since it traverses every node in both trees to check for equality
# Easy
# https://leetcode.com/problems/same-tree/description/

# Learned: First time using an inline return statement, 
# this is a brilliant method for going back up to a node to traverse the other branches/subtree

# Definition for a binary tree node. 
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        # none is not a value of a node, it indicates branch that doesnt have a node
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False
        # if nodes with values exist that dont match then trees are not the same
        elif p.val != q.val:
            return False
        else: # if values do match then the remainder of the tree needs to be searched
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
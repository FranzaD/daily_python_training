# Leetcode Question 19: Symmetric Tree
# Solved: 
# Big O Notation: O() runtime 
# Easy
# https://leetcode.com/problems/symmetric-tree/description/

# Learned:

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def isMirror(p, q):
            # if left and right subtrees are none, not symmetric since there's no tree
            if p is None and q is None:
                return False
            # return if only one subtree is none
            elif p is None and q is not None:
                return False
            # if values of left and right subtree nodes don't match 
            elif p.val != q.val:
                return False
            # if the values of left and right subtree nodes do match continue traversing
            elif p.val == q.val:
                return isMirror(p.left, q.right) and isMirror(p.right, p.left)
            
        if root is None:
            return False
        else:
            return isMirror(root.left, root.right)
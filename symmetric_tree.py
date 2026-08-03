# Leetcode Question 19: Symmetric Tree
# Solved: 8/3/2026
# Big O Notation: O(n) runtime since it runs through every node in the tree not skipping any until found false
# Easy
# https://leetcode.com/problems/symmetric-tree/description/

# Learned: That recursion doesn't need to return a values to store in a list, instead nodes can be compared, 
# and then iterated to the next with a new function call

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
        def isMirror(left_node, right_node):
            # if left and right subtrees are none, symmetric since a node exists but left and right branches are none!
            if left_node is None and right_node is None:
                return True
            # not symmetric if one branch is none and the other isn't
            elif left_node is None and right_node is not None or left_node is not None and right_node is None:
                return False
            # if values of left and right subtree nodes don't match 
            elif left_node.val != right_node.val:
                return False
            # if the values of left and right subtree nodes do match continue traversing
            elif left_node.val == right_node.val:
                return isMirror(left_node.left, right_node.right) and isMirror(left_node.right, right_node.left)
            
        if root is None:
            return False
        else: # start recursion if root has node
            return isMirror(root.left, root.right)
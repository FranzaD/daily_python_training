# Leetcode Question 18: Same Tree
# Solved: 
# Big O Notation: O() runtime 
# Easy
# https://leetcode.com/problems/same-tree/description/

# Learned:

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
        # functional that will traverse both trees and do the actual recursion
        def inorderTraversal(treeNode):
            """
            :rtype: list
            """
            if treeNode is None:
                return [None]
            left_values = inorderTraversal(treeNode.left)
            right_values = inorderTraversal(treeNode.right)

            return left_values + [treeNode.val] + right_values 

        # traverse p recursively
        p_list = inorderTraversal(p)
        
        # traverse q recursively
        q_list = inorderTraversal(q)
        
        # return true or false from a comparsion of p and q lists 
        if p_list == q_list:
            return True
        else:
            return False
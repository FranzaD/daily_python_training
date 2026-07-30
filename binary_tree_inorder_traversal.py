# Leetcode Question 17: Binary Tree Inorder Traversal
# Solved: 
# Big O Notation: O() runtime 
# Easy
# https://leetcode.com/problems/binary-tree-inorder-traversal/description/

# Learned: Reviewing recursion and inorder traversal of trees

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
        result_list = []
        if root is None:
            # base case - what happens here? return an empty list
            return []
        # step 1: recurse left
        while self.inorderTraversal(root.left) is not None:
            result_list.append(root.val)
        # step 2: record node.val
        result.append(root.val)
        # step 3: recurse right
        while self.inorderTraversal(root.right) is not None:
            result_list.append(root.val)
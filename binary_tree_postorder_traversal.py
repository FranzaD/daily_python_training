# Leetcode Question 31: Binary Tree Postorder Traversal
# Solved: 8/18/2026
# Big O Notation: O(n) runtime, O(h) space where h is the height of the tree
# Easy
# https://leetcode.com/problems/binary-tree-postorder-traversal/description/

# Learned: postorder traversal is traversing a binary tree in the order left -> right -> self

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if root is None:
            return []

        left_node = self.postorderTraversal(root.left)
        right_node = self.postorderTraversal(root.right)

        return left_node + right_node + [root.val]
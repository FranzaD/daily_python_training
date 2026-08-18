# Leetcode Question 30: Binary Tree Preorder Traversal
# Solved: 8/17/2026
# Big O Notation: O(n) runtime, O(h) space where h is the height of the tree
# Easy
# https://leetcode.com/problems/binary-tree-preorder-traversal/description/

# Learned: preorder traversal is traversing a binary tree in the order self -> left -> right
# runtime is linear since we iterate through every node in the tree, and space is O(h) since we are using recursion and the maximum depth of the recursion stack is equal to the height of the tree

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        #base case
        if root is None:
            return []

        left_node = self.preorderTraversal(root.left)
        right_node = self.preorderTraversal(root.right)

        return [root.val] + left_node + right_node 
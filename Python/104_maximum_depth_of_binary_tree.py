# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """ Recursion """
    def maxDepth(self, root):
        if not root:
            return 0

        leftMaxDepth = self.maxDepth(root.left)
        rightMaxDepth = self.maxDepth(root.right)

        return max(leftMaxDepth, rightMaxDepth) + 1


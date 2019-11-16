# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root):

        if not root:
            return 0

        leftMinDepth = self.minDepth(root.left)
        rightMinDepth = self.minDepth(root.right)

        if not root.left or not root.right:
            return max(leftMinDepth, rightMinDepth) + 1

        return min(leftMinDepth, rightMinDepth) + 1
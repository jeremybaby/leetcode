# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution1:
    """ Recursion """
    def isSubtree(self, s, t):
        if not s: return False
        if self.isSameTree(s, t): return True
        return  self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def isSameTree(self, s, t):
        if not s and not t: return True
        if not s or not t: return False
        if s.val != t.val: return False

        return self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right)


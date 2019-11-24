# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution1:
    """Recursion"""
    def binaryTreePaths(self, root):
        res = []
        if not root: return res
        self.helper(res, root, "")
        return res

    def helper(self, res, root, path):
        # 边界条件 碰到叶子结点
        if not root.left and not root.right:
            res.append(path + str(root.val))

        # 有左孩子
        if root.left:
            self.helper(res, root.left, path + str(root.val) + "->")
        # 有有孩子
        if root.right:
            self.helper(res, root.right, path + str(root.val) + "->")


class Solution2:
    def binaryTreePaths(self, root):
        if not root: return []
        res = []
        stack = [(root, str(root.val))]

        while stack:
            node, path = stack.pop()
            if not node.left and not node.right:
                res.append(path)

            if node.left:
                stack.append((node.left, path + "->" + str(node.left.val)))
            if node.right:
                stack.append((node.right, path + "->" + str(node.right.val)))

        return res
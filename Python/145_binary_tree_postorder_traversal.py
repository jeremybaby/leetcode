# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution1:
    """递归"""
    def __init__(self):
        self._res = []

    def postorderTraversal(self, root):
        if not root:
            return

        self.postorderTraversal(root.left)
        self.postorderTraversal(root.right)
        self._res.append(root.val)

        return self._res


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution2:
    """迭代"""
    def postorderTraversal(self, root):

        res = []

        if not root:
            return res

        stack = [root]

        while stack:
            node = stack.pop()

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            res.append(node.val)

        return res[::-1]
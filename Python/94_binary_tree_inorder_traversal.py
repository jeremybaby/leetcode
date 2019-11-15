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

    def inorderTraversal(self, root):
        if not root:
            return

        self.inorderTraversal(root.left)
        self._res.append(root.val)
        self.inorderTraversal(root.right)

        return self._res

class Solution2:
    """ 迭代，维护stack:
      - 只要左子树不为空一直迭代，一直入栈
      - 打印当前值
      - 看右子树
    """
    def inorderTraversal(self, root):

        res, stack = [], []

        cur = root

        while cur or stack:

            while cur:
                stack.append(cur)
                cur = cur.left

            # 看当前值
            cur = stack.pop()
            res.append(cur.val)
            # 看右子树
            cur = cur.right

        return res
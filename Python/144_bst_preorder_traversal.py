# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution1:
    """递归实现"""
    def __init__(self):
        self._res = []

    def preorderTraversal(self, root):
        if not root:
            return

        self._res.append(root.val)
        self.preorderTraversal(root.left)
        self.preorderTraversal(root.right)

        return self._res

class Solution2:
    """使用stack:
      - 每次pop()栈顶元素为node
      - node.right有值，就入栈
      - node.left有值，就入栈
    """
    def preorderTraversal(self, root):

        if not root:
            return []

        stack = [root]
        res = []

        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return res


class Solution3:
    """ 迭代实现: 使用stack """
    def preorderTraversal(self, root):

        res, stack = [], []

        p = root

        while p or stack:

            while p:
                res.append(p.val)
                stack.append(p)
                p = p.left

            p = stack.pop().right

        return res
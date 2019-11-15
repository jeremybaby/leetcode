# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution1:
    """ 递归 """
    def levelOrder(self, root):

        levels = []

        if not root:
            return levels

        def helper(node, level):
            if len(levels) == level:
                levels.append([])

            levels[level].append(node.val)

            if node.left:
                helper(node.left, level + 1)
            if node.right:
                helper(node.right, level + 1)

        helper(root, 0)

        return levels

class Solution2:
    """ 使用list 模拟队列 """
    def levelOrder(self, root):

        if not root:
            return

        res, queue = [], [root]

        while queue:
            cur_level = []
            cur_len = len(queue)

            for i in range(cur_len):
                cur_node = queue.pop(0)
                cur_level.append(cur_node.val)

                if cur_node.left:
                    queue.append(cur_node.left)

                if cur_node.right:
                    queue.append(cur_node.right)
            res.append(cur_level)

        return res

from collections import deque

class Solution3:
    """ 使用Python中 collections.deque """
    def levelOrder(self, root):

        levels = []

        if not root:
            return levels

        level = 0
        queue = deque([root, ])

        while queue:
            levels.append([])
            level_length = len(queue)

            for i in range(level_length):
                node = queue.popleft()

                levels[level].append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1

        return levels
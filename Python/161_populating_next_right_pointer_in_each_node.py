class Solution1:
    """LevelOrder 但不符合题意O(1)的Space"""
    def connect(self, root):
        if not root: return None

        queue = [root]
        pre = None

        while queue:

            size = len(queue)

            for i in range(size):
                node = queue.pop(0)
                if i > 0:
                    pre.next = node
                    # 下面的不用加，因为默认为None
                    # if i == size - 1:
                    #     node.next = None

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

                pre = node

        return root


class Solution2:
    """PreOrder Recursion  Time: O(n) Space: O(1)"""
    def connect(self, root):

        if not root: return None

        if root.left:
            root.left.next = root.right

        if root.next and root.right:
            root.right.next = root.next.left

        self.connect(root.left)
        self.connect(root.right)

        return root


class Solution3:
    """PreOrder Iteration Time: O(n) Space: O(1)"""
    def connect(self, root):

        if not root: return None

        # start代表每层的开始
        start = root

        while start:
            # cur代表当前层的扫描指针
            cur = start
            while cur:
                if cur.left:
                    cur.left.next = cur.right
                if cur.right and cur.next:
                    cur.right.next = cur.next.left
                cur = cur.next
            start = start.left

        return root
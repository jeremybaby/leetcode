# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def splitListToParts(self, root, k):

        i = length = 0
        cur = root
        res = []

        while cur:
            length += 1
            cur = cur.next

        count, ex_count = length // k, length % k

        while i < k:
            if root:
                res.append(root)
                for j in range(count + int(i < ex_count) - 1):
                    root = root.next

                temp = root.next
                root.next = None
                root = temp
            else:
                # 注意，一定一定是None哈！！！
                res.append(None)
            i += 1

        return res


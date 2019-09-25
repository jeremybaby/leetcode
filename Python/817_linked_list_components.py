# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution1:
    """在G中就+1，移动指针直到不在G中"""
    def numComponents(self, head, G):
        cur = head
        count = 0

        while cur:
            if cur.val in G:
                count += 1
                while cur.next and cur.val in G:
                    cur = cur.next

            cur = cur.next

        return count


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution2:
    """把G转换为set，效率提升了10倍数+"""
    def numComponents(self, head, G):
        cur = head
        count = 0
        lookup = set()

        for e in G:
            lookup.add(e)

        while cur:
            if cur.val in lookup:
                count += 1
                while cur.next and cur.val in lookup:
                    cur = cur.next

            cur = cur.next

        return count
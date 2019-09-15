# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution1:
    def reverseBetween(self, head, m, n):
        """[1, 2, 3, 4, 5] --(2，4)--> [1, 4, 3, 2 ,5]"""
        dummy = ListNode(0)
        dummy.next = head
        i = 1
        mid_head = dummy

        while (i < m):
            mid_head = head
            head = head.next
            i += 1

        # mid_head = 1
        # mid_tail = 2
        mid_tail = head

        prev = None
        while i >= m and i <= n:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
            i += 1
        # head = 5 prev = 4

        mid_head.next = prev
        mid_tail.next = head

        return dummy.next


class Solution2:
    def reverseBetween(self, head, m, n):
        """"""
        pre = dummy = ListNode(0)
        dummy.next = head
        i = 1

        while i < m:
            pre = pre.next

        cur = pre.next

        while i >= m and i <= n:
            temp = cur.next
            cur.next = temp.next
            temp.next = pre.next
            pre.next = temp

        return dummy.next
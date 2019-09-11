# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution1:
    """单指针"""
    def removeElements(self, head, val):
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy

        while cur.next:
            if (cur.next.val == val):
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next

class Solution2:
    """双指针"""
    def removeElements(self, head, val):
        dummy = ListNode(0)
        dummy.next = head
        prev, cur = dummy, dummy.next

        while cur:
            if (cur.val == val):
                prev.next = cur.next
            else:
                prev = cur
            cur = cur.next

        return dummy.next


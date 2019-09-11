# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """迭代：双指针"""
        cur = head
        prev = None
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev


class Solution2:
    def reverseList(self, head):
        """递归"""
        if not head or not head.next:
            return head

        ret = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return ret

# head = 4:      5 --> 4 --> NULL
# head = 3:      5 --> 4 --> 3 --> NULL
# head = 2, 1:      5 --> 4 --> 3 ---> 2 --> 1 --> NULL

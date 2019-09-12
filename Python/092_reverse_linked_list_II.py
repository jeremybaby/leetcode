# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        i = 1
        mid_head = dummy

        while (i < m):
            mid_head = head
            head = head.next
            i += 1

        # mid_head = 1
        mid_tail = head  # head = 2

        prev = None
        while i >= m and i <= n:
            temp = head.next  # temp = 3, 4, 5
            head.next = prev  # 4 --> 3 --> 2--> NULL
            prev = head  # prev = 2, 3, 4
            head = temp  # head = 3, 4, 5
            i += 1  # i = 3, 4, 5
        # head = 5 prev = 4

        mid_head.next = prev
        mid_tail.next = head

        #         while dummy.next:
        #             dummy = dummy.next
        #             print(dummy.val)
        return dummy.next




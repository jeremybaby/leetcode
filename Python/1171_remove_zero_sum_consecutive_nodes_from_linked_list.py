# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    """prefix sum"""
    def removeZeroSumSublists(self, head):
        dummy = ListNode(0)
        dummy.next = head
        sum = 0
        lookup = {sum: dummy}
        cur = head

        while cur:
            sum += cur.val
            if sum in lookup:
                lookup[sum].next = cur.next
            else:
                lookup[sum] = cur
            cur = cur.next

        return dummy.next
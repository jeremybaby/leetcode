# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Solution1: 双指针
class Solution:
    def plusOne(self, head):
        dummy = ListNode(0)
        dummy.next = head
        slow = fast = dummy

        while fast.next:
            fast = fast.next
            if fast.val != 9:
                slow = fast
                print(fast.val)

        slow.val += 1
        while slow.next:
            slow = slow.next
            slow.val = 0

        if dummy.val:
            return dummy
        return head

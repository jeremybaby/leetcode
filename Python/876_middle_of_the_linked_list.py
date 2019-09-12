# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution1:
    """遍历取得链表长度len，再遍历len / 2"""
    def middleNode(self, head):

        dummy = head
        len = self.lenList(dummy)
        half_pos = len // 2

        while half_pos:
            head = head.next
            half_pos -= 1
        return head

    def lenList(self, head):
        len = 0
        while head:
            head = head.next
            len += 1
        return len

class Solution2:
    """空间换时间，链表放在list中"""
    def middleNode(self, head):

        result = []

        while head:
            # 注意先append 再移动指针
            result.append(head)
            head = head.next

        return result[len(result) // 2]

class Solution3:
    """快慢指针"""
    def middleNode(self, head):

        fast = slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow

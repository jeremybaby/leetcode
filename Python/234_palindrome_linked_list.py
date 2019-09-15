# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution1:
    """全部元素入栈，然后第二次遍历与stack.pop()比较"""
    def isPalindrome(self, head):
        cur = head
        stack = []

        while cur:
            stack.append(cur.val)
            cur = cur.next

        while head:
            if head.val != stack.pop():
                return False
            head = head.next

        return True

class Solution2:
    """快慢指针 + 栈"""
    def isPalindrome(self, head):
        fast = slow = head
        stack = []

        while fast and fast.next:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next

        # 奇数个元素时
        if fast:
            slow = slow.next

        while slow:
            if stack.pop() != slow.val:
                return False
            slow = slow.next

        return True

class Solution3:
    """快慢指针 + 反转前半部分链表"""
    def isPalindrome(self, head):
        if not head:
            return True

        prev = fast = slow = head

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # 奇数
        if fast:
            slow = slow.next

        prev.next = None
        fast = self.reverseList(head)

        while slow and fast:
            if slow.val != fast.val:
                return False
            slow = slow.next
            fast = fast.next

        return True

    def reverseList(self, head):

        cur = head
        prev = None

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        return prev
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    """思路: 三指针: 原链表的指针、小于原链表的指针、大于原链表的指针"""
    def partition(self, head, x):
        old = dummy = ListNode(0)
        cur = dummy.next = head

        new = newList = ListNode(0)

        while cur:
            if cur.val >= x:
                new.next = cur
                new = new.next
            else:
                old.next = cur
                old = old.next

            cur = cur.next

        new.next = None
        old.next = newList.next

        return dummy.next

class Solution2:
    """思路: Solution1因为old和cur的指针可以合并,每次把>=x的那一项剔除掉即可"""
    def partition(self, head, x):
        cur = dummy = ListNode(0)
        dummy.next = head

        new = newList = ListNode(0)

        while cur.next:
            if cur.next.val >= x:
                new.next = cur.next
                new = new.next
                cur.next = cur.next.next
            else:
                cur = cur.next

        new.next = None
        cur.next = newList.next

        return dummy.next

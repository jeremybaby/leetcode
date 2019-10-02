# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head, k):

        def reverseList(head):
            prev = None
            cur = head
            while cur:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
            return prev

        if not head or not head.next:
            return head

        newList = None
        length = 0
        probe = head
        while probe:
            length += 1
            probe = probe.next
        if k > length:
            return head
        elif k == length:
            return reverseList(head)

        probe = head
        tempHead = None
        while probe and length >= k:
            tempTail = tempHead
            tempHead = cur = probe
            for i in range(k - 1):
                cur = cur.next
            probe = cur.next
            cur.next = None
            if newList == None:
                newList = reverseList(head)
            else:
                tempTail.next = reverseList(tempHead)
            length -= k

        if length > 0:
            tempHead.next = probe

        return newList if newList else head


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        if not head or not head.next or k == 1:
            return head

        def reverseOneGroup(pre, next):
            prev = None
            res = cur = pre.next
            while cur != next:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
            pre.next = prev
            res.next = next
            return res

        dummy = ListNode(0)
        dummy.next = head
        pre, cur = dummy, head
        i = 1
        while cur:
            if i % k == 0:
                pre = reverseOneGroup(pre, cur.next)
                cur = pre.next
            else:
                cur = cur.next
            i += 1
        return dummy.next
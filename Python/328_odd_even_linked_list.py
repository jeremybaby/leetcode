# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution1:
    def oddEvenList(self, head):
        if not head:
            return head

        odd = head
        evenHead = even = head.next

        while even and even.next:
            nextOdd = even.next
            # 奇 --> 奇
            odd.next = nextOdd
            # 偶 --> 偶
            even.next = nextOdd.next
            # next奇 --> 偶头节点
            nextOdd.next = evenHead

            odd = odd.next
            even = even.next

        return head

class Solution2:
    """Solution1的改进，无须每次都nextOdd连偶头节点，只需最终连即可"""
    def oddEvenList(self, head):
        if not head:
            return head

        odd = head
        evenHead = even = head.next

        while even and even.next:
            # 奇 --> 奇
            odd.next = odd.next.next
            # 偶 --> 偶
            even.next = even.next.next

            odd = odd.next
            even = even.next

        odd.next = evenHead

        return head

    
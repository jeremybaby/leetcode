# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution0:
    def deleteDuplicates(self, head):
        dummy = ListNode(0)
        prev = dummy
        dummy.next = head
        # 每次肯定要迭代pre，所以用pre去生成cur
        cur = head
        while cur.next:
            # 注意：不要用firstVal这样的临时变量，直接使用prev.next
            firstVal = cur.val
            # Attention： 一定是数字的比较而非节点的比较
            while firstVal == cur.next.val:
                cur = cur.next
                print('cur val: ', firstVal)
            if cur.val == firstVal:
                print('prev val: ', prev.val)
                prev.next = cur.next
                prev = cur.next
            else:
                prev = cur
            cur = cur.next
        """既要修改prev、又要修改cur"""
        return dummy.next

class Solution1:
    def deleteDuplicates(self, head):
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        # 每次修改的是prev
        while prev.next:
            # 用prev去修改cur
            cur = prev.next

            while cur.next and cur.val == cur.next.val:
                cur = cur.next

            # 注意这里比较的不是val!!!切记！
            if cur == prev.next:
                prev = cur
            else:
                prev.next = cur.next

        return dummy.next


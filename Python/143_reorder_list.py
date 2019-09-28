# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
思路1： 把后一半的链表进行反转，
        如何找到一半呢？ ---> 快慢指针
然后可以进行插入 / 搞个新链表，重新弄
思路2：把链表存入list里，然后从开始进行插入
未想到的思路：相反顺序 ---> 使用栈
"""


class Solution1:
    """Solution1:
       - 快慢指针到链表的一半
       - 后半段链表进行反转
       - 逐个插入到前半段链表中
    """
    def reorderList(self, head):
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        l1 = head
        l2 = self.reverseList(slow.next)
        # remember to set None
        slow.next = None

        while l1 and l2:
            temp = l2
            l2 = l2.next

            temp.next = l1.next
            l1.next = temp

            l1 = temp.next

        return head

    def reverseList(self, head):
        prev = None
        cur = head
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        return prev


class Solution2:
    """Solution2:
       - 所有元素存入栈中
       - 每次pop()的元素插入前半段链表
    """
    def reorderList(self, head):
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head

        cur = head
        stack = []

        while cur:
            stack.append(cur)
            cur = cur.next

        cur = head
        mid = len(stack) // 2
        while mid > 0:
            mid -= 1
            ele = stack.pop()

            ele.next = cur.next
            cur.next = ele
            cur = ele.next
        # 注意，这里一定要结束，而且使用cur指针
        # 否则会造成超时哦
        cur.next = None

        return head


class Solution3:
    """Solution3:
      - 所有元素存入数组中
      - 两个索引从左至右、从右至左进行遍历，互相链接
    """
    def reorderList(self, head):
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head
        cur = head
        arr = []

        while cur:
            arr.append(cur)
            cur = cur.next

        i, j = 0, len(arr) - 1
        while i < j:
            arr[i].next = arr[j]
            arr[j].next = arr[i + 1]
            i += 1
            j -= 1
        arr[i].next = None

        return head
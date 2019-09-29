# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution1:
    """Solution1:
    - k %= len
    - 快指针先走k步
    - 快慢指针同时走，最终快指针到达末尾，慢指针到达距离结尾k个位置
    """
    def rotateRight(self, head, k):

        if not head or not head.next:
            return head
        # 获取长度
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next

        # 计算k
        k %= length
        if k == 0:
            return head

        # 快指针先走k步
        fast = slow = head
        for i in range(k):
            fast = fast.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        # 注意fast.next已经到末尾了，只需链接到头部
        fast.next = head
        newHead = slow.next
        slow.next = None

        return newHead

class Solution2:
    """
      - 先遍历一边获得链表长度
      - 把表头表尾链起来
      - 往后走len - k % len个节点到达新表的头一个节点，此时断开链表即可

    """
    def rotateRight(self, head, k):

        if not head or not head.next:
            return head

        cur = head
        length = 1
        while cur.next:
            length += 1
            cur = cur.next

        # 链接尾和头
        cur.next = head
        # 向后走length - k % length步
        for i in range(length - k % length):
            cur = cur.next
        head = cur.next
        cur.next = None

        return head
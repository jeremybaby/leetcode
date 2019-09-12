# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution1(object):
    """ 集合存储所有节点，Time: O(n), Space: O(n)"""
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        sets = set()

        while head:
            if head in sets:
                return head
            sets.add(head)
            head = head.next

        return None

class Solution2(object):
    """快慢指针：Time: O(n), Space: O(1)"""
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
            # 有环存在
            if (slow == fast):
                # slow和head相交时，即为环的入口
                while (slow != head):
                    head = head.next
                    slow = slow.next
                return slow

        return None
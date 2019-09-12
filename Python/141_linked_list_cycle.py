# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution1(object):
    """集合存储所有节点，Time: O(n), Space: O(1)"""
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        nodes = set()

        while (head):
            if head in nodes:
                return True
            nodes.add(head)
            head = head.next

        return False

class Solution2(object):
    """快慢指针，有环时跑得快的和慢的总会重合"""
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        fast = slow = head

        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if (slow == fast):
                return True

        return False
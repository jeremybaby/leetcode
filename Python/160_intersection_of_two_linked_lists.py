# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution1(object):
    """
    - 由于两个链表长度不相同，我们分别获取两个链表的长度，
    - 让长的链表指针向右移动,直到两个链表的长度相同
    - 遍历，如果有两个节点相同，那么就直接返回，否则没找到返回None
    """
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None
        lenA = self.getLen(headA)
        lenB = self.getLen(headB)
        probeA = headA
        probeB = headB

        while lenA != lenB:
            if lenA > lenB:
                lenA -= 1
                probeA = probeA.next
            else:
                lenB -= 1
                probeB = probeB.next

        while probeA:
            if probeA == probeB:
                return probeA
            probeA = probeA.next
            probeB = probeB.next

        return None

    def getLen(self, head):
        length = 0
        probe = head
        while probe != None:
            length += 1
            probe = probe.next
        return length


class Solution2(object):
    def getIntersectionNode(self, headA, headB):
        """
          - 遍历链表 A 并将每个结点的地址/引用存储在哈希表中。
          - 然后检查链表 B 中的每一个结点是在A中，若在，即返回
        """
        setA = set()
        ha, hb = headA, headB
        while ha:
            setA.add(ha)
            ha = ha.next

        while hb:
            if hb in setA:
                return hb
            hb = hb.next
        return None

class Solution3(object):
    """ 环的思想
        ha --> hb --> None
        hb --> ha --> None
    """
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        ha, hb = headA, headB
        while ha != hb:
            ha = ha.next if ha else headB
            hb = hb.next if hb else headA

        return ha


class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random

class Solution1:
    """
      - 哈希表存储所有链表的节点，然后再连线
        - key: 原node
        - value: deep copied node
        - 注意: dict的定义、使用、查找
    """
    def copyRandomList(self, head):
        if not head:
            return head
        lookup = {}
        probe = head
        while probe:
            lookup[probe] = Node(probe.val, None, None)
            probe = probe.next

        probe = head
        while probe:
            lookup[probe].next = lookup.get(probe.next)
            lookup[probe].random = lookup.get(probe.random)
            probe = probe.next

        return lookup[head]


"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""


class Solution2:
    def copyRandomList(self, head):
        if not head:
            return head

        # Step1: 遍历，将拷贝节点放在原节点的右边
        probe = head
        while probe:
            temp = probe.next
            # 注意，此处原节点末尾的None，已经复制给了拷贝节点最后的next
            probe.next = Node(probe.val, temp, None)
            probe = temp

        # Step2: 遍历，复制原节点random指针到拷贝节点
        probe = head
        while probe:
            if probe.random:
                probe.next.random = probe.random.next
            probe = probe.next.next

        # Step3: 拆分，原节点与拷贝节点分别两个指针进行遍历
        probe = head
        probe_cpy = newList = head.next
        while probe_cpy.next:
            # 恢复原节点的next指向
            probe.next = probe.next.next
            probe = probe.next
            # 更新新节点的next指向
            probe_cpy.next = probe_cpy.next.next
            probe_cpy = probe_cpy.next

        # 原节点的末尾置空
        probe.next = None
        return newList


"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""

class Solution3:
    """DFS"""
    def __init__(self):
        self.lookup = {}

    def copyRandomList(self, head):
        if not head:
            return head
        if head in self.lookup:
            return self.lookup[head]

        # 创建和原节点一样值的node
        node = Node(head.val, None, None)
        # 存储到hashmap中
        self.lookup[head] = node
        # 分别 顺着 random 和 next 指针进行回溯
        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)

        return node


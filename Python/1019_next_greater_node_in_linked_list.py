# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    """单调栈从左至右"""
    def nextLargerNodes(self, head):

        nums = []
        # 链表先转为数组
        while head:
            nums.append(head.val)
            head = head.next

        stack = []
        # 初始化返回结果都为0
        res = [0] * len(nums)

        # 从左至右迭代nums
        for i, n in enumerate(nums):
            # 只要当前元素比栈顶的元素的值大
            while stack and nums[stack[-1]] < n:
                # stack.pop()为栈顶的索引
                # 记录比栈顶元素右边第一个larger的数字为n
                res[stack.pop()] = n
            # 把每个索引入栈
            stack.append(i)
        return res


class Solution2:
    """单调栈从右至左"""
    def nextLargerNodes(self, head):

        nums = []
        while head:
            nums.append(head.val)
            head = head.next

        stack = []
        res = [0] * len(nums)
        i = len(nums) - 1
        # 从右至左遍历
        while i >= 0:
            # 当前元素只要大于栈顶就一直pop
            while stack and stack[-1] <= nums[i]:
                stack.pop()
            # 栈有值，说明栈顶比自己大
            if stack:
                res[i] = stack[-1]
            stack.append(nums[i])

            i -= 1

        return res
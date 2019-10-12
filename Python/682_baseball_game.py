class Solution:
    """栈： 自己实现"""
    def calPoints(self, ops):

        stack = []

        for s in ops:
            if s.isdigit():
                stack.append(int(s))
            elif s[0] == '-' and s[1:].isdigit():
                # 负数
                stack.append(int(s))
            elif len(stack) > 1 and s == '+':
                stack.append(stack[-1] + stack[-2])
            elif s == 'C':
                stack.pop()
            elif s == 'D':
                stack.append(stack[-1] * 2)

        return sum(stack)

class Solution_Promote:
    """官方题解优化
       - 时间复杂度 O(n)
       - 空间复杂度 O(n)
    """
    def calPoints(self, ops):

        stack = []

        for op in ops: # 修改1： 变量命名
            """
            以下全部放入else中，都是要append(int(op))嘛
            if op.isdigit():
                stack.append(int(op))
            elif op[0] == '-' and op[1:].isdigit():
                # 负数
                stack.append(int(op))
            """
            # if len(stack) > 1 and op == '+':
            if op == '+':
                # 这里假定了'+'出现时至少有2个元素
                stack.append(stack[-1] + stack[-2])
            elif op == 'C':
                stack.pop()
            elif op == 'D':
                stack.append(stack[-1] * 2)
            else:
                stack.append(int(op))

        return sum(stack)
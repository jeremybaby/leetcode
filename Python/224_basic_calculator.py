class Solution:
    def calculate(self, s: str) -> int:

        num, res = 0, 0
        stack = []
        # 记录数字的符号, 题目说没有负数, 说明第一个为正数, 设为1
        sign = 1

        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == '+':
                res += sign * num
                num, sign = 0, 1
            elif c == '-':
                res += sign * num
                num, sign = 0, -1
            elif c == '(':
                # 把括号前的运算结果和符号存起来
                stack.append(res)
                stack.append(sign)
                # res一定要重新置为0
                # num不需要置为0的原因：'('前面必定是'+'或'-'
                # sign 这里重新分配为1，从正数开始算
                res, sign = 0, 1
            elif c == ')':
                res += sign * num
                num = 0
                res = stack.pop() * res + stack.pop()
        res += sign * num

        return res
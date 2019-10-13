class Solution:
    """
     思路：
     - 如果是数字计算出来 num = num * 10 + 当前数字
     - 遇到符号，对stack进行处理，看上一个符号
        + 存符号之前的数字
        - 存符号之前的负数
        * 修改top为 top * 符号之前的数字
        / 修改top为 top / 符号之前的数字
        更新上一个符号为当前符号，更新数字为0
    """
    def calculate(self, s):

        s += "+0"
        num = 0
        stack = []
        operations = {'+', '-', '*', '/'}

        # sign是前一个的运算符，初始化为加号
        sign = '+'

        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c in operations:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack[-1] = stack[-1] * num
                elif sign == '/':
                    stack[-1] = int(stack[-1] / num)

                # 只要遇到运算符num就要初始化为0
                sign, num = c, 0
                print('c: ', c, '\tstack: ', stack, '\tsign: ', sign)

        return sum(stack)

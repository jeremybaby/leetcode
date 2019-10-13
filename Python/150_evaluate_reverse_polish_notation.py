class Solution1_1:
    def evalRPN(self, tokens):

        stack = []
        operations = {'+', '-', '*', '/'}
        # 也可以写成 operations = "+-*/"

        for token in tokens:
            if token not in operations:
                stack.append(int(token))
            else:
                right = stack.pop()
                left = stack.pop()
                if token == '+':
                    tmp = left + right
                elif token == '*':
                    tmp = left * right
                elif token == '-':
                    tmp = left - right
                else:
                    tmp = int(left / right)
                    """
                    if left * right >= 0:
                        tmp = left // right
                    else:
                        tmp = -(abs(left) // abs(right))
                    """
                stack.append(tmp)

        return stack[0]


import math

class Solution1_2:
    def evalRPN(self, tokens):

        stack = []

        for token in tokens:
            if token not in "+-*/":
                stack.append(token)
            else:
                right = stack.pop()
                left = stack.pop()
                expression = left + token + right

                if token == '/':
                    # 不可用math.floor(); 6 / -12时用floor为-1
                    tmp = math.trunc(eval(expression))
                else:
                    tmp = eval(expression)

                # 注意这里push进去的要转换为str哦
                stack.append(str(tmp))

        return int(stack.pop())
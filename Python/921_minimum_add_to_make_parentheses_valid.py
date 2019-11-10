class Solution1:
    """Stack
    维护一个计数变量
    - 遇到左括号，入栈
    - 遇到右括号，
      - 栈空的话计数+1
      - 栈不空，pop()出来的元素不是'('，即此时括号不匹配.
    - 最后计数加上栈里剩余的元素个数 （比如stack里面只有'((('）
    """
    def minAddToMakeValid(self, S):

        lookup = {'(': ')'}

        stack = []

        res = 0

        for parenthese in S:
            if parenthese in lookup:
                stack.append(parenthese)
            elif len(stack) == 0 or parenthese != lookup[stack.pop()]:
                res += 1

        res += len(stack)

        return res


class Solution2:
    """
     思路：计算前缀子数组的[平衡度]：
        左括号出现平衡度加一，右括号出现平衡度减一，为0是此时匹配
     具体实现：
         维护一个平衡度变量和res，遍历数组
        - 左括号，平衡度加一
        - 右括号，平衡度减一
        - 当平衡度为-1时，代表出现了一个不匹配的')'，我们res+1，平衡度加一.
        - ans += 平衡度（考虑到只有'((('的情况）
    """
    def minAddToMakeValid(self, S):

        ans, avgDegree = 0, 0

        for symbol in S:

            avgDegree += 1 if symbol == '(' else -1

            if avgDegree == -1:
                ans += 1
                avgDegree += 1

        ans += avgDegree

        return ans
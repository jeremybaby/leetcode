class Solution1:
    """计算括号的深度x，答案就是2^x的累加和"""
    def scoreOfParentheses(self, S):

        ans, depth = 0, 0

        for i in range(len(S)):
            if S[i] == '(':
                depth += 1
            else:
                depth -= 1
                if S[i - 1] == '(':
                    ans += (1 << depth)

        return ans
""" eg. (()(()))
(           depth = 1
((          depth = 2
(()         depth = 1, ans = 2
(()(        depth = 2
(()((       depth = 3
(()((()     depth = 2, ans = 2 + (1 << 2) = 6
(()((())    depth = 1
(()((()))   depth = 0
"""


class Solution2:
    def scoreOfParentheses(self, S):

        # 第一个元素用于返回总得分
        stack = [0]

        for c in S:
            # 深度+1, 新的深度得分为0
            if c == '(':
                stack.append(0)
            else:
                # 深度减1
                v = stack.pop()
                # w是上一层深度的得分
                w = stack.pop()
                # 遇到的是‘()’，那么只将得分加一
                stack.append(w + max(2 * v, 1))

        return stack.pop()
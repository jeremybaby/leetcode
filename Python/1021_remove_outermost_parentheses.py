class Solution1_0:
    def removeOuterParentheses(self, S):

        res, stack = "", []
        lookup = {'(': ')', '[': ']', '{': '}'}

        start_idx = 1

        for i in range(len(S)):
            s = S[i]
            # 左括号push进去
            if s in lookup:
                stack.append(s)
            # 右括号匹配的话pop出去
            elif stack and s == lookup[stack[-1]]:
                stack.pop()

            # 如果此时栈空了，说明这是一个原语
            if not stack:
                res += S[start_idx: i]
                # 加2是因为需要排除第二个原语的开头
                start_idx = i + 2

        return res


class Solution1_1:
    """ 因为S只能是'('或')',所以做了一些优化  """
    def removeOuterParentheses(self, S):

        res, stack = "", []

        start_idx = 1

        for i in range(len(S)):
            s = S[i]
            if s == '(':
                stack.append(s)
            else:  # 只能是')'
                stack.pop()

            if not stack:
                res += S[start_idx: i]
                start_idx = i + 2

        return res

class Solution1_2:
    """ 不使用stack，使用计数变量 """
    def removeOuterParentheses(self, S):

        res, stack = "", []

        cnt = 0
        start_idx = 0

        for i in range(len(S)):
            cnt += 1 if S[i] == '(' else -1

            if not cnt:
                res += S[start_idx + 1: i]
                start_idx = i + 1

        return res

class Solution2:
    """ 维护一个计数变量cnt，左括号就加1，右括号就减1
        遇到'(', cnt不是0时就加入结果
        遇到')', cnt不是1时就加入结果
    """
    def removeOuterParentheses(self, S):

        ans = ""
        cnt = 0

        for s in S:
            if s == '(':
                if cnt != 0:
                    ans += '('
                cnt += 1
            else:
                if cnt != 1:
                    ans += ')'
                cnt -= 1

        return ans


class Solution3:
    """   分别对左右括号进行计数
    tips:
          - 最外面的左括号跳过，L初始为1
          - 左括号数 == 右括号数字时就是最外面的左括号
    """
    def removeOuterParentheses(self, S):

        L, R = 1, 0
        ans = ''

        i = 1
        while i < len(S):

            if S[i] == '(':
                L += 1
            else:
                R += 1

            if L != R:
                ans += S[i]
            else:
                L, R = 1, 0
                i += 1

            i += 1

        return ans



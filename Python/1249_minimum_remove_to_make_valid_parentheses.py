class Solution:
    def minRemoveToMakeValid(self, s):

        stack = []

        ans = []

        for symbol in s:
            if symbol == '(':
                stack.append(symbol)
                ans.append(symbol)
            elif symbol == ')':
                if stack and stack.pop() == '(':
                    ans.append(symbol)
            else:
                ans.append(symbol)

        if len(stack) != 0:
            stack = []
            for i in range(len(ans) - 1, -1, -1):
                if ans[i] == ')':
                    stack.append(ans[i])
                elif ans[i] == '(':
                    if not stack or stack.pop() != ')':
                        ans[i] = ""
        return "".join(ans)

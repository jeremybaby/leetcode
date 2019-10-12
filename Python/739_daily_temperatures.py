class Solution:

    def dailyTemperatures(self, T):

        stack = []
        ans = [0] * len(T)

        for i in range(len(T)):
            t = T[i]

            # stack[-1][1]为单调栈栈顶的温度
            while stack and stack[-1][1] < t:
                idx, val = stack.pop()
                ans[idx] = i - idx

            # 把索引和温度都存入栈中
            stack.append((i, t))

        return ans
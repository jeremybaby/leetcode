class Solution1:
    """超时，mmp"""
    def maxWidthRamp(self, A):

        max_len = 0
        length = len(A)

        for i in range(length):

            if max_len >= length - 1 - i:
                break

            j = i + 1
            while j < length:
                if A[j] >= A[i]:
                    max_len = max(max_len, j - i)
                j += 1

        return max_len


class Solution2:
    def maxWidthRamp(self, A):

        stack = []
        ans = 0

        for i, a in enumerate(A):
            # 当前元素小与栈顶元素，构造一个单调递减栈
            if not stack or a < stack[-1][1]:
                stack.append((i, a))
            else:
                # 从栈顶开始遍历
                idx = len(stack) - 1
                while idx >= 0 and a >= stack[idx][1]:
                    ans = max(ans, i - stack[idx][0])
                    idx -= 1

        return ans
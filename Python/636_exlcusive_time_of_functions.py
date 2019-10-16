class Solution:
    """
     思路：
     - 每一个log的start / end time设为prevTime，
     - 再拿到当前log的 start/end time，计算出时间差

    """
    def exclusiveTime(self, n, logs):

        stack = []
        ans = [0] * n
        prevTime = 0

        for log in logs:
            idx, type, time = log.split(':')
            if type == 'start':
                if stack:
                    ans[stack[-1]] += int(time) - prevTime
                stack.append(int(idx))
                prevTime = int(time)
            else:
                ans[stack[-1]] += int(time) - prevTime + 1
                stack.pop()
                prevTime = int(time) + 1

        return ans


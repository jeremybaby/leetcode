class Solution:
    def climbStairs(self, n):

        # fibonacci
        prev, current = 0, 1

        for i in range(n):
            prev, current = current, prev + current

        return current


class Solution2:
    """DP: 具有最优子结构 & 无后效性 特点
       - 状态dp[i]代表能到达第i阶的方法总数
       - 边界状态，dp[0] = 0, dp[1] = 1, dp[2] = 2
       - 状态转移方程: dp[i] = dp[i-1] + dp[i-2]
    """
    def climbStairs(self, n):

        if n == 1:
            return 1

        f = [0 for _ in range(n + 1)]

        f[1], f[2] = 1, 2

        for i in range(3, n + 1):
            f[i] = f[i - 1] + f[i - 2]

        return f[n]


class Solution3_1:
    """非记忆递归：超时"""
    def climbStairs(self, n):
        if n <= 2:
            return n

        return self.climbStairs(n - 1) + self.climbStairs(n - 2)


class Solution3_2:
    """记忆型递归"""
    def __init__(self):
        self.map = {1: 1, 2: 2}

    def climbStairs(self, n):
        if n not in self.map:
            self.map[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.map[n]
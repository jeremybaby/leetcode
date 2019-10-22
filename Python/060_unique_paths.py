class Solution1_1:
    """ Math: 组合C(m+n-2, m-1)
        从m+n-2总步数中选m-1步向右
    """
    def uniquePaths(self, m, n):
        def factorial(m):
            ans = 1
            while m:
                ans *= m
                m -= 1
            return ans

        return factorial(m + n - 2) // factorial(m - 1) // factorial(n - 1)

import math
class Solution1_2:
    """ 使用math.factorial, 最后用int()转"""
    def uniquePaths(self, m, n):
        res = math.factorial(m+n-2) / math.factorial(m-1) / math.factorial(n-1)
        return int()


class Solution2_1:
    def uniquePaths(self, m, n):

        # step1: 初始化dp (辣鸡写法)
        dp = []
        dp.append([1 for i in range(n)])
        for i in range(1, m):
            dp.append([0 if i else 1 for i in range(n)])

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m - 1][n - 1]


class Solution2_2:
    """上版辣鸡代码优化 O(mn)空间复杂度，O(mn)时间复杂度"""
    def uniquePaths(self, m, n):

        dp = [[1 * n] + [[1] + [0] * (n - 1) for _ in range(1, m)]]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]


class Solution3:
    """优化为O(2n)"""
    def uniquePaths(self, m, n):

        pre, cur = [1] * n, [1] * n

        for i in range(1, m):
            for j in range(1, n):
                cur[j] = pre[j] + cur[j - 1]
            pre = cur[:]

        return pre[-1]


class Solution4:
    """优化为O(n)"""
    def uniquePaths(self, m, n):

        cur = [1] * n

        for i in range(1, m):
            for j in range(1, n):
                cur[j] += cur[j - 1]

        return cur[-1]


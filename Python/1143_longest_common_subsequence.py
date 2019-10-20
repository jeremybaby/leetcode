class Solution1:
    """动态规划：循环写法"""
    def longestCommonSubsequence(self, text1, text2) -> int:

        if not text1 or not text2:
            return 0

        m, n = len(text1), len(text2)

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[m][n]


from functools import lru_cache

class Solution2:
    def longestCommonSubsequence(self, text1, text2):

        m, n = len(text1), len(text2)

        @lru_cache(None)
        def lcs(i, j):

            if i == 0 or j == 0:
                return 0

            if text1[i - 1] == text2[j - 1]:
                return lcs(i - 1, j - 1) + 1
            else:
                return max(lcs(i, j - 1), lcs(i - 1, j))

        return lcs(m, n)
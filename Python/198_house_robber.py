class Solution1:
    """dp方程"""
    def rob(self, nums):

        if not nums:
            return 0

        n = len(nums)

        dp = [0] * (n + 1)
        dp[1] = nums[0]

        for i in range(2, n + 1):
            dp[i] = max(dp[i - 2] + nums[i - 1], dp[i - 1])

        return dp[-1]


class Solution2:
    """   多么优雅的代码
          [2, 7, 9, 3, 1]
        - num: 2 last:  0  cur:  2
        - num: 7 last:  2  cur:  7
        - num: 9 last:  7  cur:  11
        - num: 3 last:  11  cur:  11
        - num: 1 last:  11  cur:  12
    """
    def rob(self, nums):
        last, cur = 0, 0

        for num in nums:
            last, cur = cur, max(last + num, cur)

        return cur
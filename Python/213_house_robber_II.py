class Solution:
    def rob(self, nums):

        def rob_helper(nums):
            cur, pre = 0, 0

            for num in nums:
                pre, cur = cur, max(pre + num, cur)

            return cur

        if len(nums) == 1:
            return nums[0]

        return max(rob_helper(nums[1:]), rob_helper(nums[:-1]))


class Solution2:
    """dp方程，思路同上"""
    def rob(self, nums):

        if not nums: return 0

        if len(nums) <= 2: return max(nums)

        def rob_helper(nums):

            if not nums: return 0

            n = len(nums)

            if n <= 2: return max(nums)

            dp = [0] * (n + 1)
            dp[1] = nums[0]

            for i in range(2, n + 1):
                dp[i] = max(dp[i - 2] + nums[i - 1], dp[i - 1])

            return dp[-1]

        return max(rob_helper(nums[1:]), rob_helper(nums[:-1]))
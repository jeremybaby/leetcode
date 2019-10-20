class Solution:
    def lengthOfLIS(self, nums):

        if not nums:
            return 0

        dp = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(i):

                if nums[j] < nums[i]:
                    # 如果只是dp[i] = dp[j] + 1，下表中的右下角就会被置为2
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)


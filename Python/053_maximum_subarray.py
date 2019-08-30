class Solution:
    def maxSubArray(self, nums):

        if max(sum) < 0:
            return max(sum)

        local_max, global_max = 0, 0
        for num in nums:
            local_max = max(0, local_max + num)
            global_max = max(local_max, global_max)

        return global_max

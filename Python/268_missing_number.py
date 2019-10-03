class Solution1:
    """Math
      高斯求和 - sum(nums)
    """
    def missingNumber(self, nums):
        length = len(nums)
        sum_gauss = length * (length + 1) // 2

        return sum_gauss - sum(nums)
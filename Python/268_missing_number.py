class Solution1:
    """Math
      高斯求和 - sum(nums)
    """
    def missingNumber(self, nums):
        length = len(nums)
        sum_gauss = length * (length + 1) // 2

        return sum_gauss - sum(nums)


class Solution2:
    """
        nums数组和0~len(nums)的所有数异或
    """
    def missingNumber(self, nums):
        last_ele = len(nums)

        # i从0 ～ n-1
        for i, val in enumerate(nums):
            last_ele ^= i ^ val

        return last_ele


class Solution3:
    """用集合存储"""
    def missingNumber(self, nums):

        sets = set(nums)

        for i in range(len(nums) + 1):
            if i not in sets:
                return i


class Solution4:
    """先排序，看index是否和value相同"""
    def missingNumber(self, nums):

        nums.sort()

        for i in range(len(nums)):
            if i != nums[i]:
                return i

        return i + 1
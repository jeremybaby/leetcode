class Solution1:
    """ defaultdict计数 """
    def majorityElement(self, nums):

        from collections import defaultdict
        lookup = defaultdict(int)

        half_len = len(nums) // 2

        for num in nums:
            lookup[num] += 1
            if lookup[num] > half_len:
                return num

class Solution2:
    """众数的出现次数 > Ln / 2」, 排序完后中间的数就是众数"""
    def majorityElement(self, nums):

        nums.sort()
        return nums[len(nums) // 2]


class Solution3:
    """
      我们维护一个计数器，
      - 如果遇到一个我们目前的候选众数，就将计数器加一，
      - 否则减一
      只要计数器等于0,我们就将nums中之前访问的数字全部忘记,
      并把下一个数字当做候选的众数
    """
    def majorityElement(self, nums):

        count = 0
        candidate = None

        for num in nums:

            if count == 0:
                candidate = num

            count += (1 if num == candidate else -1)

        return candidate
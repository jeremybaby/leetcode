class Solution1_1:
    """dict计数，返回计数为1的数字
    """
    def singleNumber(self, nums):

        ans, dict = [], {}

        for num in nums:
            if num not in dict:
                dict[num] = 1
            else:
                dict[num] += 1

        for num in dict:
            if dict[num] == 1:
                return num


class Solution1_2:
    """defaultdict初始化为0，进行计数，返回计数结果为1的数字"""
    def singleNumber(self, nums):

        from collections import defaultdict
        d = defaultdict(int)

        for num in nums:
            d[num] += 1

        for num in nums:
            if d[num] == 1:
                return num

class Solution1_3:
    """使用collections.Counter"""
    def singleNumber(self, nums):

        for k,v in collections.Counter(nums).items():
            if v == 1:
                return k

class Solution2:
    """
    Math:
      [3 * (a + b + c) - (a + a + a + b + b + b + c) ] / 2 = c
    """
    def singleNumber(self, nums):
        return (3 * sum(set(nums)) - sum(nums)) // 2

class Solution3:
    """
       先把数组排序，每次移动3位
       - 如果不等于下一个数字，就证明找到了
       - 如果已经到了最后一位，就证明找到了
    """
    def singleNumber(self, nums):

        nums.sort()

        i, length = 0, len(nums)

        while i < length:

            if i == length - 1 or nums[i] != nums[i+1]:
                return nums[i]

            i += 3


class Solution:
    """
        16位整数中-32768到32767（-2^15~2^15-1）,最高位为符号位

        32位整数中-2147483648到2147 483 647（-2^31~2^31-1）
    """
    def singleNumber(self, nums: List[int]) -> int:

        ans = 0
        for i in range(32):
            count = 0
            mask = 1 << i
            for num in nums:
                if num & mask:
                    count += 1
            if count % 3 == 1:
                ans |= mask

        #python的整型由于其没有最大值，
        # 所以，当输入是一堆负数的时候，会导致认为结果是个整数！
        # 因为32位有符号的被认为成了无符号的，所以这就是Python的一个坑
        # 如果不在这个范围内，说明了结果被认为是无符号的数了，需要减去2^32
        if ans >= 2 ** 31:
            ans -= 2 ** 32

        return ans
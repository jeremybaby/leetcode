class Solution1_1:
    """异或"""
    def singleNumber(self, nums):

        ans = 0
        # Step1: 异或所有数字
        for num in nums:
            ans ^= num

        # Step2: 找出结果右边第一位为1的掩码
        mask = 1
        while (mask & ans) == 0:
            mask <<= 1

        num1, num2 = 0, 0
        # Step3: 分成两个子数组
        for num in nums:
            if num & mask == 0:
                num1 ^= num
            else:
                # 此处是不等于0，不一定为1哦
                num2 ^= num

        return [num1, num2]


class Solution1_2:
    """异或"""
    def singleNumber(self, nums):

        ans = 0

        for num in nums:
            ans ^= num

        # bit代表从右数第bit位为1
        bit = 0
        while not (ans & 1):
            ans >>= 1
            bit += 1

        num1, num2 = 0, 0
        for num in nums:
            temp = num
            if (temp >> bit) & 1:
                num1 ^= num
            else:
                num2 ^= num

        return [num1, num2]


class Solution2_1:
    """
        所有元素出现次数用哈希表计数，返回出现一次的数字
        注意defaultdict的使用
    """
    def singleNumber(self, nums):

        from collections import defaultdict
        d = defaultdict(int)

        # 所有元素计数
        for num in nums:
            d[num] += 1

        ans = []
        for num in nums:
            if d[num] == 1:
                ans.append(num)

        return ans


class Solution2_2:
    """
        所有元素出现次数用哈希表计数，返回出现一次的数字
        不使用defaultdict
    """

    def singleNumber(self, nums):

        count_dict = {}
        for num in nums:
            if num in count_dict:
                count_dict[num] += 1
            else:
                count_dict[num] = 1

        ans = []
        for key, value in count_dict.items():
            if value == 1:
                ans.append(key)

        return ans


class Solution2_3:
    """
        遍历数组，在dict中设为1，不在pop()出去，返回dict.keys()
    """
    def singleNumber(self, nums):

        _dict = {}

        for num in nums:
            if num not in _dict:
                _dict[num] = 1
            else:
                # 也可以用 del _dic[num]
                _dict.pop(num)

        return _dict.keys()


class Solution2_4:
    """ 哈希表
        注意set()的使用
    """
    def singleNumber(self, nums):

        ans_set = set()

        for num in nums:
            if num in ans_set:
                ans_set.remove(num)
            else:
                ans_set.add(num)

        return list(ans_set)

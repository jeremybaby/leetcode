class Solution(object):
    """ 剑指 offer第15题
    思路：
    Step1: 先判断整数二进制表示中最右边一位是不是1;
        判断方法：数字和1(00000001)作&运算看结果是不是0
    Step2: 循环把输入的整数右移一位，判断是不是1，直到整个数变0
    """
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n:
            if n & 1:
                count += 1
            # 上面两行可以优化为 count += n & 1
            n = n >> 1
            # 可以用 n >>= 1
        return count

class Solution2(object):
    """ Follow up: 如果数字是负数呢？
    思路：
    - 我们把数字和1做&运算，判断最低位是不是1.
    - 接着把1(0001)左移一位得到2(0010)，
    - 再和n做与运算，能判断n的次低位是不是1......
    """
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        flag = 1
        # while flag: 这样会超时
        for i in range(32):
            if (n & flag):
                count += 1
            flag <<= 1
        return count

class Solution3(object):
    """
    思路：
        把一个整数减去1，再和原整数做与运算，会把该整数最右边的1变成0.
        以1100为例，减去1的结果是(1011)，
        我们再把1100和1011做位与运算，得到的结果是1000
        一个整数的二进制中有多少个1，就可以进行多少次这样的运算
    """
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0

        while n:
            n = n & (n - 1)
            count += 1

        return count
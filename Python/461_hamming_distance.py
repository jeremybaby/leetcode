class Solution1:
    """骚操作"""
    def hammingDistance(self, x, y):
        return bin(x ^ y).count('1')

class Solution2:
    """位运算"""
    def hammingDistance(self, x, y):

        count, mask = 0, 1
        ans = x ^ y

        for i in range(32):
            if (ans & mask):
                count += 1
            mask <<= 1

        return count

    class Solution3:
        """
        思路：
            把一个整数减去1，再和原整数做与运算，会把该整数最右边的1变成0.
            以1100为例，减去1的结果是(1011)，
            我们再把1100和1011做位与运算，得到的结果是1000
            一个整数的二进制中有多少个1，就可以进行多少次这样的运算
        """
        def hammingDistance(self, x, y):
            count = 0
            ans = x ^ y

            while ans:
                ans &= (ans - 1)
                count += 1

            return count

    class Solution4:
        """ 剑指 offer第15题变体，不推荐这种做法，幸好题目里都是正数
        思路：
        Step1: 先判断整数二进制表示中最右边一位是不是1;
            判断方法：数字和1(00000001)作&运算看结果是不是0
        Step2: 循环把输入的整数右移一位，判断是不是1，直到整个数变0
        """
        def hammingDistance(self, x, y):

            count = 0
            ans = x ^ y

            while ans:
                if ans & 1:
                    count += 1
                ans >>= 1

            return count
class Solution1:
    """
        因为n为正整数，所以最终看 n ^ (n >> 1) == 最大的数
        假设为数字10(1010)，右移为5(0101)，10 ^ 5 = 1111 = 2 ^ 4 - 1
    """
    def hasAlternatingBits(self, n):
        if n == 1:
            return True

        count, num = 0, n
        next = n >> 1

        # 统计n有多少个1
        while num:
            num &= num - 1
            count += 1

        # 偶数的话，最终为2*count,奇数为2*count+1
        # 1010，最终2^4-1  101(5) 最终为 2*2-1 = 3,即2^3-1
        bits = count * 2 if n % 2 == 0 else count * 2 - 1
        max = 2 ** bits - 1

        return n ^ next == max

class Solution2:
    """左移： n ^ (n << 1) = 11...11 """
    def hasAlternatingBits(self, n):

        count, MASK = 0, 1

        for i in range(32):
            if n & MASK:
                count += 1
            MASK <<= 1

        bits = count * 2 if n % 2 else count * 2 + 1
        max = 2 ** bits - 1

        temp = n << 1

        # 左移的话考虑个位为0的情况，再或一个1
        if n & 1 == 0:
            temp |= 1

        return temp ^ n == max

class Solution3:
    """骚操作"""
    def hasAlternatingBits(self, n):
        tmp = n ^ (n >> 1)
        return tmp & (tmp + 1) == 0

class Solution4:
    """
    把给定的数字转换成一个二进制数字串m检查两个相邻的数字是否相同。
    - 时间复杂度: O(1),
        对于任意输入，我们执行O(w)工作,其中w是n中的二进制位数且w ≤ 32
    - 空间复杂度: O(w)

    """
    def hasAlternatingBits(self, n):

        # 10的话为0b1010
        s = bin(n)[2:]

        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                return False

        return True

class Solution5:
    """骚操作"""
    def hasAlternatingBits(self, n):
        return '00' not in bin(n) and '11' not in bin(n)


class Solution6:
    """
        我们可以通过 n%2 和 n//2 操作获得最后一位和其余的位。
        如果最后一位等于剩余的最后一位，则答案是 False 的，
        反之, 答案是True.
    """

    def hasAlternatingBits(self, n):

        while n:
            last = n % 2
            n //= 2
            if n % 2 == last:
                return False
        return True

class Solution7(object):
    def hasAlternatingBits(self, n):

        while n > 2:
            # 如果数字的后两位是11，那么和3 and后结果为3
            # 如果后两位是00，那么取反得到11，然后和3 and运算得到3
            if (n & 3 == 3) or ((~n) & 3 == 3):
                return False
            n = n >> 1  # 移位
        return True

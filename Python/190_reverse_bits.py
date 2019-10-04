class Solution1:
    """
        遍历每一位，去和1进行与，
        - 如果是1，那么我们设在最高位上
    """
    def reverseBits(self, n):

        ans, MASK = 0, 1

        for i in range(32):
            if n & MASK:
                ans |= 1 << (31 - i)
            MASK <<= 1

        return ans

class Solution2:
    """二进制字符串填充0后反转，然后转为10进制"""
    def reverseBits(self, n):
        return int("0b" + bin(n)[2:].zfill(32)[::-1], 2)
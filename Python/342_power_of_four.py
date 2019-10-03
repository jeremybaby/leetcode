class Solution1:
    """骚操作：4的幂中1的位置总是在奇数位上。"""
    """0b1010101010101010101010101010101 的16进制表示为0x55555555"""
    def isPowerOfFour(self, num):
        return num > 0 and num & (num - 1) == 0 \
               and (num & 0x55555555) == num

class Solution2:
    """骚操作：我们们在确定其是2的次方数了之后，
    发现只要是4的次方数，减1之后可以被3整除。"""
    def isPowerOfFour(self, num):
        return num > 0 and num & (num - 1) == 0 \
               and (num - 1) % 3 == 0


class Solution3:
    """以终为始"""
    def isPowerOfFour(self, num):
        if num < 1:
            return False

        i = 1
        while i <= num:
            i *= 4

        return i == num


class Solution4:
    """循环除"""
    def isPowerOfFour(self, num):

        if num < 1:
            return False

        while num % 4 == 0:
            num //= 4

        return num == 1
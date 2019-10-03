class Solution1:
    """骚操作"""
    def isPowerOfTwo(self, n):
        if n < 0:
            return False
        return bin(n).count('1') == 1


class Solution2:
    """更骚的操作"""
    def isPowerOfTwo(self, n):
        return n > 0 and n & (n - 1) == 0


class Solution3:
    """左移mask与n相与"""
    def isPowerOfTwo(self, n):
        if n <= 0:
            return False

        count, mask = 0, 1

        # 这里用while mask一直会超时
        for i in range(32):
            # 添加一点优化
            if count > 1:
                return False
            if n & mask:
                count += 1
            mask <<= 1

        return count == 1


class Solution4:
    """右移数字与1相与"""
    def isPowerOfTwo(self, n):
        if n < 0:
            return False

        count = 0
        while n:
            if count > 1:
                return False
            if n & 1:
                count += 1
            n >>= 1

        return count == 1
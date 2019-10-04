class Solution:
    def getSum(self, a, b):
                
        MASK = 0x100000000 # 8个0，33位数字

        while b:
        	# 可以用 % MASK的方式，也可以用 & 0xffffffff的方式
            a, b = (a ^ b) % MASK, ((a & b) << 1) % MASK
        
        #也可以写 if a > 0x7FFFFFFF
        if a & 0x80000000 != 0: 
        # 2^31 ~ 2^32 之间应该表示为负数，第一位为符号位
            # 负数的补码 --> 原码：取反 + 1
            return -((~a + 1) & 0x7fffffff) 
            # 另一种方式: return -((~a + 1) % MASK)
            # 另一种方式：return  ~(a^0xFFFFFFFF) ？？？

        return a


class Solution:
    def addBinary(self, a, b):

        result, carry, val = "", 0, 0

        # Attention1：add from right to left
        # Attention2：add carry value
        for i in range(max(len(a), len(b))):
            # add last carry value
            val = carry
            if i < len(a):
                # int()
                val += int(a[-(i+1)])
            if i < len(b):
                val += int(b[-(i+1)])

            carry, val = val // 2, val % 2
            # str()
            result += str(val)
        if carry:
            result += '1'

        return result[::-1]

class Solution:
    def plusOne(self, digits):

        for i in reversed(range(len(digits))):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits

        # Solution 2：
        # return str(10 ** len(digits)

        digits[0] = 1
        digits.append(0)
        return digits


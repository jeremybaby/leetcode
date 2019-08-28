class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False

        num = 0
        a = x
        while (a):
            temp = a % 10
            num = num * 10 + temp
            a = a // 10

        if num == x:
            return True
        return False

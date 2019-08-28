class Solution:
    def reverse(self, x):

        # -214783648 ~ 214783647
        num = 0

        a = abs(x)

        while (a):
           temp =  a % 10
           num = num * 10 + temp
           a = int(a / 10)

        if x > 0 and num <= 2**31-1:
            return num
        elif x < 0 and num <= 2**31:
            return -num
        else:
            return 0
class Solution1:
    """ 牛顿迭代法
        求 sqrt(a)，即我们求 x^2 - a = 0的跟
        - 牛顿利用切线的方式逼近，每次在某点(随意选取)上做切线
        - 可得到迭代方程为 x(n+1) = x(n) - f(x(n)) / f'(x(n))
        - 对于本题，cur =  cur - (cur^2 - a) / (2cur)
        - 化简为  cur =  (cur + a / cur) / 2
    """

    def mySqrt(self, x):
        if x == 0:
            return 0

        # 起始的时候在这可以比较随意设置
        cur = x
        EPS = 1e-6

        while abs(cur - x / cur) > EPS:
            cur = (cur + x / cur) / 2.0

        return int(cur)


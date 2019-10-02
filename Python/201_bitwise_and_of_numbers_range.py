class Solution:
    """
    首先考虑如果区间是[k,k]那么返回值就是k。
    如果区间是[m,n]，即此时n > m，
    那么从m变化到n这些数字，bit的最低位最后的“与”的结果一定是0，
    因为从m变化到m＋1，
    - 如果m的最低位是0，那么此时变化到1，与之后这一位肯定还是0，
    - 如果m最低位是1，那么m＋1最后一位肯定是0.
    所以与的最终结果最低位肯定还是0.
    如果n > m，那么它们的最低位肯定是0，此时只需去计算n/2与m/2的结果
    """
    def rangeBitwiseAnd(self, m, n):
        count = 0

        while m != n:
            m = m >> 1
            n = n >> 1
            count += 1
        return (m << count)
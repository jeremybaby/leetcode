class Solution1_1:
    """ 自上而下的递归：超时
        - 超时原因：重复计算
    """
    def minimumTotal(self, triangle):

        n = len(triangle)

        def minSum(i, j):
            if i == n - 1:
                return triangle[i][j]

            x, y = minSum(i + 1, j), minSum(i + 1, j + 1)

            return min(x, y) + triangle[i][j]

        return minSum(0, 0)


class Solution1_2:
    """Solution1_1 的优化：
        初始化minSum为-1
        每次算出minSum的结果，就存储起来，避免重复进行计算！
    """
    def minimumTotal(self, triangle):

        n = len(triangle)

        minSum = [[-1] * i for i in range(1, n + 1)]

        def MinS(i, j):

            if minSum[i][j] != -1:
                return minSum[i][j]

            if i == n - 1:
                minSum[i][j] = triangle[i][j]
            else:
                x, y = MinS(i + 1, j), MinS(i + 1, j + 1)
                minSum[i][j] = min(x, y) + triangle[i][j]

            return minSum[i][j]

        return MinS(0, 0)


class Solution2:
    """自底向上的动规：O(n^2)的空间"""
    def minimumTotal(self, triangle):

        n = len(triangle)

        minSum = [[0] * i for i in range(1, n)]
        minSum.append(triangle[-1])

        for i in range(n - 2, -1, -1):
            for j in range(i + 1):
                minValue = min(minSum[i + 1][j], minSum[i + 1][j + 1])
                minSum[i][j] =  minValue + triangle[i][j]

        return minSum[0][0]

class Solution3:
    """动态规划自己直接写出了最优解
       自底向上
        [
             [2],
            [3,4],
           [6,5,7],
          [4,1,8,3]
        ]

        [11]
        [9, 10]
        [7, 6, 10]
        [4, 1, 8, 3]

    """
    def minimumTotal(self, triangle):

        ans = triangle[-1]

        for col in range(len(triangle) - 2, -1, -1):

            for i in range(col + 1):
                ans[i] = triangle[col][i] + min(ans[i], ans[i + 1])

        return ans[0]


class Solution4:
    """ans辅助空间都可以不要,直接使用triangle的最后一行"""
    def minimumTotal(self, triangle):

        n = len(triangle)

        for i in range(n - 2, -1, -1):
            for j in range(i + 1):
                minValue = min(triangle[n-1][j], triangle[n-1][j+1])
                triangle[n - 1][j] = minValue + triangle[i][j]

        return triangle[-1][0]
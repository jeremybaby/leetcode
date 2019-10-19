class Solution:
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


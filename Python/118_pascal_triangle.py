class Solution1_1:

    """
       i与j的下标从1开始，第i行有i个元素，先全部置为1
       然后修改不是两边上的元素，[i, j]为上一行[i-1,j-1]与[i-1, j]的元素和
       注意，尤其要注意下标！！！

    # [
    #      [1],       i = 0, j = 0
    #     [1,1],      i = 1, j = 0，1
    #    [1,2,1],     i = 2, j = 0, 1, 2      row[1] = a[1][0] + a[1][1]
    #   [1,3,3,1],    i = 3, j = 0, 1, 2, 3   row[1] = a[2][0] + a[2][1], row[2] = a[2][1] + a[2][2]
    #  [1,4,6,4,1]
    # ]
    """
    def generate(self, numRows):

        res = []

        for i in range(numRows):
            row = []

            for j in range(i + 1):

                row.append(1)

                # 非边上元素才进行修改
                if j > 0 and j < i:
                    row[j] = res[i - 1][j - 1] + res[i - 1][j]

            res.append(row)

        return res

class Solution1_2:

   def generate(self, numRows):

        res = []

        for i in range(numRows):
            row = []

            for j in range(i + 1):

                if j in (0, i):
                    row.append(1)
                else:
                    row.append(res[i - 1][j - 1] + res[i - 1][j])

            res.append(row)

        return res
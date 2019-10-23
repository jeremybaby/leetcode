class Solution:
    def minCost(self, costs):

        if not costs:
            return 0

        n = len(costs)

        for i in range(1, n):
            costs[i][0] += min(costs[i - 1][1], costs[i - 1][2])
            costs[i][1] += min(costs[i - 1][0], costs[i - 1][2])
            costs[i][2] += min(costs[i - 1][0], costs[i - 1][1])

        return min(costs[-1])


class Solution2:
    def minCost(self, costs):

        if not costs:
            return 0

        n = len(costs)

        for i in range(1, n):
            for j in range(3):
                # 每次add 除j外的颜色
                costs[i][j] += min(costs[i - 1][:j] + costs[i - 1][j + 1:])

        return min(costs[-1])
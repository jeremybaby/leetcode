class Solution1:
    """ min(奇数位置个数， 偶数位置个数)"""
    def minCostToMoveChips(self, chips):

        odd_count, even_count = 0, 0

        for chip in chips:
            # 注意：判断奇数的另法: if chip & 1 == 1:
            if chip % 2 == 1:
                odd_count += 1
            else:
                even_count += 1

        # even_count也可以用总长度去减odd_count

        return min(odd_count, even_count)


class Solution1_2:
    """优雅的解法"""
    def minCostToMoveChips(self, chips):

        #  也可以用Counter:
        #  odds = collections.Counter([c % 2 for c in chips])
        #  也可以用len计数
        #  odds = len([i for i in chips if i % 2 == 1])
        odds = sum(i % 2 for i in chips)

        return min(odds, len(chips) - odds)

class Solution1_2:
    """优雅的写法2"""
    def minCostToMoveChips(self, chips):
        res = [0, 0]
        for c in chips:
            res[c % 2] += 1
        return min(res)
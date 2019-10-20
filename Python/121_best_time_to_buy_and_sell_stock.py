class Solution0:
    """暴力解法：超时"""
    def maxProfit(self, prices):

        maxProfit = 0

        for i in range(len(prices) - 1):
            for j in range(i + 1, len(prices)):
                profit = prices[j] - prices[i]

                if profit > maxProfit:
                    maxProfit = profit

        return maxProfit


class Solution1:
    """一次遍历：记录min_price与max_profit"""
    def maxProfit(self, prices):

        min_price, max_profit = float('inf'), 0

        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price

        return max_profit
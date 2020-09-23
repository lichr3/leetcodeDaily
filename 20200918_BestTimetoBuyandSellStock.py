import sys

class Solution:
    def maxProfit(self, prices) -> int:
        if len(prices) <= 1:
            return 0
        curr_buy = prices[0]        # curr_buy：当前买入价格; curr_sell：当前卖出价格
        curr_sell = prices[0]       # 先把买入和卖出设为同一天，然后根据情况进行更新
        curr_profit = 0             # curr_profit:当前收入
        for i in range(1, len(prices)):
            if prices[i] > curr_sell:   # 若当天股票价格高于curr_sell，则更新curr_sell和条件更新curr_profit
                curr_sell = prices[i]
                curr_profit = max(curr_sell - curr_buy, curr_profit)
            elif prices[i] < curr_buy:  # 若当天股票价格低于curr_buy，则同时更新curr_buy和curr_sell
                curr_buy = prices[i]
                curr_sell = prices[i]
        return curr_profit

    # 参考答案：记录
    def maxProfit2(self, prices) -> int:
        minprice = sys.maxsize
        maxprofit = 0
        for price in prices:
            if price < minprice:
                minprice = price
            if price - minprice > maxprofit:
                maxprofit = price - minprice
        return maxprofit

test = Solution()
stock = eval(input("Please input the infomation of stocks:\n"))
print("maximum profit is ", test.maxProfit2(stock))





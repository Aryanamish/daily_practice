class Solution:
    def maxProfit(self, prices):
        buy,sell,profit=prices[0],prices[0],0
        for i in prices:
            if i < buy:
                buy = i
                sell = i
            elif i > sell and profit < i - buy:
                sell = i
                profit = sell - buy
        return profit


if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit([2,4,1]))
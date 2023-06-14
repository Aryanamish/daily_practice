class Solution:
    MOD = 1000000007
    def profitableSchemes(self, n: int, minProfit, group, profit):
        self.profit = profit
        self.min_profit = minProfit
        self.group = group
        self.ans = 0
        self.total_profit(n, 0, 0)
        return self.ans

    def total_profit(self, n, curr_profit, index):
        if n < 0:
            return
        profit = self.profit
        min_profit = self.min_profit
        group = self.group
        if index >= len(profit):
            if curr_profit > min_profit:
                print(f"{n=}, {curr_profit=}, {index=}")
                self.ans = (self.ans + 1) % self.MOD
            return
        self.total_profit(n, curr_profit, index+1)
        self.total_profit(n - group[index], curr_profit + profit[index], index+1)

if __name__ == '__main__':
    s = Solution()
    print(s.profitableSchemes(5, 3, [2,2], [2,3]))
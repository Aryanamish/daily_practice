

class Solution:

    def coin_change_rec(self, coins, index, target):
        if index == 0:
            if target % coins[index] == 0:
                return target // coins[index]
            return 1e9
        not_take = self.coin_change_rec(
            coins, index=index - 1, target=target) + 0
        take = 1e9
        if target - coins[index] >= 0:
            take = self.coin_change_rec(
                coins, index=index, target=target - coins[index]) + 1

        return min(take, not_take)

    def coin_change(self, coins, target):
        dp = [[0 for _ in range(target+1)] for _ in range(len(coins))]
        n = len(coins)
        for i in range(0, target+1):
            if i % coins[0] == 0:
                dp[0][i] = i // coins[0]
            else:
                dp[0][i] = float('inf')

        for c in range(1, len(coins)):
            for t in range(target+1):
                not_take = dp[c-1][t] + 0
                take = float('inf')
                if t - coins[c] >= 0:
                    take = dp[c][t - coins[c]] + 1
                dp[c][t] = min(take, not_take)
        return dp[n-1][target]


if __name__ == '__main__':
    s = Solution()
    n, target = list(map(int, input().split()))
    coins = list(map(int, input().split()))
    ans = s.coin_change(coins, target=target)
    if ans == float('inf'):
        print('-1')
    else:
        print(ans)

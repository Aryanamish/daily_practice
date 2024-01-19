class Solution:
    def coin_change_rec(self, coins, index, target):
        if index == 0:
            if target % coins[index] == 0:
                return 1
            return -1e9

        not_take = self.coin_change_rec(coins, index-1, target)
        take = -1e9
        if target < coins[index]:
            take = self.coin_change_rec(
                coins, index, target - coins[index]) + 1

        return max(take, not_take)


if __name__ == '__main__':
    s = Solution()
    n, target = list(map(int, input().split()))
    coins = list(map(int, input().split()))

    print(s.coin_change_rec(coins, n-1, target))

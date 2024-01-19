import sys

input = sys.stdin.readline


def print(x, end='\n'):
    return sys.stdout.write(str(x) + end)


class Solution:
    MOD = (10**9) + 7
    MEMO = {}

    def rec(self, target):
        if target == 0 or target == 1:
            return 1
        if target < 0:
            return 0
        if target in self.MEMO:
            return self.MEMO[target]

        ans = 0
        for i in range(1, 7):
            ans = (ans + self.rec(target=target - i)) % self.MOD
        self.MEMO[target] = ans
        return ans

    def dice_combination(self, target):
        return self.for_loop(target)

    def for_loop(self, target):
        dp = [0] * (target + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, target + 1):
            for j in [1, 2, 3, 4, 5, 6]:
                if i - j < 0:
                    break
                dp[i] = (dp[i] + dp[i-j]) % self.MOD
        return dp[target] % self.MOD


if __name__ == '__main__':

    n = int(input())
    s = Solution()

    print(s.dice_combination(target=n))

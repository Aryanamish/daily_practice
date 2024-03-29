class Solution:

    def __init__(self):
        pass

    def count_bst(self, n):
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                dp[i] += dp[i - j] * dp[j - 1]
        return dp[n]


s = Solution()
print(s.count_bst(5))
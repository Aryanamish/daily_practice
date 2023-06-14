#{
# Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3


class Solution:

    def count(self, coins, N, Sum):
        dp = [[-1 for _ in range(Sum + 1)] for _ in range(N + 1)]

        for i in range(N + 1):
            dp[i][0] = 1

        for i in range(1, Sum + 1):
            dp[0][i] = 0

        for i in range(1, N + 1):
            for j in range(1, Sum + 1):
                dp[i][j] = dp[i - 1][j]
                if coins[i - 1] <= j:
                    dp[i][j] += dp[i][j - coins[i - 1]]
        print(dp)
        return dp[-1][-1]

    def rec(self, coins, pointer, s):
        if s == 0:
            return 1
        if s < 0:
            return 0
        if pointer >= len(coins):
            return 0

        return self.rec(coins, pointer, s - coins[pointer]) + self.rec(
            coins, pointer + 1, s)


#{
# Driver Code Starts.


def main():
    s = Solution()
    print(s.count([1, 2, 3], 3, 4))


if __name__ == "__main__":
    main()

# } Driver Code Ends
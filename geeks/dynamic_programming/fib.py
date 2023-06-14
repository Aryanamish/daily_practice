#{
# Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3


class Solution:
    #Function to find the nth fibonacci number using top-down approach.
    def findNthFibonacci(self, number, dp):
        for i in range(2, number + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[number]


#{
# Driver Code Starts.


def main():
    dp = [0] * 100
    dp[0] = 0
    dp[1] = 1
    dp[2] = 1
    testcases = int(input())
    while (testcases > 0):
        number = int(input())

        print(Solution().findNthFibonacci(number, dp))
        testcases -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends
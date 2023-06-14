#User function Template for python3
import sys

sys.setrecursionlimit(1325)


class Solution:

    def min_jump(self, arr, n):
        dp = self.dp
        dp[0] = 0
        for i in range(1, n):
            for j in range(0, i):
                if arr[j] + j >= i:
                    if dp[j] != float('inf'):
                        dp[i] = min(dp[i], dp[j] + 1)
        return dp[n - 1]

    def minJumps(self, arr, n):
        self.dp = [float('inf')] * (n + 1)
        res = self.min_jump(arr, n)
        return -1 if res == float('inf') else res


#{
# Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    # with open('G:\\daily_practice\\geeks\\dynamic_programming\\txt.txt') as f:
    #     Arr = list(map(int, f.read().split()))
    #     n = Arr[0]
    #     Arr = Arr[1:]
    #     ob = Solution()
    #     ans = ob.minJumps(Arr, n)
    #     print(ans)

    T = int(input())
    for i in range(T):
        n = int(input())
        Arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.minJumps(Arr, n)
        print(ans)
# } Driver Code Ends
#User function template for Python


class Solution:
    #Function to find the days of buying and selling stock for max profit.

    def stockBuySell(self, A, n):
        print(self.rec(A, 0, -1, 0))
        return []

    def rec(self, price, n, bought, profit):
        if n >= len(price):
            return 0
        if n - 1 == len(price) and bought != -1:
            return price[n] - bought
        ans = 0
        if bought == -1:
            ans = self.rec(price, n + 1, price[n], profit)
        ans = max(ans, self.rec(price, n + 1, bought, profit))
        profit += ans
        return profit


#{
# Driver Code Starts
#Initial template for Python


def check(ans, A, p):
    c = 0
    for i in range(len(ans)):
        c += A[ans[i][1]] - A[ans[i][0]]
    if (c == p):
        return 1
    else:
        return 0


if __name__ == '__main__':
    t = 1
    while (t > 0):
        n = 7
        A = [100, 180, 260, 310, 40, 535, 695]
        ob = Solution()
        ans = ob.stockBuySell(A, n)
        p = 0
        for i in range(n - 1):
            p += max(0, A[i + 1] - A[i])
        if (len(ans) == 0):
            print("No Profit", end="")
        else:
            print(check(ans, A, p), end="")
        print()
        t -= 1
# } Driver Code Ends
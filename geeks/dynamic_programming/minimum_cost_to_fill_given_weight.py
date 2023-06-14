#User function Template for python3


class Solution:
    choice = []

    def minimumCost(self, cost, n, W):
        self.memo = [[-1 for i in range(n + 1)] for i in range(W + 1)]
        return self.rec(cost, 0, n, w, 0)

    def rec(self, cost, pointer, N, W, current_cost):

        if pointer >= N:
            return float('inf')
        if W == 0:
            return current_cost
        if W < 0:
            return float('inf')

        if self.memo[W][N] != -1:
            return self.memo[W][N]
        self.choice.append(cost[pointer])
        ans1 = self.rec(cost, pointer, N, W - (pointer + 1),
                        current_cost + cost[pointer])
        self.choice.pop()
        ans2 = self.rec(cost, pointer + 1, N, W, current_cost)
        self.memo[W][N] = min(ans1, ans2)
        return self.memo[W][N]


#{
# Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = 1
    for i in range(T):
        n, w = 5, 5
        n, w = int(n), int(w)
        a = [int(x) for x in [20, 10, 4, 50, 100]]
        ob = Solution()
        ans = ob.minimumCost(a, n, w)
        print(ans)

# } Driver Code Ends
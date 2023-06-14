#User function Template for python3


class Solution:

    def optimalKeys(self, N):
        # code here
        self.count = 0
        ans = self.rec(N - 1, 1, 0, strokes='')
        print(self.count)
        return ans

    def rec(self, n, no_of_a, copy, strokes):

        if n <= 0:
            # if no_of_a == 432:
            # print(strokes, ": ", no_of_a)
            self.count += 1
            return no_of_a

        # if copy is True:
        # ans = no_of_a + (no_of_a * n)
        # print(strokes, " paste " * n, ": ", ans)
        # return ans
        ans = [0] * 3

        if n > 2:
            ans[1] = self.rec(n - 2, no_of_a, no_of_a,
                              strokes + " + copy")  # key2, key3
        if copy != 0:
            ans[2] = self.rec(n - 1, no_of_a + copy, copy,
                              strokes + " + paste")
        if copy == 0:
            ans[0] = self.rec(n - 1, no_of_a + 1, copy,
                              strokes + " + A")  # key1

        return max(ans)


#{
# Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())

        ob = Solution()
        print(ob.optimalKeys(N))
# } Driver Code Ends
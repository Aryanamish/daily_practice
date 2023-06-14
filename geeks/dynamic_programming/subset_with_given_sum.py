class Solution:

    def __init__(self):
        pass

    def dp(self, arr, n, s):
        dp = [[-1] * n] * s

    def subset(self, arr, n, s):
        if s == 0:
            return 1
        if n + 1 == 0 or s < 0:
            return 0
        return self.subset(arr, n - 1, s - arr[n]) + self.subset(arr, n - 1, s)


s = Solution()
s.s = 35
print(s.subset([10, 5, 2, 3, 6], 4, 8))

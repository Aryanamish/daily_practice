class Solution:

    def __init__(self):
        pass

    def dp_sol(self, arr, n):
        prev_prev = arr[0]
        prev = max(arr[0], arr[1])

        for i in range(2, n):
            prev_prev, prev = prev, max(prev, prev_prev + arr[i])
        return prev

    def max_non_consicutive_sum(self, arr, n):
        if n == 0:
            return arr[0]
        if n == 1:
            return max(arr[n - 1], arr[n])
        return max(
            self.max_non_consicutive_sum(arr, n - 2) + arr[n],
            self.max_non_consicutive_sum(arr, n - 1))


s = Solution()
print(s.max_non_consicutive_sum([10, 5, 15, 20, 2, 30], 5))
print(s.dp_sol([10, 5, 15, 20, 2, 30], 6))

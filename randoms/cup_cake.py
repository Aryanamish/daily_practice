from queue import PriorityQueue


class Solution:

    def find_prev(self, arr, i):
        for idx in range(i-1, -1, -1):
            if arr[idx] > 0:
                return arr[idx]
        return 1

    def find_next(self, arr, i):
        for idx in range(i+1, len(arr)):

            if arr[idx] > 0:
                return arr[idx]
        return 1

    def solve(self, arr):
        n = len(arr)
        pq = PriorityQueue()
        [pq.put((arr[i], i)) for i in range(n)]
        score = 0
        while pq.qsize() > 0:
            elm = pq.get()
            arr[elm[1]] = -1
            score += self.find_prev(arr, elm[1]) * self.find_next(arr, elm[1])
        return score

    def all_combination(self, arr, score, ans, order=1):

        for i in range(len(arr)):
            if arr[i] < 0:
                continue
            temp = arr[i]
            arr[i] = -1 * order
            new_score = self.find_prev(arr, i) * self.find_next(arr, i)
            temp_score = self.all_combination(
                arr, score + new_score, ans, order+1)
            # if temp_score >= ans[0]:
            #     print(f"{arr=} {temp_score=}")
            ans[0] = max(ans[0], temp_score)
            arr[i] = temp
        return score

    def all_combination_tabulation(self, arr):
        n = len(arr)
        dp = [0] * n

        for i in range(n):
            for j in range(i, n):
                if arr[j] < 0:
                    continue
                temp = arr[j]
                arr[j] = -1
                new_score = self.find_prev(arr, j) * self.find_next(arr, j)
                temp_score = new_score
                if j > 0:
                    temp_score += dp[j - 1]
                dp[j] = max(dp[j], temp_score)
                arr[j] = temp

        return dp[n - 1]

    # Helper functions find_prev and find_next are assumed to be defined elsewhere.


s = Solution()
print(s.solve([5, 1, 8, 3]))
ans = [0]
s.all_combination([10, 9, 8, 7, 6, 5, 4, 3], 0, ans)
print(ans[0])
print(s.all_combination_tabulation([10, 9, 8, 7, 6, 5, 4, 3]))


def all_combination(arr, score, ans, order=1):
    def find_prev(arr, i):
        for idx in range(i-1, -1, -1):
            if arr[idx] > 0:
                return arr[idx]
        return 1

    def find_next(arr, i):
        for idx in range(i+1, len(arr)):

            if arr[idx] > 0:
                return arr[idx]
        return 1
    for i in range(len(arr)):
        if arr[i] < 0:
            continue
        temp = arr[i]
        arr[i] = -1 * order
        new_score = find_prev(arr, i) * find_next(arr, i)
        temp_score = all_combination(arr, score + new_score, ans, order+1)
        # if temp_score >= ans[0]:
        #     print(f"{arr=} {temp_score=}")
        ans[0] = max(ans[0], temp_score)
        arr[i] = temp
    return score

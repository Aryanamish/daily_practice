#{
# Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

# } Driver Code Ends
#User function Template for python3


class Solution:

    #Function to return a list of indexes denoting the required
    #combinations whose sum is equal to given number.
    def get_tuple(self, count):
        ans = []
        for i in range(0, 20):
            for _ in range(count[i]):
                ans.append(i + 1)
        return tuple(ans)

    def combinationalSum(self, A, B):
        count = [0] * 20
        ans = set()
        order = []

        def solve(arr, s, ptr=0):
            if s == 0:
                t = self.get_tuple(count)
                if t not in ans:
                    ans.add(t)
                    order.append(t)
                return

            for i in range(ptr, len(arr)):
                if arr[i] <= s:
                    count[arr[i] - 1] += 1
                    solve(arr, s - arr[i], i)
                    count[arr[i]] -= 1

        A.sort()
        solve(A, B)
        return order


#{
# Driver Code Starts.

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        a = list(map(int, input().strip().split()))
        s = int(input())
        ob = Solution()
        result = ob.combinationalSum(a, s)
        if (not len(result)):
            print("Empty")
            continue
        for i in range(len(result)):
            print("(", end="")
            size = len(result[i])
            for j in range(size - 1):
                print(result[i][j], end=" ")
            if (size):
                print(result[i][size - 1], end=")")
            else:
                print(")", end="")
        print()

# } Driver Code Ends
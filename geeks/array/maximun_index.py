#User function Template for python3


class Solution:
    #Complete this function
    # Function to find the maximum index difference.
    def maxIndexDiff(self, arr, n):
        min_a = [[arr[0], 0]]
        for i in range(1, n):
            if arr[i] < min_a[-1][0]:
                min_a.append([arr[i], i])
            else:
                min_a.append([min_a[-1][0], min_a[-1][1]])

        max_a = [[arr[-1], n - 1] for _ in arr]

        i = n - 2
        j = n - 1
        while j >= 0 and i >= 0:
            minimum = min_a[i]
            if max_a[i][0] >= min_a[i][0]:
                i -= 1
            else:
                if max_a[i + 1][0] < min_a[i][0]:
                    j -= 1
                    max_a[i] = [arr[j], j]
                else:
                    max_a[i] = [arr[j], j]
                    i -= 1

        ans = 0
        for i in range(n):
            ans = max(max_a[i][1] - min_a[i][1], ans)
        return ans


#{
#  Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):

        n = int(input())

        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.maxIndexDiff(arr, n))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends
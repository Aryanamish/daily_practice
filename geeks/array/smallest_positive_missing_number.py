#User function Template for python3


class Solution:

    #Function to find the smallest positive number missing from the array.
    def missingNumber(self, arr, n):
        if n == 0:
            return 1
        i = 0
        while i < n:
            if 0 < arr[i] <= n:
                x = arr[i] - 1
                arr[i], arr[x] = arr[x], arr[i]
                if i == x:
                    i += 1
                continue
            arr[i] = -1
            i += 1

        for i in range(n):
            if arr[i] == -1:
                return i + 1
        return n + 1


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
        print(ob.missingNumber(arr, n))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends
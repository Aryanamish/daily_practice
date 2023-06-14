class Solution:
    #User function Template for python3

    ##Complete this function
    #Function to find index of element x in the array if it is present.
    def binary(self, arr, low, high, x):
        if low < high:

            def inrange(index):
                return 0 <= index < len(arr)

            mid = (low + high) // 2
            if arr[mid] == x:
                return mid

            elif inrange(mid + 1) and arr[mid + 1] == x:
                return mid + 1
            elif inrange(mid - 1) and arr[mid - 1] == x:
                return mid - 1

            if arr[mid] > x:
                return self.binary(arr, low, mid - 1, x)
            else:
                return self.binary(arr, mid + 1, high, x)
        return -1

    def closer(self, arr, n, x):
        return self.binary(arr, 0, n, x)


#{
# Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):
        N = int(input())
        A = list(map(int, input().split()))
        X = int(input())
        obj = Solution()
        res = obj.closer(A, N, X)
        print(res)
        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends
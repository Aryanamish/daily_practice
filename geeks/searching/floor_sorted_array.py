class Solution:
    #User function Template for python3

    #Complete this function
    def findFloor(self, arr, n, x):
        low = 0
        high = n - 1
        if n == 0:
            return -1
        if n == 1:
            if arr[0] < x:
                return 0
            else:
                return -1

        while low < high:
            mid = (low + high) // 2
            if arr[mid] == x:
                return mid
            if arr[mid] > x:
                high = mid - 1
            elif arr[mid] < x:
                low = mid + 1
        if arr[low] <= x:
            return low
        else:
            return low - 1


#{
# Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):

        NX = [int(x) for x in input().strip().split()]
        N = NX[0]
        X = NX[1]

        A = [int(x) for x in input().strip().split()]

        obj = Solution()
        print(obj.findFloor(A, N, X))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends

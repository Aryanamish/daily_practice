#User function Template for python3


class Solution:

    #Function to find the minimum element in sorted and rotated array.
    def minNumber(self, arr, low, high):
        m = arr[0]
        if arr[0] < arr[-1]:
            return arr[0]
        while low <= high:
            if low + 1 == high:
                return min(arr[low], arr[high])
            mid = (high + low) // 2
            if arr[mid] < arr[high]:
                high = mid
            elif arr[mid] > arr[low]:
                low = mid


#{
# Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):

        N = int(input())

        A = [int(x) for x in input().strip().split()]
        obj = Solution()
        print(obj.minNumber(A, 0, N - 1))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends
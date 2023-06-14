#User function Template for python3
class Solution:
    ##Complete this function
    #Function to rearrange  the array elements alternately.

    def store_two_number(self, arr, index, b, mx):
        arr[index] = (arr[index] % mx) + (b % mx) * mx

    def rearrange(self, arr, n):
        mx = arr[-1] + 100
        if n == 1:
            return

        i = 0
        j = n - 1
        idx = 0
        while i <= j:
            self.store_two_number(arr, idx, arr[j], mx)
            idx += 1
            if idx == n:
                break
            self.store_two_number(arr, idx, arr[i], mx)
            idx += 1
            i += 1
            j -= 1

        for i in range(n):
            arr[i] //= mx


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
        ob.rearrange(arr, n)

        for i in arr:
            print(i, end=" ")

        print()

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends
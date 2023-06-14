class Solution:
    #Function to count the frequency of all elements from 1 to N in the array.
    def frequencyCount(self, arr, n, p):
        mx = max(p + 1, 100)

        for i in range(n):
            x = (arr[i] % mx) - 1
            if x >= n:
                continue
            if arr[x] < mx:
                prev_num = 1
            else:
                prev_num = (arr[x] // mx) + 1
            arr[x] = (arr[x] % mx) + (prev_num % mx) * mx

        for i in range(n):
            arr[i] = arr[i] // mx


#{
# Driver Code Starts
#Initial Template for Python 3

import math
if __name__ == "__main__":
    T = int(input())
    while (T > 0):
        N = int(input())
        arr = [int(x) for x in input().strip().split()]
        P = int(input())
        ob = Solution()
        ob.frequencyCount(arr, N, P)
        for i in arr:
            print(i, end=" ")
        print()
        T -= 1

# } Driver Code Ends
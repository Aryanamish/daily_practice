#User function Template for python3


class Solution:
    #Complete this function
    #Function to find the maximum occurred integer in all ranges.
    def maxOccured(self, L, R, N, maxx):
        count = {i: 0 for i in range(maxx + 2)}
        for i in range(N):
            count[L[i]] += 1
            count[R[i] + 1] -= 1
        ans = 0
        ans_count = count[0]
        print(count)
        current_count = count[0]

        for key, val in count.items():
            current_count += val
            if current_count > ans_count:
                ans_count = current_count
                ans = key
        return ans


#{
#  Driver Code Starts
#Initial Template for Python 3

import math

A = [0] * 1000000


def main():

    T = int(input())

    while (T > 0):

        global A
        A = [0] * 1000000

        N = int(input())

        L = [int(x) for x in input().strip().split()]
        R = [int(x) for x in input().strip().split()]

        maxx = max(R)
        ob = Solution()
        print(ob.maxOccured(L, R, N, maxx))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends
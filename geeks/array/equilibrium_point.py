# User function Template for python3


class Solution:
    # Complete this function

    #Function to find equilibrium point in the array.
    def equilibriumPoint(self, arr, N):
        sum1, sum2 = 0, 0
        i = 0
        j = N - 1
        while i < j:
            if sum1 < sum2:
                sum1 += arr[i]
                i += 1
            else:
                sum2 += arr[j]
                j -= 1
            if sum1 == sum2:
                if i +  == j:
                    return i + 2

        return -1


#{
#  Driver Code Starts
# Initial Template for Python 3

import math


def main():

    T = int(input())

    while (T > 0):

        N = int(input())

        A = [int(x) for x in input().strip().split()]
        ob = Solution()

        print(ob.equilibriumPoint(A, N))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends
#User function Template for python3
class Solution:
    #Complete this function
    # Function for finding maximum AND value.
    def check_bit(self, arr, pattern):
        count = 0
        for i in arr:
            if pattern & i >= pattern:
                count += 1
                if count == 2:
                    return True

    def maxAND(self, arr, N):

        pattern = ''
        ans = 0

        for i in range(7, -1, -1):
            if self.check_bit(arr, int(pattern + '1' + '0' * i, 2)):
                pattern += '1'
            else:
                pattern += '0'
        return int(pattern, 2)


#{
#  Driver Code Starts
#Initial Template for Python 3

import math


def main():

    T = int(input())

    while (T > 0):

        n = int(input())

        arr = [int(x) for x in input().strip().split()]
        obj = Solution()
        print(obj.maxAND(arr, n))
        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends
#User function Template for python3


class Solution:

    #Function to find two repeated elements.
    def twoRepeated(self, arr, N):
        i = 0
        while i < len(arr):
            if arr[i] <= 0:
                i += 1
            else:
                target_index = arr[i] - 1
                if target_index == i:
                    arr[i] = -1
                else:
                    to_be_swapped_value = arr[target_index]
                    if to_be_swapped_value <= 0:
                        arr[i] = 0
                        arr[target_index] -= 1
                    else:
                        arr[i] = to_be_swapped_value
                        arr[target_index] = -1

        print(arr)
        return [1, 2]


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
        ans = obj.twoRepeated(A, N)
        print(ans[0], ans[1])

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends
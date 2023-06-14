#User function Template for python3


class Solution:
    ##Complete this function
    #Function to check if array is sorted and rotated.

    def reverse(self, arr, start, end):
        end -= 1
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    def is_sorted(self, arr, n):
        reverse = False if arr[0] < arr[1] else True

        for i in range(1, n):
            if reverse:
                if arr[i] > arr[i - 1]:
                    return False
            else:
                if arr[i] < arr[i - 1]:
                    return False
        return True

    def checkRotatedAndSorted(self, arr, n):
        first = arr[0]
        second = arr[1]

        if self.is_sorted(arr, n) is False:
            self.reverse(arr, n - 2, n)
            self.reverse(arr, 0, n - 2)
            arr.reverse()
            return True
        return False


#{
#  Driver Code Starts
import atexit

import atexit
import io
import sys

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        a = list(map(int, input().strip().split()))
        ob = Solution()
        if ob.checkRotatedAndSorted(a, n) or ob.checkRotatedAndSorted(
                a[::-1], n):
            print("Yes")
        else:
            print("No")

# } Driver Code Ends

{
    0: 0,
    1: 1, 
    2: 1, 
    3: 1, 
    4: -1, 
    5: 0, 
    6: -1, 
    7: 0, 
    8: 0, 
    9: 0, 
    10: -1
}
{
    0: 0 
    1: 1    
    2:
    3:
    4:
    5:
    6:
    7:
    8:
    9:
    10:

}
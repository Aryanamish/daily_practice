# your task is to complete this function
# function should return index to the any valid peak element
class Solution:

    def peakElement(self, arr, n):
        if n == 1:
            return 0
        if n == 2:
            if arr[0] > arr[1]:
                return 0
            else:
                return 1
        low = 0
        high = n - 1
        while low <= high:
            if low == high:
                return low
            mid = (high + low) // 2
            if mid == 0:
                if arr[mid] > arr[mid + 1]:
                    return mid
                else:
                    low = mid + 1

            elif arr[mid - 1] < arr[mid] > arr[mid + 1]:
                return mid
            elif arr[mid - 1] >= arr[mid]:
                high = mid - 1
            elif arr[mid + 1] >= arr[mid]:
                low = mid + 1
        return -1
        # return (low + high) // 2


#{
# Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        index = Solution().peakElement(arr.copy(), n)
        flag = False
        if index < 0 or index >= n:
            flag = False
        else:
            if index == 0 and n == 1:
                flag = True
            elif index == 0 and arr[index] >= arr[index + 1]:
                flag = True
            elif index == n - 1 and arr[index] >= arr[index - 1]:
                flag = True
            elif arr[index - 1] <= arr[index] and arr[index] >= arr[index + 1]:
                flag = True
            else:
                flag = False

        if flag:
            print(1)
        else:
            print(0)
# Contributed by: Harshit Sidhwa

# } Driver Code Ends
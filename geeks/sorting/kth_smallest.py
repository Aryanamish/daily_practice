#User function Template for python3
class Solution:
    #Function to find the kth smallest element in the array.
    def lamuto(self, arr, low, high):
        pivot = arr[high]
        i = low
        for j in range(low, high):
            if arr[j] <= pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[i], arr[high] = arr[high], arr[i]
        return i

    def kthSmallest(self, arr, n, k):
        ans = 0

        def recursion(arr, low, high, k):
            if low < high:
                result = self.lamuto(arr, low, high)
                if result == k - 1:
                    return arr[result]
                elif result < k:
                    recursion(arr, result + 1, high, k)
                else:
                    recursion(arr, low, result - 1, k)

        return recursion(arr, 0, n - 1, k) or arr[k - 1]


#{
# Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n, k = map(int, input().strip().split())
        a = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.kthSmallest(a, n, k))
# } Driver Code Ends
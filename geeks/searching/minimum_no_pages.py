class Solution:

    #Function to find minimum number of pages.
    def is_possible(self, arr, k, high):
        s = 0
        student = 1
        for i in range(len(arr)):
            if s + arr[i] <= high:
                s += arr[i]
            else:
                s = arr[i]
                student += 1
        return student <= k

    def findPages(self, arr, n, k):
        total_sum = sum(arr)
        mx = max(arr)

        low = mx
        high = total_sum
        ans = 0
        while low <= high:
            mid = (low + high) // 2
            if self.is_possible(arr, k, mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans


#{
# Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        n = int(input())

        arr = [int(x) for x in input().strip().split()]
        m = int(input())

        ob = Solution()

        print(ob.findPages(arr, n, m))
# } Driver Code Ends
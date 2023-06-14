#User function Template for python3
class Solution:

    #Function to find if there exists a triplet in the
    #array A[] which sums up to X.
    def twoSum(self, arr, low, high, s):
        i = low + 1
        j = high - 1
        curr_sum = arr[i] + arr[j]
        while i < j:
            if curr_sum == s:
                return True
            if curr_sum > s:
                curr_sum -= arr[j]
                j -= 1
                curr_sum += arr[j]
            else:
                curr_sum -= arr[i]
                i += 1
                curr_sum += arr[i]
        return False

    def find3Numbers(self, arr, n, X):
        arr.sort()
        for i in range(n - 2):
            if self.twoSum(arr, i, n, X - arr[i]) is True:
                return True
        return False


#{
# Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n, X = map(int, input().strip().split())
        A = list(map(int, input().strip().split()))
        ob = Solution()
        if (ob.find3Numbers(A, n, X)):
            print(1)
        else:
            print(0)
# } Driver Code Ends
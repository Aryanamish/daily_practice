class Solution:

    def minDist(self, arr, n, x, y):
        i = j = 0
        ans = float('infinity')
        while i < n and j < n:
            if arr[i] == x:
                if arr[j] == y:
                    ans = min(abs(j - i), ans)
                    i = j
                    j += 1
                else:
                    j += 1
            elif arr[i] == y:
                if arr[i] == x:
                    ans = min(abs(j - i), ans)
                    j = i
                    i += 1
                else:
                    i += 1
            else:
                i += 1
                j += 1
        return ans if ans < float('infinity') else -1


#{
# Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        x, y = list(map(int, input().strip().split()))
        print(Solution().minDist(arr, n, x, y))

# } Driver Code Ends
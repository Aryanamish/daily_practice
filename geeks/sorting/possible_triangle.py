#User function Template for python3


class Solution:

    def findotherTwo(self, arr, i, count):
        j = i + 1
        k = len(arr) - 1
        while j < k:
            if arr[i] + arr[j] > arr[k]:
                count += k - j
                j += 1
                k = len(arr) - 1
            else:
                k -= 1
                if j == i + 1 and k == j:
                    j += 1
                    k = len(arr) - 1
        return count

    def findNumberOfTriangles(self, arr, n):
        arr.sort()
        count = 0
        for i in range(n - 2):
            count = self.findotherTwo(arr, i, count)
        return count


#{
# Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.findNumberOfTriangles(arr, n))

# } Driver Code Ends
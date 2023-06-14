#User function Template for python3


class Solution:

    #Function to count the number of substrings that start and end with 1.
    def binarySubstring(self, n, s):
        ans = 0
        ones = 0
        for i in s:
            if i == '1':
                ans += ones
                ones += 1

        return ans


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        s = str(input())
        obj = Solution()
        print(obj.binarySubstring(n, s))
# } Driver Code Ends
#User function Template for python3


class Solution:

    #Function to find the largest number after k swaps.
    def find_max(self, s, k, num, i=0):
        if k == 0 or i >= len(s):
            return

        n = len(s)
        mx = s[i]

        for j in range(i + 1, n):
            if int(s[j]) > int(mx):
                mx = s[j]

        if (mx != s[i]):
            k = k - 1

        for j in range(i, n):
            if (s[j] == mx):
                s[i], s[j] = s[j], s[i]
                new_str = "".join(s)
                if int(new_str) > int(num[0]):
                    num[0] = new_str

                self.find_max(s, k, num, i + 1)

                s[i], s[j] = s[j], s[i]

    def findMaximumNum(self, s, k):
        num = [s]
        s = list(s)
        self.find_max(s, k, num)
        return num[0]


#{
# Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        k = int(input())
        s = input()
        ob = Solution()
        print(ob.findMaximumNum(s, k))

# } Driver Code Ends
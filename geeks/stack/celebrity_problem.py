#User function Template for python3


class Solution:

    #Function to find if there is a celebrity in the party or not.
    def celebrity(self, M, n):
        celeb = 0
        pointer = n - 1

        while celeb < pointer:
            if M[celeb][pointer] == 1:
                celeb += 1
            else:
                pointer -= 1

        for i in range(n):
            if M[celeb][i] == 1 or (M[i][celeb] == 0 and i != celeb):
                return -1

        return celeb


#{
# Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().strip().split()))
        k = 0
        m = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(a[k])
                k += 1
            m.append(row)
        ob = Solution()
        print(ob.celebrity(m, n))
# } Driver Code Ends
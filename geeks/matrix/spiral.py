#User function Template for python3


class Solution:

    #Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self, m, r, c):

        top_left = 0
        top_right = c - 1

        bottom_left = 0
        bottom_right = r - 1
        ans = []
        if c == 1:
            for i in range(r):
                ans.append(m[i][0])
        elif r == 1:
            for j in range(c):
                ans.append(m[0][j])
        else:
            while top_left <= bottom_right and top_right >= bottom_left:
                if top_left == bottom_right:
                    for j in range(bottom_left, top_right + 1):
                        ans.append(m[top_left][j])
                    top_left += 1
                    bottom_right -= 1
                elif top_right == bottom_left:
                    for i in range(top_left, bottom_right + 1):
                        ans.append(m[i][bottom_left])
                    top_right -= 1
                    bottom_left += 1
                else:
                    for j in range(top_left, top_right + 1):
                        ans.append(m[top_left][j])
                    top_left += 1

                    for i in range(top_left, bottom_right + 1):
                        ans.append(m[i][top_right])
                    top_right -= 1

                    for j in range(top_right, bottom_left - 1, -1):
                        ans.append(m[bottom_right][j])
                    bottom_right -= 1

                    for i in range(bottom_right, top_left - 1, -1):
                        ans.append(m[i][bottom_left])
                    bottom_left += 1
        return ans


# 06 06 02 28 02
# 12 26 30 28 07
# 22 25 03 04 23

#{
# Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        r, c = map(int, input().strip().split())
        values = list(map(int, input().strip().split()))
        k = 0
        matrix = []
        for i in range(r):
            row = []
            for j in range(c):
                row.append(values[k])
                k += 1
            matrix.append(row)
        obj = Solution()
        ans = obj.spirallyTraverse(matrix, r, c)
        for i in ans:
            print(i, end=" ")
        print()

# } Driver Code Ends
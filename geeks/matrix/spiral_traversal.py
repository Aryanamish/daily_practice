#User function Template for python3


class Solution:

    #Function to return a list of integers denoting spiral traversal of matrix.
    def spiral(self, matrix, r, c, x_axis, y_axis):
        ans = []
        j_start = x_axis
        j_end = c - x_axis - 1

        i_start = y_axis
        i_end = r - y_axis - 1
        i = i_start
        j = j_start
        while i_start <= i_end and j_start <= j_end:

            i = i_start
            j = j_start
            # 0,0
            inside = False
            while j < j_end:
                inside = True
                ans.append(matrix[i][j])
                j += 1
            # 0,5
            if inside is False:
                break
            inside = False
            while i < i_end:
                inside = True
                ans.append(matrix[i][j])
                i += 1
            if inside is False:
                break
            inside = False
            # 3,5

            while j > j_start:
                inside = True
                ans.append(matrix[i][j])
                j -= 1
            if inside is False:
                break
            inside = False
            # 3,0

            while i > i_start:
                inside = True
                ans.append(matrix[i][j])
                i -= 1
            if inside is False:
                break
            # 0,0

            x_axis += 1
            y_axis += 1
            j_start = x_axis
            j_end = c - x_axis - 1

            i_start = y_axis
            i_end = r - y_axis - 1
        ans.append(matrix[i][j])
        return ans

    def spirallyTraverse(self, matrix, r, c):
        ans = []
        return self.spiral(matrix, r, c, 0, 0)


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
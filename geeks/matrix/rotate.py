def print_matrix(matrix):
    for i in matrix:
        for j in i:
            print(j, end=" ")
        print()


class Rotate_matrix:

    def rotate_top_layer(self, m, pt_start, pt_end):

        #base case to exit the Loop
        if pt_start >= pt_end:
            return m

        # to rotate the Corner pieces
        a = pt_start
        b = pt_end
        m[a][a], m[b][a], m[b][b], m[a][b] = m[a][b], m[a][a], m[b][a], m[b][b]

        #for rotating top and bottom layer
        # for rotating m[0] elements
        for i in range(pt_start + 1, pt_end):
            m[i][pt_start], m[pt_start][i] = m[pt_start][i], m[i][pt_start]

        # for rotating m[-1] elements
        for i in range(pt_start + 1, pt_end + 1):
            m[i][pt_end], m[pt_end][i] = m[pt_end][i], m[i][pt_end]

        # for rotating the left and right layer
        # it is just replacing the top and bottom layer where the left and
        # right layer data is stored from the previous step
        for i in range(pt_start + 1, pt_end):
            m[pt_start][i], m[pt_end][i] = m[pt_end][i], m[pt_start][i]

        # Rotate the Inner layer recursively
        return self.rotate_top_layer(m, pt_start + 1, pt_end - 1)

    def rotate(self, matrix):
        self.rotate_top_layer(matrix, 0, len(matrix) - 1)


#User function Template for python3


class Solution:

    #Function to rotate matrix anticlockwise by 90 degrees.
    def rotate_corner(self, a, n, x):
        if x < n // 2:
            a[x][x], a[x][n - 1 - x], a[n - 1 - x][x], a[n - 1 - x][
                n - 1 - x] = a[x][n - 1 - x], a[n - 1 -
                                                x][n - 1 -
                                                   x], a[x][x], a[n - 1 - x][x]
            self.rotate_sides(a, n, x)

    def rotate_sides(self, a, n, x):
        for j in range(x + 1, n - x - 1):
            a[x][j], a[n - 1 - j][x] = a[n - 1 - j][x], a[x][j]

        for j in range(x + 1, n - x - 1):
            a[n - 1 - x][j], a[n - 1 - j][n - 1 - x] = a[n - 1 -
                                                         j][n - 1 -
                                                            x], a[n - 1 - x][j]

        for j in range(x + 1, n - x - 1):
            a[n - 1 - x][j], a[x][n - 1 - j] = a[x][n - 1 - j], a[n - 1 - x][j]

        self.rotate_corner(a, n, x + 1)

    def rotateby90(self, a, n):
        self.rotate_corner(a, n, 0)


# [
# [7, 14, 21, 28, 35, 42, 49],
# [6, 13, 20, 27, 34, 41, 48],
# [5, 12, 19, 26, 33, 40, 47],
# [4, 11, 18, 25, 32, 39, 46],
# [3, 10, 17, 24, 31, 38, 45],
# [2, 9, 16, 23, 30, 37, 44],
# [1, 8, 15, 22, 29, 36, 43]
# ]

# 01 02 03 04 05
# 06 07 08 09 10
# 11 12 13 14 15
# 16 17 18 19 20
# 21 22 23 24 25

# 01 16 11 06 05
# 04 07 08 09 24
# 03 12 13 14 23
# 02 17 18 19 22
# 21 20 15 10 25

#{
# Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        matrix = [[0 for j in range(n)] for i in range(n)]
        line1 = [int(x) for x in input().strip().split()]
        k = 0
        for i in range(n):
            for j in range(n):
                matrix[i][j] = line1[k]
                k += 1
        obj = Solution()
        obj.rotateby90(matrix, n)
        for i in range(n):
            for j in range(n):
                print(matrix[i][j], end=" ")
        print()

# } Driver Code Ends

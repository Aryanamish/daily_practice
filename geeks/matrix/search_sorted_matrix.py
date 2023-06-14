#User function Template for python3


class Solution:

    #Function to search a given number in row-column sorted matrix.
    def binary_search(self, arr, elem, start, end):
        if start > end:
            return False

        m = (start + end) // 2
        if arr[m] == elem:
            return True
        if elem > arr[m]:
            return self.binary_search(arr, elem, m + 1, end)
        else:
            return self.binary_search(arr, elem, start, m - 1)

    def binary_search_column(self, matrix, elem, start, end, j):
        if start > end:
            return False

        m = (start + end) // 2
        if matrix[m][j] == elem:
            return True
        if elem > matrix[m][j]:
            return self.binary_search_column(matrix, elem, m + 1, end, j)
        else:
            return self.binary_search_column(matrix, elem, start, m - 1, j)

    def search(self, matrix, n, m, x):

        pos = 0

        while pos < n and pos < m:
            if self.binary_search(matrix[pos], x, pos, m - 1) is True:
                return True
            elif self.binary_search_column(matrix, x, pos, n - 1, pos) is True:
                return True
            pos += 1

        return False


#{
# Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        size = input().strip().split()
        r = int(size[0])
        c = int(size[1])
        line = input().strip().split()
        matrix = [[0 for _ in range(c)] for _ in range(r)]
        for i in range(r):
            for j in range(c):
                matrix[i][j] = int(line[i * c + j])
        target = int(input())
        obj = Solution()
        if (obj.search(matrix, r, c, target)):
            print(1)
        else:
            print(0)

# } Driver Code Ends
from collections import deque


class Solution:

    #Function to find distance of nearest 1 in the grid for each cell.
    def nearest(self, grid):
        output = [[-1 for j in i] for i in grid]
        q = deque()
        # adding all the ones to the queue
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1 and output[i][j] == -1:
                    q.append((i, j, grid[i][j]))
                    output[i][j] = 0

        quardinates = ((1, 0), (-1, 0), (0, 1), (0, -1))
        m = len(grid)
        n = len(grid[0])

        while len(q) != 0:
            s = q.popleft()
            for quad in quardinates:
                x = s[0] + quad[0]
                y = s[1] + quad[1]

                if 0 <= x < m and 0 <= y < n and output[x][y] == -1:
                    q.append((x, y, s[0] + 1))
                    output[x][y] = s[2]
        print()
        return output


#{
# Driver Code Starts
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n, m = map(int, input().split())
        grid = []
        for _ in range(n):
            a = list(map(int, input().split()))
            grid.append(a)
        obj = Solution()
        ans = obj.nearest(grid)
        for i in ans:
            for j in i:
                print(j, end=" ")
            print()

# } Driver Code Ends